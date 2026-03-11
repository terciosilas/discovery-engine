# Estado do Projeto -- Discovery Engine

> Ultima atualizacao: 2026-03-10 (Sessao #2)

## Fase Atual

**Fase 0 -- Fundacao (100% concluida)**
**Fase 1 -- Ingestao e Mapeamento (20% concluida)**

## O que foi feito

### Sessao #2 (2026-03-10)
- Instalado GitHub CLI (gh v2.87.3) e autenticado como terciosilas
- Criado repo privado: github.com/terciosilas/discovery-engine (4 commits)
- Construido src/core/integrity.py -- SHA-256 para rastreabilidade
- Construido src/core/audit.py -- Logger append-only JSON
- Construido src/core/bibliography.py -- Gestao BibTeX + licencas
- Configurado Google Colab (Tercio primeira vez): GPU T4, Drive montado
- Instalado Google Drive para Desktop (G:\Meu Drive)
- **MIGRADO projeto do OneDrive para Google Drive** (DEC-006)
  - G:\Meu Drive\Discovery_Engine (local)
  - /content/drive/MyDrive/Discovery_Engine (Colab)
- Construido src/ingestion/pubmed.py -- Cliente E-utilities API
- Construido src/ingestion/unpaywall.py -- Verificacao de licenca OA
- Construido src/ingestion/semantic_scholar.py -- Citacoes e influencia
- **Primeira busca exploratoria validada:**
  - 20 papers do PubMed ("proteomics aging longevity", 2020+)
  - Licencas verificadas: 8 OA, 12 restritos
  - 20 referencias registradas em bibliography/
  - Audit log gerado
- Configs: search_queries.yaml + inclusion_criteria.yaml
- 40 testes unitarios passando (23 core + 17 ingestao)

### Sessao #1 (2026-03-10)
- Definido tema, infraestrutura, governanca
- Criada estrutura de pastas e documentos fundacionais

## Raciocinio em andamento

- Pipeline PubMed -> Unpaywall -> Bibliography esta funcional e validado
- Dos 20 papers, 8 sao OA mas so 2 permitem armazenamento de PDF (cc-by)
- Maioria dos papers de alto impacto (Nature, Cell) usa cc-by-nc-nd, que nao permite redistribuicao
- Para a pesquisa, isso nao eh problema: usamos metadados + abstracts (fair use)
- Semantic Scholar ainda nao foi usado em producao, mas o modulo esta pronto
- Proximo passo eh escalar: buscar 500+ papers com todas as queries definidas

## Bloqueios atuais

- Nenhum

## Proximo passo concreto

1. **Busca em escala** -- Executar todas as 6 queries do search_queries.yaml (500 papers cada)
2. **Enriquecer com Semantic Scholar** -- Adicionar citation_count e influential_citations
3. **Aplicar criterios de inclusao/exclusao** do inclusion_criteria.yaml
4. **Gerar relatorio Fase 1** -- Estatisticas, mapa de conceitos, gaps identificados
5. **Construir drugbank.py e chembl.py** -- Bases de medicamentos

## Contexto tecnico ativo

- **Maquina:** i5-1135G7, 24GB RAM, 18GB disco C: livre
- **Google Drive:** G:\Meu Drive (2 TB, 1.35 TB livres)
- **Google Colab:** Configurado, GPU T4, Drive montado
- **GitHub:** terciosilas/discovery-engine (privado, 4 commits, branch main)
- **GitHub CLI:** gh v2.87.3 autenticado
- **Python:** 3.14.2 local, requests instalado
- **Testes:** 40 passando (pytest)
- **Acervo:** 20 referencias, 8 OA, 0 PDFs armazenados
- **APIs:** PubMed (testado), Unpaywall (testado), Semantic Scholar (modulo pronto)
