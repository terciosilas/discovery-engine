# Editorial Manager -- Ordem de Upload dos Arquivos

**Journal:** GeroScience (Springer Nature)
**Portal:** https://www.editorialmanager.com/jaaa/
**Article Type:** Original Research Article
**Data:** 2026-03-11

---

## Ordem de Upload

O Editorial Manager solicita arquivos em categorias especificas. Seguir esta ordem:

### Step 1: Cover Letter

| # | Arquivo | Tipo no EM | Tamanho |
|---|---------|-----------|---------|
| 1 | `COVER_LETTER_GEROSCIENCE.docx` | Cover Letter | 12 KB |

### Step 2: Manuscrito Principal

| # | Arquivo | Tipo no EM | Tamanho |
|---|---------|-----------|---------|
| 2 | `PAPER_GEROSCIENCE_SUBMISSION.docx` | Manuscript | 24 KB |

### Step 3: Figuras Principais (upload individual, na ordem)

| # | Arquivo | Tipo no EM | Tamanho | Legenda |
|---|---------|-----------|---------|---------|
| 3 | `fig1_pipeline_overview.png` | Figure | 202 KB | Fig. 1 -- Discovery Engine pipeline overview |
| 4 | `fig2_top20_ranking.png` | Figure | 192 KB | Fig. 2 -- Top-20 geroprotector candidates |
| 5 | `fig3_bootstrap_stability.png` | Figure | 219 KB | Fig. 3 -- Bootstrap ranking stability |
| 6 | `fig4_ablation_study.png` | Figure | 144 KB | Fig. 4 -- Feature ablation study |
| 7 | `fig5_sensitivity_analysis.png` | Figure | 127 KB | Fig. 5 -- Weight sensitivity analysis |

### Step 4: Material Suplementar

| # | Arquivo | Tipo no EM | Tamanho | Descricao |
|---|---------|-----------|---------|-----------|
| 8 | `supplementary/Figure_S1_external_validation_benchmark.png` | Supplementary Material | 382 KB | Fig. S1 -- External validation and benchmark |
| 9 | `supplementary/Figure_S2_mechanistic_network.png` | Supplementary Material | 1,250 KB | Fig. S2 -- Mechanistic network (drugs-targets-hallmarks) |
| 10 | `supplementary/Table_S1_full_ranking.csv` | Supplementary Material | 17 KB | Table S1 -- Complete ranking of 162 compounds |
| 11 | `supplementary/Table_S2_search_queries.md` | Supplementary Material | 2 KB | Table S2 -- PubMed search queries |
| 12 | `supplementary/Table_S3_bootstrap_top20.csv` | Supplementary Material | 1 KB | Table S3 -- Bootstrap statistics for top 20 |
| 13 | `supplementary/Table_S4_ablation_results.csv` | Supplementary Material | 1 KB | Table S4 -- Ablation study results |
| 14 | `supplementary/Table_S5_sensitivity_configs.csv` | Supplementary Material | 1 KB | Table S5 -- Sensitivity analysis configurations |
| 15 | `supplementary/Table_S6_graph_metrics.csv` | Supplementary Material | 1 KB | Table S6 -- Knowledge graph metrics |
| 16 | `supplementary/Table_S7_aging_targets.csv` | Supplementary Material | 4 KB | Table S7 -- Aging-associated targets |

### Totais

| Categoria | Quantidade | Tamanho Total |
|-----------|-----------|---------------|
| Cover Letter | 1 | 12 KB |
| Manuscrito | 1 | 24 KB |
| Figuras principais | 5 | 884 KB |
| Material suplementar | 9 | 1,659 KB |
| **Total** | **16 arquivos** | **~2.6 MB** |

---

## Notas Importantes

1. **Formato das figuras:** PNG 300 DPI aceito para submissao inicial. TIFF so sera exigido apos aceitacao.
2. **Tabelas suplementares em CSV:** O Editorial Manager aceita CSV. Se pedir outro formato, converter para XLSX com `openpyxl`.
3. **Table_S2 em Markdown:** Se o sistema nao aceitar .md, converter para .docx com `pandoc Table_S2_search_queries.md -o Table_S2_search_queries.docx`.
4. **Todos os arquivos estao em:** `submission/submission_package/`
5. **Preprint (discovery_engine_preprint.docx):** NAO enviar ao GeroScience -- este e exclusivo para bioRxiv.

---

## Verificacao Pre-Upload

- [ ] Todos os 16 arquivos presentes no diretorio
- [ ] DOCX abrem corretamente no Word/LibreOffice
- [ ] Figuras PNG abrem e estao legiveis
- [ ] CSVs abrem corretamente (encoding UTF-8)
- [ ] Email no manuscrito: terciosilas@gmail.com (confirmado)
- [ ] Abstract com 248 palavras (dentro do limite 150-250)
- [ ] Referencias numeradas [1]-[11] com DOIs

---

*Gerado pelo Discovery Engine pipeline -- T-079*
