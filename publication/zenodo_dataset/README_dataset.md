# Discovery Engine Dataset

**Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis**

Tercio S. Azevedo (2026)

---

## Description

This dataset contains all processed data, validation results, and figures from the Discovery Engine project -- a computational pipeline that identifies geroprotective compound candidates by integrating multiple biological data sources into a knowledge graph.

The pipeline processes data from 6 public databases (PubMed, Semantic Scholar, GenAge, Open Targets, ChEMBL, DrugAge), constructs a multipartite knowledge graph (479 nodes, 898 edges), and ranks 162 drug candidates using a weighted multi-feature scoring system.

## Data Origin

All data was derived from publicly available sources:

| Source | Version | Access | Records |
|--------|---------|--------|---------|
| PubMed | E-utilities API | Public | 376 papers |
| Semantic Scholar | Batch API v1 | Public | 356 enriched |
| GenAge | Build 21 | Public | 307 genes |
| Open Targets | GraphQL API 2024 | Public | 1,118 associations |
| ChEMBL | REST API v33 | Public | 7 activity records |
| DrugAge | Build 5 | Public | 1,046 compounds |

Processing date: March 2026. Pipeline seed: 42 (deterministic).

## Directory Structure

```
zenodo_dataset/
  ranking/                     Final compound ranking
  validation/                  External validation against DrugAge
  mechanistic_analysis/        Hallmarks of aging mapping
  knowledge_graph/             Graph structure and metrics
  figures/                     Publication-quality figures (300 DPI)
  supplementary_tables/        All supplementary tables from the paper
```

## File Descriptions

### ranking/

| File | Description |
|------|-------------|
| `ranked_candidates_162.csv` | Complete ranking of all 162 drug candidates |

**Columns:**
- `Rank` -- Position in final ranking (1-162)
- `Compound` -- Drug compound name
- `ChEMBL_ID` -- ChEMBL database identifier
- `Score` -- Composite score (0-1, weighted sum of 6 features)
- `Phase` -- Maximum clinical trial phase (0-4)
- `Aging_Targets` -- Number of aging-related protein targets
- `Lifespan_Pct` -- Lifespan extension percentage from DrugAge (0 if no data)
- `pChEMBL` -- Binding potency (-log10 of IC50/Ki in M; 0 if no data)
- `Known_Geroprotector` -- Whether compound is a curated known geroprotector (True/False)
- `Mechanisms` -- Mechanism of action annotation
- `Sources` -- Data sources contributing to this compound's entry

### validation/

| File | Description |
|------|-------------|
| `drugage_validation.csv` | Cross-reference of 162 compounds against DrugAge database |
| `drugage_validation_figure.png` | Validation visualization (rank distribution, precision/recall, enrichment) |
| `drugage_validation_report.md` | Detailed validation report with statistical analysis |

**drugage_validation.csv columns:**
- `rank` -- Position in Discovery Engine ranking
- `composto` -- Compound name
- `score` -- Composite score
- `in_drugage` -- Whether found in DrugAge (True/False)
- `drugage_name` -- Matched name in DrugAge (if found)
- `drugage_studies` -- Number of DrugAge studies
- `drugage_species` -- Species tested
- `drugage_avg_lifespan_pct` -- Average lifespan change percentage
- `drugage_max_lifespan_pct` -- Maximum lifespan change
- `drugage_efeito_positivo` -- Positive lifespan effect (True/False)

### mechanistic_analysis/

| File | Description |
|------|-------------|
| `mechanistic_mapping.csv` | Top-20 compounds mapped to hallmarks of aging |
| `mechanistic_network.png` | Network visualization: drugs -> targets -> hallmarks |
| `mechanistic_report.md` | Detailed mechanistic interpretation report |

**mechanistic_mapping.csv columns:**
- `rank` -- Position in ranking
- `composto` -- Compound name
- `score` -- Composite score
- `fase_clinica` -- Clinical trial phase
- `lifespan_pct` -- Lifespan extension percentage
- `mecanismos` -- Mechanism of action
- `alvos` -- Molecular targets (comma-separated gene symbols)
- `pathways` -- Key pathways affected
- `hallmarks` -- Hallmarks of aging covered
- `n_hallmarks` -- Number of hallmarks
- `fontes` -- Data sources

### knowledge_graph/

| File | Description |
|------|-------------|
| `knowledge_graph.json` | Complete graph structure (nodes and edges) |
| `graph_metrics.json` | Centrality metrics for all nodes |
| `graph_communities.json` | Community detection results |

**knowledge_graph.json structure:**
- `nodes` -- Array of graph nodes with attributes:
  - `id` -- Node identifier
  - `type` -- Node type: "protein", "drug", or "disease"
  - `attributes` -- Type-specific attributes
- `edges` -- Array of edges with:
  - `source` -- Source node ID
  - `target` -- Target node ID
  - `type` -- Edge type: "drug_target" or "drug_disease"
  - `weight` -- Edge weight (clinical phase)
- `summary` -- Graph-level statistics (node counts, edge counts, density)

### figures/

| File | Description |
|------|-------------|
| `fig1_pipeline_overview.png` | Pipeline architecture overview |
| `fig2_top20_ranking.png` | Top-20 compound ranking bar chart |
| `fig3_bootstrap_stability.png` | Bootstrap stability analysis (n=1,000) |
| `fig4_ablation_study.png` | Feature ablation study |
| `fig5_sensitivity_analysis.png` | Weight sensitivity analysis |
| `Figure_S1_external_validation_benchmark.png` | DrugAge validation + benchmark (4 panels) |
| `Figure_S2_mechanistic_network.png` | Mechanistic network: drugs -> targets -> hallmarks |

All figures are 300 DPI, suitable for print publication.

### supplementary_tables/

| File | Description |
|------|-------------|
| `Table_S1_full_ranking.csv` | Complete ranking (same as ranking/ranked_candidates_162.csv) |
| `Table_S2_search_queries.md` | PubMed search strategies and filtering criteria |
| `Table_S3_bootstrap_top20.csv` | Bootstrap results: mean rank, std, CI for top 20 |
| `Table_S4_ablation_results.csv` | Ablation study: rank impact per feature removal |
| `Table_S5_sensitivity_configs.csv` | 5 weight configurations and resulting ranks |
| `Table_S6_graph_metrics.csv` | Knowledge graph centrality metrics |
| `Table_S7_aging_targets.csv` | Top 50 aging targets with Ensembl IDs |

## Usage

### Loading the ranking in Python

```python
import csv

with open("ranking/ranked_candidates_162.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"#{row['Rank']} {row['Compound']}: score={row['Score']}")
```

### Loading the knowledge graph in Python

```python
import json
import networkx as nx

with open("knowledge_graph/knowledge_graph.json") as f:
    data = json.load(f)

G = nx.Graph()
for node in data["nodes"]:
    G.add_node(node["id"], **node.get("attributes", {}), type=node["type"])
for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"], type=edge["type"], weight=edge.get("weight", 1))

print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
```

## Reproducibility

- Pipeline code: https://github.com/terciosilas/discovery-engine
- All results are deterministic with `seed=42`
- SHA-256 checksums for all inputs/outputs are recorded in `audit_logs/`

## License

This dataset is released under the Creative Commons Attribution 4.0 International License (CC-BY-4.0).

## Citation

```
Azevedo, T.S. (2026). Discovery Engine Dataset: Computational Identification of
Geroprotective Compound Candidates [Data set]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

## Contact

Tercio S. Azevedo -- tercio@callamarys.com.br
