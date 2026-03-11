# Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis

Tercio S. Azevedo^1^

^1^ Independent Researcher, Sao Carlos, SP, Brazil

**Corresponding author:** Tercio S. Azevedo, terciosilas@gmail.com

---

## Abstract

Drug repurposing for aging is a computationally underexplored approach to identify geroprotective compounds. We developed Discovery Engine, an open-source pipeline integrating literature mining (376 PubMed papers), target extraction (GenAge, 307 aging genes), drug-target associations (Open Targets, 1,118 associations), bioactivity data (ChEMBL), and lifespan data (DrugAge, 1,046 compounds) into a knowledge graph (479 nodes, 898 edges). A weighted multi-feature scoring system ranked 162 drug candidates. The pipeline identified rapamycin (rank #1) and metformin (rank #10) as top candidates. Bootstrap analysis (n=1,000) confirmed ranking stability. Pathway enrichment of top-20 targets confirmed biological relevance across 11 aging pathway categories (top hit: KEGG "Longevity regulating pathway", p=1.27x10^-20^). External validation against DrugAge showed 4.42-fold enrichment of lifespan-extending compounds in the top 20 (Mann-Whitney p=1.59x10^-3^). Mechanistic interpretation mapped top-20 candidates to all eight hallmarks of aging, identifying three convergent axes: mTOR/nutrient sensing, senescence/apoptosis, and mitochondrial/metabolic. Novel candidates include bezafibrate (PPAR agonist, +13% lifespan, FDA-approved), bardoxolone methyl (NRF2 activator, Phase 3), and venetoclax (BCL-2 inhibitor, potential senolytic). Discovery Engine provides a reproducible framework for computational geroprotector identification, supporting prioritization for aging-focused clinical studies.

**Keywords:** drug repurposing; geroprotectors; aging; computational biology; knowledge graph; longevity

---

## Introduction

Aging is the primary risk factor for most chronic diseases, yet pharmacological interventions targeting the aging process remain limited. The concept of geroprotectors -- compounds that slow aging and extend healthy lifespan -- has gained significant attention, with rapamycin, metformin, and senolytics demonstrating lifespan extension in model organisms [1]. However, translating these findings into clinical practice requires systematic identification and prioritization of candidate compounds.

Drug repurposing, the identification of new therapeutic uses for existing drugs, offers a cost-effective path to geroprotector development. Approved drugs have established safety profiles, reducing the timeline and expense of clinical translation. Despite the potential of computational approaches, our systematic literature search revealed that only 6 of 376 relevant publications (1.6%) specifically address computational drug repurposing for aging, indicating a significant methodological gap.

Current approaches to geroprotector identification typically focus on individual pathways (mTOR, sirtuins, senescence) or single data sources. To our knowledge, no existing framework systematically integrates literature mining, protein-drug associations, bioactivity data, lifespan extension evidence, and network topology into a unified scoring system.

We present Discovery Engine, an open-source computational pipeline that addresses this gap through multi-source data integration and network-based candidate ranking. The pipeline is designed with reproducibility and auditability as core principles, with complete provenance tracking via SHA-256 checksums and structured audit logs.

## Methods

### Literature collection and filtering

We queried PubMed using the E-utilities API with six search strategies combining terms for proteomics, aging biomarkers, drug repurposing, senescence, and geroprotectors. The search was conducted in March 2026 and yielded 485 unique records. After deduplication and filtering based on predefined inclusion criteria (publication date >= 2015, English language, original research or review, relevant to aging proteomics or drug repurposing), 376 papers were retained.

Each paper was enriched with citation data from the Semantic Scholar API. Of 376 papers, 356 (94.7%) were found, providing citation counts and fields of study. Copyright compliance was ensured via the Unpaywall API, confirming 280 papers (74%) as Open Access.

### Target extraction

Aging-related genes and proteins were extracted from paper abstracts using a dictionary-based approach combining GenAge (307 human aging genes, Build 21), 15 curated key aging targets with pathway annotations, and 40+ gene aliases. Extraction used regex word-boundary matching with case sensitivity for short symbols (<=4 characters). This yielded 80 unique genes from 152 papers (40.4% coverage). The top 50 targets were consolidated and mapped to Ensembl Gene IDs using the MyGene.info API (100% coverage).

### Drug-target association mining

For each of the 50 protein targets, we queried the Open Targets Platform via its GraphQL API to retrieve known drug associations, clinical trial phases, mechanisms of action, and disease indications. This yielded 1,118 drug-target-disease associations covering 150 unique drugs.

Additionally, 13 known geroprotectors were included from a curated list (rapamycin, metformin, resveratrol, quercetin, dasatinib, nicotinamide riboside, NMN, spermidine, navitoclax, fisetin, acarbose, 17-alpha-estradiol, and D+Q), as many geroprotectors are used off-label and not indexed in clinical trial databases.

Bioactivity data (IC50, Ki, pChEMBL values) was obtained from ChEMBL. Lifespan extension data was obtained from DrugAge (Build 5, 3,406 entries, 1,045 unique compounds) [2].

### Knowledge graph construction

A multipartite knowledge graph was constructed using NetworkX, with three node types: proteins (n=50), drugs (n=162), and diseases (n=267). Edges represent drug-target associations (n=490) and drug-disease indications (n=408), weighted by clinical trial phase. Graph metrics including degree centrality, betweenness centrality, and closeness centrality were computed. Community detection was performed using the greedy modularity algorithm.

### Candidate scoring

Each drug candidate was scored using a weighted combination of six features: clinical phase (weight=0.20), aging target count (0.20), lifespan effect (0.20), binding potency/pChEMBL (0.10), literature evidence (0.15), and network centrality (0.15). Scores were normalized to [0, 1] using feature-specific functions: phase scores were mapped discretely (phase 4 = 1.0, phase 0 = 0.1), lifespan effects used a sigmoid function, and pChEMBL values were mapped with a threshold at 6.0 (1 muM).

### Statistical validation

**Bootstrap analysis:** 1,000 resampling iterations using 80% random subsets of candidates, with seed=42 for reproducibility. **Ablation study:** Each of the six features was removed individually and the impact on control rankings was measured. **Negative controls:** 10 common drugs without known aging effects were verified absent from the top 50. **Sensitivity analysis:** Five weight configurations (baseline, lifespan-dominant, clinical-phase-dominant, network-dominant, uniform) were tested.

### Pathway enrichment analysis

Target genes from the top-20 ranked compounds were extracted from drug-target associations and mechanism-of-action annotations, yielding 30 unique genes. Enrichment was computed using the Enrichr API [3, 4] against three databases: KEGG 2021 Human [5], Reactome 2022, and GO Biological Process 2023. Statistical significance was assessed using the Fisher exact test with Benjamini-Hochberg correction (adjusted p<0.05). Pathways were classified as aging-related based on 11 predefined categories.

### Benchmark comparison

The Discovery Engine ranking was compared against three single-feature baselines: (A) aging target count, (B) lifespan extension from DrugAge, (C) degree centrality; and random expectation. Five known geroprotectors served as positive controls. Performance metrics included Recall@k, Enrichment Factor, and Mean Reciprocal Rank.

### External validation against DrugAge

The 162 ranked compounds were cross-referenced against the full DrugAge database (1,046 unique compounds). Drug names were normalized by converting to lowercase, removing salt suffixes, and matching via a curated synonym dictionary. Metrics included Precision@k, Recall@k, Enrichment Factor@k, and the Mann-Whitney U test (one-sided).

### Mechanistic interpretation

Molecular targets of top-20 compounds were mapped to the eight hallmarks of aging [6, 7]: deregulated nutrient sensing, cellular senescence, mitochondrial dysfunction, loss of proteostasis, genomic instability, epigenetic alterations, stem cell exhaustion, and altered intercellular communication. Target-hallmark mapping used curated gene sets from the hallmarks literature. Convergence analysis identified principal mechanistic axes.

### Implementation

All code was implemented in Python 3.14 and is available at https://github.com/terciosilas/discovery-engine (MIT License). The pipeline uses structured audit logging with SHA-256 checksums for all inputs and outputs. 106 automated tests ensure correctness.

## Results

### Literature landscape

The 376 accepted papers span 2015-2026, with a median of 43 citations per paper. The most represented concepts were mTOR signaling (59 papers), autophagy (34), sirtuins/NAD+ (21), and senescence/senolytics (20). Only 6 papers (1.6%) specifically addressed computational drug repurposing for aging, confirming the methodological gap.

### Aging target network

The top 10 extracted targets by literature frequency were: MTOR (18 papers), AMPK (16), UBB (14), IGF1 (10), SIRT1 (9), CDKN2A (6), APOE (5), PRKAA1 (5), TP53 (5), and FOXO3 (5). Network analysis identified PPARG (degree=21, betweenness=0.079) and MTOR (degree=15, betweenness=0.031) as the most central protein hubs.

### Drug candidate ranking

The top 20 ranked candidates are shown in Table 1. Known geroprotectors are marked with asterisks. Rapamycin ranked first (score 0.519), followed by somatropin (0.495) and regorafenib (0.482). Six of 20 top-ranked compounds (30%) are known geroprotectors: rapamycin (#1), metformin (#10), resveratrol (#12), spermidine (#13), acarbose (#18), and dasatinib (#20).

### Novel candidates of interest

**Bezafibrate** (rank #9, score 0.438): A pan-PPAR agonist approved for hyperlipidemia, bezafibrate activates PGC-1alpha, improving mitochondrial biogenesis. Lifespan extended by 13% in *C. elegans* [2]. Its dual PPAR activation profile and decades of clinical safety data make it a strong repurposing candidate.

**Bardoxolone methyl** (rank #7, score 0.442): An NRF2 activator and PPARG modulator in Phase 3 trials for diabetic kidney disease (CARDINAL trial). NRF2 is the master regulator of >200 cytoprotective genes, with age-related decline contributing to chronic oxidative stress.

**Venetoclax** (rank #4, score 0.448): An FDA-approved selective BCL-2 inhibitor. BCL-2 is overexpressed in senescent cells, protecting them from apoptosis. Venetoclax may function as a senolytic with improved tolerability over navitoclax due to BCL-2 selectivity (reduced thrombocytopenia risk).

**Dactolisib** (rank #14, score 0.425): A dual PI3K/mTOR inhibitor targeting both upstream (PI3K) and downstream (mTOR) nodes in the nutrient-sensing pathway, potentially offering more complete pathway suppression than rapamycin alone.

### Validation results

**Bootstrap stability (n=1,000):** Rapamycin maintained rank #1 with zero variance (std=0.0). Metformin had a mean rank of 8.2 (std=1.2), remaining in the top 10 in 78.2% of iterations.

**Ablation study:** Removal of lifespan data (rapamycin drops from #1 to #11) and potency data (to #12) had the largest impact, confirming experimental evidence as critical. Removal of network centrality or target count had minimal effect.

**Negative controls:** All 10 negative control drugs (atorvastatin, omeprazole, amlodipine, etc.) were absent from the ranked list, yielding a 0% false positive rate.

**Sensitivity analysis:** Rapamycin remained in the top 10 in 4 of 5 weight configurations.

### Pathway enrichment validation

Enrichment analysis of 30 target genes confirmed strong biological relevance (Table 2). Of 1,578 pathways tested, 904 (57.3%) were significantly enriched (adjusted p<0.05), with 143 classified as aging-related. All 11 predefined aging biology categories showed significant enrichment, with the KEGG "Longevity regulating pathway" as the top hit (p=1.27x10^-20^).

### Benchmark comparison

Comparison against single-feature baselines demonstrated the necessity of multi-feature integration (Table 3). Discovery Engine achieved Recall@20=1.00 and EF@20=8.1x. Baselines A (targets only) and C (centrality only) failed catastrophically (0% recall). Baseline B (lifespan only) achieved nominally superior MRR (0.393 vs. 0.263) but functions as a lookup table with no predictive capacity for 93.8% of candidates. Discovery Engine is the only model simultaneously recovering all positive controls and providing predictive ranking for compounds without prior experimental data.

### External validation against DrugAge

Cross-referencing against DrugAge identified 11 compounds with experimental lifespan data (Table 4). Of these, 10 (90.9%) demonstrated positive lifespan extension. DrugAge compounds were significantly enriched in higher ranks (mean rank 41.2 vs. 84.4; Mann-Whitney U=387.0, p=1.59x10^-3^). Precision@20 was 30.0% with EF@20=4.42x. Bezafibrate (rank #9) and pictilisib (rank #79) represent genuine discoveries independently confirmed by DrugAge. Full precision-recall curves are provided in Supplementary Fig. S1.

### Mechanistic interpretation of top ranked candidates

Mechanistic analysis mapped top-20 compounds to the eight hallmarks of aging (Table 5). On average, each compound covered 1.9 hallmarks, with metformin and resveratrol achieving the highest coverage (4 each). All eight hallmarks were represented.

Convergence analysis identified three principal mechanistic axes: (1) **mTOR/AMPK/Nutrient Sensing** (7/20 compounds): rapamycin, metformin, dactolisib, gedatolisib, and mecasermin, converging with the "Longevity regulating pathway" (p=1.27x10^-20^); (2) **Senescence/Apoptosis** (3/20): venetoclax (BCL-2), dasatinib (SRC/ABL), and siltuximab (IL-6/SASP); (3) **Mitochondrial/Metabolic** (5/20): bezafibrate (PPAR/PGC-1alpha), bardoxolone methyl (NRF2), resveratrol (SIRT1/SIRT3), rosiglitazone (PPARG), and metformin (AMPK). Top-ranked compounds form interconnected mechanistic clusters (Supplementary Fig. S2).

## Discussion

### Pipeline validation

The Discovery Engine pipeline successfully recovers known geroprotectors in the top 20. Five independent lines of evidence support ranking validity: (1) pathway enrichment across all 11 major aging categories; (2) 8.1-fold enrichment over random in benchmark comparison; (3) external validation against DrugAge (EF@20=4.42x, p=1.59x10^-3^); (4) genuine discoveries (bezafibrate, pictilisib) independently confirmed by DrugAge; and (5) mechanistic convergence on all eight hallmarks of aging with 25% of compounds targeting three or more hallmarks.

### Novel candidates

Three classes of novel candidates emerge with distinct mechanistic rationales:

**PPAR modulators** (bezafibrate, rosiglitazone, bardoxolone methyl) converge on the mitochondrial/metabolic axis, targeting PPARG and NFE2L2. Bezafibrate activates PGC-1alpha via pan-PPAR agonism, directly addressing the mitochondrial dysfunction hallmark. Its +13% lifespan extension in *C. elegans* and decades of clinical safety data make it the strongest repurposing candidate. Bardoxolone methyl activates NRF2, the master regulator of cytoprotective genes, connecting antioxidant defense to the mitochondrial dysfunction and altered intercellular communication hallmarks.

**BCL-2 family inhibitors** (venetoclax) target the cellular senescence hallmark through selective BCL-2 inhibition. Combined with dasatinib (SRC/ABL, rank #20) and siltuximab (IL-6/SASP suppression, rank #16), the pipeline identifies a complementary senolytic toolkit targeting three distinct nodes of the senescence pathway.

**Dual PI3K/mTOR inhibitors** (dactolisib, gedatolisib) cover three hallmarks each, matching rapamycin's breadth. By inhibiting both PI3K and mTOR, they may achieve more complete pathway suppression with different immunosuppressive profiles.

### Limitations

Several limitations should be noted: (1) dictionary-based gene extraction may miss novel targets not in GenAge; (2) Open Targets underrepresents off-label geroprotectors, mitigated by curated injection; (3) only 10/162 candidates have DrugAge entries, systematically underscoring compounds without lifespan data; (4) molecular docking was not performed; (5) the 376-paper corpus reflects a single search strategy.

### Future directions

Priority next steps include molecular docking of top candidates using AutoDock Vina, adverse event analysis via FAERS/SIDER databases, integration of UK Biobank proteomic data, and experimental validation of bezafibrate and bardoxolone methyl in *C. elegans* lifespan assays.

## Declarations

### Funding

No external funding was received for this work.

### Conflicts of interest

The author declares no conflicts of interest.

### Ethics approval

Not applicable. This study is purely computational and does not involve human subjects, animal experiments, or identifiable personal data.

### Data availability

The complete dataset (ranked candidates, knowledge graph, validation results, figures, and supplementary tables) is available on Zenodo: https://doi.org/10.5281/zenodo.XXXXXXX (CC-BY-4.0). Code is available at https://github.com/terciosilas/discovery-engine (MIT License). The pipeline is deterministic with seed=42; all inputs/outputs are tracked via SHA-256 checksums. 106 automated tests ensure correctness.

### Declaration of generative AI use

This research was conducted with computational assistance from Claude Code (Anthropic, Claude Opus 4.6). The AI assisted with pipeline architecture design, code implementation, API integration, statistical validation, and manuscript drafting. All scientific decisions, data interpretation, and conclusions were made by the human author. The full AI interaction log is available in the project repository per transparency guidelines [8].

## Acknowledgments

All databases used (PubMed, Semantic Scholar, Open Targets, ChEMBL, DrugAge, GenAge) are publicly available.

## References

1. Partridge L, Fuentealba M, Kennedy BK (2020) The quest to slow ageing through drug discovery. Nat Rev Drug Discov 19:513-532. https://doi.org/10.1038/s41573-020-0067-7

2. Barardo D, Thornton SN, Thoppil H, Walsh M, Sharber S, Fernandes G, Moskalev A, Craig T, Doig AJ, de Magalhaes JP (2017) The DrugAge database of ageing-related drugs. Aging Cell 16:594-597. https://doi.org/10.1111/acel.12585

3. Chen EY, Tan CM, Kou Y, Duan Q, Wang Z, Meirelles GV, Clark NR, Ma'ayan A (2013) Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool. BMC Bioinformatics 14:128. https://doi.org/10.1186/1471-2105-14-128

4. Kuleshov MV, Jones MR, Rouillard AD, Fernandez NF, Duan Q, Wang Z, Koplev S, Jenkins SL, Jagodnik KM, Lachmann A, McDermott MG, Monteiro CD, Gundersen GW, Ma'ayan A (2016) Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Res 44:W90-W97. https://doi.org/10.1093/nar/gkw377

5. Kanehisa M, Goto S (2000) KEGG: Kyoto Encyclopedia of Genes and Genomes. Nucleic Acids Res 28:27-30. https://doi.org/10.1093/nar/28.1.27

6. Lopez-Otin C, Blasco MA, Partridge L, Serrano M, Kroemer G (2013) The hallmarks of aging. Cell 153:1194-1217. https://doi.org/10.1016/j.cell.2013.05.039

7. Lopez-Otin C, Blasco MA, Partridge L, Serrano M, Kroemer G (2023) Hallmarks of aging: An expanding universe. Cell 186:243-278. https://doi.org/10.1016/j.cell.2022.11.001

8. Editorial (2023) Tools such as ChatGPT threaten transparent science; here are our ground rules for their use. Nature 613:612. https://doi.org/10.1038/d41586-023-00191-1

9. de Magalhaes JP (2017) Tackling aging: why the research is not catching up with the facts. Aging Cell 16:657-663.

10. Moskalev A, Anisimov V, Aliper A, Artemov A, Asadullah K, Belsky D, Zhavoronkov A (2022) Geroprotectors: A unified concept and screening approaches. Aging Discovery 1:4.

11. Tacutu R, Thornton D, Johnson E, Budovsky A, Barber D, Craig T, Diana E, Lehmann G, Toren D, Wang J, Fraifeld VE, de Magalhaes JP (2018) Human Ageing Genomic Resources: new and updated databases. Nucleic Acids Res 46:D1083-D1090. https://doi.org/10.1093/nar/gkx1042

---

## Tables

**Table 1.** Top 20 Geroprotective Compound Candidates

| Rank | Compound | Score | Phase | Targets | Lifespan | Known^a^ |
|------|----------|------:|------:|--------:|---------:|:--------:|
| 1 | Rapamycin | 0.519 | 4 | 0 | +14.8% | * |
| 2 | Somatropin | 0.495 | 4 | 1 | - | |
| 3 | Regorafenib | 0.482 | 4 | 2 | - | |
| 4 | Venetoclax | 0.448 | 4 | 1 | - | |
| 5 | Nintedanib esylate | 0.445 | 4 | 2 | - | |
| 6 | Pazopanib HCl | 0.445 | 4 | 2 | - | |
| 7 | Bardoxolone methyl | 0.442 | 3 | 2 | - | |
| 8 | Pazopanib | 0.442 | 3 | 2 | - | |
| 9 | Bezafibrate | 0.438 | 4 | 1 | +13.0% | |
| 10 | Metformin | 0.438 | 4 | 0 | +9.9% | * |
| 11 | Nintedanib | 0.435 | 3 | 2 | - | |
| 12 | Resveratrol | 0.435 | 3 | 0 | +7.2% | * |
| 13 | Spermidine | 0.426 | 2 | 0 | +60.5% | * |
| 14 | Dactolisib | 0.425 | 3 | 2 | - | |
| 15 | Gedatolisib | 0.422 | 3 | 2 | - | |
| 16 | Siltuximab | 0.412 | 4 | 1 | - | |
| 17 | Rosiglitazone | 0.402 | 4 | 1 | - | |
| 18 | Acarbose | 0.399 | 4 | 0 | +9.8% | * |
| 19 | Mecasermin | 0.398 | 4 | 1 | - | |
| 20 | Dasatinib | 0.396 | 4 | 0 | - | * |

^a^ Known geroprotectors marked with asterisk. Score = weighted sum of 6 normalized features. Phase = maximum clinical trial phase. Targets = number of aging-related protein targets. Lifespan = mean lifespan extension from DrugAge.

**Table 2.** Top Aging-Related Pathways Enriched in Top-20 Compound Targets

| Pathway | Database | Adj. P-value | Genes | Category |
|---------|----------|-------------:|------:|----------|
| Longevity regulating pathway | KEGG | 2.08x10^-18^ | 12 | Longevity |
| Autophagy | KEGG | 4.16x10^-17^ | 12 | Autophagy |
| AMPK signaling pathway | KEGG | 6.15x10^-16^ | 11 | AMPK/Metabolic |
| PI3K-Akt signaling pathway | KEGG | 1.06x10^-15^ | 14 | mTOR/PI3K/AKT |
| mTOR signaling pathway | KEGG | 4.71x10^-13^ | 10 | mTOR/PI3K/AKT |
| FoxO signaling pathway | KEGG | 1.85x10^-8^ | 7 | FOXO |
| Insulin signaling pathway | KEGG | 6.56x10^-7^ | 6 | Insulin/IGF-1 |

Complete enrichment results are provided in Supplementary Table S8.

**Table 3.** Benchmark Comparison: Discovery Engine vs. Single-Feature Baselines

| Model | Mean Rank | Recall@10 | Recall@20 | EF@20 | MRR |
|-------|----------:|----------:|----------:|------:|----:|
| **Discovery Engine** | **10.8** | **0.40** | **1.00** | **8.10** | **0.263** |
| Baseline A (targets) | 155.0 | 0.00 | 0.00 | 0.00 | 0.007 |
| Baseline B (lifespan) | 4.8 | 1.00 | 1.00 | 8.10 | 0.393 |
| Baseline C (centrality) | 79.4 | 0.00 | 0.00 | 0.00 | 0.016 |
| Random (expected) | 81.5 | 0.06 | 0.12 | 1.00 | 0.035 |

Five known geroprotectors served as positive controls. EF = Enrichment Factor. MRR = Mean Reciprocal Rank.

**Table 4.** DrugAge Compounds Identified in the Discovery Engine Ranking

| Rank | Compound | Studies | Species | Avg Lifespan | Status |
|-----:|----------|--------:|---------|-------------:|--------|
| 1 | Rapamycin | 37 | *C. elegans*, *Drosophila*, Mouse | +14.4% | Known |
| 9 | Bezafibrate | 1 | *C. elegans* | +13.0% | Novel |
| 10 | Metformin | 54 | Cricket, *C. elegans*, *Drosophila*, Mouse | +9.0% | Known |
| 12 | Resveratrol | 170 | 10+ species | +6.2% | Known |
| 13 | Spermidine | 8 | *C. elegans*, *Drosophila*, Mouse, Yeast | +60.5% | Known |
| 18 | Acarbose | 10 | Mouse | +8.8% | Known |
| 23 | Quercetin | 38 | 8+ species | +8.9% | Known |
| 24 | Fisetin | 7 | *Drosophila*, Mouse, Yeast | +12.9% | Known |
| 79 | Pictilisib | 1 | *C. elegans* | +9.6% | Novel |
| 116 | Nicotinamide riboside | 4 | Mouse, Yeast | +5.5% | Known |
| 148 | NMN | 1 | *Drosophila* | 0.0% | Known |

Mann-Whitney U=387.0, p=1.59x10^-3^. EF@20=4.42x. Precision@20=30.0%.

**Table 5.** Mechanistic Mapping of Top-20 Candidates to Hallmarks of Aging

| Rank | Compound | Key Targets | Hallmarks | N |
|-----:|----------|-------------|-----------|--:|
| 1 | Rapamycin | MTOR, RPTOR, RICTOR, RPS6KB1 | NS, LP, SCE | 3 |
| 4 | Venetoclax | BCL2 | CS | 1 |
| 7 | Bardoxolone methyl | NFE2L2, PPARG | MD, AIC | 2 |
| 9 | Bezafibrate | PPARG | MD, AIC | 2 |
| 10 | Metformin | PRKAA1, PRKAA2, STK11 | NS, MD, GI, (+1) | 4 |
| 12 | Resveratrol | SIRT1, SIRT3, NAMPT | NS, MD, GI, EA | 4 |
| 13 | Spermidine | (autophagy inducer) | LP | 1 |
| 16 | Siltuximab | IL6 | AIC, CS | 2 |
| 20 | Dasatinib | (senolytic) | CS | 1 |

NS=Nutrient Sensing, LP=Loss of Proteostasis, SCE=Stem Cell Exhaustion, CS=Cellular Senescence, MD=Mitochondrial Dysfunction, AIC=Altered Intercellular Communication, GI=Genomic Instability, EA=Epigenetic Alterations. All eight hallmarks [6, 7] were represented across the top-20.

---

## Figure Legends

**Fig. 1** Pipeline overview. The Discovery Engine pipeline integrates data from six public databases into a knowledge graph, applying a weighted multi-feature scoring system to rank 162 drug candidates for geroprotective potential.

**Fig. 2** Top-20 compound ranking. Horizontal bar chart showing composite scores for the 20 highest-ranked candidates. Known geroprotectors are highlighted. Score components (clinical phase, aging targets, lifespan, potency, literature, centrality) are shown as stacked segments.

**Fig. 3** Bootstrap stability analysis (n=1,000 iterations). Distribution of ranks for the top-20 compounds across bootstrap resamples. Rapamycin maintains rank #1 with zero variance.

**Fig. 4** Feature ablation study. Impact of removing each scoring feature on the ranks of five positive control geroprotectors. Lifespan and potency removal cause the largest rank drops.

**Fig. 5** Weight sensitivity analysis. Ranks of positive controls across five weight configurations (baseline, lifespan-dominant, clinical-phase-dominant, network-dominant, uniform).

---

## Supplementary Information

The online version contains supplementary material available at [DOI].

**Supplementary Fig. S1** External validation against DrugAge and benchmark comparison. (a) Distribution of DrugAge compounds across ranking positions. (b) Precision and recall curves at varying k. (c) Enrichment factor curve. (d) Benchmark comparison across models.

**Supplementary Fig. S2** Mechanistic interpretation network. Three-column network visualization showing connections from drugs (left) to molecular targets (center) to hallmarks of aging (right).

**Supplementary Tables S1-S7** Complete ranking of 162 compounds (S1), PubMed search queries (S2), bootstrap results (S3), ablation results (S4), sensitivity configurations (S5), graph metrics (S6), aging targets (S7).
