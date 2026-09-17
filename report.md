# p53 structure-confidence report

## The question

Can the supplied computational structure evidence identify a defensible starting region for further work on human p53, and what biological caveats must not be overlooked?

## The protein & files

The analysis used the supplied wild-type human p53 P04637 FASTA (`data/p53.fasta`), which contains 393 residues. It compared:

- the AlphaFold DB model (`data/p53_alphafold_model.cif`; AF-P04637-F1, version 6), including its per-residue pLDDT and PAE data; and
- the course-fold model and its confidence data (`results/course_fold_p53.json`).

The AlphaFold DB and course-fold model sequences match the supplied 393-residue FASTA exactly. No substitutions, truncations, missing positions, duplicated positions, or unmapped positions were detected.

The supplied structures are isolated single-chain models. They do not establish the structure of the functional p53 tetramer, a p53–MDM2 complex, another partner-bound state, or the undocumented experimental construct.

## The right confidence

For a fold or region-selection question, the relevant confidence measure is **per-residue pLDDT**. It reports local model confidence and is the basis of the primary regional comparison. PAE is used separately for uncertainty in the relative placement of regions; it is not substituted for pLDDT in the regional fold comparison.

The completed viewer and figures provide visual checks of the same outputs:

- `results/visual_validation/alphafold_plddt_regions.png`
- `results/visual_validation/course_fold_plddt_regions.png`
- `results/visual_validation/alphafold_pae_regions.png`
- `results/visual_validation/course_fold_pae_regions.png`
- `results/alphafold_p53_3d_plddt.png`
- the interactive viewer served by `app.py`

## Structure check

Both model sequences match the supplied 393-residue p53 FASTA exactly. Each model is one isolated chain. This is a sequence-and-model consistency check, not confirmation that either model reproduces the owner’s experimental construct or functional assembly.

## The trap and honest truth

### Primary regional result: residues 1–93 versus 94–312

The prespecified illustrative rule required both a difference of at least 10 pLDDT units and a core-to-N-terminal mean ratio of at least 1.10.

| Model | Residues 1–93 mean | Residues 94–312 mean | Difference | Ratio | Rule |
|---|---:|---:|---:|---:|---|
| AlphaFold DB | 48.42 | 90.84 | 42.42 | 1.88 | Satisfied |
| Course fold | 64.18 | 86.32 | 22.15 | 1.35 | Satisfied |

This is the primary model-score result. It supports residues **94–312** as the preferred computational starting region under the stated rule.

The regional mean should not erase local variation. Residues **294–312** are reproducibly weaker in both models under the `<70` threshold, and residue **296** is below pLDDT 50 in both models. The supplied materials do not establish the biological cause of this patch. It should not be relabelled as a linker, domain boundary, or tetramerisation transition based on pLDDT alone.

### Boundary-sensitivity check: excluding residues 294–312

As a sensitivity analysis—not a redefinition of the biological core boundary—I recalculated the core mean for residues **94–293** and compared it with the original **94–312** definition:

| Model | Core mean, 94–312 | Core mean, 94–293 | Change (94–293 minus 94–312) |
|---|---:|---:|---:|
| AlphaFold DB | 90.84 | 95.15 | +4.30 |
| Course fold | 86.32 | 88.92 | +2.60 |

The increase is expected because the excluded 294–312 patch is weaker, but the primary conclusion does not change. Against the unchanged N-terminal comparison (1–93), the 94–293 means remain higher by 46.72 pLDDT units (ratio 1.96) for AlphaFold DB and 24.75 units (ratio 1.39) for the course fold. Both still satisfy the prespecified illustrative rule (difference ≥10 and ratio ≥1.10). This sensitivity result does not establish a new biological domain boundary.

### Separate 18–28 trap

Residues 18–28 were assessed separately because the interview notes that this segment may look helical in an isolated AlphaFold model but could become ordered in a partner-bound context.

| Model | Mean pLDDT | Minimum | Residues below 70 | Residues below 50 |
|---|---:|---:|---|---|
| AlphaFold DB | 68.88 | 57.66 | 18, 19, 26, 27, 28 | None |
| Course fold | 70.74 | 58.95 | 26, 27, 28 | None |

The mean PAE between residues 18–28 and the 94–312 core is high in both directions:

- AlphaFold DB: 30.70 Å and 28.65 Å
- Course fold: 28.06 Å and 28.49 Å

Thus, the isolated models provide local confidence values for 18–28 but do not establish its precise placement relative to the core. Holló’s interview statement is directly relevant: this region is floppy in isolation and becomes ordered on MDM2 binding. Together with the moderate pLDDT and high PAE relative to the core, the defensible biological verdict is that residues 18–28 should be treated as an **induced-fold recognition helix**, not a rigid free-state design template. This does not prove a particular bound conformation, induced fit mechanism, MDM2 affinity, or druggability.

The actionable next step for medicinal chemistry is to design and model against the relevant complex, or validate the conformation experimentally, before using residues 18–28 as a fixed target. The supplied single-chain model cannot provide that complex or validation. This caveat is separate from, and does not overturn, the primary 94–312 regional comparison.

## Answer/recommendation

**Yes—use residues 94–312 as the preferred computational starting region under the illustrative rule.** Both independent model sources satisfy the rule, and both show substantially higher mean pLDDT for 94–312 than for residues 1–93.

The owner can act on this as a **narrow prioritisation of a region for computational inspection in the supplied isolated, sequence-matched models**. The owner should retain the local 294–312 warning and should not treat the regional mean as uniform residue-level support.

The owner cannot act on this result as validation of a molecule, peptide, binding site, interface, tetramer assembly, partner-bound conformation, experimental construct, or assay outcome. Residues 18–28 should be treated as an induced-fold recognition helix—not a rigid free-state design template. Before using it as a fixed target, design/model against the relevant complex or validate its conformation experimentally.

## Caveats & next steps

1. Obtain the experimental construct sequence and assay context before transferring any model-based conclusion to the experiment.
2. Align that construct to wild-type P04637 and check tags, linkers, mutations, truncations, numbering, chain count, oligomeric state, and partners.
3. Treat residues 294–312 as a locally weaker patch without assigning an unsupported biological explanation.
4. If a binding site or interface is proposed, require appropriate structural/PAE or experimental interface evidence; regional pLDDT means alone are insufficient.
5. Use the interactive viewer and saved figures to inspect the confidence pattern, but do not treat visual appearance as confidence evidence beyond the underlying reported pLDDT and PAE values.

## AI-use disclosure

Agent A (Data owner) provided data structure, goal of the porject, what to analyze and deliver.


Agent B (Pi) assisted with file inspection, extraction and comparison of the supplied sequence, model confidence values, and PAE values; calculation checking already recorded in the project; generation of figures and an interactive viewer; and drafting this report from the verified project materials. No new web search, fold, or modelling was performed for this report.

Person (I) provided bridge between the agents, checked the information provided by agent A match with the validation results obtained with agent B.
