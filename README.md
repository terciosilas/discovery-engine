# Discovery Engine

**Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis**

Tercio S. Azevedo | Independent Researcher | Sao Carlos, SP, Brazil

---

## Overview

Discovery Engine is an open-source computational pipeline that identifies geroprotective compound candidates by integrating multiple biological data sources into a knowledge graph and scoring drugs based on their aging-relevant properties.

The pipeline processes data from 6 public databases, constructs a multipartite knowledge graph (479 nodes, 898 edges), and ranks 162 drug candidates using a weighted multi-feature scoring system.

## Scientific Objective

Systematic identification of FDA-approved or clinically tested drugs with potential geroprotective (aging-delaying) properties, prioritized for repurposing in aging-focused clinical studies.

## Pipeline Overview

```
PubMed (376 papers)
     |
     v
Protein Extraction (GenAge, 307 genes)
     |
     v
Target Mapping (Open Targets, 1,118 associations)
     |
     v
Drug-Target Linking (ChEMBL, DrugAge)
     |
     v
Knowledge Graph (NetworkX: 50 proteins, 162 drugs, 267 diseases)
     |
     v
Candidate Scoring (6 features, weighted sum)
     |
     v
Statistical Validation (bootstrap, ablation, negative controls)
     |
     v
External Validation (DrugAge, pathway enrichment, benchmark)
     |
     v
Ranked Candidates + Paper Draft
```

## Key Results

- **Rapamycin** (rank #1) and **Metformin** (rank #10) correctly identified as top geroprotectors
- **Bootstrap stability:** Rapamycin rank #1 with zero variance (n=1,000)
- **Pathway enrichment:** 11/11 aging pathway categories significantly enriched (top hit: "Longevity regulating pathway", p=1.27e-20)
- **External validation:** 4.42x enrichment of DrugAge compounds in top-20 (Mann-Whitney p=1.59e-3)
- **Novel candidates:** Bezafibrate (PPAR agonist, +13% lifespan), Bardoxolone methyl (NRF2 activator), Venetoclax (BCL-2 senolytic)
- **Zero false positives** among 10 negative controls

## Data Sources

| Source | Version | Records |
|--------|---------|---------|
| PubMed | E-utilities API | 376 papers |
| Semantic Scholar | Batch API v1 | 356 enriched |
| GenAge | Build 21 | 307 genes |
| Open Targets | GraphQL API 2024 | 1,118 associations |
| ChEMBL | REST API v33 | 7 activity records |
| DrugAge | Build 5 | 1,046 compounds |

## Reproducing the Analysis

### Prerequisites

- Python 3.10+
- Internet connection (for API queries)

### Setup

```bash
git clone https://github.com/terciosilas/discovery-engine.git
cd discovery-engine
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Running the Pipeline

The pipeline runs in sequential phases. Each phase produces outputs in `data/processed/` and `results/`.

```bash
# Phase 1: Literature search and ingestion
python -m src.ingestion.orquestrador

# Phase 2: Analysis and scoring
python -m src.analysis.protein_extractor data/processed/papers_enriched_fase1_*.json
python -m src.analysis.target_mapper data/processed/protein_ranking_*.json data/processed/
python -m src.analysis.drug_target_linker data/processed/top50_alvos_consolidados_*.json data/processed/
python -m src.analysis.knowledge_graph data/processed/drug_candidates_*.json data/processed/drug_target_associations_*.json data/processed/
python -m src.analysis.candidate_scorer data/processed/drug_candidates_*.json data/processed/knowledge_graph_*.json data/processed/

# Phase 3: Validation
python -m src.validation.computational data/processed/ranked_candidates_*.json results/

# Phase 4: Extended validation and analysis
python -m src.validation.benchmark data/processed/ranked_candidates_*.json outputs/model_benchmark/
python -m src.validation.external_drugage data/processed/ranked_candidates_*.json results/external_validation_drugage/
python -m src.analysis.pathway_enrichment data/processed/ranked_candidates_*.json outputs/pathway_enrichment/
python -m src.analysis.mechanistic_interpretation data/processed/ranked_candidates_*.json results/mechanistic_interpretation/
```

### Running Tests

```bash
pytest tests/ -v
```

106 automated tests cover all pipeline modules.

### Reproducibility

- Pipeline is deterministic with `seed=42`
- All inputs/outputs tracked via SHA-256 checksums in `audit_logs/`
- Execution provenance recorded in structured JSON audit logs

## Project Structure

```
discovery-engine/
  config/                    # Search queries and pipeline configuration
  data/
    external/                # DrugAge, GenAge reference data
    processed/               # Pipeline outputs (JSON, not in git)
  docs/                      # Project state, decisions, backlog
  src/
    core/                    # Integrity checks, audit logging, bibliography
    ingestion/               # PubMed, Semantic Scholar, ChEMBL, DrugAge clients
    analysis/                # Protein extraction, target mapping, graph, scoring
    validation/              # Bootstrap, ablation, benchmark, external validation
    visualization/           # Figures and supplementary tables
  tests/                     # 106 automated tests (pytest)
  outputs/                   # Paper draft, figures, supplementary material
  results/                   # Validation results (DrugAge, mechanistic)
  audit_logs/                # Execution provenance (append-only)
  security/                  # .env.example template
```

## Scoring System

Each drug candidate is scored using 6 weighted features:

| Feature | Weight | Source |
|---------|--------|--------|
| Clinical trial phase | 20% | Open Targets |
| Aging target count | 20% | GenAge + Open Targets |
| Lifespan extension | 20% | DrugAge |
| Binding potency (pChEMBL) | 10% | ChEMBL |
| Literature evidence | 15% | PubMed + Semantic Scholar |
| Network centrality | 15% | Knowledge graph |

## Outputs

- `outputs/PAPER_DRAFT_v1.md` — Full manuscript (IMRaD format)
- `outputs/COVER_LETTER.md` — Journal cover letter
- `outputs/figures/` — 5 publication-quality figures (300 DPI)
- `outputs/supplementary/` — 7 supplementary tables + 2 figures
- `results/` — Validation data (CSV, JSON, PNG, MD)

## Declaration of AI Use

This research was conducted with computational assistance from Claude Code (Anthropic, Claude Opus 4.6). The AI assisted with pipeline architecture, code implementation, API integration, statistical validation, and manuscript drafting. All scientific decisions, data interpretation, and conclusions were made by the human author.

## License

MIT License

## Citation

If you use Discovery Engine in your research, please cite:

```
Azevedo, T.S. (2026). Computational Identification of Geroprotective Compound
Candidates via Multi-Source Biological Network Analysis. bioRxiv [preprint].
```
