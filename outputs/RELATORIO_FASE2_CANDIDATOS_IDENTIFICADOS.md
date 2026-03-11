# Relatorio Fase 2: Candidatos Identificados

> Discovery Engine -- Identificacao computacional de compostos geroprotetores
> Data: 2026-03-11 | Sessao #5 | Operador: Tercio Silas
> Assistido por: Claude Code (Anthropic)

---

## Resumo Executivo

A Fase 2 cruzou os 376 papers do acervo com 5 bases de dados publicas
para identificar **162 compostos candidatos a geroprotetores**, ranqueados
por um score multi-feature. Os controles positivos (rapamycin #1, metformin #10)
validaram a metodologia.

**Resultado principal:** Alem dos 13 geroprotetores conhecidos, identificamos
compostos como **Bezafibrate** (PPAR agonist, +13% lifespan, fase 4),
**Dactolisib** (dual PI3K/mTOR inhibitor, fase 3), e **Bardoxolone methyl**
(NRF2 activator, fase 3) como candidatos promissores para drug repurposing
em longevidade.

---

## 1. Pipeline Executado

### 1.1 Extracao de Alvos Proteicos (Bloco 2A)

- **Metodo:** Dicionario curado (GenAge 307 genes + 15 alvos-chave + 40+ aliases)
  com regex word-boundary matching nos abstracts
- **Resultado:** 80 genes/proteinas unicos extraidos de 152 papers (40.4% cobertura)
- **Top 50 consolidados** com Ensembl IDs via MyGene.info (100% cobertura)

**Top 10 alvos por numero de papers:**

| Rank | Gene | Papers | Via/Pathway |
|------|------|--------|-------------|
| 1 | MTOR | 18 | mTOR/PI3K/AKT |
| 2 | AMPK | 16 | Energy sensing |
| 3 | UBB | 14 | Proteostasis |
| 4 | IGF1 | 10 | Insulin/IGF-1 signaling |
| 5 | SIRT1 | 9 | Sirtuinas/NAD+ |
| 6 | CDKN2A | 6 | p16/Senescence |
| 7 | APOE | 5 | Lipid metabolism |
| 8 | PRKAA1 | 5 | AMPK catalytic |
| 9 | TP53 | 5 | p53/Senescence |
| 10 | FOXO3 | 5 | FOXO/Insulin signaling |

### 1.2 Consulta a Bases de Drogas (Bloco 2B)

**Open Targets Platform:**
- 50 alvos consultados via GraphQL API
- 1,118 associacoes droga-alvo-doenca encontradas
- 150 drogas unicas do Open Targets

**ChEMBL:**
- 12 geroprotetores consultados para atividades biologicas
- 7 com dados de pChEMBL (potencia)
- Rapamycin pChEMBL melhor: 8.26 (excelente)

**DrugAge:**
- 1,046 compostos com dados de lifespan em modelo animal
- 10 candidatos cruzados com dados de extensao de vida
- Spermidine: +60.5% lifespan medio (maior efeito)

### 1.3 Grafo de Conhecimento (Bloco 2C)

- **479 nos:** 50 proteinas + 162 drogas + 267 doencas
- **898 arestas:** protein-drug (targets) + drug-disease (indication)
- **51 comunidades** detectadas (Louvain/greedy modularity)
- **Maior componente:** 433 nos (90% conectado)

**Proteinas mais centrais (hub proteins):**
1. PPARG (grau=21, betweenness=0.079)
2. FLT1 (grau=21, betweenness=0.024)
3. PIK3R1 (grau=20, betweenness=0.010)
4. MTOR (grau=15, betweenness=0.031)
5. FGFR1 (grau=15, betweenness=0.012)

### 1.4 Ranqueamento (Bloco 2D)

**Formula de scoring (6 features ponderadas):**

| Feature | Peso | Logica |
|---------|------|--------|
| Fase clinica | 20% | Aprovado=1.0, Fase 3=0.75, Fase 2=0.5 |
| N. alvos envelhecimento | 20% | Normalizado min-max |
| Efeito lifespan (DrugAge) | 20% | Sigmoid: 10%=0.5, 30%=0.75 |
| Potencia (pChEMBL) | 10% | >=8=excelente, >=6=ativo |
| Evidencia literatura | 15% | Geroprotetor=0.8, outros=0.3 |
| Centralidade no grafo | 15% | Normalizado min-max |

---

## 2. Ranking Final: Top 30 Candidatos

| Rank | Composto | Score | Fase | Alvos | Lifespan | Tipo |
|------|----------|-------|------|-------|----------|------|
| **1** | **Rapamycin** | **0.519** | 4 | 0 | +14.8% | Geroprotetor conhecido |
| 2 | Somatropin | 0.495 | 4 | 1 | 0.0% | GH receptor |
| 3 | Regorafenib | 0.482 | 4 | 2 | 0.0% | Multi-kinase inhibitor |
| 4 | Venetoclax | 0.448 | 4 | 1 | 0.0% | BCL-2 inhibitor |
| 5 | Nintedanib esylate | 0.445 | 4 | 2 | 0.0% | FGFR/FLT inhibitor |
| 6 | Pazopanib HCl | 0.445 | 4 | 2 | 0.0% | Multi-kinase |
| 7 | Bardoxolone methyl | 0.442 | 3 | 2 | 0.0% | NRF2 activator |
| 8 | Pazopanib | 0.442 | 3 | 2 | 0.0% | Multi-kinase |
| **9** | **Bezafibrate** | **0.438** | 4 | 1 | +13.0% | PPAR agonist |
| **10** | **Metformin** | **0.438** | 4 | 0 | +9.9% | Geroprotetor conhecido |
| 11 | Nintedanib | 0.435 | 3 | 2 | 0.0% | FGFR/FLT inhibitor |
| **12** | **Resveratrol** | **0.435** | 3 | 0 | +7.2% | Geroprotetor conhecido |
| **13** | **Spermidine** | **0.426** | 2 | 0 | **+60.5%** | Geroprotetor conhecido |
| 14 | Dactolisib | 0.425 | 3 | 2 | 0.0% | Dual PI3K/mTOR |
| 15 | Gedatolisib | 0.422 | 3 | 2 | 0.0% | Dual PI3K/mTOR |
| 16 | Siltuximab | 0.412 | 4 | 1 | 0.0% | Anti-IL6 |
| 17 | Rosiglitazone | 0.402 | 4 | 1 | 0.0% | PPAR-gamma agonist |
| **18** | **Acarbose** | **0.399** | 4 | 0 | +9.8% | Geroprotetor conhecido |
| 19 | Mecasermin | 0.398 | 4 | 1 | 0.0% | IGF-1 receptor |
| **20** | **Dasatinib** | **0.396** | 4 | 0 | 0.0% | Geroprotetor conhecido |

---

## 3. Insights Principais

### 3.1 Candidatos Novos (nao-geroprotetores conhecidos)

| Composto | Score | Por que e interessante |
|----------|-------|----------------------|
| **Bezafibrate** | 0.438 | PPAR agonist aprovado, +13% lifespan, pleiotropico |
| **Bardoxolone methyl** | 0.442 | Ativa NRF2 + PPARG, fase 3, nefropatia diabetica |
| **Dactolisib** | 0.425 | Dual PI3K/mTOR inhibitor (mesma via rapamycin), fase 3 |
| **Venetoclax** | 0.448 | BCL-2 inhibitor (senolitico?), aprovado para leucemia |
| **Siltuximab** | 0.412 | Anti-IL6 (inflamaging), aprovado |

### 3.2 Vias Biologicas Dominantes

1. **mTOR/PI3K/AKT** -- Rapamycin, Dactolisib, Gedatolisib, SF-1126
2. **Senescence/BCL-2** -- Venetoclax, Navitoclax, Dasatinib
3. **PPAR/Metabolismo** -- Bezafibrate, Rosiglitazone, Bardoxolone
4. **Sirtuinas/NAD+** -- Resveratrol, NMN, NR
5. **Insulin/IGF-1** -- Somatropin, Mecasermin, Metformin

### 3.3 Validacao dos Controles

- Rapamycin #1 (esperado: top 3) -- **OK**
- Metformin #10 (esperado: top 10) -- **OK**
- Resveratrol #12 (esperado: top 20) -- **OK**
- Spermidine #13 (esperado: top 20) -- **OK**
- Acarbose #18 (esperado: top 30) -- **OK**
- Dasatinib #20 (esperado: top 30) -- **OK**

---

## 4. Limitacoes

1. **Alvos dos geroprotetores nao conectados no grafo** -- Open Targets retorna
   drogas em clinical trials, nao geroprotetores off-label. Os 13 foram injetados
   manualmente sem conexao protein-drug no grafo.

2. **Limite de 100 associacoes por alvo** -- Alguns alvos (MTOR, BCL2, PPARG)
   podem ter mais de 100 drogas associadas. Aumentar o limite na Fase 3.

3. **Lifespan data limitado** -- Apenas 10/162 candidatos tem dados DrugAge.
   Compostos novos (nao testados em modelo animal) nao tem esse feature.

4. **Score de literatura simplificado** -- Geroprotetores recebem 0.8 fixo.
   Na Fase 3, usar contagem real de papers + citacoes como evidencia.

5. **Sem docking molecular** -- Validacao computacional de binding sera feita
   na Fase 3 (T-062).

---

## 5. Arquivos Gerados

| Arquivo | Descricao | Tamanho |
|---------|-----------|---------|
| `protein_ranking_*.json` | Ranking de 80 genes/proteinas | 20 KB |
| `protein_extraction_*.json` | Extracao por paper | ~150 KB |
| `top50_alvos_consolidados_*.json` | 50 alvos com Ensembl IDs | 15 KB |
| `drug_target_associations_*.json` | 1118 associacoes OT | 478 KB |
| `drug_candidates_*.json` | 162 candidatos consolidados | 117 KB |
| `knowledge_graph_*.json` | Grafo (479 nos, 898 arestas) | 123 KB |
| `graph_metrics_*.json` | Metricas de centralidade | 17 KB |
| `graph_communities_*.json` | 51 comunidades | 14 KB |
| `ranked_candidates_*.json` | 162 candidatos ranqueados | 118 KB |

---

## 6. Proximos Passos (Fase 3)

1. Validacao cruzada com literatura existente
2. Analise de seguranca (FAERS/SIDER)
3. Reproducibilidade (3 execucoes, bootstrap 1000x)
4. Cross-validation do scoring
5. Ablation study (remover features uma a uma)
6. Controle negativo (drogas ineficazes fora do top 50)
7. Docking molecular (se viavel com AutoDock Vina)

---

*Gerado automaticamente pelo Discovery Engine v0.2*
*Rastreabilidade: audit_logs/ contem hashes SHA-256 de todos os inputs/outputs*
