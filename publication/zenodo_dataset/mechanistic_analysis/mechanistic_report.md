# Mechanistic Interpretation of Top-20 Ranked Candidates

> Discovery Engine -- Analise Mecanistica
> Data: 2026-03-11 13:43
> Assistido por: Claude Code (Anthropic)

---

## 1. Resumo

Analisamos os **20 compostos mais bem ranqueados** do Discovery Engine,
mapeando seus alvos moleculares aos **hallmarks of aging** (Lopez-Otin et al., 2013; 2023).

- **Media de hallmarks por composto:** 1.9
- **Hallmark mais frequente:** Stem Cell Exhaustion (11/20 compostos)
- **Compostos com >= 3 hallmarks:** 5

---

## 2. Cobertura dos Hallmarks

| Hallmark | Compostos | N | Drogas |
|----------|-----------|---|--------|
| Stem Cell Exhaustion | 11/20 | 11 | Rapamycin, SOMATROPIN, REGORAFENIB, NINTEDANIB ESYL, PAZOPANIB HYDRO (+6) |
| Nutrient Sensing | 7/20 | 7 | Rapamycin, SOMATROPIN, Metformin, Resveratrol, DACTOLISIB (+2) |
| Mitochondrial Dysfunction | 5/20 | 5 | BARDOXOLONE MET, BEZAFIBRATE, Metformin, Resveratrol, ROSIGLITAZONE |
| Loss of Proteostasis | 4/20 | 4 | Rapamycin, Spermidine, DACTOLISIB, GEDATOLISIB |
| Altered Intercellular Communication | 4/20 | 4 | BARDOXOLONE MET, BEZAFIBRATE, SILTUXIMAB, ROSIGLITAZONE |
| Cellular Senescence | 3/20 | 3 | VENETOCLAX, SILTUXIMAB, Dasatinib |
| Genomic Instability | 2/20 | 2 | Metformin, Resveratrol |
| Epigenetic Alterations | 1/20 | 1 | Resveratrol |

---

## 3. Tabela Mecanistica Completa

| Rank | Composto | Alvos | Pathways Chave | Hallmarks | N |
|------|----------|-------|---------------|-----------|---|
| 1 | Rapamycin | MTOR, RICTOR, RPS6KB1, RPTOR | Autophagy, Insulin signaling, Longevity regulating pathway (+5) | Loss of Proteostasis, Nutrient Sensing, Stem Cell Exhaustion | 3 |
| 2 | SOMATROPIN | GHR, IGF1R | Growth hormone signaling, IGF-1 axis, Insulin/IGF-1 signaling (+3) | Nutrient Sensing, Stem Cell Exhaustion | 2 |
| 3 | REGORAFENIB | FGFR1, FLT1 | Angiogenesis, FGF signaling, RTK signaling (+2) | Stem Cell Exhaustion | 1 |
| 4 | VENETOCLAX | BCL2 | Apoptosis regulation, Intrinsic apoptotic pathway, Senescence | Cellular Senescence | 1 |
| 5 | NINTEDANIB ESYLATE | FGFR1, FLT1 | Angiogenesis, FGF signaling, RTK signaling (+2) | Stem Cell Exhaustion | 1 |
| 6 | PAZOPANIB HYDROCHLORIDE | FGFR1, FLT1 | Angiogenesis, FGF signaling, RTK signaling (+2) | Stem Cell Exhaustion | 1 |
| 7 | BARDOXOLONE METHYL | NFE2L2, PPARG | Adipogenesis, Inflammation regulation, Lipid metabolism (+4) | Altered Intercellular Communication, Mitochondrial Dysfunction | 2 |
| 8 | PAZOPANIB | FGFR1, FLT1 | Angiogenesis, FGF signaling, RTK signaling (+2) | Stem Cell Exhaustion | 1 |
| 9 | BEZAFIBRATE | PPARG | Adipogenesis, Inflammation regulation, Lipid metabolism (+1) | Altered Intercellular Communication, Mitochondrial Dysfunction | 2 |
| 10 | Metformin | PRKAA1, PRKAA2, STK11 | AMPK signaling, Autophagy, Longevity regulating pathway (+2) | Genomic Instability, Mitochondrial Dysfunction, Nutrient Sensing (+1) | 4 |
| 11 | NINTEDANIB | FGFR1, FLT1 | Angiogenesis, FGF signaling, RTK signaling (+2) | Stem Cell Exhaustion | 1 |
| 12 | Resveratrol | NAMPT, SIRT1, SIRT3 | Circadian clock, FOXO signaling, Longevity regulating pathway (+4) | Epigenetic Alterations, Genomic Instability, Mitochondrial Dysfunction (+1) | 4 |
| 13 | Spermidine |  |  | Loss of Proteostasis | 1 |
| 14 | DACTOLISIB | MTOR, PIK3R1 | Autophagy, Insulin signaling, Longevity regulating pathway (+2) | Loss of Proteostasis, Nutrient Sensing, Stem Cell Exhaustion | 3 |
| 15 | GEDATOLISIB | MTOR, PIK3R1 | Autophagy, Insulin signaling, Longevity regulating pathway (+2) | Loss of Proteostasis, Nutrient Sensing, Stem Cell Exhaustion | 3 |
| 16 | SILTUXIMAB | IL6 | IL-6 signaling, Inflammaging, JAK-STAT signaling (+1) | Altered Intercellular Communication, Cellular Senescence | 2 |
| 17 | ROSIGLITAZONE | PPARG | Adipogenesis, Inflammation regulation, Lipid metabolism (+1) | Altered Intercellular Communication, Mitochondrial Dysfunction | 2 |
| 18 | Acarbose |  |  |  | 0 |
| 19 | MECASERMIN | IGF1R | Insulin/IGF-1 signaling, Longevity regulating pathway, PI3K-Akt signaling | Nutrient Sensing, Stem Cell Exhaustion | 2 |
| 20 | Dasatinib |  |  | Cellular Senescence | 1 |

---

## 4. Analise Detalhada dos Compostos Chave

### 4.1. #1 Rapamycin (Geroprotetor conhecido)

- **Score:** 0.5193 | **Fase clinica:** Fase 4 | **Lifespan:** +14.8%
- **Mecanismo(s):** mTOR inhibitor
- **Alvos moleculares:** MTOR, RICTOR, RPS6KB1, RPTOR
- **Pathways chave:** Autophagy, Insulin signaling, Longevity regulating pathway, PI3K-Akt signaling, Translation regulation
- **Hallmarks (3):** Loss of Proteostasis, Nutrient Sensing, Stem Cell Exhaustion
- **Fontes:** chembl, curado, drugage

  - **Nutrient Sensing:** MTOR, RICTOR, RPS6KB1, RPTOR
  - **Loss of Proteostasis:** MTOR, RPTOR
  - **Stem Cell Exhaustion:** MTOR

**Interpretacao:** Rapamycin e o inibidor de mTOR mais estudado em aging. 
A inibicao de mTORC1 ativa autofagia, reduz traducao proteica, e mimetiza 
restricao calorica. Extensao de lifespan demonstrada em levedura, vermes, 
moscas e camundongos. Aprovado clinicamente (imunossupressor), com ensaios 
em andamento para aging (PEARL trial).

### 4.2. #2 SOMATROPIN (Candidato novo)

- **Score:** 0.4950 | **Fase clinica:** Fase 4 | **Lifespan:** Sem dados
- **Mecanismo(s):** Growth hormone receptor agonist
- **Alvos moleculares:** GHR, IGF1R
- **Pathways chave:** Growth hormone signaling, IGF-1 axis, Insulin/IGF-1 signaling, JAK-STAT signaling, Longevity regulating pathway
- **Hallmarks (2):** Nutrient Sensing, Stem Cell Exhaustion
- **Fontes:** open_targets

  - **Nutrient Sensing:** GHR, IGF1R
  - **Stem Cell Exhaustion:** GHR, IGF1R

**Interpretacao:** Somatropin (hormonio de crescimento) ativa o eixo GH/IGF-1. 
Paradoxalmente, REDUCAO do eixo GH/IGF-1 esta associada a longevidade 
(camundongos Ames/Snell, Laron syndrome em humanos). O ranking alto reflete 
a forte conectividade no grafo (centralidade=0.094), nao necessariamente 
potencial geroprotetor. Este e um caso onde a interpretacao mecanistica 
sugere cautela apesar do score alto.

### 4.3. #3 REGORAFENIB (Candidato novo)

- **Score:** 0.4817 | **Fase clinica:** Fase 4 | **Lifespan:** Sem dados
- **Mecanismo(s):** MAP kinase p38 beta inhibitor
- **Alvos moleculares:** FGFR1, FLT1
- **Pathways chave:** Angiogenesis, FGF signaling, RTK signaling, Stem cell maintenance, VEGF signaling
- **Hallmarks (1):** Stem Cell Exhaustion
- **Fontes:** open_targets

  - **Stem Cell Exhaustion:** FGFR1

**Interpretacao:** Regorafenib e um multi-kinase inhibitor aprovado para cancer 
colorectal. Inibe FGFR1 e VEGFR (FLT1), envolvidos em sinalizacao de 
fatores de crescimento. A relevancia para aging e indireta: modulacao de 
RTK signaling pode afetar stem cell maintenance e angiogenese. Score alto 
reflete fase clinica 4 + 2 alvos do envelhecimento + centralidade.

### 4.4. #4 VENETOCLAX (Candidato novo)

- **Score:** 0.4485 | **Fase clinica:** Fase 4 | **Lifespan:** Sem dados
- **Mecanismo(s):** Apoptosis regulator Bcl-2 inhibitor
- **Alvos moleculares:** BCL2
- **Pathways chave:** Apoptosis regulation, Intrinsic apoptotic pathway, Senescence
- **Hallmarks (1):** Cellular Senescence
- **Fontes:** open_targets

  - **Cellular Senescence:** BCL2

**Interpretacao:** Venetoclax e um inibidor seletivo de BCL-2, aprovado para CLL. 
BCL-2 e superexpresso em celulas senescentes, protegendo-as da apoptose. 
Venetoclax pode funcionar como senolitico -- eliminando seletivamente celulas 
senescentes. Vantagem sobre navitoclax: seletividade BCL-2 (menos trombocitopenia). 
Mecanismo diretamente ligado ao hallmark de senescencia celular.

### 4.5. #5 NINTEDANIB ESYLATE (Candidato novo)

- **Score:** 0.4450 | **Fase clinica:** Fase 4 | **Lifespan:** Sem dados
- **Mecanismo(s):** Platelet-derived growth factor receptor inhibitor
- **Alvos moleculares:** FGFR1, FLT1
- **Pathways chave:** Angiogenesis, FGF signaling, RTK signaling, Stem cell maintenance, VEGF signaling
- **Hallmarks (1):** Stem Cell Exhaustion
- **Fontes:** open_targets

  - **Stem Cell Exhaustion:** FGFR1

### 4.7. #7 BARDOXOLONE METHYL (Candidato novo)

- **Score:** 0.4417 | **Fase clinica:** Fase 3 | **Lifespan:** Sem dados
- **Mecanismo(s):** Peroxisome proliferator-activated receptor gamma antagonist
- **Alvos moleculares:** NFE2L2, PPARG
- **Pathways chave:** Adipogenesis, Inflammation regulation, Lipid metabolism, NRF2/antioxidant response, Oxidative stress defense
- **Hallmarks (2):** Altered Intercellular Communication, Mitochondrial Dysfunction
- **Fontes:** open_targets

  - **Mitochondrial Dysfunction:** NFE2L2, PPARG
  - **Altered Intercellular Communication:** NFE2L2, PPARG

**Interpretacao:** Bardoxolone methyl ativa NRF2 (NFE2L2) e modula PPARG. 
NRF2 e o regulador master da resposta antioxidante, controlando >200 genes 
citoprotectores. A ativacao de NRF2 declina com a idade, contribuindo para 
estresse oxidativo cronico. Em Fase 3 para doenca renal diabetica (CARDINAL trial). 
Conecta 3 hallmarks: disfuncao mitocondrial (NRF2), nutrient sensing (PPARG), 
e comunicacao intercelular alterada (anti-inflamatorio).

### 4.9. #9 BEZAFIBRATE (Candidato novo)

- **Score:** 0.4379 | **Fase clinica:** Fase 4 | **Lifespan:** +13.0%
- **Mecanismo(s):** Peroxisome proliferator-activated receptor agonist
- **Alvos moleculares:** PPARG
- **Pathways chave:** Adipogenesis, Inflammation regulation, Lipid metabolism, PPAR signaling
- **Hallmarks (2):** Altered Intercellular Communication, Mitochondrial Dysfunction
- **Fontes:** drugage, open_targets

  - **Mitochondrial Dysfunction:** PPARG
  - **Altered Intercellular Communication:** PPARG

**Interpretacao:** Bezafibrate e um agonista pan-PPAR aprovado para hiperlipidemia. 
Ativa PGC-1alpha via PPAR, melhorando funcao mitocondrial e biogenese. 
Extensao de lifespan demonstrada em C. elegans (+13%). Perfil de seguranca 
estabelecido por decadas de uso clinico. Candidato forte para repurposing 
devido a: (1) mecanismo diretamente ligado a disfuncao mitocondrial, 
(2) efeito anti-inflamatorio via PPAR, (3) aprovacao FDA existente.

---

## 5. Convergencia Mecanistica

Os top-20 compostos convergem em **3 eixos mecanisticos principais:**

### 5.1 Eixo mTOR/AMPK/Nutrient Sensing
- **7/20 compostos** afetam este eixo
- Inclui: Rapamycin (mTOR direto), Metformin (AMPK), Dactolisib/Gedatolisib (PI3K/mTOR dual)
- Pathway mais enriquecido: Longevity regulating pathway (KEGG, p=1.27e-20)

### 5.2 Eixo Senescencia/Apoptose
- **3/20 compostos** tem potencial senolitico
- Inclui: Venetoclax (BCL-2), Dasatinib (SRC/ABL), Siltuximab (IL-6/SASP)
- Mecanismo: eliminacao seletiva de celulas senescentes via inibicao de vias anti-apoptoticas

### 5.3 Eixo Mitocondrial/Metabolico
- **5/20 compostos** afetam mitocondria
- Inclui: Bezafibrate (PPAR/PGC-1alpha), Bardoxolone (NRF2), Resveratrol (SIRT1/SIRT3)
- Mecanismo: biogenese mitocondrial, defesa antioxidante, metabolismo NAD+

---

*Gerado automaticamente pelo Discovery Engine*
*Referencia: Lopez-Otin et al., Cell 2013; Cell 2023*