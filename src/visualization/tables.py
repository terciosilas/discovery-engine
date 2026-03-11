"""Geracao de tabelas suplementares formatadas.

Gera tabelas S3-S7 a partir dos dados processados.

Uso:
    python -m src.visualization.tables data/processed/ outputs/supplementary/
"""

import csv
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def gerar_table_s3_bootstrap(validation_path: Path, output_dir: Path) -> Path:
    """Table S3: Bootstrap stability results for top 20 compounds."""
    with open(validation_path) as f:
        data = json.load(f)

    path = output_dir / "Table_S3_bootstrap_top20.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Compound", "Mean_Rank", "Median_Rank", "Std_Dev",
            "Min_Rank", "Max_Rank", "Top10_Freq_Pct", "N_Appearances"
        ])
        for nome, stats in data["bootstrap"]["top20_estavel"]:
            writer.writerow([
                nome.title(),
                stats["rank_medio"],
                stats["rank_mediano"],
                stats["rank_std"],
                stats["rank_min"],
                stats["rank_max"],
                stats["top10_freq"],
                stats["n_aparicoes"]
            ])

    logger.info(f"Table S3 salva: {path}")
    return path


def gerar_table_s4_ablation(validation_path: Path, output_dir: Path) -> Path:
    """Table S4: Ablation study results."""
    with open(validation_path) as f:
        data = json.load(f)

    labels = {
        "fase_clinica": "Clinical Phase",
        "n_alvos_envelhecimento": "Aging Targets",
        "lifespan_efeito": "Lifespan Effect",
        "pchembl": "Binding Potency (pChEMBL)",
        "literatura": "Literature Evidence",
        "centralidade_grafo": "Graph Centrality"
    }

    path = output_dir / "Table_S4_ablation_results.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Feature_Removed", "Original_Weight", "Rapamycin_Rank",
            "Metformin_Rank", "Avg_Rank_Change", "Max_Rank_Change",
            "Positive_Controls_OK"
        ])
        for feat, result in data["ablation"].items():
            writer.writerow([
                labels.get(feat, feat),
                result["peso_original"],
                result["rapamycin_rank"],
                result["metformin_rank"],
                round(result["avg_rank_change"], 2),
                result["max_rank_change"],
                result["controle_ok"]
            ])

    logger.info(f"Table S4 salva: {path}")
    return path


def gerar_table_s5_sensitivity(validation_path: Path, output_dir: Path) -> Path:
    """Table S5: Sensitivity analysis configurations and ranks."""
    with open(validation_path) as f:
        data = json.load(f)

    path = output_dir / "Table_S5_sensitivity_configs.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Configuration", "Rapamycin_Rank", "Metformin_Rank",
            "Spermidine_Rank", "Resveratrol_Rank", "Top5_Compounds"
        ])
        for config in data["sensibilidade"]["configuracoes"]:
            writer.writerow([
                config["configuracao"],
                config["rapamycin_rank"],
                config["metformin_rank"],
                config["spermidine_rank"],
                config["resveratrol_rank"],
                "; ".join(config["top5"])
            ])

    logger.info(f"Table S5 salva: {path}")
    return path


def gerar_table_s6_graph_metrics(metrics_path: Path, output_dir: Path) -> Path:
    """Table S6: Knowledge graph centrality metrics for protein targets."""
    with open(metrics_path) as f:
        data = json.load(f)

    path = output_dir / "Table_S6_graph_metrics.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Protein", "Degree", "Degree_Centrality",
            "Betweenness_Centrality", "Closeness_Centrality"
        ])
        for prot in data["top_proteinas_centralidade"]:
            writer.writerow([
                prot["label"],
                prot["grau"],
                round(prot["degree_centrality"], 4),
                round(prot["betweenness"], 4),
                round(prot["closeness"], 4)
            ])

    logger.info(f"Table S6 salva: {path}")
    return path


def gerar_table_s7_targets(targets_path: Path, output_dir: Path) -> Path:
    """Table S7: Top 50 aging targets with Ensembl IDs."""
    with open(targets_path) as f:
        targets = json.load(f)

    path = output_dir / "Table_S7_aging_targets.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Rank", "Symbol", "Full_Name", "Ensembl_ID",
            "Papers_Mentioning", "Total_Mentions", "Pathway", "Source"
        ])
        for t in targets:
            writer.writerow([
                t["rank_original"],
                t["symbol"],
                t["nome"],
                t["ensembl_id"],
                t["papers_mencionando"],
                t["mencoes_totais"],
                t.get("via", ""),
                t["fonte"]
            ])

    logger.info(f"Table S7 salva: {path}")
    return path


def gerar_todas_tabelas(data_dir: str | Path, output_dir: str | Path) -> list[Path]:
    """Gera todas as tabelas suplementares."""
    data_dir = Path(data_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    validation_files = sorted(data_dir.glob("validation_results_*.json"))
    metrics_files = sorted(data_dir.glob("graph_metrics_*.json"))
    targets_files = sorted(data_dir.glob("top50_alvos_consolidados_*.json"))

    if not validation_files:
        raise FileNotFoundError(f"Nenhum validation_results_*.json em {data_dir}")

    validation_path = validation_files[-1]
    metrics_path = metrics_files[-1] if metrics_files else None
    targets_path = targets_files[-1] if targets_files else None

    tabelas = []
    tabelas.append(gerar_table_s3_bootstrap(validation_path, output_dir))
    tabelas.append(gerar_table_s4_ablation(validation_path, output_dir))
    tabelas.append(gerar_table_s5_sensitivity(validation_path, output_dir))

    if metrics_path:
        tabelas.append(gerar_table_s6_graph_metrics(metrics_path, output_dir))
    if targets_path:
        tabelas.append(gerar_table_s7_targets(targets_path, output_dir))

    logger.info(f"Total: {len(tabelas)} tabelas suplementares geradas")
    return tabelas


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data/processed"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "outputs/supplementary"
    gerar_todas_tabelas(data_dir, output_dir)
