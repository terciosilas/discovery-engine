# PMO — Plano Mestre do Projeto Discovery Engine

> "Identificação computacional de compostos geroprotetores via análise proteômica multi-ômica"
> Versão: 1.0 | Data: 2026-03-10 | Operador: Tércio Silas

---

## 1. Visão Geral

### O que é este projeto?
Uma pesquisa científica que usa inteligência artificial para encontrar medicamentos já existentes
que possam retardar o envelhecimento humano. Fazemos isso analisando computacionalmente
milhões de dados sobre proteínas do envelhecimento e cruzando com bases de medicamentos.

### Por que é viável?
- Existem bases de dados públicas com milhões de registros sobre proteínas e medicamentos
- Nenhum ser humano consegue cruzar essas informações manualmente
- IA + computação em nuvem (gratuita) consegue
- Não precisa de laboratório — a contribuição é computacional

### Qual o resultado esperado?
Uma lista priorizada de medicamentos existentes com potencial geroprotetor,
validada estatisticamente, publicada em journal científico de alto impacto.

---

## 2. Fases do Projeto

```
Fase 0: Fundação        ██░░░░░░░░  10%   ← ESTAMOS AQUI
Fase 1: Ingestão        ░░░░░░░░░░   0%
Fase 2: Análise         ░░░░░░░░░░   0%
Fase 3: Validação       ░░░░░░░░░░   0%
Fase 4: Publicação      ░░░░░░░░░░   0%
Fase 5: Extensão        ░░░░░░░░░░   0%   (futuro)
```

### Fase 0 — Fundação (2-3 semanas)
**Objetivo:** Montar toda a infraestrutura e governança.

| Entrega | Descrição |
|---|---|
| Estrutura de pastas | OneDrive organizado conforme padrão |
| GitHub repo privado | Código versionado |
| Google Colab configurado | Ambiente de processamento |
| Módulos core | bibliography.py, audit.py, integrity.py |
| Documentos éticos | Declarações de uso de IA e fontes |
| Pipeline de ingestão básico | Busca no PubMed funcionando |

### Fase 1 — Ingestão e Mapeamento (4-6 semanas)
**Objetivo:** Coletar e organizar o conhecimento existente.

| Entrega | Descrição |
|---|---|
| Base de papers | 1.000+ papers indexados com metadados |
| Base de medicamentos | DrugBank + ChEMBL carregados |
| Base de proteínas | GenAge + HALL + DrugAge carregados |
| Mapa de conceitos | Grafo visual de termos/proteínas/drogas |
| Relatório de gaps | Onde estão as oportunidades |

### Fase 2 — Análise e Cruzamento (6-8 semanas)
**Objetivo:** Cruzar dados e identificar candidatos.

| Entrega | Descrição |
|---|---|
| Grafo de conhecimento | proteína ↔ doença ↔ droga ↔ alvo |
| Modelo ML | Ranqueamento de candidatos geroprotetores |
| Lista de candidatos | Top 20-50 compostos com score de confiança |
| Análise de segurança | Efeitos adversos conhecidos dos candidatos |

### Fase 3 — Validação Computacional (4-6 semanas)
**Objetivo:** Validar os candidatos com rigor científico.

| Entrega | Descrição |
|---|---|
| Validação cruzada | Comparação com literatura e trials existentes |
| Análise estatística | Bootstrap, cross-validation, p-values |
| Docking molecular | Simulação de interação proteína-droga (se viável) |
| Relatório de validação | Documento com nível de confiança por candidato |

### Fase 4 — Publicação (4-8 semanas)
**Objetivo:** Publicar em journal científico.

| Entrega | Descrição |
|---|---|
| Paper completo | Formato IMRaD (Introdução, Métodos, Resultados, Discussão) |
| Material suplementar | Código, dados, queries (tudo reproduzível) |
| Preprint | Publicado no bioRxiv/medRxiv |
| Submissão a journal | Paper submetido para peer review |

---

## 3. Como validamos a pesquisa

> "Tércio, validação científica tem 3 camadas. Pense como a validação de 3 camadas do ERP."

### Camada 1 — Validação Interna (nós fazemos)

| Teste | O que verifica | Como |
|---|---|---|
| **Reprodutibilidade** | Mesmo input → mesmo output? | Rodar pipeline 3x, comparar resultados |
| **Cross-validation** | Modelo funciona com dados que nunca viu? | Separar 20% dos dados, treinar com 80%, testar com 20% |
| **Bootstrap** | Resultados são estáveis? | Reamostrar 1.000x, verificar se ranking muda |
| **Ablation study** | Cada componente contribui? | Remover uma feature por vez, medir impacto |
| **Análise de sensibilidade** | Resultado muda com parâmetros diferentes? | Variar thresholds, verificar robustez |
| **Controle positivo** | Sistema encontra o que já se sabe? | Testar se identifica geroprotetores conhecidos (rapamicina, metformina) |
| **Controle negativo** | Sistema rejeita o que não funciona? | Testar com drogas sabidamente ineficazes |

**Regra de ouro:** Se o sistema não encontra rapamicina e metformina como candidatos,
algo está errado com a metodologia. Esses são os "controles positivos" — sabemos que funcionam.

### Camada 2 — Validação por Pares (outros verificam)

| Etapa | O que acontece | Quem faz |
|---|---|---|
| **Preprint** | Publicar versão preliminar no bioRxiv/medRxiv | Nós publicamos, comunidade comenta |
| **Peer Review** | Journal envia para 2-3 especialistas anônimos | Especialistas da área |
| **Revisões** | Pareceristas apontam falhas, pedem correções | Nós corrigimos e resubmetemos |
| **Aceitação** | Paper aprovado após revisões | Editor do journal decide |

**O que os pareceristas avaliam:**
- Metodologia é sólida? (estatística, ML, dados)
- Resultados são reproduzíveis? (código e dados disponíveis?)
- Conclusões são suportadas pelos dados? (sem overclaim)
- Limitações são reconhecidas? (honestidade intelectual)
- Contribuição é original? (não repete o que já existe)

### Camada 3 — Validação Experimental (futuro, outros fazem)

| Etapa | O que acontece | Quem faz |
|---|---|---|
| **Validação in vitro** | Testar candidatos em células | Laboratório parceiro |
| **Validação in vivo** | Testar em organismos modelo | Laboratório parceiro |
| **Ensaio clínico** | Testar em humanos | Instituição de pesquisa |

**Importante:** Nossa pesquisa é COMPUTACIONAL. A Camada 3 não é nossa responsabilidade.
O que publicamos é: "Identificamos estes candidatos com este nível de confiança.
Recomendamos validação experimental." Se alguém validar experimentalmente e confirmar,
aí sim temos potencial Nobel.

---

## 4. Como testamos o sistema

> "Testes no Discovery Engine funcionam como no ERP — automatizados, em camadas."

### Testes unitários (`tests/`)

```python
# Exemplo: testar se o módulo de busca retorna resultados válidos
def test_pubmed_search_returns_results():
    results = search_pubmed("proteomics aging", max_results=10)
    assert len(results) > 0
    assert all(r.doi for r in results)

# Exemplo: testar se o controle positivo funciona
def test_positive_control_rapamycin():
    candidates = run_pipeline(target_proteins=AGING_PROTEINS)
    rapamycin_found = any(c.name == "rapamycin" for c in candidates)
    assert rapamycin_found, "Pipeline falhou no controle positivo: rapamicina não encontrada"
```

### Testes de integração

| Teste | Verifica |
|---|---|
| Pipeline end-to-end | Dados entram crus → candidatos saem ranqueados |
| Integridade de dados | SHA-256 dos inputs não mudou durante processamento |
| Reprodutibilidade | Mesma execução 2x → mesmo resultado |
| Audit trail | Todo passo foi logado em audit_logs/ |

### Testes de qualidade dos dados

| Teste | Verifica |
|---|---|
| Completude | Todos os campos obrigatórios preenchidos? |
| Duplicatas | Mesmo paper/droga aparece 2x? |
| Consistência | DOI resolve para o paper correto? |
| Licenças | Todo PDF armazenado tem licença open access verificada? |

---

## 5. Onde submeter a pesquisa

> "Tércio, journals científicos são como ligas de futebol — têm divisões.
> Vamos mirar na primeira divisão, mas com plano B e C."

### O que é um Journal?

Revista científica que publica pesquisas revisadas por especialistas (peer review).
Cada journal tem um **Fator de Impacto (IF)** — quanto maior, mais prestigioso.
Para referência: Nature tem IF ~64, Science ~56. IF >10 é excelente. IF >5 é muito bom.

### Estratégia de publicação em 2 etapas

**Etapa 1 — Preprint (publicação imediata, sem peer review)**

| Plataforma | Área | Custo | Tempo |
|---|---|---|---|
| **bioRxiv** | Biologia | Grátis | 24-48h |
| **medRxiv** | Medicina | Grátis | 24-48h |
| **arXiv** | Computação/IA | Grátis | 24-48h |

- Publica imediatamente (sem esperar revisão)
- Garante **prioridade da descoberta** (carimbo de data)
- Comunidade pode comentar e dar feedback
- Muitos pesquisadores publicam aqui primeiro e depois submetem ao journal
- NÃO é publicação definitiva, mas é aceito e respeitado

**Etapa 2 — Journal com peer review (publicação definitiva)**

#### Alvos primários (IF > 10) — "Primeira divisão"

| Journal | IF | Área | Open Access | Taxa de publicação |
|---|---|---|---|---|
| **Nature Aging** | ~17 | Envelhecimento | Híbrido | ~€9.500 (se OA) |
| **Aging Cell** | ~11 | Biologia do envelhecimento | Sim | ~€3.200 |
| **Nature Communications** | ~17 | Multidisciplinar | Sim | ~€5.790 |
| **Briefings in Bioinformatics** | ~14 | Bioinformática | Híbrido | Grátis (se não OA) |
| **npj Aging** | ~5 | Envelhecimento | Sim | Grátis |

#### Alvos secundários (IF 5-10) — "Plano B"

| Journal | IF | Área | Open Access | Taxa |
|---|---|---|---|---|
| **GeroScience** | ~7 | Gerociência | Híbrido | ~€3.390 (se OA) |
| **Frontiers in Aging** | ~4 | Envelhecimento | Sim | ~€2.950 |
| **Aging** | ~5 | Envelhecimento | Sim | ~€3.400 |
| **Drug Discovery Today** | ~8 | Drug discovery | Híbrido | Grátis (se não OA) |
| **Bioinformatics** | ~6 | Bioinformática | Híbrido | Grátis (se não OA) |

#### Alvos terciários (IF < 5) — "Plano C, garantido"

| Journal | IF | Área | Open Access | Taxa |
|---|---|---|---|---|
| **PLOS ONE** | ~3 | Multidisciplinar | Sim | ~$2.290 |
| **Scientific Reports** | ~4 | Multidisciplinar | Sim | ~€2.190 |
| **PeerJ** | ~3 | Biologia | Sim | ~$1.700 |
| **Molecules** | ~5 | Química/Farmacologia | Sim | ~CHF 2.700 |
| **International Journal of Molecular Sciences** | ~5 | Biologia molecular | Sim | ~CHF 2.700 |

### Custos — como reduzir

| Estratégia | Como funciona |
|---|---|
| **Journals gratuitos** | Briefings in Bioinformatics, npj Aging, Drug Discovery Today não cobram se não for OA |
| **Waiver** | Muitos journals concedem isenção para pesquisadores de países em desenvolvimento |
| **Preprint como "publicação"** | bioRxiv é gratuito e muitas vezes suficiente para reconhecimento |
| **Journals com taxa baixa** | PeerJ (~$1.700) é respeitado e acessível |

### Processo de submissão passo a passo

```
1. PREPARAÇÃO (antes de submeter)
   ├── Paper no formato do journal (cada um tem template próprio)
   ├── Carta de apresentação (cover letter) ao editor
   ├── Declaração de conflito de interesses
   ├── Declaração de uso de IA
   ├── Código e dados em repositório público (GitHub/Zenodo)
   └── Material suplementar organizado

2. SUBMISSÃO (online, pelo site do journal)
   ├── Criar conta no sistema de submissão do journal
   ├── Upload do manuscrito + suplementar
   ├── Sugerir 3-5 revisores (opcional mas recomendado)
   └── Pagar taxa (se aplicável) ou solicitar waiver

3. TRIAGEM EDITORIAL (1-2 semanas)
   ├── Editor-chefe avalia se o paper é adequado para o journal
   ├── Se sim → envia para peer review
   └── Se não → "desk rejection" (rápido, sem revisão)
       → Submeter ao próximo journal da lista

4. PEER REVIEW (4-12 semanas)
   ├── 2-3 revisores anônimos avaliam o paper
   ├── Escrevem relatório com críticas e sugestões
   └── Recomendam: aceitar / revisão menor / revisão maior / rejeitar

5. DECISÃO EDITORIAL
   ├── ACEITO → parabéns! Paper publicado.
   ├── REVISÃO MENOR → corrigir detalhes, resubmeter (1-2 semanas)
   ├── REVISÃO MAIOR → mudanças significativas, resubmeter (4-8 semanas)
   └── REJEITADO → analisar feedback, melhorar, submeter ao próximo journal

6. PUBLICAÇÃO
   ├── Prova final (galley proof) para revisão de erros tipográficos
   ├── Paper online (geralmente em 1-2 semanas após aceitação)
   └── DOI atribuído — paper é permanente e citável
```

### Linha do tempo realista

```
Mês 1-2:   Fase 0 (Fundação) + início Fase 1
Mês 3-4:   Fase 1 (Ingestão e Mapeamento)
Mês 5-7:   Fase 2 (Análise e Cruzamento)
Mês 8-9:   Fase 3 (Validação)
Mês 10:    Fase 4a (Escrita do paper)
Mês 11:    Preprint no bioRxiv (publicação imediata)
Mês 12:    Submissão ao journal-alvo
Mês 13-18: Peer review + revisões + publicação final
```

**Total estimado: 12-18 meses** do início à publicação.

---

## 6. Glossário para o Operador

> "Tércio, quando eu usar estes termos, é isso que significam."

| Termo | O que significa |
|---|---|
| **Proteômica** | Estudo de todas as proteínas de um organismo |
| **Geroprotetor** | Substância que retarda o envelhecimento |
| **Drug repurposing** | Encontrar novo uso para medicamento já existente |
| **Multi-ômica** | Combinar dados de proteínas, genes, metabólitos |
| **Meta-análise** | Análise que combina resultados de muitos estudos |
| **Machine Learning (ML)** | IA que aprende padrões a partir de dados |
| **Preprint** | Paper publicado antes da revisão por pares |
| **Peer review** | Revisão por especialistas anônimos |
| **Journal** | Revista científica que publica pesquisas |
| **Fator de Impacto (IF)** | Medida de prestígio de um journal |
| **DOI** | Identificador único e permanente de um paper |
| **BibTeX** | Formato padrão para gerenciar referências bibliográficas |
| **Open Access** | Publicação gratuita para leitura (pode custar para publicar) |
| **IMRaD** | Formato padrão de paper: Introdução, Métodos, Resultados e Discussão |
| **Cross-validation** | Técnica para testar se o modelo generaliza |
| **Bootstrap** | Reamostragem estatística para medir estabilidade |
| **Controle positivo** | Teste com algo que sabemos que funciona (ex: rapamicina) |
| **Controle negativo** | Teste com algo que sabemos que NÃO funciona |
| **Ablation study** | Remover uma parte por vez para ver o que contribui |
| **Docking molecular** | Simulação de como uma droga encaixa numa proteína |
| **Cover letter** | Carta ao editor explicando por que o paper é relevante |
| **Desk rejection** | Rejeição rápida pelo editor sem enviar para revisores |
| **Waiver** | Isenção de taxa de publicação |
| **Sirtuína** | Família de proteínas que regulam envelhecimento |
| **Klotho** | Proteína anti-envelhecimento ("proteína da juventude") |
| **FOXO3** | Gene mais consistentemente associado a longevidade humana |
| **mTOR** | Via de crescimento celular — inibir retarda envelhecimento |
| **Senolítico** | Droga que mata células envelhecidas (senescentes) |
| **NAD+** | Molécula essencial para energia celular, declina com a idade |
| **Telomerase** | Enzima que protege as pontas dos cromossomos |
| **SASP** | Substâncias tóxicas secretadas por células velhas |
| **UK Biobank** | Maior base de dados biomédica do mundo (500.000 pessoas) |
| **DrugBank** | Base de dados de medicamentos e alvos |
| **ChEMBL** | Base de dados de atividade biológica de compostos |
| **GenAge** | Base de dados de genes do envelhecimento |
| **PubMed** | Base de dados de artigos médicos/biológicos |

---

## 7. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Resultados inconclusivos | Média | Alto | Controles positivos/negativos desde o início |
| Paper rejeitado no journal A | Alta (normal) | Baixo | Lista de 15 journals alternativos |
| Pesquisa similar publicada antes | Média | Alto | Preprint no bioRxiv garante prioridade de data |
| Google Colab insuficiente | Baixa | Médio | Migrar para Colab Pro ($10/mês) ou Kaggle |
| Custo de publicação alto | Média | Médio | Journals gratuitos + solicitação de waiver |
| Perda de dados | Baixa | Crítico | OneDrive com versionamento + GitHub |
| Questões éticas não previstas | Baixa | Alto | Consultar diretrizes COPE antes de submeter |

---

## 8. Métricas de Sucesso

| Fase | Métrica | Meta |
|---|---|---|
| Fase 1 | Papers indexados | > 1.000 |
| Fase 1 | Fontes de dados integradas | > 5 |
| Fase 2 | Candidatos identificados | 20-50 compostos |
| Fase 3 | Controle positivo encontrado | Rapamicina + Metformina no top 10 |
| Fase 3 | Reprodutibilidade | 100% (mesmo resultado em 3 execuções) |
| Fase 4 | Preprint publicado | Sim |
| Fase 4 | Paper aceito em journal IF > 5 | Sim |
