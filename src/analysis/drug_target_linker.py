"""Pipeline de cruzamento droga-alvo.

Consulta Open Targets e ChEMBL para os top 50 alvos proteicos,
cruza com DrugAge para efeitos em lifespan, e gera o dataset
completo de associacoes droga-alvo-doenca para o grafo de conhecimento.
"""

import csv
import json
import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from src.core.audit import AuditLogger
from src.ingestion.chembl import ChEMBLClient
from src.ingestion.drugbank import (
    GEROPROTETORES_CONHECIDOS,
    DrugTargetAssociation,
    OpenTargetsClient,
)

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

CHECKPOINT_DIR = DATA_DIR / "checkpoints"


@dataclass
class DrugCandidate:
    """Candidato a geroprotetor com dados consolidados."""

    drug_id: str = ""  # ChEMBL ID
    nome: str = ""
    max_fase_clinica: int = 0
    alvos: list[dict[str, Any]] = field(default_factory=list)
    doencas: list[str] = field(default_factory=list)
    mecanismos_acao: list[str] = field(default_factory=list)
    pchembl_melhor: float = 0.0
    lifespan_efeito: float = 0.0  # % de DrugAge
    lifespan_especies: list[str] = field(default_factory=list)
    geroprotetor_conhecido: bool = False
    n_alvos_envelhecimento: int = 0
    fontes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "drug_id": self.drug_id,
            "nome": self.nome,
            "max_fase_clinica": self.max_fase_clinica,
            "alvos": self.alvos,
            "doencas": self.doencas,
            "mecanismos_acao": self.mecanismos_acao,
            "pchembl_melhor": self.pchembl_melhor,
            "lifespan_efeito": self.lifespan_efeito,
            "lifespan_especies": self.lifespan_especies,
            "geroprotetor_conhecido": self.geroprotetor_conhecido,
            "n_alvos_envelhecimento": self.n_alvos_envelhecimento,
            "fontes": self.fontes,
        }


def carregar_alvos(alvos_path: Path) -> list[dict[str, Any]]:
    """Carrega lista consolidada de alvos.

    Args:
        alvos_path: Caminho do JSON de alvos consolidados.

    Returns:
        Lista de dicts com dados dos alvos.
    """
    with open(alvos_path, "r", encoding="utf-8") as f:
        return json.load(f)


def carregar_drugage(drugage_path: Path | None = None) -> dict[str, list[dict[str, Any]]]:
    """Carrega DrugAge e indexa por nome de composto.

    Args:
        drugage_path: Caminho do CSV DrugAge.

    Returns:
        Dict de nome_composto_lower -> lista de entradas DrugAge.
    """
    if drugage_path is None:
        drugage_path = DATA_DIR / "external" / "drugage.csv"

    if not drugage_path.exists():
        logger.warning("DrugAge nao encontrado: %s", drugage_path)
        return {}

    index: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for encoding in ["utf-8", "cp1252", "latin-1"]:
        try:
            with open(drugage_path, "r", encoding=encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nome = row.get("compound_name", "").strip().lower()
                    if not nome:
                        continue

                    try:
                        avg_change = float(row.get("avg_lifespan_change_percent", "0") or "0")
                    except ValueError:
                        avg_change = 0.0

                    entry = {
                        "compound_name": row.get("compound_name", "").strip(),
                        "species": row.get("species", "").strip(),
                        "strain": row.get("strain", "").strip(),
                        "dosage": row.get("dosage", "").strip(),
                        "avg_lifespan_change_percent": avg_change,
                        "max_lifespan_change_percent": row.get("max_lifespan_change_percent", ""),
                        "gender": row.get("gender", "").strip(),
                        "significance": row.get("significance", "").strip(),
                    }
                    index[nome].append(entry)

            logger.info("DrugAge carregado: %d compostos unicos", len(index))
            return index
        except UnicodeDecodeError:
            continue

    logger.error("Nao foi possivel decodificar DrugAge")
    return {}


def carregar_checkpoint(ckpt_path: Path) -> dict[str, Any]:
    """Carrega checkpoint de consulta anterior."""
    if ckpt_path.exists():
        try:
            with open(ckpt_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            logger.warning("Checkpoint corrompido, iniciando do zero")
    return {"alvos_consultados": [], "associacoes": [], "timestamp": ""}


def salvar_checkpoint(ckpt_path: Path, data: dict[str, Any]) -> None:
    """Salva checkpoint atomicamente."""
    import tempfile
    ckpt_path.parent.mkdir(parents=True, exist_ok=True)
    data["timestamp"] = datetime.now().isoformat()
    tmp = ckpt_path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    tmp.replace(ckpt_path)


def consultar_open_targets(
    alvos: list[dict[str, Any]],
    ckpt_path: Path | None = None,
) -> list[dict[str, Any]]:
    """Consulta Open Targets para todos os alvos.

    Args:
        alvos: Lista de alvos com ensembl_id.
        ckpt_path: Caminho do checkpoint (para retomada).

    Returns:
        Lista de associacoes droga-alvo-doenca.
    """
    if ckpt_path is None:
        ckpt_path = CHECKPOINT_DIR / "ckpt_open_targets.json"

    ckpt = carregar_checkpoint(ckpt_path)
    alvos_ja_consultados = set(ckpt["alvos_consultados"])
    todas_associacoes = list(ckpt["associacoes"])

    ot_client = OpenTargetsClient()

    alvos_pendentes = [
        a for a in alvos
        if a.get("ensembl_id") and a["ensembl_id"] not in alvos_ja_consultados
    ]

    logger.info(
        "Open Targets: %d alvos pendentes (de %d total, %d ja consultados)",
        len(alvos_pendentes), len(alvos), len(alvos_ja_consultados),
    )

    for i, alvo in enumerate(alvos_pendentes):
        ensembl_id = alvo["ensembl_id"]
        symbol = alvo.get("symbol", "")

        try:
            assocs = ot_client.buscar_drogas_por_alvo(ensembl_id, max_results=100)

            for assoc in assocs:
                todas_associacoes.append(assoc.to_dict())

            alvos_ja_consultados.add(ensembl_id)
            logger.info(
                "[%d/%d] %s (%s): %d associacoes",
                i + 1, len(alvos_pendentes), symbol, ensembl_id, len(assocs),
            )

        except Exception as e:
            logger.error("Erro consultando %s: %s", symbol, e)

        # Checkpoint a cada 5 alvos
        if (i + 1) % 5 == 0 or i == len(alvos_pendentes) - 1:
            salvar_checkpoint(ckpt_path, {
                "alvos_consultados": list(alvos_ja_consultados),
                "associacoes": todas_associacoes,
            })

    logger.info(
        "Open Targets concluido: %d associacoes totais de %d alvos",
        len(todas_associacoes), len(alvos_ja_consultados),
    )
    return todas_associacoes


def consultar_chembl_atividades(
    drug_ids: list[str],
    chembl_client: ChEMBLClient | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Consulta ChEMBL para atividades dos compostos.

    Busca apenas compostos que ja foram identificados via Open Targets +
    geroprotetores conhecidos. Foco em IC50/Ki com pChEMBL >= 5.

    Args:
        drug_ids: Lista de ChEMBL IDs de drogas para consultar.
        chembl_client: Cliente ChEMBL (opcional, cria um novo se nao fornecido).

    Returns:
        Dict de drug_chembl_id -> lista de atividades.
    """
    if chembl_client is None:
        chembl_client = ChEMBLClient()

    resultados: dict[str, list[dict[str, Any]]] = {}

    logger.info("ChEMBL: consultando atividades de %d compostos...", len(drug_ids))

    for i, drug_id in enumerate(drug_ids):
        try:
            activities = chembl_client.buscar_atividades_por_composto(
                drug_id, max_results=50,
            )
            if activities:
                resultados[drug_id] = [a.to_dict() for a in activities]

            if (i + 1) % 10 == 0:
                logger.info(
                    "[%d/%d] ChEMBL atividades: %s -> %d resultados",
                    i + 1, len(drug_ids), drug_id, len(activities),
                )

        except Exception as e:
            logger.error("Erro ChEMBL atividades %s: %s", drug_id, e)

    logger.info("ChEMBL concluido: %d compostos com atividades", len(resultados))
    return resultados


def executar_pipeline(
    alvos_path: Path,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    """Executa pipeline completo de cruzamento droga-alvo.

    1. Carrega alvos consolidados
    2. Consulta Open Targets para associacoes
    3. Cruza com DrugAge para efeitos em lifespan
    4. Consolida candidatos unicos
    5. Salva resultados

    Args:
        alvos_path: Caminho do JSON de alvos consolidados.
        output_dir: Diretorio de output.

    Returns:
        Estatisticas do pipeline.
    """
    audit = AuditLogger(modulo="drug_target_linker")
    audit.registrar_input(alvos_path)

    if output_dir is None:
        output_dir = DATA_DIR / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Carregar alvos
    alvos = carregar_alvos(alvos_path)
    logger.info("Alvos carregados: %d", len(alvos))

    # 2. Carregar DrugAge
    drugage = carregar_drugage()

    # 3. Consultar Open Targets
    associacoes = consultar_open_targets(alvos)

    # 4. Injetar geroprotetores conhecidos como candidatos
    # Open Targets foca em drugs em clinical trials. Muitos geroprotetores
    # sao off-label ou suplementos, entao precisam ser injetados manualmente.
    drogas_por_id: dict[str, DrugCandidate] = {}
    nomes_geroprotetores = {g["nome"].lower() for g in GEROPROTETORES_CONHECIDOS}
    chembl_geroprotetores = {g["chembl_id"] for g in GEROPROTETORES_CONHECIDOS if g["chembl_id"]}

    for gero in GEROPROTETORES_CONHECIDOS:
        cid = gero["chembl_id"]
        if not cid:
            continue
        drogas_por_id[cid] = DrugCandidate(
            drug_id=cid,
            nome=gero["nome"],
            max_fase_clinica=gero["fase"],
            mecanismos_acao=[gero["mecanismo"]],
            geroprotetor_conhecido=True,
            fontes=["curado"],
        )

    # 5. Consultar ChEMBL para atividades dos geroprotetores
    gero_chembl_ids = [g["chembl_id"] for g in GEROPROTETORES_CONHECIDOS if g["chembl_id"]]
    chembl_client = ChEMBLClient()
    chembl_atividades = consultar_chembl_atividades(gero_chembl_ids, chembl_client)

    # Atualizar pChEMBL dos geroprotetores
    for cid, atividades in chembl_atividades.items():
        if cid in drogas_por_id:
            melhor = max((a.get("pchembl_value", 0) for a in atividades), default=0)
            drogas_por_id[cid].pchembl_melhor = melhor

    # 6. Consolidar drogas do Open Targets
    for assoc in associacoes:
        drug_id = assoc.get("drug_id", "")
        if not drug_id:
            continue

        if drug_id not in drogas_por_id:
            drogas_por_id[drug_id] = DrugCandidate(
                drug_id=drug_id,
                nome=assoc.get("drug_nome", ""),
                fontes=["open_targets"],
            )

        droga = drogas_por_id[drug_id]

        # Atualizar fase clinica
        fase = assoc.get("fase_clinica", 0)
        if fase > droga.max_fase_clinica:
            droga.max_fase_clinica = fase

        # Adicionar alvo
        target_gene = assoc.get("target_gene", "")
        if target_gene and not any(a.get("gene") == target_gene for a in droga.alvos):
            droga.alvos.append({
                "gene": target_gene,
                "ensembl_id": assoc.get("target_id", ""),
                "nome": assoc.get("target_nome", ""),
            })

        # Adicionar doenca
        disease = assoc.get("disease_nome", "")
        if disease and disease not in droga.doencas:
            droga.doencas.append(disease)

        # Mecanismo de acao
        moa = assoc.get("mecanismo_acao", "")
        if moa and moa not in droga.mecanismos_acao:
            droga.mecanismos_acao.append(moa)

        # Marcar como geroprotetor conhecido
        if drug_id in chembl_geroprotetores or droga.nome.lower() in nomes_geroprotetores:
            droga.geroprotetor_conhecido = True

    # 7. Cruzar com DrugAge
    for droga in drogas_por_id.values():
        nome_lower = droga.nome.lower()
        if nome_lower in drugage:
            entries = drugage[nome_lower]
            # Media do efeito em lifespan (apenas entradas significativas)
            efeitos = [e["avg_lifespan_change_percent"] for e in entries
                       if e["avg_lifespan_change_percent"] != 0]
            if efeitos:
                droga.lifespan_efeito = round(sum(efeitos) / len(efeitos), 2)
                droga.lifespan_especies = list(set(
                    e["species"] for e in entries if e["species"]
                ))
            if "drugage" not in droga.fontes:
                droga.fontes.append("drugage")

    # 8. Contar alvos do envelhecimento
    alvos_symbols = {a["symbol"] for a in alvos}
    for droga in drogas_por_id.values():
        droga.n_alvos_envelhecimento = sum(
            1 for a in droga.alvos if a["gene"] in alvos_symbols
        )

    # 9. Salvar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 9a. Associacoes completas (para o grafo)
    assoc_path = output_dir / f"drug_target_associations_{timestamp}.json"
    with open(assoc_path, "w", encoding="utf-8") as f:
        json.dump(associacoes, f, ensure_ascii=False, indent=2)
    audit.registrar_output(assoc_path)

    # 9b. Candidatos consolidados
    candidatos = sorted(
        drogas_por_id.values(),
        key=lambda d: (d.n_alvos_envelhecimento, d.max_fase_clinica, d.lifespan_efeito),
        reverse=True,
    )
    candidatos_path = output_dir / f"drug_candidates_{timestamp}.json"
    with open(candidatos_path, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in candidatos], f, ensure_ascii=False, indent=2)
    audit.registrar_output(candidatos_path)

    # Estatisticas
    total_drogas = len(drogas_por_id)
    com_lifespan = sum(1 for d in drogas_por_id.values() if d.lifespan_efeito != 0)
    geroprotetores_encontrados = sum(
        1 for d in drogas_por_id.values() if d.geroprotetor_conhecido
    )

    stats = {
        "total_associacoes": len(associacoes),
        "total_drogas_unicas": total_drogas,
        "drogas_com_lifespan_data": com_lifespan,
        "geroprotetores_conhecidos_encontrados": geroprotetores_encontrados,
        "alvos_consultados": len(alvos),
        "arquivo_associacoes": assoc_path.name,
        "arquivo_candidatos": candidatos_path.name,
    }

    # Log final
    logger.info("=" * 60)
    logger.info("PIPELINE DRUG-TARGET CONCLUIDO")
    logger.info("Alvos consultados: %d", len(alvos))
    logger.info("Associacoes totais: %d", len(associacoes))
    logger.info("Drogas unicas: %d", total_drogas)
    logger.info("Com dados DrugAge (lifespan): %d", com_lifespan)
    logger.info("Geroprotetores conhecidos encontrados: %d/13", geroprotetores_encontrados)
    logger.info("TOP 15 DROGAS (por n. alvos envelhecimento):")
    for c in candidatos[:15]:
        logger.info(
            "  %s (fase %d, %d alvos, lifespan=%.1f%%): %s",
            c.nome or c.drug_id, c.max_fase_clinica,
            c.n_alvos_envelhecimento, c.lifespan_efeito,
            ", ".join(a["gene"] for a in c.alvos[:5]),
        )
    logger.info("Salvos: %s, %s", assoc_path.name, candidatos_path.name)
    logger.info("=" * 60)

    audit.registrar_contagens(
        lidos=len(alvos),
        validos=total_drogas,
        processados=len(associacoes),
        rejeitados=0,
    )
    audit.adicionar_metadado("estatisticas", stats)
    audit.finalizar(status="SUCESSO")

    return stats


if __name__ == "__main__":
    import sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    processed_dir = DATA_DIR / "processed"
    alvos_files = sorted(processed_dir.glob("top50_alvos_consolidados_*.json"))

    if not alvos_files:
        logger.error("Nenhum arquivo de alvos consolidados encontrado")
        sys.exit(1)

    alvos_path = alvos_files[-1]
    logger.info("Usando: %s", alvos_path.name)

    stats = executar_pipeline(alvos_path)
    print(json.dumps(stats, indent=2, ensure_ascii=False))
