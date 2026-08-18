"""Validate the generated academic portfolio without network requests."""

from __future__ import annotations

import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path("_site").resolve()
BASEURL = os.environ.get("PORTFOLIO_BASEURL", "/al-folio").rstrip("/")
EXPECTED_ROUTES = {
    "/",
    "/about/",
    "/cv/",
    "/notes/",
    "/notes/design-and-analysis-of-algorithms/",
    "/notes/design-and-analysis-of-algorithms/formula-sheet/",
    "/notes/design-and-analysis-of-algorithms/lecture-01-algorithmic-foundations/",
    "/notes/design-and-analysis-of-algorithms/lecture-02-minimum-enclosing-circles/",
    "/notes/design-and-analysis-of-algorithms/lecture-03-divide-and-conquer-recurrences/",
    "/notes/design-and-analysis-of-algorithms/lecture-04-simultaneous-minimum-maximum/",
    "/notes/design-and-analysis-of-algorithms/lecture-05-deterministic-linear-selection/",
    "/notes/design-and-analysis-of-algorithms/lecture-06-binary-search-rotated-arrays/",
    "/notes/design-and-analysis-of-algorithms/lecture-07-binary-search-trees/",
    "/notes/design-and-analysis-of-algorithms/lecture-08-height-balanced-search-trees/",
    "/notes/design-and-analysis-of-algorithms/lecture-09-consolidated-algorithm-review/",
    "/notes/parametric-inference/",
    "/notes/parametric-inference/formula-sheet/",
    "/notes/parametric-inference/lecture-01-point-estimation-risk-mse/",
    "/notes/parametric-inference/lecture-02-unbiased-estimation-umvue-crlb/",
    "/notes/parametric-inference/lecture-03-existence-uniqueness-unbiased-estimators/",
    "/notes/parametric-inference/lecture-04-sufficiency-rao-blackwell-ancillarity/",
    "/notes/parametric-inference/lecture-05-completeness-exponential-families-basu/",
    "/notes/parametric-inference/lecture-06-lehmann-scheffe-umvue-consistency/",
    "/notes/parametric-inference/lecture-07-hypothesis-testing-likelihood-ratio/",
    "/notes/parametric-inference/lecture-08-bayesian-inference-bayes-risk/",
    "/notes/sample-surveys/",
    "/notes/sample-surveys/formula-sheet/",
    "/notes/sample-surveys/lecture-01-foundations-and-representativeness/",
    "/notes/sample-surveys/lecture-02-finite-population-and-srs/",
    "/notes/sample-surveys/lecture-03-design-based-estimation/",
    "/notes/sample-surveys/lecture-04-confidence-intervals-and-sample-size/",
    "/projects/",
    "/projects/audio-denoising/",
    "/projects/copula-air-pollution/",
    "/projects/football-probability/",
    "/projects/sequential-testing/",
    "/projects/stein-shrinkage/",
    "/publications/",
    "/research/",
    "/research/battery-dispatch/",
    "/research/battery-life/",
    "/research/em-convergence/",
    "/research/medical-vlm/",
}

EXPECTED_PROJECT_ASSETS = {
    "assets/img/projects/audio/amplitude-variance.png",
    "assets/img/projects/audio/denoised-waveform.png",
    "assets/img/projects/copula/marginals-joint.png",
    "assets/img/projects/copula/pseudo-observations.png",
    "assets/img/projects/football/elo-top-five.png",
    "assets/img/projects/sequential/cutoff-growth.png",
}


class PortfolioHTMLParser(HTMLParser):
    """Collect document metadata, links, and JSON-LD blocks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.description = ""
        self.canonical = ""
        self.json_ld: list[str] = []
        self.links: list[str] = []
        self.title_parts: list[str] = []
        self._in_title = False
        self._in_json_ld = False
        self._json_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and attributes.get("name") == "description":
            self.description = attributes.get("content", "")
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href", "")
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_parts = []
        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.links.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_parts))
            self._in_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)
        if self._in_json_ld:
            self._json_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def route_for(path: Path) -> str:
    relative = path.relative_to(SITE).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return f"/{relative.removesuffix('index.html')}"
    return f"/{relative}"


def local_target(source: Path, url: str) -> Path | None:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or url.startswith(("mailto:", "tel:", "data:", "javascript:", "#")):
        return None

    path = unquote(parts.path)
    if not path:
        return None
    if BASEURL and path.startswith(BASEURL):
        path = path.removeprefix(BASEURL)
    elif BASEURL and path.startswith("/"):
        raise AssertionError(f"{source}: root-relative URL does not use {BASEURL}: {url}")
    else:
        current_route = route_for(source)
        route_parent = Path(current_route.removeprefix("/")).parent
        path = (route_parent / path).as_posix()

    candidate = SITE / path.lstrip("/")
    if path.endswith("/"):
        return candidate / "index.html"
    if candidate.is_dir():
        return candidate / "index.html"
    return candidate


def main() -> int:
    if not SITE.is_dir():
        raise AssertionError("Build the Jekyll site before running validation.")

    html_files = sorted(SITE.rglob("*.html"))
    routes = {route_for(path) for path in html_files}
    missing_routes = EXPECTED_ROUTES - routes
    assert not missing_routes, f"Missing routes: {sorted(missing_routes)}"

    titles: dict[str, Path] = {}
    checked_links = 0
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        parser = PortfolioHTMLParser()
        parser.feed(text)

        assert parser.title, f"{path}: missing title"
        assert parser.title not in titles, f"{path}: duplicate title also used by {titles.get(parser.title)}"
        titles[parser.title] = path
        assert parser.description, f"{path}: missing meta description"
        assert parser.canonical, f"{path}: missing canonical URL"

        for block in parser.json_ld:
            json.loads(block)

        for url in parser.links:
            target = local_target(path, url)
            if target is None:
                continue
            checked_links += 1
            assert target.exists(), f"{path}: unresolved internal URL {url} -> {target}"

    generated_text = "\n".join(path.read_text(encoding="utf-8") for path in html_files)
    assert not re.search(r"Albert Einstein|The Godfather|Lorem ipsum", generated_text, re.IGNORECASE)
    assert '"@type": "Person"' in (SITE / "index.html").read_text(encoding="utf-8")
    assert '"@type": "ResearchProject"' in (SITE / "research/em-convergence/index.html").read_text(encoding="utf-8")

    search_data = (SITE / "index.html").read_text(encoding="utf-8")
    assert 'section: "Research"' in search_data
    assert 'section: "Projects"' in search_data

    stylesheet = (SITE / "assets/css/main.css").read_text(encoding="utf-8")
    assert "--aa-font-prose" in stylesheet
    assert "--aa-reading-width" in stylesheet

    assert (SITE / "feed.xml").is_file()
    assert (SITE / "sitemap.xml").is_file()
    for asset in EXPECTED_PROJECT_ASSETS:
        assert (SITE / asset).is_file(), f"Missing published project asset: {asset}"
    assert not (SITE / "assets/pdf/projects").exists(), "Unsanitised source reports were published"
    for excluded in ("assets/audio", "assets/html", "assets/jupyter", "assets/plotly", "assets/video", "test"):
        assert not (SITE / excluded).exists(), f"Excluded demo path was published: {excluded}"

    print(f"Portfolio validation passed: {len(html_files)} HTML files, {checked_links} internal URLs, {len(titles)} unique titles.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as error:
        print(f"Portfolio validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
