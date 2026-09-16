# DDLS 2026 — Week 4 interview transcript

**Lab:** Interview a Structural-Biology Data Owner
**Data owner:** Dr. Margit Holló — Structural cancer-biology researcher (p53)
**Student:** Baris Kara <baris51519@gmail.com>
**Exported:** 2026-09-16T11:28:09+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

Can you walk me through the protein and what you are ultimately trying to decide from the AlphaFold model?

**Dr. Margit Holló**:

I’m Dr Margit Holló at Karolinska Institutet, working on human p53. The sequence contains the N-terminal regulatory region, the central DNA-binding core, and the C-terminal regulatory and tetramerisation regions; the AlphaFold model is the 3D picture of that protein. Ultimately, I want to know whether the model’s residue-by-residue scores are higher for the core, **94–312**, than for the N-terminal region, **1–93**, before treating the core as the better-supported region in our protocol. My medicinal-chemistry collaborator wants a defined target on the neat front-end helix, around **18–28**; which part will you examine first?

**You**:

What exactly is the molecule you are studying — one protein, multiple chains, or a complex? Roughly how many residues are there?

**Dr. Margit Holló**:

One protein: human p53, UniProt **P04637**, 393 amino acids. The model is the single polypeptide, not a p53–MDM2 complex or a multichain assembly. Are you checking the chain definition before calculating the two regional means?

**You**:

I would like to understand the project before I check something, so please bare with me and save your questions to later discussion. Do you have the exact sequence as a FASTA file?

**Dr. Margit Holló**:

Yes. **`p53.fasta`** contains the plain human p53 reference sequence, all **393 residues**, UniProt P04637. No engineered tags or additional chains.

**You**:

Where did the structure come from — AlphaFold Database, or did you run the prediction yourself?

**Dr. Margit Holló**:

It came from the public **AlphaFold Database**; I did not run the prediction myself. The coordinate file is **`p53_alphafold_model.cif`**.

**You**:

Is the model a single chain or an assembly such as a dimer or protein complex?

**Dr. Margit Holló**:

It is a **single p53 polypeptide chain**, 393 residues—not a dimer, tetramer, or protein complex. Biologically p53 can tetramerise, but this model is only one chain.

**You**:

What is the biologically functional form of the protein — does it normally work as a monomer, dimer, or with another binding partner?

**Dr. Margit Holló**:

Functionally, p53 works primarily as a **tetramer**—a four-subunit transcription factor that binds DNA. It also engages partners such as MDM2, which suppresses and regulates it, but the file you have is only one isolated p53 chain.

**You**:

What other files do you currently have — FASTA, PDB/mmCIF, confidence files, or anything else?

**Dr. Margit Holló**:

Three files:

- **`p53.fasta`** — the 393-residue reference sequence.
- **`p53_alphafold_model.cif`** — the single-chain AlphaFold coordinate model.
- **`p53_alphafold_pae.json`** — a large numerical companion file from AlphaFold; I have not used it.

No separate PDB file.

**You**:

Does the model include residue-level confidence information such as pLDDT, and do you also have a PAE/error matrix?

**Dr. Margit Holló**:

The mmCIF contains a residue-associated numerical field, and the JSON is the large grid of numbers that came with the model. I have not interpreted either; the technical part is yours, not mine.

**You**:

Does the sequence used to generate the structure exactly match the construct you use experimentally — same length, mutations, truncations, and tags?

**Dr. Margit Holló**:

The FASTA is the **393-residue wild-type human p53 reference sequence**, with no listed mutations, truncations, or tags. I have not been given a separate experimental construct specification, so I cannot claim it matches whatever construct you use at the bench.

**You**:

Which exact region or residues of the model are important for the decision you want to make?

**Dr. Margit Holló**:

The decision compares two regions:

- **N-terminal region: residues 1–93**
- **DNA-binding core: residues 94–312**

I need the mean of the residue-associated scores for each region, then a yes/no decision on whether the core is clearly higher. Separately, the proposed design target is the front-end helix around **18–28**.

**You**:

What do you want to infer from those residues specifically — for example, whether the region is folded, where a pocket is, where a binder might bind, or which residues to mutate?

**Dr. Margit Holló**:

The immediate inference is narrower: whether the **94–312 DNA-binding core** has a clearly higher mean of the residue-associated model scores than **1–93**, so we can label the core the more dependable region in the protocol. I am not asking you to locate a pocket or nominate mutations at this stage; the separate medicinal-chemistry idea is to examine the **18–28 N-terminal helix** as a possible binding target.

**You**:

What experimental decision will you make based on the structure — which mutations, molecule, construct, or experiment would change depending on the answer?

**Dr. Margit Holló**:

The practical decision is a **protocol rule**, not a mutation call. If residues **94–312** have a clearly higher regional mean than **1–93**, we will label the DNA-binding core the more dependable part for structure-guided work; if the separation is not clear, we write no such rule and avoid directing the medicinal-chemistry team on that basis. The proposed molecule against **18–28** is a separate hypothesis, not something this comparison can validate.

**You**:

Who will act on that result, and what would be the practical cost if that structural interpretation were wrong?

**Dr. Margit Holló**:

The medicinal-chemistry collaborator and the colleagues applying our shared p53 structure protocol will act on it. If wrong, they could spend limited synthesis and assay time treating the wrong region as a sound design basis—particularly costly if we direct them toward the **18–28** helix and obtain misleading binders or no useful molecule at all.

**You**:

What makes you confident that this part of the model is correct? What are you seeing in the structure that reassures you?

**Dr. Margit Holló**:

The central DNA-binding region appears compact and beautifully folded in the picture, while the N-terminus contains a clean helix around **18–28**. That is what caught my eye; biologically, the core is the domain that contacts DNA and carries the classic cancer hotspots. Which region are you asking me to justify specifically—the core or the front-end helix?

**You**:

Can you justify both regions please

**Dr. Margit Holló**:

The **94–312 core** looks compact and coherently folded, which fits its known role as p53’s DNA-contacting domain and the location of the major cancer mutations. The **18–28 segment** appears as a particularly neat, continuous helix at the front of the chain; it contains the transactivation residues that engage MDM2, so it is biologically interesting as a possible design handle.

That is visual and biological justification, not the regional numerical comparison you need. You must calculate the two means from the residue-associated values in the mmCIF before writing the protocol rule.

**You**:

For the exact residues you want to rely on, is the confidence equally strong there, or is your confidence mainly based on the overall appearance of the model?

**Dr. Margit Holló**:

I have not established that for the exact residues. My judgement so far is based mainly on the model’s appearance: the core looks compact, and **18–28** forms a clean helix. Whether the numerical values are equally strong across those regions is precisely what you must test from the mmCIF.

**You**:

Is the region you care about expected to be structured on its own, or could it become ordered only when it binds another molecule or protein?

**Dr. Margit Holló**:

Honestly, that end of p53 is pretty floppy in the tube until it latches onto MDM2, although the model shows such a clear helix that I assumed it was fine. The **18–28** segment is the MDM2-contacting transactivation motif; that distinction matters greatly before treating it as a fixed drug target.

**You**:

If multiple chains are involved, what makes you confident about how the chains sit relative to each other, rather than just that each chain folds well individually?

**Dr. Margit Holló**:

There are no multiple chains in this model, so there is no inter-chain arrangement to assess. The file is one isolated 393-residue p53 chain; its biological tetramerisation is not represented.

**You**:

Do you have any experimental evidence that the chains interact or assemble in that way?

**Dr. Margit Holló**:

For the tetramer, yes: p53 tetramerisation is established biologically through its C-terminal oligomerisation domain. But this file contains no assembled tetramer, and I have no experimental evidence from this model for any chain–chain arrangement.

**You**:

Do you have any experimental evidence that the chains interact or assemble in that way?

**Dr. Margit Holló**:

Yes, for **p53 tetramerisation** there is extensive experimental evidence involving its C-terminal oligomerisation domain. But this structure file contains only one isolated chain, so it provides no evidence for how four chains assemble—or for a p53–MDM2 complex.

**You**:

Could any residues that look surface-exposed in this model actually become buried when the biologically relevant assembly forms?

**Dr. Margit Holló**:

Yes. Residues exposed on this isolated chain could become buried at the **p53 tetramer interface**, especially near the C-terminal oligomerisation region. This model cannot tell us which surfaces are altered on assembly because it contains no tetramer; the **18–28** motif is instead an N-terminal partner-binding site, chiefly relevant to MDM2.
