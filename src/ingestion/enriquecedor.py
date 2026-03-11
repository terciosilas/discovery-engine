"""Enriquecimento de papers com dados do Semantic Scholar.

Adiciona citation_count, influential_citation_count, tldr, fields_of_study
e s2_paper_id aos papers ja coletados do PubMed.
Progresso incremental via checkpoint para resiliencia a interrupcoes.
"""

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.core.audit import AuditLogger
from src.ingestion.semantic_scholar import SemanticScholarClient

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
CHECKPOINT_DIR = DATA_DIR / "checkpoints"


def carregar_papers(input_path: Path) -> list[dict[str, Any]]:
    """Carrega papers de um arquivo JSON.

    Args:
        input_path: Caminho do JSON (ex: papers_fase1_20260310_231443.json).

    Returns:
        Lista de dicts com dados dos papers.

    Raises:
        FileNotFoundError: Se o arquivo nao existe.
        ValueError: Se o formato e invalido.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"Formato invalido: esperava lista, recebeu {type(data).__name__}")

    if data and not isinstance(data[0], dict):
        raise ValueError(f"Formato invalido: itens devem ser dicts, recebeu {type(data[0]).__name__}")

    logger.info("Carregados %d papers de %s", len(data), input_path.name)
    return data


def carregar_checkpoint(checkpoint_path: Path) -> dict[str, dict[str, Any]]:
    """Carrega checkpoint de enriquecimento anterior.

    Args:
        checkpoint_path: Caminho do arquivo de checkpoint.

    Returns:
        Dict de DOI -> dados S2 ja enriquecidos.
    """
    if not checkpoint_path.exists():
        return {}

    try:
        with open(checkpoint_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        resultados = data.get("resultados", {})
        logger.info("Checkpoint carregado: %d papers ja processados", len(resultados))
        return resultados
    except (json.JSONDecodeError, KeyError) as e:
        logger.warning("Checkpoint corrompido (%s), recomeçando do zero", e)
        return {}


def salvar_checkpoint(
    checkpoint_path: Path,
    resultados: dict[str, dict[str, Any]],
    input_file: str,
    timestamp_inicio: str,
) -> None:
    """Salva checkpoint de enriquecimento incremental.

    Usa escrita atomica (temp + rename) para evitar corrupcao.

    Args:
        checkpoint_path: Caminho do arquivo de checkpoint.
        resultados: Dict de DOI -> dados S2.
        input_file: Nome do arquivo de input.
        timestamp_inicio: Quando o enriquecimento comecou.
    """
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)

    checkpoint_data = {
        "versao": 1,
        "timestamp_inicio": timestamp_inicio,
        "input_file": input_file,
        "total_processados": len(resultados),
        "resultados": resultados,
    }

    # Escrita atomica: temp -> rename
    temp_path = checkpoint_path.with_suffix(".tmp")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
    temp_path.replace(checkpoint_path)


def enriquecer_paper(paper: dict, s2_data: dict[str, Any]) -> dict:
    """Adiciona campos do Semantic Scholar a um paper.

    Cria uma COPIA do dict original (nunca modifica o original).

    Args:
        paper: Dict original do paper (PubMed).
        s2_data: Dados obtidos do S2 (do checkpoint).

    Returns:
        Novo dict com campos adicionais.
    """
    enriched = dict(paper)

    if s2_data.get("status") == "encontrado":
        enriched["s2_paper_id"] = s2_data.get("s2_paper_id", "")
        enriched["citation_count"] = s2_data.get("citation_count", 0)
        enriched["influential_citation_count"] = s2_data.get("influential_citation_count", 0)
        enriched["tldr"] = s2_data.get("tldr", "")
        enriched["fields_of_study"] = s2_data.get("fields_of_study", [])
        enriched["reference_count"] = s2_data.get("reference_count", 0)
        enriched["is_open_access_s2"] = s2_data.get("is_open_access", False)
        enriched["s2_enriquecido"] = True
        enriched["s2_timestamp"] = s2_data.get("timestamp", "")
    else:
        enriched["s2_enriquecido"] = False
        enriched["s2_status"] = "nao_encontrado"
        enriched["citation_count"] = 0
        enriched["influential_citation_count"] = 0
        enriched["tldr"] = ""
        enriched["fields_of_study"] = []

    return enriched


def enriquecer_papers_s2(
    input_path: Path,
    s2_api_key: str = "",
    checkpoint_interval: int = 10,
) -> dict[str, Any]:
    """Enriquece papers com dados do Semantic Scholar.

    Fluxo:
    1. Carrega papers do JSON
    2. Verifica/carrega checkpoint (retoma de onde parou)
    3. Para cada paper com DOI nao processado: chama S2 API
    4. Salva checkpoint incrementalmente
    5. Mescla dados S2 nos papers
    6. Salva arquivo enriquecido
    7. Gera audit log

    Args:
        input_path: Caminho do JSON de papers.
        s2_api_key: API key do S2 (opcional, aumenta rate limit).
        checkpoint_interval: Salvar checkpoint a cada N papers.

    Returns:
        Dict com estatisticas da execucao.
    """
    audit = AuditLogger(modulo="enriquecimento_s2")
    audit.registrar_input(input_path)
    inicio = time.time()
    timestamp_inicio = datetime.now(timezone.utc).isoformat()

    # 1. Carregar papers
    papers = carregar_papers(input_path)
    total = len(papers)

    if total == 0:
        logger.warning("Nenhum paper para enriquecer")
        audit.registrar_anomalia("Arquivo de input vazio")
        audit.registrar_contagens(lidos=0, validos=0, processados=0, rejeitados=0)
        audit.finalizar(status="SUCESSO_COM_ALERTAS")
        return {"total": 0, "mensagem": "Arquivo vazio"}

    # 2. Checkpoint
    checkpoint_path = CHECKPOINT_DIR / f"ckpt_enrich_{input_path.stem}.json"
    resultados = carregar_checkpoint(checkpoint_path)
    ja_processados = len(resultados)

    if ja_processados > 0:
        logger.info("Retomando de checkpoint: %d/%d papers ja processados", ja_processados, total)

    # 3. Loop de enriquecimento
    client = SemanticScholarClient(api_key=s2_api_key)
    encontrados = sum(1 for r in resultados.values() if r.get("status") == "encontrado")
    nao_encontrados = sum(1 for r in resultados.values() if r.get("status") == "nao_encontrado")
    erros = 0
    processados_nesta_sessao = 0

    papers_pendentes = [p for p in papers if p.get("doi", "").lower() not in resultados]
    logger.info(
        "Enriquecimento: %d pendentes, %d ja no checkpoint (de %d total)",
        len(papers_pendentes), ja_processados, total,
    )

    for i, paper in enumerate(papers_pendentes, 1):
        doi = paper.get("doi", "").lower()
        if not doi:
            continue

        # Tentar por DOI
        s2_paper = client.get_paper_by_doi(doi)

        # Fallback por PMID se DOI falhou e PMID existe
        if s2_paper is None and paper.get("pmid"):
            s2_paper = client.get_paper(f"PMID:{paper['pmid']}")

        now_iso = datetime.now(timezone.utc).isoformat()

        if s2_paper is not None:
            resultados[doi] = {
                "status": "encontrado",
                "s2_paper_id": s2_paper.paper_id,
                "citation_count": s2_paper.citation_count,
                "influential_citation_count": s2_paper.influential_citation_count,
                "tldr": s2_paper.tldr,
                "fields_of_study": s2_paper.fields_of_study,
                "reference_count": s2_paper.reference_count,
                "is_open_access": s2_paper.is_open_access,
                "timestamp": now_iso,
            }
            encontrados += 1
        else:
            resultados[doi] = {
                "status": "nao_encontrado",
                "timestamp": now_iso,
            }
            nao_encontrados += 1

        processados_nesta_sessao += 1

        # Progresso a cada 20 papers
        if processados_nesta_sessao % 20 == 0:
            logger.info(
                "Enriquecimento: %d/%d processados nesta sessao "
                "(%d encontrados, %d nao encontrados, total %d/%d)",
                processados_nesta_sessao, len(papers_pendentes),
                encontrados, nao_encontrados,
                len(resultados), total,
            )

        # Checkpoint incremental
        if processados_nesta_sessao % checkpoint_interval == 0:
            salvar_checkpoint(checkpoint_path, resultados, input_path.name, timestamp_inicio)

    # Checkpoint final
    salvar_checkpoint(checkpoint_path, resultados, input_path.name, timestamp_inicio)
    logger.info(
        "Enriquecimento concluido: %d encontrados, %d nao encontrados de %d total",
        encontrados, nao_encontrados, total,
    )

    # 4. Merge
    papers_enriquecidos = []
    for paper in papers:
        doi = paper.get("doi", "").lower()
        s2_data = resultados.get(doi, {"status": "nao_encontrado"})
        papers_enriquecidos.append(enriquecer_paper(paper, s2_data))

    # 5. Salvar output
    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = processed_dir / f"papers_enriched_fase1_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers_enriquecidos, f, ensure_ascii=False, indent=2)

    audit.registrar_output(output_path)

    # 6. Estatisticas
    duracao = time.time() - inicio
    citacoes = [p["citation_count"] for p in papers_enriquecidos if p.get("s2_enriquecido")]
    media_citacoes = sum(citacoes) / len(citacoes) if citacoes else 0

    # Top 10 mais citados
    top_10 = sorted(
        [p for p in papers_enriquecidos if p.get("s2_enriquecido")],
        key=lambda x: x["citation_count"],
        reverse=True,
    )[:10]
    top_10_resumo = [
        {"doi": p["doi"], "titulo": p["titulo"][:80], "citation_count": p["citation_count"]}
        for p in top_10
    ]

    estatisticas = {
        "duracao_segundos": round(duracao, 1),
        "total_papers": total,
        "encontrados_s2": encontrados,
        "nao_encontrados_s2": nao_encontrados,
        "taxa_cobertura_s2": round(encontrados / total * 100, 1) if total else 0,
        "total_citacoes": sum(citacoes),
        "media_citacoes": round(media_citacoes, 1),
        "mediana_citacoes": sorted(citacoes)[len(citacoes) // 2] if citacoes else 0,
        "top_10_mais_citados": top_10_resumo,
        "arquivo_output": output_path.name,
        "processados_nesta_sessao": processados_nesta_sessao,
    }

    # Anomalias
    taxa_nao_encontrados = nao_encontrados / total * 100 if total else 0
    if taxa_nao_encontrados > 30:
        audit.registrar_anomalia(
            f"Taxa alta de papers nao encontrados no S2: {taxa_nao_encontrados:.1f}% "
            f"({nao_encontrados}/{total}). Investigar manualmente."
        )

    # DOIs nao encontrados para reprocessamento
    dois_nao_encontrados = [
        doi for doi, r in resultados.items() if r.get("status") == "nao_encontrado"
    ]
    if dois_nao_encontrados:
        audit.adicionar_metadado("dois_nao_encontrados", dois_nao_encontrados)

    audit.registrar_contagens(
        lidos=total,
        validos=total,
        processados=encontrados,
        rejeitados=nao_encontrados,
    )
    audit.adicionar_metadado("estatisticas", estatisticas)

    status_final = "SUCESSO" if nao_encontrados == 0 else "SUCESSO_COM_ALERTAS"
    audit.finalizar(status=status_final)

    logger.info("=" * 60)
    logger.info("ENRIQUECIMENTO S2 CONCLUIDO")
    logger.info("Duracao: %.1f segundos", duracao)
    logger.info("Encontrados: %d | Nao encontrados: %d | Total: %d", encontrados, nao_encontrados, total)
    logger.info("Cobertura S2: %.1f%%", estatisticas["taxa_cobertura_s2"])
    logger.info("Media citacoes: %.1f | Total citacoes: %d", media_citacoes, sum(citacoes))
    logger.info("Output: %s", output_path.name)
    logger.info("=" * 60)

    return estatisticas


if __name__ == "__main__":
    import os
    import sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    # Encontrar o arquivo de papers mais recente
    processed_dir = DATA_DIR / "processed"
    papers_files = sorted(processed_dir.glob("papers_fase1_*.json"))
    if not papers_files:
        logger.error("Nenhum arquivo papers_fase1_*.json encontrado")
        sys.exit(1)

    input_path = papers_files[-1]
    logger.info("Usando: %s", input_path.name)

    s2_api_key = os.environ.get("S2_API_KEY", "")
    resultado = enriquecer_papers_s2(input_path, s2_api_key=s2_api_key)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
