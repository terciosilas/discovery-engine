# CLAUDE.md — Discovery Engine

> Pesquisa científica: Identificação computacional de compostos geroprotetores via análise proteômica multi-ômica
> Local: OneDrive/Discovery_Engine
> Operador: Tércio Silas (leigo em biologia/medicina — Claude Code compensa a lacuna técnica)

---

## Objetivo

Construir um sistema computacional que cruza dados proteômicos de envelhecimento com bases de medicamentos existentes para identificar candidatos a geroprotetores (drug repurposing). Pesquisa publicável em journal de alto impacto.

## Stack Técnico

| Componente | Tecnologia | Onde roda |
|---|---|---|
| Orquestração | Claude Code | Local (máquina Tércio) |
| Processamento pesado | Google Colab (GPU grátis) | Nuvem Google |
| Armazenamento | OneDrive (785 GB livres) | Nuvem Microsoft |
| Código | Python 3.10+ | Colab + Local |
| Banco de dados | SQLite (portável, funciona no OneDrive) | OneDrive |
| Versionamento | GitHub (repo PRIVADO) | Nuvem GitHub |
| Análise exploratória | Jupyter Notebooks | Colab |
| APIs científicas | PubMed, Semantic Scholar, Unpaywall, DrugBank, ChEMBL | Gratuitas |

## Restrições de Infraestrutura

- **Máquina local:** i5-1135G7, 24GB RAM, 18GB disco livre — NÃO sobrecarregar
- Processamento pesado SEMPRE no Google Colab
- Dados SEMPRE no OneDrive (nunca acumular no disco C:)
- Scripts locais devem ser leves (chamadas API, orquestração)

## Regras Específicas do Projeto

### Direitos Autorais
- NUNCA baixar papers de fontes piratas (Sci-Hub, Library Genesis)
- Verificar licença via Unpaywall API ANTES de armazenar PDF
- Open Access (CC-BY, CC-BY-SA, CC0) → baixar PDF completo
- Restrito → guardar APENAS metadados + abstract (fair use)
- Registrar DOI + SHA-256 + licença em `bibliography/license_registry.json`

### Ética em Pesquisa
- Declarar uso de IA em toda publicação
- Critérios de inclusão/exclusão definidos ANTES das buscas (não post-hoc)
- Resultados negativos são resultados válidos — NUNCA omitir
- Transparência metodológica total: código aberto, queries documentadas

### Segurança
- Repositório GitHub PRIVADO
- API keys em `.env`, NUNCA no git
- SHA-256 em todo arquivo de dados (integridade)
- Audit log de todo acesso a dados

### Governança
- Segue o padrão global (~/.claude/GOVERNANCA.md) adaptado para pesquisa
- `audit_logs/` append-only
- `config/` versionado no git
- Outputs com timestamp, nunca sobrescrever

## Estrutura de Pastas

```
Discovery_Engine/
├── CLAUDE.md                  ← Este arquivo
├── docs/
│   ├── STATE.md               ← Estado atual (atualizado toda sessão)
│   ├── DECISIONS.md           ← Registro de decisões
│   ├── BACKLOG.md             ← O que falta fazer
│   └── PMO.md                 ← Plano mestre do projeto
├── src/
│   ├── core/                  ← Módulos fundamentais
│   ├── ingestion/             ← Coleta de papers e dados
│   ├── analysis/              ← Processamento e análise
│   └── reporting/             ← Geração de relatórios
├── config/                    ← Parâmetros versionados (git)
├── data/
│   ├── raw/                   ← Dados originais (SAGRADOS)
│   ├── processed/             ← Dados processados
│   └── analysis/              ← Resultados de análise
├── bibliography/              ← BibTeX, licenças, DOIs
├── ethics/                    ← Declarações éticas
├── audit_logs/                ← Logs append-only
├── outputs/                   ← Relatórios com timestamp
├── tests/                     ← Testes automatizados
├── notebooks/                 ← Jupyter para Colab
└── security/                  ← .env e configs sensíveis
```

## Comandos Úteis

```bash
# Abrir o projeto
cd "C:\Users\tercio.azevedo\OneDrive\Discovery_Engine" && claude

# Retomar sessão
"Retome o projeto. Leia STATE.md, DECISIONS.md e BACKLOG.md."
```
