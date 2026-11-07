"""Render curated project data into the committed static page (Python 3.9+)."""

import argparse
import html
import json
from pathlib import Path
import string
import sys
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
BEGIN = "        <!-- BEGIN GENERATED PROJECTS -->\n"
END = "        <!-- END GENERATED PROJECTS -->\n"
PROJECT_IDS = {"savvit": "p1-title", "search": "p2-title", "farm": "p3-title"}
FIELDS = {"name", "title_lines", "subtitle", "summary", "contribution_label",
          "contribution", "technologies", "evidence"}


def text(value, field, allow_empty=False):
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise ValueError(f"{field} must be {'a string' if allow_empty else 'a non-empty string'}")
    return html.escape(value, quote=True)


def text_list(value, field):
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field} must be a non-empty list")
    return [text(item, field) for item in value]


def evidence_url(value):
    text(value, "evidence URL")
    # Evidence points at published resources; no scripts, credentials or whitespace.
    if any(c.isspace() or ord(c) < 32 for c in value) or "\\" in value:
        raise ValueError("evidence URL must not contain whitespace or backslashes")
    try:
        parsed = urlsplit(value)
        _ = parsed.port  # Accessing the property validates a supplied port.
    except ValueError as error:
        raise ValueError("invalid evidence URL") from error
    if (parsed.scheme != "https" or not parsed.hostname or
            parsed.username is not None or parsed.password is not None):
        raise ValueError("evidence URL must be an absolute HTTPS URL without credentials")
    return html.escape(value, quote=True)


def render_projects(data, template):
    if not isinstance(data, dict) or set(data) != set(PROJECT_IDS):
        raise ValueError("projects must contain exactly savvit, search and farm")
    values = {}
    for key, title_id in PROJECT_IDS.items():
        project = data[key]
        if not isinstance(project, dict) or set(project) != FIELDS:
            raise ValueError(f"{key}: unexpected or missing project fields")
        name = text(project["name"], "name")
        title = "<br>".join(text_list(project["title_lines"], "title_lines"))
        subtitle = text(project["subtitle"], "subtitle", allow_empty=True)
        if subtitle:
            title += f' <span class="subtle-name">{subtitle}</span>'
        values[key + "_title"] = f'<h3 id="{title_id}">{title}</h3>'
        values[key + "_summary"] = f'<p>{text(project["summary"], "summary")}</p>'
        label = text(project["contribution_label"], "contribution_label")
        contribution = text(project["contribution"], "contribution")
        values[key + "_contribution"] = (
            f'<p class="project-contribution"><strong>{label}</strong>{contribution}</p>'
        )
        technologies = ' <span>·</span> '.join(text_list(project["technologies"], "technologies"))
        values[key + "_technologies"] = (
            f'<div class="project-stack" aria-label="Technologies">{technologies}</div>'
        )
        evidence = project["evidence"]
        if not isinstance(evidence, list) or not evidence:
            raise ValueError(f"{key}: evidence must contain at least one link")
        links = []
        for link in evidence:
            if not isinstance(link, dict) or set(link) != {"label", "url", "accessible_label"}:
                raise ValueError(f"{key}: unexpected or missing evidence fields")
            url = evidence_url(link["url"])
            label = text(link["label"], "evidence label")
            accessible_label = text(link["accessible_label"], "accessible_label")
            links.append(
                f'<a class="project-link" href="{url}" target="_blank" rel="noopener noreferrer" '
                f'aria-label="{accessible_label}">{label} <span aria-hidden="true">↗</span></a>'
            )
        values[key + "_evidence"] = (
            f'<div class="project-actions" role="group" aria-label="{name} evidence">'
            + "".join(links) + "</div>"
        )
    formatter = string.Template(template)
    placeholders = [match.group("named") or match.group("braced")
                    for match in formatter.pattern.finditer(template)]
    if len(placeholders) != len(values) or set(placeholders) != set(values):
        raise ValueError("template must use each project placeholder exactly once")
    return formatter.substitute(values)


def update_page(page, projects):
    if page.count(BEGIN) != 1 or page.count(END) != 1:
        raise ValueError("index.html must contain exactly one pair of project markers")
    before, remainder = page.split(BEGIN)
    if END not in remainder:
        raise ValueError("project markers are out of order")
    _, after = remainder.split(END)
    return before + BEGIN + projects + END + after


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if index.html needs regeneration")
    args = parser.parse_args(argv)
    try:
        data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
        template = (ROOT / "templates/projects.html").read_text(encoding="utf-8")
        path = ROOT / "index.html"
        page = path.read_text(encoding="utf-8")
        updated = update_page(page, render_projects(data, template))
        if args.check:
            if page != updated:
                print("index.html is stale; run python tools/render_projects.py", file=sys.stderr)
                return 1
            print("Project HTML is up to date.")
        elif page != updated:
            path.write_text(updated, encoding="utf-8")
            print("Updated project HTML in index.html.")
        else:
            print("Project HTML is already up to date.")
    except (OSError, ValueError) as error:
        print(f"Project generation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
