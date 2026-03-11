"""Gera PDF do preprint com figuras embutidas para bioRxiv."""

import base64
import re
from pathlib import Path

def embed_figures_in_md(md_text: str, figures_dir: Path) -> str:
    """Substitui referencias a figuras por imagens base64 inline."""
    # Mapa de figuras
    fig_map = {
        "Fig. 1": "fig1_pipeline_overview.png",
        "Fig. 2": "fig2_top20_ranking.png",
        "Fig. 3": "fig3_bootstrap_stability.png",
        "Fig. 4": "fig4_ablation_study.png",
        "Fig. 5": "fig5_sensitivity_analysis.png",
    }
    return md_text, fig_map


def create_preprint_md(source_md: Path, figures_dir: Path, output_md: Path) -> None:
    """Cria versao do manuscrito com figuras inseridas apos cada secao relevante."""
    text = source_md.read_text(encoding="utf-8")

    # Remover a linha final de target journal
    text = re.sub(r"\n---\n\n\*Manuscript prepared.*$", "", text, flags=re.DOTALL)

    # Inserir figuras no corpo do texto, logo apos as legendas
    fig_files = {
        "fig1_pipeline_overview.png": "Fig. 1",
        "fig2_top20_ranking.png": "Fig. 2",
        "fig3_top20_ranking.png": "Fig. 2",
        "fig3_bootstrap_stability.png": "Fig. 3",
        "fig4_ablation_study.png": "Fig. 4",
        "fig5_sensitivity_analysis.png": "Fig. 5",
    }

    # Substituir a secao "Figure Legends" por figuras embutidas
    legend_section = re.search(r"## Figure Legends\n\n(.+?)(?=\n---|\n## )", text, re.DOTALL)
    if legend_section:
        legends_text = legend_section.group(1)
        new_figures_section = "## Figures\n\n"

        for fname, label in [
            ("fig1_pipeline_overview.png", "Fig. 1"),
            ("fig2_top20_ranking.png", "Fig. 2"),
            ("fig3_bootstrap_stability.png", "Fig. 3"),
            ("fig4_ablation_study.png", "Fig. 4"),
            ("fig5_sensitivity_analysis.png", "Fig. 5"),
        ]:
            fpath = figures_dir / fname
            if fpath.exists():
                # Extrair legenda correspondente
                pattern = rf"\*\*{re.escape(label)}\*\*\s+(.+?)(?=\n\n\*\*Fig\.|\Z)"
                match = re.search(pattern, legends_text, re.DOTALL)
                caption = match.group(1).strip() if match else ""
                new_figures_section += f"![{label}]({fpath.as_posix()})\n\n"
                new_figures_section += f"**{label}.** {caption}\n\n"

        text = text[:legend_section.start()] + new_figures_section + text[legend_section.end():]

    output_md.write_text(text, encoding="utf-8")
    print(f"Preprint MD salvo: {output_md}")


def md_to_pdf_via_html(md_path: Path, pdf_path: Path, figures_dir: Path) -> None:
    """Converte MD -> HTML -> PDF com figuras embutidas."""
    import pypandoc

    # Converter MD para HTML
    html_body = pypandoc.convert_file(
        str(md_path), "html",
        extra_args=["--standalone", "--metadata", "title=Discovery Engine Preprint"]
    )

    # Embutir imagens como base64 no HTML
    def replace_img_src(match: re.Match) -> str:
        src = match.group(1)
        # Tentar resolver o caminho
        img_path = Path(src)
        if not img_path.exists():
            img_path = figures_dir / img_path.name
        if not img_path.exists():
            return match.group(0)

        data = img_path.read_bytes()
        b64 = base64.b64encode(data).decode()
        return f'src="data:image/png;base64,{b64}"'

    html_body = re.sub(r'src="([^"]+)"', replace_img_src, html_body)

    # Adicionar CSS para formatacao academica
    css = """
    <style>
        @page { size: letter; margin: 2.5cm; }
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 11pt;
            line-height: 1.5;
            max-width: 18cm;
            margin: 0 auto;
            color: #000;
        }
        h1 { font-size: 16pt; text-align: center; margin-bottom: 0.5em; }
        h2 { font-size: 13pt; margin-top: 1.5em; }
        h3 { font-size: 11pt; margin-top: 1em; }
        table {
            border-collapse: collapse;
            width: 100%;
            font-size: 9pt;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #999;
            padding: 4px 8px;
            text-align: left;
        }
        th { background-color: #f0f0f0; font-weight: bold; }
        img { max-width: 100%; height: auto; margin: 1em 0; }
        p { margin: 0.5em 0; }
        sup { font-size: 0.7em; }
    </style>
    """
    html_body = html_body.replace("</head>", css + "</head>")

    # Gerar PDF
    from weasyprint import HTML
    HTML(string=html_body).write_pdf(str(pdf_path))
    print(f"PDF gerado: {pdf_path} ({pdf_path.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    source = base / "submission" / "PAPER_GEROSCIENCE_SUBMISSION.md"
    figures = base / "outputs" / "figures"
    out_dir = base / "submission" / "submission_package"

    # Passo 1: Criar MD com figuras referenciadas
    preprint_md = out_dir / "discovery_engine_preprint.md"
    create_preprint_md(source, figures, preprint_md)

    # Passo 2: Gerar PDF
    preprint_pdf = out_dir / "discovery_engine_preprint.pdf"
    md_to_pdf_via_html(preprint_md, preprint_pdf, figures)
