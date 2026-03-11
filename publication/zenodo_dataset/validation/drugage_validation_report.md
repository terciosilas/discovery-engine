# External Validation Against DrugAge

> Discovery Engine -- Validacao Externa
> Data: 2026-03-11 13:18
> Assistido por: Claude Code (Anthropic)

---

## 1. Resumo Executivo

Cruzamos os **162 compostos** do ranking Discovery Engine com a base **DrugAge** (Build 5, 1,046 compostos unicos na base).

- **11 compostos** do ranking estao presentes no DrugAge
- **10** destes tem efeito positivo em lifespan
- **Precision@10:** 30.00%
- **Precision@20:** 30.00%
- **Precision@50:** 16.00%
- **Enrichment Factor@20:** 4.42x (vs. aleatorio)
- **Media rank DrugAge:** 41.2 (vs. 84.4 para nao-DrugAge)

- **Mann-Whitney U:** 387.0, p = 1.59e-03 (significativa)

---

## 2. Compostos DrugAge Encontrados no Ranking

| Rank | Composto | Score | DrugAge Name | Estudos | Especies | Avg Lifespan % | Melhor % | Efeito + |
|------|----------|-------|-------------|---------|----------|----------------|----------|----------|
| 1 | Rapamycin | 0.5193 | Rapamycin | 37 | Caenorhabditis elegans, Drosophila melanogaster, M | 14.4% | 38.4% | Sim |
| 9 | BEZAFIBRATE | 0.4379 | Bezafibrate | 1 | Caenorhabditis elegans | 13.0% | 13.0% | Sim |
| 10 | Metformin | 0.4375 | Metformin | 54 | Acheta domesticus, Caenorhabditis elegans, Drosoph | 9.0% | 79.0% | Sim |
| 12 | Resveratrol | 0.4346 | Resveratrol | 170 | Aedes aegypti, Anastrepha ludens, Anopheles stephe | 6.2% | 70.0% | Sim |
| 13 | Spermidine | 0.4263 | Spermidine | 8 | Adineta vaga, Caenorhabditis elegans, Drosophila m | 60.5% | 233.0% | Sim |
| 18 | Acarbose | 0.3989 | Acarbose | 10 | Mus musculus | 8.8% | 22.0% | Sim |
| 23 | Quercetin | 0.3927 | Quercetin | 38 | Aedes aegypti, Aedes albopictus, Caenorhabditis el | 8.9% | 59.9% | Sim |
| 24 | Fisetin | 0.3862 | Fisetin | 7 | Drosophila melanogaster, Mus musculus, Saccharomyc | 12.9% | 55.0% | Sim |
| 79 | PICTILISIB | 0.3230 | Pictilisib | 1 | Caenorhabditis elegans | 9.6% | 9.6% | Sim |
| 116 | Nicotinamide riboside | 0.2857 | Nicotinamide riboside | 4 | Mus musculus, Saccharomyces cerevisiae | 5.5% | 20.0% | Sim |
| 148 | Nicotinamide mononucleotide | 0.2200 | Nicotinamide mononucleotide | 1 | Drosophila melanogaster | 0.0% | 0.0% | Nao |

---

## 3. Metricas de Validacao

| Metrica | Valor | Interpretacao |
|---------|-------|---------------|
| Precision@10 | 30.00% | 3/10 do top-10 sao DrugAge |
| Precision@20 | 30.00% | 6/20 do top-20 sao DrugAge |
| Precision@50 | 16.00% | 8/50 do top-50 sao DrugAge |
| Recall@10 | 27.27% | Fracao dos DrugAge encontrados no top-10 |
| Recall@20 | 54.55% | Fracao dos DrugAge encontrados no top-20 |
| Recall@50 | 72.73% | Fracao dos DrugAge encontrados no top-50 |
| Recall Total | 100.00% | Todos os DrugAge presentes no ranking foram encontrados |
| EF@10 | 4.42x | Melhor que aleatorio no top-10 |
| EF@20 | 4.42x | Melhor que aleatorio no top-20 |
| EF@50 | 2.36x | Melhor que aleatorio no top-50 |
| Media Rank (DrugAge) | 41.2 | Posicao media dos compostos DrugAge |
| Media Rank (nao-DrugAge) | 84.4 | Posicao media dos demais compostos |
| Media Rank (efeito +) | 30.5 | Posicao media dos DrugAge com efeito positivo |

---

## 4. Compostos DrugAge no Top-20

**6 compostos** do top-20 estao no DrugAge:

- **#1 Rapamycin** (geroprotetor conhecido): 37 estudos DrugAge, +14.4% lifespan medio
- **#9 BEZAFIBRATE** (candidato novo): 1 estudos DrugAge, +13.0% lifespan medio
- **#10 Metformin** (geroprotetor conhecido): 54 estudos DrugAge, +9.0% lifespan medio
- **#12 Resveratrol** (geroprotetor conhecido): 170 estudos DrugAge, +6.2% lifespan medio
- **#13 Spermidine** (geroprotetor conhecido): 8 estudos DrugAge, +60.5% lifespan medio
- **#18 Acarbose** (geroprotetor conhecido): 10 estudos DrugAge, +8.8% lifespan medio

---

## 5. Interpretacao Estatistica

O Enrichment Factor de **4.42x** no top-20 indica enriquecimento **forte** de compostos DrugAge nas posicoes mais altas do ranking.

A media de rank dos compostos DrugAge (41.2) e significativamente menor que a dos demais compostos (84.4), indicando que o Discovery Engine prioriza compostos com evidencia experimental de extensao de lifespan.

O teste Mann-Whitney U (U=387.0, p=1.59e-03) confirma que a diferenca e estatisticamente significativa (hipotese alternativa: ranks DrugAge < ranks nao-DrugAge).

### 5.1 Consideracoes Importantes

- O DrugAge contem compostos testados em diversas especies (C. elegans, Drosophila, Mus musculus, etc.), nem todos com efeito positivo em lifespan
- Compostos com efeito negativo (reduzem lifespan) tambem estao no DrugAge
- O Discovery Engine usa lifespan_efeito como uma das 6 features (peso 20%), portanto existe correlacao parcial esperada
- A validacao mais relevante e para compostos DrugAge que o pipeline NAO usou como controles positivos (descobertas genuinas como bezafibrate)

---

*Gerado automaticamente pelo Discovery Engine*
*Rastreabilidade: audit_logs/ contem hashes SHA-256 de todos os inputs/outputs*