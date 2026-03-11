# Zenodo Upload Checklist

**Dataset:** Discovery Engine -- Geroprotective Compound Candidates
**Version:** 1.0
**Data:** 2026-03-11

---

## 1. Pre-Upload Verification

- [x] Dataset organizado em `publication/zenodo_dataset/` (25 arquivos, 6 diretorios)
- [x] README_dataset.md com descricao, colunas, instrucoes de uso
- [x] LICENSE (CC-BY-4.0)
- [x] ZENODO_METADATA.json com metadados completos
- [x] Repositorio GitHub publico (https://github.com/terciosilas/discovery-engine)
- [x] Nenhum dado sensivel ou credencial nos arquivos
- [x] Figuras em 300 DPI, formato PNG

## 2. Arquivos para Upload

### ranking/ (1 arquivo)
- [ ] `ranked_candidates_162.csv` -- Ranking completo dos 162 compostos

### validation/ (3 arquivos)
- [ ] `drugage_validation.csv` -- Cruzamento com DrugAge
- [ ] `drugage_validation_figure.png` -- Figura de validacao
- [ ] `drugage_validation_report.md` -- Relatorio estatistico

### mechanistic_analysis/ (3 arquivos)
- [ ] `mechanistic_mapping.csv` -- Mapeamento hallmarks of aging
- [ ] `mechanistic_network.png` -- Rede drogas-alvos-hallmarks
- [ ] `mechanistic_report.md` -- Relatorio mecanistico

### knowledge_graph/ (3 arquivos)
- [ ] `knowledge_graph.json` -- Grafo completo (479 nos, 898 arestas)
- [ ] `graph_metrics.json` -- Metricas de centralidade
- [ ] `graph_communities.json` -- Comunidades detectadas

### figures/ (7 arquivos)
- [ ] `fig1_pipeline_overview.png`
- [ ] `fig2_top20_ranking.png`
- [ ] `fig3_bootstrap_stability.png`
- [ ] `fig4_ablation_study.png`
- [ ] `fig5_sensitivity_analysis.png`
- [ ] `Figure_S1_external_validation_benchmark.png`
- [ ] `Figure_S2_mechanistic_network.png`

### supplementary_tables/ (8 arquivos)
- [ ] `Table_S1_full_ranking.csv`
- [ ] `Table_S2_search_queries.md`
- [ ] `Table_S3_bootstrap_top20.csv`
- [ ] `Table_S4_ablation_results.csv`
- [ ] `Table_S5_sensitivity_configs.csv`
- [ ] `Table_S6_graph_metrics.csv`
- [ ] `Table_S7_aging_targets.csv`

### Root (2 arquivos)
- [ ] `README_dataset.md`
- [ ] `LICENSE`

**Total: 25 arquivos**

## 3. Metadados Zenodo

| Campo | Valor |
|-------|-------|
| Titulo | Discovery Engine Dataset: Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis |
| Tipo | Dataset |
| Acesso | Open Access |
| Licenca | CC-BY-4.0 |
| Autor | Azevedo, Tercio S. |
| Afiliacao | Independent Researcher, Sao Carlos, SP, Brazil |
| Data | 2026-03-11 |
| Versao | 1.0 |
| Idioma | English |
| Keywords | drug repurposing, geroprotectors, aging, longevity, computational biology, knowledge graph, DrugAge, GenAge, mTOR, senolytics |
| Related | https://github.com/terciosilas/discovery-engine (isSupplementTo) |

Arquivo de metadados: `publication/ZENODO_METADATA.json`

## 4. Passos para Gerar o DOI

### Opcao A: Upload Manual via Zenodo Web

1. Acessar https://zenodo.org e fazer login (ou criar conta)
2. Clicar "New Upload"
3. Fazer upload do ZIP `discovery-engine-dataset-v1.0.zip`
4. Preencher metadados conforme `ZENODO_METADATA.json`:
   - Upload type: Dataset
   - Title: (copiar do JSON)
   - Authors: Azevedo, Tercio S.
   - Description: (copiar HTML do JSON)
   - License: Creative Commons Attribution 4.0
   - Keywords: (copiar do JSON)
   - Related identifiers: GitHub repo URL, relation "isSupplementTo"
5. Clicar "Preview" para verificar
6. Clicar "Publish"
7. Copiar o DOI gerado (formato: 10.5281/zenodo.XXXXXXX)

### Opcao B: Integracao GitHub-Zenodo (Recomendado)

1. Acessar https://zenodo.org e fazer login
2. Ir em Settings > GitHub
3. Ativar o repositorio `terciosilas/discovery-engine`
4. Criar a release `discovery-engine-dataset-v1.0` no GitHub (ja preparada)
5. O Zenodo detecta automaticamente a release e gera DOI
6. Verificar metadados no Zenodo e editar se necessario
7. O DOI e gerado automaticamente

### Pos-Upload

8. [ ] Atualizar DOI no paper (PAPER_DRAFT_v1.md, secao Data Availability)
9. [ ] Atualizar DOI no README.md do GitHub
10. [ ] Atualizar DOI no README_dataset.md do Zenodo
11. [ ] Verificar que o badge do Zenodo aparece no GitHub

## 5. Badge para o README.md

Apos gerar o DOI, adicionar ao README.md do GitHub:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

---

*Checklist gerado pelo Discovery Engine pipeline*
