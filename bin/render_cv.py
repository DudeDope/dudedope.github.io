"""Render the site CV while preserving al-folio's legacy HTML fields.

The CV plugin reads ``label`` and ``summary`` from ``_data/cv.yml``. RenderCV
2.x instead accepts ``headline`` and section entries, so this script creates a
temporary compatible document before invoking RenderCV. The canonical content
remains in one checked-in YAML file.
"""

from __future__ import annotations

import argparse
import copy
import re
import subprocess
import tempfile
from pathlib import Path

import yaml


MONTHS = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12",
}


def rendercv_date(value: object) -> object:
    """Convert the site's readable ``Mon YYYY`` dates for RenderCV 2.x."""

    if not isinstance(value, str):
        return value
    match = re.fullmatch(r"([A-Z][a-z]{2}) (\d{4})", value.strip())
    if not match or match.group(1) not in MONTHS:
        return value
    return f"{match.group(2)}-{MONTHS[match.group(1)]}"


def render(source: Path, settings: Path) -> None:
    document = yaml.safe_load(source.read_text(encoding="utf-8"))
    cv = copy.deepcopy(document["cv"])

    label = cv.pop("label", None)
    summary = cv.pop("summary", None)
    image = cv.pop("image", None)
    if label:
        cv["headline"] = label
    if image:
        cv["photo"] = image

    sections = cv.get("sections", {})
    if "Experience" in sections:
        for entry in sections["Experience"]:
            for key in ("start_date", "end_date"):
                if key in entry:
                    entry[key] = rendercv_date(entry[key])
    if "Projects" in sections:
        rendered_projects = []
        for entry in sections["Projects"]:
            rendered_entry = dict(entry)
            url = rendered_entry.pop("url", None)
            if url:
                rendered_entry["name"] = f"[{rendered_entry['name']}]({url})"
            rendered_projects.append(rendered_entry)
        sections["Projects"] = rendered_projects
    if "Skills" in sections:
        sections["Skills"] = [
            {"label": entry["name"], "details": ", ".join(entry.get("keywords", []))}
            for entry in sections["Skills"]
        ]
    if "Honors and Awards" in sections:
        for entry in sections["Honors and Awards"]:
            entry.pop("title", None)
    if summary:
        cv["sections"] = {"Profile": [{"bullet": summary.strip()}], **sections}

    payload = {"cv": cv}
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", prefix="rendercv_", dir=source.parent, encoding="utf-8", delete=False
    ) as temporary:
        yaml.safe_dump(payload, temporary, sort_keys=False, allow_unicode=True)
        temporary_path = Path(temporary.name)

    try:
        subprocess.run(
            ["rendercv", "render", str(temporary_path), "--settings", str(settings.resolve()), "--quiet"],
            check=True,
        )
    finally:
        temporary_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("_data/cv.yml"))
    parser.add_argument("--settings", type=Path, default=Path("assets/rendercv/settings.yaml"))
    args = parser.parse_args()
    render(args.source, args.settings)


if __name__ == "__main__":
    main()
