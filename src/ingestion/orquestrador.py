"""Orquestrador de busca em escala.

Executa todas as queries do search_queries.yaml, deduplica,
filtra, verifica licencas e registra no bibliography.
Gera audit log completo de toda a execucao.
"""

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from src.core.audit import AuditLogger
from src.core.bibliography import GestorBibliografia, Referencia
from src.ingestion.filtro import filtrar_batch
from src.ingestion.pubmed import PubMedArticle, PubMedClient
from src.ingestion.unpaywall import UnpaywallClient

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"


def carregar_queries(config_path: Path | None = None) -> list[dict]:
    """Carrega queries do arquivo de configuracao.

    Args:
        config_path: Caminho do YAML (padrao: config/search_queries.yaml).

    Returns:
        Lista de dicts com query, max_results, date_range, descricao.
    """
    if config_path is None:
        config_path = CONFIG_DIR / "search_queries.yaml"

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    queries = config.get("fase_1_exploratorio", {}).get("pubmed", [])
    logger.info("Carregadas %d queries do config", len(queries))
    return queries


def executar_busca_completa(
    pubmed_api_key: str = "",
    pubmed_email: str = "",
    unpaywall_email: str = "discovery.engine@research.org",
) -> dict[str, Any]:
    """Executa o pipeline completo de busca em escala.

    Fluxo:
    1. Carrega queries do config
    2. Busca papers no PubMed (todas as queries)
    3. Deduplica por DOI
    4. Aplica filtros de inclusao/exclusao
    5. Verifica licencas via Unpaywall
    6. Registra no bibliography
    7. Salva resultados em data/processed/
    8. Gera audit log

    Args:
        pubmed_api_key: API key do NCBI (opcional).
        pubmed_email: Email para o NCBI.
        unpaywall_email: Email para o Unpaywall.

    Returns:
        Dict com estatisticas da execucao.
    """
    audit = AuditLogger(modulo="busca_escala_fase1")
    inicio = time.time()

    # --- 1. Carregar queries ---
    queries = carregar_queries()
    audit.adicionar_metadado("total_queries", len(queries))

    # --- 2. Buscar no PubMed ---
    pubmed = PubMedClient(api_key=pubmed_api_key, email=pubmed_email)
    todos_artigos: list[PubMedArticle] = []

    for i, q in enumerate(queries, 1):
        query_str = q["query"]
        max_results = q.get("max_results", 100)
        date_range = q.get("date_range", "")
        descricao = q.get("descricao", "")

        date_min = ""
        date_max = ""
        if date_range and ":" in date_range:
            parts = date_range.split(":")
            date_min = parts[0]
            date_max = parts[1]

        logger.info(
            "[%d/%d] Buscando: '%s' (max=%d) - %s",
            i, len(queries), query_str, max_results, descricao,
        )

        articles = pubmed.search_and_fetch(
            query=query_str,
            max_results=max_results,
            date_min=date_min,
            date_max=date_max,
        )
        todos_artigos.extend(articles)
        logger.info("[%d/%d] %d artigos retornados", i, len(queries), len(articles))

    total_bruto = len(todos_artigos)
    logger.info("Total bruto (com duplicatas): %d artigos", total_bruto)

    # --- 3. Deduplicar por DOI ---
    vistos: set[str] = set()
    unicos: list[PubMedArticle] = []
    sem_doi: int = 0

    for art in todos_artigos:
        if not art.doi:
            sem_doi += 1
            continue
        doi_lower = art.doi.lower()
        if doi_lower not in vistos:
            vistos.add(doi_lower)
            unicos.append(art)

    duplicatas = total_bruto - len(unicos) - sem_doi
    logger.info(
        "Deduplicacao: %d unicos, %d duplicatas removidas, %d sem DOI",
        len(unicos), duplicatas, sem_doi,
    )

    # --- 4. Filtrar ---
    aceitos, rejeitados = filtrar_batch(unicos)
    logger.info("Filtro: %d aceitos, %d rejeitados", len(aceitos), len(rejeitados))

    # --- 5. Verificar licencas via Unpaywall ---
    unpaywall = UnpaywallClient(email=unpaywall_email)
    dois_para_verificar = [a.doi for a in aceitos if a.doi]
    logger.info("Verificando licencas de %d papers via Unpaywall...", len(dois_para_verificar))
    licencas = unpaywall.check_licenses_batch(dois_para_verificar)

    # --- 6. Registrar no bibliography ---
    gestor = GestorBibliografia()
    novos_registrados = 0

    for art in aceitos:
        if not art.doi:
            continue
        lic_info = licencas.get(art.doi.lower())
        licenca = lic_info.licenca if lic_info else ""

        ref = Referencia(
            doi=art.doi,
            titulo=art.titulo,
            autores=art.autores,
            ano=art.ano,
            journal=art.journal,
            abstract=art.abstract,
            licenca=licenca,
            pmid=art.pmid,
            fonte="pubmed",
        )
        if gestor.adicionar(ref):
            novos_registrados += 1

    # --- 7. Salvar resultados processados ---
    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Salvar papers aceitos como JSON
    papers_file = processed_dir / f"papers_fase1_{timestamp}.json"
    papers_data = [art.to_dict() for art in aceitos]
    with open(papers_file, "w", encoding="utf-8") as f:
        json.dump(papers_data, f, ensure_ascii=False, indent=2)

    # Salvar rejeitados para auditoria
    rejected_file = processed_dir / f"rejeitados_fase1_{timestamp}.json"
    with open(rejected_file, "w", encoding="utf-8") as f:
        json.dump(rejeitados, f, ensure_ascii=False, indent=2)

    audit.registrar_output(papers_file)
    audit.registrar_output(rejected_file)

    # --- 8. Estatisticas finais ---
    duracao = time.time() - inicio
    resumo_bib = gestor.resumo()

    estatisticas = {
        "duracao_segundos": round(duracao, 1),
        "queries_executadas": len(queries),
        "total_bruto": total_bruto,
        "sem_doi": sem_doi,
        "duplicatas_removidas": duplicatas,
        "unicos": len(unicos),
        "aceitos_filtro": len(aceitos),
        "rejeitados_filtro": len(rejeitados),
        "licencas_verificadas": len(licencas),
        "open_access": sum(1 for l in licencas.values() if l.is_oa),
        "novos_registrados": novos_registrados,
        "acervo_total": resumo_bib,
        "arquivo_papers": str(papers_file.name),
        "arquivo_rejeitados": str(rejected_file.name),
    }

    # Motivos de rejeicao agregados
    motivos: dict[str, int] = {}
    for r in rejeitados:
        motivo = r["motivo"].split(":")[0].strip()
        motivos[motivo] = motivos.get(motivo, 0) + 1
    estatisticas["motivos_rejeicao"] = motivos

    audit.registrar_contagens(
        lidos=total_bruto,
        validos=len(unicos),
        processados=len(aceitos),
        rejeitados=len(rejeitados),
    )
    audit.adicionar_metadado("estatisticas", estatisticas)
    audit.finalizar(status="SUCESSO")

    logger.info("=" * 60)
    logger.info("BUSCA EM ESCALA CONCLUIDA")
    logger.info("Duracao: %.1f segundos", duracao)
    logger.info("Bruto: %d | Unicos: %d | Aceitos: %d | Rejeitados: %d",
                total_bruto, len(unicos), len(aceitos), len(rejeitados))
    logger.info("Novos no acervo: %d | Acervo total: %d",
                novos_registrados, resumo_bib["total_referencias"])
    logger.info("=" * 60)

    return estatisticas


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    resultado = executar_busca_completa()
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
