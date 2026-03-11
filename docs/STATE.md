# Estado do Projeto -- Discovery Engine

> Ultima atualizacao: 2026-03-10 (Sessao #4)

## Fase Atual

**Fase 0 -- Fundacao (100%)**
**Fase 1 -- Ingestao e Mapeamento (100%)**
**Fase 2 -- Analise e Cruzamento (0%)**

## O que foi feito

### Sessao #4 (2026-03-10)
- Construido `src/ingestion/enriquecedor.py` -- Enriquecimento S2 com checkpoint incremental
- Construido `src/ingestion/chembl.py` -- Cliente API ChEMBL (compostos, alvos, atividades)
- Construido `src/ingestion/drugbank.py` -- DrugBank vocabulario + Open Targets GraphQL
  - 13 geroprotetores conhecidos curados (rapamycin, metformin, resveratrol, etc.)
  - 15 alvos-chave do envelhecimento curados (MTOR, SIRT1, FOXO3, etc.)
- Adicionado `get_papers_batch()` ao Semantic Scholar (POST /paper/batch)
- **Enriquecimento S2 executado:**
  - 356/376 papers encontrados no S2 (94.7% cobertura)
  - 20 papers genuinamente nao indexados no S2
  - Total citacoes: 420,749 | Media: 1,181.9 | Mediana: 43
  - Checkpoint incremental funcionou (retomou de 189 para 356)
- **77 testes passando** (37 novos: 10 enriquecedor, 23 chembl/drugbank, 4 dados curados)
- Corrigido rate limit S2: retry com backoff exponencial no get_paper()

### Sessao #3 (2026-03-10)
- Construido filtro.py e orquestrador.py
- Busca em escala: 485 brutos, 376 aceitos, 97 rejeitados
- Relatorio Fase 1 "Mapa do Terreno" gerado
- Gap confirmado: drug repurposing computacional = apenas 6 papers

### Sessao #2 (2026-03-10)
- GitHub repo, Colab, Google Drive, modulos core, modulos ingestao, 40 testes

### Sessao #1 (2026-03-10)
- Tema, infraestrutura, governanca, estrutura de pastas

## Raciocinio em andamento

- **Fase 1 CONCLUIDA.** Acervo completo com 376 papers, 356 enriquecidos com citacoes.
- **Modulos de drogas prontos:** ChEMBL client + Open Targets client + geroprotetores curados.
- **Proxima fase (2) requer:**
  1. Extrair proteinas-alvo dos abstracts dos 376 papers (NER ou regex)
  2. Consultar ChEMBL/Open Targets para cada proteina-alvo
  3. Construir grafo de conhecimento: proteina <-> droga <-> doenca
  4. Aplicar ML para ranquear candidatos a geroprotetores
- **Observacao sobre citacoes:** Alguns papers no top-10 tem DOIs mismatched
  (DOI aponta para paper antigo com muitas citacoes). Mediana de 43 e mais
  representativa. Limpeza de DOIs mismatched e desejavel mas nao critica.

## Bloqueios atuais

- Nenhum

## Proximo passo concreto

1. **Extrair proteinas-alvo dos abstracts** (NER com scispaCy ou regex curado)
2. **Consultar Open Targets para cada alvo** -- drogas associadas
3. **Consultar ChEMBL para atividades** -- potencia (IC50/Ki) de drogas nos alvos
4. **Construir grafo de conhecimento** -- NetworkX ou similar
5. **Ranquear candidatos** -- Score baseado em citacoes + potencia + fase clinica

## Contexto tecnico ativo

- **Google Drive:** G:\Meu Drive\Discovery_Engine
- **GitHub:** terciosilas/discovery-engine (9 commits)
- **Testes:** 77 passando
- **Acervo:** 376 papers aceitos, 356 enriquecidos S2 (94.7%)
- **Dados:**
  - data/processed/papers_fase1_*.json (376 papers PubMed)
  - data/processed/papers_enriched_fase1_*.json (356 com citacoes S2)
  - data/checkpoints/ckpt_enrich_*.json (checkpoint de enriquecimento)
- **Modulos de drogas:** chembl.py, drugbank.py (Open Targets + dados curados)
- **Relatorio:** outputs/RELATORIO_FASE1_MAPA_DO_TERRENO.md
