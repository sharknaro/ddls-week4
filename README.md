# p53 structure evidence readout

A small, database-free FastAPI application serving the verified p53 structure evidence and a single-page Tailwind/3Dmol.js readout.

## Run

From this folder:

```bash
uv run uvicorn app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/.

The structure panel loads the AlphaFold CIF through the app API and renders the protein backbone in 3Dmol.js. The confidence panel includes the residue number, amino-acid code, and pLDDT value for all 393 residues, with the claimed intervals marked. If the CDN is unavailable, the page shows an explicit loading error rather than an empty panel. Allow network access to `https://3Dmol.csb.pitt.edu` and `https://cdn.tailwindcss.com` in the browser.

The app reads `results/results.json` and the supplied structure/PAE files from disk. It does not run folds or use a database. Tailwind CSS and 3Dmol.js are loaded from their CDNs by the browser.
