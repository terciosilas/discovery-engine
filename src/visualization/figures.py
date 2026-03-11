"""Geracao de figuras de qualidade para publicacao.

Gera 5 figuras principais para o paper:
- Fig 1: Pipeline overview (flowchart)
- Fig 2: Top 20 candidate ranking (horizontal bar)
- Fig 3: Bootstrap stability (error bars)
- Fig 4: Ablation study (heatmap)
- Fig 5: Sensitivity analysis (grouped bar)

Uso:
    python -m src.visualization.figures data/processed/ outputs/figures/
"""

import json
import logging
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

logger = logging.getLogger(__name__)

# Estilo para publicacao
STYLE = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
}

# Cores
COR_GEROPROTETOR = "#2196F3"  # azul
COR_NOVO = "#FF9800"  # laranja
COR_DESTAQUE = "#E91E63"  # rosa
COR_GRID = "#E0E0E0"


def _aplicar_estilo() -> None:
    """Aplica estilo de publicacao."""
    plt.rcParams.update(STYLE)


def gerar_fig1_pipeline(output_dir: Path) -> Path:
    """Fig 1: Pipeline overview -- flowchart dos 4 blocos."""
    _aplicar_estilo()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    blocos = [
        (1.5, 5.5, "Phase 1\nLiterature\nCollection", "#E3F2FD",
         "PubMed: 376 papers\nSemantic Scholar\nUnpaywall (OA)"),
        (4.0, 5.5, "Phase 2A\nTarget\nExtraction", "#E8F5E9",
         "GenAge: 307 genes\nRegex NER\n50 targets"),
        (6.5, 5.5, "Phase 2B\nDrug-Target\nLinking", "#FFF3E0",
         "Open Targets\nChEMBL\nDrugAge"),
        (1.5, 2.5, "Phase 2C\nKnowledge\nGraph", "#F3E5F5",
         "479 nodes\n898 edges\n51 communities"),
        (4.0, 2.5, "Phase 2D\nCandidate\nScoring", "#FFEBEE",
         "6 features\n162 candidates\nWeighted sum"),
        (6.5, 2.5, "Phase 3\nValidation", "#E0F7FA",
         "Bootstrap 1000x\nAblation study\nNeg. controls"),
    ]

    for x, y, titulo, cor, detalhe in blocos:
        rect = mpatches.FancyBboxPatch(
            (x - 0.9, y - 0.8), 1.8, 1.6,
            boxstyle="round,pad=0.1", facecolor=cor,
            edgecolor="#424242", linewidth=1.2
        )
        ax.add_patch(rect)
        ax.text(x, y + 0.3, titulo, ha="center", va="center",
                fontsize=9, fontweight="bold")
        ax.text(x, y - 0.35, detalhe, ha="center", va="center",
                fontsize=6.5, color="#616161")

    # Setas horizontais (linha superior)
    for x_start in [2.4, 4.9]:
        ax.annotate("", xy=(x_start + 0.7, 5.5), xytext=(x_start, 5.5),
                     arrowprops=dict(arrowstyle="->", color="#424242", lw=1.5))

    # Seta vertical (Open Targets -> Grafo)
    ax.annotate("", xy=(1.5, 3.3), xytext=(1.5, 4.7),
                arrowprops=dict(arrowstyle="->", color="#424242", lw=1.5))
    # Setas horizontais (linha inferior)
    for x_start in [2.4, 4.9]:
        ax.annotate("", xy=(x_start + 0.7, 2.5), xytext=(x_start, 2.5),
                     arrowprops=dict(arrowstyle="->", color="#424242", lw=1.5))

    # Seta diagonal
    ax.annotate("", xy=(4.0, 3.3), xytext=(6.5, 4.7),
                arrowprops=dict(arrowstyle="->", color="#424242",
                                lw=1.5, linestyle="--"))

    # Resultado final
    rect_final = mpatches.FancyBboxPatch(
        (7.8, 2.0), 1.8, 1.0,
        boxstyle="round,pad=0.1", facecolor="#C8E6C9",
        edgecolor="#2E7D32", linewidth=2.0
    )
    ax.add_patch(rect_final)
    ax.text(8.7, 2.5, "Ranked\nCandidates\n(n=162)", ha="center", va="center",
            fontsize=9, fontweight="bold", color="#1B5E20")
    ax.annotate("", xy=(7.8, 2.5), xytext=(7.4, 2.5),
                arrowprops=dict(arrowstyle="->", color="#2E7D32", lw=2.0))

    ax.set_title("Figure 1. Discovery Engine Pipeline Overview",
                 fontsize=13, fontweight="bold", pad=15)

    path = output_dir / "fig1_pipeline_overview.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    logger.info(f"Fig 1 salva: {path}")
    return path


def gerar_fig2_ranking(ranked_path: Path, output_dir: Path) -> Path:
    """Fig 2: Top 20 candidate ranking -- horizontal bar chart."""
    _aplicar_estilo()

    with open(ranked_path) as f:
        ranked = json.load(f)

    top20 = ranked[:20]
    top20.reverse()  # para plot de baixo para cima

    nomes = [c["nome"].title() for c in top20]
    scores = [c["score_total"] for c in top20]
    is_gero = [c.get("geroprotetor_conhecido", False) for c in top20]
    cores = [COR_GEROPROTETOR if g else COR_NOVO for g in is_gero]

    fig, ax = plt.subplots(figsize=(8, 7))
    bars = ax.barh(range(len(nomes)), scores, color=cores, edgecolor="white",
                   linewidth=0.5, height=0.7)

    ax.set_yticks(range(len(nomes)))
    ax.set_yticklabels(nomes)
    ax.set_xlabel("Composite Score")
    ax.set_xlim(0, 0.6)
    ax.axvline(x=0.4, color=COR_GRID, linestyle="--", linewidth=0.8, alpha=0.7)

    # Rank labels
    for i, (score, bar) in enumerate(zip(scores, bars)):
        rank = 20 - i
        ax.text(score + 0.005, i, f"#{rank}", va="center", fontsize=7,
                color="#424242")

    # Legenda
    patch_gero = mpatches.Patch(color=COR_GEROPROTETOR, label="Known geroprotector")
    patch_novo = mpatches.Patch(color=COR_NOVO, label="Novel candidate")
    ax.legend(handles=[patch_gero, patch_novo], loc="lower right", frameon=True)

    ax.set_title("Figure 2. Top 20 Geroprotective Compound Candidates",
                 fontsize=12, fontweight="bold")
    ax.grid(axis="x", alpha=0.3)

    path = output_dir / "fig2_top20_ranking.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    logger.info(f"Fig 2 salva: {path}")
    return path


def gerar_fig3_bootstrap(validation_path: Path, output_dir: Path) -> Path:
    """Fig 3: Bootstrap stability -- error bar chart for top 20."""
    _aplicar_estilo()

    with open(validation_path) as f:
        data = json.load(f)

    bootstrap = data["bootstrap"]["top20_estavel"]

    nomes = []
    medias = []
    stds = []
    mins = []
    maxs = []
    for nome, stats in bootstrap:
        nomes.append(nome.title())
        medias.append(stats["rank_medio"])
        stds.append(stats["rank_std"])
        mins.append(stats["rank_min"])
        maxs.append(stats["rank_max"])

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(nomes))
    errs_low = [m - mn for m, mn in zip(medias, mins)]
    errs_high = [mx - m for m, mx in zip(medias, maxs)]

    ax.errorbar(x, medias, yerr=[errs_low, errs_high], fmt="o",
                color=COR_GEROPROTETOR, capsize=4, capthick=1.2,
                markersize=6, linewidth=1.2)

    # Destacar rapamycin e metformin
    for i, nome in enumerate(nomes):
        if nome.lower() in ("rapamycin", "metformin"):
            ax.plot(i, medias[i], "o", color=COR_DESTAQUE, markersize=10,
                    zorder=5)
            ax.annotate(nome, (i, medias[i]),
                        textcoords="offset points", xytext=(10, -5),
                        fontsize=8, fontweight="bold", color=COR_DESTAQUE)

    ax.set_xticks(x)
    ax.set_xticklabels(nomes, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Mean Rank (1,000 bootstrap iterations)")
    ax.set_xlabel("Compound")
    ax.invert_yaxis()
    ax.set_title("Figure 3. Bootstrap Ranking Stability (n=1,000, 80% resampling)",
                 fontsize=12, fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    ax.axhline(y=10, color=COR_GRID, linestyle="--", linewidth=0.8, alpha=0.7,
               label="Top 10 threshold")
    ax.legend(loc="lower right")

    path = output_dir / "fig3_bootstrap_stability.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    logger.info(f"Fig 3 salva: {path}")
    return path


def gerar_fig4_ablation(validation_path: Path, output_dir: Path) -> Path:
    """Fig 4: Ablation study -- heatmap de impacto."""
    _aplicar_estilo()

    with open(validation_path) as f:
        data = json.load(f)

    ablation = data["ablation"]
    features = list(ablation.keys())
    labels = {
        "fase_clinica": "Clinical Phase",
        "n_alvos_envelhecimento": "Aging Targets",
        "lifespan_efeito": "Lifespan Effect",
        "pchembl": "Binding Potency",
        "literatura": "Literature",
        "centralidade_grafo": "Graph Centrality"
    }

    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Painel A: Rank de controles positivos
    rap_ranks = [ablation[f]["rapamycin_rank"] for f in features]
    met_ranks = [ablation[f]["metformin_rank"] for f in features]
    feat_labels = [labels.get(f, f) for f in features]

    y = np.arange(len(features))
    width = 0.35

    axes[0].barh(y - width / 2, rap_ranks, width, label="Rapamycin",
                 color=COR_GEROPROTETOR, edgecolor="white")
    axes[0].barh(y + width / 2, met_ranks, width, label="Metformin",
                 color=COR_NOVO, edgecolor="white")
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(feat_labels)
    axes[0].set_xlabel("Rank after feature removal")
    axes[0].axvline(x=10, color=COR_DESTAQUE, linestyle="--", linewidth=1,
                    label="Top 10 threshold")
    axes[0].legend(loc="lower right", fontsize=8)
    axes[0].set_title("A. Positive Control Ranks", fontweight="bold")
    axes[0].grid(axis="x", alpha=0.3)

    # Painel B: Mudanca media de rank
    avg_changes = [ablation[f]["avg_rank_change"] for f in features]
    controle_ok = [ablation[f]["controle_ok"] for f in features]
    cores = [("#4CAF50" if ok else "#F44336") for ok in controle_ok]

    axes[1].barh(y, avg_changes, color=cores, edgecolor="white", height=0.6)
    axes[1].set_xlabel("Avg. rank change across all candidates")
    axes[1].set_title("B. Feature Impact", fontweight="bold")
    axes[1].grid(axis="x", alpha=0.3)

    # Legenda painel B
    patch_ok = mpatches.Patch(color="#4CAF50", label="Controls maintained")
    patch_fail = mpatches.Patch(color="#F44336", label="Controls disrupted")
    axes[1].legend(handles=[patch_ok, patch_fail], loc="lower right", fontsize=8)

    fig.suptitle("Figure 4. Ablation Study: Feature Importance",
                 fontsize=12, fontweight="bold", y=1.02)
    fig.tight_layout()

    path = output_dir / "fig4_ablation_study.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    logger.info(f"Fig 4 salva: {path}")
    return path


def gerar_fig5_sensibilidade(validation_path: Path, output_dir: Path) -> Path:
    """Fig 5: Sensitivity analysis -- grouped bar para 4 compostos em 5 configs."""
    _aplicar_estilo()

    with open(validation_path) as f:
        data = json.load(f)

    configs = data["sensibilidade"]["configuracoes"]
    config_names = [c["configuracao"].replace("_", "\n") for c in configs]
    compostos = ["rapamycin", "metformin", "spermidine", "resveratrol"]
    cores_comp = [COR_GEROPROTETOR, COR_NOVO, "#9C27B0", "#4CAF50"]

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(configs))
    width = 0.18

    for i, (comp, cor) in enumerate(zip(compostos, cores_comp)):
        ranks = [c[f"{comp}_rank"] for c in configs]
        offset = (i - 1.5) * width
        bars = ax.bar(x + offset, ranks, width, label=comp.title(),
                      color=cor, edgecolor="white", linewidth=0.5)
        # Valor no topo
        for bar, rank in zip(bars, ranks):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f"#{rank}", ha="center", va="bottom", fontsize=7)

    ax.set_xticks(x)
    ax.set_xticklabels(config_names, fontsize=8)
    ax.set_ylabel("Rank")
    ax.set_xlabel("Weight Configuration")
    ax.axhline(y=10, color=COR_DESTAQUE, linestyle="--", linewidth=1,
               alpha=0.7, label="Top 10 threshold")
    ax.legend(loc="upper left", fontsize=8, ncol=3)
    ax.set_title("Figure 5. Sensitivity Analysis: Rank Stability Across Weight Configurations",
                 fontsize=11, fontweight="bold")
    ax.grid(axis="y", alpha=0.3)

    # Y invertido nao -- rank menor = melhor, vai de cima pra baixo
    ax.set_ylim(0, max(80, max(c.get("spermidine_rank", 1) for c in configs) + 5))

    path = output_dir / "fig5_sensitivity_analysis.png"
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    logger.info(f"Fig 5 salva: {path}")
    return path


def gerar_todas_figuras(data_dir: str | Path, output_dir: str | Path) -> list[Path]:
    """Gera todas as figuras para publicacao.

    Args:
        data_dir: Diretorio com JSONs processados.
        output_dir: Diretorio de saida para PNGs.

    Returns:
        Lista de caminhos das figuras geradas.
    """
    data_dir = Path(data_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Encontrar arquivos mais recentes
    ranked_files = sorted(data_dir.glob("ranked_candidates_*.json"))
    validation_files = sorted(data_dir.glob("validation_results_*.json"))

    if not ranked_files:
        raise FileNotFoundError(f"Nenhum ranked_candidates_*.json em {data_dir}")
    if not validation_files:
        raise FileNotFoundError(f"Nenhum validation_results_*.json em {data_dir}")

    ranked_path = ranked_files[-1]
    validation_path = validation_files[-1]

    logger.info(f"Usando ranked: {ranked_path.name}")
    logger.info(f"Usando validation: {validation_path.name}")

    figuras = []
    figuras.append(gerar_fig1_pipeline(output_dir))
    figuras.append(gerar_fig2_ranking(ranked_path, output_dir))
    figuras.append(gerar_fig3_bootstrap(validation_path, output_dir))
    figuras.append(gerar_fig4_ablation(validation_path, output_dir))
    figuras.append(gerar_fig5_sensibilidade(validation_path, output_dir))

    logger.info(f"Total: {len(figuras)} figuras geradas em {output_dir}")
    return figuras


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data/processed"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "outputs/figures"
    gerar_todas_figuras(data_dir, output_dir)
