# rnk7v — Things worth making

A concise, framework-free personal site. Open `index.html` directly for the bundled fallback. Images are embedded; no visitor-side GitHub requests, fonts or analytics are required.

- `python3 scripts/build.py` renders `dist/index.html` offline.
- `python3 scripts/build.py --refresh` fetches the latest stable public Actstride release and refreshes the single version label, release URL and date. Historical screenshots and milestones remain pinned to their documented release.
- The existing GitHub Actions workflow deploys to Cloudflare Pages on pushes to main, manual dispatch and a daily schedule. Scheduled runs skip identical live content.
- The approximate one-week build period is elapsed time through v1.5.0, not measured working hours.
- The Actstride application, its repository and its deployment are independent and are not modified by this site.
