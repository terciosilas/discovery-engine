"""Sistema de scoring e ranqueamento de candidatos geroprotetores.

Combina multiplas features para ranquear compostos por potencial
de drug repurposing para longevidade:
  - Evidencia na literatura (citacoes, papers mencionando alvos)
  - Potencia biologica (pChEMBL)
  - Fase clinica (aprovado > fase 3 > fase 2 > ...)
  - Dados de lifespan in vivo (DrugAge)
  - Centralidade no grafo de conhecimento
  - Numero de alvos do envelhecimento atingidos
  - Status de geroprotetor conhecido (controle positivo)
"""

import json
import logging
import math
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from src.core.audit import AuditLogger

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


# Pesos do scoring (somam ~1.0)
PESOS = {
    "fase_clinica": 0.20,       # Seguranca em humanos ja demonstrada
    "n_alvos_envelhecimento": 0.20,  # Pleiotropia - atinge multiplas vias
    "lifespan_efeito": 0.20,    # Evidencia direta de extensao de vida
    "pchembl": 0.10,            # Potencia biologica
    "literatura": 0.15,         # Evidencia na literatura cientifica
    "centralidade_grafo": 0.15, # Posicao no network biologico
}


@dataclass
class ScoredCandidate:
    """Candidato com score calculado."""

    rank: int = 0
    drug_id: str = ""
    nome: str = ""
    score_total: float = 0.0
    score_detalhado: dict[str, float] = field(default_factory=dict)
    max_fase_clinica: int = 0
    n_alvos_envelhecimento: int = 0
    alvos: list[str] = field(default_factory=list)
    lifespan_efeito: float = 0.0
    lifespan_especies: list[str] = field(default_factory=list)
    pchembl_melhor: float = 0.0
    mecanismos_acao: list[str] = field(default_factory=list)
    geroprotetor_conhecido: bool = False
    centralidade_grau: float = 0.0
    fontes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "rank": self.rank,
            "drug_id": self.drug_id,
            "nome": self.nome,
            "score_total": round(self.score_total, 4),
            "score_detalhado": {k: round(v, 4) for k, v in self.score_detalhado.items()},
            "max_fase_clinica": self.max_fase_clinica,
            "n_alvos_envelhecimento": self.n_alvos_envelhecimento,
            "alvos": self.alvos,
            "lifespan_efeito": self.lifespan_efeito,
            "lifespan_especies": self.lifespan_especies,
            "pchembl_melhor": self.pchembl_melhor,
            "mecanismos_acao": self.mecanismos_acao,
            "geroprotetor_conhecido": self.geroprotetor_conhecido,
            "centralidade_grau": round(self.centralidade_grau, 4),
            "fontes": self.fontes,
        }


def _normalizar_min_max(valor: float, min_val: float, max_val: float) -> float:
    """Normaliza valor para 0-1 usando min-max."""
    if max_val == min_val:
        return 0.5
    return max(0.0, min(1.0, (valor - min_val) / (max_val - min_val)))


def _score_fase_clinica(fase: int) -> float:
    """Score baseado na fase clinica (0-1)."""
    # Fase 4 (aprovado) = 1.0, Fase 3 = 0.75, Fase 2 = 0.5, Fase 1 = 0.25, Fase 0 = 0.1
    scores = {0: 0.1, 1: 0.25, 2: 0.5, 3: 0.75, 4: 1.0}
    return scores.get(fase, 0.1)


def _score_lifespan(efeito: float) -> float:
    """Score baseado no efeito em lifespan (0-1).

    Efeito positivo (extensao) = bom. Logaritmico para nao dominar.
    """
    if efeito <= 0:
        return 0.0
    # Sigmoid-like: 10% = 0.5, 30% = 0.75, 50%+ = ~0.9
    return min(1.0, 1.0 - 1.0 / (1.0 + efeito / 15.0))


def _score_pchembl(pchembl: float) -> float:
    """Score baseado na potencia (pChEMBL, 0-1).

    pChEMBL >= 8 = excelente, >= 6 = ativo, < 5 = fraco.
    """
    if pchembl <= 0:
        return 0.0
    if pchembl >= 9:
        return 1.0
    if pchembl >= 6:
        return 0.5 + (pchembl - 6) / 6.0
    return max(0.0, pchembl / 12.0)


def calcular_scores(
    candidatos_path: Path,
    metricas_path: Path,
    papers_path: Path | None = None,
    output_dir: Path | None = None,
) -> list[ScoredCandidate]:
    """Calcula scores para todos os candidatos.

    Args:
        candidatos_path: JSON de drug_candidates.
        metricas_path: JSON de graph_metrics.
        papers_path: JSON de papers enriquecidos (para citacoes).
        output_dir: Diretorio de output.

    Returns:
        Lista de ScoredCandidate ordenados por score.
    """
    audit = AuditLogger(modulo="candidate_scorer")
    audit.registrar_input(candidatos_path)
    audit.registrar_input(metricas_path)

    if output_dir is None:
        output_dir = DATA_DIR / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Carregar dados
    with open(candidatos_path, "r", encoding="utf-8") as f:
        candidatos = json.load(f)
    with open(metricas_path, "r", encoding="utf-8") as f:
        metricas = json.load(f)

    # Indexar centralidade de drogas no grafo
    centrality_idx: dict[str, float] = {}
    for d in metricas.get("top_drogas_centralidade", []):
        node = d.get("node", "")
        # node format: "drug:CHEMBL..."
        drug_id = node.replace("drug:", "")
        centrality_idx[drug_id] = d.get("degree_centrality", 0)

    # Carregar dados de literatura (papers enriquecidos) para menções
    literature_score: dict[str, float] = {}
    if papers_path and papers_path.exists():
        with open(papers_path, "r", encoding="utf-8") as f:
            papers = json.load(f)
        audit.registrar_input(papers_path)
        # Nao usamos citacoes neste ponto, apenas contagem de papers
        # Isso fica mais relevante quando cruzamos com os alvos
        logger.info("Papers carregados para referencia: %d", len(papers))

    # Calcular scores
    max_alvos = max((c.get("n_alvos_envelhecimento", 0) for c in candidatos), default=1)
    max_centrality = max(centrality_idx.values(), default=0.01)

    scored: list[ScoredCandidate] = []

    for cand in candidatos:
        drug_id = cand.get("drug_id", "")
        if not drug_id:
            continue

        sc = ScoredCandidate(
            drug_id=drug_id,
            nome=cand.get("nome", ""),
            max_fase_clinica=cand.get("max_fase_clinica", 0),
            n_alvos_envelhecimento=cand.get("n_alvos_envelhecimento", 0),
            alvos=[a.get("gene", "") for a in cand.get("alvos", [])],
            lifespan_efeito=cand.get("lifespan_efeito", 0.0),
            lifespan_especies=cand.get("lifespan_especies", []),
            pchembl_melhor=cand.get("pchembl_melhor", 0.0),
            mecanismos_acao=cand.get("mecanismos_acao", []),
            geroprotetor_conhecido=cand.get("geroprotetor_conhecido", False),
            centralidade_grau=centrality_idx.get(drug_id, 0.0),
            fontes=cand.get("fontes", []),
        )

        # Scores individuais (0-1)
        s_fase = _score_fase_clinica(sc.max_fase_clinica)
        s_alvos = _normalizar_min_max(sc.n_alvos_envelhecimento, 0, max_alvos)
        s_lifespan = _score_lifespan(sc.lifespan_efeito)
        s_pchembl = _score_pchembl(sc.pchembl_melhor)
        s_literatura = 0.3 if sc.fontes else 0.0  # Base score, melhorado na Fase 3
        if sc.geroprotetor_conhecido:
            s_literatura = 0.8  # Geroprotetores tem evidencia forte
        s_centralidade = _normalizar_min_max(
            sc.centralidade_grau, 0, max_centrality,
        ) if max_centrality > 0 else 0.0

        sc.score_detalhado = {
            "fase_clinica": s_fase,
            "n_alvos_envelhecimento": s_alvos,
            "lifespan_efeito": s_lifespan,
            "pchembl": s_pchembl,
            "literatura": s_literatura,
            "centralidade_grafo": s_centralidade,
        }

        # Score total ponderado
        sc.score_total = sum(
            sc.score_detalhado[k] * PESOS[k]
            for k in PESOS
        )

        scored.append(sc)

    # Ordenar por score total
    scored.sort(key=lambda s: s.score_total, reverse=True)

    # Atribuir ranks
    for i, sc in enumerate(scored):
        sc.rank = i + 1

    # Salvar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"ranked_candidates_{timestamp}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in scored], f, ensure_ascii=False, indent=2)
    audit.registrar_output(output_path)

    # Verificar controles positivos
    rapamycin_rank = next((s.rank for s in scored if "rapamycin" in s.nome.lower()), -1)
    metformin_rank = next((s.rank for s in scored if "metformin" in s.nome.lower()), -1)

    # Log final
    logger.info("=" * 60)
    logger.info("RANQUEAMENTO DE CANDIDATOS CONCLUIDO")
    logger.info("Total candidatos ranqueados: %d", len(scored))
    logger.info("")
    logger.info("PESOS: %s", PESOS)
    logger.info("")
    logger.info("CONTROLES POSITIVOS:")
    logger.info("  Rapamycin: rank #%d (meta: top 10)", rapamycin_rank)
    logger.info("  Metformin: rank #%d (meta: top 10)", metformin_rank)
    controle_ok = rapamycin_rank <= 10 and metformin_rank <= 10
    logger.info("  Status: %s", "PASSOU" if controle_ok else "FALHOU - ajustar pesos!")
    logger.info("")
    logger.info("TOP 20 CANDIDATOS:")
    for sc in scored[:20]:
        gero = " *" if sc.geroprotetor_conhecido else ""
        logger.info(
            "  #%d %s (score=%.3f, fase=%d, alvos=%d, lifespan=%.1f%%)%s",
            sc.rank, sc.nome or sc.drug_id, sc.score_total,
            sc.max_fase_clinica, sc.n_alvos_envelhecimento,
            sc.lifespan_efeito, gero,
        )
    logger.info("")
    logger.info("Salvo: %s", output_path.name)
    logger.info("=" * 60)

    audit.registrar_contagens(
        lidos=len(candidatos),
        validos=len(scored),
        processados=len(scored),
        rejeitados=0,
    )
    audit.adicionar_metadado("rapamycin_rank", rapamycin_rank)
    audit.adicionar_metadado("metformin_rank", metformin_rank)
    audit.adicionar_metadado("controle_positivo_passou", controle_ok)
    audit.finalizar(status="SUCESSO" if controle_ok else "SUCESSO_COM_ALERTAS")

    return scored


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    processed_dir = DATA_DIR / "processed"
    cand_files = sorted(processed_dir.glob("drug_candidates_*.json"))
    metr_files = sorted(processed_dir.glob("graph_metrics_*.json"))
    paper_files = sorted(processed_dir.glob("papers_enriched_fase1_*.json"))

    if not cand_files or not metr_files:
        logger.error("Arquivos de input nao encontrados")
        exit(1)

    papers_path = paper_files[-1] if paper_files else None

    scored = calcular_scores(
        candidatos_path=cand_files[-1],
        metricas_path=metr_files[-1],
        papers_path=papers_path,
    )
    print(f"\nTotal: {len(scored)} candidatos ranqueados")
    rapamycin = next((s for s in scored if "rapamycin" in s.nome.lower()), None)
    metformin = next((s for s in scored if "metformin" in s.nome.lower()), None)
    if rapamycin:
        print(f"Rapamycin: rank #{rapamycin.rank}, score={rapamycin.score_total:.3f}")
    if metformin:
        print(f"Metformin: rank #{metformin.rank}, score={metformin.score_total:.3f}")
