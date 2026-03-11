# Registro de Decisões — Discovery Engine

> Decisões são IMUTÁVEIS. Se mudar de ideia, criar nova decisão referenciando a anterior.
> Formato: DEC-XXX | Data | Decisão | Alternativas | Motivo | Reversível?

---

## DEC-001: Tema da pesquisa (2026-03-10)

- **Decisão:** Proteínas/Longevidade + Drug Repurposing com IA
- **Título provisório:** "Identificação computacional de compostos geroprotetores via análise proteômica multi-ômica"
- **Alternativas descartadas:**
  1. Tintas de resfriamento radiativo → precisa laboratório para validar formulações
  2. Tratamento de água de baixo custo → precisa laboratório para testes de eficácia
  3. Saneamento básico inovador → mais social/político que computacional
  4. Drug repurposing puro → combinado com proteômica é mais original
- **Motivo:** 100% computacional (não precisa lab), dados públicos imensos (UK Biobank, DrugBank, GenAge, HALL, ChEMBL), gap enorme (biólogos não têm capacidade computacional avançada), potencial de impacto altíssimo
- **Reversível?** Sim, mas investimento significativo a partir da Fase 1

## DEC-002: Infraestrutura (2026-03-10)

- **Decisão:** OneDrive (armazenamento) + Google Colab (processamento) + Claude Code local (orquestração)
- **Alternativas descartadas:**
  1. Tudo local → máquina não aguenta (i5, 18GB disco livre)
  2. Azure VM → custo desnecessário nesta fase
  3. GitHub Codespaces → 60h/mês pode não ser suficiente
- **Motivo:** Gratuito, 785 GB disponíveis no OneDrive, Colab tem GPU grátis, máquina local só orquestra
- **Reversível?** Sim, pode migrar para cloud paga quando necessário

## DEC-003: Governança e ética (2026-03-10)

- **Decisão:** Aplicar mesmo padrão de governança do ERP Callamarys, adaptado para pesquisa científica
- **Inclui:** Audit logs append-only, SHA-256 em todo arquivo, bibliography com licenças verificadas, declaração de uso de IA, critérios de inclusão pré-definidos, código aberto
- **Alternativas descartadas:**
  1. Governança mínima → risco de rejeição em journals por falta de rastreabilidade
  2. Governança total Big4 → excessivo para pesquisa acadêmica
- **Motivo:** Rigor suficiente para publicação em journals de alto impacto sem burocracia excessiva
- **Reversível?** Não — governança é fundacional

## DEC-004: Direitos autorais (2026-03-10)

- **Decisão:** Apenas papers Open Access (CC-BY, CC-BY-SA, CC0) têm PDF armazenado. Papers restritos = apenas metadados + abstract.
- **Alternativas descartadas:**
  1. Usar Sci-Hub → ilegal, compromete integridade da pesquisa
  2. Ignorar papers pagos → perde informação relevante
- **Motivo:** 100% legal, fair use para abstracts, Unpaywall API verifica licença automaticamente
- **Reversível?** Não — integridade acadêmica é inegociável

## DEC-005: Protocolo de continuidade entre sessões (2026-03-10)

- **Decisão:** Sistema de 3 arquivos (STATE.md + DECISIONS.md + BACKLOG.md) em todo projeto, com protocolo de leitura ao iniciar e atualização ao finalizar cada sessão
- **Aplicação:** TODOS os projetos (adicionado ao CLAUDE.md global)
- **Alternativas descartadas:**
  1. Confiar na memória do MEMORY.md → limite de 200 linhas, genérico demais
  2. Resumo no CLAUDE.md → mistura estrutura com estado, fica confuso
  3. Arquivo único SESSION_LOG → cresce infinitamente, perde foco
- **Motivo:** Separa responsabilidades (estado vs. decisões vs. backlog), preserva raciocínio, evita re-debates
- **Reversível?** Sim, mas não há razão para reverter
