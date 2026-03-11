# Estado do Projeto -- Discovery Engine

> Ultima atualizacao: 2026-03-10 (Sessao #2)

## Fase Atual

**Fase 0 -- Fundacao (60% concluida)**

## O que foi feito

### Sessao #2 (2026-03-10)
- Instalado GitHub CLI (`gh`) e autenticado como `terciosilas`
- Criado repo privado: github.com/terciosilas/discovery-engine
- Inicializado git local, primeiro commit e push
- Criado `.gitignore` (Python, data, outputs, secrets) e `.env.example`
- Construido `src/core/integrity.py` -- SHA-256 para rastreabilidade
- Construido `src/core/audit.py` -- Logger append-only JSON (GOVERNANCA.md)
- Construido `src/core/bibliography.py` -- Gestao BibTeX + licencas + PDFs
- Criado `config/search_queries.yaml` -- 6 queries iniciais para PubMed
- Criado `config/inclusion_criteria.yaml` -- Criterios pre-definidos com controles positivos/negativos
- Criado `tests/test_core.py` -- 23 testes unitarios (100% passando)
- Tercio abriu Google Colab (em portugues), sendo guiado na configuracao

### Sessao #1 (2026-03-10)
- Definido tema: Proteinas/Longevidade + Drug Repurposing com IA
- Pesquisa exploratoria em 5 campos
- Definida infraestrutura: OneDrive + Google Colab + Claude Code local
- Definida governanca: espelho do ERP (audit_logs, SHA-256, bibliography, etica)
- Criada estrutura de pastas no OneDrive
- Criados documentos fundacionais (CLAUDE.md, STATE, DECISIONS, BACKLOG, PMO)
- Declaracoes eticas criadas (uso de IA + fontes)

## Raciocinio em andamento

- Combinamos proteomica de longevidade com drug repurposing porque eh **100% computacional**
  e tem datasets publicos imensos (UK Biobank, DrugBank, GenAge, HALL, ChEMBL)
- A abordagem eh meta-analise computacional com ML/IA -- nao experimental
- O diferencial: usar IA para cruzar dados proteomicos de envelhecimento com bases
  de medicamentos existentes, identificando candidatos em escala sobre-humana
- Nao precisamos de laboratorio -- validacao computacional + estatistica
- Modulos core prontos e testados -- base solida para construir pipelines de ingestao
- Proximo foco: pipeline PubMed (ingestao real de dados)

## Bloqueios atuais

- Google Colab: Tercio esta configurando (primeira vez)
- Nota: Colab em portugues -- menus traduzidos (ex: "Ambiente de execucao" em vez de "Runtime")

## Proximo passo concreto

1. **Finalizar configuracao Colab** -- Tercio precisa montar Drive e testar GPU
2. **Construir `src/ingestion/pubmed.py`** -- Pipeline de busca via E-utilities API
3. **Primeira busca exploratoria** -- Top 500 papers "proteomics aging longevity" (2020-2026)
4. **Construir `src/ingestion/unpaywall.py`** -- Verificacao de licenca antes de armazenar PDFs

## Contexto tecnico ativo

- **Maquina:** i5-1135G7, 24GB RAM, 18GB disco C: livre
- **OneDrive:** 785 GB livres no plano 1TB
- **Google Colab:** Em configuracao (Tercio primeira vez)
- **GitHub:** terciosilas/discovery-engine (PRIVADO, branch main, 2 commits)
- **GitHub CLI:** gh v2.87.3 instalado e autenticado
- **Python:** 3.14.2 local
- **Testes:** 23 passando (pytest)
- **APIs:** PubMed (gratis, sem key), Semantic Scholar (gratis, key opcional)
