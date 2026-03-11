# Backlog — Discovery Engine

> Priorizado por fase. Itens dentro de cada fase em ordem de execução.
> Status: [ ] pendente | [~] em andamento | [x] concluído | [-] descartado

---

## Fase 0 — Fundação

- [x] Definir tema e abordagem
- [x] Definir infraestrutura
- [x] Definir governança e ética
- [x] Criar estrutura de pastas
- [x] Criar documentos fundacionais (CLAUDE.md, STATE, DECISIONS, BACKLOG, PMO)
- [ ] Configurar Google Colab (tutorial para Tércio)
- [ ] Criar repo privado no GitHub (`discovery-engine`)
- [ ] Configurar `.gitignore` e `.env.example`
- [ ] Criar `src/core/bibliography.py` (gestão BibTeX + licenças + DOI)
- [ ] Criar `src/core/audit.py` (log de auditoria append-only)
- [ ] Criar `src/core/integrity.py` (SHA-256 de arquivos)
- [ ] Criar `ethics/DECLARACAO_USO_IA.md`
- [ ] Criar `ethics/DECLARACAO_FONTES.md`
- [ ] Criar `config/search_queries.yaml` (queries iniciais)
- [ ] Criar `config/inclusion_criteria.yaml` (critérios de seleção)

## Fase 1 — Ingestão e Mapeamento

- [ ] Construir `src/ingestion/pubmed.py` (API E-utilities do PubMed)
- [ ] Construir `src/ingestion/semantic_scholar.py` (API Semantic Scholar)
- [ ] Construir `src/ingestion/unpaywall.py` (verificação de licença)
- [ ] Construir `src/ingestion/drugbank.py` (dados de medicamentos)
- [ ] Construir `src/ingestion/chembl.py` (atividade biológica)
- [ ] Primeira busca: top 500 papers "proteomics aging longevity" (2020-2026)
- [ ] Primeira busca: top 500 papers "drug repurposing aging" (2020-2026)
- [ ] Gerar mapa de conceitos (grafo de termos/proteínas/drogas)
- [ ] Identificar gaps na literatura
- [ ] Relatório Fase 1: "Mapa do Terreno"

## Fase 2 — Análise e Cruzamento

- [ ] Carregar datasets públicos (GenAge, DrugAge, HALL, ChEMBL)
- [ ] Construir grafo de conhecimento: proteína ↔ doença ↔ droga ↔ alvo
- [ ] Identificar proteínas-chave do envelhecimento (Klotho, FOXO3, sirtuinas, etc.)
- [ ] Cruzar proteínas-alvo com bases de medicamentos existentes
- [ ] Aplicar ML para ranquear candidatos a geroprotetores
- [ ] Validação estatística dos candidatos
- [ ] Relatório Fase 2: "Candidatos Identificados"

## Fase 3 — Validação Computacional

- [ ] Validação cruzada com literatura existente
- [ ] Análise de segurança dos candidatos (efeitos adversos conhecidos)
- [ ] Modelagem de interações proteína-droga (docking computacional se viável)
- [ ] Comparação com resultados de ensaios clínicos existentes
- [ ] Análise de reprodutibilidade (bootstrap, cross-validation)
- [ ] Relatório Fase 3: "Validação e Confiança"

## Fase 4 — Publicação

- [ ] Revisão bibliográfica formal (formato journal)
- [ ] Escrever paper no formato IMRaD (Introdução, Métodos, Resultados, Discussão)
- [ ] Gerar figuras e tabelas de qualidade para publicação
- [ ] Preparar material suplementar (código, dados, queries)
- [ ] Submeter preprint (bioRxiv ou medRxiv)
- [ ] Identificar journals-alvo e submeter
- [ ] Responder revisões dos pareceristas

## Fase 5 — Extensão (futuro)

- [ ] Expandir análise para novos datasets
- [ ] Colaboração com laboratórios para validação experimental
- [ ] Apresentação em conferências
- [ ] Novas publicações derivadas
