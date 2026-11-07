# Brandon Ho — portfolio preview

A personal portfolio for graduate, junior and internship applications, with a balanced selection of web development, algorithms and software systems work.

## Current status

The preview is published at https://brandonho419.github.io/portfolio-preview/.
This address is temporary. The permanent address and any custom domain will be decided separately.
The page retains `noindex,nofollow` while it is a preview. This discourages search indexing; it does not restrict public access.

Expected graduation: 2027. Achievements and certifications will be added when suitable verified content is available.

## Run locally

Viewing the site requires no installation, build step, API key or backend.
Editing project data requires Python 3.9 or later, using only its standard library.

Open `index.html` in a browser, use VS Code Live Server, or run:

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000. Google Fonts requires internet access; system fonts provide a fallback.
JavaScript only updates the footer year. Core content and navigation work without it.

## Structure

- `index.html`: committed static page; its marked project section is generated.
- `data/projects.json`: curated project titles, descriptions, technologies and evidence links.
- `templates/projects.html`: project layout and conceptual illustrations.
- `tools/render_projects.py`: validates project data and regenerates the marked section.
- `tests/test_render_projects.py`: generator regression tests.
- `styles.css`: responsive editorial design, keyboard focus and reduced-motion support.
- `script.js`: footer year.
- `favicon.svg`: BH mark.
- `.nojekyll`: static GitHub Pages publishing.

## Maintain project evidence

Edit project text and links in `data/projects.json`, then run from the repository root:

```sh
python tools/render_projects.py
python tools/render_projects.py --check
python -m unittest discover -s tests -v
```

Use `python3` if your system requires it, or `py -3` on Windows.
Review and commit the updated `index.html` alongside data or template changes. GitHub Pages serves the committed HTML; it does not run the generator.
Do not hand-edit between `BEGIN GENERATED PROJECTS` and `END GENERATED PROJECTS` in `index.html`.
Other page sections remain editable directly in `index.html`. Layout and illustration edits belong in `templates/projects.html`.
The generator checks all inputs before writing, escapes text and attributes, and changes only the marked section. `--check` reports stale HTML without writing.

Each of the three project entries has a name, title lines, optional subtitle (empty string when absent), summary, contribution label and text, technologies, and evidence links.
The existing `savvit`, `search` and `farm` keys map to the three curated layout slots. Adding or reordering projects requires an intentional template and generator update.
All text is plain text, not embedded HTML. Evidence URLs must be absolute HTTPS URLs without credentials or whitespace.

When real material is ready:

1. Add an appropriately sized screenshot or recording with descriptive alternative text or a caption in `templates/projects.html`.
2. Replace the relevant conceptual illustration where appropriate, preserving its responsive layout.
3. Add an evidence entry with `label`, `url` and `accessible_label` in that project's JSON data. Use a published HTTPS address for a screenshot, walkthrough or demo.
4. Regenerate, review the diff and test the actual destination before publishing. Link validation checks URL format, not whether the destination exists.

For example, add this object to a project's `evidence` array only after replacing the example URL with a working demo:

```json
{
  "label": "Try demo",
  "url": "https://example.com/your-demo/",
  "accessible_label": "Try the Mini Search Engine demo"
}
```

Only links present in the data are rendered. There are no placeholder demo buttons on the published page.

Illustrations currently on the site are original conceptual diagrams, not screenshots, test results or performance measurements.
Savvit is a university group project; its description distinguishes Brandon's individual contributions.
Do not add unverified accomplishments, certifications or performance claims.

## Verify changes

Run the generator check and regression tests above. No CI workflow is checked in; these checks currently run locally.
The content refactor preserves the existing markup and CSS. Browser checks remain necessary for visual or layout changes.

- Inspect the introduction and all projects at desktop, tablet and narrow mobile widths.
- Confirm there is no horizontal scrolling and project text and evidence links remain readable.
- Use Tab to check the skip link, navigation, evidence links and contact links.
- Check section navigation, all external destinations and the email link.
- Disable JavaScript and verify the content remains usable.
- Check reduced-motion preferences and offline font fallbacks.

## Publishing and planned work

The site uses GitHub Pages. Pushing approved changes to the configured publishing branch updates the public preview.
Do not change Pages configuration or add deployment workflows as part of content edits.

Project data is now separate from markup. A later approved stage may refresh selected GitHub metadata daily.
Project selection, personal contributions and achievement descriptions will remain curated.
Automatic metadata updates, screenshots, demos, certifications and a résumé download are not yet implemented.
