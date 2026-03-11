[Date]

Editor-in-Chief
Aging Cell

Dear Editor,

We are pleased to submit our manuscript entitled **"Computational Identification of Geroprotective Compound Candidates via Multi-Source Biological Network Analysis"** for consideration in *Aging Cell*.

**Summary.** We present Discovery Engine, an open-source computational pipeline that integrates literature mining (376 PubMed papers), aging target databases (GenAge, 307 genes), drug-target associations (Open Targets, 1,118 associations), bioactivity data (ChEMBL), and lifespan records (DrugAge, 1,046 compounds) into a knowledge graph (479 nodes, 898 edges). A weighted multi-feature scoring system ranks 162 drug candidates for geroprotective potential.

**Key findings:**

- The pipeline independently recovers known geroprotectors: rapamycin (#1), metformin (#10), resveratrol (#12), spermidine (#13), acarbose (#18), and dasatinib (#20) in the top 20, validating the methodology.
- Bootstrap analysis (n=1,000) confirms ranking stability (rapamycin std=0.0, metformin std=1.2).
- Zero false positives among 10 negative controls.
- Novel candidates with existing clinical safety data include bezafibrate (PPAR agonist, +13% lifespan, FDA-approved), bardoxolone methyl (NRF2/PPARG activator, Phase 3), and venetoclax (BCL-2 inhibitor, potential senolytic).

**Why Aging Cell.** Our work addresses a methodological gap: only 1.6% of 376 relevant publications specifically tackle computational drug repurposing for aging. Discovery Engine provides a reproducible, auditable framework that bridges this gap, directly relevant to Aging Cell's readership interested in geroprotector discovery and translational aging research.

**Novelty.** To our knowledge, no existing framework systematically integrates literature mining, protein-drug associations, bioactivity data, lifespan extension evidence, and network topology into a unified geroprotector scoring system. The identification of bezafibrate and venetoclax as top candidates with existing safety profiles offers immediate translational potential.

**Reproducibility and transparency.** All code is open-source (GitHub, MIT License), all data files are provided, and the pipeline is fully deterministic (seed=42) with SHA-256 checksums for all inputs and outputs. We include a transparent declaration of AI assistance per Nature Machine Intelligence guidelines.

This manuscript has not been published elsewhere and is not under consideration by another journal. The preprint will be deposited on bioRxiv upon submission.

We look forward to your consideration.

Sincerely,

**Tercio S. Azevedo**
Independent Researcher
Sao Carlos, SP, Brazil
terciosilas@gmail.com
