# Estado do Projeto -- Discovery Engine

> Ultima atualizacao: 2026-03-11 (Sessao #9)

## Fase Atual

**Fase 0 -- Fundacao (100%)**
**Fase 1 -- Ingestao e Mapeamento (100%)**
**Fase 2 -- Analise e Cruzamento (95%)** -- T-048 (visualizacao grafo) pendente
**Fase 3 -- Validacao Computacional (100%)** -- T-056/T-062 descartados
**Fase 4 -- Publicacao (100%)** << PRONTO PARA SUBMISSAO

## O que foi feito

### Sessao #9 (2026-03-11)
- **T-079: Submissao GeroScience preparada:**
  - `submission/editorial_manager_upload_order.md` -- ordem de upload dos 16 arquivos com tamanhos e categorias
  - `submission/editorial_manager_metadata.md` -- todos os campos para copiar no Editorial Manager (titulo, short title, abstract, keywords, declaracoes)
  - `submission/suggested_reviewers.md` -- 4 revisores com emails institucionais verificados e justificativas
  - Revisores: de Magalhaes (Birmingham), Zhavoronkov (Insilico), Seluanov (Rochester), Barzilai (Einstein)
  - Nenhum revisor a evitar (sem conflitos identificados)
  - Email corrigido em 11 arquivos: tercio@callamarys.com.br -> terciosilas@gmail.com
  - DOCX regenerados com email correto
  - **Projeto PRONTO para submissao.** Falta apenas upload manual pelo operador.

### Sessao #8 (2026-03-11)
- **T-078: Preprint bioRxiv preparado:**
  - `submission/submission_package/discovery_engine_preprint.docx` (798 KB, figuras embutidas)
  - `submission/preprint_submission_metadata.md` (titulo, abstract, keywords, categoria)
  - `submission/biorxiv_submission_checklist.md` (passos, campos, declaracoes)
  - Categoria bioRxiv: Bioinformatics
  - bioRxiv aceita Word com figuras; gera PDF automaticamente
  - **Proximo passo manual:** Upload em https://submit.biorxiv.org/
- **T-077: Paper formatado para GeroScience:**
  - `submission/PAPER_GEROSCIENCE_SUBMISSION.md` -- manuscrito adaptado (refs numeradas, abstract 248 palavras, Declarations, italico)
  - `submission/COVER_LETTER_GEROSCIENCE.md` -- cover letter direcionada ao GeroScience
  - `submission/geroscience_submission_checklist.md` -- checklist completo com campos, reviewers, passos
  - `submission/submission_package/` -- 16 arquivos prontos para upload (manuscrito + 5 figs + supplementary)
  - 4 sugestoes de reviewers: de Magalhaes, Zhavoronkov, Seluanov, Barzilai
  - **Proximo passo manual:** Converter MD->DOCX e submeter via Editorial Manager
- **T-075: Dataset Zenodo preparado:**
  - `publication/zenodo_dataset/` com 25 arquivos em 6 categorias
  - README_dataset.md com descricao de colunas e instrucoes de uso
  - LICENSE CC-BY-4.0 para dados
  - ZENODO_METADATA.json com metadados completos
  - `publication/zenodo_upload_checklist.md` com passos para gerar DOI
  - Release GitHub: v1.0 (https://github.com/terciosilas/discovery-engine/releases/tag/v1.0)
  - Paper atualizado com secao Data Availability (placeholder DOI)
  - **Proximo passo manual:** Ativar integracao Zenodo-GitHub e publicar
- **T-074: Repositorio tornado PUBLICO:**
  - README.md criado (descricao, pipeline, instrucoes reproducao, citacao)
  - requirements.txt criado (7 dependencias: numpy, scipy, matplotlib, networkx, requests, PyYAML, pytest)
  - .gitignore atualizado (exclui JSONs grandes, audit_logs, caches; inclui dados externos)
  - Auditoria de seguranca: zero credenciais, zero caminhos hardcoded, operador anonimizado
  - 106 testes passando (confirmado)
  - Dados externos (DrugAge, GenAge) incluidos para reproducibilidade
  - 61 arquivos commitados (~15k linhas): code + outputs + figuras + resultados
  - Repo publico: https://github.com/terciosilas/discovery-engine
  - Topics: drug-repurposing, aging, geroprotectors, computational-biology, knowledge-graph, longevity
- **Analise Mecanistica dos Top-20 (completa):**
  - Criado `src/analysis/mechanistic_interpretation.py` (~550 linhas)
  - 20 compostos analisados, media 1.9 hallmarks/composto
  - Todos os 8 hallmarks of aging cobertos
  - 3 eixos mecanisticos: mTOR/nutrient sensing (7/20), senescencia/apoptose (3/20), mitocondrial/metabolico (5/20)
  - Hallmark mais frequente: Stem Cell Exhaustion (11/20)
  - Metformin e resveratrol com maior cobertura (4 hallmarks cada)
  - Outputs: results/mechanistic_interpretation/ (4 arquivos: CSV, PNG, MD, JSON)
  - Figure_S2_mechanistic_network.png (rede drogas->alvos->hallmarks, 300 DPI)
- **Paper PAPER_DRAFT_v1.md atualizado:**
  - Methods 2.10: Mechanistic Interpretation
  - Results 3.9: Mechanistic Interpretation of Top Ranked Candidates (Table 5)
  - Discussion 4.1: 5 linhas independentes de evidencia (antes eram 4)
  - Discussion 4.2: Candidatos novos expandidos com insights mecanisticos
  - Abstract atualizado com interpretacao mecanistica
  - References: Lopez-Otin 2013, 2023
- **Supplementary atualizado:** Figure_S2 adicionada ao README

### Sessao #7 (2026-03-11) -- continuacao
- **Validacao Externa DrugAge (completa):**
  - Criado `src/validation/external_drugage.py` (~550 linhas)
  - Cruzamento normalizado: 11/162 compostos encontrados no DrugAge, 10 com efeito positivo
  - Metricas: P@10=30%, P@20=30%, EF@20=4.42x, Mann-Whitney p=1.59e-03
  - Media rank DrugAge=41.2 vs nao-DrugAge=84.4 (significativamente menor)
  - Bezafibrate (#9) e Pictilisib (#79) = descobertas genuinas confirmadas pelo DrugAge
  - Outputs: results/external_validation_drugage/ (4 arquivos: CSV, PNG, MD, JSON)
  - Figure_S1_external_validation_benchmark.png (4 paineis, 300 DPI)
- **Paper PAPER_DRAFT_v1.md atualizado:**
  - Methods 2.9: External Validation Against DrugAge
  - Results 3.8: External Validation Against DrugAge (Table 4)
  - Discussion 4.1: 4 linhas independentes de evidencia (antes eram 3)
  - Abstract atualizado com resultados DrugAge

### Sessao #7 (2026-03-11)
- **Pathway Enrichment Analysis:**
  - Criado `src/analysis/pathway_enrichment.py` (~450 linhas)
  - 1578 pathways, 904 significativos, 11/11 categorias aging enriquecidas
  - Top KEGG: "Longevity regulating pathway" (p=1.27e-20)
- **Benchmark Metodologico:**
  - Criado `src/validation/benchmark.py` (~500 linhas)
  - DE: R@20=1.00, EF@20=8.10; Baselines A/C: falha catastrofica; B: lookup table
- **Dependencia nova:** scipy
- **106 testes passando**

### Sessao #6 (2026-03-11)
- Bloco 4A/4B/4C: Figuras (5 PNGs), tabelas suplementares (7), cover letter
- Criado src/visualization/figures.py e tables.py
- Dependencia nova: matplotlib 3.10.8

### Sessao #5 (2026-03-11)
- Fase 2 completa (target mapping, drug linking, grafo, scoring, 97 testes)
- Fase 3 completa (bootstrap, ablation, controles negativos, sensibilidade, 106 testes)
- PAPER_DRAFT_v1.md criado (IMRaD completo)

### Sessao #4 (2026-03-10)
- Enriquecimento S2 (356/376, 94.7%), ChEMBL client, DrugBank client, 77 testes


## Raciocinio em andamento

- **Fase 4 COMPLETA (100%).** Todo o trabalho computacional e de preparacao esta finalizado.
- **Paper tem 5 linhas de evidencia independentes:**
  1. Pathway enrichment (11/11 categorias aging, p=1.27e-20)
  2. Benchmark (EF=8.1x, unico modelo com recall+predicao)
  3. Validacao externa DrugAge (EF@20=4.42x, Mann-Whitney p=1.59e-03)
  4. Descobertas genuinas (bezafibrate, pictilisib confirmados)
  5. Interpretacao mecanistica (8/8 hallmarks, 3 eixos convergentes)
- **Todas as tarefas computacionais concluidas:**
  - ~~T-074: Tornar repo GitHub publico~~ -- FEITO
  - ~~T-075: Publicar dados no Zenodo~~ -- PREPARADO
  - ~~T-077: Formatar para GeroScience~~ -- FEITO
  - ~~T-078: Preparar preprint bioRxiv~~ -- FEITO
  - ~~T-079: Preparar submissao GeroScience~~ -- FEITO
- **Restam apenas acoes manuais do operador** (ver abaixo).

## Bloqueios atuais

Nenhum bloqueio tecnico. Apenas acoes manuais pendentes.

## Proximo passo concreto (acoes manuais do operador)

1. **Criar ORCID** (se nao tiver): https://orcid.org/register
2. **Ativar integracao Zenodo-GitHub:** zenodo.org > Settings > GitHub > Flip switch > Publicar release
3. ~~Atualizar DOI Zenodo~~ -- FEITO (10.5281/zenodo.18966721)
4. **Submeter ao bioRxiv:** https://submit.biorxiv.org/ (seguir `submission/biorxiv_submission_checklist.md`)
5. **Submeter ao GeroScience:** https://www.editorialmanager.com/jaaa/ (seguir `submission/editorial_manager_upload_order.md`)
6. **Anotar numeros de submissao** (bioRxiv DOI + Editorial Manager #)

## Contexto tecnico ativo

- **Google Drive:** G:\Meu Drive\Discovery_Engine
- **GitHub:** terciosilas/discovery-engine (PUBLICO)
- **Testes:** 106 passando
- **Modulos:** 27 arquivos Python em src/ (+1 nesta sessao: mechanistic_interpretation.py)
- **Dependencias:** networkx 3.6.1, matplotlib 3.10.8, scipy
- **Outputs:**
  - outputs/PAPER_DRAFT_v1.md (paper completo)
  - outputs/COVER_LETTER.md
  - outputs/figures/ (5 PNGs, 300 DPI)
  - outputs/supplementary/ (7 tabelas + README)
  - outputs/pathway_enrichment/ (4 arquivos: CSV, PNG, MD, JSON)
  - outputs/model_benchmark/ (4 arquivos: CSV, PNG, MD, JSON)
  - outputs/RELATORIO_FASE1_MAPA_DO_TERRENO.md
  - outputs/RELATORIO_FASE2_CANDIDATOS_IDENTIFICADOS.md
  - outputs/RELATORIO_FASE3_VALIDACAO_CONFIANCA.md
  - results/external_validation_drugage/ (4 arquivos: CSV, PNG, MD, JSON)
  - results/mechanistic_interpretation/ (4 arquivos: CSV, PNG, MD, JSON)
