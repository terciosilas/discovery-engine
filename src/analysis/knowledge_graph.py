"""Grafo de Conhecimento do Discovery Engine.

Constroi grafo multipartido: Proteina <-> Droga <-> Doenca
usando NetworkX. Calcula metricas de centralidade e identifica
clusters/comunidades.
"""

import json
import logging
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import networkx as nx

from src.core.audit import AuditLogger

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


@dataclass
class GraphStats:
    """Estatisticas do grafo."""

    n_nos: int = 0
    n_arestas: int = 0
    n_proteinas: int = 0
    n_drogas: int = 0
    n_doencas: int = 0
    densidade: float = 0.0
    componentes_conectados: int = 0
    maior_componente: int = 0

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "n_nos": self.n_nos,
            "n_arestas": self.n_arestas,
            "n_proteinas": self.n_proteinas,
            "n_drogas": self.n_drogas,
            "n_doencas": self.n_doencas,
            "densidade": round(self.densidade, 6),
            "componentes_conectados": self.componentes_conectados,
            "maior_componente": self.maior_componente,
        }


def construir_grafo(
    associacoes_path: Path,
    candidatos_path: Path,
    alvos_path: Path,
) -> nx.Graph:
    """Constroi grafo de conhecimento a partir dos dados coletados.

    Nos:
        - Proteinas (tipo='protein', cor=azul)
        - Drogas (tipo='drug', cor=verde se geroprotetor, vermelho se nao)
        - Doencas (tipo='disease', cor=laranja)

    Arestas:
        - protein-drug: associacao droga-alvo (peso = fase clinica)
        - drug-disease: indicacao (peso = fase clinica)

    Args:
        associacoes_path: JSON de associacoes Open Targets.
        candidatos_path: JSON de candidatos consolidados.
        alvos_path: JSON de alvos consolidados.

    Returns:
        Grafo NetworkX.
    """
    # Carregar dados
    with open(associacoes_path, "r", encoding="utf-8") as f:
        associacoes = json.load(f)
    with open(candidatos_path, "r", encoding="utf-8") as f:
        candidatos = json.load(f)
    with open(alvos_path, "r", encoding="utf-8") as f:
        alvos = json.load(f)

    G = nx.Graph()

    # Indexar candidatos por drug_id
    candidatos_idx = {c["drug_id"]: c for c in candidatos}
    alvos_idx = {a["symbol"]: a for a in alvos}

    # 1. Adicionar nos de proteinas
    for alvo in alvos:
        node_id = f"protein:{alvo['symbol']}"
        G.add_node(
            node_id,
            tipo="protein",
            label=alvo["symbol"],
            nome=alvo.get("nome", ""),
            ensembl_id=alvo.get("ensembl_id", ""),
            papers_mencionando=alvo.get("papers_mencionando", 0),
            via=alvo.get("via", ""),
        )

    # 2. Adicionar nos de drogas e arestas protein-drug
    drogas_adicionadas = set()
    doencas_adicionadas = set()

    for assoc in associacoes:
        drug_id = assoc.get("drug_id", "")
        drug_nome = assoc.get("drug_nome", "")
        target_gene = assoc.get("target_gene", "")
        disease_nome = assoc.get("disease_nome", "")
        fase = assoc.get("fase_clinica", 0)

        if not drug_id or not target_gene:
            continue

        # No de droga
        drug_node = f"drug:{drug_id}"
        if drug_id not in drogas_adicionadas:
            cand = candidatos_idx.get(drug_id, {})
            G.add_node(
                drug_node,
                tipo="drug",
                label=drug_nome,
                drug_id=drug_id,
                max_fase=cand.get("max_fase_clinica", fase),
                geroprotetor=cand.get("geroprotetor_conhecido", False),
                lifespan_efeito=cand.get("lifespan_efeito", 0.0),
                pchembl=cand.get("pchembl_melhor", 0.0),
                n_alvos=len(cand.get("alvos", [])),
            )
            drogas_adicionadas.add(drug_id)

        # Aresta protein-drug
        protein_node = f"protein:{target_gene}"
        if G.has_node(protein_node):
            moa = assoc.get("mecanismo_acao", "")
            tipo_acao = assoc.get("tipo_acao", "")
            G.add_edge(
                protein_node, drug_node,
                tipo="targets",
                fase_clinica=fase,
                mecanismo=moa,
                acao=tipo_acao,
                weight=max(1, fase),
            )

        # No de doenca e aresta drug-disease
        if disease_nome:
            disease_node = f"disease:{disease_nome}"
            if disease_nome not in doencas_adicionadas:
                G.add_node(
                    disease_node,
                    tipo="disease",
                    label=disease_nome,
                    disease_id=assoc.get("disease_id", ""),
                )
                doencas_adicionadas.add(disease_nome)

            G.add_edge(
                drug_node, disease_node,
                tipo="indication",
                fase_clinica=fase,
                weight=max(1, fase),
            )

    # 3. Adicionar geroprotetores que nao foram conectados via Open Targets
    for cand in candidatos:
        drug_id = cand["drug_id"]
        drug_node = f"drug:{drug_id}"
        if not G.has_node(drug_node):
            G.add_node(
                drug_node,
                tipo="drug",
                label=cand["nome"],
                drug_id=drug_id,
                max_fase=cand.get("max_fase_clinica", 0),
                geroprotetor=cand.get("geroprotetor_conhecido", False),
                lifespan_efeito=cand.get("lifespan_efeito", 0.0),
                pchembl=cand.get("pchembl_melhor", 0.0),
                n_alvos=len(cand.get("alvos", [])),
            )

    logger.info(
        "Grafo construido: %d nos, %d arestas",
        G.number_of_nodes(), G.number_of_edges(),
    )
    return G


def calcular_metricas(G: nx.Graph) -> dict[str, Any]:
    """Calcula metricas de centralidade e estruturais no grafo.

    Args:
        G: Grafo NetworkX.

    Returns:
        Dict com metricas globais e por no.
    """
    # Metricas globais
    proteinas = [n for n, d in G.nodes(data=True) if d.get("tipo") == "protein"]
    drogas = [n for n, d in G.nodes(data=True) if d.get("tipo") == "drug"]
    doencas = [n for n, d in G.nodes(data=True) if d.get("tipo") == "disease"]

    stats = GraphStats(
        n_nos=G.number_of_nodes(),
        n_arestas=G.number_of_edges(),
        n_proteinas=len(proteinas),
        n_drogas=len(drogas),
        n_doencas=len(doencas),
        densidade=nx.density(G),
    )

    # Componentes conectados
    if G.number_of_nodes() > 0:
        componentes = list(nx.connected_components(G))
        stats.componentes_conectados = len(componentes)
        stats.maior_componente = max(len(c) for c in componentes) if componentes else 0

    # Centralidade de grau
    degree_centrality = nx.degree_centrality(G)

    # Betweenness centrality (pode ser lento em grafos grandes)
    betweenness = nx.betweenness_centrality(G) if G.number_of_nodes() < 5000 else {}

    # Closeness centrality
    closeness = nx.closeness_centrality(G) if G.number_of_nodes() < 5000 else {}

    # Top proteinas por centralidade
    protein_centrality = sorted(
        [(n, degree_centrality[n]) for n in proteinas if n in degree_centrality],
        key=lambda x: x[1],
        reverse=True,
    )

    # Top drogas por centralidade
    drug_centrality = sorted(
        [(n, degree_centrality[n]) for n in drogas if n in degree_centrality],
        key=lambda x: x[1],
        reverse=True,
    )

    # Drogas com mais conexoes a proteinas do envelhecimento
    drug_aging_connections: dict[str, int] = {}
    for drug_node in drogas:
        neighbors = list(G.neighbors(drug_node))
        n_protein_neighbors = sum(
            1 for n in neighbors if G.nodes[n].get("tipo") == "protein"
        )
        drug_aging_connections[drug_node] = n_protein_neighbors

    drug_aging_rank = sorted(
        drug_aging_connections.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    metricas = {
        "global": stats.to_dict(),
        "top_proteinas_centralidade": [
            {
                "node": n,
                "label": G.nodes[n].get("label", ""),
                "degree_centrality": round(dc, 4),
                "betweenness": round(betweenness.get(n, 0), 4),
                "closeness": round(closeness.get(n, 0), 4),
                "grau": G.degree(n),
            }
            for n, dc in protein_centrality[:20]
        ],
        "top_drogas_centralidade": [
            {
                "node": n,
                "label": G.nodes[n].get("label", ""),
                "degree_centrality": round(dc, 4),
                "betweenness": round(betweenness.get(n, 0), 4),
                "n_alvos_envelhecimento": drug_aging_connections.get(n, 0),
                "geroprotetor": G.nodes[n].get("geroprotetor", False),
                "lifespan_efeito": G.nodes[n].get("lifespan_efeito", 0),
                "grau": G.degree(n),
            }
            for n, dc in drug_centrality[:30]
        ],
        "top_drogas_aging_connections": [
            {
                "node": n,
                "label": G.nodes[n].get("label", ""),
                "n_alvos_envelhecimento": count,
                "geroprotetor": G.nodes[n].get("geroprotetor", False),
                "max_fase": G.nodes[n].get("max_fase", 0),
            }
            for n, count in drug_aging_rank[:30] if count > 0
        ],
    }

    logger.info("Metricas calculadas para %d nos", G.number_of_nodes())
    return metricas


def detectar_comunidades(G: nx.Graph) -> dict[str, Any]:
    """Detecta comunidades/clusters no grafo.

    Usa algoritmo de Louvain (greedy modularity) disponivel no NetworkX.

    Args:
        G: Grafo NetworkX.

    Returns:
        Dict com comunidades e seus membros.
    """
    if G.number_of_nodes() == 0:
        return {"n_comunidades": 0, "comunidades": []}

    # Greedy modularity communities
    from networkx.algorithms.community import greedy_modularity_communities

    communities = list(greedy_modularity_communities(G))

    resultado = {
        "n_comunidades": len(communities),
        "comunidades": [],
    }

    for i, community in enumerate(communities):
        membros = list(community)
        tipos = Counter(G.nodes[n].get("tipo", "") for n in membros)
        proteinas = [
            G.nodes[n].get("label", n) for n in membros
            if G.nodes[n].get("tipo") == "protein"
        ]
        drogas = [
            G.nodes[n].get("label", n) for n in membros
            if G.nodes[n].get("tipo") == "drug"
        ]
        geroprotetores = [
            G.nodes[n].get("label", n) for n in membros
            if G.nodes[n].get("geroprotetor", False)
        ]

        resultado["comunidades"].append({
            "id": i,
            "tamanho": len(membros),
            "tipos": dict(tipos),
            "proteinas": proteinas[:15],
            "drogas_exemplo": drogas[:10],
            "geroprotetores": geroprotetores,
        })

    # Ordenar por tamanho
    resultado["comunidades"].sort(key=lambda c: c["tamanho"], reverse=True)

    logger.info("Detectadas %d comunidades", len(communities))
    return resultado


def executar_pipeline_grafo(
    output_dir: Path | None = None,
) -> dict[str, Any]:
    """Executa pipeline completo do grafo de conhecimento.

    Args:
        output_dir: Diretorio de output.

    Returns:
        Estatisticas.
    """
    audit = AuditLogger(modulo="knowledge_graph")

    if output_dir is None:
        output_dir = DATA_DIR / "processed"

    processed_dir = DATA_DIR / "processed"

    # Localizar arquivos mais recentes
    assoc_files = sorted(processed_dir.glob("drug_target_associations_*.json"))
    cand_files = sorted(processed_dir.glob("drug_candidates_*.json"))
    alvos_files = sorted(processed_dir.glob("top50_alvos_consolidados_*.json"))

    if not assoc_files or not cand_files or not alvos_files:
        logger.error("Arquivos de input nao encontrados")
        return {"erro": "Arquivos de input nao encontrados"}

    assoc_path = assoc_files[-1]
    cand_path = cand_files[-1]
    alvos_path = alvos_files[-1]

    audit.registrar_input(assoc_path)
    audit.registrar_input(cand_path)
    audit.registrar_input(alvos_path)

    # 1. Construir grafo
    G = construir_grafo(assoc_path, cand_path, alvos_path)

    # 2. Calcular metricas
    metricas = calcular_metricas(G)

    # 3. Detectar comunidades
    comunidades = detectar_comunidades(G)

    # 4. Salvar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 4a. Grafo como adjacency list (para recarregar)
    grafo_path = output_dir / f"knowledge_graph_{timestamp}.json"
    grafo_data = nx.node_link_data(G)
    with open(grafo_path, "w", encoding="utf-8") as f:
        json.dump(grafo_data, f, ensure_ascii=False, indent=2)
    audit.registrar_output(grafo_path)

    # 4b. Metricas
    metricas_path = output_dir / f"graph_metrics_{timestamp}.json"
    with open(metricas_path, "w", encoding="utf-8") as f:
        json.dump(metricas, f, ensure_ascii=False, indent=2)
    audit.registrar_output(metricas_path)

    # 4c. Comunidades
    comunidades_path = output_dir / f"graph_communities_{timestamp}.json"
    with open(comunidades_path, "w", encoding="utf-8") as f:
        json.dump(comunidades, f, ensure_ascii=False, indent=2)
    audit.registrar_output(comunidades_path)

    # Log final
    global_stats = metricas.get("global", {})
    logger.info("=" * 60)
    logger.info("GRAFO DE CONHECIMENTO CONCLUIDO")
    logger.info("Nos: %d (proteinas=%d, drogas=%d, doencas=%d)",
                global_stats.get("n_nos", 0),
                global_stats.get("n_proteinas", 0),
                global_stats.get("n_drogas", 0),
                global_stats.get("n_doencas", 0))
    logger.info("Arestas: %d", global_stats.get("n_arestas", 0))
    logger.info("Componentes conectados: %d", global_stats.get("componentes_conectados", 0))
    logger.info("Maior componente: %d nos", global_stats.get("maior_componente", 0))
    logger.info("Comunidades detectadas: %d", comunidades.get("n_comunidades", 0))
    logger.info("")
    logger.info("TOP 5 PROTEINAS (centralidade de grau):")
    for p in metricas.get("top_proteinas_centralidade", [])[:5]:
        logger.info("  %s: grau=%d, centrality=%.4f, betweenness=%.4f",
                    p["label"], p["grau"], p["degree_centrality"], p["betweenness"])
    logger.info("")
    logger.info("TOP 10 DROGAS (mais conexoes a alvos do envelhecimento):")
    for d in metricas.get("top_drogas_aging_connections", [])[:10]:
        gero_mark = " [GEROPROTETOR]" if d["geroprotetor"] else ""
        logger.info("  %s: %d alvos, fase=%d%s",
                    d["label"], d["n_alvos_envelhecimento"], d["max_fase"], gero_mark)
    logger.info("=" * 60)

    audit.registrar_contagens(
        lidos=3,
        validos=global_stats.get("n_nos", 0),
        processados=global_stats.get("n_arestas", 0),
        rejeitados=0,
    )
    audit.adicionar_metadado("metricas_globais", global_stats)
    audit.adicionar_metadado("n_comunidades", comunidades.get("n_comunidades", 0))
    audit.finalizar(status="SUCESSO")

    return {
        **global_stats,
        "n_comunidades": comunidades.get("n_comunidades", 0),
        "arquivo_grafo": grafo_path.name,
        "arquivo_metricas": metricas_path.name,
        "arquivo_comunidades": comunidades_path.name,
    }


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    stats = executar_pipeline_grafo()
    print(json.dumps(stats, indent=2, ensure_ascii=False))
