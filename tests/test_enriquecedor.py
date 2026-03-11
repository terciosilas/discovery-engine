"""Testes do modulo de enriquecimento com Semantic Scholar.

Usa mocks para nao depender de APIs externas.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.ingestion.enriquecedor import (
    carregar_papers,
    carregar_checkpoint,
    salvar_checkpoint,
    enriquecer_paper,
    enriquecer_papers_s2,
)
from src.ingestion.semantic_scholar import S2Paper


# === FIXTURES ===


SAMPLE_PAPERS = [
    {
        "pmid": "38000001",
        "doi": "10.1038/s41586-024-00001-1",
        "titulo": "Proteomic signatures of aging",
        "autores": ["Johnson, Alice"],
        "journal": "Nature Aging",
        "ano": 2024,
        "abstract": "We analyzed plasma proteomics data.",
        "keywords": ["proteomics", "aging"],
        "tipo_publicacao": ["journal article"],
        "pmc_id": "PMC1234567",
    },
    {
        "pmid": "38000002",
        "doi": "10.1016/j.cell.2024.00002",
        "titulo": "mTOR inhibition extends lifespan",
        "autores": ["Smith, Bob"],
        "journal": "Cell",
        "ano": 2024,
        "abstract": "Rapamycin extends lifespan in mice.",
        "keywords": ["mTOR", "rapamycin"],
        "tipo_publicacao": ["journal article"],
        "pmc_id": "",
    },
]

SAMPLE_S2_DATA_FOUND = {
    "status": "encontrado",
    "s2_paper_id": "abc123def456",
    "citation_count": 42,
    "influential_citation_count": 8,
    "tldr": "Plasma proteomics reveals aging signatures.",
    "fields_of_study": ["Medicine", "Biology"],
    "reference_count": 55,
    "is_open_access": True,
    "timestamp": "2026-03-10T12:00:00+00:00",
}

SAMPLE_S2_DATA_NOT_FOUND = {
    "status": "nao_encontrado",
    "timestamp": "2026-03-10T12:00:00+00:00",
}


# === CARREGAR PAPERS ===


class TestCarregarPapers:
    """Testes de carga de papers do JSON."""

    def test_carregar_papers_valido(self, tmp_path: Path) -> None:
        json_file = tmp_path / "papers.json"
        json_file.write_text(json.dumps(SAMPLE_PAPERS), encoding="utf-8")

        papers = carregar_papers(json_file)
        assert len(papers) == 2
        assert papers[0]["doi"] == "10.1038/s41586-024-00001-1"

    def test_carregar_papers_arquivo_inexistente(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            carregar_papers(tmp_path / "nao_existe.json")

    def test_carregar_papers_formato_invalido(self, tmp_path: Path) -> None:
        json_file = tmp_path / "papers.json"
        json_file.write_text('{"not": "a list"}', encoding="utf-8")

        with pytest.raises(ValueError, match="esperava lista"):
            carregar_papers(json_file)

    def test_carregar_papers_lista_vazia(self, tmp_path: Path) -> None:
        json_file = tmp_path / "papers.json"
        json_file.write_text("[]", encoding="utf-8")

        papers = carregar_papers(json_file)
        assert papers == []


# === CHECKPOINT ===


class TestCheckpoint:
    """Testes do sistema de checkpoint incremental."""

    def test_checkpoint_salvar_e_carregar(self, tmp_path: Path) -> None:
        ckpt_path = tmp_path / "checkpoint.json"
        resultados = {
            "10.1038/test1": SAMPLE_S2_DATA_FOUND,
            "10.1016/test2": SAMPLE_S2_DATA_NOT_FOUND,
        }

        salvar_checkpoint(ckpt_path, resultados, "papers.json", "2026-03-10T00:00:00")
        loaded = carregar_checkpoint(ckpt_path)

        assert len(loaded) == 2
        assert loaded["10.1038/test1"]["status"] == "encontrado"
        assert loaded["10.1038/test1"]["citation_count"] == 42
        assert loaded["10.1016/test2"]["status"] == "nao_encontrado"

    def test_checkpoint_inexistente(self, tmp_path: Path) -> None:
        loaded = carregar_checkpoint(tmp_path / "nao_existe.json")
        assert loaded == {}

    def test_checkpoint_corrompido(self, tmp_path: Path) -> None:
        ckpt_path = tmp_path / "corrupted.json"
        ckpt_path.write_text("not valid json{{{", encoding="utf-8")

        loaded = carregar_checkpoint(ckpt_path)
        assert loaded == {}

    def test_checkpoint_cria_diretorio(self, tmp_path: Path) -> None:
        ckpt_path = tmp_path / "sub" / "dir" / "checkpoint.json"
        salvar_checkpoint(ckpt_path, {}, "papers.json", "2026-03-10T00:00:00")
        assert ckpt_path.exists()


# === ENRIQUECER PAPER ===


class TestEnriquecerPaper:
    """Testes da funcao de merge de dados S2."""

    def test_paper_encontrado(self) -> None:
        original = SAMPLE_PAPERS[0].copy()
        enriched = enriquecer_paper(original, SAMPLE_S2_DATA_FOUND)

        assert enriched["s2_enriquecido"] is True
        assert enriched["citation_count"] == 42
        assert enriched["influential_citation_count"] == 8
        assert enriched["tldr"] == "Plasma proteomics reveals aging signatures."
        assert "Medicine" in enriched["fields_of_study"]
        assert enriched["s2_paper_id"] == "abc123def456"

    def test_paper_nao_encontrado(self) -> None:
        original = SAMPLE_PAPERS[0].copy()
        enriched = enriquecer_paper(original, SAMPLE_S2_DATA_NOT_FOUND)

        assert enriched["s2_enriquecido"] is False
        assert enriched["s2_status"] == "nao_encontrado"
        assert enriched["citation_count"] == 0
        assert enriched["tldr"] == ""

    def test_nao_modifica_original(self) -> None:
        original = SAMPLE_PAPERS[0].copy()
        original_copy = original.copy()

        enriquecer_paper(original, SAMPLE_S2_DATA_FOUND)

        # Original deve estar intacto
        assert original == original_copy
        assert "citation_count" not in original

    def test_preserva_campos_originais(self) -> None:
        original = SAMPLE_PAPERS[0].copy()
        enriched = enriquecer_paper(original, SAMPLE_S2_DATA_FOUND)

        # Campos PubMed preservados
        assert enriched["pmid"] == "38000001"
        assert enriched["doi"] == "10.1038/s41586-024-00001-1"
        assert enriched["titulo"] == "Proteomic signatures of aging"
        assert enriched["journal"] == "Nature Aging"


# === ENRIQUECER PAPERS S2 (FLUXO COMPLETO) ===


class TestEnriquecerPapersS2:
    """Testes do fluxo completo de enriquecimento."""

    def _create_input_file(self, tmp_path: Path) -> Path:
        """Cria arquivo de input para testes."""
        json_file = tmp_path / "papers_fase1_test.json"
        json_file.write_text(json.dumps(SAMPLE_PAPERS), encoding="utf-8")
        return json_file

    @patch("src.ingestion.enriquecedor.SemanticScholarClient")
    @patch("src.ingestion.enriquecedor.AuditLogger")
    @patch("src.ingestion.enriquecedor.DATA_DIR")
    @patch("src.ingestion.enriquecedor.CHECKPOINT_DIR")
    def test_fluxo_completo(
        self,
        mock_ckpt_dir: MagicMock,
        mock_data_dir: MagicMock,
        mock_audit_class: MagicMock,
        mock_s2_class: MagicMock,
        tmp_path: Path,
    ) -> None:
        # Setup dirs
        mock_data_dir.__truediv__ = lambda self, x: tmp_path / x
        mock_ckpt_dir.__truediv__ = lambda self, x: tmp_path / "checkpoints" / x
        (tmp_path / "processed").mkdir()
        (tmp_path / "checkpoints").mkdir()

        # Setup S2 mock
        mock_s2 = MagicMock()
        mock_s2_class.return_value = mock_s2

        s2_paper = S2Paper(
            paper_id="abc123",
            doi="10.1038/s41586-024-00001-1",
            titulo="Proteomic signatures",
            citation_count=42,
            influential_citation_count=8,
            tldr="Test TLDR",
            fields_of_study=["Medicine"],
            reference_count=55,
            is_open_access=True,
        )
        # Primeiro paper encontrado, segundo nao
        mock_s2.get_paper_by_doi.side_effect = [s2_paper, None]
        mock_s2.get_paper.return_value = None  # Fallback PMID tambem nao encontra

        # Setup audit mock
        mock_audit = MagicMock()
        mock_audit_class.return_value = mock_audit

        # Criar input
        input_file = self._create_input_file(tmp_path)

        # Executar
        resultado = enriquecer_papers_s2(input_file)

        # Verificacoes
        assert resultado["total_papers"] == 2
        assert resultado["encontrados_s2"] == 1
        assert resultado["nao_encontrados_s2"] == 1
        assert resultado["taxa_cobertura_s2"] == 50.0

        # Verificar que audit foi chamado
        mock_audit.registrar_input.assert_called_once()
        mock_audit.finalizar.assert_called_once()

    @patch("src.ingestion.enriquecedor.SemanticScholarClient")
    @patch("src.ingestion.enriquecedor.AuditLogger")
    @patch("src.ingestion.enriquecedor.DATA_DIR")
    @patch("src.ingestion.enriquecedor.CHECKPOINT_DIR")
    def test_retomada_checkpoint(
        self,
        mock_ckpt_dir: MagicMock,
        mock_data_dir: MagicMock,
        mock_audit_class: MagicMock,
        mock_s2_class: MagicMock,
        tmp_path: Path,
    ) -> None:
        # Setup dirs
        mock_data_dir.__truediv__ = lambda self, x: tmp_path / x
        mock_ckpt_dir.__truediv__ = lambda self, x: tmp_path / "checkpoints" / x
        (tmp_path / "processed").mkdir()
        ckpt_dir = tmp_path / "checkpoints"
        ckpt_dir.mkdir()

        # Criar checkpoint pre-existente (primeiro paper ja processado)
        ckpt_data = {
            "versao": 1,
            "timestamp_inicio": "2026-03-10T00:00:00",
            "input_file": "papers_fase1_test.json",
            "total_processados": 1,
            "resultados": {
                "10.1038/s41586-024-00001-1": SAMPLE_S2_DATA_FOUND,
            },
        }
        ckpt_path = ckpt_dir / "ckpt_enrich_papers_fase1_test.json"
        ckpt_path.write_text(json.dumps(ckpt_data), encoding="utf-8")

        # S2 mock - so deve ser chamado 1x (segundo paper)
        mock_s2 = MagicMock()
        mock_s2_class.return_value = mock_s2
        mock_s2.get_paper_by_doi.return_value = None
        mock_s2.get_paper.return_value = None

        # Audit mock
        mock_audit = MagicMock()
        mock_audit_class.return_value = mock_audit

        input_file = self._create_input_file(tmp_path)
        resultado = enriquecer_papers_s2(input_file)

        # Segundo paper nao encontrado
        assert resultado["encontrados_s2"] == 1
        assert resultado["nao_encontrados_s2"] == 1
        # S2 so chamado 1x (segundo paper), nao 2x
        assert mock_s2.get_paper_by_doi.call_count == 1
