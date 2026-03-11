"""Testes para modulos da Fase 2: Analise e Cruzamento.

Testa target_mapper, drug_target_linker, knowledge_graph e candidate_scorer.
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


# --- target_mapper ---

class TestTargetMapper:
    """Testes para src/analysis/target_mapper.py."""

    def test_buscar_mygene_batch_parse_response(self):
        """Testa parsing de resposta do MyGene.info."""
        from src.analysis.target_mapper import buscar_mygene_batch

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "symbol": "MTOR",
                "ensembl": {"gene": "ENSG00000198793"},
                "uniprot": {"Swiss-Prot": "P42345"},
                "entrezgene": 2475,
                "name": "mechanistic target of rapamycin kinase",
            },
            {
                "query": "FAKEGENE",
                "notfound": True,
            },
        ]
        mock_response.raise_for_status = MagicMock()

        with patch("src.analysis.target_mapper.requests.post", return_value=mock_response):
            result = buscar_mygene_batch(["MTOR", "FAKEGENE"])

        assert "MTOR" in result
        assert result["MTOR"]["ensembl_gene"] == "ENSG00000198793"
        assert result["MTOR"]["uniprot"] == "P42345"
        assert "FAKEGENE" not in result

    def test_buscar_mygene_ensembl_list(self):
        """Testa quando ensembl retorna lista (multiplos IDs)."""
        from src.analysis.target_mapper import buscar_mygene_batch

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "symbol": "APOE",
                "ensembl": [
                    {"gene": "ENSG00000130203"},
                    {"gene": "ENSG00000227150"},
                ],
                "uniprot": {"Swiss-Prot": ["P02649"]},
                "entrezgene": 348,
                "name": "apolipoprotein E",
            },
        ]
        mock_response.raise_for_status = MagicMock()

        with patch("src.analysis.target_mapper.requests.post", return_value=mock_response):
            result = buscar_mygene_batch(["APOE"])

        assert result["APOE"]["ensembl_gene"] == "ENSG00000130203"
        assert result["APOE"]["uniprot"] == "P02649"

    def test_consolidar_ranking_filtra_compostos(self):
        """Testa que compostos (prefixo _) sao filtrados."""
        from src.analysis.target_mapper import consolidar_ranking

        ranking = [
            {"rank": 1, "symbol": "_RAPAMYCIN", "nome": "rapamycin",
             "papers_mencionando": 49, "mencoes_totais": 178,
             "ensembl_id": "", "uniprot_id": "", "via": "", "fonte": "composto"},
            {"rank": 2, "symbol": "MTOR", "nome": "mTOR",
             "papers_mencionando": 18, "mencoes_totais": 23,
             "ensembl_id": "ENSG00000198793", "uniprot_id": "", "via": "", "fonte": "genage"},
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(ranking, f)
            ranking_path = Path(f.name)

        with tempfile.TemporaryDirectory() as tmpdir:
            with patch("src.analysis.target_mapper.buscar_mygene_batch", return_value={}):
                alvos = consolidar_ranking(ranking_path, output_dir=Path(tmpdir), top_n=10)

        assert len(alvos) == 1
        assert alvos[0].symbol == "MTOR"
        ranking_path.unlink()


# --- drug_target_linker ---

class TestDrugTargetLinker:
    """Testes para src/analysis/drug_target_linker.py."""

    def test_carregar_drugage(self):
        """Testa carregamento do DrugAge CSV."""
        from src.analysis.drug_target_linker import carregar_drugage

        csv_content = (
            "compound_name,species,strain,dosage,avg_lifespan_change_percent\n"
            "Rapamycin,Mus musculus,UM-HET3,14 ppm,14.8\n"
            "Metformin,Caenorhabditis elegans,N2,50 mM,9.9\n"
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
            f.write(csv_content)
            csv_path = Path(f.name)

        result = carregar_drugage(csv_path)
        assert "rapamycin" in result
        assert len(result["rapamycin"]) == 1
        assert result["rapamycin"][0]["avg_lifespan_change_percent"] == 14.8
        assert "metformin" in result
        csv_path.unlink()

    def test_drug_candidate_to_dict(self):
        """Testa conversao de DrugCandidate para dict."""
        from src.analysis.drug_target_linker import DrugCandidate

        dc = DrugCandidate(
            drug_id="CHEMBL413",
            nome="Rapamycin",
            max_fase_clinica=4,
            geroprotetor_conhecido=True,
        )
        d = dc.to_dict()
        assert d["drug_id"] == "CHEMBL413"
        assert d["geroprotetor_conhecido"] is True
        assert d["max_fase_clinica"] == 4

    def test_checkpoint_save_load(self):
        """Testa checkpoint atomico."""
        from src.analysis.drug_target_linker import carregar_checkpoint, salvar_checkpoint

        with tempfile.TemporaryDirectory() as tmpdir:
            ckpt_path = Path(tmpdir) / "ckpt_test.json"
            data = {"alvos_consultados": ["ENSG00000198793"], "associacoes": [{"x": 1}]}
            salvar_checkpoint(ckpt_path, data)
            loaded = carregar_checkpoint(ckpt_path)
            assert loaded["alvos_consultados"] == ["ENSG00000198793"]
            assert len(loaded["associacoes"]) == 1

    def test_checkpoint_corrompido(self):
        """Testa checkpoint corrompido retorna vazio."""
        from src.analysis.drug_target_linker import carregar_checkpoint

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("INVALID JSON{{{")
            ckpt_path = Path(f.name)

        loaded = carregar_checkpoint(ckpt_path)
        assert loaded["alvos_consultados"] == []
        ckpt_path.unlink()


# --- knowledge_graph ---

class TestKnowledgeGraph:
    """Testes para src/analysis/knowledge_graph.py."""

    def _create_test_data(self, tmpdir: str) -> tuple[Path, Path, Path]:
        """Cria dados de teste minimos."""
        alvos = [
            {"symbol": "MTOR", "nome": "mTOR", "ensembl_id": "ENSG00000198793",
             "papers_mencionando": 18, "via": "mTOR/PI3K"},
            {"symbol": "SIRT1", "nome": "Sirtuin 1", "ensembl_id": "ENSG00000096717",
             "papers_mencionando": 9, "via": "Sirtuinas"},
        ]
        associacoes = [
            {"drug_id": "CHEMBL1", "drug_nome": "DrugA", "target_gene": "MTOR",
             "target_id": "ENSG00000198793", "disease_nome": "Cancer",
             "disease_id": "EFO123", "fase_clinica": 3, "mecanismo_acao": "inhibitor",
             "tipo_acao": "INHIBITOR"},
            {"drug_id": "CHEMBL1", "drug_nome": "DrugA", "target_gene": "SIRT1",
             "target_id": "ENSG00000096717", "disease_nome": "Diabetes",
             "disease_id": "EFO456", "fase_clinica": 2, "mecanismo_acao": "",
             "tipo_acao": ""},
            {"drug_id": "CHEMBL2", "drug_nome": "DrugB", "target_gene": "MTOR",
             "target_id": "ENSG00000198793", "disease_nome": "Cancer",
             "disease_id": "EFO123", "fase_clinica": 4, "mecanismo_acao": "inhibitor",
             "tipo_acao": "INHIBITOR"},
        ]
        candidatos = [
            {"drug_id": "CHEMBL1", "nome": "DrugA", "max_fase_clinica": 3,
             "alvos": [{"gene": "MTOR"}, {"gene": "SIRT1"}],
             "geroprotetor_conhecido": False, "lifespan_efeito": 0, "pchembl_melhor": 7.5},
            {"drug_id": "CHEMBL2", "nome": "DrugB", "max_fase_clinica": 4,
             "alvos": [{"gene": "MTOR"}],
             "geroprotetor_conhecido": True, "lifespan_efeito": 14.8, "pchembl_melhor": 8.2},
        ]

        d = Path(tmpdir)
        alvos_path = d / "alvos.json"
        assoc_path = d / "assoc.json"
        cand_path = d / "cand.json"

        with open(alvos_path, "w") as f: json.dump(alvos, f)
        with open(assoc_path, "w") as f: json.dump(associacoes, f)
        with open(cand_path, "w") as f: json.dump(candidatos, f)

        return assoc_path, cand_path, alvos_path

    def test_construir_grafo_nos(self):
        """Testa que grafo tem nos corretos."""
        from src.analysis.knowledge_graph import construir_grafo

        with tempfile.TemporaryDirectory() as tmpdir:
            assoc_p, cand_p, alvos_p = self._create_test_data(tmpdir)
            G = construir_grafo(assoc_p, cand_p, alvos_p)

        assert G.number_of_nodes() >= 4  # 2 proteins + 2 drugs + diseases
        assert G.has_node("protein:MTOR")
        assert G.has_node("protein:SIRT1")
        assert G.has_node("drug:CHEMBL1")
        assert G.has_node("drug:CHEMBL2")

    def test_construir_grafo_arestas(self):
        """Testa que arestas protein-drug existem."""
        from src.analysis.knowledge_graph import construir_grafo

        with tempfile.TemporaryDirectory() as tmpdir:
            assoc_p, cand_p, alvos_p = self._create_test_data(tmpdir)
            G = construir_grafo(assoc_p, cand_p, alvos_p)

        assert G.has_edge("protein:MTOR", "drug:CHEMBL1")
        assert G.has_edge("protein:MTOR", "drug:CHEMBL2")
        assert G.has_edge("protein:SIRT1", "drug:CHEMBL1")

    def test_calcular_metricas(self):
        """Testa calculo de metricas."""
        from src.analysis.knowledge_graph import calcular_metricas, construir_grafo

        with tempfile.TemporaryDirectory() as tmpdir:
            assoc_p, cand_p, alvos_p = self._create_test_data(tmpdir)
            G = construir_grafo(assoc_p, cand_p, alvos_p)
            metricas = calcular_metricas(G)

        assert "global" in metricas
        assert metricas["global"]["n_proteinas"] == 2
        assert metricas["global"]["n_drogas"] == 2
        assert len(metricas["top_proteinas_centralidade"]) > 0

    def test_detectar_comunidades(self):
        """Testa deteccao de comunidades."""
        from src.analysis.knowledge_graph import construir_grafo, detectar_comunidades

        with tempfile.TemporaryDirectory() as tmpdir:
            assoc_p, cand_p, alvos_p = self._create_test_data(tmpdir)
            G = construir_grafo(assoc_p, cand_p, alvos_p)
            comunidades = detectar_comunidades(G)

        assert comunidades["n_comunidades"] >= 1
        assert len(comunidades["comunidades"]) >= 1


# --- candidate_scorer ---

class TestCandidateScorer:
    """Testes para src/analysis/candidate_scorer.py."""

    def test_score_fase_clinica(self):
        """Testa scoring de fase clinica."""
        from src.analysis.candidate_scorer import _score_fase_clinica

        assert _score_fase_clinica(4) == 1.0
        assert _score_fase_clinica(3) == 0.75
        assert _score_fase_clinica(0) == 0.1

    def test_score_lifespan(self):
        """Testa scoring de lifespan."""
        from src.analysis.candidate_scorer import _score_lifespan

        assert _score_lifespan(0) == 0.0
        assert _score_lifespan(-5) == 0.0
        assert _score_lifespan(10) > 0.3
        assert _score_lifespan(30) > _score_lifespan(10)
        assert _score_lifespan(100) <= 1.0

    def test_score_pchembl(self):
        """Testa scoring de pChEMBL."""
        from src.analysis.candidate_scorer import _score_pchembl

        assert _score_pchembl(0) == 0.0
        assert _score_pchembl(6) >= 0.5
        assert _score_pchembl(8) > _score_pchembl(6)
        assert _score_pchembl(9) == 1.0

    def test_normalizar_min_max(self):
        """Testa normalizacao min-max."""
        from src.analysis.candidate_scorer import _normalizar_min_max

        assert _normalizar_min_max(5, 0, 10) == 0.5
        assert _normalizar_min_max(0, 0, 10) == 0.0
        assert _normalizar_min_max(10, 0, 10) == 1.0
        assert _normalizar_min_max(15, 0, 10) == 1.0  # clamp
        assert _normalizar_min_max(5, 5, 5) == 0.5  # equal min/max

    def test_calcular_scores_ranking(self):
        """Testa que o ranking respeita a logica."""
        from src.analysis.candidate_scorer import calcular_scores

        candidatos = [
            {"drug_id": "CHEMBL413", "nome": "Rapamycin", "max_fase_clinica": 4,
             "n_alvos_envelhecimento": 1, "alvos": [{"gene": "MTOR"}],
             "lifespan_efeito": 14.8, "lifespan_especies": ["mouse"],
             "pchembl_melhor": 8.2, "mecanismos_acao": ["mTOR inhibitor"],
             "geroprotetor_conhecido": True, "fontes": ["curado"]},
            {"drug_id": "CHEMBL_FAKE", "nome": "FakeDrug", "max_fase_clinica": 1,
             "n_alvos_envelhecimento": 0, "alvos": [],
             "lifespan_efeito": 0, "lifespan_especies": [],
             "pchembl_melhor": 0, "mecanismos_acao": [],
             "geroprotetor_conhecido": False, "fontes": []},
        ]
        metricas = {
            "top_drogas_centralidade": [
                {"node": "drug:CHEMBL413", "degree_centrality": 0.05},
            ],
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            cand_path = Path(tmpdir) / "cand.json"
            metr_path = Path(tmpdir) / "metr.json"
            with open(cand_path, "w") as f: json.dump(candidatos, f)
            with open(metr_path, "w") as f: json.dump(metricas, f)

            scored = calcular_scores(cand_path, metr_path, output_dir=Path(tmpdir))

        assert scored[0].nome == "Rapamycin"
        assert scored[0].score_total > scored[1].score_total
        assert scored[0].rank == 1

    def test_scored_candidate_to_dict(self):
        """Testa conversao ScoredCandidate para dict."""
        from src.analysis.candidate_scorer import ScoredCandidate

        sc = ScoredCandidate(
            rank=1, drug_id="CHEMBL413", nome="Rapamycin",
            score_total=0.52, geroprotetor_conhecido=True,
        )
        d = sc.to_dict()
        assert d["rank"] == 1
        assert d["nome"] == "Rapamycin"
        assert d["score_total"] == 0.52


# --- protein_extractor ---

class TestProteinExtractor:
    """Testes para src/analysis/protein_extractor.py."""

    def test_extrair_mtor(self):
        """Testa extracao de mTOR de texto."""
        from src.analysis.protein_extractor import construir_dicionario, extrair_genes_de_texto

        dicio = construir_dicionario()
        # "mTOR" alias tem 4 chars -> case-sensitive. Usar alias longo.
        texto = "The mechanistic target of rapamycin pathway regulates aging. MTOR is key."
        result = extrair_genes_de_texto(texto, dicio)
        assert "MTOR" in result
        assert result["MTOR"] >= 2

    def test_extrair_compostos(self):
        """Testa extracao de compostos."""
        from src.analysis.protein_extractor import construir_dicionario, extrair_genes_de_texto

        dicio = construir_dicionario()
        texto = "Rapamycin and metformin are geroprotective. Resveratrol activates SIRT1."
        result = extrair_genes_de_texto(texto, dicio)
        assert "_RAPAMYCIN" in result
        assert "_METFORMIN" in result
        assert "_RESVERATROL" in result
        assert "SIRT1" in result

    def test_case_sensitivity(self):
        """Testa case sensitivity para simbolos curtos."""
        from src.analysis.protein_extractor import construir_dicionario, extrair_genes_de_texto

        dicio = construir_dicionario()
        # "CAT" o gene vs "cat" animal - deve detectar apenas "CAT" uppercase
        texto = "The CAT gene encodes catalase. The cat sat on the mat."
        result = extrair_genes_de_texto(texto, dicio)
        # CAT deve aparecer (gene symbol e case-sensitive para simbolos curtos)
        assert "CAT" in result
