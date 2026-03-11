"""Cliente da API Semantic Scholar.

Complementa PubMed com dados de citacao, influencia e referencias.
API gratuita com rate limit de 1 req/s (sem key) ou 10 req/s (com key).
Documentacao: https://api.semanticscholar.org/
"""

import logging
import time
from dataclasses import dataclass, field
from typing import Any

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://api.semanticscholar.org/graph/v1"

# Rate limit: 1 req/s sem key (usar 1.5s para margem de seguranca)
MIN_INTERVAL_S = 1.5


@dataclass
class S2Paper:
    """Representa um paper do Semantic Scholar."""

    paper_id: str = ""
    doi: str = ""
    titulo: str = ""
    autores: list[str] = field(default_factory=list)
    ano: int = 0
    abstract: str = ""
    venue: str = ""
    citation_count: int = 0
    influential_citation_count: int = 0
    reference_count: int = 0
    is_open_access: bool = False
    fields_of_study: list[str] = field(default_factory=list)
    tldr: str = ""  # Too Long Didn't Read (resumo de 1 frase gerado por IA)
    url: str = ""
    external_ids: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "paper_id": self.paper_id,
            "doi": self.doi,
            "titulo": self.titulo,
            "autores": self.autores,
            "ano": self.ano,
            "abstract": self.abstract,
            "venue": self.venue,
            "citation_count": self.citation_count,
            "influential_citation_count": self.influential_citation_count,
            "reference_count": self.reference_count,
            "is_open_access": self.is_open_access,
            "fields_of_study": self.fields_of_study,
            "tldr": self.tldr,
            "url": self.url,
            "external_ids": self.external_ids,
        }


class SemanticScholarClient:
    """Cliente para a API do Semantic Scholar.

    Fornece dados de citacao e influencia que o PubMed nao oferece.
    Util para ranquear papers por impacto real na area.
    """

    # Campos que pedimos na API
    PAPER_FIELDS = (
        "paperId,externalIds,title,authors,year,abstract,venue,"
        "citationCount,influentialCitationCount,referenceCount,"
        "isOpenAccess,fieldsOfStudy,tldr,url"
    )

    def __init__(self, api_key: str = "") -> None:
        """Inicializa o cliente Semantic Scholar.

        Args:
            api_key: API key (opcional, aumenta rate limit).
        """
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers["x-api-key"] = api_key
        self._last_request_time: float = 0.0
        self.min_interval = 0.12 if api_key else MIN_INTERVAL_S

    def _rate_limit(self) -> None:
        """Aguarda tempo minimo entre requisicoes."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_request_time = time.time()

    def search(
        self,
        query: str,
        max_results: int = 100,
        year_min: int = 0,
        year_max: int = 0,
        fields_of_study: list[str] | None = None,
    ) -> list[S2Paper]:
        """Busca papers por query.

        Args:
            query: Texto de busca.
            max_results: Maximo de resultados (API max 1000 por busca).
            year_min: Ano minimo.
            year_max: Ano maximo.
            fields_of_study: Filtro por area (ex: ["Medicine", "Biology"]).

        Returns:
            Lista de S2Paper.
        """
        papers: list[S2Paper] = []
        offset = 0
        limit = min(max_results, 100)  # API max 100 por pagina

        while offset < max_results:
            self._rate_limit()

            params: dict[str, str] = {
                "query": query,
                "offset": str(offset),
                "limit": str(min(limit, max_results - offset)),
                "fields": self.PAPER_FIELDS,
            }

            if year_min or year_max:
                year_range = f"{year_min or ''}-{year_max or ''}"
                params["year"] = year_range

            if fields_of_study:
                params["fieldsOfStudy"] = ",".join(fields_of_study)

            try:
                response = self.session.get(
                    f"{BASE_URL}/paper/search",
                    params=params,
                    timeout=30,
                )
                if response.status_code == 429:
                    logger.warning("Rate limit atingido no Semantic Scholar. Aguardando 5s...")
                    time.sleep(5)
                    continue
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error("Erro na busca Semantic Scholar: %s | Query: %s", e, query[:50])
                break

            data = response.json()
            total = data.get("total", 0)

            if offset == 0:
                logger.info(
                    "S2 search: '%s' -> %d resultados disponiveis (buscando ate %d)",
                    query[:50],
                    total,
                    max_results,
                )

            for item in data.get("data", []):
                paper = self._parse_paper(item)
                if paper:
                    papers.append(paper)

            offset += limit
            if offset >= total:
                break

        logger.info("S2 search concluida: %d papers coletados", len(papers))
        return papers

    def get_paper(self, paper_id: str, _retries: int = 3) -> S2Paper | None:
        """Busca um paper especifico por ID (DOI, PMID, S2 ID, etc.).

        Args:
            paper_id: Identificador. Formatos aceitos:
                - DOI: "DOI:10.1234/example"
                - PMID: "PMID:12345678"
                - S2 ID: "649def34f8be52c8b66281af98ae884c09aef38b"
            _retries: Tentativas restantes em caso de 429.

        Returns:
            S2Paper ou None se nao encontrado.
        """
        self._rate_limit()

        try:
            response = self.session.get(
                f"{BASE_URL}/paper/{paper_id}",
                params={"fields": self.PAPER_FIELDS},
                timeout=15,
            )
            if response.status_code == 404:
                logger.debug("Paper nao encontrado no S2: %s", paper_id)
                return None
            if response.status_code == 429 and _retries > 0:
                wait = 5 * (4 - _retries)  # 5s, 10s, 15s
                logger.warning("S2 rate limit (429) para %s. Aguardando %ds...", paper_id[:40], wait)
                time.sleep(wait)
                return self.get_paper(paper_id, _retries=_retries - 1)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error("Erro no fetch S2: %s | ID: %s", e, paper_id)
            return None

        return self._parse_paper(response.json())

    def get_papers_batch(self, paper_ids: list[str], batch_size: int = 100) -> dict[str, S2Paper]:
        """Busca multiplos papers em batch (muito mais eficiente que individual).

        Usa o endpoint POST /paper/batch que aceita ate 500 IDs por chamada.

        Args:
            paper_ids: Lista de identificadores (DOI:..., PMID:..., ou S2 ID).
            batch_size: Tamanho de cada batch (max 500).

        Returns:
            Dict de paper_id_original -> S2Paper (somente encontrados).
        """
        results: dict[str, S2Paper] = {}
        batch_size = min(batch_size, 500)

        for i in range(0, len(paper_ids), batch_size):
            batch = paper_ids[i:i + batch_size]
            self._rate_limit()

            try:
                response = self.session.post(
                    f"{BASE_URL}/paper/batch",
                    json={"ids": batch},
                    params={"fields": self.PAPER_FIELDS},
                    timeout=60,
                )
                if response.status_code == 429:
                    logger.warning("S2 batch rate limit. Aguardando 10s...")
                    time.sleep(10)
                    # Retry este batch
                    self._rate_limit()
                    response = self.session.post(
                        f"{BASE_URL}/paper/batch",
                        json={"ids": batch},
                        params={"fields": self.PAPER_FIELDS},
                        timeout=60,
                    )
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error("Erro no batch S2: %s | Batch %d-%d", e, i, i + len(batch))
                continue

            data_list = response.json()
            for original_id, paper_data in zip(batch, data_list):
                if paper_data is not None:
                    paper = self._parse_paper(paper_data)
                    if paper:
                        results[original_id] = paper

            logger.info(
                "S2 batch %d-%d: %d/%d encontrados",
                i, i + len(batch),
                sum(1 for d in data_list if d is not None),
                len(batch),
            )

        logger.info("S2 batch total: %d/%d encontrados", len(results), len(paper_ids))
        return results

    def get_paper_by_doi(self, doi: str) -> S2Paper | None:
        """Busca paper por DOI.

        Args:
            doi: Identificador DOI.

        Returns:
            S2Paper ou None.
        """
        return self.get_paper(f"DOI:{doi}")

    def get_citations(self, paper_id: str, max_results: int = 100) -> list[S2Paper]:
        """Busca papers que citam o paper dado.

        Args:
            paper_id: ID do paper (DOI:..., PMID:..., ou S2 ID).
            max_results: Maximo de citacoes.

        Returns:
            Lista de S2Paper que citam o paper.
        """
        self._rate_limit()

        try:
            response = self.session.get(
                f"{BASE_URL}/paper/{paper_id}/citations",
                params={
                    "fields": "paperId,externalIds,title,authors,year,citationCount,isOpenAccess",
                    "limit": str(min(max_results, 1000)),
                },
                timeout=30,
            )
            if response.status_code == 404:
                return []
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error("Erro buscando citacoes S2: %s | ID: %s", e, paper_id)
            return []

        papers = []
        for item in response.json().get("data", []):
            citing = item.get("citingPaper", {})
            paper = self._parse_paper(citing)
            if paper:
                papers.append(paper)

        logger.info("S2 citations: %d citacoes encontradas para %s", len(papers), paper_id[:30])
        return papers

    def _parse_paper(self, data: dict) -> S2Paper | None:
        """Parseia dados de um paper do Semantic Scholar."""
        if data is None:
            return None

        paper = S2Paper()
        paper.paper_id = data.get("paperId", "")
        paper.titulo = data.get("title", "")
        paper.ano = data.get("year") or 0
        paper.abstract = data.get("abstract", "") or ""
        paper.venue = data.get("venue", "") or ""
        paper.citation_count = data.get("citationCount") or 0
        paper.influential_citation_count = data.get("influentialCitationCount") or 0
        paper.reference_count = data.get("referenceCount") or 0
        paper.is_open_access = data.get("isOpenAccess", False) or False
        paper.fields_of_study = data.get("fieldsOfStudy") or []
        paper.url = data.get("url", "") or ""

        # External IDs (DOI, PMID, etc.)
        ext_ids = data.get("externalIds") or {}
        paper.external_ids = {k: str(v) for k, v in ext_ids.items() if v}
        paper.doi = ext_ids.get("DOI", "").lower() if ext_ids.get("DOI") else ""

        # TLDR (resumo de 1 frase)
        tldr = data.get("tldr")
        if tldr and isinstance(tldr, dict):
            paper.tldr = tldr.get("text", "")

        # Autores
        for author in data.get("authors") or []:
            name = author.get("name", "")
            if name:
                paper.autores.append(name)

        return paper
