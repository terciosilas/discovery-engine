# PMO -- Plano Mestre do Projeto Discovery Engine

> "Identificacao computacional de compostos geroprotetores via analise proteomica multi-omica"
> Versao: 2.0 | Atualizado: 2026-03-11 | Operador: Tercio Silas
> Assistido por: Claude Code (Anthropic)

---

## COMO USAR ESTE DOCUMENTO

Este PMO e a **fonte unica de verdade** sobre o progresso do projeto.
Cada sessao do Claude Code deve:
1. **Ao iniciar:** Ler este PMO + STATE.md + DECISIONS.md
2. **Ao trabalhar:** Marcar tarefas como [~] (em andamento) e [x] (concluido)
3. **Ao finalizar:** Atualizar este PMO com tarefas concluidas + adicionar entrada no log de sessoes

**Legenda de status:**
- `[ ]` Pendente
- `[~]` Em andamento (sessao atual)
- `[x]` Concluido (com sessao e data)
- `[-]` Descartado (com motivo)

---

## DASHBOARD DE PROGRESSO

```
Fase 0: Fundacao             ██████████ 100%   COMPLETA
Fase 1: Ingestao/Mapeamento  ██████████ 100%   COMPLETA
Fase 2: Analise/Cruzamento   ░░░░░░░░░░   0%   << PROXIMA
Fase 3: Validacao             ░░░░░░░░░░   0%
Fase 4: Publicacao            ░░░░░░░░░░   0%
```

**Metricas atuais:**
| Metrica | Valor |
|---|---|
| Papers no acervo | 376 aceitos (de 485 brutos) |
| Papers enriquecidos S2 | 356 (94.7%) |
| Testes automatizados | 77 passando |
| Commits no GitHub | 10 |
| Decisoes registradas | DEC-001 a DEC-006 |
| Sessoes concluidas | 4 |

---

## FASE 0 -- FUNDACAO

> Objetivo: Montar infraestrutura, governanca e modulos core.
> Status: **COMPLETA** (Sessoes #1-#2)

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-001 | Definir tema e abordagem (DEC-001) | [x] | #1 |
| T-002 | Definir infraestrutura (DEC-002) | [x] | #1 |
| T-003 | Definir governanca e etica (DEC-003) | [x] | #1 |
| T-004 | Criar estrutura de pastas | [x] | #1 |
| T-005 | Criar docs fundacionais (CLAUDE.md, STATE, DECISIONS, BACKLOG, PMO) | [x] | #1 |
| T-006 | Configurar Google Colab (GPU T4 + Drive montado) | [x] | #2 |
| T-007 | Criar repo privado GitHub (discovery-engine) | [x] | #2 |
| T-008 | Configurar .gitignore e .env.example | [x] | #2 |
| T-009 | Migrar OneDrive -> Google Drive (DEC-006) | [x] | #2 |
| T-010 | Construir src/core/integrity.py (SHA-256) | [x] | #2 |
| T-011 | Construir src/core/audit.py (logs append-only) | [x] | #2 |
| T-012 | Construir src/core/bibliography.py (BibTeX + licencas) | [x] | #2 |
| T-013 | Criar ethics/DECLARACAO_USO_IA.md | [x] | #1 |
| T-014 | Criar ethics/DECLARACAO_FONTES.md | [x] | #1 |
| T-015 | Criar config/search_queries.yaml | [x] | #2 |
| T-016 | Criar config/inclusion_criteria.yaml | [x] | #2 |

---

## FASE 1 -- INGESTAO E MAPEAMENTO

> Objetivo: Coletar literatura, verificar licencas, enriquecer com citacoes, mapear terreno.
> Status: **COMPLETA** (Sessoes #2-#4)

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-017 | Construir src/ingestion/pubmed.py (API E-utilities) | [x] | #2 |
| T-018 | Construir src/ingestion/unpaywall.py (verificacao licenca) | [x] | #2 |
| T-019 | Construir src/ingestion/semantic_scholar.py (API S2) | [x] | #2 |
| T-020 | Construir src/ingestion/filtro.py (criterios inclusao/exclusao) | [x] | #3 |
| T-021 | Construir src/ingestion/orquestrador.py (pipeline completo) | [x] | #3 |
| T-022 | Executar busca em escala (6 queries, 485 brutos) | [x] | #3 |
| T-023 | Deduplicar e filtrar (376 aceitos, 97 rejeitados) | [x] | #3 |
| T-024 | Verificar licencas Unpaywall (280 OA, 74%) | [x] | #3 |
| T-025 | Verificar controle positivo (Lehallier 2019) | [x] | #3 |
| T-026 | Gerar Relatorio Fase 1 "Mapa do Terreno" | [x] | #3 |
| T-027 | Construir src/ingestion/enriquecedor.py (S2 + checkpoint) | [x] | #4 |
| T-028 | Adicionar batch API ao Semantic Scholar (POST /paper/batch) | [x] | #4 |
| T-029 | Executar enriquecimento S2 (356/376, 94.7% cobertura) | [x] | #4 |
| T-030 | Construir src/ingestion/chembl.py (API ChEMBL) | [x] | #4 |
| T-031 | Construir src/ingestion/drugbank.py (DrugBank + Open Targets) | [x] | #4 |
| T-032 | Curar lista de 13 geroprotetores conhecidos | [x] | #4 |
| T-033 | Curar lista de 15 alvos-chave do envelhecimento (com Ensembl IDs) | [x] | #4 |
| T-034 | Testes unitarios completos (77 passando) | [x] | #4 |

---

## FASE 2 -- ANALISE E CRUZAMENTO

> Objetivo: Extrair alvos dos papers, cruzar com bases de drogas, construir grafo, ranquear candidatos.
> Status: **PENDENTE**
> Estimativa: 3-5 sessoes

### Bloco 2A -- Extracao de Alvos Proteicos

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-035 | Construir extrator de proteinas/genes dos abstracts (NER ou regex) | [ ] | |
| T-036 | Executar extracao nos 376 abstracts | [ ] | |
| T-037 | Validar extracao: MTOR, SIRT1, FOXO3 devem aparecer no top | [ ] | |
| T-038 | Consolidar ranking de top 50 proteinas-alvo | [ ] | |
| T-039 | Mapear proteinas para UniProt IDs | [ ] | |

### Bloco 2B -- Consulta a Bases de Drogas

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-040 | Consultar Open Targets para cada alvo -> drogas associadas | [ ] | |
| T-041 | Consultar ChEMBL para atividades (IC50/Ki) dos compostos | [ ] | |
| T-042 | Baixar DrugBank vocabulary e integrar | [ ] | |
| T-043 | Carregar GenAge (genes do envelhecimento) | [ ] | |
| T-044 | Carregar DrugAge (drogas com efeito em lifespan) | [ ] | |

### Bloco 2C -- Grafo de Conhecimento

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-045 | Construir grafo: proteina <-> droga <-> doenca (NetworkX) | [ ] | |
| T-046 | Calcular metricas de centralidade no grafo | [ ] | |
| T-047 | Identificar clusters/comunidades de proteinas | [ ] | |
| T-048 | Gerar visualizacao do grafo | [ ] | |

### Bloco 2D -- Ranqueamento de Candidatos

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-049 | Definir score de potencial geroprotetor (formula/ML) | [ ] | |
| T-050 | Implementar scoring: citacoes + potencia + fase clinica + centralidade | [ ] | |
| T-051 | Ranquear top 20-50 candidatos a geroprotetores | [ ] | |
| T-052 | Controle positivo: rapamycin e metformin devem estar no top 10 | [ ] | |
| T-053 | Gerar Relatorio Fase 2: "Candidatos Identificados" | [ ] | |
| T-054 | Testes para modulos da Fase 2 | [ ] | |

---

## FASE 3 -- VALIDACAO COMPUTACIONAL

> Objetivo: Validar candidatos com rigor estatistico e cientifico.
> Status: **PENDENTE**
> Estimativa: 2-4 sessoes

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-055 | Validacao cruzada com literatura existente | [ ] | |
| T-056 | Analise de seguranca (efeitos adversos conhecidos via FAERS/SIDER) | [ ] | |
| T-057 | Reproducibilidade: executar pipeline 3x, comparar resultados | [ ] | |
| T-058 | Bootstrap (1000 reamostragens) para estabilidade do ranking | [ ] | |
| T-059 | Cross-validation do modelo (treinar 80%, testar 20%) | [ ] | |
| T-060 | Ablation study: remover features uma a uma, medir impacto | [ ] | |
| T-061 | Controle negativo: drogas sabidamente ineficazes fora do top 50 | [ ] | |
| T-062 | Docking molecular basico (se viavel com AutoDock Vina) | [ ] | |
| T-063 | Analise de sensibilidade (variar thresholds) | [ ] | |
| T-064 | Gerar Relatorio Fase 3: "Validacao e Confianca" | [ ] | |
| T-065 | Testes para modulos da Fase 3 | [ ] | |

---

## FASE 4 -- PUBLICACAO

> Objetivo: Escrever e publicar paper cientifico.
> Status: **PENDENTE**
> Estimativa: 3-5 sessoes

### Bloco 4A -- Escrita do Paper

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-066 | Escrever Introducao (contexto + gap + hipotese) | [ ] | |
| T-067 | Escrever Metodos (pipeline, dados, ML, estatistica) | [ ] | |
| T-068 | Escrever Resultados (candidatos, grafo, validacao) | [ ] | |
| T-069 | Escrever Discussao (significado, limitacoes, trabalho futuro) | [ ] | |
| T-070 | Escrever Abstract e Titulo final | [ ] | |

### Bloco 4B -- Material Visual e Suplementar

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-071 | Gerar figuras de qualidade para publicacao | [ ] | |
| T-072 | Gerar tabelas formatadas | [ ] | |
| T-073 | Preparar material suplementar (codigo, dados, queries) | [ ] | |
| T-074 | Publicar codigo no GitHub (tornar publico) | [ ] | |
| T-075 | Publicar dados no Zenodo (DOI permanente) | [ ] | |

### Bloco 4C -- Submissao

| ID | Tarefa | Status | Sessao |
|---|---|---|---|
| T-076 | Escrever cover letter | [ ] | |
| T-077 | Formatar paper no template do journal-alvo | [ ] | |
| T-078 | Submeter preprint (bioRxiv/medRxiv) | [ ] | |
| T-079 | Submeter ao journal-alvo #1 | [ ] | |
| T-080 | Responder revisoes dos pareceristas | [ ] | |

---

## LOG DE SESSOES

> Historico de cada sessao: o que foi feito, tarefas concluidas, decisoes tomadas.

### Sessao #1 (2026-03-10)
- **Foco:** Definicao do projeto
- **Tarefas concluidas:** T-001, T-002, T-003, T-004, T-005, T-013, T-014
- **Decisoes:** DEC-001 (tema), DEC-002 (infra), DEC-003 (governanca), DEC-004 (direitos autorais), DEC-005 (continuidade)
- **Resultado:** Estrutura completa do projeto criada

### Sessao #2 (2026-03-10)
- **Foco:** Infraestrutura + modulos core + ingestao
- **Tarefas concluidas:** T-006 a T-012, T-015 a T-019
- **Decisoes:** DEC-006 (migrar para Google Drive)
- **Resultado:** GitHub + Colab + Drive + 3 modulos core + 3 modulos ingestao + 40 testes

### Sessao #3 (2026-03-10)
- **Foco:** Busca em escala + Relatorio Fase 1
- **Tarefas concluidas:** T-020 a T-026
- **Decisoes:** Nenhuma nova
- **Resultado:** 376 papers aceitos, gap confirmado (6 papers drug repurposing), Relatorio Mapa do Terreno

### Sessao #4 (2026-03-10)
- **Foco:** Enriquecimento S2 + modulos de drogas
- **Tarefas concluidas:** T-027 a T-034
- **Decisoes:** Nenhuma nova
- **Resultado:** 356 papers enriquecidos (94.7%), ChEMBL + DrugBank + Open Targets prontos, 77 testes
- **Incidente:** Rate limit S2 na primeira execucao (50.3% cobertura). Resolvido com batch API (94.7%).

### Sessao #5 (pendente)
- **Foco previsto:** Fase 2A -- Extracao de alvos proteicos (T-035 a T-039)
- **Pre-requisito:** Ler PMO.md + STATE.md. Retomar de T-035.

---

## ESTRATEGIA DE PUBLICACAO

### Journals-alvo (prioridade)

| Prioridade | Journal | IF | Taxa OA | Nota |
|---|---|---|---|---|
| 1 | Nature Aging | ~17 | ~EUR 9.500 | Se resultados excepcionais |
| 2 | Aging Cell | ~11 | ~EUR 3.200 | Melhor fit tematico |
| 3 | Briefings in Bioinformatics | ~14 | Gratis (nao-OA) | Foco em metodo |
| 4 | GeroScience | ~7 | ~EUR 3.390 | Boa aceitacao |
| 5 | npj Aging | ~5 | Gratis | Mais acessivel |
| B1 | Drug Discovery Today | ~8 | Gratis (nao-OA) | Plano B |
| B2 | PLOS ONE | ~3 | ~USD 2.290 | Garantido |

### Preprint: bioRxiv (gratis, publicacao em 24-48h, garante prioridade)

---

## VALIDACAO CIENTIFICA (3 CAMADAS)

| Camada | O que | Quem | Quando |
|---|---|---|---|
| 1. Interna | Reproducibilidade, cross-validation, bootstrap, controles +/- | Nos | Fase 3 |
| 2. Pares | Preprint + peer review em journal | Especialistas | Fase 4 |
| 3. Experimental | Testes in vitro/in vivo | Laboratorios parceiros | Futuro |

**Regra de ouro:** Se o pipeline NAO encontrar rapamicina e metformina no top 10, a metodologia esta errada.

---

## METRICAS DE SUCESSO

| Fase | Metrica | Meta | Real |
|---|---|---|---|
| Fase 0 | Modulos core funcionando | 3 | 3 (integrity, audit, bibliography) |
| Fase 1 | Papers indexados | >300 | 376 |
| Fase 1 | Cobertura S2 | >80% | 94.7% |
| Fase 1 | Fontes de dados integradas | >3 | 5 (PubMed, S2, Unpaywall, ChEMBL, OpenTargets) |
| Fase 2 | Candidatos identificados | 20-50 | - |
| Fase 3 | Controle positivo no top 10 | Rapamicina + Metformina | - |
| Fase 3 | Reproducibilidade | 100% | - |
| Fase 4 | Preprint publicado | Sim | - |
| Fase 4 | Paper aceito IF > 5 | Sim | - |

---

## GLOSSARIO RAPIDO

| Termo | Significado |
|---|---|
| Geroprotetor | Substancia que retarda o envelhecimento |
| Drug repurposing | Novo uso para medicamento ja existente |
| Proteomica | Estudo de todas as proteinas de um organismo |
| NER | Named Entity Recognition -- extrair nomes de entidades de texto |
| mTOR | Via de crescimento celular -- inibir retarda envelhecimento |
| Senolitico | Droga que mata celulas envelhecidas |
| IC50 | Concentracao que inibe 50% da atividade -- menor = mais potente |
| pChEMBL | -log10(molar) padronizado -- maior = mais potente (>6 = ativo) |
| IMRaD | Formato de paper: Introducao, Metodos, Resultados, Discussao |
| Preprint | Paper publicado antes da revisao por pares (bioRxiv) |

---

## RISCOS ATIVOS

| Risco | Status | Mitigacao |
|---|---|---|
| Rate limit APIs (S2, ChEMBL) | MITIGADO | Batch API + retry com backoff |
| Resultados inconclusivos | MONITORAR | Controles positivos desde Fase 2 |
| Paper rejeitado journal #1 | ACEITO | Lista de 7 journals alternativos |
| Pesquisa similar publicada antes | MONITORAR | Preprint garante prioridade |
| Google Colab insuficiente | BAIXO | 2TB Drive, GPU T4 gratis |
