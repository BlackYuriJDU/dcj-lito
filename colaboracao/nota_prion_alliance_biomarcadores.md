# Brief technical note — two independent-verification results relevant to prion clinical-trial design

*Projeto DCJ - Lito (independent initiative, Brazil) · 2026-08-26 · accompanying open repository: github.com/BlackYuriJDU/dcj-lito*

Dear Dr. Minikel and Dr. Vallabh,

Congratulations on PRiSM's launch and on the open-regulatory-documents policy — we reviewed the April 2026 community statement and the July mid-year update before writing this. Two results from our independent reanalyses of public datasets may be useful to trial design and biomarker strategy. Both come with methods, seeds and every intermediate number openly published.

## 1. Blood biomarker signatures can collapse under standard covariate adjustment — quantify before relying on them

Reanalysis of GSE140069 (Nat Commun 2020; 57 sCJD / 48 controls, 939 miRNAs, Illumina): the naive comparison yields 84 miRNAs significant at FDR<0.05 (10↑/74↓). A standard OLS with age + sex + RIN (covariates all present in the series matrix) leaves **1** surviving at FDR<0.05 (939 tests). The structure causing this is textbook: cases were 12.8 years older (66.4 vs 53.6) with worse RNA integrity (RIN 5.59 vs 6.50). The four discovery miRNAs keep direction and nominal significance (p = 7×10⁻⁴–4×10⁻²), and only hsa-miR-93-5p survives FDR in the detection-filtered universe (q = 0.048) — a genuine but weaker-than-presented signal. This is not an accusation (the original authors adjusted age themselves); it is a quantified demonstration of how naive-vs-adjusted divergence can inflate peripheral biomarker panels — relevant when CSF is unavailable and blood markers are the fallback for trial screening or pharmacodynamic readouts.

**Complementary cross-compartment test**: validated targets (miRTarBase 10.0, Functional MTI) of the four discovery blood miRNAs are **not** over-represented among the up-regulated brain DEGs of GSE160208 (hypergeometric, all q = 1.0; overlaps at or below chance). The blood signature appears to reflect peripheral processes rather than the cerebral transcriptional program — cautioning against blood→brain causal inference in biomarker interpretation.

## 2. STX6 GWAS signal is expression-mediated to the limit summary statistics allow

Independent QC/fine-mapping of GCST90001389 (4,110 cases / 13,569 controls) confirms all three published loci; blind whole-genome clumping rediscovers them as the top-3 clusters (pipeline sensitivity, not circular confirmation). For STX6 specifically: a five-cohort brain eQTL meta-analysis (CommonMind n=586, ROSMAP n=560, BrainSeq n=479, GTEx v10 DLPFC n=285, GTEx v10 cerebellum n=272; eQTL Catalogue r8, retrieved by remote tabix region queries) makes the GWAS lead variant rs11586493 a **genome-wide significant brain eQTL (p = 6.6×10⁻⁴⁷; z ≈ 14)** with **89% effect-direction concordance** across 390 harmonised variants. Regional ABF colocalization (Giambartolomei) concentrates the entire posterior on shared-block hypotheses (H₃+H₄ ≈ 0.995; H₀/H₁/H₂ ≈ 0). Strict H₄ is unidentifiable under r² ≥ 0.97 within the cluster — we say so explicitly — but the pattern (significant meta-eQTL at the lead + direction concordance + single fine-mapping cluster) is consistent with the 2020 association and the 2025 functional nomination of rs3747957 being two views of the same regulatory event. If STX6 expression matters to prion disease pathogenesis, expression is also a stratification variable worth tracking in natural-history and trial cohorts.

## Closing

We are a non-laboratory initiative; our contribution is verification-grade open reanalysis. If either item is wrong, we would be grateful to know why. If useful, everything is reproducible from the repository (pure-stdlib statistical core cross-validated against R; regression tests vs scipy at 1e-9).

With respect and gratitude for the open-science precedent,
Projeto DCJ - Lito
