# Backlog -- Discovery Engine

> Priorizado por fase. Itens dentro de cada fase em ordem de execucao.
> Status: [ ] pendente | [~] em andamento | [x] concluido | [-] descartado

---

## Fase 0 -- Fundacao

- [x] Definir tema e abordagem
- [x] Definir infraestrutura
- [x] Definir governanca e etica
- [x] Criar estrutura de pastas
- [x] Criar documentos fundacionais (CLAUDE.md, STATE, DECISIONS, BACKLOG, PMO)
- [~] Configurar Google Colab (Tercio em andamento)
- [x] Criar repo privado no GitHub (`discovery-engine`)
- [x] Configurar `.gitignore` e `.env.example`
- [x] Criar `src/core/bibliography.py` (gestao BibTeX + licencas + DOI)
- [x] Criar `src/core/audit.py` (log de auditoria append-only)
- [x] Criar `src/core/integrity.py` (SHA-256 de arquivos)
- [x] Criar `ethics/DECLARACAO_USO_IA.md`
- [x] Criar `ethics/DECLARACAO_FONTES.md`
- [x] Criar `config/search_queries.yaml` (queries iniciais)
- [x] Criar `config/inclusion_criteria.yaml` (criterios de selecao)

## Fase 1 -- Ingestao e Mapeamento

- [ ] Construir `src/ingestion/pubmed.py` (API E-utilities do PubMed)
- [ ] Construir `src/ingestion/semantic_scholar.py` (API Semantic Scholar)
- [ ] Construir `src/ingestion/unpaywall.py` (verificacao de licenca)
- [ ] Construir `src/ingestion/drugbank.py` (dados de medicamentos)
- [ ] Construir `src/ingestion/chembl.py` (atividade biologica)
- [ ] Primeira busca: top 500 papers "proteomics aging longevity" (2020-2026)
- [ ] Primeira busca: top 500 papers "drug repurposing aging" (2020-2026)
- [ ] Gerar mapa de conceitos (grafo de termos/proteinas/drogas)
- [ ] Identificar gaps na literatura
- [ ] Relatorio Fase 1: "Mapa do Terreno"

## Fase 2 -- Analise e Cruzamento

- [ ] Carregar datasets publicos (GenAge, DrugAge, HALL, ChEMBL)
- [ ] Construir grafo de conhecimento: proteina <-> doenca <-> droga <-> alvo
- [ ] Identificar proteinas-chave do envelhecimento (Klotho, FOXO3, sirtuinas, etc.)
- [ ] Cruzar proteinas-alvo com bases de medicamentos existentes
- [ ] Aplicar ML para ranquear candidatos a geroprotetores
- [ ] Validacao estatistica dos candidatos
- [ ] Relatorio Fase 2: "Candidatos Identificados"

## Fase 3 -- Validacao Computacional

- [ ] Validacao cruzada com literatura existente
- [ ] Analise de seguranca dos candidatos (efeitos adversos conhecidos)
- [ ] Modelagem de interacoes proteina-droga (docking computacional se viavel)
- [ ] Comparacao com resultados de ensaios clinicos existentes
- [ ] Analise de reprodutibilidade (bootstrap, cross-validation)
- [ ] Relatorio Fase 3: "Validacao e Confianca"

## Fase 4 -- Publicacao

- [ ] Revisao bibliografica formal (formato journal)
- [ ] Escrever paper no formato IMRaD (Introducao, Metodos, Resultados, Discussao)
- [ ] Gerar figuras e tabelas de qualidade para publicacao
- [ ] Preparar material suplementar (codigo, dados, queries)
- [ ] Submeter preprint (bioRxiv ou medRxiv)
- [ ] Identificar journals-alvo e submeter
- [ ] Responder revisoes dos pareceristas

## Fase 5 -- Extensao (futuro)

- [ ] Expandir analise para novos datasets
- [ ] Colaboracao com laboratorios para validacao experimental
- [ ] Apresentacao em conferencias
- [ ] Novas publicacoes derivadas
