# GeroScience Submission Checklist

**Manuscript:** Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis
**Journal:** GeroScience (Springer Nature, ISSN: 2509-9035)
**Article type:** Original Research Article
**Data:** 2026-03-11

---

## 1. Manuscript Files

| File | Status | Format |
|------|--------|--------|
| [x] Main manuscript (`PAPER_GEROSCIENCE_SUBMISSION.md`) | Pronto | MD (converter para .docx) |
| [x] Cover letter (`COVER_LETTER_GEROSCIENCE.md`) | Pronto | MD (converter para .docx) |
| [x] Fig. 1 - Pipeline overview | Pronto | PNG 300 DPI |
| [x] Fig. 2 - Top-20 ranking | Pronto | PNG 300 DPI |
| [x] Fig. 3 - Bootstrap stability | Pronto | PNG 300 DPI |
| [x] Fig. 4 - Ablation study | Pronto | PNG 300 DPI |
| [x] Fig. 5 - Sensitivity analysis | Pronto | PNG 300 DPI |
| [x] Supplementary Fig. S1 | Pronto | PNG 300 DPI |
| [x] Supplementary Fig. S2 | Pronto | PNG 300 DPI |
| [x] Supplementary Tables S1-S7 | Pronto | CSV |

## 2. Conversao de Formato

Antes de submeter, converter:

```bash
# Opcao 1: Pandoc (recomendado)
pandoc PAPER_GEROSCIENCE_SUBMISSION.md -o PAPER_GEROSCIENCE_SUBMISSION.docx
pandoc COVER_LETTER_GEROSCIENCE.md -o COVER_LETTER_GEROSCIENCE.docx

# Opcao 2: Converter figuras PNG para TIFF (exigido para publicacao final)
# convert fig1_pipeline_overview.png fig1_pipeline_overview.tiff
```

Nota: Para submissao inicial, GeroScience aceita formatos nao padrao. A formatacao final so e exigida apos aceitacao.

## 3. Verificacao de Figuras

| Requisito | Status |
|-----------|--------|
| [x] Resolucao >= 300 DPI | Todas em 300 DPI |
| [x] Formato PNG (TIFF para versao final) | PNG OK para submissao |
| [x] Legendas completas no manuscrito | Sim, secao "Figure Legends" |
| [x] Evitar vermelho/verde juntos | Verificado |
| [x] Texto legivel em reducao | Verificado |
| [x] Figuras referenciadas no texto | Sim |

## 4. Campos Obrigatorios no Editorial Manager

| Campo | Valor |
|-------|-------|
| Article Type | Original Research Article |
| Title | Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis |
| Running Title | Computational Geroprotector Identification |
| Author | Tercio S. Azevedo |
| Affiliation | Independent Researcher, Sao Carlos, SP, Brazil |
| Email | tercio@callamarys.com.br |
| ORCID | (preencher se disponivel) |
| Keywords | drug repurposing; geroprotectors; aging; computational biology; knowledge graph; longevity |
| Abstract | 248 palavras (limite: 150-250) |
| Word count | ~4,500 palavras (corpo principal, excluindo refs/tabelas) |
| Figures | 5 principais + 2 suplementares |
| Tables | 5 principais |
| Supplementary | 7 tabelas + 2 figuras |
| Data Availability | Zenodo DOI + GitHub URL |
| Funding | None |
| Conflicts | None |
| Ethics | Not applicable (computational study) |
| AI Disclosure | Claude Code (Anthropic) -- declarado no manuscrito |

## 5. Sugestoes de Reviewers

| Reviewer | Afiliacao | Expertise | Motivo |
|----------|-----------|-----------|--------|
| Joao Pedro de Magalhaes | University of Birmingham | GenAge/DrugAge creator, aging genomics | Criador dos bancos de dados usados |
| Alex Zhavoronkov | Insilico Medicine | AI drug discovery, aging | Lider em AI para aging |
| Andrei Seluanov | University of Rochester | Aging biology, geroprotectors | Especialista em mecanismos de aging |
| Nir Barzilai | Albert Einstein College | TAME trial, metformin/aging | Lider em translational geroscience |

## 6. Checklist Pre-Submissao

### Manuscrito
- [x] Abstract entre 150-250 palavras (248 palavras)
- [x] Keywords incluidas (6 termos)
- [x] Referencias numeradas no estilo Springer [1, 2, 3...]
- [x] DOIs incluidos nas referencias
- [x] Nomes cientificos em italico (*C. elegans*, *Drosophila*)
- [x] Tabelas com notas de rodape
- [x] Secao Declarations completa (Funding, Conflicts, Ethics, Data, AI)
- [x] Acknowledgments incluidos
- [x] Secao Introduction sem subsecoes (conforme padrao GeroScience)
- [x] Methods com subsecoes descritivas

### Integridade Cientifica
- [x] Todos os resultados reproduziveis (seed=42)
- [x] Controles negativos testados (0% falsos positivos)
- [x] Validacao externa independente (DrugAge)
- [x] Limitacoes claramente declaradas
- [x] Uso de AI declarado transparentemente

### Dados e Codigo
- [x] Repositorio GitHub publico: https://github.com/terciosilas/discovery-engine
- [x] Dataset Zenodo preparado (DOI pendente)
- [x] 106 testes automatizados passando
- [x] Audit logs com SHA-256

## 7. Passos para Submissao

1. [ ] Criar conta no Editorial Manager: https://www.editorialmanager.com/jaaa/
2. [ ] Converter manuscrito MD -> DOCX (pandoc)
3. [ ] Converter cover letter MD -> DOCX
4. [ ] Upload manuscrito principal
5. [ ] Upload cover letter
6. [ ] Upload figuras 1-5 individualmente
7. [ ] Upload supplementary material (figs S1-S2 + tables S1-S7)
8. [ ] Preencher metadados do artigo
9. [ ] Adicionar suggested reviewers
10. [ ] Preview e submit
11. [ ] Anotar numero de submissao

## 8. Apos Submissao

- [ ] Depositar preprint no bioRxiv (opcional, verificar politica)
- [ ] Gerar DOI Zenodo e atualizar manuscrito
- [ ] Atualizar STATE.md com status da submissao

## 9. Informacoes do Journal

| Dado | Valor |
|------|-------|
| Publisher | Springer Nature |
| ISSN | 2509-9035 (online), 2509-9027 (print) |
| Impact Factor | ~6.4 (2024) |
| CiteScore | ~11.4 |
| Acceptance Rate | ~25% for original research |
| Review Time | Rapid initial screening; external review if passed |
| APC (Open Access) | USD 4,490 / EUR 3,490 / GBP 2,890 |
| Submission Portal | https://www.editorialmanager.com/jaaa/ |
| Society | American Aging Association |

---

*Checklist gerado pelo Discovery Engine pipeline*
