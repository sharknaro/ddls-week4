# p53 structure evidence readout

A small, database-free FastAPI application serving the verified p53 structure evidence and a single-page Tailwind/3Dmol.js readout.

## Run

From this folder:

```bash
uv run uvicorn app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/.

The structure panel loads the AlphaFold CIF and course-fold PDB through the app API and renders them in 3Dmol.js. If the CDN is unavailable, the page shows an explicit loading error rather than an empty panel. Allow network access to `https://3Dmol.csb.pitt.edu` and `https://cdn.tailwindcss.com` in the browser.

The app reads `results/results.json` and the supplied structure/PAE files from disk. It does not run folds or use a database. Tailwind CSS and 3Dmol.js are loaded from their CDNs by the browser.
