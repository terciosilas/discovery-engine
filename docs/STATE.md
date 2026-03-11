# Estado do Projeto -- Discovery Engine

> Ultima atualizacao: 2026-03-10 (Sessao #3)

## Fase Atual

**Fase 0 -- Fundacao (100%)**
**Fase 1 -- Ingestao e Mapeamento (70%)**

## O que foi feito

### Sessao #3 (2026-03-10)
- Construido src/ingestion/filtro.py -- Criterios de inclusao/exclusao
- Construido src/ingestion/orquestrador.py -- Pipeline completo de busca
- **Busca em escala executada:**
  - 6 queries PubMed, 485 papers brutos
  - Deduplicacao: 473 unicos (10 duplicatas, 2 sem DOI)
  - Filtro: 376 aceitos, 97 rejeitados (taxa 79.5%)
  - Licencas: 280 OA (74%), 141 com licenca OA registrada
  - Acervo: 381 referencias
  - Duracao: 3.5 minutos
- Controle positivo (Lehallier 2019) ENCONTRADO no acervo
- DOIs dos controles corrigidos no config
- **Relatorio Fase 1 "Mapa do Terreno" gerado:**
  - Distribuicao temporal (pico em 2025, area em expansao)
  - Top journals: Aging Cell, GeroScience, Nature Comms, Nature Aging
  - Gap identificado: drug repurposing computacional = apenas 6 papers
  - Machine learning aplicado = apenas 10 papers
  - Confirma originalidade da pesquisa

### Sessao #2 (2026-03-10)
- GitHub repo, Colab, Google Drive, modulos core, modulos ingestao, 40 testes

### Sessao #1 (2026-03-10)
- Tema, infraestrutura, governanca, estrutura de pastas

## Raciocinio em andamento

- **Gap confirmado:** Muita proteomica descritiva (o que muda no envelhecimento)
  mas POUCO cruzamento computacional com bases de medicamentos
- Apenas 6 papers mencionam "drug repurposing" no contexto de aging
- Apenas 10 papers usam "machine learning" -- nosso diferencial
- **Proteinas/vias mais estudadas:** mTOR (59), rapamycin (46), mitocondrias (73),
  NAD+ (24), sirtuinas (21), senoliticos (20)
- Essas sao as proteinas/vias que devemos priorizar no cruzamento com DrugBank/ChEMBL
- Proximo: Enriquecer com citation counts e construir modulos de bases de drogas

## Bloqueios atuais

- Nenhum

## Proximo passo concreto

1. **Enriquecer com Semantic Scholar** -- citation_count para os 381 papers
2. **Construir drugbank.py** -- Carregar base de medicamentos
3. **Construir chembl.py** -- Carregar atividade biologica
4. **Identificar top 50 proteinas-alvo** a partir dos papers
5. **Cruzar proteinas x drogas** -- Inicio da Fase 2

## Contexto tecnico ativo

- **Google Drive:** G:\Meu Drive\Discovery_Engine
- **GitHub:** terciosilas/discovery-engine (6 commits)
- **Testes:** 40 passando
- **Acervo:** 381 referencias, 141 OA, 240 restritos
- **Dados:** data/processed/papers_fase1_*.json (376 papers)
- **Relatorio:** outputs/RELATORIO_FASE1_MAPA_DO_TERRENO.md
