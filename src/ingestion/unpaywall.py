"""Verificacao de licenca via Unpaywall API.

Dado um DOI, verifica se o paper eh open access e qual a licenca.
Obrigatorio verificar ANTES de armazenar qualquer PDF (DEC-004).
Documentacao: https://unpaywall.org/products/api
"""

import logging
import time
from dataclasses import dataclass
from typing import Any

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://api.unpaywall.org/v2"

# Rate limit: 100.000 req/dia (~1.15 req/s), mas ser conservador
MIN_INTERVAL_S = 0.5


@dataclass
class LicenseInfo:
    """Informacoes de licenca de um paper."""

    doi: str = ""
    is_oa: bool = False
    oa_status: str = ""  # gold, green, hybrid, bronze, closed
    licenca: str = ""
    url_pdf: str = ""
    url_landing_page: str = ""
    publisher: str = ""
    titulo: str = ""
    ano: int = 0
    journal: str = ""

    @property
    def permite_armazenamento(self) -> bool:
        """Verifica se a licenca permite armazenar o PDF (DEC-004)."""
        licencas_permitidas = {
            "cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa", "cc0",
            "cc-by-4.0", "cc-by-sa-4.0", "cc-by-nc-4.0", "cc-by-nc-sa-4.0",
            "public-domain", "pd",
        }
        return self.licenca.lower() in licencas_permitidas

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "doi": self.doi,
            "is_oa": self.is_oa,
            "oa_status": self.oa_status,
            "licenca": self.licenca,
            "permite_armazenamento": self.permite_armazenamento,
            "url_pdf": self.url_pdf,
            "url_landing_page": self.url_landing_page,
            "publisher": self.publisher,
            "titulo": self.titulo,
            "ano": self.ano,
            "journal": self.journal,
        }


class UnpaywallClient:
    """Cliente para a API do Unpaywall.

    Verifica status de open access e licenca de papers via DOI.
    Requer um email valido para identificacao (politica do Unpaywall).
    """

    def __init__(self, email: str = "discovery.engine@research.org") -> None:
        """Inicializa o cliente Unpaywall.

        Args:
            email: Email para identificacao na API (obrigatorio pelo Unpaywall).
        """
        self.email = email
        self.session = requests.Session()
        self._last_request_time: float = 0.0

    def _rate_limit(self) -> None:
        """Aguarda tempo minimo entre requisicoes."""
        elapsed = time.time() - self._last_request_time
        if elapsed < MIN_INTERVAL_S:
            time.sleep(MIN_INTERVAL_S - elapsed)
        self._last_request_time = time.time()

    def check_license(self, doi: str) -> LicenseInfo | None:
        """Verifica licenca de um paper pelo DOI.

        Args:
            doi: Identificador DOI do paper.

        Returns:
            LicenseInfo com dados de licenca, ou None se DOI nao encontrado.
        """
        doi = doi.strip().lower()
        if not doi:
            logger.warning("DOI vazio recebido")
            return None

        self._rate_limit()

        url = f"{BASE_URL}/{doi}"
        params = {"email": self.email}

        try:
            response = self.session.get(url, params=params, timeout=15)
            if response.status_code == 404:
                logger.debug("DOI nao encontrado no Unpaywall: %s", doi)
                return None
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error("Erro na consulta Unpaywall: %s | DOI: %s", e, doi)
            return None

        data = response.json()
        return self._parse_response(doi, data)

    def check_licenses_batch(self, dois: list[str]) -> dict[str, LicenseInfo]:
        """Verifica licencas de multiplos papers.

        Args:
            dois: Lista de DOIs.

        Returns:
            Dict de DOI -> LicenseInfo (apenas DOIs encontrados).
        """
        results: dict[str, LicenseInfo] = {}
        total = len(dois)

        for i, doi in enumerate(dois):
            info = self.check_license(doi)
            if info:
                results[doi.strip().lower()] = info

            if (i + 1) % 50 == 0:
                logger.info("Unpaywall: %d/%d DOIs verificados", i + 1, total)

        logger.info(
            "Unpaywall batch concluido: %d/%d DOIs encontrados, %d open access",
            len(results),
            total,
            sum(1 for r in results.values() if r.is_oa),
        )
        return results

    def _parse_response(self, doi: str, data: dict) -> LicenseInfo:
        """Parseia resposta do Unpaywall em LicenseInfo."""
        info = LicenseInfo(doi=doi)

        info.is_oa = data.get("is_oa", False)
        info.oa_status = data.get("oa_status", "closed")
        info.titulo = data.get("title", "")
        info.publisher = data.get("publisher", "")
        info.journal = data.get("journal_name", "")

        year = data.get("year")
        if year:
            try:
                info.ano = int(year)
            except (ValueError, TypeError):
                pass

        # Melhor localizacao OA
        best_oa = data.get("best_oa_location")
        if best_oa:
            info.licenca = best_oa.get("license", "") or ""
            info.url_pdf = best_oa.get("url_for_pdf", "") or ""
            info.url_landing_page = best_oa.get("url_for_landing_page", "") or ""

        # Se nao tem licenca na best_oa, tentar outras localizacoes
        if not info.licenca:
            for location in data.get("oa_locations", []):
                license_val = location.get("license", "")
                if license_val:
                    info.licenca = license_val
                    if not info.url_pdf:
                        info.url_pdf = location.get("url_for_pdf", "") or ""
                    break

        return info
