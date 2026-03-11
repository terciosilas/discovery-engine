"""Modulo de acesso a dados de medicamentos.

Combina dados do DrugBank (vocabulario aberto) com Open Targets
para associacoes droga-proteina-doenca.

DrugBank XML completo requer registro em https://go.drugbank.com/
O vocabulario aberto (nomes, categorias, IDs) e livre.
Open Targets REST API e totalmente publica.
"""

import csv
import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import requests

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

OPEN_TARGETS_URL = "https://api.platform.opentargets.org/api/v4/graphql"


@dataclass
class Drug:
    """Representa um medicamento."""

    drugbank_id: str = ""
    nome: str = ""
    tipo: str = ""  # small molecule, biotech, etc.
    categorias: list[str] = field(default_factory=list)
    cas_number: str = ""
    unii: str = ""
    chembl_id: str = ""
    fase_clinica: int = 0  # 0-4
    alvos: list[dict[str, str]] = field(default_factory=list)  # [{gene, uniprot_id, acao}]
    indicacoes: list[str] = field(default_factory=list)
    mecanismo_acao: str = ""
    aprovado: bool = False

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "drugbank_id": self.drugbank_id,
            "nome": self.nome,
            "tipo": self.tipo,
            "categorias": self.categorias,
            "cas_number": self.cas_number,
            "unii": self.unii,
            "chembl_id": self.chembl_id,
            "fase_clinica": self.fase_clinica,
            "alvos": self.alvos,
            "indicacoes": self.indicacoes,
            "mecanismo_acao": self.mecanismo_acao,
            "aprovado": self.aprovado,
        }


@dataclass
class DrugTargetAssociation:
    """Associacao droga-alvo do Open Targets."""

    drug_id: str = ""
    drug_nome: str = ""
    target_id: str = ""  # Ensembl gene ID
    target_gene: str = ""
    target_nome: str = ""
    disease_id: str = ""
    disease_nome: str = ""
    fase_clinica: int = 0
    mecanismo_acao: str = ""
    tipo_acao: str = ""  # inhibitor, agonist, etc.
    fonte: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "drug_id": self.drug_id,
            "drug_nome": self.drug_nome,
            "target_id": self.target_id,
            "target_gene": self.target_gene,
            "target_nome": self.target_nome,
            "disease_id": self.disease_id,
            "disease_nome": self.disease_nome,
            "fase_clinica": self.fase_clinica,
            "mecanismo_acao": self.mecanismo_acao,
            "tipo_acao": self.tipo_acao,
            "fonte": self.fonte,
        }


class DrugBankVocabulary:
    """Carregador do vocabulario aberto do DrugBank.

    O arquivo drugbank_vocabulary.csv contem nomes, IDs e tipos
    de todos os medicamentos. Disponivel em:
    https://go.drugbank.com/releases/latest#open-data
    """

    def __init__(self, vocab_path: Path | None = None) -> None:
        """Inicializa o carregador.

        Args:
            vocab_path: Caminho do CSV de vocabulario.
                Padrao: data/external/drugbank_vocabulary.csv
        """
        self.vocab_path = vocab_path or DATA_DIR / "external" / "drugbank_vocabulary.csv"
        self._drugs: dict[str, Drug] = {}
        self._by_name: dict[str, str] = {}  # nome_lower -> drugbank_id

    def carregar(self) -> int:
        """Carrega o vocabulario do CSV.

        Returns:
            Numero de medicamentos carregados.

        Raises:
            FileNotFoundError: Se o arquivo nao existe.
        """
        if not self.vocab_path.exists():
            raise FileNotFoundError(
                f"Vocabulario DrugBank nao encontrado: {self.vocab_path}\n"
                "Baixe de: https://go.drugbank.com/releases/latest#open-data\n"
                "Salve em: data/external/drugbank_vocabulary.csv"
            )

        # Detectar encoding
        for encoding in ["utf-8", "cp1252", "latin-1"]:
            try:
                with open(self.vocab_path, "r", encoding=encoding) as f:
                    f.read(1024)
                break
            except UnicodeDecodeError:
                continue

        with open(self.vocab_path, "r", encoding=encoding, newline="") as f:
            # Detectar delimitador
            sample = f.read(2048)
            f.seek(0)
            delimiter = "," if sample.count(",") > sample.count(";") else ";"
            reader = csv.DictReader(f, delimiter=delimiter)

            for row in reader:
                drug = Drug()
                drug.drugbank_id = row.get("DrugBank ID", "").strip()
                drug.nome = row.get("Common name", "").strip()
                drug.tipo = row.get("Type", "").strip()
                drug.cas_number = row.get("CAS Number", "").strip()
                drug.unii = row.get("UNII", "").strip()

                if drug.drugbank_id:
                    self._drugs[drug.drugbank_id] = drug
                    if drug.nome:
                        self._by_name[drug.nome.lower()] = drug.drugbank_id

        logger.info("DrugBank vocabulario carregado: %d medicamentos", len(self._drugs))
        return len(self._drugs)

    def buscar_por_id(self, drugbank_id: str) -> Drug | None:
        """Busca medicamento por DrugBank ID.

        Args:
            drugbank_id: Ex: "DB00945" (aspirina).

        Returns:
            Drug ou None.
        """
        return self._drugs.get(drugbank_id)

    def buscar_por_nome(self, nome: str) -> Drug | None:
        """Busca medicamento por nome.

        Args:
            nome: Nome do medicamento (case insensitive).

        Returns:
            Drug ou None.
        """
        drugbank_id = self._by_name.get(nome.lower())
        if drugbank_id:
            return self._drugs.get(drugbank_id)
        return None

    def listar_todos(self) -> list[Drug]:
        """Lista todos os medicamentos carregados."""
        return list(self._drugs.values())

    @property
    def total(self) -> int:
        """Total de medicamentos carregados."""
        return len(self._drugs)


class OpenTargetsClient:
    """Cliente GraphQL para a API do Open Targets.

    Fornece associacoes droga-alvo-doenca validadas.
    API publica sem necessidade de registro.
    """

    def __init__(self) -> None:
        """Inicializa o cliente Open Targets."""
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"
        self._last_request_time: float = 0.0

    def _rate_limit(self) -> None:
        """Aguarda tempo minimo entre requisicoes."""
        elapsed = time.time() - self._last_request_time
        if elapsed < 0.5:
            time.sleep(0.5 - elapsed)
        self._last_request_time = time.time()

    def _query(self, query: str, variables: dict | None = None) -> dict | None:
        """Executa query GraphQL no Open Targets.

        Args:
            query: Query GraphQL.
            variables: Variaveis da query.

        Returns:
            JSON de resposta ou None em caso de erro.
        """
        self._rate_limit()

        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        try:
            response = self.session.post(OPEN_TARGETS_URL, json=payload, timeout=30)
            if response.status_code == 429:
                logger.warning("Open Targets rate limit. Aguardando 5s...")
                time.sleep(5)
                return self._query(query, variables)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Erro Open Targets API: %s", e)
            return None

    def buscar_drogas_por_alvo(
        self,
        ensembl_gene_id: str,
        max_results: int = 50,
    ) -> list[DrugTargetAssociation]:
        """Busca drogas associadas a um gene/proteina.

        Args:
            ensembl_gene_id: ID Ensembl do gene (ex: "ENSG00000198793" para mTOR).
            max_results: Maximo de resultados.

        Returns:
            Lista de DrugTargetAssociation.
        """
        query = """
        query DrugsByTarget($ensemblId: String!, $size: Int!) {
          target(ensemblId: $ensemblId) {
            id
            approvedSymbol
            approvedName
            knownDrugs(size: $size) {
              uniqueDrugs
              uniqueTargets
              count
              rows {
                drug {
                  id
                  name
                  maximumClinicalTrialPhase
                  mechanismsOfAction {
                    rows {
                      mechanismOfAction
                      actionType
                    }
                  }
                }
                disease {
                  id
                  name
                }
                phase
                ctIds
              }
            }
          }
        }
        """
        variables = {"ensemblId": ensembl_gene_id, "size": max_results}
        data = self._query(query, variables)

        if data is None or "data" not in data:
            return []

        target_data = data["data"].get("target")
        if target_data is None:
            logger.debug("Gene nao encontrado no Open Targets: %s", ensembl_gene_id)
            return []

        gene_symbol = target_data.get("approvedSymbol", "")
        gene_name = target_data.get("approvedName", "")
        known_drugs = target_data.get("knownDrugs") or {}

        associations = []
        for row in known_drugs.get("rows", []):
            drug_info = row.get("drug", {})
            disease_info = row.get("disease") or {}

            assoc = DrugTargetAssociation()
            assoc.drug_id = drug_info.get("id", "")
            assoc.drug_nome = drug_info.get("name", "")
            assoc.target_id = ensembl_gene_id
            assoc.target_gene = gene_symbol
            assoc.target_nome = gene_name
            assoc.disease_id = disease_info.get("id", "")
            assoc.disease_nome = disease_info.get("name", "")
            assoc.fase_clinica = row.get("phase") or 0
            assoc.fonte = "open_targets"

            # Mecanismo de acao
            moa = drug_info.get("mechanismsOfAction", {})
            moa_rows = moa.get("rows", []) if moa else []
            if moa_rows:
                assoc.mecanismo_acao = moa_rows[0].get("mechanismOfAction", "")
                assoc.tipo_acao = moa_rows[0].get("actionType", "")

            associations.append(assoc)

        logger.info(
            "Open Targets: %d associacoes droga-alvo para %s (%s)",
            len(associations), gene_symbol, ensembl_gene_id,
        )
        return associations

    def buscar_alvos_por_droga(self, drug_id: str, max_results: int = 50) -> list[DrugTargetAssociation]:
        """Busca alvos de uma droga especifica.

        Args:
            drug_id: ChEMBL ID da droga (ex: "CHEMBL413").
            max_results: Maximo de resultados.

        Returns:
            Lista de DrugTargetAssociation.
        """
        query = """
        query TargetsByDrug($chemblId: String!, $size: Int!) {
          drug(chemblId: $chemblId) {
            id
            name
            maximumClinicalTrialPhase
            knownDrugs(size: $size) {
              rows {
                target {
                  id
                  approvedSymbol
                  approvedName
                }
                disease {
                  id
                  name
                }
                phase
              }
            }
          }
        }
        """
        variables = {"chemblId": drug_id, "size": max_results}
        data = self._query(query, variables)

        if data is None or "data" not in data:
            return []

        drug_data = data["data"].get("drug")
        if drug_data is None:
            logger.debug("Droga nao encontrada no Open Targets: %s", drug_id)
            return []

        drug_name = drug_data.get("name", "")
        known_drugs = drug_data.get("knownDrugs") or {}

        associations = []
        for row in known_drugs.get("rows", []):
            target_info = row.get("target") or {}
            disease_info = row.get("disease") or {}

            assoc = DrugTargetAssociation()
            assoc.drug_id = drug_id
            assoc.drug_nome = drug_name
            assoc.target_id = target_info.get("id", "")
            assoc.target_gene = target_info.get("approvedSymbol", "")
            assoc.target_nome = target_info.get("approvedName", "")
            assoc.disease_id = disease_info.get("id", "")
            assoc.disease_nome = disease_info.get("name", "")
            assoc.fase_clinica = row.get("phase") or 0
            assoc.fonte = "open_targets"

            associations.append(assoc)

        logger.info(
            "Open Targets: %d associacoes alvo-droga para %s (%s)",
            len(associations), drug_name, drug_id,
        )
        return associations

    def buscar_gene_por_simbolo(self, gene_symbol: str) -> str:
        """Busca o Ensembl Gene ID a partir do simbolo do gene.

        Args:
            gene_symbol: Simbolo do gene (ex: "MTOR", "SIRT1").

        Returns:
            Ensembl Gene ID (ex: "ENSG00000198793") ou string vazia.
        """
        query = """
        query GeneSearch($queryString: String!) {
          search(queryString: $queryString, entityNames: ["target"], page: {size: 5, index: 0}) {
            hits {
              id
              name
              entity
              ... on Target {
                approvedSymbol
              }
            }
          }
        }
        """
        variables = {"queryString": gene_symbol}
        data = self._query(query, variables)

        if data is None or "data" not in data:
            return ""

        hits = data["data"].get("search", {}).get("hits", [])
        for hit in hits:
            if hit.get("approvedSymbol", "").upper() == gene_symbol.upper():
                return hit.get("id", "")

        # Se nao encontrou match exato, retorna o primeiro hit se existir
        if hits:
            return hits[0].get("id", "")

        return ""


# --- Geroprotetores conhecidos ---

# Lista curada dos principais geroprotetores mencionados na literatura
# Referencia: nosso acervo de 376 papers + revisoes sistematicas
GEROPROTETORES_CONHECIDOS = [
    {"nome": "Rapamycin", "chembl_id": "CHEMBL413", "drugbank_id": "DB00877",
     "mecanismo": "mTOR inhibitor", "fase": 4, "alias": ["sirolimus"]},
    {"nome": "Metformin", "chembl_id": "CHEMBL1431", "drugbank_id": "DB00331",
     "mecanismo": "AMPK activator", "fase": 4, "alias": []},
    {"nome": "Resveratrol", "chembl_id": "CHEMBL71", "drugbank_id": "DB02709",
     "mecanismo": "SIRT1 activator", "fase": 3, "alias": []},
    {"nome": "Quercetin", "chembl_id": "CHEMBL159", "drugbank_id": "DB04216",
     "mecanismo": "Senolytic (PI3K/AKT)", "fase": 2, "alias": []},
    {"nome": "Dasatinib", "chembl_id": "CHEMBL1421", "drugbank_id": "DB01254",
     "mecanismo": "Senolytic (tyrosine kinase inhibitor)", "fase": 4, "alias": []},
    {"nome": "Nicotinamide riboside", "chembl_id": "CHEMBL1232779", "drugbank_id": "DB14226",
     "mecanismo": "NAD+ precursor", "fase": 2, "alias": ["NR"]},
    {"nome": "Nicotinamide mononucleotide", "chembl_id": "CHEMBL1233417", "drugbank_id": "",
     "mecanismo": "NAD+ precursor", "fase": 2, "alias": ["NMN"]},
    {"nome": "Spermidine", "chembl_id": "CHEMBL14240", "drugbank_id": "DB03566",
     "mecanismo": "Autophagy inducer", "fase": 2, "alias": []},
    {"nome": "Senolytics D+Q", "chembl_id": "", "drugbank_id": "",
     "mecanismo": "Senolytic combination (Dasatinib + Quercetin)", "fase": 2, "alias": []},
    {"nome": "Navitoclax", "chembl_id": "CHEMBL1236639", "drugbank_id": "DB12340",
     "mecanismo": "Senolytic (BCL-2 inhibitor)", "fase": 3, "alias": ["ABT-263"]},
    {"nome": "Fisetin", "chembl_id": "CHEMBL159654", "drugbank_id": "DB07795",
     "mecanismo": "Senolytic (PI3K/AKT/mTOR)", "fase": 2, "alias": []},
    {"nome": "Acarbose", "chembl_id": "CHEMBL1566", "drugbank_id": "DB00284",
     "mecanismo": "Alpha-glucosidase inhibitor", "fase": 4, "alias": []},
    {"nome": "17alpha-Estradiol", "chembl_id": "CHEMBL1005469", "drugbank_id": "",
     "mecanismo": "Non-feminizing estrogen", "fase": 0, "alias": []},
]

# Alvos-chave do envelhecimento (genes humanos)
# Identificados a partir do mapa de conceitos da Fase 1
ALVOS_ENVELHECIMENTO = [
    {"gene": "MTOR", "nome": "Mechanistic target of rapamycin", "ensembl": "ENSG00000198793",
     "via": "mTOR/PI3K/AKT", "papers_mencionando": 59},
    {"gene": "SIRT1", "nome": "Sirtuin 1", "ensembl": "ENSG00000096717",
     "via": "Sirtuinas/NAD+", "papers_mencionando": 21},
    {"gene": "SIRT3", "nome": "Sirtuin 3", "ensembl": "ENSG00000071909",
     "via": "Sirtuinas/Mitocondria", "papers_mencionando": 21},
    {"gene": "SIRT6", "nome": "Sirtuin 6", "ensembl": "ENSG00000077463",
     "via": "Sirtuinas/DNA repair", "papers_mencionando": 21},
    {"gene": "FOXO3", "nome": "Forkhead box O3", "ensembl": "ENSG00000118689",
     "via": "FOXO/Insulin signaling", "papers_mencionando": 6},
    {"gene": "AMPK", "nome": "AMP-activated protein kinase", "ensembl": "ENSG00000111725",
     "via": "AMPK/Energy sensing", "papers_mencionando": 15},
    {"gene": "KL", "nome": "Klotho", "ensembl": "ENSG00000133116",
     "via": "Klotho/FGF23", "papers_mencionando": 2},
    {"gene": "TP53", "nome": "Tumor protein p53", "ensembl": "ENSG00000141510",
     "via": "p53/Senescence", "papers_mencionando": 11},
    {"gene": "CDKN2A", "nome": "Cyclin dependent kinase inhibitor 2A (p16)", "ensembl": "ENSG00000147889",
     "via": "p16/Senescence", "papers_mencionando": 11},
    {"gene": "TERT", "nome": "Telomerase reverse transcriptase", "ensembl": "ENSG00000164362",
     "via": "Telomere maintenance", "papers_mencionando": 10},
    {"gene": "NAMPT", "nome": "Nicotinamide phosphoribosyltransferase", "ensembl": "ENSG00000105835",
     "via": "NAD+ biosynthesis", "papers_mencionando": 24},
    {"gene": "ATG5", "nome": "Autophagy related 5", "ensembl": "ENSG00000057663",
     "via": "Autophagy", "papers_mencionando": 34},
    {"gene": "LMNA", "nome": "Lamin A/C", "ensembl": "ENSG00000160789",
     "via": "Nuclear lamina/Progeria", "papers_mencionando": 5},
    {"gene": "GDF11", "nome": "Growth differentiation factor 11", "ensembl": "ENSG00000135414",
     "via": "Rejuvenation/Parabiosis", "papers_mencionando": 5},
    {"gene": "BCL2", "nome": "BCL2 apoptosis regulator", "ensembl": "ENSG00000171791",
     "via": "Apoptosis/Senolytic target", "papers_mencionando": 20},
]
