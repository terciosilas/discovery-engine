"""Modulo de gestao bibliografica.

Gerencia referencias em formato BibTeX, verifica licencas via Unpaywall,
registra DOIs e hashes SHA-256 de papers armazenados.
"""

import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.core.integrity import calcular_sha256

logger = logging.getLogger(__name__)

# Caminhos padrao
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BIBLIOGRAPHY_DIR = BASE_DIR / "bibliography"
REFERENCES_BIB = BIBLIOGRAPHY_DIR / "references.bib"
LICENSE_REGISTRY = BIBLIOGRAPHY_DIR / "license_registry.json"

# Licencas que permitem armazenamento de PDF completo
LICENCAS_OPEN_ACCESS = frozenset({
    "cc-by",
    "cc-by-sa",
    "cc-by-nc",
    "cc-by-nc-sa",
    "cc0",
    "cc-by-4.0",
    "cc-by-sa-4.0",
    "cc-by-nc-4.0",
    "cc-by-nc-sa-4.0",
    "public-domain",
    "pd",
})


class Referencia:
    """Representa uma referencia bibliografica com metadados e licenca."""

    def __init__(
        self,
        doi: str,
        titulo: str,
        autores: list[str],
        ano: int,
        journal: str = "",
        abstract: str = "",
        licenca: str = "",
        url_pdf: str = "",
        pmid: str = "",
        fonte: str = "",
    ) -> None:
        self.doi = doi.strip().lower() if doi else ""
        self.titulo = titulo.strip()
        self.autores = autores
        self.ano = ano
        self.journal = journal.strip()
        self.abstract = abstract.strip()
        self.licenca = licenca.strip().lower()
        self.url_pdf = url_pdf.strip()
        self.pmid = pmid.strip()
        self.fonte = fonte  # pubmed, semantic_scholar, manual
        self.data_registro = datetime.now(timezone.utc).isoformat()
        self.hash_pdf: str | None = None
        self.caminho_pdf: str | None = None

    @property
    def eh_open_access(self) -> bool:
        """Verifica se a licenca permite armazenamento do PDF."""
        return self.licenca in LICENCAS_OPEN_ACCESS

    @property
    def bibtex_key(self) -> str:
        """Gera chave BibTeX no formato PrimeiroAutor_Ano."""
        if self.autores:
            primeiro_autor = self.autores[0]
            # Formato "Sobrenome, Iniciais" -> pega antes da virgula
            if "," in primeiro_autor:
                sobrenome = primeiro_autor.split(",")[0].strip()
            else:
                # Formato "Iniciais Sobrenome" -> pega ultimo token
                sobrenome = primeiro_autor.split()[-1]
            sobrenome = re.sub(r"[^a-zA-Z]", "", sobrenome)
        else:
            sobrenome = "Unknown"
        return f"{sobrenome}_{self.ano}"

    def to_bibtex(self) -> str:
        """Converte para formato BibTeX.

        Returns:
            String no formato BibTeX.
        """
        author_str = " and ".join(self.autores)
        lines = [
            f"@article{{{self.bibtex_key},",
            f"  title = {{{self.titulo}}},",
            f"  author = {{{author_str}}},",
            f"  year = {{{self.ano}}},",
        ]
        if self.journal:
            lines.append(f"  journal = {{{self.journal}}},")
        if self.doi:
            lines.append(f"  doi = {{{self.doi}}},")
        if self.pmid:
            lines.append(f"  pmid = {{{self.pmid}}},")
        if self.abstract:
            abstract_limpo = self.abstract.replace("{", "").replace("}", "")
            lines.append(f"  abstract = {{{abstract_limpo}}},")
        lines.append("}")
        return "\n".join(lines)

    def to_registry_entry(self) -> dict[str, Any]:
        """Converte para entrada no license_registry.json."""
        return {
            "doi": self.doi,
            "titulo": self.titulo,
            "autores": self.autores,
            "ano": self.ano,
            "journal": self.journal,
            "licenca": self.licenca,
            "eh_open_access": self.eh_open_access,
            "pmid": self.pmid,
            "fonte": self.fonte,
            "url_pdf": self.url_pdf,
            "hash_pdf": self.hash_pdf,
            "caminho_pdf": self.caminho_pdf,
            "data_registro": self.data_registro,
        }


class GestorBibliografia:
    """Gerencia o acervo bibliografico do projeto.

    Responsabilidades:
    - Adicionar/buscar referencias
    - Manter references.bib atualizado
    - Manter license_registry.json com hashes SHA-256
    - Garantir conformidade com politica de direitos autorais (DEC-004)
    """

    def __init__(
        self,
        bibliography_dir: str | Path | None = None,
    ) -> None:
        """Inicializa o gestor bibliografico.

        Args:
            bibliography_dir: Diretorio de bibliografia (padrao: bibliography/).
        """
        self.bibliography_dir = Path(bibliography_dir) if bibliography_dir else BIBLIOGRAPHY_DIR
        self.bibliography_dir.mkdir(parents=True, exist_ok=True)

        self.references_bib = self.bibliography_dir / "references.bib"
        self.license_registry = self.bibliography_dir / "license_registry.json"

        self._registry: dict[str, dict] = self._carregar_registry()

    def _carregar_registry(self) -> dict[str, dict]:
        """Carrega o registry de licencas do disco."""
        if self.license_registry.exists():
            with open(self.license_registry, "r", encoding="utf-8") as f:
                dados = json.load(f)
                # Indexar por DOI para busca rapida
                return {entry["doi"]: entry for entry in dados if entry.get("doi")}
        return {}

    def _salvar_registry(self) -> None:
        """Salva o registry de licencas no disco."""
        entries = list(self._registry.values())
        with open(self.license_registry, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
        logger.debug("License registry salvo: %d entradas", len(entries))

    def adicionar(self, ref: Referencia) -> bool:
        """Adiciona uma referencia ao acervo.

        Args:
            ref: Referencia a ser adicionada.

        Returns:
            True se adicionada, False se ja existia.
        """
        if not ref.doi:
            logger.warning("Referencia sem DOI ignorada: %s", ref.titulo[:60])
            return False

        if ref.doi in self._registry:
            logger.debug("Referencia ja existe: %s", ref.doi)
            return False

        # Registrar no registry
        self._registry[ref.doi] = ref.to_registry_entry()
        self._salvar_registry()

        # Adicionar ao BibTeX
        self._append_bibtex(ref)

        logger.info(
            "Referencia adicionada: %s | OA: %s | %s",
            ref.doi,
            ref.eh_open_access,
            ref.titulo[:50],
        )
        return True

    def buscar_por_doi(self, doi: str) -> dict | None:
        """Busca uma referencia pelo DOI.

        Args:
            doi: Identificador DOI.

        Returns:
            Entrada do registry ou None se nao encontrada.
        """
        return self._registry.get(doi.strip().lower())

    def registrar_pdf(self, doi: str, caminho_pdf: str | Path) -> bool:
        """Registra o armazenamento de um PDF com hash SHA-256.

        Verifica se a licenca permite armazenamento antes de registrar.

        Args:
            doi: DOI do paper.
            caminho_pdf: Caminho onde o PDF foi salvo.

        Returns:
            True se registrado, False se licenca nao permite ou DOI nao encontrado.
        """
        doi = doi.strip().lower()
        entry = self._registry.get(doi)

        if not entry:
            logger.error("DOI nao encontrado no registry: %s", doi)
            return False

        if not entry.get("eh_open_access"):
            logger.error(
                "BLOQUEADO: Tentativa de armazenar PDF sem licenca OA. DOI: %s, Licenca: %s",
                doi,
                entry.get("licenca", "desconhecida"),
            )
            return False

        caminho_pdf = Path(caminho_pdf)
        if not caminho_pdf.exists():
            logger.error("PDF nao encontrado: %s", caminho_pdf)
            return False

        hash_pdf = calcular_sha256(caminho_pdf)
        entry["hash_pdf"] = hash_pdf
        entry["caminho_pdf"] = str(caminho_pdf)
        self._salvar_registry()

        logger.info("PDF registrado: %s | Hash: %s", doi, hash_pdf[:16])
        return True

    def total_referencias(self) -> int:
        """Retorna o total de referencias no acervo."""
        return len(self._registry)

    def total_open_access(self) -> int:
        """Retorna o total de referencias com licenca open access."""
        return sum(1 for e in self._registry.values() if e.get("eh_open_access"))

    def total_com_pdf(self) -> int:
        """Retorna o total de referencias com PDF armazenado."""
        return sum(1 for e in self._registry.values() if e.get("hash_pdf"))

    def resumo(self) -> dict[str, int]:
        """Retorna resumo estatistico do acervo."""
        return {
            "total_referencias": self.total_referencias(),
            "total_open_access": self.total_open_access(),
            "total_com_pdf": self.total_com_pdf(),
            "total_restrito": self.total_referencias() - self.total_open_access(),
        }

    def _append_bibtex(self, ref: Referencia) -> None:
        """Adiciona entrada BibTeX ao arquivo references.bib."""
        with open(self.references_bib, "a", encoding="utf-8") as f:
            f.write("\n" + ref.to_bibtex() + "\n")
