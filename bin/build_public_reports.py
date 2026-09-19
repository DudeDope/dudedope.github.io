"""Build redacted public editions of portfolio project reports.

The source PDFs are intentionally not committed because their title pages contain
student identifiers. Pass a directory containing the four ``*-report.pdf`` files.
The script creates clean attribution pages and copies only the non-identifying body
pages into the deployable ``*-public.pdf`` files.
"""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


REPORTS = {
    "sequential-testing": {
        "source": "sequential-testing-report.pdf",
        "title": "Optimal Stopping in a Finite Reward-Sampling Game",
        "subtitle": "Originally submitted as “Sequential Testing”",
        "authors": ["Abhirup Mistry", "Aditya Aryan", "Deep Jayesh Hariya", "Drishti Singla", "Mrittika Giri", "Nandita Sen"],
        "supervisor": "Dr. Arnab Chakraborty",
        "course": "Statistical Methods II · Indian Statistical Institute, Kolkata",
        "date": "27 March 2024",
        "first_body_page": 1,
    },
    "audio-denoising": {
        "source": "audio-denoising-report.pdf",
        "title": "Variance-Gated Suppression of Noise-Dominated Audio",
        "subtitle": "Originally submitted as “De-noising Audio”",
        "authors": [
            "Adeesh Ajay Devasthale",
            "Aditya Aryan",
            "Deep Jayesh Hariya",
            "Nishant Lamboria",
            "Sauparna Kar",
            "Srijan Bhowmick",
        ],
        "supervisor": "Dr. Arnab Chakraborty",
        "course": "Statistical Methods I · Indian Statistical Institute, Kolkata",
        "date": "27 November 2023",
        "first_body_page": 1,
    },
    "football-elo-logistic": {
        "source": "football-elo-logistic-report.pdf",
        "title": "Elo-Based Football Probability Modelling",
        "subtitle": "Original course report with a retrospective betting simulation",
        "authors": ["Aditya Aryan"],
        "supervisor": "Dr. Ayanendranath Basu",
        "course": "Statistical Methods IV · Indian Statistical Institute, Kolkata",
        "date": "May 2025",
        "first_body_page": 1,
    },
    "copula-air-pollution": {
        "source": "copula-air-pollution-report.pdf",
        "title": "Copula Modelling of Air-Pollution Episodes",
        "subtitle": "A bivariate study of duration and cumulative severity in Bengaluru",
        "authors": ["Amritanshu Aditya", "Ayush Aryan", "Aditya Aryan"],
        "supervisor": "Prof. Shyamal Krishna De",
        "course": "Applied Statistics Unit · Indian Statistical Institute, Kolkata",
        "date": "April 2026",
        # The original title/abstract page also begins the contents, whose continuation
        # occupies page 2. Start at the first substantive section instead.
        "first_body_page": 2,
    },
}


def cover_page(metadata: dict[str, object]) -> PdfReader:
    buffer = BytesIO()
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "PortfolioTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=29,
        textColor=HexColor("#1d2024"),
        spaceAfter=10 * mm,
    )
    subtitle = ParagraphStyle(
        "PortfolioSubtitle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=11,
        leading=17,
        textColor=HexColor("#4f5964"),
        spaceAfter=18 * mm,
    )
    label = ParagraphStyle(
        "PortfolioLabel",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=12,
        textColor=HexColor("#426b8c"),
        spaceAfter=2 * mm,
    )
    body = ParagraphStyle(
        "PortfolioBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=16,
        textColor=HexColor("#1d2024"),
        spaceAfter=9 * mm,
    )

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=28 * mm,
        rightMargin=28 * mm,
        topMargin=34 * mm,
        bottomMargin=28 * mm,
        title=str(metadata["title"]),
        author=", ".join(metadata["authors"]),
    )
    author_lines = "<br/>".join(metadata["authors"])
    story = [
        Paragraph(str(metadata["title"]), title),
        Paragraph(str(metadata["subtitle"]), subtitle),
        Paragraph("AUTHORS", label),
        Paragraph(author_lines, body),
        Paragraph("SUPERVISOR", label),
        Paragraph(str(metadata["supervisor"]), body),
        Paragraph("COURSE / UNIT", label),
        Paragraph(str(metadata["course"]), body),
        Paragraph("ORIGINAL REPORT DATE", label),
        Paragraph(str(metadata["date"]), body),
        Spacer(1, 11 * mm),
        Paragraph("PUBLIC PORTFOLIO EDITION", label),
        Paragraph(
            "September 2026 · Student identifiers removed; substantive report pages otherwise retained from the original submission.",
            body,
        ),
    ]
    document.build(story)
    buffer.seek(0)
    return PdfReader(buffer)


def build_report(source_dir: Path, output_dir: Path, stem: str, metadata: dict[str, object]) -> None:
    source = source_dir / str(metadata["source"])
    if not source.exists():
        raise FileNotFoundError(f"Missing source report: {source}")

    reader = PdfReader(source)
    writer = PdfWriter()
    writer.add_page(cover_page(metadata).pages[0])
    for page in reader.pages[int(metadata["first_body_page"]) :]:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": str(metadata["title"]),
            "/Author": ", ".join(metadata["authors"]),
            "/Subject": "Redacted public portfolio edition",
        }
    )

    destination = output_dir / f"{stem}-public.pdf"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as stream:
        writer.write(stream)
    print(f"Built {destination} ({len(writer.pages)} pages)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("assets/pdf/projects"))
    args = parser.parse_args()
    for stem, metadata in REPORTS.items():
        build_report(args.source_dir, args.output_dir, stem, metadata)


if __name__ == "__main__":
    main()
