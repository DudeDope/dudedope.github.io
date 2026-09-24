"""Compile the portfolio CV from its custom LaTeX template.

The source template and its logo live in assets/cv. The generated PDF is
written to the stable public path already used by the website.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


def render(source: Path, output: Path) -> None:
    """Compile source twice with pdfLaTeX and copy the resulting PDF."""

    compiler = shutil.which("pdflatex")
    if compiler is None:
        raise SystemExit("pdflatex is required to render the CV.")

    source = source.resolve()
    logo = source.with_name("ISIlogo-blue.png")
    if not source.is_file():
        raise SystemExit(f"CV source not found: {source}")
    if not logo.is_file():
        raise SystemExit(f"CV logo not found: {logo}")

    with tempfile.TemporaryDirectory(prefix="portfolio_cv_") as temporary:
        build_dir = Path(temporary)
        build_source = build_dir / source.name
        shutil.copy2(source, build_source)
        shutil.copy2(logo, build_dir / logo.name)

        command = [
            compiler,
            "-interaction=nonstopmode",
            "-halt-on-error",
            build_source.name,
        ]
        for _ in range(2):
            subprocess.run(command, cwd=build_dir, check=True)

        rendered_pdf = build_source.with_suffix(".pdf")
        output = output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(rendered_pdf, output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("assets/cv/Aditya_Aryan_CV.tex"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("assets/rendercv/rendercv_output/Aditya_Aryan_CV.pdf"),
    )
    args = parser.parse_args()
    render(args.source, args.output)


if __name__ == "__main__":
    main()
