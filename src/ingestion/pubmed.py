"""Pipeline de busca no PubMed via E-utilities API.

Usa a API gratuita do NCBI para buscar papers por query.
Rate limits: 3 req/s sem API key, 10 req/s com API key.
Documentacao: https://www.ncbi.nlm.nih.gov/books/NBK25497/
"""

import logging
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Any

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEARCH_URL = f"{BASE_URL}/esearch.fcgi"
FETCH_URL = f"{BASE_URL}/efetch.fcgi"

# Rate limit: 3 req/s sem key
MIN_INTERVAL_S = 0.35


@dataclass
class PubMedArticle:
    """Representa um artigo retornado pelo PubMed."""

    pmid: str = ""
    doi: str = ""
    titulo: str = ""
    autores: list[str] = field(default_factory=list)
    journal: str = ""
    ano: int = 0
    abstract: str = ""
    keywords: list[str] = field(default_factory=list)
    tipo_publicacao: list[str] = field(default_factory=list)
    pmc_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Converte para dicionario."""
        return {
            "pmid": self.pmid,
            "doi": self.doi,
            "titulo": self.titulo,
            "autores": self.autores,
            "journal": self.journal,
            "ano": self.ano,
            "abstract": self.abstract,
            "keywords": self.keywords,
            "tipo_publicacao": self.tipo_publicacao,
            "pmc_id": self.pmc_id,
        }


class PubMedClient:
    """Cliente para a API E-utilities do PubMed/NCBI.

    Busca artigos cientificos por query e retorna metadados estruturados.
    Respeita rate limits automaticamente.
    """

    def __init__(
        self,
        api_key: str = "",
        email: str = "",
        tool: str = "discovery_engine",
    ) -> None:
        """Inicializa o cliente PubMed.

        Args:
            api_key: API key do NCBI (opcional, aumenta rate limit para 10 req/s).
            email: Email do pesquisador (recomendado pelo NCBI).
            tool: Nome da ferramenta (identificacao para o NCBI).
        """
        self.api_key = api_key
        self.email = email
        self.tool = tool
        self.session = requests.Session()
        self._last_request_time: float = 0.0

        self.min_interval = 0.12 if api_key else MIN_INTERVAL_S

    def _rate_limit(self) -> None:
        """Aguarda tempo minimo entre requisicoes."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_request_time = time.time()

    def _base_params(self) -> dict[str, str]:
        """Parametros comuns a todas as requisicoes."""
        params: dict[str, str] = {"tool": self.tool}
        if self.email:
            params["email"] = self.email
        if self.api_key:
            params["api_key"] = self.api_key
        return params

    def search(
        self,
        query: str,
        max_results: int = 100,
        date_min: str = "",
        date_max: str = "",
        sort: str = "relevance",
    ) -> list[str]:
        """Busca PMIDs no PubMed por query.

        Args:
            query: Query de busca (sintaxe PubMed).
            max_results: Maximo de resultados.
            date_min: Data minima (YYYY/MM/DD).
            date_max: Data maxima (YYYY/MM/DD).
            sort: Ordenacao (relevance, pub_date, first_author).

        Returns:
            Lista de PMIDs encontrados.
        """
        pmids: list[str] = []
        batch_size = min(max_results, 500)  # PubMed max retmax = 10000
        retstart = 0

        while retstart < max_results:
            self._rate_limit()

            params = self._base_params()
            params.update({
                "db": "pubmed",
                "term": query,
                "retmax": str(min(batch_size, max_results - retstart)),
                "retstart": str(retstart),
                "sort": sort,
                "retmode": "xml",
            })
            if date_min:
                params["mindate"] = date_min
                params["datetype"] = "pdat"
            if date_max:
                params["maxdate"] = date_max
                if "datetype" not in params:
                    params["datetype"] = "pdat"

            try:
                response = self.session.get(SEARCH_URL, params=params, timeout=30)
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error("Erro na busca PubMed: %s | Query: %s", e, query[:50])
                break

            root = ET.fromstring(response.text)

            # Total de resultados disponiveis
            count_elem = root.find("Count")
            total_available = int(count_elem.text) if count_elem is not None and count_elem.text else 0

            if retstart == 0:
                logger.info(
                    "PubMed search: '%s' -> %d resultados disponiveis (buscando ate %d)",
                    query[:50],
                    total_available,
                    max_results,
                )

            id_list = root.find("IdList")
            if id_list is None:
                break

            batch_ids = [id_elem.text for id_elem in id_list.findall("Id") if id_elem.text]
            if not batch_ids:
                break

            pmids.extend(batch_ids)
            retstart += len(batch_ids)

            if retstart >= total_available:
                break

        logger.info("PubMed search concluida: %d PMIDs coletados", len(pmids))
        return pmids

    def fetch_articles(self, pmids: list[str], batch_size: int = 100) -> list[PubMedArticle]:
        """Busca metadados completos de artigos por PMIDs.

        Args:
            pmids: Lista de PMIDs.
            batch_size: Tamanho do batch (max 200 recomendado).

        Returns:
            Lista de PubMedArticle com metadados.
        """
        articles: list[PubMedArticle] = []

        for i in range(0, len(pmids), batch_size):
            batch = pmids[i:i + batch_size]
            self._rate_limit()

            params = self._base_params()
            params.update({
                "db": "pubmed",
                "id": ",".join(batch),
                "retmode": "xml",
                "rettype": "abstract",
            })

            try:
                response = self.session.get(FETCH_URL, params=params, timeout=60)
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error("Erro no fetch PubMed: %s | Batch %d-%d", e, i, i + len(batch))
                continue

            batch_articles = self._parse_articles(response.text)
            articles.extend(batch_articles)

            logger.debug(
                "Fetch batch %d-%d: %d artigos parseados",
                i, i + len(batch), len(batch_articles),
            )

        logger.info("PubMed fetch concluido: %d artigos com metadados", len(articles))
        return articles

    def search_and_fetch(
        self,
        query: str,
        max_results: int = 100,
        date_min: str = "",
        date_max: str = "",
        sort: str = "relevance",
    ) -> list[PubMedArticle]:
        """Busca e retorna artigos completos em uma unica chamada.

        Args:
            query: Query de busca.
            max_results: Maximo de resultados.
            date_min: Data minima (YYYY/MM/DD).
            date_max: Data maxima (YYYY/MM/DD).
            sort: Ordenacao.

        Returns:
            Lista de PubMedArticle.
        """
        pmids = self.search(query, max_results, date_min, date_max, sort)
        if not pmids:
            return []
        return self.fetch_articles(pmids)

    def _parse_articles(self, xml_text: str) -> list[PubMedArticle]:
        """Parseia XML do PubMed em lista de PubMedArticle."""
        articles: list[PubMedArticle] = []

        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as e:
            logger.error("Erro parseando XML do PubMed: %s", e)
            return articles

        for article_elem in root.findall(".//PubmedArticle"):
            article = self._parse_single_article(article_elem)
            if article:
                articles.append(article)

        return articles

    def _parse_single_article(self, elem: ET.Element) -> PubMedArticle | None:
        """Parseia um unico PubmedArticle do XML."""
        article = PubMedArticle()

        # PMID
        pmid_elem = elem.find(".//PMID")
        if pmid_elem is not None and pmid_elem.text:
            article.pmid = pmid_elem.text

        # Titulo
        title_elem = elem.find(".//ArticleTitle")
        if title_elem is not None:
            article.titulo = "".join(title_elem.itertext()).strip()

        # Abstract
        abstract_parts = elem.findall(".//AbstractText")
        if abstract_parts:
            parts = []
            for part in abstract_parts:
                label = part.get("Label", "")
                text = "".join(part.itertext()).strip()
                if label and text:
                    parts.append(f"{label}: {text}")
                elif text:
                    parts.append(text)
            article.abstract = " ".join(parts)

        # Autores
        for author in elem.findall(".//Author"):
            lastname = author.find("LastName")
            forename = author.find("ForeName")
            if lastname is not None and lastname.text:
                name = lastname.text
                if forename is not None and forename.text:
                    name = f"{lastname.text}, {forename.text}"
                article.autores.append(name)

        # Journal
        journal_elem = elem.find(".//Journal/Title")
        if journal_elem is not None and journal_elem.text:
            article.journal = journal_elem.text

        # Ano
        year_elem = elem.find(".//PubDate/Year")
        if year_elem is not None and year_elem.text:
            try:
                article.ano = int(year_elem.text)
            except ValueError:
                pass
        if article.ano == 0:
            medline_year = elem.find(".//PubDate/MedlineDate")
            if medline_year is not None and medline_year.text:
                try:
                    article.ano = int(medline_year.text[:4])
                except ValueError:
                    pass

        # DOI
        for id_elem in elem.findall(".//ArticleId"):
            if id_elem.get("IdType") == "doi" and id_elem.text:
                article.doi = id_elem.text.strip().lower()
            elif id_elem.get("IdType") == "pmc" and id_elem.text:
                article.pmc_id = id_elem.text.strip()

        # Keywords
        for kw in elem.findall(".//Keyword"):
            if kw.text:
                article.keywords.append(kw.text.strip())

        # Tipo de publicacao
        for pt in elem.findall(".//PublicationType"):
            if pt.text:
                article.tipo_publicacao.append(pt.text.strip())

        return article
