"""Extrator de proteinas/genes de abstracts cientificos.

Usa dicionario curado (GenAge + alvos conhecidos + aliases) para identificar
mencoes de proteinas e genes em textos biomedicos.
Abordagem: dicionario + regex. Sem dependencias pesadas (sem scispaCy/spaCy).
"""

import csv
import json
import logging
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from src.core.audit import AuditLogger

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


@dataclass
class GeneEntry:
    """Entrada no dicionario de genes."""

    symbol: str = ""
    nome: str = ""
    aliases: list[str] = field(default_factory=list)
    uniprot_id: str = ""
    ensembl_id: str = ""
    entrez_id: str = ""
    fonte: str = ""  # genage, curado, drugbank
    via: str = ""  # mTOR, sirtuinas, etc.

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "symbol": self.symbol,
            "nome": self.nome,
            "aliases": self.aliases,
            "uniprot_id": self.uniprot_id,
            "ensembl_id": self.ensembl_id,
            "entrez_id": self.entrez_id,
            "fonte": self.fonte,
            "via": self.via,
        }


@dataclass
class ExtractionResult:
    """Resultado da extracao de um paper."""

    doi: str = ""
    titulo: str = ""
    genes_encontrados: list[str] = field(default_factory=list)
    contagens: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "doi": self.doi,
            "titulo": self.titulo,
            "genes_encontrados": self.genes_encontrados,
            "contagens": self.contagens,
        }


def carregar_genage(genage_path: Path | None = None) -> list[GeneEntry]:
    """Carrega genes do GenAge (database de genes humanos do envelhecimento).

    Args:
        genage_path: Caminho do CSV (padrao: data/external/genage_human.csv).

    Returns:
        Lista de GeneEntry.
    """
    if genage_path is None:
        genage_path = DATA_DIR / "external" / "genage_human.csv"

    if not genage_path.exists():
        logger.warning("GenAge nao encontrado: %s", genage_path)
        return []

    entries = []
    with open(genage_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = GeneEntry(
                symbol=row.get("symbol", "").strip(),
                nome=row.get("name", "").strip(),
                uniprot_id=row.get("uniprot", "").strip(),
                entrez_id=row.get("entrez gene id", "").strip(),
                fonte="genage",
            )
            if entry.symbol:
                entries.append(entry)

    logger.info("GenAge: %d genes carregados", len(entries))
    return entries


def construir_dicionario() -> dict[str, GeneEntry]:
    """Constroi dicionario completo de genes/proteinas do envelhecimento.

    Combina:
    1. GenAge (307 genes)
    2. Alvos curados (15 alvos-chave com Ensembl IDs)
    3. Aliases e sinonimos comuns

    Returns:
        Dict de termo_busca (lowercase) -> GeneEntry.
    """
    dicionario: dict[str, GeneEntry] = {}

    # 1. Carregar GenAge
    genage = carregar_genage()
    for entry in genage:
        key = entry.symbol.upper()
        dicionario[key] = entry

    # 2. Alvos curados (com Ensembl IDs e vias)
    # Importar do drugbank.py
    from src.ingestion.drugbank import ALVOS_ENVELHECIMENTO

    for alvo in ALVOS_ENVELHECIMENTO:
        symbol = alvo["gene"]
        if symbol in dicionario:
            # Enriquecer com Ensembl ID e via
            dicionario[symbol].ensembl_id = alvo["ensembl"]
            dicionario[symbol].via = alvo["via"]
        else:
            dicionario[symbol] = GeneEntry(
                symbol=symbol,
                nome=alvo["nome"],
                ensembl_id=alvo["ensembl"],
                via=alvo.get("via", ""),
                fonte="curado",
            )

    # 3. Aliases comuns (proteinas mencionadas por nome, nao por simbolo)
    _ALIASES: dict[str, list[str]] = {
        "MTOR": ["mTOR", "mechanistic target of rapamycin", "FRAP1", "FRAP", "RAFT1"],
        "SIRT1": ["sirtuin 1", "sirtuin-1", "SIR2L1", "Sir2"],
        "SIRT3": ["sirtuin 3", "sirtuin-3"],
        "SIRT6": ["sirtuin 6", "sirtuin-6"],
        "FOXO3": ["FOXO3A", "FOXO3a", "forkhead box O3"],
        "PRKAA1": ["AMPK", "AMP-activated protein kinase", "AMPKalpha1", "AMPK-alpha"],
        "KL": ["klotho", "alpha-klotho", "alpha klotho"],
        "TP53": ["p53", "tumor protein p53"],
        "CDKN2A": ["p16", "p16INK4a", "p16-INK4a", "INK4a"],
        "CDKN1A": ["p21", "p21CIP1", "p21-CIP1", "WAF1"],
        "TERT": ["telomerase", "hTERT", "telomerase reverse transcriptase"],
        "TERC": ["telomerase RNA", "hTERC", "TERC"],
        "NAMPT": ["visfatin", "PBEF", "nicotinamide phosphoribosyltransferase"],
        "ATG5": ["autophagy related 5", "ATG-5"],
        "ATG7": ["autophagy related 7"],
        "BECN1": ["beclin 1", "beclin-1", "Beclin1"],
        "BCL2": ["Bcl-2", "B-cell lymphoma 2", "BCL-2"],
        "LMNA": ["lamin A", "lamin A/C", "lamin-A", "progerin"],
        "GDF11": ["growth differentiation factor 11", "BMP11"],
        "IGF1": ["insulin-like growth factor 1", "IGF-1", "somatomedin C"],
        "IGF1R": ["IGF-1R", "IGF1 receptor", "insulin-like growth factor 1 receptor"],
        "INSR": ["insulin receptor"],
        "GH1": ["growth hormone", "somatotropin"],
        "GHR": ["growth hormone receptor"],
        "NFE2L2": ["NRF2", "Nrf2", "nuclear factor erythroid 2"],
        "NFKB1": ["NF-kB", "NF-kappaB", "NFkB", "nuclear factor kappa B"],
        "TNF": ["TNF-alpha", "TNFalpha", "tumor necrosis factor"],
        "IL6": ["interleukin 6", "interleukin-6", "IL-6"],
        "IL1B": ["interleukin 1 beta", "interleukin-1beta", "IL-1beta", "IL-1B"],
        "PPARGC1A": ["PGC-1alpha", "PGC1alpha", "PGC-1a", "PPARGC1A"],
        "SOD2": ["MnSOD", "manganese superoxide dismutase", "SOD-2"],
        "CAT": ["catalase"],
        "GPX1": ["glutathione peroxidase", "GPx1"],
        "HSPA1A": ["HSP70", "Hsp70", "heat shock protein 70"],
        "HSP90AA1": ["HSP90", "Hsp90", "heat shock protein 90"],
        "UBB": ["ubiquitin"],
        "PSEN1": ["presenilin 1", "presenilin-1"],
        "APP": ["amyloid precursor protein", "APP"],
        "APOE": ["apolipoprotein E", "ApoE", "APOE4", "APOE2"],
        "WRN": ["Werner syndrome", "Werner helicase", "WRN helicase"],
        "ERCC2": ["XPD", "xeroderma pigmentosum D"],
        "BLM": ["Bloom syndrome", "BLM helicase"],
    }

    for symbol, aliases in _ALIASES.items():
        if symbol not in dicionario:
            dicionario[symbol] = GeneEntry(symbol=symbol, fonte="alias")
        dicionario[symbol].aliases = aliases
        # Adicionar aliases como entradas que apontam para o gene principal
        for alias in aliases:
            alias_key = alias.upper()
            if alias_key not in dicionario:
                dicionario[alias_key] = dicionario[symbol]

    # 4. Compostos geroprotetores (nao sao genes, mas sao alvos de busca)
    _COMPOSTOS: dict[str, list[str]] = {
        "_RAPAMYCIN": ["rapamycin", "sirolimus", "rapamicin"],
        "_METFORMIN": ["metformin", "metformina"],
        "_RESVERATROL": ["resveratrol"],
        "_QUERCETIN": ["quercetin", "quercetina"],
        "_DASATINIB": ["dasatinib"],
        "_SPERMIDINE": ["spermidine", "spermidina"],
        "_NR": ["nicotinamide riboside", "NR"],
        "_NMN": ["nicotinamide mononucleotide", "NMN"],
        "_NAVITOCLAX": ["navitoclax", "ABT-263", "ABT263"],
        "_FISETIN": ["fisetin", "fisetina"],
        "_ACARBOSE": ["acarbose", "acarbosa"],
        "_NAD": ["NAD+", "NAD(+)", "nicotinamide adenine dinucleotide"],
    }

    for comp_key, aliases in _COMPOSTOS.items():
        entry = GeneEntry(symbol=comp_key, nome=aliases[0], aliases=aliases, fonte="composto")
        dicionario[comp_key] = entry
        for alias in aliases:
            dicionario[alias.upper()] = entry

    logger.info("Dicionario total: %d entradas unicas", len(set(id(v) for v in dicionario.values())))
    return dicionario


def extrair_genes_de_texto(
    texto: str,
    dicionario: dict[str, GeneEntry],
) -> dict[str, int]:
    """Extrai genes/proteinas de um texto usando dicionario.

    Args:
        texto: Texto para busca (titulo + abstract + keywords).
        dicionario: Dicionario de genes (de construir_dicionario()).

    Returns:
        Dict de gene_symbol -> contagem de mencoes.
    """
    contagens: dict[str, int] = {}
    texto_upper = texto.upper()

    # Agrupar por gene principal (resolver aliases)
    gene_principal: dict[str, GeneEntry] = {}
    for key, entry in dicionario.items():
        gene_principal[key] = entry

    # Buscar cada termo no texto
    termos_buscados: set[str] = set()
    for key, entry in dicionario.items():
        symbol = entry.symbol

        # Buscar o symbol principal
        if symbol not in termos_buscados:
            termos_buscados.add(symbol)
            # Gene symbols: busca exata com word boundary
            if not symbol.startswith("_"):
                pattern = r'\b' + re.escape(symbol) + r'\b'
                matches = len(re.findall(pattern, texto))
                if matches > 0:
                    contagens[symbol] = contagens.get(symbol, 0) + matches

        # Buscar aliases
        for alias in entry.aliases:
            alias_upper = alias.upper()
            if alias_upper in termos_buscados:
                continue
            termos_buscados.add(alias_upper)

            # Case insensitive para nomes longos, case sensitive para simbolos curtos
            if len(alias) <= 4:
                pattern = r'\b' + re.escape(alias) + r'\b'
                matches = len(re.findall(pattern, texto))
            else:
                pattern = r'\b' + re.escape(alias) + r'\b'
                matches = len(re.findall(pattern, texto, re.IGNORECASE))

            if matches > 0:
                contagens[symbol] = contagens.get(symbol, 0) + matches

    return contagens


def extrair_de_papers(
    papers_path: Path,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    """Executa extracao de genes em todos os papers.

    Args:
        papers_path: Caminho do JSON de papers enriquecidos.
        output_dir: Diretorio de output (padrao: data/processed/).

    Returns:
        Dict com estatisticas e ranking.
    """
    audit = AuditLogger(modulo="extracao_proteinas")
    audit.registrar_input(papers_path)

    if output_dir is None:
        output_dir = DATA_DIR / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Carregar papers
    with open(papers_path, "r", encoding="utf-8") as f:
        papers = json.load(f)
    logger.info("Carregados %d papers", len(papers))

    # Construir dicionario
    dicionario = construir_dicionario()

    # Extrair de cada paper
    resultados: list[ExtractionResult] = []
    contagem_global: Counter = Counter()
    papers_por_gene: Counter = Counter()

    for paper in papers:
        # Combinar titulo + abstract + keywords para busca
        texto = " ".join([
            paper.get("titulo", ""),
            paper.get("abstract", ""),
            " ".join(paper.get("keywords", [])),
        ])

        contagens = extrair_genes_de_texto(texto, dicionario)

        resultado = ExtractionResult(
            doi=paper.get("doi", ""),
            titulo=paper.get("titulo", ""),
            genes_encontrados=list(contagens.keys()),
            contagens=contagens,
        )
        resultados.append(resultado)

        for gene, count in contagens.items():
            contagem_global[gene] += count
            papers_por_gene[gene] += 1

    # Ranking de genes por numero de papers (nao por contagem bruta)
    ranking = sorted(
        papers_por_gene.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    # Top 50
    top50 = ranking[:50]

    # Separar genes de compostos
    genes_top50 = [(g, c) for g, c in top50 if not g.startswith("_")]
    compostos_top = [(g.lstrip("_"), c) for g, c in top50 if g.startswith("_")]

    # Construir output detalhado do ranking
    ranking_detalhado = []
    for gene, n_papers in ranking:
        entry = dicionario.get(gene)
        ranking_detalhado.append({
            "rank": len(ranking_detalhado) + 1,
            "symbol": gene,
            "nome": entry.nome if entry else "",
            "papers_mencionando": n_papers,
            "mencoes_totais": contagem_global[gene],
            "ensembl_id": entry.ensembl_id if entry else "",
            "uniprot_id": entry.uniprot_id if entry else "",
            "via": entry.via if entry else "",
            "fonte": entry.fonte if entry else "",
        })

    # Salvar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 1. Ranking completo
    ranking_path = output_dir / f"protein_ranking_{timestamp}.json"
    with open(ranking_path, "w", encoding="utf-8") as f:
        json.dump(ranking_detalhado, f, ensure_ascii=False, indent=2)
    audit.registrar_output(ranking_path)

    # 2. Extracao por paper
    extraction_path = output_dir / f"protein_extraction_{timestamp}.json"
    extraction_data = [r.to_dict() for r in resultados]
    with open(extraction_path, "w", encoding="utf-8") as f:
        json.dump(extraction_data, f, ensure_ascii=False, indent=2)
    audit.registrar_output(extraction_path)

    # Estatisticas
    papers_com_genes = sum(1 for r in resultados if r.genes_encontrados)
    total_genes_unicos = len(contagem_global)

    estatisticas = {
        "total_papers": len(papers),
        "papers_com_genes": papers_com_genes,
        "cobertura": round(papers_com_genes / len(papers) * 100, 1) if papers else 0,
        "genes_unicos_encontrados": total_genes_unicos,
        "genes_genage_encontrados": sum(
            1 for g in contagem_global if dicionario.get(g, GeneEntry()).fonte == "genage"
        ),
        "top_50_genes": [(g, c) for g, c in genes_top50[:50]],
        "top_compostos": compostos_top[:15],
        "arquivo_ranking": ranking_path.name,
        "arquivo_extracao": extraction_path.name,
    }

    audit.registrar_contagens(
        lidos=len(papers),
        validos=papers_com_genes,
        processados=papers_com_genes,
        rejeitados=len(papers) - papers_com_genes,
    )
    audit.adicionar_metadado("estatisticas", estatisticas)
    audit.finalizar(status="SUCESSO")

    logger.info("=" * 60)
    logger.info("EXTRACAO DE PROTEINAS CONCLUIDA")
    logger.info("Papers: %d | Com genes: %d (%.1f%%)",
                len(papers), papers_com_genes, estatisticas["cobertura"])
    logger.info("Genes unicos: %d", total_genes_unicos)
    logger.info("TOP 15 GENES (por n. papers):")
    for gene, n_papers in genes_top50[:15]:
        entry = dicionario.get(gene, GeneEntry())
        logger.info("  %s (%s): %d papers", gene, entry.nome[:40], n_papers)
    logger.info("TOP 10 COMPOSTOS:")
    for comp, n_papers in compostos_top[:10]:
        logger.info("  %s: %d papers", comp, n_papers)
    logger.info("=" * 60)

    return estatisticas


if __name__ == "__main__":
    import sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    processed_dir = DATA_DIR / "processed"
    enriched_files = sorted(processed_dir.glob("papers_enriched_fase1_*.json"))
    if not enriched_files:
        # Fallback para papers nao-enriquecidos
        enriched_files = sorted(processed_dir.glob("papers_fase1_*.json"))

    if not enriched_files:
        logger.error("Nenhum arquivo de papers encontrado")
        sys.exit(1)

    input_path = enriched_files[-1]
    logger.info("Usando: %s", input_path.name)

    resultado = extrair_de_papers(input_path)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
