# Declaração de Fontes e Direitos Autorais

> Projeto: Discovery Engine
> Data: 2026-03-10
> Pesquisador: Tércio Silas Azevedo

---

## Política de Acesso a Fontes

Este projeto utiliza **exclusivamente** fontes legais e éticas para obtenção de literatura científica:

### Fontes autorizadas

| Fonte | Tipo | Licença |
|---|---|---|
| PubMed / PubMed Central | Artigos open access | Licenças CC variadas |
| arXiv / bioRxiv / medRxiv | Preprints | CC-BY ou equivalente |
| Semantic Scholar | Metadados + abstracts | API aberta |
| Unpaywall | Verificação de licença | API aberta |
| DOAJ | Diretório de journals OA | Aberto |
| Google Scholar | Metadados | Aberto |

### Bases de dados autorizadas

| Base | Tipo | Licença |
|---|---|---|
| DrugBank | Medicamentos | Creative Commons |
| ChEMBL | Atividade biológica | CC-BY-SA |
| GenAge / DrugAge / AnAge | Genes do envelhecimento | Aberto |
| HALL | Longevidade humana | Aberto |
| UniProt | Proteínas | CC-BY |
| Human Protein Atlas | Expressão proteica | CC-BY-SA |

### Fontes PROIBIDAS

- Sci-Hub
- Library Genesis (LibGen)
- Qualquer repositório não autorizado de papers

## Regras de armazenamento

1. **Papers Open Access (CC-BY, CC-BY-SA, CC0):** PDF completo armazenado em `data/raw/papers/`
2. **Papers com restrição de acesso:** Apenas metadados e abstract armazenados
3. Todo paper armazenado tem registro em `bibliography/license_registry.json` com:
   - DOI
   - Licença verificada via Unpaywall
   - Hash SHA-256 do arquivo
   - Data de download
4. Verificação de licença é AUTOMATIZADA — o sistema não permite armazenamento sem licença verificada

## Citação

Todas as fontes utilizadas são citadas no formato BibTeX em `bibliography/references.bib`.
Nenhuma informação é utilizada sem atribuição adequada ao autor original.
