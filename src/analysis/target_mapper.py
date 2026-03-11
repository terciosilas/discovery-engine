"""Mapeamento de alvos proteicos para IDs de bancos de dados.

Usa MyGene.info (API publica, sem auth) para mapear gene symbols para
Ensembl Gene IDs, UniProt IDs e Entrez Gene IDs.
Consolida o ranking de proteinas filtrando compostos e preenchendo IDs faltantes.
"""

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

from src.core.audit import AuditLogger

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

MYGENE_URL = "https://mygene.info/v3"
MIN_INTERVAL_S = 0.35  # MyGene.info: 3 requests/s free


@dataclass
class TargetInfo:
    """Informacoes consolidadas de um alvo proteico."""

    symbol: str = ""
    nome: str = ""
    ensembl_id: str = ""
    uniprot_id: str = ""
    entrez_id: str = ""
    papers_mencionando: int = 0
    mencoes_totais: int = 0
    via: str = ""
    fonte: str = ""
    rank_original: int = 0

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "symbol": self.symbol,
            "nome": self.nome,
            "ensembl_id": self.ensembl_id,
            "uniprot_id": self.uniprot_id,
            "entrez_id": self.entrez_id,
            "papers_mencionando": self.papers_mencionando,
            "mencoes_totais": self.mencoes_totais,
            "via": self.via,
            "fonte": self.fonte,
            "rank_original": self.rank_original,
        }


def buscar_mygene_batch(
    symbols: list[str],
    species: str = "human",
) -> dict[str, dict[str, Any]]:
    """Busca multiplos genes de uma vez no MyGene.info (POST /query).

    Args:
        symbols: Lista de gene symbols.
        species: Especie (padrao: human).

    Returns:
        Dict de symbol -> {ensembl_gene, uniprot, entrezgene, name}.
    """
    url = f"{MYGENE_URL}/query"
    resultados: dict[str, dict[str, Any]] = {}

    # MyGene aceita batch de ate 1000 genes via POST
    batch_size = 200
    for i in range(0, len(symbols), batch_size):
        batch = symbols[i:i + batch_size]
        query_str = ",".join(batch)

        params = {
            "q": query_str,
            "scopes": "symbol",
            "fields": "ensembl.gene,uniprot.Swiss-Prot,entrezgene,name,symbol",
            "species": species,
            "size": len(batch),
        }

        try:
            response = requests.post(url, data=params, timeout=30)
            if response.status_code == 429:
                logger.warning("MyGene rate limit. Aguardando 5s...")
                time.sleep(5)
                response = requests.post(url, data=params, timeout=30)

            response.raise_for_status()
            dados = response.json()

            if not isinstance(dados, list):
                dados = [dados]

            for item in dados:
                if item.get("notfound", False):
                    continue
                sym = item.get("symbol", item.get("query", "")).upper()
                if not sym:
                    continue

                # Extrair Ensembl Gene ID
                ensembl_raw = item.get("ensembl", {})
                ensembl_gene = ""
                if isinstance(ensembl_raw, list):
                    ensembl_gene = ensembl_raw[0].get("gene", "") if ensembl_raw else ""
                elif isinstance(ensembl_raw, dict):
                    ensembl_gene = ensembl_raw.get("gene", "")

                # Extrair UniProt
                uniprot_raw = item.get("uniprot", {})
                uniprot = ""
                if isinstance(uniprot_raw, dict):
                    sp = uniprot_raw.get("Swiss-Prot", "")
                    if isinstance(sp, list):
                        uniprot = sp[0] if sp else ""
                    else:
                        uniprot = sp

                resultados[sym] = {
                    "ensembl_gene": ensembl_gene,
                    "uniprot": uniprot,
                    "entrezgene": str(item.get("entrezgene", "")),
                    "name": item.get("name", ""),
                }

            logger.info("MyGene batch %d-%d: %d/%d encontrados",
                        i + 1, min(i + batch_size, len(symbols)),
                        len([s for s in batch if s.upper() in resultados]),
                        len(batch))

        except requests.RequestException as e:
            logger.error("Erro MyGene.info batch %d: %s", i, e)

        time.sleep(MIN_INTERVAL_S)

    return resultados


def consolidar_ranking(
    ranking_path: Path,
    output_dir: Path | None = None,
    top_n: int = 50,
) -> list[TargetInfo]:
    """Consolida ranking de proteinas: filtra compostos, mapeia IDs faltantes.

    Args:
        ranking_path: Caminho do JSON de ranking (de protein_extractor).
        output_dir: Diretorio de output (padrao: data/processed/).
        top_n: Numero de alvos no ranking final.

    Returns:
        Lista de TargetInfo consolidados.
    """
    audit = AuditLogger(modulo="target_mapper")
    audit.registrar_input(ranking_path)

    if output_dir is None:
        output_dir = DATA_DIR / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Carregar ranking
    with open(ranking_path, "r", encoding="utf-8") as f:
        ranking = json.load(f)
    logger.info("Ranking carregado: %d entradas", len(ranking))

    # Filtrar compostos (prefixo _)
    genes_only = [r for r in ranking if not r["symbol"].startswith("_")]
    logger.info("Genes (sem compostos): %d", len(genes_only))

    # Top N genes
    top_genes = genes_only[:top_n]

    # Identificar genes sem Ensembl ID
    sem_ensembl = [g["symbol"] for g in top_genes if not g.get("ensembl_id")]
    logger.info("Genes sem Ensembl ID: %d/%d", len(sem_ensembl), len(top_genes))

    # Buscar IDs faltantes via MyGene.info
    mygene_data: dict[str, dict[str, Any]] = {}
    if sem_ensembl:
        logger.info("Consultando MyGene.info para %d genes...", len(sem_ensembl))
        mygene_data = buscar_mygene_batch(sem_ensembl)
        logger.info("MyGene.info: %d/%d encontrados", len(mygene_data), len(sem_ensembl))

    # Construir lista consolidada
    alvos: list[TargetInfo] = []
    for i, gene in enumerate(top_genes):
        symbol = gene["symbol"]
        target = TargetInfo(
            symbol=symbol,
            nome=gene.get("nome", ""),
            ensembl_id=gene.get("ensembl_id", ""),
            uniprot_id=gene.get("uniprot_id", ""),
            entrez_id="",
            papers_mencionando=gene.get("papers_mencionando", 0),
            mencoes_totais=gene.get("mencoes_totais", 0),
            via=gene.get("via", ""),
            fonte=gene.get("fonte", ""),
            rank_original=gene.get("rank", i + 1),
        )

        # Preencher com dados do MyGene.info
        mg = mygene_data.get(symbol, {})
        if mg:
            if not target.ensembl_id and mg.get("ensembl_gene"):
                target.ensembl_id = mg["ensembl_gene"]
            if not target.uniprot_id and mg.get("uniprot"):
                target.uniprot_id = mg["uniprot"]
            if not target.entrez_id and mg.get("entrezgene"):
                target.entrez_id = mg["entrezgene"]
            if not target.nome and mg.get("name"):
                target.nome = mg["name"]

        alvos.append(target)

    # Re-numerar ranking
    for i, alvo in enumerate(alvos):
        alvo.rank_original = i + 1

    # Estatisticas
    com_ensembl = sum(1 for a in alvos if a.ensembl_id)
    com_uniprot = sum(1 for a in alvos if a.uniprot_id)
    com_entrez = sum(1 for a in alvos if a.entrez_id)

    # Salvar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"top{top_n}_alvos_consolidados_{timestamp}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump([a.to_dict() for a in alvos], f, ensure_ascii=False, indent=2)
    audit.registrar_output(output_path)

    # Log final
    logger.info("=" * 60)
    logger.info("CONSOLIDACAO DE ALVOS CONCLUIDA")
    logger.info("Total alvos: %d", len(alvos))
    logger.info("Com Ensembl ID: %d/%d (%.0f%%)", com_ensembl, len(alvos),
                com_ensembl / len(alvos) * 100 if alvos else 0)
    logger.info("Com UniProt ID: %d/%d (%.0f%%)", com_uniprot, len(alvos),
                com_uniprot / len(alvos) * 100 if alvos else 0)
    logger.info("Com Entrez ID: %d/%d (%.0f%%)", com_entrez, len(alvos),
                com_entrez / len(alvos) * 100 if alvos else 0)
    logger.info("Top 10:")
    for alvo in alvos[:10]:
        logger.info("  #%d %s (%d papers) ensembl=%s",
                    alvo.rank_original, alvo.symbol,
                    alvo.papers_mencionando, alvo.ensembl_id or "FALTANDO")
    logger.info("Salvo: %s", output_path.name)
    logger.info("=" * 60)

    audit.registrar_contagens(
        lidos=len(genes_only),
        validos=len(alvos),
        processados=com_ensembl,
        rejeitados=len(genes_only) - len(alvos),
    )
    audit.adicionar_metadado("cobertura_ensembl", f"{com_ensembl}/{len(alvos)}")
    audit.adicionar_metadado("cobertura_uniprot", f"{com_uniprot}/{len(alvos)}")
    audit.finalizar(status="SUCESSO")

    return alvos


if __name__ == "__main__":
    import sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    processed_dir = DATA_DIR / "processed"
    ranking_files = sorted(processed_dir.glob("protein_ranking_*.json"))

    if not ranking_files:
        logger.error("Nenhum arquivo de ranking encontrado")
        sys.exit(1)

    ranking_path = ranking_files[-1]
    logger.info("Usando: %s", ranking_path.name)

    alvos = consolidar_ranking(ranking_path, top_n=50)
    print(f"\nTotal: {len(alvos)} alvos consolidados")
    print(f"Com Ensembl ID: {sum(1 for a in alvos if a.ensembl_id)}")
