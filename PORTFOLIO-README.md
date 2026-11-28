# rnk7v personal archive

A single-page, framework-free portfolio. `index.html` opens independently, with a v1.5.0 release fallback and all images embedded. It does not contact GitHub from the visitor's browser.

- `python3 scripts/build.py` renders `dist/index.html` without network access.
- `python3 scripts/build.py --refresh` fetches the latest stable public Actstride release and updates only the two version labels, two release URLs and one date. Historical text and screenshot captions remain fixed.
- Existing Cloudflare Pages deployment runs on push, manually, and once daily. A scheduled run skips deployment when live content matches. The existing two Cloudflare secrets are reused; no new secret is needed.
- Development time is a manually recorded approximate elapsed period (about one week through v1.5.0), not recorded work hours or repository age.

No Actstride application code is changed. The genuine images are from the released Actstride archive and the previous portfolio.
