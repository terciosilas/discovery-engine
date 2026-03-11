"""Testes dos modulos de ingestao: pubmed, unpaywall, semantic_scholar.

Usa mocks para nao depender de APIs externas.
"""

from unittest.mock import MagicMock, patch

import pytest

from src.ingestion.pubmed import PubMedArticle, PubMedClient
from src.ingestion.unpaywall import LicenseInfo, UnpaywallClient
from src.ingestion.semantic_scholar import S2Paper, SemanticScholarClient


# === PUBMED ===


PUBMED_SEARCH_XML = """<?xml version="1.0" encoding="UTF-8"?>
<eSearchResult>
    <Count>1500</Count>
    <RetMax>3</RetMax>
    <RetStart>0</RetStart>
    <IdList>
        <Id>38000001</Id>
        <Id>38000002</Id>
        <Id>38000003</Id>
    </IdList>
</eSearchResult>"""

PUBMED_FETCH_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
    <PubmedArticle>
        <MedlineCitation>
            <PMID>38000001</PMID>
            <Article>
                <Journal>
                    <Title>Nature Aging</Title>
                    <JournalIssue>
                        <PubDate><Year>2024</Year></PubDate>
                    </JournalIssue>
                </Journal>
                <ArticleTitle>Proteomic signatures of aging in human plasma</ArticleTitle>
                <Abstract>
                    <AbstractText>We analyzed plasma proteomics data from 50,000 participants.</AbstractText>
                </Abstract>
                <AuthorList>
                    <Author>
                        <LastName>Johnson</LastName>
                        <ForeName>Alice</ForeName>
                    </Author>
                    <Author>
                        <LastName>Smith</LastName>
                        <ForeName>Bob</ForeName>
                    </Author>
                </AuthorList>
            </Article>
            <KeywordList>
                <Keyword>proteomics</Keyword>
                <Keyword>aging</Keyword>
            </KeywordList>
        </MedlineCitation>
        <PubmedData>
            <ArticleIdList>
                <ArticleId IdType="doi">10.1038/s41586-024-00001-1</ArticleId>
                <ArticleId IdType="pmc">PMC1234567</ArticleId>
            </ArticleIdList>
        </PubmedData>
    </PubmedArticle>
</PubmedArticleSet>"""


class TestPubMedClient:
    """Testes do cliente PubMed."""

    def test_pubmed_article_to_dict(self) -> None:
        article = PubMedArticle(
            pmid="12345",
            doi="10.1234/test",
            titulo="Test Paper",
            autores=["Silva, J."],
            journal="Nature",
            ano=2024,
        )
        d = article.to_dict()
        assert d["pmid"] == "12345"
        assert d["doi"] == "10.1234/test"

    @patch("src.ingestion.pubmed.requests.Session")
    def test_search_returns_pmids(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.text = PUBMED_SEARCH_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = PubMedClient()
        client.session = mock_session
        pmids = client.search("proteomics aging", max_results=3)

        assert len(pmids) == 3
        assert "38000001" in pmids
        assert "38000002" in pmids
        assert "38000003" in pmids

    @patch("src.ingestion.pubmed.requests.Session")
    def test_fetch_articles(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.text = PUBMED_FETCH_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = PubMedClient()
        client.session = mock_session
        articles = client.fetch_articles(["38000001"])

        assert len(articles) == 1
        art = articles[0]
        assert art.pmid == "38000001"
        assert art.doi == "10.1038/s41586-024-00001-1"
        assert "Proteomic" in art.titulo
        assert len(art.autores) == 2
        assert art.autores[0] == "Johnson, Alice"
        assert art.journal == "Nature Aging"
        assert art.ano == 2024
        assert "50,000" in art.abstract
        assert "proteomics" in art.keywords
        assert art.pmc_id == "PMC1234567"

    def test_parse_empty_xml(self) -> None:
        client = PubMedClient()
        articles = client._parse_articles("<PubmedArticleSet></PubmedArticleSet>")
        assert articles == []

    def test_parse_invalid_xml(self) -> None:
        client = PubMedClient()
        articles = client._parse_articles("not xml at all")
        assert articles == []


# === UNPAYWALL ===


UNPAYWALL_OA_RESPONSE = {
    "doi": "10.1038/s41586-024-00001-1",
    "is_oa": True,
    "oa_status": "gold",
    "title": "Proteomic signatures of aging",
    "publisher": "Nature Publishing Group",
    "journal_name": "Nature Aging",
    "year": 2024,
    "best_oa_location": {
        "license": "cc-by-4.0",
        "url_for_pdf": "https://example.com/paper.pdf",
        "url_for_landing_page": "https://doi.org/10.1038/s41586-024-00001-1",
    },
    "oa_locations": [],
}

UNPAYWALL_CLOSED_RESPONSE = {
    "doi": "10.1234/closed.001",
    "is_oa": False,
    "oa_status": "closed",
    "title": "A closed paper",
    "publisher": "Elsevier",
    "journal_name": "Some Journal",
    "year": 2023,
    "best_oa_location": None,
    "oa_locations": [],
}


class TestUnpaywallClient:
    """Testes do cliente Unpaywall."""

    def test_license_info_permite_oa(self) -> None:
        info = LicenseInfo(doi="10.1234/test", is_oa=True, licenca="cc-by-4.0")
        assert info.permite_armazenamento is True

    def test_license_info_bloqueia_closed(self) -> None:
        info = LicenseInfo(doi="10.1234/test", is_oa=False, licenca="proprietary")
        assert info.permite_armazenamento is False

    def test_license_info_to_dict(self) -> None:
        info = LicenseInfo(doi="10.1234/test", is_oa=True, licenca="cc-by")
        d = info.to_dict()
        assert d["doi"] == "10.1234/test"
        assert d["permite_armazenamento"] is True

    @patch("src.ingestion.unpaywall.requests.Session")
    def test_check_license_oa(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = UNPAYWALL_OA_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = UnpaywallClient()
        client.session = mock_session
        info = client.check_license("10.1038/s41586-024-00001-1")

        assert info is not None
        assert info.is_oa is True
        assert info.licenca == "cc-by-4.0"
        assert info.permite_armazenamento is True
        assert "pdf" in info.url_pdf

    @patch("src.ingestion.unpaywall.requests.Session")
    def test_check_license_closed(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = UNPAYWALL_CLOSED_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = UnpaywallClient()
        client.session = mock_session
        info = client.check_license("10.1234/closed.001")

        assert info is not None
        assert info.is_oa is False
        assert info.permite_armazenamento is False

    @patch("src.ingestion.unpaywall.requests.Session")
    def test_check_license_not_found(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = UnpaywallClient()
        client.session = mock_session
        info = client.check_license("10.9999/nonexistent")

        assert info is None

    def test_check_license_empty_doi(self) -> None:
        client = UnpaywallClient()
        info = client.check_license("")
        assert info is None


# === SEMANTIC SCHOLAR ===


S2_SEARCH_RESPONSE = {
    "total": 1500,
    "offset": 0,
    "data": [
        {
            "paperId": "abc123",
            "externalIds": {"DOI": "10.1234/s2test.001", "PubMed": "99000001"},
            "title": "Machine Learning for Drug Repurposing in Aging",
            "authors": [{"name": "Maria Santos"}, {"name": "John Doe"}],
            "year": 2024,
            "abstract": "We developed an ML pipeline for drug repurposing.",
            "venue": "Nature Machine Intelligence",
            "citationCount": 42,
            "influentialCitationCount": 8,
            "referenceCount": 55,
            "isOpenAccess": True,
            "fieldsOfStudy": ["Medicine", "Computer Science"],
            "tldr": {"text": "An ML pipeline identifies drug repurposing candidates for aging."},
            "url": "https://www.semanticscholar.org/paper/abc123",
        }
    ],
}


class TestSemanticScholarClient:
    """Testes do cliente Semantic Scholar."""

    def test_s2paper_to_dict(self) -> None:
        paper = S2Paper(
            paper_id="abc",
            doi="10.1234/test",
            titulo="Test",
            citation_count=10,
        )
        d = paper.to_dict()
        assert d["paper_id"] == "abc"
        assert d["citation_count"] == 10

    @patch("src.ingestion.semantic_scholar.requests.Session")
    def test_search(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = S2_SEARCH_RESPONSE
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = SemanticScholarClient()
        client.session = mock_session
        papers = client.search("drug repurposing aging", max_results=1)

        assert len(papers) == 1
        paper = papers[0]
        assert paper.paper_id == "abc123"
        assert paper.doi == "10.1234/s2test.001"
        assert "Machine Learning" in paper.titulo
        assert len(paper.autores) == 2
        assert paper.citation_count == 42
        assert paper.influential_citation_count == 8
        assert paper.is_open_access is True
        assert "Medicine" in paper.fields_of_study
        assert "ML pipeline" in paper.tldr

    @patch("src.ingestion.semantic_scholar.requests.Session")
    def test_get_paper_not_found(self, mock_session_class: MagicMock) -> None:
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        client = SemanticScholarClient()
        client.session = mock_session
        paper = client.get_paper("DOI:10.9999/nonexistent")

        assert paper is None

    def test_parse_paper_empty(self) -> None:
        client = SemanticScholarClient()
        paper = client._parse_paper({})
        assert paper is not None
        assert paper.titulo == ""

    def test_parse_paper_none(self) -> None:
        client = SemanticScholarClient()
        paper = client._parse_paper(None)
        assert paper is None
