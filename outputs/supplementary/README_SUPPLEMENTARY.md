# Supplementary Material

**Paper:** Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis

**Author:** Tercio S. Azevedo

---

## Contents

| File | Description |
|------|-------------|
| `Table_S1_full_ranking.csv` | Complete ranking of all 162 drug candidates with scores and features |
| `Table_S2_search_queries.md` | PubMed search queries and inclusion/exclusion criteria |
| `Table_S3_bootstrap_top20.csv` | Bootstrap stability results for top 20 compounds (n=1,000) |
| `Table_S4_ablation_results.csv` | Ablation study results: rank changes per feature removal |
| `Table_S5_sensitivity_configs.csv` | Sensitivity analysis: 5 weight configurations and resulting ranks |
| `Table_S6_graph_metrics.csv` | Knowledge graph centrality metrics for top protein targets |
| `Table_S7_aging_targets.csv` | Top 50 aging targets with Ensembl IDs and literature frequency |
| `Figure_S1_external_validation_benchmark.png` | External validation against DrugAge + benchmark comparison (4 panels) |
| `Figure_S2_mechanistic_network.png` | Mechanistic interpretation: drugs -> targets -> hallmarks of aging network |

## Data Availability

- **Code:** https://github.com/terciosilas/discovery-engine (MIT License)
- **Raw data:** All processed JSON files available in `data/processed/`
- **Reproducibility:** Pipeline deterministic with `seed=42`; all inputs/outputs tracked via SHA-256 checksums

## Data Sources

| Source | Version | Access | Records Used |
|--------|---------|--------|--------------|
| PubMed | E-utilities API | Public | 376 papers |
| Semantic Scholar | Batch API v1 | Public | 356 enriched |
| GenAge | Build 21 | Public | 307 genes |
| Open Targets | GraphQL API 2024 | Public | 1,118 associations |
| ChEMBL | REST API v33 | Public | 7 activity records |
| DrugAge | Build 5 | Public | 1,046 compounds |
| Unpaywall | REST API | Public | 280 OA papers |
