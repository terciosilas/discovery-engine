# Estado do Projeto — Discovery Engine

> Última atualização: 2026-03-10 (Sessão #1)

## Fase Atual

**Fase 0 — Fundação (10% concluída)**

## O que foi feito

### Sessão #1 (2026-03-10)
- Definido tema: Proteínas/Longevidade + Drug Repurposing com IA
- Pesquisa exploratória em 5 campos (resfriamento, água, saneamento, proteínas, drug repurposing)
- Definida infraestrutura: OneDrive + Google Colab + Claude Code local
- Definida governança: espelho do ERP (audit_logs, SHA-256, bibliography, ética)
- Criada estrutura de pastas no OneDrive
- Criados documentos fundacionais (CLAUDE.md, STATE.md, DECISIONS.md, BACKLOG.md, PMO.md)
- Adicionado Protocolo de Continuidade ao CLAUDE.md global (todos os projetos)

## Raciocínio em andamento

- Combinamos proteômica de longevidade com drug repurposing porque é **100% computacional**
  e tem datasets públicos imensos (UK Biobank, DrugBank, GenAge, HALL, ChEMBL)
- A abordagem é meta-análise computacional com ML/IA — não experimental
- O diferencial seria: usar IA para cruzar dados proteômicos de envelhecimento com bases
  de medicamentos existentes, identificando candidatos que pesquisadores de bancada não
  conseguiriam encontrar por limitação humana de escala
- Não precisamos de laboratório — a validação é computacional + estatística,
  e o resultado é uma lista priorizada de candidatos para validação experimental por terceiros
- O operador (Tércio) é leigo em biologia — todo o vocabulário técnico deve ser
  explicado em termos acessíveis

## Bloqueios atuais

- Nenhum bloqueio técnico
- Tércio ainda não configurou Google Colab (nunca usou)
- GitHub repo privado ainda não criado

## Próximo passo concreto

1. **Configurar Google Colab** — tutorial guiado para Tércio
2. **Criar repo privado no GitHub** — `discovery-engine`
3. **Construir módulo `src/core/bibliography.py`** — gestão de referências BibTeX + licenças
4. **Construir módulo `src/ingestion/pubmed.py`** — pipeline de busca no PubMed via API
5. **Primeira busca exploratória** — 100 papers mais citados sobre proteômica do envelhecimento

## Contexto técnico ativo

- **Máquina:** i5-1135G7, 24GB RAM, 18GB disco C: livre — NÃO sobrecarregar
- **OneDrive:** 785 GB livres no plano 1TB
- **Google Colab:** Não configurado ainda
- **GitHub:** Tem conta (github.com/terciosilas), repo ainda não criado
- **APIs:** PubMed (grátis, sem key), Semantic Scholar (grátis, key opcional)
