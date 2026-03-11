"""Filtro de inclusao/exclusao de papers.

Aplica os criterios definidos em config/inclusion_criteria.yaml
para garantir que apenas papers relevantes entrem no acervo.
Criterios definidos ANTES das buscas (exigencia etica).
"""

import logging
import re
from dataclasses import dataclass, field
from typing import Any

from src.ingestion.pubmed import PubMedArticle

logger = logging.getLogger(__name__)


@dataclass
class ResultadoFiltro:
    """Resultado da aplicacao dos filtros em um paper."""

    aceito: bool = False
    motivo_rejeicao: str = ""
    warnings: list[str] = field(default_factory=list)


# Termos de exclusao (presentes no titulo ou abstract = rejeitar)
TERMOS_EXCLUSAO = [
    "cosmetic aging",
    "food aging",
    "material aging",
    "wine aging",
    "cheese aging",
    "food preservation",
    "material science",
    "skin aging cosmetic",
    "photo-aging skin",
]

# Tipos de publicacao excluidos
TIPOS_EXCLUIDOS = {
    "retracted publication",
    "retraction of publication",
    "erratum",
    "published erratum",
    "editorial",
    "letter",
    "comment",
    "case reports",
}

# Termos biologicos (pelo menos 1 deve estar presente)
TERMOS_BIOLOGICOS = [
    "aging", "longevity", "senescence", "geroprotect",
    "healthspan", "lifespan", "geroscience", "senolytic",
    "age-related", "anti-aging", "ageing",
]

# Termos moleculares (pelo menos 1 deve estar presente)
TERMOS_MOLECULARES = [
    "protein", "proteom", "drug", "compound", "molecule",
    "inhibitor", "agonist", "kinase", "receptor", "enzyme",
    "sirtuin", "mtor", "foxo", "klotho", "nad+", "rapamycin",
    "metformin", "senolytic", "dasatinib", "quercetin",
]


def filtrar_paper(article: PubMedArticle) -> ResultadoFiltro:
    """Aplica criterios de inclusao/exclusao a um paper.

    Args:
        article: Artigo do PubMed.

    Returns:
        ResultadoFiltro indicando se o paper foi aceito ou rejeitado.
    """
    resultado = ResultadoFiltro()
    texto = f"{article.titulo} {article.abstract}".lower()

    # --- EXCLUSAO (qualquer criterio exclui) ---

    # Tipo de publicacao
    tipos_paper = {t.lower() for t in article.tipo_publicacao}
    tipos_match = tipos_paper & TIPOS_EXCLUIDOS
    if tipos_match:
        resultado.motivo_rejeicao = f"Tipo excluido: {', '.join(tipos_match)}"
        return resultado

    # Termos de exclusao no titulo/abstract
    for termo in TERMOS_EXCLUSAO:
        if termo.lower() in texto:
            resultado.motivo_rejeicao = f"Termo excluido: '{termo}'"
            return resultado

    # Abstract muito curto
    abstract_palavras = len(article.abstract.split()) if article.abstract else 0
    if abstract_palavras < 50:
        resultado.motivo_rejeicao = f"Abstract muito curto ({abstract_palavras} palavras, minimo 50)"
        return resultado

    # Titulo muito curto
    titulo_palavras = len(article.titulo.split()) if article.titulo else 0
    if titulo_palavras < 5:
        resultado.motivo_rejeicao = f"Titulo muito curto ({titulo_palavras} palavras, minimo 5)"
        return resultado

    # Sem DOI
    if not article.doi:
        resultado.motivo_rejeicao = "Sem DOI"
        return resultado

    # --- INCLUSAO (todos os criterios devem ser atendidos) ---

    # Pelo menos 1 termo biologico
    tem_biologico = any(termo in texto for termo in TERMOS_BIOLOGICOS)
    if not tem_biologico:
        resultado.motivo_rejeicao = "Sem termo biologico relevante"
        return resultado

    # Pelo menos 1 termo molecular
    tem_molecular = any(termo in texto for termo in TERMOS_MOLECULARES)
    if not tem_molecular:
        resultado.motivo_rejeicao = "Sem termo molecular relevante"
        return resultado

    # Ano dentro do periodo
    if article.ano and (article.ano < 2020 or article.ano > 2026):
        resultado.motivo_rejeicao = f"Fora do periodo (ano={article.ano})"
        return resultado

    # --- ACEITO ---
    resultado.aceito = True

    # Warnings (nao bloqueiam, mas registram)
    if abstract_palavras < 100:
        resultado.warnings.append(f"Abstract curto ({abstract_palavras} palavras)")
    if not article.keywords:
        resultado.warnings.append("Sem keywords")

    return resultado


def filtrar_batch(articles: list[PubMedArticle]) -> tuple[list[PubMedArticle], list[dict[str, Any]]]:
    """Aplica filtros a um batch de papers.

    Args:
        articles: Lista de artigos do PubMed.

    Returns:
        Tupla (aceitos, rejeitados) onde rejeitados tem motivo.
    """
    aceitos: list[PubMedArticle] = []
    rejeitados: list[dict[str, Any]] = []

    for art in articles:
        resultado = filtrar_paper(art)
        if resultado.aceito:
            aceitos.append(art)
        else:
            rejeitados.append({
                "doi": art.doi,
                "titulo": art.titulo[:80],
                "motivo": resultado.motivo_rejeicao,
            })

    logger.info(
        "Filtro aplicado: %d aceitos, %d rejeitados de %d total",
        len(aceitos), len(rejeitados), len(articles),
    )
    return aceitos, rejeitados
