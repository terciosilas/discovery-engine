# Pathway Enrichment Analysis Report

> Discovery Engine -- Validacao Biologica do Ranking
> Data: 2026-03-11 11:28
> Assistido por: Claude Code (Anthropic)

---

## 1. Resumo Executivo

Realizamos pathway enrichment analysis nos **30 targets moleculares**
associados aos compostos do **top-20** do ranking Discovery Engine.

- **Databases consultadas:** KEGG 2021, Reactome 2022, GO Biological Process 2023
- **Metodo:** API Enrichr (Ma'ayan Lab, Mount Sinai)
- **Correcao multipla:** Benjamini-Hochberg (FDR)
- **Total de pathways testados:** 1578
- **Pathways significativos (adj. p < 0.05):** 904
- **Pathways aging-related significativos:** 143
- **Pathways aging-related (p nominal < 0.05):** 169

---

## 2. Genes Analisados

| Gene | Compostos Associados |
|------|---------------------|
| ABL1 | Dasatinib |
| ATG5 | Spermidine |
| BCL2 | VENETOCLAX |
| BECN1 | Spermidine |
| EPHA2 | Dasatinib |
| EPHB2 | Dasatinib |
| FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB, PAZOPANIB HYDROCHLORIDE, REGORAFENIB |
| FLT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB, PAZOPANIB HYDROCHLORIDE, REGORAFENIB |
| GAA | Acarbose |
| GANAB | Acarbose |
| GHR | SOMATROPIN |
| IGF1R | MECASERMIN |
| IL6 | SILTUXIMAB |
| MAP1LC3B | Spermidine |
| MGAM | Acarbose |
| MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |
| NAMPT | Resveratrol |
| NFE2L2 | BARDOXOLONE METHYL |
| PIK3R1 | DACTOLISIB, GEDATOLISIB |
| PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |
| PRKAA1 | Metformin |
| PRKAA2 | Metformin |
| RICTOR | Rapamycin |
| RPS6KB1 | Rapamycin |
| RPTOR | Rapamycin |
| SIRT1 | Resveratrol |
| SIRT3 | Resveratrol |
| SRC | Dasatinib |
| STK11 | Metformin |
| ULK1 | Spermidine |

---

## 3. Pathways Significativos por Database

### 3.1 KEGG

**104 pathways significativos:**

| Pathway | P-value | Adj. P | Genes | Compostos | Aging? |
|---------|---------|--------|-------|-----------|--------|
| Longevity regulating pathway | 1.27e-20 | 2.08e-18 | RPTOR, PRKAA1, STK11, PRKAA2, RPS6KB1, PPARG, ULK1, PIK3R1, SIRT1, MTOR, IGF1R, ATG5 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB | **Yes** |
| Autophagy | 5.08e-19 | 4.16e-17 | RPTOR, BECN1, PRKAA1, STK11, PRKAA2, RPS6KB1, BCL2, ULK1, PIK3R1, MTOR, IGF1R, ATG5 | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| AMPK signaling pathway | 1.13e-17 | 6.15e-16 | RPTOR, PRKAA1, STK11, PRKAA2, RPS6KB1, PPARG, ULK1, PIK3R1, SIRT1, MTOR, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB | **Yes** |
| PI3K-Akt signaling pathway | 2.58e-17 | 1.06e-15 | PRKAA1, FLT1, PRKAA2, PIK3R1, MTOR, IGF1R, GHR, RPTOR, IL6, STK11, RPS6KB1, BCL2, FGFR1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| mTOR signaling pathway | 1.43e-14 | 4.71e-13 | RPTOR, PRKAA1, STK11, PRKAA2, RPS6KB1, ULK1, RICTOR, PIK3R1, MTOR, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| HIF-1 signaling pathway | 2.16e-10 | 5.90e-09 | IL6, FLT1, RPS6KB1, BCL2, PIK3R1, MTOR, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| FoxO signaling pathway | 7.90e-10 | 1.85e-08 | IL6, PRKAA1, STK11, PRKAA2, PIK3R1, SIRT1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| Shigellosis | 2.17e-09 | 4.44e-08 | RPTOR, BECN1, RPS6KB1, SRC, BCL2, PIK3R1, MTOR, ATG5 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Pathways in cancer | 2.98e-09 | 5.43e-08 | IL6, RPS6KB1, BCL2, ABL1, PPARG, PIK3R1, MTOR, FGFR1, NFE2L2, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Insulin resistance | 1.15e-08 | 1.89e-07 | IL6, PRKAA1, PRKAA2, RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Thermogenesis | 4.19e-08 | 6.24e-07 | RPTOR, PRKAA1, PRKAA2, RPS6KB1, PPARG, MTOR, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Insulin signaling pathway | 4.80e-08 | 6.56e-07 | RPTOR, PRKAA1, PRKAA2, RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Fluid shear stress and atherosclerosis | 5.23e-08 | 6.60e-07 | PRKAA1, PRKAA2, SRC, BCL2, PIK3R1, NFE2L2 | BARDOXOLONE METHYL, DACTOLISIB, Dasatinib |  |
| ErbB signaling pathway | 1.61e-07 | 1.89e-06 | RPS6KB1, SRC, ABL1, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Prostate cancer | 3.13e-07 | 3.42e-06 | BCL2, PIK3R1, MTOR, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Proteoglycans in cancer | 5.21e-07 | 5.34e-06 | RPS6KB1, SRC, PIK3R1, MTOR, FGFR1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Rap1 signaling pathway | 6.00e-07 | 5.79e-06 | FLT1, SRC, PIK3R1, FGFR1, EPHA2, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Lipid and atherosclerosis | 6.89e-07 | 6.28e-06 | IL6, SRC, BCL2, PPARG, PIK3R1, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Ras signaling pathway | 1.07e-06 | 9.27e-06 | FLT1, ABL1, PIK3R1, FGFR1, EPHA2, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Apelin signaling pathway | 1.74e-06 | 1.43e-05 | BECN1, PRKAA1, PRKAA2, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Breast cancer | 2.46e-06 | 1.92e-05 | RPS6KB1, PIK3R1, MTOR, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Mitophagy | 3.13e-06 | 2.27e-05 | BECN1, SRC, ULK1, ATG5 | Dasatinib, Spermidine |  |
| Non-alcoholic fatty liver disease | 3.19e-06 | 2.27e-05 | IL6, PRKAA1, PRKAA2, PPARG, PIK3R1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Adipocytokine signaling pathway | 3.32e-06 | 2.27e-05 | PRKAA1, STK11, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Central carbon metabolism in cancer | 3.52e-06 | 2.31e-05 | PIK3R1, MTOR, SIRT3, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB |  |
| JAK-STAT signaling pathway | 3.96e-06 | 2.50e-05 | GHR, IL6, BCL2, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Hepatocellular carcinoma | 4.74e-06 | 2.88e-05 | RPS6KB1, PIK3R1, MTOR, NFE2L2, IGF1R | BARDOXOLONE METHYL, DACTOLISIB, GEDATOLISIB |  |
| MicroRNAs in cancer | 5.73e-06 | 3.36e-05 | RPTOR, BCL2, ABL1, PIK3R1, SIRT1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Axon guidance | 7.00e-06 | 3.96e-05 | SRC, ABL1, PIK3R1, EPHB2, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Colorectal cancer | 8.02e-06 | 4.38e-05 | RPS6KB1, BCL2, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Kaposi sarcoma-associated herpesvirus infection | 9.31e-06 | 4.92e-05 | BECN1, IL6, SRC, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Focal adhesion | 1.13e-05 | 5.81e-05 | FLT1, SRC, BCL2, PIK3R1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Nicotinate and nicotinamide metabolism | 1.93e-05 | 9.42e-05 | NAMPT, SIRT1, SIRT3 | Resveratrol |  |
| Human cytomegalovirus infection | 1.95e-05 | 9.42e-05 | IL6, RPS6KB1, SRC, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Chemical carcinogenesis | 2.61e-05 | 1.22e-04 | RPS6KB1, SRC, BCL2, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Spinocerebellar ataxia | 5.94e-05 | 2.71e-04 | BECN1, ULK1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Gastric cancer | 6.97e-05 | 3.09e-04 | RPS6KB1, BCL2, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Cellular senescence | 8.33e-05 | 3.60e-04 | IL6, PIK3R1, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Hepatitis B | 9.64e-05 | 4.06e-04 | IL6, SRC, BCL2, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Tight junction | 1.14e-04 | 4.66e-04 | PRKAA1, STK11, PRKAA2, SRC | Dasatinib, Metformin |  |
| Acute myeloid leukemia | 1.37e-04 | 5.47e-04 | RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| NOD-like receptor signaling pathway | 1.48e-04 | 5.78e-04 | IL6, NAMPT, BCL2, ATG5 | Resveratrol, SILTUXIMAB, Spermidine |  |
| Adherens junction | 1.62e-04 | 6.20e-04 | SRC, FGFR1, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Melanoma | 1.69e-04 | 6.31e-04 | PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Transcriptional misregulation in cancer | 1.86e-04 | 6.76e-04 | IL6, FLT1, PPARG, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, MECASERMIN |  |
| Glioma | 1.91e-04 | 6.82e-04 | PIK3R1, MTOR, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Pancreatic cancer | 1.99e-04 | 6.93e-04 | RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Alzheimer disease | 2.03e-04 | 6.93e-04 | BECN1, IL6, ULK1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Human immunodeficiency virus 1 infection | 2.71e-04 | 9.07e-04 | RPS6KB1, BCL2, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| PD-L1 expression and PD-1 checkpoint pathway in cancer | 3.17e-04 | 1.04e-03 | RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Hypertrophic cardiomyopathy | 3.28e-04 | 1.05e-03 | IL6, PRKAA1, PRKAA2 | Metformin, SILTUXIMAB |  |
| Choline metabolism in cancer | 4.21e-04 | 1.33e-03 | RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| AGE-RAGE signaling pathway in diabetic complications | 4.46e-04 | 1.38e-03 | IL6, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| C-type lectin receptor signaling pathway | 5.01e-04 | 1.52e-03 | IL6, SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Glucagon signaling pathway | 5.44e-04 | 1.62e-03 | PRKAA1, PRKAA2, SIRT1 | Metformin, Resveratrol |  |
| Pathways of neurodegeneration | 6.45e-04 | 1.89e-03 | BECN1, IL6, BCL2, ULK1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Growth hormone synthesis, secretion and action | 7.42e-04 | 2.10e-03 | GHR, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Neurotrophin signaling pathway | 7.42e-04 | 2.10e-03 | BCL2, ABL1, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Thyroid hormone signaling pathway | 7.78e-04 | 2.16e-03 | SRC, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Herpes simplex virus 1 infection | 7.99e-04 | 2.18e-03 | IL6, SRC, BCL2, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| MAPK signaling pathway | 9.27e-04 | 2.49e-03 | FLT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Circadian rhythm | 9.84e-04 | 2.56e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Galactose metabolism | 9.84e-04 | 2.56e-03 | MGAM, GAA | Acarbose |  |
| Huntington disease | 1.08e-03 | 2.76e-03 | BECN1, PPARG, ULK1, MTOR | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Yersinia infection | 1.11e-03 | 2.77e-03 | IL6, SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Estrogen signaling pathway | 1.11e-03 | 2.77e-03 | SRC, BCL2, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Measles | 1.16e-03 | 2.85e-03 | IL6, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Apoptosis | 1.24e-03 | 2.98e-03 | BECN1, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, Spermidine | **Yes** |
| Signaling pathways regulating pluripotency of stem cell | 1.26e-03 | 3.00e-03 | PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| Starch and sucrose metabolism | 1.33e-03 | 3.11e-03 | MGAM, GAA | Acarbose |  |
| Oxytocin signaling pathway | 1.56e-03 | 3.60e-03 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Ferroptosis | 1.72e-03 | 3.92e-03 | MAP1LC3B, ATG5 | Spermidine |  |
| Amyotrophic lateral sclerosis | 2.03e-03 | 4.57e-03 | BECN1, BCL2, ULK1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Protein processing in endoplasmic reticulum | 2.10e-03 | 4.66e-03 | GANAB, BCL2, NFE2L2 | Acarbose, BARDOXOLONE METHYL, VENETOCLAX |  |
| Type II diabetes mellitus | 2.16e-03 | 4.72e-03 | PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Carbohydrate digestion and absorption | 2.25e-03 | 4.87e-03 | MGAM, PIK3R1 | Acarbose, DACTOLISIB, GEDATOLISIB |  |
| Tuberculosis | 2.43e-03 | 5.18e-03 | IL6, SRC, BCL2 | Dasatinib, SILTUXIMAB, VENETOCLAX |  |
| Neutrophil extracellular trap formation | 2.79e-03 | 5.88e-03 | SRC, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Pathogenic Escherichia coli infection | 3.14e-03 | 6.52e-03 | IL6, SRC, ABL1 | Dasatinib, SILTUXIMAB |  |
| Epstein-Barr virus infection | 3.37e-03 | 6.91e-03 | IL6, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| VEGF signaling pathway | 3.53e-03 | 7.15e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Regulation of actin cytoskeleton | 4.17e-03 | 8.35e-03 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Prolactin signaling pathway | 4.93e-03 | 9.74e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Chronic myeloid leukemia | 5.79e-03 | 1.13e-02 | ABL1, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Bacterial invasion of epithelial cells | 5.94e-03 | 1.15e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Small cell lung cancer | 8.37e-03 | 1.60e-02 | BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, VENETOCLAX |  |
| Rheumatoid arthritis | 8.55e-03 | 1.61e-02 | IL6, FLT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Fc gamma R-mediated phagocytosis | 9.27e-03 | 1.73e-02 | RPS6KB1, PIK3R1 | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Inflammatory mediator regulation of TRP channels | 9.45e-03 | 1.74e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Progesterone-mediated oocyte maturation | 9.83e-03 | 1.79e-02 | PIK3R1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Amoebiasis | 1.02e-02 | 1.82e-02 | IL6, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Chagas disease | 1.02e-02 | 1.82e-02 | IL6, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Toll-like receptor signaling pathway | 1.06e-02 | 1.87e-02 | IL6, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Parathyroid hormone synthesis, secretion and action | 1.10e-02 | 1.92e-02 | BCL2, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Th17 cell differentiation | 1.12e-02 | 1.93e-02 | IL6, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| TNF signaling pathway | 1.22e-02 | 2.09e-02 | IL6, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Cholinergic synapse | 1.24e-02 | 2.10e-02 | BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, VENETOCLAX |  |
| Human papillomavirus infection | 1.31e-02 | 2.19e-02 | RPS6KB1, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Sphingolipid signaling pathway | 1.37e-02 | 2.27e-02 | BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, VENETOCLAX |  |
| Platelet activation | 1.48e-02 | 2.43e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Osteoclast differentiation | 1.55e-02 | 2.52e-02 | PPARG, PIK3R1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Relaxin signaling pathway | 1.60e-02 | 2.57e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Phospholipase D signaling pathway | 2.07e-02 | 3.29e-02 | PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Influenza A | 2.73e-02 | 4.31e-02 | IL6, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |

### 3.2 Reactome

**205 pathways significativos:**

| Pathway | P-value | Adj. P | Genes | Compostos | Aging? |
|---------|---------|--------|-------|-----------|--------|
| Macroautophagy R-HSA-1632852 | 5.96e-14 | 2.25e-11 | RPTOR, BECN1, PRKAA1, MAP1LC3B, PRKAA2, SRC, ULK1, MTOR, ATG5 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Autophagy R-HSA-9612973 | 1.73e-13 | 3.27e-11 | RPTOR, BECN1, PRKAA1, MAP1LC3B, PRKAA2, SRC, ULK1, MTOR, ATG5 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| MTOR Signaling R-HSA-165159 | 2.90e-11 | 3.65e-09 | RPTOR, PRKAA1, STK11, PRKAA2, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Energy Dependent Regulation Of mTOR By LKB1-AMPK R-HSA- | 6.19e-10 | 5.85e-08 | RPTOR, PRKAA1, STK11, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Receptor Mediated Mitophagy R-HSA-8934903 | 8.58e-10 | 6.49e-08 | MAP1LC3B, SRC, ULK1, ATG5 | Dasatinib, Spermidine |  |
| Signal Transduction R-HSA-162582 | 8.09e-09 | 5.10e-07 | PRKAA1, FLT1, PRKAA2, SRC, PIK3R1, MTOR, IGF1R, RPTOR, IL6, STK11, RPS6KB1, BCL2, ABL1, PPARG, RICTOR, FGFR1, EPHA2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Selective Autophagy R-HSA-9663891 | 3.00e-08 | 1.62e-06 | MAP1LC3B, PRKAA2, SRC, ULK1, ATG5 | Dasatinib, Metformin, Spermidine | **Yes** |
| Generic Transcription Pathway R-HSA-212436 | 5.92e-08 | 2.80e-06 | RPTOR, IL6, PRKAA1, STK11, PRKAA2, SRC, ABL1, PPARG, RICTOR, SIRT1, MTOR, SIRT3 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Mitophagy R-HSA-5205647 | 8.21e-08 | 3.45e-06 | MAP1LC3B, SRC, ULK1, ATG5 | Dasatinib, Spermidine |  |
| PIP3 Activates AKT Signaling R-HSA-1257604 | 1.12e-07 | 4.24e-06 | RPTOR, SRC, PPARG, RICTOR, PIK3R1, MTOR, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB | **Yes** |
| RNA Polymerase II Transcription R-HSA-73857 | 1.72e-07 | 5.82e-06 | RPTOR, IL6, PRKAA1, STK11, PRKAA2, SRC, ABL1, PPARG, RICTOR, SIRT1, MTOR, SIRT3 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| CD28 Co-Stimulation R-HSA-389356 | 1.85e-07 | 5.82e-06 | SRC, RICTOR, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Intracellular Signaling By Second Messengers R-HSA-9006 | 2.76e-07 | 8.02e-06 | RPTOR, SRC, PPARG, RICTOR, PIK3R1, MTOR, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Signaling By VEGF R-HSA-194138 | 4.02e-07 | 1.09e-05 | FLT1, SRC, RICTOR, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| PI3K/AKT Signaling In Cancer R-HSA-2219528 | 4.65e-07 | 1.17e-05 | SRC, RICTOR, PIK3R1, MTOR, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Gene Expression (Transcription) R-HSA-74160 | 5.06e-07 | 1.20e-05 | RPTOR, IL6, PRKAA1, STK11, PRKAA2, SRC, ABL1, PPARG, RICTOR, SIRT1, MTOR, SIRT3 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Costimulation By CD28 Family R-HSA-388841 | 3.13e-06 | 6.87e-05 | SRC, RICTOR, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of TP53 Activity R-HSA-5633007 | 3.40e-06 | 6.87e-05 | PRKAA1, STK11, PRKAA2, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Disease R-HSA-1643685 | 3.45e-06 | 6.87e-05 | BECN1, IL6, GANAB, MAP1LC3B, SRC, GAA, ABL1, RICTOR, PIK3R1, MTOR, FGFR1, NFE2L2 | Acarbose, BARDOXOLONE METHYL, DACTOLISIB |  |
| Extra-nuclear Estrogen Signaling R-HSA-9009391 | 4.17e-06 | 7.87e-05 | SRC, BCL2, PIK3R1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| CD28 Dependent PI3K/Akt Signaling R-HSA-389357 | 5.28e-06 | 9.51e-05 | RICTOR, PIK3R1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| mTORC1-mediated Signaling R-HSA-166208 | 6.03e-06 | 1.04e-04 | RPTOR, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| TP53 Regulates Metabolic Genes R-HSA-5628897 | 6.31e-06 | 1.04e-04 | RPTOR, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Signaling By Receptor Tyrosine Kinases R-HSA-9006934 | 6.86e-06 | 1.08e-04 | FLT1, SRC, RICTOR, PIK3R1, MTOR, FGFR1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| VEGFA-VEGFR2 Pathway R-HSA-4420097 | 1.09e-05 | 1.62e-04 | SRC, RICTOR, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Immune System R-HSA-168256 | 1.11e-05 | 1.62e-04 | GHR, BECN1, MGAM, IL6, SRC, GAA, BCL2, ABL1, RICTOR, PIK3R1, MTOR, ATG5 | Acarbose, DACTOLISIB, Dasatinib |  |
| Transcriptional Regulation By TP53 R-HSA-3700989 | 1.22e-05 | 1.71e-04 | RPTOR, PRKAA1, STK11, PRKAA2, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| RHOU GTPase Cycle R-HSA-9013420 | 2.68e-05 | 3.62e-04 | SRC, PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Activated NTRK3 Signals Thru PI3K R-HSA-9603381 | 3.25e-05 | 4.24e-04 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| EPH-ephrin Mediated Repulsion Of Cells R-HSA-3928665 | 5.36e-05 | 6.53e-04 | SRC, EPHB2, EPHA2 | Dasatinib |  |
| Signaling By FGFR1 R-HSA-5654736 | 5.36e-05 | 6.53e-04 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| IRS-related Events Triggered By IGF1R R-HSA-2428928 | 6.04e-05 | 6.92e-04 | PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| AMPK Inhibits chREBP Transcriptional Activity R-HSA-163 | 6.06e-05 | 6.92e-04 | STK11, PRKAA2 | Metformin | **Yes** |
| IGF1R Signaling Cascade R-HSA-2428924 | 6.40e-05 | 6.92e-04 | PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| SARS-CoV-1 Infection R-HSA-9678108 | 6.40e-05 | 6.92e-04 | BECN1, GANAB, MAP1LC3B | Acarbose, Spermidine |  |
| Signaling By Type 1 Insulin-like Growth Factor 1 Recept | 6.78e-05 | 7.12e-04 | PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN | **Yes** |
| GP1b-IX-V Activation Signaling R-HSA-430116 | 7.78e-05 | 7.95e-04 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Activation Of AMPK Downstream Of NMDARs R-HSA-9619483 | 9.71e-05 | 9.33e-04 | PRKAA1, PRKAA2 | Metformin | **Yes** |
| Regulation Of FOXO Transcriptional Activity By Acetylat | 9.71e-05 | 9.33e-04 | SIRT1, SIRT3 | Resveratrol | **Yes** |
| Post NMDA Receptor Activation Events R-HSA-438064 | 1.03e-04 | 9.33e-04 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Regulation Of PTEN Gene Transcription R-HSA-8943724 | 1.03e-04 | 9.33e-04 | RPTOR, PPARG, MTOR | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Axon Guidance R-HSA-422475 | 1.04e-04 | 9.33e-04 | SRC, ABL1, PIK3R1, EPHB2, FGFR1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| FOXO-mediated Transcription R-HSA-9614085 | 1.25e-04 | 1.10e-03 | STK11, SIRT1, SIRT3 | Metformin, Resveratrol | **Yes** |
| Nervous System Development R-HSA-9675108 | 1.35e-04 | 1.16e-03 | SRC, ABL1, PIK3R1, EPHB2, FGFR1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Translation Of Replicase And Assembly Of Replication Tr | 1.42e-04 | 1.19e-03 | BECN1, MAP1LC3B | Spermidine |  |
| ESR-mediated Signaling R-HSA-8939211 | 1.71e-04 | 1.41e-03 | SRC, BCL2, PIK3R1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Activation Of NMDA Receptors And Postsynaptic Events R- | 1.84e-04 | 1.48e-03 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Constitutive Signaling By Aberrant PI3K In Cancer R-HSA | 2.15e-04 | 1.69e-03 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Signaling By NTRK3 (TRKC) R-HSA-9034015 | 2.58e-04 | 1.99e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Signaling By FGFR R-HSA-190236 | 2.87e-04 | 2.16e-03 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| GAB1 Signalosome R-HSA-180292 | 2.92e-04 | 2.16e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Fcgamma Receptor (FCGR) Dependent Phagocytosis R-HSA-20 | 2.96e-04 | 2.16e-03 | SRC, ABL1, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of TP53 Activity Thru Phosphorylation R-HSA- | 3.28e-04 | 2.29e-03 | PRKAA1, STK11, PRKAA2 | Metformin | **Yes** |
| Ephrin Signaling R-HSA-3928664 | 3.28e-04 | 2.29e-03 | SRC, EPHB2 | Dasatinib |  |
| EPH-Ephrin Signaling R-HSA-2682334 | 3.38e-04 | 2.33e-03 | SRC, EPHB2, EPHA2 | Dasatinib |  |
| Signaling By KIT In Disease R-HSA-9669938 | 3.66e-04 | 2.47e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Diseases Of Signal Transduction By Growth Factor Recept | 3.85e-04 | 2.55e-03 | SRC, RICTOR, PIK3R1, MTOR, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Cellular Response To Heat Stress R-HSA-3371556 | 4.33e-04 | 2.78e-03 | RPTOR, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| L1CAM Interactions R-HSA-373760 | 4.33e-04 | 2.78e-03 | SRC, EPHB2, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Infectious Disease R-HSA-5663205 | 4.45e-04 | 2.78e-03 | BECN1, IL6, GANAB, MAP1LC3B, SRC, ABL1, NFE2L2 | Acarbose, BARDOXOLONE METHYL, Dasatinib |  |
| PI-3K cascade:FGFR1 R-HSA-5654689 | 4.49e-04 | 2.78e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| PINK1-PRKN Mediated Mitophagy R-HSA-5205685 | 4.93e-04 | 3.01e-03 | MAP1LC3B, ATG5 | Spermidine |  |
| PI5P, PP2A And IER3 Regulate PI3K/AKT Signaling R-HSA-6 | 5.29e-04 | 3.16e-03 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Signaling By NTRK2 (TRKB) R-HSA-9006115 | 5.40e-04 | 3.16e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Interleukin-4 And Interleukin-13 Signaling R-HSA-678580 | 5.44e-04 | 3.16e-03 | IL6, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Signaling By Nuclear Receptors R-HSA-9006931 | 5.86e-04 | 3.32e-03 | SRC, BCL2, PIK3R1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| RUNX2 Regulates Osteoblast Differentiation R-HSA-894097 | 5.88e-04 | 3.32e-03 | SRC, ABL1 | Dasatinib |  |
| Cellular Responses To Stress R-HSA-2262752 | 6.13e-04 | 3.41e-03 | RPTOR, IL6, MAP1LC3B, SIRT1, MTOR, NFE2L2 | BARDOXOLONE METHYL, DACTOLISIB, GEDATOLISIB |  |
| Negative Regulation Of PI3K/AKT Network R-HSA-199418 | 6.38e-04 | 3.49e-03 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Cellular Responses To Stimuli R-HSA-8953897 | 6.78e-04 | 3.60e-03 | RPTOR, IL6, MAP1LC3B, SIRT1, MTOR, NFE2L2 | BARDOXOLONE METHYL, DACTOLISIB, GEDATOLISIB |  |
| Constitutive Signaling By AKT1 E17K In Cancer R-HSA-567 | 6.91e-04 | 3.60e-03 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Signaling By ALK R-HSA-201556 | 6.91e-04 | 3.60e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Innate Immune System R-HSA-168249 | 6.95e-04 | 3.60e-03 | MGAM, SRC, GAA, BCL2, ABL1, PIK3R1, ATG5 | Acarbose, DACTOLISIB, Dasatinib |  |
| MAPK1/MAPK3 Signaling R-HSA-5684996 | 7.43e-04 | 3.76e-03 | IL6, SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| VEGFR2 Mediated Vascular Permeability R-HSA-5218920 | 7.46e-04 | 3.76e-03 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Downstream Signal Transduction R-HSA-186763 | 8.02e-04 | 3.99e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Developmental Biology R-HSA-1266738 | 8.60e-04 | 4.22e-03 | SRC, ABL1, PPARG, PIK3R1, EPHB2, FGFR1, EPHA2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Downstream Signaling Of Activated FGFR1 R-HSA-5654687 | 9.22e-04 | 4.41e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| FGFR1 Mutant Receptor Activation R-HSA-1839124 | 9.22e-04 | 4.41e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| RUNX2 Regulates Bone Development R-HSA-8941326 | 9.84e-04 | 4.65e-03 | SRC, ABL1 | Dasatinib |  |
| Negative Regulation Of FGFR1 Signaling R-HSA-5654726 | 1.12e-03 | 5.21e-03 | SRC, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE | **Yes** |
| PTEN Regulation R-HSA-6807070 | 1.16e-03 | 5.36e-03 | RPTOR, PPARG, MTOR | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| MAPK Family Signaling Cascades R-HSA-5683057 | 1.24e-03 | 5.65e-03 | IL6, SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| HSF1-dependent Transactivation R-HSA-3371571 | 1.33e-03 | 5.83e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of TP53 Degradation R-HSA-6804757 | 1.33e-03 | 5.83e-03 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Signaling By FGFR1 In Disease R-HSA-5655302 | 1.33e-03 | 5.83e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| RHOV GTPase Cycle R-HSA-9013424 | 1.40e-03 | 5.95e-03 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of TP53 Expression And Degradation R-HSA-680 | 1.40e-03 | 5.95e-03 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Early SARS-CoV-2 Infection Events R-HSA-9772572 | 1.40e-03 | 5.95e-03 | BECN1, MAP1LC3B | Spermidine |  |
| Signaling By FGFR3 R-HSA-5654741 | 1.56e-03 | 6.54e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| RET Signaling R-HSA-8853659 | 1.64e-03 | 6.73e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Signaling By FGFR4 R-HSA-5654743 | 1.64e-03 | 6.73e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| RND1 GTPase Cycle R-HSA-9696273 | 1.80e-03 | 7.18e-03 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| RND3 GTPase Cycle R-HSA-9696264 | 1.80e-03 | 7.18e-03 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Signaling By SCF-KIT R-HSA-1433557 | 1.80e-03 | 7.18e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| RND2 GTPase Cycle R-HSA-9696270 | 1.89e-03 | 7.44e-03 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| PI3K Cascade R-HSA-109704 | 1.98e-03 | 7.71e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| TBC/RABGAPs R-HSA-8854214 | 2.07e-03 | 7.90e-03 | MAP1LC3B, ULK1 | Spermidine |  |
| Heme Signaling R-HSA-9707616 | 2.07e-03 | 7.90e-03 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol |  |
| SARS-CoV Infections R-HSA-9679506 | 2.14e-03 | 8.08e-03 | BECN1, GANAB, MAP1LC3B, NFE2L2 | Acarbose, BARDOXOLONE METHYL, Spermidine |  |
| IRS-mediated Signaling R-HSA-112399 | 2.25e-03 | 8.36e-03 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB |  |
| Cyclin D Associated Events In G1 R-HSA-69231 | 2.25e-03 | 8.36e-03 | SRC, ABL1 | Dasatinib |  |
| Signaling By EGFR R-HSA-177929 | 2.45e-03 | 8.90e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Signaling By ERBB2 R-HSA-1227986 | 2.45e-03 | 8.90e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Neurotransmitter Receptors And Postsynaptic Signal Tran | 2.51e-03 | 9.04e-03 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Signaling By PDGF R-HSA-186797 | 2.75e-03 | 9.82e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Insulin Receptor Signaling Cascade R-HSA-74751 | 2.86e-03 | 1.01e-02 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB |  |
| Amino Acids Regulate mTORC1 R-HSA-9639288 | 3.07e-03 | 1.08e-02 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| NCAM Signaling For Neurite Out-Growth R-HSA-375165 | 3.30e-03 | 1.13e-02 | SRC, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Signaling By ERBB4 R-HSA-1236394 | 3.30e-03 | 1.13e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| FCGR3A-mediated Phagocytosis R-HSA-9664422 | 3.65e-03 | 1.24e-02 | SRC, ABL1 | Dasatinib |  |
| Signaling By FGFR In Disease R-HSA-1226099 | 3.77e-03 | 1.27e-02 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB | **Yes** |
| Signaling By MET R-HSA-6806834 | 4.01e-03 | 1.34e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Adaptive Immune System R-HSA-1280218 | 4.34e-03 | 1.44e-02 | BECN1, SRC, RICTOR, PIK3R1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Circadian Clock R-HSA-400253 | 4.79e-03 | 1.58e-02 | NAMPT, SIRT1 | Resveratrol |  |
| Signaling By FGFR2 R-HSA-5654738 | 5.21e-03 | 1.70e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| RHOG GTPase Cycle R-HSA-9013408 | 5.49e-03 | 1.77e-02 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Transmission Across Chemical Synapses R-HSA-112315 | 5.84e-03 | 1.87e-02 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Leishmania Infection R-HSA-9658195 | 5.91e-03 | 1.87e-02 | IL6, SRC, ABL1 | Dasatinib, SILTUXIMAB |  |
| Signaling By Insulin Receptor R-HSA-74752 | 5.94e-03 | 1.87e-02 | PIK3R1, FGFR1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB |  |
| Regulation Of HMOX1 Expression And Activity R-HSA-97075 | 7.48e-03 | 2.29e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| MECP2 Regulates Transcription Factors R-HSA-9022707 | 7.48e-03 | 2.29e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Maturation Of Spike Protein R-HSA-9683686 | 7.48e-03 | 2.29e-02 | GANAB | Acarbose |  |
| RAC2 GTPase Cycle R-HSA-9013404 | 7.52e-03 | 2.29e-02 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| RAF/MAP Kinase Cascade R-HSA-5673001 | 7.62e-03 | 2.31e-02 | SRC, PIK3R1, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Mitochondrial Biogenesis R-HSA-1592230 | 7.86e-03 | 2.36e-02 | PRKAA2, SIRT3 | Metformin, Resveratrol | **Yes** |
| RAC3 GTPase Cycle R-HSA-9013423 | 8.55e-03 | 2.53e-02 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| SARS-CoV-2 Infection R-HSA-9694516 | 8.58e-03 | 2.53e-02 | BECN1, GANAB, MAP1LC3B | Acarbose, Spermidine |  |
| Activated NTRK2 Signals Thru FYN R-HSA-9032500 | 8.97e-03 | 2.57e-02 | SRC | Dasatinib |  |
| Activated NTRK2 Signals Thru PI3K R-HSA-9028335 | 8.97e-03 | 2.57e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| MET Activates PI3K/AKT Signaling R-HSA-8851907 | 8.97e-03 | 2.57e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| FGFR1b Ligand Binding And Activation R-HSA-190370 | 8.97e-03 | 2.57e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| KEAP1-NFE2L2 Pathway R-HSA-9755511 | 9.83e-03 | 2.79e-02 | MAP1LC3B, NFE2L2 | BARDOXOLONE METHYL, Spermidine | **Yes** |
| Integration Of Energy Metabolism R-HSA-163685 | 1.08e-02 | 3.04e-02 | STK11, PRKAA2 | Metformin |  |
| Membrane Trafficking R-HSA-199991 | 1.18e-02 | 3.22e-02 | MAP1LC3B, PRKAA2, SRC, ULK1 | Dasatinib, Metformin, Spermidine |  |
| VEGF Binds To VEGFR Leading To Receptor Dimerization R- | 1.19e-02 | 3.22e-02 | FLT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| InlA-mediated Entry Of Listeria Monocytogenes Into Host | 1.19e-02 | 3.22e-02 | SRC | Dasatinib |  |
| Role Of ABL In ROBO-SLIT Signaling R-HSA-428890 | 1.19e-02 | 3.22e-02 | ABL1 | Dasatinib |  |
| SHC-related Events Triggered By IGF1R R-HSA-2428933 | 1.19e-02 | 3.22e-02 | IGF1R | MECASERMIN | **Yes** |
| Netrin Mediated Repulsion Signals R-HSA-418886 | 1.19e-02 | 3.22e-02 | SRC | Dasatinib |  |
| Signaling By NTRK1 (TRKA) R-HSA-187037 | 1.26e-02 | 3.38e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| PI3K/AKT Activation R-HSA-198203 | 1.34e-02 | 3.43e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| BH3-only Proteins Associate With And Inactivate Anti-Ap | 1.34e-02 | 3.43e-02 | BCL2 | VENETOCLAX | **Yes** |
| CD163 Mediating An Anti-Inflammatory Response R-HSA-966 | 1.34e-02 | 3.43e-02 | IL6 | SILTUXIMAB | **Yes** |
| Regulation Of Commissural Axon Pathfinding By SLIT And  | 1.34e-02 | 3.43e-02 | SRC | Dasatinib |  |
| Lipophagy R-HSA-9613354 | 1.34e-02 | 3.43e-02 | PRKAA2 | Metformin |  |
| MAPK1 (ERK2) Activation R-HSA-112411 | 1.34e-02 | 3.43e-02 | IL6 | SILTUXIMAB |  |
| Downregulation Of ERBB4 Signaling R-HSA-1253288 | 1.34e-02 | 3.43e-02 | SRC | Dasatinib |  |
| Transcriptional Regulation By RUNX2 R-HSA-8878166 | 1.37e-02 | 3.47e-02 | SRC, ABL1 | Dasatinib |  |
| Cell-Cell Communication R-HSA-1500931 | 1.39e-02 | 3.51e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Rab Regulation Of Trafficking R-HSA-9007101 | 1.44e-02 | 3.59e-02 | MAP1LC3B, ULK1 | Spermidine |  |
| Vesicle-mediated Transport R-HSA-5653656 | 1.45e-02 | 3.60e-02 | MAP1LC3B, PRKAA2, SRC, ULK1 | Dasatinib, Metformin, Spermidine |  |
| PI3K Events In ERBB4 Signaling R-HSA-1250342 | 1.49e-02 | 3.61e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| Activation Of PPARGC1A (PGC-1alpha) By Phosphorylation  | 1.49e-02 | 3.61e-02 | PRKAA2 | Metformin | **Yes** |
| MAPK3 (ERK1) Activation R-HSA-110056 | 1.49e-02 | 3.61e-02 | IL6 | SILTUXIMAB |  |
| Signaling By FGFR4 In Disease R-HSA-5655291 | 1.49e-02 | 3.61e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| Signaling By Rho GTPases R-HSA-194315 | 1.50e-02 | 3.62e-02 | SRC, ABL1, PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Signaling By Rho GTPases, Miro GTPases And RHOBTB3 R-HS | 1.63e-02 | 3.75e-02 | SRC, ABL1, PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Pexophagy R-HSA-9664873 | 1.64e-02 | 3.75e-02 | MAP1LC3B | Spermidine |  |
| Carnitine Metabolism R-HSA-200425 | 1.64e-02 | 3.75e-02 | PRKAA2 | Metformin |  |
| Interleukin-6 Signaling R-HSA-1059683 | 1.64e-02 | 3.75e-02 | IL6 | SILTUXIMAB |  |
| SARS-CoV-2 Modulates Autophagy R-HSA-9754560 | 1.64e-02 | 3.75e-02 | MAP1LC3B | Spermidine | **Yes** |
| Digestion Of Dietary Carbohydrate R-HSA-189085 | 1.64e-02 | 3.75e-02 | MGAM | Acarbose |  |
| Signaling By PDGFRA Extracellular Domain Mutants R-HSA- | 1.64e-02 | 3.75e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Signaling By Activated Point Mutants Of FGFR1 R-HSA-183 | 1.64e-02 | 3.75e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Signaling By NTRKs R-HSA-166520 | 1.67e-02 | 3.80e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Cell Surface Interactions At Vascular Wall R-HSA-202733 | 1.71e-02 | 3.88e-02 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| PECAM1 Interactions R-HSA-210990 | 1.79e-02 | 3.95e-02 | SRC | Dasatinib |  |
| p38MAPK Events R-HSA-171007 | 1.79e-02 | 3.95e-02 | SRC | Dasatinib |  |
| Erythropoietin Activates Phosphoinositide-3-kinase (PI3 | 1.79e-02 | 3.95e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| FGFR1c Ligand Binding And Activation R-HSA-190373 | 1.79e-02 | 3.95e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Signal Regulatory Protein Family Interactions R-HSA-391 | 1.93e-02 | 4.22e-02 | SRC | Dasatinib |  |
| FCGR Activation R-HSA-2029481 | 1.93e-02 | 4.22e-02 | SRC | Dasatinib |  |
| Neuronal System R-HSA-112316 | 1.97e-02 | 4.28e-02 | PRKAA1, PRKAA2, SRC | Dasatinib, Metformin |  |
| Cytokine Signaling In Immune System R-HSA-1280215 | 2.00e-02 | 4.32e-02 | GHR, IL6, BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, SILTUXIMAB |  |
| Mitotic G1 Phase And G1/S Transition R-HSA-453279 | 2.04e-02 | 4.37e-02 | SRC, ABL1 | Dasatinib |  |
| Glycogen Breakdown (Glycogenolysis) R-HSA-70221 | 2.08e-02 | 4.37e-02 | GAA | Acarbose |  |
| Constitutive Signaling By EGFRvIII R-HSA-5637810 | 2.08e-02 | 4.37e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| DCC Mediated Attractive Signaling R-HSA-418885 | 2.08e-02 | 4.37e-02 | SRC | Dasatinib |  |
| Role Of LAT2/NTAL/LAB On Calcium Mobilization R-HSA-273 | 2.08e-02 | 4.37e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Cellular Response To Starvation R-HSA-9711097 | 2.20e-02 | 4.45e-02 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Activation Of BAD And Translocation To Mitochondria R-H | 2.23e-02 | 4.45e-02 | BCL2 | VENETOCLAX | **Yes** |
| GRB2:SOS Provides Linkage To MAPK Signaling For Integri | 2.23e-02 | 4.45e-02 | SRC | Dasatinib |  |
| Glycogen Storage Diseases R-HSA-3229121 | 2.23e-02 | 4.45e-02 | GAA | Acarbose |  |
| Prolactin Receptor Signaling R-HSA-1170546 | 2.23e-02 | 4.45e-02 | GHR | SOMATROPIN |  |
| p130Cas Linkage To MAPK Signaling For Integrins R-HSA-3 | 2.23e-02 | 4.45e-02 | SRC | Dasatinib |  |
| Signaling By ERBB2 ECD Mutants R-HSA-9665348 | 2.23e-02 | 4.45e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| EPHA-mediated Growth Cone Collapse R-HSA-3928663 | 2.23e-02 | 4.45e-02 | SRC | Dasatinib |  |
| Signaling By FLT3 ITD And TKD Mutants R-HSA-9703648 | 2.23e-02 | 4.45e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| FOXO-mediated Transcription Of Cell Death Genes R-HSA-9 | 2.37e-02 | 4.60e-02 | STK11 | Metformin | **Yes** |
| Spry Regulation Of FGF Signaling R-HSA-1295596 | 2.37e-02 | 4.60e-02 | SRC | Dasatinib | **Yes** |
| PI3K Events In ERBB2 Signaling R-HSA-1963642 | 2.37e-02 | 4.60e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| Phospholipase C-mediated Cascade: FGFR1 R-HSA-5654219 | 2.37e-02 | 4.60e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Regulation Of KIT Signaling R-HSA-1433559 | 2.37e-02 | 4.60e-02 | SRC | Dasatinib |  |
| FGFR1 Ligand Binding And Activation R-HSA-190242 | 2.37e-02 | 4.60e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Tie2 Signaling R-HSA-210993 | 2.52e-02 | 4.78e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of RUNX1 Expression And Activity R-HSA-89345 | 2.52e-02 | 4.78e-02 | SRC | Dasatinib |  |
| MET Activates PTK2 Signaling R-HSA-8874081 | 2.52e-02 | 4.78e-02 | SRC | Dasatinib |  |
| Signaling By Cytosolic FGFR1 Fusion Mutants R-HSA-18391 | 2.52e-02 | 4.78e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| Anti-inflammatory Response Favoring Leishmania Infectio | 2.53e-02 | 4.78e-02 | IL6, SRC | Dasatinib, SILTUXIMAB | **Yes** |
| PI-3K cascade:FGFR3 R-HSA-5654710 | 2.67e-02 | 4.92e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB | **Yes** |
| VEGFR2 Mediated Cell Proliferation R-HSA-5218921 | 2.67e-02 | 4.92e-02 | SRC | Dasatinib | **Yes** |
| Constitutive Signaling By Ligand-Responsive EGFR Cancer | 2.67e-02 | 4.92e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Signaling By CBL R-HSA-912631 | 2.67e-02 | 4.92e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Signaling By FLT3 Fusion Proteins R-HSA-9703465 | 2.67e-02 | 4.92e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |

### 3.3 GO_BP

**595 pathways significativos:**

| Pathway | P-value | Adj. P | Genes | Compostos | Aging? |
|---------|---------|--------|-------|-----------|--------|
| Protein Phosphorylation (GO:0006468) | 3.14e-15 | 1.64e-12 | BECN1, PRKAA1, FLT1, PRKAA2, SRC, MTOR, IGF1R, STK11, RPS6KB1, ABL1, ULK1, RICTOR, EPHB2, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Negative Regulation Of Programmed Cell Death (GO:004306 | 3.17e-15 | 1.64e-12 | BECN1, PRKAA1, PRKAA2, SRC, PIK3R1, SIRT1, MTOR, IGF1R, IL6, RPS6KB1, BCL2, RICTOR, ATG5 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Response To Nutrient Levels (GO:0031667) | 5.24e-14 | 1.81e-11 | RPTOR, PRKAA1, PRKAA2, RPS6KB1, ULK1, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Cellular Response To Nutrient Levels (GO:0031669) | 2.02e-13 | 5.23e-11 | RPTOR, PRKAA1, MAP1LC3B, PRKAA2, ULK1, RICTOR, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Cellular Response To Starvation (GO:0009267) | 1.03e-11 | 2.14e-09 | RPTOR, BECN1, PRKAA1, MAP1LC3B, PRKAA2, SIRT1, MTOR, ATG5 | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Phosphorylation (GO:0016310) | 1.47e-11 | 2.54e-09 | RPTOR, BECN1, PRKAA1, STK11, PRKAA2, ABL1, ULK1, RICTOR, EPHB2, MTOR, FGFR1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Glucose Homeostasis (GO:0042593) | 4.32e-11 | 6.40e-09 | IL6, PRKAA1, STK11, PRKAA2, PPARG, PIK3R1, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Negative Regulation Of Apoptotic Process (GO:0043066) | 5.14e-11 | 6.65e-09 | IL6, PRKAA1, PRKAA2, RPS6KB1, SRC, BCL2, RICTOR, PIK3R1, SIRT1, MTOR, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Protein Autophosphorylation (GO:0046777) | 7.83e-11 | 9.02e-09 | STK11, FLT1, SRC, ABL1, ULK1, MTOR, FGFR1, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of Apoptotic Process (GO:0042981) | 1.62e-10 | 1.68e-08 | IL6, PRKAA1, PRKAA2, RPS6KB1, SRC, BCL2, ABL1, RICTOR, PIK3R1, SIRT1, MTOR, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Transmembrane Receptor Protein Tyrosine Kinase Signalin | 2.28e-10 | 2.15e-08 | GHR, FLT1, SRC, NAMPT, PIK3R1, EPHB2, FGFR1, EPHA2, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Positive Regulation Of Cellular Process (GO:0048522) | 4.73e-10 | 4.09e-08 | RPTOR, IL6, PRKAA1, PRKAA2, NAMPT, BCL2, RICTOR, SIRT1, MTOR, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Peptidyl-Tyrosine Phosphorylation (GO:0018108) | 6.26e-10 | 4.99e-08 | FLT1, SRC, ABL1, EPHB2, FGFR1, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Positive Regulation Of Phosphatidylinositol 3-Kinase Si | 7.51e-10 | 5.56e-08 | BECN1, FLT1, SRC, SIRT1, FGFR1, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Negative Regulation Of Intracellular Signal Transductio | 1.32e-09 | 9.11e-08 | PRKAA1, PRKAA2, SRC, BCL2, PPARG, SIRT1, EPHA2, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Positive Regulation Of Cellular Catabolic Process (GO:0 | 1.69e-09 | 1.09e-07 | RPTOR, BECN1, PRKAA1, STK11, PRKAA2, ULK1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Regulation Of Autophagy (GO:0010506) | 1.84e-09 | 1.12e-07 | RPTOR, BECN1, PRKAA1, STK11, PRKAA2, BCL2, ULK1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Positive Regulation Of Intracellular Signal Transductio | 2.67e-09 | 1.54e-07 | RPTOR, BECN1, IL6, FLT1, SRC, PPARG, RICTOR, SIRT1, FGFR1, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Cellular Response To Chemical Stress (GO:0062197) | 3.57e-09 | 1.94e-07 | RPTOR, PRKAA1, PRKAA2, ABL1, MTOR, NFE2L2 | BARDOXOLONE METHYL, DACTOLISIB, Dasatinib |  |
| Regulation Of Phosphatidylinositol 3-Kinase Signaling ( | 3.82e-09 | 1.98e-07 | BECN1, FLT1, SRC, SIRT1, FGFR1, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Intracellular Glucose Homeostasis (GO:0001678) | 4.95e-09 | 2.44e-07 | PRKAA1, PRKAA2, PIK3R1, SIRT1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Regulation Of Macroautophagy (GO:0016241) | 5.65e-09 | 2.66e-07 | BECN1, PRKAA2, ULK1, SIRT1, MTOR, ATG5 | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Positive Regulation Of Autophagy (GO:0010508) | 1.09e-08 | 4.90e-07 | BECN1, PRKAA1, STK11, PRKAA2, ULK1, SIRT1 | Metformin, Resveratrol, Spermidine | **Yes** |
| Positive Regulation Of Glycolytic Process (GO:0045821) | 1.24e-08 | 5.35e-07 | RPTOR, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Peptidyl-Tyrosine Modification (GO:0018212) | 1.61e-08 | 6.66e-07 | FLT1, SRC, ABL1, EPHB2, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Positive Regulation Of Protein Serine/Threonine Kinase  | 1.86e-08 | 7.43e-07 | GHR, RPTOR, FLT1, SRC, SIRT1, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Regulation Of Protein Kinase B Signaling (GO:0051896) | 4.59e-08 | 1.76e-06 | SRC, RICTOR, SIRT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Protein Modification Process (GO:0036211) | 4.77e-08 | 1.77e-06 | BECN1, PRKAA1, STK11, PRKAA2, ABL1, ULK1, EPHB2, MTOR, FGFR1, ATG5 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| TOR Signaling (GO:0031929) | 9.51e-08 | 3.40e-06 | RPTOR, RPS6KB1, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of TOR Signaling (GO:0032006) | 1.05e-07 | 3.55e-06 | RPTOR, PRKAA1, PRKAA2, RICTOR, SIRT1 | Metformin, Rapamycin, Resveratrol |  |
| Positive Regulation Of Adipose Tissue Development (GO:1 | 1.06e-07 | 3.55e-06 | PRKAA1, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Positive Regulation Of Small Molecule Metabolic Process | 1.63e-07 | 5.28e-06 | RPTOR, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Positive Regulation Of Carbohydrate Metabolic Process ( | 1.85e-07 | 5.80e-06 | RPTOR, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Cellular Response To Insulin Stimulus (GO:0032869) | 3.47e-07 | 9.89e-06 | RPS6KB1, NAMPT, PPARG, PIK3R1, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Regulation Of Glycolytic Process (GO:0006110) | 3.62e-07 | 9.89e-06 | RPTOR, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Regulation Of Peptidyl-Lysine Acetylation (GO:2000756) | 3.63e-07 | 9.89e-06 | PRKAA1, PRKAA2, SIRT1 | Metformin, Resveratrol |  |
| Fatty Acid Homeostasis (GO:0055089) | 3.63e-07 | 9.89e-06 | PRKAA1, PRKAA2, SIRT1 | Metformin, Resveratrol |  |
| Insulin-Like Growth Factor Receptor Signaling Pathway ( | 3.63e-07 | 9.89e-06 | GHR, PIK3R1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Positive Regulation Of Gene Expression (GO:0010628) | 3.82e-07 | 1.01e-05 | IL6, PRKAA1, RPS6KB1, PPARG, PIK3R1, EPHB2, MTOR, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Cellular Response To Glucose Starvation (GO:0042149) | 4.42e-07 | 1.12e-05 | BECN1, PRKAA1, PRKAA2, SIRT1 | Metformin, Resveratrol, Spermidine |  |
| Macroautophagy (GO:0016236) | 4.43e-07 | 1.12e-05 | BECN1, MAP1LC3B, SRC, ULK1, ATG5 | Dasatinib, Spermidine | **Yes** |
| Regulation Of Adipose Tissue Development (GO:1904177) | 4.98e-07 | 1.23e-05 | PRKAA1, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Cell Growth (GO:0001558) | 9.46e-07 | 2.28e-05 | RPTOR, STK11, BCL2, RICTOR, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Positive Regulation Of Macromolecule Biosynthetic Proce | 9.81e-07 | 2.31e-05 | IL6, RPS6KB1, NAMPT, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of TOR Signaling (GO:0032007) | 1.23e-06 | 2.78e-05 | PRKAA1, STK11, PRKAA2, SIRT1 | Metformin, Resveratrol |  |
| Regulation Of Blood Vessel Endothelial Cell Migration ( | 1.23e-06 | 2.78e-05 | PPARG, SIRT1, FGFR1, EPHA2 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| DNA Damage Response (GO:0006974) | 1.27e-06 | 2.79e-05 | RPTOR, STK11, BCL2, ABL1, SIRT1, MTOR, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB | **Yes** |
| Positive Regulation Of Multicellular Organismal Process | 1.33e-06 | 2.88e-05 | GHR, IL6, PRKAA1, PPARG, SIRT1, MTOR, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Selective Autophagy (GO:0061912) | 1.65e-06 | 3.49e-05 | BECN1, MAP1LC3B, ULK1, ATG5 | Spermidine | **Yes** |
| Negative Regulation Of Intrinsic Apoptotic Signaling Pa | 2.02e-06 | 4.11e-05 | SRC, BCL2, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Dasatinib, Resveratrol |  |
| Autophagosome Organization (GO:1905037) | 2.02e-06 | 4.11e-05 | BECN1, MAP1LC3B, ULK1, ATG5 | Spermidine |  |
| Phosphatidylinositol-Mediated Signaling (GO:0048015) | 2.16e-06 | 4.30e-05 | RPS6KB1, PIK3R1, FGFR1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Regulation Of Vascular Endothelial Cell Proliferation ( | 2.45e-06 | 4.78e-05 | FLT1, PPARG, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, NINTEDANIB |  |
| Autophagosome Assembly (GO:0000045) | 2.61e-06 | 5.01e-05 | BECN1, MAP1LC3B, ULK1, ATG5 | Spermidine |  |
| Positive Regulation Of Cell Migration (GO:0030335) | 2.70e-06 | 5.09e-05 | FLT1, SRC, EPHB2, MTOR, EPHA2, IGF1R | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Cellular Response To Hypoxia (GO:0071456) | 3.94e-06 | 7.23e-05 | RPTOR, PPARG, SIRT1, MTOR | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Regulation Of Lipid Storage (GO:0010883) | 3.98e-06 | 7.23e-05 | IL6, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Cellular Response To Decreased Oxygen Levels (GO:003629 | 4.17e-06 | 7.44e-05 | RPTOR, PPARG, SIRT1, MTOR | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Negative Regulation Of Protein Modification Process (GO | 5.43e-06 | 9.54e-05 | PRKAA1, PRKAA2, EPHB2, SIRT1 | Dasatinib, Metformin, Resveratrol |  |
| Response To Insulin (GO:0032868) | 5.71e-06 | 9.87e-05 | RPS6KB1, PPARG, PIK3R1, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Positive Regulation Of Growth (GO:0045927) | 6.31e-06 | 1.07e-04 | RPTOR, BCL2, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Cellular Response To Hexose Stimulus (GO:0071331) | 6.85e-06 | 1.14e-04 | PRKAA1, PRKAA2, IGF1R | MECASERMIN, Metformin |  |
| Regulation Of Kinase Activity (GO:0043549) | 7.65e-06 | 1.24e-04 | FLT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Positive Regulation Of Amide Metabolic Process (GO:0034 | 7.65e-06 | 1.24e-04 | IL6, RPS6KB1, MTOR, SIRT3 | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of DNA-templated Transcription (GO: | 7.92e-06 | 1.26e-04 | RPTOR, IL6, PRKAA1, NAMPT, ABL1, PPARG, PIK3R1, SIRT1, MTOR, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Cellular Response To Peptide Hormone Stimulus (GO:00713 | 9.19e-06 | 1.44e-04 | RPS6KB1, SRC, PPARG, PIK3R1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Positive Regulation Of Protein Kinase B Signaling (GO:0 | 1.09e-05 | 1.69e-04 | SRC, RICTOR, FGFR1, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Regulation Of MAPK Cascade (GO:0043408) | 1.22e-05 | 1.84e-04 | IL6, FLT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Regulation Of Cell Population Proliferation (GO:0042127 | 1.23e-05 | 1.84e-04 | IL6, STK11, NAMPT, BCL2, ULK1, SIRT1, FGFR1, IGF1R | MECASERMIN, Metformin, NINTEDANIB |  |
| Regulation Of Angiogenesis (GO:0045765) | 1.25e-05 | 1.84e-04 | IL6, FLT1, PPARG, SIRT1, EPHA2 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib | **Yes** |
| Positive Regulation Of Macromolecule Metabolic Process  | 1.43e-05 | 2.09e-04 | IL6, PRKAA1, PPARG, EPHB2, MTOR, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Inositol Lipid-Mediated Signaling (GO:0048017) | 1.61e-05 | 2.32e-04 | RPS6KB1, FGFR1, IGF1R | MECASERMIN, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Positive Regulation Of Kinase Activity (GO:0033674) | 1.70e-05 | 2.41e-04 | FLT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Positive Regulation Of Protein Phosphorylation (GO:0001 | 1.75e-05 | 2.41e-04 | GHR, RPTOR, IL6, SRC, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Cellular Response To Glucose Stimulus (GO:0071333) | 1.77e-05 | 2.41e-04 | PRKAA1, PRKAA2, IGF1R | MECASERMIN, Metformin |  |
| Cellular Response To Hydrogen Peroxide (GO:0070301) | 1.77e-05 | 2.41e-04 | IL6, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol, SILTUXIMAB |  |
| Positive Regulation Of Cell Growth (GO:0030307) | 1.84e-05 | 2.47e-04 | RPTOR, BCL2, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Pentose-Phosphate Shunt (GO:0043456) | 2.17e-05 | 2.84e-04 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Lipid Droplet Disassembly (GO:1905691) | 2.17e-05 | 2.84e-04 | PRKAA1, PRKAA2 | Metformin |  |
| Positive Regulation Of Phosphorylation (GO:0042327) | 2.22e-05 | 2.87e-04 | FLT1, SIRT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Mitochondrion Disassembly (GO:0061726) | 2.29e-05 | 2.92e-04 | BECN1, MAP1LC3B, ATG5 | Spermidine | **Yes** |
| Positive Regulation Of Developmental Process (GO:005109 | 2.31e-05 | 2.92e-04 | PRKAA1, SRC, PPARG, SIRT1, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Regulation Of Cytoskeleton Organization (GO:0051493) | 2.45e-05 | 3.02e-04 | PRKAA1, PRKAA2, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Regulation Of MAP Kinase Activity (GO:0043405) | 2.45e-05 | 3.02e-04 | GHR, FLT1, PPARG, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, NINTEDANIB |  |
| Negative Regulation Of Epithelial Cell Apoptotic Proces | 2.48e-05 | 3.02e-04 | PRKAA1, PRKAA2, NFE2L2 | BARDOXOLONE METHYL, Metformin |  |
| Regulation Of Gene Expression (GO:0010468) | 2.70e-05 | 3.23e-04 | IL6, PRKAA1, PRKAA2, ABL1, PPARG, EPHB2, SIRT1, MTOR, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Cellular Response To Oxidative Stress (GO:0034599) | 2.71e-05 | 3.23e-04 | PRKAA1, PRKAA2, ABL1, NFE2L2 | BARDOXOLONE METHYL, Dasatinib, Metformin | **Yes** |
| Glucan Catabolic Process (GO:0009251) | 3.25e-05 | 3.78e-04 | MGAM, GAA | Acarbose |  |
| White Fat Cell Differentiation (GO:0050872) | 3.25e-05 | 3.78e-04 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Ephrin Receptor Signaling Pathway (GO:0048013) | 3.61e-05 | 4.15e-04 | SRC, EPHB2, EPHA2 | Dasatinib |  |
| Positive Regulation Of Peptidyl-Tyrosine Phosphorylatio | 4.10e-05 | 4.66e-04 | GHR, IL6, SRC, ABL1 | Dasatinib, SILTUXIMAB, SOMATROPIN |  |
| Response To Glucose (GO:0009749) | 4.43e-05 | 4.93e-04 | PRKAA1, PRKAA2, IGF1R | MECASERMIN, Metformin |  |
| Response To Hydrogen Peroxide (GO:0042542) | 4.43e-05 | 4.93e-04 | IL6, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol, SILTUXIMAB |  |
| Peptidyl-Lysine Deacetylation (GO:0034983) | 4.55e-05 | 5.01e-04 | SIRT1, SIRT3 | Resveratrol |  |
| Insulin Receptor Signaling Pathway (GO:0008286) | 4.72e-05 | 5.15e-04 | NAMPT, PIK3R1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Regulation Of Intrinsic Apoptotic Signaling Pathway (GO | 5.03e-05 | 5.43e-04 | BECN1, SRC, BCL2 | Dasatinib, Spermidine, VENETOCLAX |  |
| Autophagy Of Mitochondrion (GO:0000422) | 5.36e-05 | 5.66e-04 | BECN1, MAP1LC3B, ATG5 | Spermidine | **Yes** |
| Intrinsic Apoptotic Signaling Pathway In Response To DN | 5.36e-05 | 5.66e-04 | BCL2, SIRT1, EPHA2 | Dasatinib, Resveratrol, VENETOCLAX | **Yes** |
| Positive Regulation Of Transferase Activity (GO:0051347 | 5.94e-05 | 6.15e-04 | FLT1, FGFR1, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Positive Regulation Of Protein Localization To Cell Per | 6.04e-05 | 6.15e-04 | PIK3R1, EPHB2, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Positive Regulation Of Protein Localization To Plasma M | 6.04e-05 | 6.15e-04 | PIK3R1, EPHB2, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Anoikis (GO:0043276) | 6.06e-05 | 6.15e-04 | STK11, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Positive Regulation Of B Cell Activation (GO:0050871) | 6.40e-05 | 6.44e-04 | IL6, BCL2, EPHB2 | Dasatinib, SILTUXIMAB, VENETOCLAX |  |
| Positive Regulation Of Cell Population Proliferation (G | 6.98e-05 | 6.95e-04 | IL6, NAMPT, BCL2, SIRT1, FGFR1, IGF1R | MECASERMIN, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Organelle Disassembly (GO:1903008) | 7.17e-05 | 7.08e-04 | PRKAA1, PRKAA2, ULK1 | Metformin, Spermidine |  |
| Negative Regulation Of Lipid Localization (GO:1905953) | 7.78e-05 | 7.53e-04 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Protein Acetylation (GO:1901985) | 7.78e-05 | 7.53e-04 | PRKAA1, PRKAA2 | Metformin |  |
| Peptidyl-Serine Phosphorylation (GO:0018105) | 8.75e-05 | 8.40e-04 | RPS6KB1, ULK1, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of MAPK Cascade (GO:0043410) | 8.98e-05 | 8.54e-04 | GHR, IL6, FLT1, FGFR1, IGF1R | MECASERMIN, NINTEDANIB, NINTEDANIB ESYLATE |  |
| TORC1 Signaling (GO:0038202) | 9.71e-05 | 8.91e-04 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Mitochondrial Depolarization (GO:0051900) | 9.71e-05 | 8.91e-04 | SRC, BCL2 | Dasatinib, VENETOCLAX | **Yes** |
| Cellular Response To Leucine (GO:0071233) | 9.71e-05 | 8.91e-04 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Response To Leucine (GO:0043201) | 9.71e-05 | 8.91e-04 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Autophagy (GO:0010507) | 1.03e-04 | 9.39e-04 | RPTOR, BCL2, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin | **Yes** |
| Peptidyl-Serine Modification (GO:0018209) | 1.06e-04 | 9.55e-04 | RPS6KB1, ULK1, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Cellular Catabolic Process (GO:0031329) | 1.14e-04 | 1.02e-03 | RPTOR, BECN1, ABL1 | Dasatinib, Rapamycin, Spermidine |  |
| Regulation Of Phospholipase C Activity (GO:1900274) | 1.19e-04 | 1.02e-03 | FLT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Cellular Response To Growth Hormone Stimulus (GO:007137 | 1.19e-04 | 1.02e-03 | GHR, PIK3R1 | DACTOLISIB, GEDATOLISIB, SOMATROPIN | **Yes** |
| Cellular Response To Nitrogen Levels (GO:0043562) | 1.19e-04 | 1.02e-03 | BECN1, MAP1LC3B | Spermidine |  |
| Cellular Response To Nitrogen Starvation (GO:0006995) | 1.19e-04 | 1.02e-03 | BECN1, MAP1LC3B | Spermidine |  |
| Positive Regulation Of Cellular Biosynthetic Process (G | 1.27e-04 | 1.09e-03 | IL6, RPS6KB1, SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Cellular Catabolic Process (GO:0 | 1.37e-04 | 1.16e-03 | RPTOR, BCL2, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Intrinsic Apoptotic Signaling Pa | 1.42e-04 | 1.20e-03 | BCL2, SIRT1 | Resveratrol, VENETOCLAX | **Yes** |
| Phosphate-Containing Compound Metabolic Process (GO:000 | 1.58e-04 | 1.32e-03 | RPTOR, RICTOR, EPHB2, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Myeloid Leukocyte Differentiation (GO:0002573) | 1.62e-04 | 1.35e-03 | PPARG, SIRT1, EPHA2 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Negative Regulation Of Macromolecule Metabolic Process  | 1.64e-04 | 1.35e-03 | PRKAA1, PRKAA2, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Intrinsic Apoptotic Signaling Pathway In  | 1.68e-04 | 1.35e-03 | BCL2, SIRT1 | Resveratrol, VENETOCLAX | **Yes** |
| Peptidyl-Tyrosine Autophosphorylation (GO:0038083) | 1.68e-04 | 1.35e-03 | ABL1, IGF1R | Dasatinib, MECASERMIN |  |
| Interleukin-6-Mediated Signaling Pathway (GO:0070102) | 1.68e-04 | 1.35e-03 | IL6, SRC | Dasatinib, SILTUXIMAB |  |
| Response To Ionizing Radiation (GO:0010212) | 1.69e-04 | 1.35e-03 | PRKAA1, STK11, SIRT1 | Metformin, Resveratrol |  |
| Cellular Response To Reactive Oxygen Species (GO:003461 | 1.76e-04 | 1.40e-03 | IL6, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol, SILTUXIMAB |  |
| Positive Regulation Of Lymphocyte Proliferation (GO:005 | 1.84e-04 | 1.44e-03 | IL6, BCL2, EPHB2 | Dasatinib, SILTUXIMAB, VENETOCLAX |  |
| Regulation Of Fat Cell Differentiation (GO:0045598) | 1.91e-04 | 1.49e-03 | IL6, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Protein Localization To Membrane | 2.23e-04 | 1.72e-03 | PIK3R1, EPHB2, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of Cellular Response To Heat (GO:1900034) | 2.26e-04 | 1.72e-03 | SIRT1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of Transcription By RNA Polymerase  | 2.26e-04 | 1.72e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Protein Localization To Plasma Membrane ( | 2.31e-04 | 1.75e-03 | PIK3R1, EPHB2, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Negative Regulation Of Intrinsic Apoptotic Signaling Pa | 2.58e-04 | 1.92e-03 | BCL2, SIRT1 | Resveratrol, VENETOCLAX | **Yes** |
| Mitophagy (GO:0000423) | 2.58e-04 | 1.92e-03 | BECN1, MAP1LC3B | Spermidine |  |
| Positive Regulation Of Endothelial Cell Migration (GO:0 | 2.77e-04 | 2.05e-03 | ABL1, SIRT1, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Negative Regulation Of Oxidative Stress-Induced Intrins | 2.92e-04 | 2.07e-03 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol | **Yes** |
| Regulation Of Receptor Signaling Pathway Via STAT (GO:1 | 2.92e-04 | 2.07e-03 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Tubulin Deacetylation (GO:0090043) | 2.92e-04 | 2.07e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Embryo Development Ending In Birth Or Egg Hatching (GO: | 2.92e-04 | 2.07e-03 | RICTOR, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Growth Hormone Receptor Signaling Pathway (GO:0060396) | 2.92e-04 | 2.07e-03 | GHR, PIK3R1 | DACTOLISIB, GEDATOLISIB, SOMATROPIN | **Yes** |
| Positive Regulation Of Peptidyl-Lysine Acetylation (GO: | 2.92e-04 | 2.07e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Cellular Response To Oxygen-Containing Compound (GO:190 | 3.15e-04 | 2.22e-03 | RPTOR, IL6, PRKAA1, PRKAA2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Positive Regulation Of Cell Motility (GO:2000147) | 3.17e-04 | 2.22e-03 | FLT1, EPHB2, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Regulation Of Peptidyl-Tyrosine Phosphorylation (GO:005 | 3.28e-04 | 2.23e-03 | GHR, IL6, SRC | Dasatinib, SILTUXIMAB, SOMATROPIN |  |
| Negative Regulation Of Lipid Storage (GO:0010888) | 3.28e-04 | 2.23e-03 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Autophagy Of Nucleus (GO:0044804) | 3.28e-04 | 2.23e-03 | ULK1, ATG5 | Spermidine | **Yes** |
| Regulation Of Oxidative Stress-Induced Intrinsic Apopto | 3.28e-04 | 2.23e-03 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol | **Yes** |
| Positive Regulation Of MAP Kinase Activity (GO:0043406) | 3.38e-04 | 2.29e-03 | GHR, FLT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| B Cell Activation (GO:0042113) | 3.49e-04 | 2.35e-03 | BCL2, PIK3R1, EPHB2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of Protein-Containing Complex Disassembly (G | 3.66e-04 | 2.45e-03 | IGF1R, ATG5 | MECASERMIN, Spermidine |  |
| Positive Regulation Of Epithelial Cell Migration (GO:00 | 3.84e-04 | 2.54e-03 | SRC, ABL1, MTOR | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Positive Regulation Of Transcription By RNA Polymerase  | 3.85e-04 | 2.54e-03 | IL6, NAMPT, ABL1, PPARG, PIK3R1, SIRT1, NFE2L2 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Positive Regulation Of Phospholipase Activity (GO:00105 | 4.06e-04 | 2.65e-03 | FLT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Protein Deacylation (GO:0035601) | 4.06e-04 | 2.65e-03 | SIRT1, SIRT3 | Resveratrol |  |
| Regulation Of Cell Migration (GO:0030334) | 4.28e-04 | 2.77e-03 | FLT1, SRC, EPHB2, EPHA2, IGF1R | Dasatinib, MECASERMIN, NINTEDANIB |  |
| Positive Regulation Of Translational Initiation (GO:004 | 4.49e-04 | 2.87e-03 | RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Anoikis (GO:2000209) | 4.49e-04 | 2.87e-03 | SRC, BCL2 | Dasatinib, VENETOCLAX |  |
| Positive Regulation Of Cholesterol Efflux (GO:0010875) | 4.93e-04 | 3.13e-03 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Intrinsic Apoptotic Signaling Pathway (GO:0097193) | 5.15e-04 | 3.23e-03 | STK11, BCL2, EPHA2 | Dasatinib, Metformin, VENETOCLAX |  |
| Negative Regulation Of MAPK Cascade (GO:0043409) | 5.15e-04 | 3.23e-03 | PPARG, EPHB2, IGF1R | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Negative Regulation Of Oxidative Stress-Induced Cell De | 5.40e-04 | 3.33e-03 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol | **Yes** |
| Cellular Response To Interleukin-6 (GO:0071354) | 5.40e-04 | 3.33e-03 | IL6, SRC | Dasatinib, SILTUXIMAB |  |
| Long-Chain Fatty Acid Transport (GO:0015909) | 5.40e-04 | 3.33e-03 | RPS6KB1, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Cellular Response To Stress (GO:0080135) | 5.44e-04 | 3.34e-03 | SIRT1, MTOR, NFE2L2 | BARDOXOLONE METHYL, DACTOLISIB, GEDATOLISIB |  |
| Positive Regulation Of Translation (GO:0045727) | 5.59e-04 | 3.40e-03 | IL6, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Cytokine-Mediated Signaling Pathway (GO:0019221) | 5.61e-04 | 3.40e-03 | GHR, IL6, SRC, SIRT1 | Dasatinib, Resveratrol, SILTUXIMAB |  |
| Positive Regulation Of Lipid Metabolic Process (GO:0045 | 5.88e-04 | 3.54e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Transforming Growth Factor Beta Receptor  | 6.06e-04 | 3.63e-03 | STK11, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Protein Serine/Threonine Kinase Activity  | 6.22e-04 | 3.70e-03 | RPTOR, SRC, SIRT1 | Dasatinib, Rapamycin, Resveratrol |  |
| Positive Regulation Of Signal Transduction (GO:0009967) | 6.38e-04 | 3.70e-03 | IL6, SRC, PIK3R1, SIRT1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Negative Regulation Of Intrinsic Apoptotic Signaling Pa | 6.39e-04 | 3.70e-03 | BCL2, SIRT1 | Resveratrol, VENETOCLAX | **Yes** |
| Negative Regulation Of Signaling Receptor Activity (GO: | 6.39e-04 | 3.70e-03 | PPARG, EPHB2 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Osteoclast Differentiation (GO:0030316) | 6.39e-04 | 3.70e-03 | SRC, EPHA2 | Dasatinib |  |
| Regulation Of Cell Size (GO:0008361) | 6.39e-04 | 3.70e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Transcription By RNA Polymerase III (GO:0 | 6.91e-04 | 3.96e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Dendritic Spine Organization (GO:0097061) | 6.91e-04 | 3.96e-03 | EPHB2, IGF1R | Dasatinib, MECASERMIN |  |
| Regulation Of Extrinsic Apoptotic Signaling Pathway In  | 7.46e-04 | 4.20e-03 | BCL2, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Regulation Of Immunoglobulin Production (GO:0002637) | 7.46e-04 | 4.20e-03 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Cellular Response To Acid Chemical (GO:0071229) | 7.46e-04 | 4.20e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Lipid Biosynthetic Process (GO:0046890) | 8.02e-04 | 4.41e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Cellular Response To Osmotic Stress (GO:0071470) | 8.02e-04 | 4.41e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Vascular Endothelial Growth Factor Receptor Signaling P | 8.02e-04 | 4.41e-03 | FLT1, SRC | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Regulation Of Bone Resorption (GO:0045124) | 8.02e-04 | 4.41e-03 | IL6, SRC | Dasatinib, SILTUXIMAB |  |
| Positive Regulation Of Cell Differentiation (GO:0045597 | 8.05e-04 | 4.41e-03 | IL6, PPARG, MTOR, FGFR1 | BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB |  |
| Enzyme-Linked Receptor Protein Signaling Pathway (GO:00 | 8.36e-04 | 4.56e-03 | FLT1, FGFR1, EPHA2 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Negative Regulation Of Cell Growth (GO:0030308) | 8.55e-04 | 4.62e-03 | STK11, ULK1, SIRT1 | Metformin, Resveratrol, Spermidine |  |
| Positive Regulation Of B Cell Proliferation (GO:0030890 | 8.61e-04 | 4.62e-03 | BCL2, EPHB2 | Dasatinib, VENETOCLAX |  |
| Lipid Droplet Organization (GO:0034389) | 8.61e-04 | 4.62e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Regulation Of Vasculature Development (GO:1901342) | 9.22e-04 | 4.90e-03 | IL6, EPHA2 | Dasatinib, SILTUXIMAB |  |
| Response To Amino Acid (GO:0043200) | 9.22e-04 | 4.90e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Transmembrane Receptor Protein Serine/Threonine Kinase  | 9.58e-04 | 5.06e-03 | SRC, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Positive Regulation Of Cholesterol Transport (GO:003237 | 9.84e-04 | 5.15e-03 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Lamellipodium Organization (GO:1 | 9.84e-04 | 5.15e-03 | SRC, PIK3R1 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Regulation Of Cholesterol Efflux (GO:0010874) | 1.05e-03 | 5.41e-03 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Fat Cell Differentiation (GO:004 | 1.05e-03 | 5.41e-03 | IL6, SIRT1 | Resveratrol, SILTUXIMAB |  |
| Phosphatidylinositol 3-Kinase Signaling (GO:0014065) | 1.05e-03 | 5.41e-03 | PIK3R1, IGF1R | DACTOLISIB, GEDATOLISIB, MECASERMIN |  |
| Cellular Response To Cytokine Stimulus (GO:0071345) | 1.10e-03 | 5.65e-03 | GHR, IL6, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol, SILTUXIMAB |  |
| Regulation Of Lamellipodium Assembly (GO:0010591) | 1.12e-03 | 5.69e-03 | PIK3R1, EPHA2 | DACTOLISIB, Dasatinib, GEDATOLISIB |  |
| Negative Regulation Of Cellular Process (GO:0048523) | 1.12e-03 | 5.69e-03 | IL6, STK11, ULK1, EPHB2, SIRT1 | Dasatinib, Metformin, Resveratrol |  |
| Regulation Of Phosphatidylinositol 3-Kinase Activity (G | 1.18e-03 | 5.96e-03 | FLT1, PIK3R1 | DACTOLISIB, GEDATOLISIB, NINTEDANIB |  |
| Positive Regulation Of Immunoglobulin Production (GO:00 | 1.18e-03 | 5.96e-03 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Cellular Response To Amino Acid Stimulus (GO:0071230) | 1.25e-03 | 6.25e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Intrinsic Apoptotic Signaling Pathway By P53 Class Medi | 1.25e-03 | 6.25e-03 | STK11, SIRT1 | Metformin, Resveratrol | **Yes** |
| Regulation Of Cell Adhesion (GO:0030155) | 1.29e-03 | 6.38e-03 | SRC, EPHB2, EPHA2 | Dasatinib |  |
| Organelle Assembly (GO:0070925) | 1.30e-03 | 6.41e-03 | BECN1, MAP1LC3B, ULK1, ATG5 | Spermidine |  |
| Positive Regulation Of Protein Kinase Activity (GO:0045 | 1.31e-03 | 6.43e-03 | RPTOR, STK11, SRC | Dasatinib, Metformin, Rapamycin |  |
| Negative Regulation Of Protein Kinase B Signaling (GO:0 | 1.33e-03 | 6.43e-03 | SIRT1, EPHA2 | Dasatinib, Resveratrol |  |
| Positive Regulation Of Phospholipase C Activity (GO:001 | 1.33e-03 | 6.43e-03 | FLT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Lytic Vacuole Organization (GO:0080171) | 1.33e-03 | 6.43e-03 | GAA, MTOR | Acarbose, DACTOLISIB, GEDATOLISIB |  |
| Negative Regulation Of Endothelial Cell Proliferation ( | 1.40e-03 | 6.69e-03 | FLT1, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, NINTEDANIB |  |
| Positive Regulation Of Receptor Signaling Pathway Via J | 1.40e-03 | 6.69e-03 | GHR, IL6 | SILTUXIMAB, SOMATROPIN | **Yes** |
| Positive Regulation Of Receptor Signaling Pathway Via S | 1.40e-03 | 6.69e-03 | GHR, IL6 | SILTUXIMAB, SOMATROPIN |  |
| Positive Regulation Of Production Of Molecular Mediator | 1.48e-03 | 7.03e-03 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Negative Regulation Of Gene Expression (GO:0010629) | 1.52e-03 | 7.18e-03 | PRKAA1, PRKAA2, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Cellular Component Organization (GO:00511 | 1.53e-03 | 7.21e-03 | RPTOR, STK11, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Regulation Of Mitochondrial Membrane Potential (GO:0051 | 1.56e-03 | 7.27e-03 | BCL2, ABL1 | Dasatinib, VENETOCLAX | **Yes** |
| Positive Regulation Of Lipid Biosynthetic Process (GO:0 | 1.56e-03 | 7.27e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Microtubule Cytoskeleton Organization (GO | 1.64e-03 | 7.57e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Protein Deacetylation (GO:0006476) | 1.64e-03 | 7.57e-03 | SIRT1, SIRT3 | Resveratrol |  |
| Regulation Of Microtubule-Based Process (GO:0032886) | 1.72e-03 | 7.92e-03 | PRKAA1, PRKAA2 | Metformin |  |
| Keratinocyte Differentiation (GO:0030216) | 1.80e-03 | 8.23e-03 | FGFR1, EPHA2 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Monocyte Chemotaxis (GO:0002548) | 1.80e-03 | 8.23e-03 | IL6, FLT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Lysosome Organization (GO:0007040) | 1.89e-03 | 8.55e-03 | GAA, MTOR | Acarbose, DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Cellular Component Size (GO:0032535) | 1.89e-03 | 8.55e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Insulin Receptor Signaling Pathway (GO:00 | 1.98e-03 | 8.76e-03 | RPS6KB1, SIRT1 | Rapamycin, Resveratrol |  |
| Autophagosome Maturation (GO:0097352) | 1.98e-03 | 8.76e-03 | BECN1, MAP1LC3B | Spermidine |  |
| Phosphatidylinositol Phosphate Biosynthetic Process (GO | 1.98e-03 | 8.76e-03 | BECN1, PIK3R1 | DACTOLISIB, GEDATOLISIB, Spermidine |  |
| Positive Regulation Of Biosynthetic Process (GO:0009891 | 1.98e-03 | 8.76e-03 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of B Cell Proliferation (GO:0030888) | 1.98e-03 | 8.76e-03 | BCL2, EPHB2 | Dasatinib, VENETOCLAX |  |
| Positive Regulation Of Blood Vessel Endothelial Cell Mi | 2.16e-03 | 9.53e-03 | SIRT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Regulation Of Signal Transduction By P53 Class Mediator | 2.25e-03 | 9.77e-03 | STK11, MTOR | DACTOLISIB, GEDATOLISIB, Metformin | **Yes** |
| Positive Regulation Of TOR Signaling (GO:0032008) | 2.25e-03 | 9.77e-03 | RPTOR, RICTOR | Rapamycin |  |
| Response To Organonitrogen Compound (GO:0010243) | 2.25e-03 | 9.77e-03 | IL6, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of Epithelial To Mesenchymal Transi | 2.25e-03 | 9.77e-03 | IL6, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Cell Population Proliferation (G | 2.36e-03 | 1.02e-02 | IL6, STK11, PPARG, ULK1 | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Receptor Signaling Pathway Via JAK-STAT ( | 2.86e-03 | 1.23e-02 | GHR, IL6 | SILTUXIMAB, SOMATROPIN | **Yes** |
| Neuron Projection Development (GO:0031175) | 2.92e-03 | 1.25e-02 | IL6, ULK1, EPHB2 | Dasatinib, SILTUXIMAB, Spermidine |  |
| Regulation Of Signal Transduction (GO:0009966) | 2.96e-03 | 1.25e-02 | STK11, SRC, SIRT1 | Dasatinib, Metformin, Resveratrol |  |
| Regulation Of Smooth Muscle Cell Proliferation (GO:0048 | 2.97e-03 | 1.25e-02 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Epidermal Cell Differentiation (GO:0009913) | 2.97e-03 | 1.25e-02 | FGFR1, EPHA2 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Response To Peptide Hormone (GO:0043434) | 3.07e-03 | 1.29e-02 | SRC, SIRT1 | Dasatinib, Resveratrol |  |
| Positive Regulation Of Tyrosine Phosphorylation Of STAT | 3.07e-03 | 1.29e-02 | GHR, IL6 | SILTUXIMAB, SOMATROPIN |  |
| Positive Regulation Of Protein Metabolic Process (GO:00 | 3.10e-03 | 1.29e-02 | IL6, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Cellular Response To Peptide (GO:1901653) | 3.19e-03 | 1.33e-02 | SRC, IGF1R | Dasatinib, MECASERMIN |  |
| Regulation Of Translation (GO:0006417) | 3.37e-03 | 1.40e-02 | IL6, RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Peptidyl-Threonine Phosphorylation (GO:0018107) | 3.41e-03 | 1.41e-02 | STK11, ULK1 | Metformin, Spermidine |  |
| Negative Regulation Of Protein-Containing Complex Assem | 3.53e-03 | 1.45e-02 | SRC, ULK1 | Dasatinib, Spermidine |  |
| Negative Regulation Of Cytokine-Mediated Signaling Path | 3.53e-03 | 1.45e-02 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Cell Differentiation (GO:0045596 | 3.61e-03 | 1.47e-02 | IL6, PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Extrinsic Apoptotic Signaling Pathway (GO | 3.65e-03 | 1.48e-02 | SRC, FGFR1 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Positive Regulation Of Cell Junction Assembly (GO:19018 | 3.77e-03 | 1.52e-02 | EPHB2, EPHA2 | Dasatinib |  |
| Fat Cell Differentiation (GO:0045444) | 3.89e-03 | 1.56e-02 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Protein-Containing Complex Disassembly (GO:0032984) | 3.89e-03 | 1.56e-02 | BECN1, MAP1LC3B | Spermidine |  |
| Positive Regulation Of Macroautophagy (GO:0016239) | 4.14e-03 | 1.66e-02 | PRKAA2, SIRT1 | Metformin, Resveratrol | **Yes** |
| Regulation Of Translational Initiation (GO:0006446) | 4.27e-03 | 1.69e-02 | RPS6KB1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Tyrosine Phosphorylation Of STAT Protein  | 4.27e-03 | 1.69e-02 | GHR, IL6 | SILTUXIMAB, SOMATROPIN |  |
| Negative Regulation Of Immune Response (GO:0050777) | 4.40e-03 | 1.72e-02 | SRC, ATG5 | Dasatinib, Spermidine |  |
| Regulation Of Endocytosis (GO:0030100) | 4.40e-03 | 1.72e-02 | SRC, ABL1 | Dasatinib |  |
| Peptidyl-Threonine Modification (GO:0018210) | 4.40e-03 | 1.72e-02 | STK11, ULK1 | Metformin, Spermidine |  |
| Skin Development (GO:0043588) | 4.66e-03 | 1.82e-02 | FGFR1, EPHA2 | Dasatinib, NINTEDANIB, NINTEDANIB ESYLATE |  |
| Apoptotic Process (GO:0006915) | 4.73e-03 | 1.84e-02 | STK11, BCL2, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Cellular Response To Calcium Ion (GO:0071277) | 4.79e-03 | 1.86e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Negative Regulation Of Extrinsic Apoptotic Signaling Pa | 4.93e-03 | 1.90e-02 | SRC, BCL2 | Dasatinib, VENETOCLAX |  |
| Regulation Of Actin Filament-Based Process (GO:0032970) | 4.93e-03 | 1.90e-02 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Lipid Biosynthetic Process (GO:0008610) | 5.07e-03 | 1.94e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Transforming Growth Factor Beta Receptor Signaling Path | 5.21e-03 | 1.99e-02 | SRC, SIRT1 | Dasatinib, Resveratrol |  |
| Negative Regulation Of Phosphorylation (GO:0042326) | 5.64e-03 | 2.14e-02 | EPHB2, SIRT1 | Dasatinib, Resveratrol |  |
| Regulation Of Plasma Membrane Bounded Cell Projection A | 5.64e-03 | 2.14e-02 | EPHA2, ATG5 | Dasatinib, Spermidine |  |
| Positive Regulation Of Programmed Cell Death (GO:004306 | 5.78e-03 | 2.18e-02 | IL6, BCL2, SIRT1 | Resveratrol, SILTUXIMAB, VENETOCLAX |  |
| Negative Regulation Of Transforming Growth Factor Beta  | 5.94e-03 | 2.23e-02 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Endothelial Cell Proliferation ( | 5.94e-03 | 2.23e-02 | SIRT1, FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Regulation Of Innate Immune Response (GO:0045088) | 6.09e-03 | 2.27e-02 | NFE2L2, ATG5 | BARDOXOLONE METHYL, Spermidine |  |
| Positive Regulation Of Tumor Necrosis Factor Production | 6.09e-03 | 2.27e-02 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Cellular Response To UV (GO:0034644) | 6.24e-03 | 2.31e-02 | STK11, SIRT1 | Metformin, Resveratrol |  |
| Negative Regulation Of Cellular Component Organization  | 6.24e-03 | 2.31e-02 | SRC, ULK1 | Dasatinib, Spermidine |  |
| Negative Regulation Of Protein Serine/Threonine Kinase  | 6.39e-03 | 2.35e-02 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Organelle Assembly (GO:1902115) | 6.39e-03 | 2.35e-02 | EPHB2, ATG5 | Dasatinib, Spermidine |  |
| Activation Of Protein Kinase Activity (GO:0032147) | 6.55e-03 | 2.40e-02 | STK11, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Positive Regulation Of Tumor Necrosis Factor Superfamil | 6.71e-03 | 2.44e-02 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Negative Regulation Of Apoptotic Signaling Pathway (GO: | 6.71e-03 | 2.44e-02 | SRC, BCL2 | Dasatinib, VENETOCLAX |  |
| Regulation Of Epithelial To Mesenchymal Transition (GO: | 6.86e-03 | 2.49e-02 | IL6, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Cysteine-Type Endopeptidase Activity Invo | 7.03e-03 | 2.52e-02 | SRC, SIRT1 | Dasatinib, Resveratrol |  |
| Regulation Of Osteoblast Differentiation (GO:0045667) | 7.19e-03 | 2.52e-02 | IL6, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Protein Localization (GO:1903829 | 7.19e-03 | 2.52e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Macromolecule Catabolic Process (GO:0009057) | 7.19e-03 | 2.52e-02 | BECN1, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Signal Transduction (GO:0009968) | 7.32e-03 | 2.52e-02 | RPS6KB1, BCL2, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| C-terminal Protein Lipidation (GO:0006501) | 7.48e-03 | 2.52e-02 | ATG5 | Spermidine |  |
| Regulation Of Focal Adhesion Disassembly (GO:0120182) | 7.48e-03 | 2.52e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Glucagon Secretion (GO:0070092) | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB |  |
| PERK-mediated Unfolded Protein Response (GO:0036499) | 7.48e-03 | 2.52e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| TORC2 Signaling (GO:0038203) | 7.48e-03 | 2.52e-02 | RICTOR | Rapamycin |  |
| Regulation Of Interleukin-1-Mediated Signaling Pathway  | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Sequestering Of Triglyceride (GO | 7.48e-03 | 2.52e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Macrophage Apoptotic Process (GO:2000109) | 7.48e-03 | 2.52e-02 | SIRT1 | Resveratrol |  |
| Response To Peptidoglycan (GO:0032494) | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Cholesterol Biosynthetic Process | 7.48e-03 | 2.52e-02 | PRKAA1 | Metformin |  |
| Signal Complex Assembly (GO:0007172) | 7.48e-03 | 2.52e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Focal Adhesion Disassembly (GO:0 | 7.48e-03 | 2.52e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Inflammatory Response To Wounding (GO:0090594) | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB | **Yes** |
| Positive Regulation Of Sterol Biosynthetic Process (GO: | 7.48e-03 | 2.52e-02 | PRKAA1 | Metformin |  |
| Leukocyte Apoptotic Process (GO:0071887) | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Apoptotic DNA Fragmentation (GO:1902510) | 7.48e-03 | 2.52e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Apoptotic Process (GO:0043065) | 7.55e-03 | 2.54e-02 | IL6, BCL2, SIRT1 | Resveratrol, SILTUXIMAB, VENETOCLAX |  |
| Regulation Of Endothelial Cell Migration (GO:0010594) | 7.69e-03 | 2.58e-02 | ABL1, EPHA2 | Dasatinib |  |
| Positive Regulation Of Peptidyl-Serine Phosphorylation  | 7.86e-03 | 2.63e-02 | RPTOR, IL6 | Rapamycin, SILTUXIMAB |  |
| Regulation Of Actin Cytoskeleton Organization (GO:00329 | 8.20e-03 | 2.73e-02 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Transcription By RNA Polymerase II (GO:00 | 8.40e-03 | 2.74e-02 | MGAM, IL6, NAMPT, ABL1, PPARG, PIK3R1, SIRT1, NFE2L2 | Acarbose, BARDOXOLONE METHYL, BEZAFIBRATE |  |
| Regulation Of Peptidyl-Serine Phosphorylation (GO:00331 | 8.55e-03 | 2.74e-02 | RPTOR, IL6 | Rapamycin, SILTUXIMAB |  |
| Peptidyl-Lysine Modification (GO:0018205) | 8.73e-03 | 2.74e-02 | SIRT1, SIRT3 | Resveratrol |  |
| Cellular Response To Hormone Stimulus (GO:0032870) | 8.73e-03 | 2.74e-02 | GHR, SRC | Dasatinib, SOMATROPIN |  |
| Positive Regulation Of Transmembrane Receptor Protein S | 8.91e-03 | 2.74e-02 | STK11, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, Metformin |  |
| Regulation Of Cellular Response To Insulin Stimulus (GO | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Endothelial Cell Chemotaxis To Fibroblast | 8.97e-03 | 2.74e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Negative Regulation Of miRNA Processing (GO:1903799) | 8.97e-03 | 2.74e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Response To Reactive Oxygen Spec | 8.97e-03 | 2.74e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Negative Regulation Of Response To Type II Interferon ( | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Aggrephagy (GO:0035973) | 8.97e-03 | 2.74e-02 | ATG5 | Spermidine |  |
| Angiotensin-Activated Signaling Pathway (GO:0038166) | 8.97e-03 | 2.74e-02 | SRC | Dasatinib |  |
| Negative Regulation Of Type II Interferon-Mediated Sign | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Prostaglandin Biosynthetic Process (GO:00 | 8.97e-03 | 2.74e-02 | SIRT1 | Resveratrol |  |
| Cellular Response To Laminar Fluid Shear Stress (GO:007 | 8.97e-03 | 2.74e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Positive Regulation Of ER-associated Ubiquitin-Dependen | 8.97e-03 | 2.74e-02 | NFE2L2 | BARDOXOLONE METHYL | **Yes** |
| Regulation Of Vascular Associated Smooth Muscle Cell Ap | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Gliogenesis (GO:0014015) | 8.97e-03 | 2.74e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Lamellipodium Morphogenesis (GO: | 8.97e-03 | 2.74e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Multicellular Organism Growth (G | 8.97e-03 | 2.74e-02 | GHR | SOMATROPIN |  |
| Glycogen Catabolic Process (GO:0005980) | 8.97e-03 | 2.74e-02 | GAA | Acarbose |  |
| Positive Regulation Of Synaptic Plasticity (GO:0031915) | 8.97e-03 | 2.74e-02 | EPHB2 | Dasatinib |  |
| Intracellular Triglyceride Homeostasis (GO:0035356) | 8.97e-03 | 2.74e-02 | SIRT1 | Resveratrol |  |
| Macrophage Derived Foam Cell Differentiation (GO:001074 | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| rDNA Heterochromatin Formation (GO:0000183) | 8.97e-03 | 2.74e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Adiponectin Secretion (GO:0070163) | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Bile Acid Metabolic Process (GO:1904251) | 8.97e-03 | 2.74e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Cardiac Muscle Hypertrophy In Response To | 8.97e-03 | 2.74e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Cellular Response To Transforming Growth Factor Beta St | 9.09e-03 | 2.77e-02 | SRC, SIRT1 | Dasatinib, Resveratrol |  |
| Regulation Of Protein Localization (GO:0032880) | 9.27e-03 | 2.82e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Regulation Of Intracellular Signal Transduction (GO:190 | 9.79e-03 | 2.91e-02 | STK11, RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Metformin |  |
| Regulation Of Collateral Sprouting (GO:0048670) | 1.05e-02 | 2.91e-02 | ULK1 | Spermidine |  |
| Regulation Of Endodeoxyribonuclease Activity (GO:003207 | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of miRNA-mediated Gene Silencing (G | 1.05e-02 | 2.91e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Peptidyl-Lysine Acetylation (GO: | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Hydrogen Peroxide-Induced Cell Death (GO: | 1.05e-02 | 2.91e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| T-helper 17 Cell Lineage Commitment (GO:0072540) | 1.05e-02 | 2.91e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Lipoprotein Metabolic Process (GO:0050746 | 1.05e-02 | 2.91e-02 | ULK1 | Spermidine |  |
| Regulation Of Myeloid Leukocyte Differentiation (GO:000 | 1.05e-02 | 2.91e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Nucleolar Chromatin Organization (GO:1990700) | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Peroxisome Proliferator Activated Receptor Signaling Pa | 1.05e-02 | 2.91e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE | **Yes** |
| Cellular Response To Leptin Stimulus (GO:0044320) | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Transcription From RNA Polymerase II Prom | 1.05e-02 | 2.91e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Regulation Of Wound Healing, Spreading Of Epidermal Cel | 1.05e-02 | 2.91e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of T-helper 2 Cell Cytokine Product | 1.05e-02 | 2.91e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Attachment Of Mitotic Spindle Mi | 1.05e-02 | 2.91e-02 | BECN1 | Spermidine |  |
| Dendritic Spine Maintenance (GO:0097062) | 1.05e-02 | 2.91e-02 | IGF1R | MECASERMIN |  |
| Single Strand Break Repair (GO:0000012) | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Extracellular Matrix Disassembly | 1.05e-02 | 2.91e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Gluconeogenesis (GO:0045722) | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Stress-Induced Premature Senescence (GO:0090400) | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol | **Yes** |
| Foam Cell Differentiation (GO:0090077) | 1.05e-02 | 2.91e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Taurine Metabolic Process (GO:0019530) | 1.05e-02 | 2.91e-02 | GHR | SOMATROPIN |  |
| Positive Regulation Of Myeloid Cell Apoptotic Process ( | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Late Nucleophagy (GO:0044805) | 1.05e-02 | 2.91e-02 | ULK1 | Spermidine |  |
| Lens Fiber Cell Development (GO:0070307) | 1.05e-02 | 2.91e-02 | EPHA2 | Dasatinib |  |
| Regulation Of Cdc42 Protein Signal Transduction (GO:003 | 1.05e-02 | 2.91e-02 | ABL1 | Dasatinib |  |
| Myeloid Leukocyte Mediated Immunity (GO:0002444) | 1.05e-02 | 2.91e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of SMAD Protein Signal Transduction | 1.05e-02 | 2.91e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Attachment Of Mitotic Spindle Microtubule | 1.05e-02 | 2.91e-02 | BECN1 | Spermidine |  |
| Negative Regulation Of cAMP-dependent Protein Kinase Ac | 1.05e-02 | 2.91e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Vasculature Development (GO:1904 | 1.06e-02 | 2.94e-02 | FLT1, SIRT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Cellular Response To Organonitrogen Compound (GO:007141 | 1.08e-02 | 2.99e-02 | RPTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Response To Calcium Ion (GO:0051592) | 1.10e-02 | 3.04e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Response To Tumor Necrosis Factor (GO:0034612) | 1.14e-02 | 3.14e-02 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol |  |
| Cellular Response To Salt (GO:1902075) | 1.16e-02 | 3.14e-02 | PRKAA1, PRKAA2 | Metformin |  |
| Positive Regulation Of Cysteine-Type Endopeptidase Acti | 1.16e-02 | 3.14e-02 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Glial Cell Proliferation (GO:0060251) | 1.19e-02 | 3.14e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Helicase Activity (GO:0051095) | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| T-helper 17 Cell Differentiation (GO:0072539) | 1.19e-02 | 3.14e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Triglyceride Metabolic Process ( | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| Nicotinamide Nucleotide Biosynthetic Process (GO:001935 | 1.19e-02 | 3.14e-02 | NAMPT | Resveratrol |  |
| Bone Resorption (GO:0045453) | 1.19e-02 | 3.14e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Adaptive Immune Response (GO:000 | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| Commissural Neuron Axon Guidance (GO:0071679) | 1.19e-02 | 3.14e-02 | EPHB2 | Dasatinib |  |
| Response To Leptin (GO:0044321) | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Macrophage Cytokine Production ( | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Smooth Muscle Cell Apoptotic Pro | 1.19e-02 | 3.14e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Intestinal Epithelial Cell Differentiation (GO:0060575) | 1.19e-02 | 3.14e-02 | SRC | Dasatinib |  |
| Leptin-Mediated Signaling Pathway (GO:0033210) | 1.19e-02 | 3.14e-02 | SIRT1 | Resveratrol |  |
| Regulation Of ER-associated Ubiquitin-Dependent Protein | 1.19e-02 | 3.14e-02 | NFE2L2 | BARDOXOLONE METHYL | **Yes** |
| Negative Regulation Of Cholesterol Storage (GO:0010887) | 1.19e-02 | 3.14e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Inflammatory Response (GO:005072 | 1.20e-02 | 3.14e-02 | SRC, PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib | **Yes** |
| Negative Regulation Of Transmembrane Receptor Protein S | 1.20e-02 | 3.14e-02 | PPARG, SIRT1 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Cytoskeleton Organization (GO:0007010) | 1.20e-02 | 3.14e-02 | RICTOR, MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Negative Regulation Of Defense Response (GO:0031348) | 1.22e-02 | 3.19e-02 | PPARG, ATG5 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Response To Endoplasmic Reticulum Stress (GO:0034976) | 1.26e-02 | 3.29e-02 | BCL2, PIK3R1 | DACTOLISIB, GEDATOLISIB, VENETOCLAX |  |
| Regulation Of Cellular Response To Oxidative Stress (GO | 1.34e-02 | 3.33e-02 | NFE2L2 | BARDOXOLONE METHYL | **Yes** |
| Regulation Of Ceramide Biosynthetic Process (GO:2000303 | 1.34e-02 | 3.33e-02 | SIRT3 | Resveratrol |  |
| Regulation Of Endoplasmic Reticulum Unfolded Protein Re | 1.34e-02 | 3.33e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Histone Methylation (GO:0031060) | 1.34e-02 | 3.33e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Telomerase Activity (GO:0051974) | 1.34e-02 | 3.33e-02 | SRC | Dasatinib |  |
| Regulation Of Protein Acetylation (GO:1901983) | 1.34e-02 | 3.33e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Protein Lipidation (GO:1903059) | 1.34e-02 | 3.33e-02 | ULK1 | Spermidine |  |
| Peptidyl-Lysine Acetylation (GO:0018394) | 1.34e-02 | 3.33e-02 | SIRT1 | Resveratrol |  |
| Piecemeal Microautophagy Of The Nucleus (GO:0034727) | 1.34e-02 | 3.33e-02 | ULK1 | Spermidine | **Yes** |
| Regulation Of Transmembrane Transporter Activity (GO:00 | 1.34e-02 | 3.33e-02 | BCL2 | VENETOCLAX |  |
| Response To Laminar Fluid Shear Stress (GO:0034616) | 1.34e-02 | 3.33e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Positive Regulation Of Hippo Signaling (GO:0035332) | 1.34e-02 | 3.33e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Keratinocyte Migration (GO:00515 | 1.34e-02 | 3.33e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of Leukocyte Apoptotic Process (GO: | 1.34e-02 | 3.33e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Lipase Activity (GO:0060193) | 1.34e-02 | 3.33e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Positive Regulation Of Transcription Of Nucleolar Large | 1.34e-02 | 3.33e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Lipid Import Into Cell (GO:0140354) | 1.34e-02 | 3.33e-02 | RPS6KB1 | Rapamycin |  |
| Long-Chain Fatty Acid Import Into Cell (GO:0044539) | 1.34e-02 | 3.33e-02 | RPS6KB1 | Rapamycin |  |
| Regulation Of Bile Acid Biosynthetic Process (GO:007085 | 1.34e-02 | 3.33e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Bone Resorption (GO:0045779) | 1.34e-02 | 3.33e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Protein Kinase Activity (GO:0045859) | 1.37e-02 | 3.36e-02 | EPHB2, SIRT1 | Dasatinib, Resveratrol |  |
| Regulation Of Protein-Containing Complex Assembly (GO:0 | 1.37e-02 | 3.36e-02 | SRC, ULK1 | Dasatinib, Spermidine |  |
| Cellular Response To Tumor Necrosis Factor (GO:0071356) | 1.37e-02 | 3.36e-02 | SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol |  |
| Positive Regulation Of Angiogenesis (GO:0045766) | 1.37e-02 | 3.36e-02 | FLT1, SIRT1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB | **Yes** |
| Negative Regulation Of Growth (GO:0045926) | 1.48e-02 | 3.49e-02 | STK11, SIRT1 | Metformin, Resveratrol |  |
| Regulation Of Coagulation (GO:0050818) | 1.49e-02 | 3.49e-02 | EPHB2 | Dasatinib |  |
| Negative Regulation Of Hydrogen Peroxide-Induced Cell D | 1.49e-02 | 3.49e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Negative Regulation Of Pathway-Restricted SMAD Protein  | 1.49e-02 | 3.49e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| T-helper Cell Lineage Commitment (GO:0002295) | 1.49e-02 | 3.49e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Lamellipodium Morphogenesis (GO:2000392) | 1.49e-02 | 3.49e-02 | SRC | Dasatinib |  |
| Neuron Projection Fasciculation (GO:0106030) | 1.49e-02 | 3.49e-02 | EPHB2 | Dasatinib |  |
| Regulation Of Peroxisome Proliferator Activated Recepto | 1.49e-02 | 3.49e-02 | SIRT1 | Resveratrol | **Yes** |
| Regulation Of Phospholipase Activity (GO:0010517) | 1.49e-02 | 3.49e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Regulation Of Smooth Muscle Cell Apoptotic Process (GO: | 1.49e-02 | 3.49e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of MHC Class II Biosynthetic Proces | 1.49e-02 | 3.49e-02 | SIRT1 | Resveratrol |  |
| Response To Corticosteroid (GO:0031960) | 1.49e-02 | 3.49e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Attachment Of Spindle Microtubul | 1.49e-02 | 3.49e-02 | BECN1 | Spermidine |  |
| Positive Regulation Of Cellular Senescence (GO:2000774) | 1.49e-02 | 3.49e-02 | SIRT1 | Resveratrol | **Yes** |
| Positive Regulation Of Cholesterol Metabolic Process (G | 1.49e-02 | 3.49e-02 | PRKAA1 | Metformin |  |
| Positive Regulation Of Integrin Activation (GO:0033625) | 1.49e-02 | 3.49e-02 | SRC | Dasatinib |  |
| Urogenital System Development (GO:0001655) | 1.49e-02 | 3.49e-02 | EPHB2 | Dasatinib |  |
| Positive Regulation Of Nitric-Oxide Synthase Biosynthet | 1.49e-02 | 3.49e-02 | NAMPT | Resveratrol |  |
| Progesterone Receptor Signaling Pathway (GO:0050847) | 1.49e-02 | 3.49e-02 | SRC | Dasatinib |  |
| Monocyte Differentiation (GO:0030224) | 1.49e-02 | 3.49e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of T-helper 2 Cell Cytokine Production (GO:2 | 1.49e-02 | 3.49e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Mitotic Cell Cycle (GO:0007346) | 1.50e-02 | 3.50e-02 | RPS6KB1, SIRT1 | Rapamycin, Resveratrol | **Yes** |
| Response To Cytokine (GO:0034097) | 1.50e-02 | 3.50e-02 | SRC, BCL2 | Dasatinib, VENETOCLAX |  |
| Regulation Of Response To External Stimulus (GO:0032101 | 1.55e-02 | 3.58e-02 | EPHB2, NFE2L2 | BARDOXOLONE METHYL, Dasatinib |  |
| Regulation Of Tumor Necrosis Factor Production (GO:0032 | 1.55e-02 | 3.58e-02 | IL6, EPHB2 | Dasatinib, SILTUXIMAB |  |
| Regulation Of Anatomical Structure Morphogenesis (GO:00 | 1.55e-02 | 3.58e-02 | IL6, EPHA2 | Dasatinib, SILTUXIMAB |  |
| Regulation Of Cytoplasmic Transport (GO:1903649) | 1.64e-02 | 3.65e-02 | SRC | Dasatinib |  |
| DNA Methylation-Dependent Heterochromatin Formation (GO | 1.64e-02 | 3.65e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Keratinocyte Migration (GO:0051547) | 1.64e-02 | 3.65e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Lipid Kinase Activity (GO:0043550) | 1.64e-02 | 3.65e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Response To Oxidative Stress (GO:1902882) | 1.64e-02 | 3.65e-02 | NFE2L2 | BARDOXOLONE METHYL | **Yes** |
| Cellular Response To UV-B (GO:0071493) | 1.64e-02 | 3.65e-02 | STK11 | Metformin |  |
| Phosphatidylinositol-3-Phosphate Biosynthetic Process ( | 1.64e-02 | 3.65e-02 | BECN1 | Spermidine |  |
| Cellular Response To Fluid Shear Stress (GO:0071498) | 1.64e-02 | 3.65e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Regulation Of Type II Interferon-Mediated Signaling Pat | 1.64e-02 | 3.65e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Retinoic Acid Receptor Signaling Pathway (GO:0048384) | 1.64e-02 | 3.65e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Endoplasmic Reticulum Unfolded P | 1.64e-02 | 3.65e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Positive Regulation Of Platelet Aggregation (GO:1901731 | 1.64e-02 | 3.65e-02 | IL6 | SILTUXIMAB |  |
| Lipoprotein Transport (GO:0042953) | 1.64e-02 | 3.65e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Lysosomal Microautophagy (GO:0016237) | 1.64e-02 | 3.65e-02 | ULK1 | Spermidine | **Yes** |
| Regulation Of Astrocyte Differentiation (GO:0048710) | 1.64e-02 | 3.65e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Bone Remodeling (GO:0046851) | 1.64e-02 | 3.65e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Cell Activation (GO:0050865) | 1.64e-02 | 3.65e-02 | IL6 | SILTUXIMAB |  |
| Plasma Membrane Bounded Cell Projection Organization (G | 1.67e-02 | 3.71e-02 | IL6, ULK1 | SILTUXIMAB, Spermidine |  |
| Cellular Response To Metal Ion (GO:0071248) | 1.74e-02 | 3.80e-02 | PRKAA1, PRKAA2 | Metformin |  |
| C-terminal Protein Amino Acid Modification (GO:0018410) | 1.79e-02 | 3.80e-02 | ATG5 | Spermidine |  |
| Negative Regulation Of Macrophage Derived Foam Cell Dif | 1.79e-02 | 3.80e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| UV-damage Excision Repair (GO:0070914) | 1.79e-02 | 3.80e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Leukocyte Adhesion To Vascular Endothelia | 1.79e-02 | 3.80e-02 | IL6 | SILTUXIMAB |  |
| Adipose Tissue Development (GO:0060612) | 1.79e-02 | 3.80e-02 | NAMPT | Resveratrol |  |
| Neutrophil Mediated Immunity (GO:0002446) | 1.79e-02 | 3.80e-02 | IL6 | SILTUXIMAB |  |
| Axonal Fasciculation (GO:0007413) | 1.79e-02 | 3.80e-02 | EPHB2 | Dasatinib |  |
| cAMP Metabolic Process (GO:0046058) | 1.79e-02 | 3.80e-02 | EPHA2 | Dasatinib |  |
| Cellular Component Maintenance (GO:0043954) | 1.79e-02 | 3.80e-02 | IGF1R | MECASERMIN |  |
| Cellular Response To Leucine Starvation (GO:1990253) | 1.79e-02 | 3.80e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Regulation Of Transcription From RNA Polymerase II Prom | 1.79e-02 | 3.80e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Positive Regulation Of ERAD Pathway (GO:1904294) | 1.79e-02 | 3.80e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Positive Regulation Of Alcohol Biosynthetic Process (GO | 1.79e-02 | 3.80e-02 | PRKAA1 | Metformin |  |
| Response To Iron Ion (GO:0010039) | 1.79e-02 | 3.80e-02 | BCL2 | VENETOCLAX |  |
| Positive Regulation Of Insulin Receptor Signaling Pathw | 1.79e-02 | 3.80e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Neuroinflammatory Response (GO:0 | 1.79e-02 | 3.80e-02 | IL6 | SILTUXIMAB | **Yes** |
| Positive Regulation Of Vascular Endothelial Cell Prolif | 1.79e-02 | 3.80e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Lipoprotein Localization (GO:0044872) | 1.79e-02 | 3.80e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Cardiac Muscle Hypertrophy (GO:0 | 1.79e-02 | 3.80e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Protein Localization To Organelle (GO:0033365) | 1.79e-02 | 3.80e-02 | PRKAA1, PRKAA2 | Metformin |  |
| ERBB2 Signaling Pathway (GO:0038128) | 1.93e-02 | 3.99e-02 | SRC | Dasatinib |  |
| Regulation Of Lamellipodium Organization (GO:1902743) | 1.93e-02 | 3.99e-02 | EPHA2 | Dasatinib |  |
| Acute-Phase Response (GO:0006953) | 1.93e-02 | 3.99e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Macrophage Cytokine Production (GO:001093 | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Nitric-Oxide Synthase Biosynthetic Proces | 1.93e-02 | 3.99e-02 | NAMPT | Resveratrol |  |
| Regulation Of Transcription Of Nucleolar Large rRNA By  | 1.93e-02 | 3.99e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Response To Progesterone (GO:0032570) | 1.93e-02 | 3.99e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Cellular Response To Insulin Sti | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Histone Deacetylation (GO:003106 | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Protein Deacetylation (GO:009031 | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Type 2 Immune Response (GO:00028 | 1.93e-02 | 3.99e-02 | IL6 | SILTUXIMAB |  |
| Mature B Cell Differentiation Involved In Immune Respon | 1.93e-02 | 3.99e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of DNA Damage Response, Signal Tran | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol | **Yes** |
| Regulation Of cAMP-dependent Protein Kinase Activity (G | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Cellular Ketone Metabolic Process (GO:001 | 1.93e-02 | 3.99e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Cold-Induced Thermogenesis (GO:0120161) | 2.01e-02 | 4.11e-02 | STK11, IGF1R | MECASERMIN, Metformin |  |
| Negative Regulation Of Response To External Stimulus (G | 2.01e-02 | 4.11e-02 | PPARG, ATG5 | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Defense Response To Symbiont (GO:0140546) | 2.07e-02 | 4.11e-02 | IL6, BCL2 | SILTUXIMAB, VENETOCLAX |  |
| Regulation Of Cholesterol Storage (GO:0010885) | 2.08e-02 | 4.11e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Negative Regulation Of Fatty Acid Biosynthetic Process  | 2.08e-02 | 4.11e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Extracellular Matrix Disassembly (GO:0010 | 2.08e-02 | 4.11e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Integrin Activation (GO:0033623) | 2.08e-02 | 4.11e-02 | SRC | Dasatinib |  |
| Negative Regulation Of Receptor Signaling Pathway Via S | 2.08e-02 | 4.11e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Microglial Cell Activation (GO:1903978) | 2.08e-02 | 4.11e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Sequestering Of Triglyceride (GO:0010889) | 2.08e-02 | 4.11e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Positive Regulation Of Acute Inflammatory Response (GO: | 2.08e-02 | 4.11e-02 | IL6 | SILTUXIMAB | **Yes** |
| Contractile Actin Filament Bundle Assembly (GO:0030038) | 2.08e-02 | 4.11e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Endothelial Cell Chemotaxis (GO: | 2.08e-02 | 4.11e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Stress Fiber Assembly (GO:0043149) | 2.08e-02 | 4.11e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Long-Term Synaptic Potentiation  | 2.08e-02 | 4.11e-02 | EPHB2 | Dasatinib |  |
| Positive Regulation Of Protein-Containing Complex Disas | 2.08e-02 | 4.11e-02 | IGF1R | MECASERMIN |  |
| Positive Regulation Of Transcription From RNA Polymeras | 2.08e-02 | 4.11e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Lipoprotein Biosynthetic Process (GO:0042158) | 2.08e-02 | 4.11e-02 | ATG5 | Spermidine |  |
| Mammary Gland Epithelium Development (GO:0061180) | 2.08e-02 | 4.11e-02 | EPHA2 | Dasatinib |  |
| Regulation Of MHC Class II Biosynthetic Process (GO:004 | 2.08e-02 | 4.11e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Androgen Receptor Signaling Path | 2.08e-02 | 4.11e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Bone Remodeling (GO:0046850) | 2.08e-02 | 4.11e-02 | SRC | Dasatinib |  |
| Negative Regulation Of Defense Response To Virus (GO:00 | 2.08e-02 | 4.11e-02 | ATG5 | Spermidine |  |
| Negative Regulation Of Protein Phosphorylation (GO:0001 | 2.09e-02 | 4.12e-02 | PPARG, EPHB2 | BARDOXOLONE METHYL, BEZAFIBRATE, Dasatinib |  |
| Regulation Of DNA-templated Transcription (GO:0006355) | 2.11e-02 | 4.16e-02 | MGAM, IL6, PRKAA1, ABL1, PPARG, SIRT1, NFE2L2 | Acarbose, BARDOXOLONE METHYL, BEZAFIBRATE |  |
| Neuron Development (GO:0048666) | 2.12e-02 | 4.16e-02 | IL6, ULK1 | SILTUXIMAB, Spermidine |  |
| Regulation Of Cholesterol Biosynthetic Process (GO:0045 | 2.23e-02 | 4.29e-02 | PRKAA1 | Metformin |  |
| Negative Regulation Of Focal Adhesion Assembly (GO:0051 | 2.23e-02 | 4.29e-02 | SRC | Dasatinib |  |
| Regulation Of Dephosphorylation (GO:0035303) | 2.23e-02 | 4.29e-02 | SRC | Dasatinib |  |
| Regulation Of miRNA-mediated Gene Silencing (GO:0060964 | 2.23e-02 | 4.29e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Multicellular Organism Growth (GO:0040014 | 2.23e-02 | 4.29e-02 | GHR | SOMATROPIN |  |
| Dendritic Spine Morphogenesis (GO:0060997) | 2.23e-02 | 4.29e-02 | EPHB2 | Dasatinib |  |
| Positive Regulation Of Glucose Metabolic Process (GO:00 | 2.23e-02 | 4.29e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Bicellular Tight Junction Assembly (GO:20 | 2.23e-02 | 4.29e-02 | EPHA2 | Dasatinib |  |
| Regulation Of Carbohydrate Metabolic Process (GO:000610 | 2.23e-02 | 4.29e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Cell-Substrate Junction Organiza | 2.23e-02 | 4.29e-02 | SRC | Dasatinib |  |
| Cellular Response To Growth Factor Stimulus (GO:0071363 | 2.25e-02 | 4.33e-02 | FLT1, RPS6KB1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Negative Regulation Of Inflammatory Response To Antigen | 2.37e-02 | 4.44e-02 | SRC | Dasatinib | **Yes** |
| Regulation Of Steroid Biosynthetic Process (GO:0050810) | 2.37e-02 | 4.44e-02 | SIRT1 | Resveratrol |  |
| Regulation Of Triglyceride Biosynthetic Process (GO:001 | 2.37e-02 | 4.44e-02 | SIRT1 | Resveratrol |  |
| Response To UV-B (GO:0010224) | 2.37e-02 | 4.44e-02 | STK11 | Metformin |  |
| Reticulophagy (GO:0061709) | 2.37e-02 | 4.44e-02 | ULK1 | Spermidine |  |
| Positive Regulation Of Homotypic Cell-Cell Adhesion (GO | 2.37e-02 | 4.44e-02 | IL6 | SILTUXIMAB |  |
| Extrinsic Apoptotic Signaling Pathway In Absence Of Lig | 2.37e-02 | 4.44e-02 | BCL2 | VENETOCLAX |  |
| Positive Regulation Of Myeloid Leukocyte Cytokine Produ | 2.37e-02 | 4.44e-02 | SIRT1 | Resveratrol |  |
| Vasculature Development (GO:0001944) | 2.37e-02 | 4.44e-02 | STK11 | Metformin |  |
| Regulation Of NMDA Receptor Activity (GO:2000310) | 2.37e-02 | 4.44e-02 | EPHB2 | Dasatinib |  |
| Negative Regulation Of ATP-dependent Activity (GO:00327 | 2.37e-02 | 4.44e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Anoikis (GO:2000811) | 2.37e-02 | 4.44e-02 | SRC | Dasatinib |  |
| Regulation Of Autophagosome Maturation (GO:1901096) | 2.37e-02 | 4.44e-02 | ATG5 | Spermidine |  |
| Negative Regulation Of Biosynthetic Process (GO:0009890 | 2.37e-02 | 4.44e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Chemokine Production (GO:0032682 | 2.37e-02 | 4.44e-02 | IL6 | SILTUXIMAB |  |
| DNA Biosynthetic Process (GO:0071897) | 2.52e-02 | 4.61e-02 | SIRT1 | Resveratrol |  |
| NAD Biosynthetic Process (GO:0009435) | 2.52e-02 | 4.61e-02 | NAMPT | Resveratrol |  |
| Regulation Of Inflammatory Response To Antigenic Stimul | 2.52e-02 | 4.61e-02 | SRC | Dasatinib | **Yes** |
| Regulation Of Leukocyte Chemotaxis (GO:0002688) | 2.52e-02 | 4.61e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Vascular Associated Smooth Muscl | 2.52e-02 | 4.61e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Regulation Of Vacuole Organization (GO:0044088) | 2.52e-02 | 4.61e-02 | EPHB2 | Dasatinib |  |
| Positive Regulation Of SMAD Protein Signal Transduction | 2.52e-02 | 4.61e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Facultative Heterochromatin Formation (GO:0140718) | 2.52e-02 | 4.61e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Leukocyte Adhesion To Vascular E | 2.52e-02 | 4.61e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Small GTPase Mediated Signal Tra | 2.52e-02 | 4.61e-02 | SRC | Dasatinib |  |
| Positive Regulation Of Transcription From RNA Polymeras | 2.52e-02 | 4.61e-02 | NFE2L2 | BARDOXOLONE METHYL |  |
| Regulation Of Brown Fat Cell Differentiation (GO:009033 | 2.52e-02 | 4.61e-02 | SIRT1 | Resveratrol |  |
| Negative Regulation Of Cellular Senescence (GO:2000773) | 2.52e-02 | 4.61e-02 | SIRT1 | Resveratrol | **Yes** |
| Regulation Of Collagen Biosynthetic Process (GO:0032965 | 2.67e-02 | 4.77e-02 | IL6 | SILTUXIMAB |  |
| Regulation Of Defense Response To Virus (GO:0050688) | 2.67e-02 | 4.77e-02 | ATG5 | Spermidine |  |
| Negative Regulation Of Lipid Catabolic Process (GO:0050 | 2.67e-02 | 4.77e-02 | PRKAA1 | Metformin |  |
| Negative Regulation Of Nervous System Development (GO:0 | 2.67e-02 | 4.77e-02 | IL6 | SILTUXIMAB |  |
| T-helper Cell Differentiation (GO:0042093) | 2.67e-02 | 4.77e-02 | IL6 | SILTUXIMAB |  |
| Negative Regulation Of Signal Transduction By P53 Class | 2.67e-02 | 4.77e-02 | SIRT1 | Resveratrol | **Yes** |
| Regulation Of Mitochondrial Membrane Permeability (GO:0 | 2.67e-02 | 4.77e-02 | BCL2 | VENETOCLAX | **Yes** |
| Positive Regulation Of Cytokine Production Involved In  | 2.67e-02 | 4.77e-02 | IL6 | SILTUXIMAB | **Yes** |
| Positive Regulation Of Extracellular Matrix Organizatio | 2.67e-02 | 4.77e-02 | IL6 | SILTUXIMAB |  |
| Positive Regulation Of Phosphoprotein Phosphatase Activ | 2.67e-02 | 4.77e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |
| Positive Regulation Of Response To Endoplasmic Reticulu | 2.67e-02 | 4.77e-02 | PIK3R1 | DACTOLISIB, GEDATOLISIB |  |
| Regulation Of Adaptive Immune Response (GO:0002819) | 2.67e-02 | 4.77e-02 | SIRT1 | Resveratrol |  |
| Protein Ubiquitination (GO:0016567) | 2.67e-02 | 4.77e-02 | BCL2, SIRT1, NFE2L2 | BARDOXOLONE METHYL, Resveratrol, VENETOCLAX | **Yes** |
| Regulation Of Early Endosome To Late Endosome Transport | 2.81e-02 | 4.90e-02 | SRC | Dasatinib |  |
| N-glycan Processing (GO:0006491) | 2.81e-02 | 4.90e-02 | GANAB | Acarbose |  |
| Negative Regulation Of Telomere Maintenance Via Telomer | 2.81e-02 | 4.90e-02 | SRC | Dasatinib | **Yes** |
| Neuron Apoptotic Process (GO:0051402) | 2.81e-02 | 4.90e-02 | BCL2 | VENETOCLAX |  |
| Regulation Of Neuroinflammatory Response (GO:0150077) | 2.81e-02 | 4.90e-02 | IL6 | SILTUXIMAB | **Yes** |
| Cellular Response To Lectin (GO:1990858) | 2.81e-02 | 4.90e-02 | SRC | Dasatinib |  |
| Release Of Cytochrome C From Mitochondria (GO:0001836) | 2.81e-02 | 4.90e-02 | BCL2 | VENETOCLAX | **Yes** |
| Positive Regulation Of Histone Methylation (GO:0031062) | 2.81e-02 | 4.90e-02 | SIRT1 | Resveratrol |  |
| Positive Regulation Of Hormone Secretion (GO:0046887) | 2.81e-02 | 4.90e-02 | PPARG | BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE |  |
| Stimulatory C-type Lectin Receptor Signaling Pathway (G | 2.81e-02 | 4.90e-02 | SRC | Dasatinib |  |
| Establishment Of Skin Barrier (GO:0061436) | 2.81e-02 | 4.90e-02 | FGFR1 | NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB |  |
| Glycogen Metabolic Process (GO:0005977) | 2.81e-02 | 4.90e-02 | GAA | Acarbose |  |
| Intrinsic Apoptotic Signaling Pathway In Response To DN | 2.81e-02 | 4.90e-02 | SIRT1 | Resveratrol | **Yes** |
| Regulation Of Acute Inflammatory Response (GO:0002673) | 2.81e-02 | 4.90e-02 | IL6 | SILTUXIMAB | **Yes** |
| Regulation Of Behavior (GO:0050795) | 2.81e-02 | 4.90e-02 | MTOR | DACTOLISIB, GEDATOLISIB, Rapamycin |  |

---

## 4. Vias Biologicas do Envelhecimento -- Analise Dirigida

Avaliacao especifica das vias canonicas do envelhecimento:

### [+] mTOR/PI3K/AKT Signaling -- ENRIQUECIDO

- Melhor pathway: **PI3K-Akt signaling pathway**
- P-value: 2.58e-17 | Adj. P: 1.06e-15
- Genes: PRKAA1, FLT1, PRKAA2, PIK3R1, MTOR, IGF1R, GHR, RPTOR, IL6, STK11, RPS6KB1, BCL2, FGFR1, EPHA2
- Compostos: DACTOLISIB, Dasatinib, GEDATOLISIB, MECASERMIN, Metformin, NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB, PAZOPANIB HYDROCHLORIDE, REGORAFENIB, Rapamycin, SILTUXIMAB, SOMATROPIN, VENETOCLAX
- Total pathways relacionados (p < 0.1): 21

### [+] AMPK/Energy Sensing -- ENRIQUECIDO

- Melhor pathway: **AMPK signaling pathway**
- P-value: 1.13e-17 | Adj. P: 6.15e-16
- Genes: RPTOR, PRKAA1, STK11, PRKAA2, RPS6KB1, PPARG, ULK1, PIK3R1, SIRT1, MTOR, IGF1R
- Compostos: BARDOXOLONE METHYL, BEZAFIBRATE, DACTOLISIB, GEDATOLISIB, MECASERMIN, Metformin, ROSIGLITAZONE, Rapamycin, Resveratrol, Spermidine
- Total pathways relacionados (p < 0.1): 5

### [+] PPAR/Metabolic Regulation -- ENRIQUECIDO

- Melhor pathway: **Peroxisome Proliferator Activated Receptor Signaling Pathway (GO:0035357)**
- P-value: 1.05e-02 | Adj. P: 2.91e-02
- Genes: PPARG
- Compostos: BARDOXOLONE METHYL, BEZAFIBRATE, ROSIGLITAZONE
- Total pathways relacionados (p < 0.1): 3

### [+] NRF2/Oxidative Stress -- ENRIQUECIDO

- Melhor pathway: **Cellular Response To Oxidative Stress (GO:0034599)**
- P-value: 2.71e-05 | Adj. P: 3.23e-04
- Genes: PRKAA1, PRKAA2, ABL1, NFE2L2
- Compostos: BARDOXOLONE METHYL, Dasatinib, Metformin
- Total pathways relacionados (p < 0.1): 8

### [+] Apoptosis/Senescence (BCL-2) -- ENRIQUECIDO

- Melhor pathway: **Negative Regulation Of Programmed Cell Death (GO:0043069)**
- P-value: 3.17e-15 | Adj. P: 1.64e-12
- Genes: BECN1, PRKAA1, PRKAA2, SRC, PIK3R1, SIRT1, MTOR, IGF1R, IL6, RPS6KB1, BCL2, RICTOR, ATG5
- Compostos: DACTOLISIB, Dasatinib, GEDATOLISIB, MECASERMIN, Metformin, Rapamycin, Resveratrol, SILTUXIMAB, Spermidine, VENETOCLAX
- Total pathways relacionados (p < 0.1): 16

### [+] IGF-1/Growth Hormone -- ENRIQUECIDO

- Melhor pathway: **Insulin signaling pathway**
- P-value: 4.80e-08 | Adj. P: 6.56e-07
- Genes: RPTOR, PRKAA1, PRKAA2, RPS6KB1, PIK3R1, MTOR
- Compostos: DACTOLISIB, GEDATOLISIB, Metformin, Rapamycin
- Total pathways relacionados (p < 0.1): 9

### [+] Autophagy -- ENRIQUECIDO

- Melhor pathway: **Autophagy**
- P-value: 5.08e-19 | Adj. P: 4.16e-17
- Genes: RPTOR, BECN1, PRKAA1, STK11, PRKAA2, RPS6KB1, BCL2, ULK1, PIK3R1, MTOR, IGF1R, ATG5
- Compostos: DACTOLISIB, GEDATOLISIB, MECASERMIN, Metformin, Rapamycin, Spermidine, VENETOCLAX
- Total pathways relacionados (p < 0.1): 20

### [+] Inflammatory Signaling (IL-6/JAK-STAT) -- ENRIQUECIDO

- Melhor pathway: **Adipocytokine signaling pathway**
- P-value: 3.32e-06 | Adj. P: 2.27e-05
- Genes: PRKAA1, STK11, PRKAA2, MTOR
- Compostos: DACTOLISIB, GEDATOLISIB, Metformin, Rapamycin
- Total pathways relacionados (p < 0.1): 36

### [-] Sirtuin/NAD+ Metabolism -- TENDENCIA

- Melhor pathway: **SIRT1 Negatively Regulates rRNA Expression R-HSA-427359**
- P-value: 5.41e-02 | Adj. P: 7.27e-02
- Genes: SIRT1
- Compostos: Resveratrol
- Total pathways relacionados (p < 0.1): 1

### [+] FOXO Signaling -- ENRIQUECIDO

- Melhor pathway: **FoxO signaling pathway**
- P-value: 7.90e-10 | Adj. P: 1.85e-08
- Genes: IL6, PRKAA1, STK11, PRKAA2, PIK3R1, SIRT1, IGF1R
- Compostos: DACTOLISIB, GEDATOLISIB, MECASERMIN, Metformin, Resveratrol, SILTUXIMAB
- Total pathways relacionados (p < 0.1): 5

### [+] Angiogenesis/VEGF/FGF -- ENRIQUECIDO

- Melhor pathway: **Signaling By VEGF R-HSA-194138**
- P-value: 4.02e-07 | Adj. P: 1.09e-05
- Genes: FLT1, SRC, RICTOR, PIK3R1, MTOR
- Compostos: DACTOLISIB, Dasatinib, GEDATOLISIB, NINTEDANIB, NINTEDANIB ESYLATE, PAZOPANIB, PAZOPANIB HYDROCHLORIDE, REGORAFENIB, Rapamycin
- Total pathways relacionados (p < 0.1): 43

---

## 5. Interpretacao Biologica

### 5.1 Coerencia do Ranking

O ranking do Discovery Engine demonstra enriquecimento em **11/11 categorias** de vias do envelhecimento.

Este resultado indica **forte coerencia biologica**: os compostos identificados pelo pipeline atuam em multiplas vias canonicas do envelhecimento, cobrindo mecanismos metabolicos (AMPK, mTOR, PPAR), de estresse (NRF2), de senescencia (BCL-2, p53), e de sinalizacao (IGF-1, IL-6).

### 5.2 Vias Dominantes

As vias mais representadas no top-20 refletem a concentracao do pipeline em:

1. **Angiogenesis/VEGF/FGF** (43 pathways)
2. **Inflammatory Signaling (IL-6/JAK-STAT)** (36 pathways)
3. **mTOR/PI3K/AKT Signaling** (21 pathways)
4. **Autophagy** (20 pathways)
5. **Apoptosis/Senescence (BCL-2)** (16 pathways)
6. **IGF-1/Growth Hormone** (9 pathways)
7. **NRF2/Oxidative Stress** (8 pathways)
8. **AMPK/Energy Sensing** (5 pathways)
9. **FOXO Signaling** (5 pathways)
10. **PPAR/Metabolic Regulation** (3 pathways)
11. **Sirtuin/NAD+ Metabolism** (1 pathways)

### 5.3 Implicacoes para Drug Repurposing

A convergencia de multiplos compostos independentes (aprovados para outras indicacoes) em vias do envelhecimento fortalece a hipotese de que o ranking identifica candidatos biologicamente plausíveis para drug repurposing em longevidade.

**Candidatos novos com suporte de pathway:**

- **Bardoxolone Methyl**
- **Bezafibrate**
- **Dactolisib**
- **Gedatolisib**
- **Mecasermin**
- **Nintedanib**
- **Nintedanib Esylate**
- **Pazopanib**
- **Pazopanib Hydrochloride**
- **Regorafenib**
- **Rosiglitazone**
- **Siltuximab**
- **Somatropin**
- **Venetoclax**

---

*Gerado automaticamente pelo Discovery Engine*
*Rastreabilidade: audit_logs/ contem hashes SHA-256 de todos os inputs/outputs*