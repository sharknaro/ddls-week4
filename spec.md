# Specification

## Decision

The owner needs a yes/no protocol decision: under a prespecified numerical rule, are human p53 residues **94–312** clearly higher in the reported model score than residues **1–93**, so that the DNA-binding core can be labelled the better-supported region for structure-guided work?

This is a comparison of unweighted regional arithmetic means. It is not a mutation call, pocket search, biological-importance ranking, validation of a drug target, validation of the 18–28 hypothesis, or analysis of an assembly.

## Protein and model

- Protein: human p53 (cellular tumour antigen p53), UniProt **P04637**.
- Sequence: **393 residues**, wild-type reference sequence, with no listed mutations, truncations, engineered tags, or additional chains.
- Model source: public **AlphaFold Database**; not predicted locally by the owner.
- Model contents: one isolated p53 polypeptide chain, not a dimer, tetramer, p53–MDM2 complex, or other multichain assembly.
- Biological context: p53 normally functions primarily as a tetramer and interacts with partners such as MDM2, but those assemblies are not represented here.
- Regions for the decision:
  - N-terminal regulatory/transactivation region: residues **1–93** (expected count 93).
  - Central DNA-binding core: residues **94–312** (expected count 219).
- Separate hypothesis, not the decision: residues **18–28**, an N-terminal MDM2-contacting/transactivation segment proposed as a possible design target. It must not be treated as a validated fixed standalone target from this comparison.
- The remaining C-terminal sequence contains tetramerisation machinery and regulatory tail, but its assembly is not modelled.

## Files

- `data/p53.fasta`: the plain 393-residue human p53 reference sequence and FASTA numbering basis.
- `data/p53_alphafold_model.cif`: the single-chain AlphaFold coordinate model. Its residue-associated local confidence is pLDDT in the B-factor column, `_atom_site.B_iso_or_equiv`; verify the field, scale/interpretation, chain, and residue mapping directly from the file before calculation.
- `data/p53_alphafold_pae.json`: the AlphaFold PAE numerical companion/grid. PAE is appropriate for claims about how parts sit together or interfaces; it is not the primary input to this regional pLDDT comparison. Because the model has one chain, it cannot establish tetramer or p53–MDM2 assembly.
- `ddls-week4-interview.md`: the authoritative interview transcript defining the owner's question and reporting requirements.

## Exact claim

The report must answer only:

> Under the prespecified criterion, residues 94–312 are / are not clearly higher than residues 1–93 in the reported model score.

The reported score must be identified exactly and mapped to FASTA residue numbers. For a fold/region claim, confidence matching the claim is per-residue pLDDT. Before reporting any structural conclusion, confirm that the model is the 393-residue human p53 chain, not another protein or an assembly.

Do not claim that this comparison validates the 18–28 helix as a fixed drug target, proves tetramer assembly, validates a p53–MDM2 complex, establishes biological importance, or replaces experimental evidence.

## Required calculation and checks

Use unweighted means over mapped residues actually included:

- `X = mean(score[1–93])`
- `Y = mean(score[94–312])`
- `Delta = Y - X`
- `ratio = Y / X`

Use the illustrative prespecified rule supplied in the interview, explicitly labelled as an arbitrary reporting rule rather than a biological law:

- `Y - X >= 10` score units, **and**
- `Y / X >= 1.10`.

The decision is **yes only if both conditions hold**.

Before calculation, establish:

1. The exact mmCIF field name, scale, units/interpretation, and why it is pLDDT.
2. The chain and residue mapping from the mmCIF to FASTA numbering.
3. Missing, duplicated, or unmapped residues.
4. That the sequence identity, length, chain count, and model contents match this p53 protein.

Report the following table:

| Region | Residues included | Expected count | Mapped count | Mean score |
|---|---:|---:|---:|---:|
| N-terminal | 1–93 | 93 | [n] | [X] |
| DNA-binding core | 94–312 | 219 | [n] | [Y] |

Then report both means, `Y-X`, `Y/X`, the criterion, and a binary yes/no decision. Do not compare sums or pool all 312 residues; the regions have unequal lengths.

## Done

This specification is satisfied only when the report contains the verified model/protein identity, exact score-field definition and mapping, missing/duplicate/unmapped-residue accounting, expected and mapped counts, both unweighted means, difference, ratio, declared criterion, and yes/no decision. The conclusion must remain narrow and limited to whether the reported model scores are clearly higher in residues 94–312 under that rule.

The owner additionally requested, for a fuller later analysis, medians, minima, maxima, quartiles, a residue-by-residue plot, boundary sensitivity, and separate treatment of 18–28. Those are later analysis requirements, not performed in this setup step.
