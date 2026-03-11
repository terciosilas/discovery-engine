"""Testes dos modulos ChEMBL e DrugBank.

Usa mocks para nao depender de APIs externas.
"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.ingestion.chembl import (
    ChEMBLActivity,
    ChEMBLClient,
    ChEMBLCompound,
    ChEMBLTarget,
)
from src.ingestion.drugbank import (
    Drug,
    DrugBankVocabulary,
    DrugTargetAssociation,
    OpenTargetsClient,
    GEROPROTETORES_CONHECIDOS,
    ALVOS_ENVELHECIMENTO,
)


# === ChEMBL ===


CHEMBL_COMPOUND_RESPONSE = {
    "molecule_chembl_id": "CHEMBL413",
    "pref_name": "SIROLIMUS",
    "max_phase": 4,
    "molecule_type": "Natural Product",
    "molecule_properties": {
        "full_molformula": "C51H79NO13",
        "full_mwt": "914.19",
    },
    "molecule_structures": {},
}

CHEMBL_TARGET_RESPONSE = {
    "target_chembl_id": "CHEMBL2842",
    "pref_name": "Serine/threonine-protein kinase mTOR",
    "target_type": "SINGLE PROTEIN",
    "organism": "Homo sapiens",
    "target_components": [
        {
            "accession": "P42345",
            "target_component_synonyms": [
                {"syn_type": "GENE_SYMBOL", "component_synonym": "MTOR"},
            ],
        }
    ],
}

CHEMBL_ACTIVITY_RESPONSE = {
    "activities": [
        {
            "activity_id": 12345,
            "molecule_chembl_id": "CHEMBL413",
            "molecule_pref_name": "SIROLIMUS",
            "target_chembl_id": "CHEMBL2842",
            "target_pref_name": "mTOR",
            "target_organism": "Homo sapiens",
            "standard_type": "IC50",
            "standard_value": "0.1",
            "standard_units": "nM",
            "standard_relation": "=",
            "pchembl_value": "10.0",
            "assay_type": "B",
            "document_chembl_id": "CHEMBL_DOC_001",
        }
    ]
}


class TestChEMBLClient:
    """Testes do cliente ChEMBL."""

    def test_compound_to_dict(self) -> None:
        comp = ChEMBLCompound(
            chembl_id="CHEMBL413",
            nome="Rapamycin",
            max_phase=4,
        )
        d = comp.to_dict()
        assert d["chembl_id"] == "CHEMBL413"
        assert d["max_phase"] == 4

    def test_target_to_dict(self) -> None:
        target = ChEMBLTarget(
            chembl_id="CHEMBL2842",
            nome="mTOR",
            gene_names=["MTOR"],
            uniprot_ids=["P42345"],
        )
        d = target.to_dict()
        assert d["chembl_id"] == "CHEMBL2842"
        assert "MTOR" in d["gene_names"]

    def test_activity_to_dict(self) -> None:
        act = ChEMBLActivity(
            compound_chembl_id="CHEMBL413",
            target_chembl_id="CHEMBL2842",
            tipo_atividade="IC50",
            valor=0.1,
            pchembl_value=10.0,
        )
        d = act.to_dict()
        assert d["tipo_atividade"] == "IC50"
        assert d["pchembl_value"] == 10.0

    @patch("src.ingestion.chembl.requests.Session")
    def test_buscar_composto(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = CHEMBL_COMPOUND_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = ChEMBLClient()
        client.session = mock_session
        comp = client.buscar_composto("CHEMBL413")

        assert comp is not None
        assert comp.chembl_id == "CHEMBL413"
        assert comp.nome_preferido == "SIROLIMUS"
        assert comp.max_phase == 4
        assert comp.formula == "C51H79NO13"

    @patch("src.ingestion.chembl.requests.Session")
    def test_buscar_alvo(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = CHEMBL_TARGET_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = ChEMBLClient()
        client.session = mock_session
        target = client.buscar_alvo("CHEMBL2842")

        assert target is not None
        assert target.chembl_id == "CHEMBL2842"
        assert target.organismo == "Homo sapiens"
        assert "MTOR" in target.gene_names
        assert "P42345" in target.uniprot_ids

    @patch("src.ingestion.chembl.requests.Session")
    def test_buscar_atividades(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = CHEMBL_ACTIVITY_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = ChEMBLClient()
        client.session = mock_session
        acts = client.buscar_atividades_por_alvo("CHEMBL2842")

        assert len(acts) == 1
        act = acts[0]
        assert act.compound_chembl_id == "CHEMBL413"
        assert act.tipo_atividade == "IC50"
        assert act.valor == 0.1
        assert act.pchembl_value == 10.0
        assert act.assay_type == "B"

    @patch("src.ingestion.chembl.requests.Session")
    def test_composto_nao_encontrado(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = ChEMBLClient()
        client.session = mock_session
        comp = client.buscar_composto("CHEMBL9999999")

        assert comp is None

    def test_parse_compound_none(self) -> None:
        assert ChEMBLClient._parse_compound(None) is None

    def test_parse_target_none(self) -> None:
        assert ChEMBLClient._parse_target(None) is None

    def test_parse_activity_none(self) -> None:
        assert ChEMBLClient._parse_activity(None) is None


# === DrugBank Vocabulary ===


DRUGBANK_CSV_CONTENT = """\
DrugBank ID,Accession Numbers,Common name,CAS Number,UNII,Type
DB00877,"DB00877",Sirolimus,53123-88-9,W36ZG6FT64,Small Molecule
DB00331,"DB00331",Metformin,657-24-9,9100L32L2N,Small Molecule
DB02709,"DB02709",Resveratrol,501-36-0,Q369O8926L,Small Molecule
"""


class TestDrugBankVocabulary:
    """Testes do carregador de vocabulario DrugBank."""

    def test_carregar_csv(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "drugbank_vocabulary.csv"
        csv_file.write_text(DRUGBANK_CSV_CONTENT, encoding="utf-8")

        vocab = DrugBankVocabulary(vocab_path=csv_file)
        total = vocab.carregar()

        assert total == 3

    def test_buscar_por_id(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "drugbank_vocabulary.csv"
        csv_file.write_text(DRUGBANK_CSV_CONTENT, encoding="utf-8")

        vocab = DrugBankVocabulary(vocab_path=csv_file)
        vocab.carregar()

        drug = vocab.buscar_por_id("DB00877")
        assert drug is not None
        assert drug.nome == "Sirolimus"
        assert drug.cas_number == "53123-88-9"

    def test_buscar_por_nome(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "drugbank_vocabulary.csv"
        csv_file.write_text(DRUGBANK_CSV_CONTENT, encoding="utf-8")

        vocab = DrugBankVocabulary(vocab_path=csv_file)
        vocab.carregar()

        drug = vocab.buscar_por_nome("metformin")
        assert drug is not None
        assert drug.drugbank_id == "DB00331"

    def test_buscar_inexistente(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "drugbank_vocabulary.csv"
        csv_file.write_text(DRUGBANK_CSV_CONTENT, encoding="utf-8")

        vocab = DrugBankVocabulary(vocab_path=csv_file)
        vocab.carregar()

        assert vocab.buscar_por_id("DB99999") is None
        assert vocab.buscar_por_nome("xyznotadrug") is None

    def test_arquivo_inexistente(self) -> None:
        vocab = DrugBankVocabulary(vocab_path=Path("/nao/existe.csv"))
        with pytest.raises(FileNotFoundError):
            vocab.carregar()

    def test_drug_to_dict(self) -> None:
        drug = Drug(drugbank_id="DB00877", nome="Sirolimus", tipo="Small Molecule")
        d = drug.to_dict()
        assert d["drugbank_id"] == "DB00877"
        assert d["nome"] == "Sirolimus"


# === Open Targets ===


OPEN_TARGETS_RESPONSE = {
    "data": {
        "target": {
            "id": "ENSG00000198793",
            "approvedSymbol": "MTOR",
            "approvedName": "mechanistic target of rapamycin kinase",
            "knownDrugs": {
                "uniqueDrugs": 5,
                "uniqueTargets": 1,
                "count": 2,
                "rows": [
                    {
                        "drug": {
                            "id": "CHEMBL413",
                            "name": "SIROLIMUS",
                            "maximumClinicalTrialPhase": 4,
                            "mechanismsOfAction": {
                                "rows": [
                                    {
                                        "mechanismOfAction": "mTOR inhibitor",
                                        "actionType": "INHIBITOR",
                                    }
                                ]
                            },
                        },
                        "disease": {
                            "id": "EFO_0000222",
                            "name": "kidney transplant rejection",
                        },
                        "phase": 4,
                        "ctIds": ["NCT00000001"],
                    }
                ],
            },
        }
    }
}


class TestOpenTargetsClient:
    """Testes do cliente Open Targets."""

    def test_drug_target_association_to_dict(self) -> None:
        assoc = DrugTargetAssociation(
            drug_id="CHEMBL413",
            drug_nome="Sirolimus",
            target_gene="MTOR",
        )
        d = assoc.to_dict()
        assert d["drug_id"] == "CHEMBL413"
        assert d["target_gene"] == "MTOR"

    @patch("src.ingestion.drugbank.requests.Session")
    def test_buscar_drogas_por_alvo(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = OPEN_TARGETS_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.post.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = OpenTargetsClient()
        client.session = mock_session
        assocs = client.buscar_drogas_por_alvo("ENSG00000198793")

        assert len(assocs) == 1
        assoc = assocs[0]
        assert assoc.drug_id == "CHEMBL413"
        assert assoc.drug_nome == "SIROLIMUS"
        assert assoc.target_gene == "MTOR"
        assert assoc.fase_clinica == 4
        assert assoc.mecanismo_acao == "mTOR inhibitor"
        assert assoc.tipo_acao == "INHIBITOR"

    @patch("src.ingestion.drugbank.requests.Session")
    def test_alvo_nao_encontrado(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": {"target": None}}
        mock_response.raise_for_status = MagicMock()
        mock_session.post.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = OpenTargetsClient()
        client.session = mock_session
        assocs = client.buscar_drogas_por_alvo("ENSG_FAKE")

        assert assocs == []


# === DADOS CURADOS ===


class TestDadosCurados:
    """Testes das listas curadas de geroprotetores e alvos."""

    def test_geroprotetores_tem_campos_obrigatorios(self) -> None:
        for gp in GEROPROTETORES_CONHECIDOS:
            assert "nome" in gp
            assert "mecanismo" in gp
            assert "fase" in gp
            assert isinstance(gp["fase"], int)

    def test_alvos_tem_campos_obrigatorios(self) -> None:
        for alvo in ALVOS_ENVELHECIMENTO:
            assert "gene" in alvo
            assert "nome" in alvo
            assert "ensembl" in alvo
            assert alvo["ensembl"].startswith("ENSG")

    def test_rapamycin_presente(self) -> None:
        nomes = [g["nome"] for g in GEROPROTETORES_CONHECIDOS]
        assert "Rapamycin" in nomes

    def test_mtor_presente(self) -> None:
        genes = [a["gene"] for a in ALVOS_ENVELHECIMENTO]
        assert "MTOR" in genes
