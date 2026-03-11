"""Testes dos modulos core: integrity, audit e bibliography."""

import json
import tempfile
from pathlib import Path

import pytest

from src.core.integrity import (
    calcular_sha256,
    calcular_sha256_texto,
    info_arquivo,
    verificar_integridade,
)
from src.core.audit import AuditLogger
from src.core.bibliography import GestorBibliografia, Referencia


# === INTEGRITY ===


class TestIntegridade:
    """Testes do modulo de integridade SHA-256."""

    def test_sha256_arquivo_simples(self, tmp_path: Path) -> None:
        arquivo = tmp_path / "teste.txt"
        arquivo.write_text("conteudo de teste", encoding="utf-8")
        hash1 = calcular_sha256(arquivo)
        hash2 = calcular_sha256(arquivo)
        assert hash1 == hash2
        assert len(hash1) == 64  # SHA-256 hex = 64 chars

    def test_sha256_arquivo_diferente(self, tmp_path: Path) -> None:
        arq1 = tmp_path / "a.txt"
        arq2 = tmp_path / "b.txt"
        arq1.write_text("conteudo A", encoding="utf-8")
        arq2.write_text("conteudo B", encoding="utf-8")
        assert calcular_sha256(arq1) != calcular_sha256(arq2)

    def test_sha256_arquivo_inexistente(self) -> None:
        with pytest.raises(FileNotFoundError):
            calcular_sha256("/caminho/inexistente.txt")

    def test_verificar_integridade_ok(self, tmp_path: Path) -> None:
        arquivo = tmp_path / "ok.txt"
        arquivo.write_text("dados intactos", encoding="utf-8")
        hash_original = calcular_sha256(arquivo)
        assert verificar_integridade(arquivo, hash_original) is True

    def test_verificar_integridade_falha(self, tmp_path: Path) -> None:
        arquivo = tmp_path / "alterado.txt"
        arquivo.write_text("dados originais", encoding="utf-8")
        assert verificar_integridade(arquivo, "hash_errado") is False

    def test_sha256_texto(self) -> None:
        hash1 = calcular_sha256_texto("texto teste")
        hash2 = calcular_sha256_texto("texto teste")
        hash3 = calcular_sha256_texto("texto diferente")
        assert hash1 == hash2
        assert hash1 != hash3

    def test_info_arquivo(self, tmp_path: Path) -> None:
        arquivo = tmp_path / "info.txt"
        arquivo.write_text("conteudo", encoding="utf-8")
        info = info_arquivo(arquivo)
        assert info["nome"] == "info.txt"
        assert info["tamanho_bytes"] > 0
        assert len(info["hash_sha256"]) == 64


# === AUDIT ===


class TestAudit:
    """Testes do modulo de auditoria."""

    def test_criar_audit_logger(self, tmp_path: Path) -> None:
        audit = AuditLogger(audit_dir=tmp_path, modulo="teste")
        assert audit.execution_id
        assert audit.modulo == "teste"
        assert audit.status == "EM_EXECUCAO"

    def test_registrar_input(self, tmp_path: Path) -> None:
        arquivo = tmp_path / "input.csv"
        arquivo.write_text("col1,col2\n1,2", encoding="utf-8")
        audit = AuditLogger(audit_dir=tmp_path, modulo="teste")
        audit.registrar_input(arquivo)
        assert len(audit.arquivos_input) == 1
        assert audit.arquivos_input[0]["nome"] == "input.csv"

    def test_finalizar_sucesso(self, tmp_path: Path) -> None:
        audit = AuditLogger(audit_dir=tmp_path, modulo="teste")
        audit.registrar_contagens(lidos=100, validos=95, processados=95, rejeitados=5)
        log_path = audit.finalizar(status="SUCESSO")
        assert log_path.exists()

        with open(log_path, "r", encoding="utf-8") as f:
            registro = json.load(f)
        assert registro["status"] == "SUCESSO"
        assert registro["registros_lidos"] == 100
        assert registro["registros_rejeitados"] == 5

    def test_finalizar_com_anomalias(self, tmp_path: Path) -> None:
        audit = AuditLogger(audit_dir=tmp_path, modulo="teste")
        audit.registrar_anomalia("Valor negativo encontrado")
        log_path = audit.finalizar(status="SUCESSO")

        with open(log_path, "r", encoding="utf-8") as f:
            registro = json.load(f)
        assert registro["status"] == "SUCESSO_COM_ALERTAS"
        assert len(registro["anomalias"]) == 1

    def test_finalizar_falha(self, tmp_path: Path) -> None:
        audit = AuditLogger(audit_dir=tmp_path, modulo="teste")
        log_path = audit.finalizar(status="FALHA", erro="Encoding invalido")

        with open(log_path, "r", encoding="utf-8") as f:
            registro = json.load(f)
        assert registro["status"] == "FALHA"
        assert "Encoding" in registro["erro"]


# === BIBLIOGRAPHY ===


class TestBibliografia:
    """Testes do modulo de gestao bibliografica."""

    def _criar_referencia(self, doi: str = "10.1234/test.001") -> Referencia:
        return Referencia(
            doi=doi,
            titulo="Test Paper on Aging Proteomics",
            autores=["Silva, J.", "Santos, M."],
            ano=2024,
            journal="Nature Aging",
            abstract="This paper studies aging proteomics.",
            licenca="cc-by-4.0",
            fonte="pubmed",
        )

    def test_referencia_open_access(self) -> None:
        ref = self._criar_referencia()
        ref.licenca = "cc-by-4.0"
        assert ref.eh_open_access is True

    def test_referencia_restrita(self) -> None:
        ref = self._criar_referencia()
        ref.licenca = "proprietary"
        assert ref.eh_open_access is False

    def test_bibtex_key(self) -> None:
        ref = self._criar_referencia()
        assert ref.bibtex_key == "Silva_2024"
        assert "2024" in ref.bibtex_key

    def test_to_bibtex(self) -> None:
        ref = self._criar_referencia()
        bib = ref.to_bibtex()
        assert "@article{" in bib
        assert "10.1234/test.001" in bib
        assert "Test Paper" in bib

    def test_gestor_adicionar_referencia(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)
        ref = self._criar_referencia()
        assert gestor.adicionar(ref) is True
        assert gestor.total_referencias() == 1

    def test_gestor_referencia_duplicada(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)
        ref = self._criar_referencia()
        gestor.adicionar(ref)
        assert gestor.adicionar(ref) is False  # Duplicata
        assert gestor.total_referencias() == 1

    def test_gestor_buscar_por_doi(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)
        ref = self._criar_referencia()
        gestor.adicionar(ref)
        entry = gestor.buscar_por_doi("10.1234/test.001")
        assert entry is not None
        assert entry["titulo"] == "Test Paper on Aging Proteomics"

    def test_gestor_registrar_pdf_open_access(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)
        ref = self._criar_referencia()
        ref.licenca = "cc-by-4.0"
        gestor.adicionar(ref)

        pdf = tmp_path / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4 fake content")

        assert gestor.registrar_pdf(ref.doi, pdf) is True

    def test_gestor_bloqueia_pdf_restrito(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)
        ref = self._criar_referencia()
        ref.licenca = "proprietary"
        gestor.adicionar(ref)

        pdf = tmp_path / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4 fake content")

        assert gestor.registrar_pdf(ref.doi, pdf) is False

    def test_gestor_resumo(self, tmp_path: Path) -> None:
        gestor = GestorBibliografia(bibliography_dir=tmp_path)

        ref_oa = self._criar_referencia("10.1234/oa.001")
        ref_oa.licenca = "cc-by-4.0"
        gestor.adicionar(ref_oa)

        ref_restrita = self._criar_referencia("10.1234/restrita.001")
        ref_restrita.licenca = "proprietary"
        gestor.adicionar(ref_restrita)

        resumo = gestor.resumo()
        assert resumo["total_referencias"] == 2
        assert resumo["total_open_access"] == 1
        assert resumo["total_restrito"] == 1

    def test_gestor_persistencia(self, tmp_path: Path) -> None:
        """Testa que dados sobrevivem a recriacao do gestor."""
        gestor1 = GestorBibliografia(bibliography_dir=tmp_path)
        gestor1.adicionar(self._criar_referencia())

        # Recriar o gestor (simula nova sessao)
        gestor2 = GestorBibliografia(bibliography_dir=tmp_path)
        assert gestor2.total_referencias() == 1
