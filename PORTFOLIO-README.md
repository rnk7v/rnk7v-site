# rnk7v — Things worth making

A concise, framework-free personal site. Open `index.html` directly for the bundled fallback. Images are embedded; no visitor-side GitHub requests, fonts or analytics are required.

- `python3 scripts/build.py` renders `dist/index.html` offline, using bundled release metadata.
- Actstride's development repository is private. Public pages link to the application, not the private source or releases. No cross-repository credentials are stored or needed by this website.
- To refresh metadata for a future stable release, an authorized maintainer can run `gh api repos/rnk7v/actstride/releases/latest > /tmp/actstride-release.json`, then `python3 scripts/build.py --release-json /tmp/actstride-release.json --output index.html`, review the changes and commit them. The build reads the original HTML before writing the updated file.
- GitHub Actions deploys to Cloudflare Pages on pushes to main and manual dispatch. The previous public-release polling schedule is disabled while the repository is private.
- The approximate one-week build period is elapsed time through v1.5.0, not measured working hours.
- The Actstride application, its repository and its deployment are independent and are not modified by this site.
