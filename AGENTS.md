# Operating instructions

## Environment

- Use `uv` for the Python environment: create it with `uv venv`.
- Run all Python with `uv run`; this is intended to work the same way on every OS.
- Do not put secrets in version control. In particular, `.env` is ignored.

## Data and files

- The supplied archive is `ddls-week4-s1-idr-confidence-dataset.zip`; its extracted data are in `data/`:
  - `data/p53.fasta` — the 393-residue wild-type human p53 reference sequence (UniProt P04637).
  - `data/p53_alphafold_model.cif` — the single-chain AlphaFold coordinate model.
  - `data/p53_alphafold_pae.json` — AlphaFold's numerical PAE companion file.
- The interview transcript is `ddls-week4-interview.md`.
- Write generated analyses, tables, plots, and reports under `results/`.
- When loading the structure, use the mmCIF residue-associated local confidence field. The AlphaFold pLDDT is in the B-factor column (`_atom_site.B_iso_or_equiv`); map it to the residue numbering and check for missing, duplicated, or unmapped residues.
- PAE is in the JSON file. Use it for questions about relative placement or interfaces between parts, not as a substitute for per-residue pLDDT when assessing a fold or region. This dataset is a single-chain model, so do not imply that it supplies a tetramer or partner interface.

## Version control

This folder is a git repository. Before any big change—installing packages, rewriting a working file, or making a large refactor—commit the current state first. Commit again whenever something starts working, with short, clear messages, so there is always history to roll back to. Never commit `.env`, `.venv/`, `__pycache__/`, or `*.pyc`.

## Evidence rule

Never report an answer about a structure without first reporting the confidence that matches the claim **and** confirming that the model is actually this protein. For a fold or region claim, report per-residue pLDDT (the mmCIF B-factor field) and its residue mapping. For a claim about how parts sit together or about an interface, report the relevant PAE and verify that the model actually contains the claimed assembly. Keep conclusions limited to what the supplied files support.
