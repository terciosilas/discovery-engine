"""Cliente da API ChEMBL.

Busca atividade biologica droga-alvo na base ChEMBL (EBI).
API publica REST, sem necessidade de registro ou API key.
Documentacao: https://www.ebi.ac.uk/chembl/api/data/docs
"""

import logging
import time
from dataclasses import dataclass, field
from typing import Any

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

# Rate limit conservador: 0.5s entre requests
MIN_INTERVAL_S = 0.5


@dataclass
class ChEMBLCompound:
    """Representa um composto/molecula do ChEMBL."""

    chembl_id: str = ""
    nome: str = ""
    nome_preferido: str = ""
    max_phase: int = 0  # 0=preclinico, 1-3=fase clinica, 4=aprovado
    tipo_molecula: str = ""
    formula: str = ""
    peso_molecular: float = 0.0
    is_oral: bool = False
    descricao: str = ""
    indicacoes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "chembl_id": self.chembl_id,
            "nome": self.nome,
            "nome_preferido": self.nome_preferido,
            "max_phase": self.max_phase,
            "tipo_molecula": self.tipo_molecula,
            "formula": self.formula,
            "peso_molecular": self.peso_molecular,
            "is_oral": self.is_oral,
            "descricao": self.descricao,
            "indicacoes": self.indicacoes,
        }


@dataclass
class ChEMBLTarget:
    """Representa um alvo biologico (proteina/gene) no ChEMBL."""

    chembl_id: str = ""
    nome: str = ""
    tipo: str = ""  # SINGLE PROTEIN, PROTEIN COMPLEX, etc.
    organismo: str = ""
    gene_names: list[str] = field(default_factory=list)
    uniprot_ids: list[str] = field(default_factory=list)
    descricao: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "chembl_id": self.chembl_id,
            "nome": self.nome,
            "tipo": self.tipo,
            "organismo": self.organismo,
            "gene_names": self.gene_names,
            "uniprot_ids": self.uniprot_ids,
            "descricao": self.descricao,
        }


@dataclass
class ChEMBLActivity:
    """Representa uma atividade biologica (interacao droga-alvo)."""

    activity_id: int = 0
    compound_chembl_id: str = ""
    compound_nome: str = ""
    target_chembl_id: str = ""
    target_nome: str = ""
    target_organismo: str = ""
    tipo_atividade: str = ""  # IC50, Ki, Kd, EC50, etc.
    valor: float = 0.0
    unidade: str = ""  # nM, uM, etc.
    relacao: str = ""  # =, <, >, etc.
    pchembl_value: float = 0.0  # -log(molar) padronizado
    assay_type: str = ""  # B=Binding, F=Functional, A=ADMET
    doi: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "activity_id": self.activity_id,
            "compound_chembl_id": self.compound_chembl_id,
            "compound_nome": self.compound_nome,
            "target_chembl_id": self.target_chembl_id,
            "target_nome": self.target_nome,
            "target_organismo": self.target_organismo,
            "tipo_atividade": self.tipo_atividade,
            "valor": self.valor,
            "unidade": self.unidade,
            "relacao": self.relacao,
            "pchembl_value": self.pchembl_value,
            "assay_type": self.assay_type,
            "doi": self.doi,
        }


class ChEMBLClient:
    """Cliente para a API REST do ChEMBL.

    Fornece acesso a dados de atividade biologica, compostos e alvos.
    Fundamental para o cruzamento proteina-droga na Fase 2.
    """

    def __init__(self) -> None:
        """Inicializa o cliente ChEMBL."""
        self.session = requests.Session()
        self.session.headers["Accept"] = "application/json"
        self._last_request_time: float = 0.0

    def _rate_limit(self) -> None:
        """Aguarda tempo minimo entre requisicoes."""
        elapsed = time.time() - self._last_request_time
        if elapsed < MIN_INTERVAL_S:
            time.sleep(MIN_INTERVAL_S - elapsed)
        self._last_request_time = time.time()

    def _get(self, endpoint: str, params: dict | None = None) -> dict | None:
        """Faz requisicao GET com rate limiting e tratamento de erros.

        Args:
            endpoint: Endpoint relativo (ex: /molecule/CHEMBL25).
            params: Query parameters.

        Returns:
            JSON parseado ou None em caso de erro.
        """
        self._rate_limit()
        url = f"{BASE_URL}{endpoint}"

        try:
            response = self.session.get(url, params=params, timeout=30)
            if response.status_code == 404:
                return None
            if response.status_code == 429:
                logger.warning("ChEMBL rate limit. Aguardando 5s...")
                time.sleep(5)
                return self._get(endpoint, params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error("Erro ChEMBL API: %s | Endpoint: %s", e, endpoint)
            return None

    # --- Compostos ---

    def buscar_composto(self, chembl_id: str) -> ChEMBLCompound | None:
        """Busca um composto pelo ChEMBL ID.

        Args:
            chembl_id: Ex: "CHEMBL25" (aspirina).

        Returns:
            ChEMBLCompound ou None.
        """
        data = self._get(f"/molecule/{chembl_id}.json")
        if data is None:
            return None
        return self._parse_compound(data)

    def buscar_composto_por_nome(self, nome: str, max_results: int = 20) -> list[ChEMBLCompound]:
        """Busca compostos por nome.

        Args:
            nome: Nome do composto (ex: "rapamycin", "metformin").
            max_results: Maximo de resultados.

        Returns:
            Lista de ChEMBLCompound.
        """
        data = self._get("/molecule/search.json", params={
            "q": nome,
            "limit": str(max_results),
        })
        if data is None:
            return []

        compounds = []
        for item in data.get("molecules", []):
            comp = self._parse_compound(item)
            if comp:
                compounds.append(comp)

        logger.info("ChEMBL busca composto '%s': %d resultados", nome, len(compounds))
        return compounds

    # --- Alvos (proteinas) ---

    def buscar_alvo(self, chembl_id: str) -> ChEMBLTarget | None:
        """Busca um alvo pelo ChEMBL ID.

        Args:
            chembl_id: Ex: "CHEMBL2842" (mTOR).

        Returns:
            ChEMBLTarget ou None.
        """
        data = self._get(f"/target/{chembl_id}.json")
        if data is None:
            return None
        return self._parse_target(data)

    def buscar_alvo_por_gene(self, gene_name: str, organismo: str = "Homo sapiens") -> list[ChEMBLTarget]:
        """Busca alvos por nome do gene.

        Args:
            gene_name: Nome do gene (ex: "MTOR", "SIRT1").
            organismo: Filtro de organismo.

        Returns:
            Lista de ChEMBLTarget.
        """
        params: dict[str, str] = {
            "target_synonym__icontains": gene_name,
            "limit": "20",
        }
        if organismo:
            params["target_organism"] = organismo

        data = self._get("/target.json", params=params)
        if data is None:
            return []

        targets = []
        for item in data.get("targets", []):
            target = self._parse_target(item)
            if target:
                targets.append(target)

        logger.info("ChEMBL busca alvo '%s': %d resultados", gene_name, len(targets))
        return targets

    def buscar_alvo_por_uniprot(self, uniprot_id: str) -> ChEMBLTarget | None:
        """Busca alvo por UniProt ID.

        Args:
            uniprot_id: Ex: "P42345" (mTOR humano).

        Returns:
            ChEMBLTarget ou None.
        """
        data = self._get(f"/target.json", params={
            "target_components__accession": uniprot_id,
            "limit": "1",
        })
        if data is None:
            return None

        targets = data.get("targets", [])
        if not targets:
            return None

        return self._parse_target(targets[0])

    # --- Atividades (droga-alvo) ---

    def buscar_atividades_por_alvo(
        self,
        target_chembl_id: str,
        tipo_atividade: str = "",
        pchembl_min: float = 0.0,
        max_results: int = 100,
    ) -> list[ChEMBLActivity]:
        """Busca atividades biologicas para um alvo.

        Args:
            target_chembl_id: ChEMBL ID do alvo.
            tipo_atividade: Filtro (ex: "IC50", "Ki").
            pchembl_min: Filtro de potencia minima (6.0 = 1uM, 7.0 = 100nM).
            max_results: Maximo de resultados.

        Returns:
            Lista de ChEMBLActivity.
        """
        params: dict[str, str] = {
            "target_chembl_id": target_chembl_id,
            "limit": str(min(max_results, 1000)),
        }
        if tipo_atividade:
            params["standard_type"] = tipo_atividade
        if pchembl_min > 0:
            params["pchembl_value__gte"] = str(pchembl_min)

        activities: list[ChEMBLActivity] = []
        offset = 0

        while offset < max_results:
            params["offset"] = str(offset)
            data = self._get("/activity.json", params=params)
            if data is None:
                break

            batch = data.get("activities", [])
            if not batch:
                break

            for item in batch:
                act = self._parse_activity(item)
                if act:
                    activities.append(act)

            offset += len(batch)
            if len(batch) < int(params["limit"]):
                break

        logger.info(
            "ChEMBL atividades para %s: %d resultados",
            target_chembl_id, len(activities),
        )
        return activities

    def buscar_atividades_por_composto(
        self,
        compound_chembl_id: str,
        max_results: int = 100,
    ) -> list[ChEMBLActivity]:
        """Busca atividades biologicas de um composto.

        Args:
            compound_chembl_id: ChEMBL ID do composto.
            max_results: Maximo de resultados.

        Returns:
            Lista de ChEMBLActivity.
        """
        params = {
            "molecule_chembl_id": compound_chembl_id,
            "limit": str(min(max_results, 1000)),
        }
        data = self._get("/activity.json", params=params)
        if data is None:
            return []

        activities = []
        for item in data.get("activities", []):
            act = self._parse_activity(item)
            if act:
                activities.append(act)

        logger.info(
            "ChEMBL atividades para %s: %d resultados",
            compound_chembl_id, len(activities),
        )
        return activities

    # --- Drogas aprovadas ---

    def listar_drogas_aprovadas(self, max_results: int = 500) -> list[ChEMBLCompound]:
        """Lista drogas com max_phase >= 4 (aprovadas).

        Args:
            max_results: Maximo de resultados.

        Returns:
            Lista de ChEMBLCompound aprovados.
        """
        compounds: list[ChEMBLCompound] = []
        offset = 0
        limit = min(max_results, 1000)

        while offset < max_results:
            data = self._get("/molecule.json", params={
                "max_phase": "4",
                "limit": str(min(limit, max_results - offset)),
                "offset": str(offset),
            })
            if data is None:
                break

            batch = data.get("molecules", [])
            if not batch:
                break

            for item in batch:
                comp = self._parse_compound(item)
                if comp:
                    compounds.append(comp)

            offset += len(batch)
            if len(batch) < limit:
                break

        logger.info("ChEMBL drogas aprovadas: %d listadas", len(compounds))
        return compounds

    # --- Parsers ---

    @staticmethod
    def _parse_compound(data: dict) -> ChEMBLCompound | None:
        """Parseia dados de um composto."""
        if data is None:
            return None

        comp = ChEMBLCompound()
        comp.chembl_id = data.get("molecule_chembl_id", "")
        comp.nome_preferido = data.get("pref_name", "") or ""
        comp.max_phase = data.get("max_phase") or 0
        comp.tipo_molecula = data.get("molecule_type", "") or ""

        # Propriedades moleculares
        props = data.get("molecule_properties") or {}
        comp.formula = props.get("full_molformula", "") or ""
        comp.peso_molecular = float(props.get("full_mwt") or 0)

        # Sinonimos / nome
        structs = data.get("molecule_structures") or {}
        comp.nome = comp.nome_preferido or comp.chembl_id

        return comp

    @staticmethod
    def _parse_target(data: dict) -> ChEMBLTarget | None:
        """Parseia dados de um alvo."""
        if data is None:
            return None

        target = ChEMBLTarget()
        target.chembl_id = data.get("target_chembl_id", "")
        target.nome = data.get("pref_name", "") or ""
        target.tipo = data.get("target_type", "") or ""
        target.organismo = data.get("organism", "") or ""

        # Componentes (genes e UniProt)
        for comp in data.get("target_components", []):
            accession = comp.get("accession", "")
            if accession:
                target.uniprot_ids.append(accession)

            for syn in comp.get("target_component_synonyms", []):
                if syn.get("syn_type") == "GENE_SYMBOL":
                    gene = syn.get("component_synonym", "")
                    if gene and gene not in target.gene_names:
                        target.gene_names.append(gene)

        return target

    @staticmethod
    def _parse_activity(data: dict) -> ChEMBLActivity | None:
        """Parseia dados de atividade biologica."""
        if data is None:
            return None

        act = ChEMBLActivity()
        act.activity_id = data.get("activity_id") or 0
        act.compound_chembl_id = data.get("molecule_chembl_id", "") or ""
        act.compound_nome = data.get("molecule_pref_name", "") or ""
        act.target_chembl_id = data.get("target_chembl_id", "") or ""
        act.target_nome = data.get("target_pref_name", "") or ""
        act.target_organismo = data.get("target_organism", "") or ""
        act.tipo_atividade = data.get("standard_type", "") or ""
        act.relacao = data.get("standard_relation", "") or ""
        act.unidade = data.get("standard_units", "") or ""
        act.assay_type = data.get("assay_type", "") or ""
        act.doi = data.get("document_chembl_id", "") or ""

        # Valores numericos
        try:
            act.valor = float(data.get("standard_value") or 0)
        except (ValueError, TypeError):
            act.valor = 0.0
        try:
            act.pchembl_value = float(data.get("pchembl_value") or 0)
        except (ValueError, TypeError):
            act.pchembl_value = 0.0

        return act
