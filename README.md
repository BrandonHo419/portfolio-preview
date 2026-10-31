# Brandon Ho — Swiss Industrial portfolio (STAGING)

**Status:** Prepared for staging deployment; not published as part of this package.

## Design direction

The user approved a ~70% Swiss Technical Editorial / ~30% Industrial Brutalism hybrid. The design uses a 12-column grid, generous white space, oversized asymmetrical `BRANDON HO.` headline, warm off-white, charcoal and restrained industrial orange, plus Archivo and IBM Plex Mono typefaces.

No glassmorphism, gradients, generic nested cards, templated three-column cards, or generic marketing slogans. Project diagrams are **original conceptual illustrations**, not screenshots, real test output, or measured performance.

## Content and privacy

- Professional public name: Brandon Ho.
- Public contact email was explicitly approved.
- Pinboard Embedder / Savvit is a university group project; the claimed individual contributions were expressly confirmed by the candidate.
- Formal Cybersecurity major is **not** claimed because the university record has not yet been verified.
- No private legal name, phone number, home address, referee details, transcript, GPA, or grades are included.
- `noindex,nofollow` is enabled only to discourage search engine indexing during staging. **It is not access protection.**

## Edit and preview locally

You can edit `index.html`, `styles.css`, and `script.js` in VS Code. Open `index.html` directly in a browser, or use VS Code Live Server. Internet access is needed to fetch Google Fonts; system fallback fonts will be used without it. No JavaScript build, npm install, API keys or backend are required.

## Publish to a separate *unadvertised* staging URL

Target: `https://brandonho419.github.io/portfolio-preview/` (proposed; not verified live).

1. Sign in to GitHub as `BrandonHo419` and create a **public** repository named `portfolio-preview`. Do not create the final account-level `BrandonHo419.github.io` repository for staging.
2. Extract the ZIP and upload the **files inside the folder** to the new repository's root: `index.html`, `styles.css`, `script.js`, `favicon.svg`, `.nojekyll` and optionally `README.md`. Do **not** upload only the ZIP file.
3. Commit the files on the `main` branch.
4. Open **Settings → Pages → Build and deployment → Source: Deploy from a branch**, choose **main** and **/(root)**, then save.
5. When deployment reports success, visit `https://brandonho419.github.io/portfolio-preview/` and test links on a computer and phone.
6. Make edits in the repository or via VS Code, and commit them to `main`; GitHub Pages republishes changes. Keep this staging site out of applications until the final release is separately approved.

Note: The GitHub connection available in this conversation can read and edit existing repositories but does not currently expose repository creation or Pages configuration. No live staging repository or URL has been created or activated by this package. GitHub Pages is public to anyone with the address. `noindex` is only a request to search engines.

Official GitHub guide: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Final production release (separate approval required)

Before launching the final professional portfolio, review all content again, add real screenshots if desired, remove the staging `noindex` meta tag, decide the permanent GitHub Pages repository and domain, and obtain explicit approval to deploy.

## Files

- `index.html` — semantic content, three selected projects and links
- `styles.css` — 12-column Swiss Industrial design and responsive layout
- `script.js` — footer year only; site works without it
- `favicon.svg` — custom BH mark
- `.nojekyll` — disables Jekyll interpretation for GitHub Pages
