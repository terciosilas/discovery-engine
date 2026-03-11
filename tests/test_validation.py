"""Testes para modulos da Fase 3: Validacao Computacional."""

import json
import tempfile
from pathlib import Path

import pytest


class TestValidacaoLiteratura:
    """Testes para validacao cruzada com literatura."""

    def test_geroprotetores_literatura_definidos(self):
        """Verifica que lista de geroprotetores da literatura existe."""
        from src.validation.computational import GEROPROTETORES_LITERATURA
        assert len(GEROPROTETORES_LITERATURA) >= 10

    def test_controles_negativos_definidos(self):
        """Verifica que lista de controles negativos existe."""
        from src.validation.computational import CONTROLES_NEGATIVOS
        assert len(CONTROLES_NEGATIVOS) >= 5

    def test_validar_literatura_formato(self):
        """Testa formato de saida da validacao."""
        from src.validation.computational import validar_literatura

        ranked = [
            {"nome": "Rapamycin", "rank": 1, "score_total": 0.5},
            {"nome": "Metformin", "rank": 2, "score_total": 0.4},
            {"nome": "FakeDrug", "rank": 3, "score_total": 0.3},
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(ranked, f)
            path = Path(f.name)

        result = validar_literatura(path)
        assert "precisao_top20" in result
        assert "geroprotetores_encontrados_top20" in result
        assert "novos_candidatos_top20" in result
        path.unlink()


class TestBootstrap:
    """Testes para bootstrap do ranking."""

    def _create_test_files(self, tmpdir: str) -> tuple[Path, Path]:
        """Cria arquivos de teste."""
        candidatos = [
            {"drug_id": f"CHEMBL{i}", "nome": f"Drug{i}",
             "max_fase_clinica": 4 - (i % 5), "n_alvos_envelhecimento": i % 3,
             "lifespan_efeito": max(0, 15 - i), "pchembl_melhor": max(0, 9 - i * 0.5),
             "geroprotetor_conhecido": i < 3, "fontes": ["curado"] if i < 3 else []}
            for i in range(20)
        ]
        candidatos[0]["nome"] = "Rapamycin"
        candidatos[1]["nome"] = "Metformin"

        metricas = {
            "top_drogas_centralidade": [
                {"node": f"drug:CHEMBL{i}", "degree_centrality": 0.05 - i * 0.002}
                for i in range(10)
            ],
        }

        d = Path(tmpdir)
        cand_path = d / "cand.json"
        metr_path = d / "metr.json"
        with open(cand_path, "w") as f: json.dump(candidatos, f)
        with open(metr_path, "w") as f: json.dump(metricas, f)
        return cand_path, metr_path

    def test_bootstrap_deterministic(self):
        """Testa que bootstrap com mesmo seed da mesmo resultado."""
        from src.validation.computational import bootstrap_ranking

        with tempfile.TemporaryDirectory() as tmpdir:
            cand_p, metr_p = self._create_test_files(tmpdir)
            r1 = bootstrap_ranking(cand_p, metr_p, n_bootstrap=10, seed=42)
            r2 = bootstrap_ranking(cand_p, metr_p, n_bootstrap=10, seed=42)

        assert r1["rapamycin"]["rank_medio"] == r2["rapamycin"]["rank_medio"]

    def test_bootstrap_rapamycin_estavel(self):
        """Testa que rapamycin e estavel no bootstrap."""
        from src.validation.computational import bootstrap_ranking

        with tempfile.TemporaryDirectory() as tmpdir:
            cand_p, metr_p = self._create_test_files(tmpdir)
            result = bootstrap_ranking(cand_p, metr_p, n_bootstrap=100, seed=42)

        rap = result.get("rapamycin", {})
        assert rap.get("rank_medio", 99) <= 5  # Deve estar no top 5


class TestAblation:
    """Testes para ablation study."""

    def test_ablation_formato(self):
        """Testa formato de saida do ablation."""
        from src.validation.computational import ablation_study

        candidatos = [
            {"drug_id": "CHEMBL413", "nome": "Rapamycin", "max_fase_clinica": 4,
             "n_alvos_envelhecimento": 1, "lifespan_efeito": 14.8,
             "pchembl_melhor": 8.2, "geroprotetor_conhecido": True, "fontes": ["curado"]},
            {"drug_id": "CHEMBL1431", "nome": "Metformin", "max_fase_clinica": 4,
             "n_alvos_envelhecimento": 0, "lifespan_efeito": 9.9,
             "pchembl_melhor": 0, "geroprotetor_conhecido": True, "fontes": ["curado"]},
        ]
        metricas = {"top_drogas_centralidade": [
            {"node": "drug:CHEMBL413", "degree_centrality": 0.05}
        ]}

        with tempfile.TemporaryDirectory() as tmpdir:
            cand_path = Path(tmpdir) / "cand.json"
            metr_path = Path(tmpdir) / "metr.json"
            with open(cand_path, "w") as f: json.dump(candidatos, f)
            with open(metr_path, "w") as f: json.dump(metricas, f)

            result = ablation_study(cand_path, metr_path)

        assert len(result) == 6  # 6 features
        for feat, r in result.items():
            assert "rapamycin_rank" in r
            assert "metformin_rank" in r
            assert "avg_rank_change" in r


class TestControleNegativo:
    """Testes para controle negativo."""

    def test_controle_negativo_passa(self):
        """Testa que controles negativos nao aparecem no ranking."""
        from src.validation.computational import validar_controles_negativos

        ranked = [
            {"nome": "Rapamycin", "rank": 1, "score_total": 0.5},
            {"nome": "Metformin", "rank": 2, "score_total": 0.4},
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(ranked, f)
            path = Path(f.name)

        result = validar_controles_negativos(path)
        assert result["passou"] is True
        assert result["taxa_falso_positivo"] == 0.0
        path.unlink()

    def test_controle_negativo_detecta_falso_positivo(self):
        """Testa deteccao de falso positivo."""
        from src.validation.computational import validar_controles_negativos

        ranked = [
            {"nome": "Ibuprofen", "rank": 5, "score_total": 0.5},
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(ranked, f)
            path = Path(f.name)

        result = validar_controles_negativos(path)
        assert result["passou"] is False
        assert len(result["falsos_positivos"]) == 1
        path.unlink()


class TestSensibilidade:
    """Testes para analise de sensibilidade."""

    def test_sensibilidade_5_configs(self):
        """Testa que 5 configuracoes sao testadas."""
        from src.validation.computational import analise_sensibilidade

        candidatos = [
            {"drug_id": "CHEMBL413", "nome": "Rapamycin", "max_fase_clinica": 4,
             "n_alvos_envelhecimento": 1, "lifespan_efeito": 14.8,
             "pchembl_melhor": 8.2, "geroprotetor_conhecido": True, "fontes": ["curado"]},
        ]
        metricas = {"top_drogas_centralidade": []}

        with tempfile.TemporaryDirectory() as tmpdir:
            cand_path = Path(tmpdir) / "cand.json"
            metr_path = Path(tmpdir) / "metr.json"
            with open(cand_path, "w") as f: json.dump(candidatos, f)
            with open(metr_path, "w") as f: json.dump(metricas, f)

            result = analise_sensibilidade(cand_path, metr_path)

        assert len(result["configuracoes"]) == 5
