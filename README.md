# Brandon Ho — portfolio preview

A personal portfolio for graduate, junior and internship applications, with a balanced selection of web development, algorithms and software systems work.

## Current status

The preview is published at https://brandonho419.github.io/portfolio-preview/.
This address is temporary. The permanent address and any custom domain will be decided separately.
The page retains `noindex,nofollow` while it is a preview. This discourages search indexing; it does not restrict public access.

Expected graduation: 2027. Achievements and certifications will be added when suitable verified content is available.

## Run locally

No installation, build step, API key or backend is required.

Open `index.html` in a browser, use VS Code Live Server, or run:

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000. Google Fonts requires internet access; system fonts provide a fallback.
JavaScript only updates the footer year. Core content and navigation work without it.

## Structure

- `index.html`: introduction, three selected projects, skills, experience and contact links.
- `styles.css`: responsive editorial design, keyboard focus and reduced-motion support.
- `script.js`: footer year.
- `favicon.svg`: BH mark.
- `.nojekyll`: static GitHub Pages publishing.

## Maintain project evidence

Each project separates its purpose from its contribution or engineering focus.
The `.project-actions` container holds the available evidence links. Currently these link to source code.

When real material is ready:

1. Add an appropriately sized screenshot or recording with descriptive alternative text or a caption.
2. Replace the project's conceptual illustration where appropriate, preserving its responsive layout.
3. Add a descriptive screenshot, walkthrough or demo link inside that project's `.project-actions` container.
4. Test the actual destination before publishing. Do not add empty links or imply a demo exists before it does.

Illustrations currently on the site are original conceptual diagrams, not screenshots, test results or performance measurements.
Savvit is a university group project; its description distinguishes Brandon's individual contributions.
Do not add unverified accomplishments, certifications or performance claims.

## Verify changes

There is no automated test suite or checked-in CI workflow.

- Inspect the introduction and all projects at desktop, tablet and narrow mobile widths.
- Confirm there is no horizontal scrolling and project text and evidence links remain readable.
- Use Tab to check the skip link, navigation, evidence links and contact links.
- Check section navigation, all external destinations and the email link.
- Disable JavaScript and verify the content remains usable.
- Check reduced-motion preferences and offline font fallbacks.

## Publishing and planned work

The site uses GitHub Pages. Pushing approved changes to the configured publishing branch updates the public preview.
Do not change Pages configuration or add deployment workflows as part of content edits.

Next: separate project data from markup for simpler maintenance. A later approved stage may refresh selected GitHub metadata daily.
Project selection, personal contributions and achievement descriptions will remain curated.
Automatic metadata updates, screenshots, demos, certifications and a résumé download are not yet implemented.
