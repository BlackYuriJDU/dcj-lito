# Letter to Prion Alliance / Vallabh–Minikel Lab (EN, ready to send)

**To:** svallabh@broadinstitute.org; eminikel@broadinstitute.org
**Subject:** Independent verification of GCST90001389 — all three loci replicate, and rs3747957 was already there in 2020

---

Dear Dr. Vallabh and Dr. Minikel,

We are an independent, non-laboratory data initiative in Brazil. Following the precedent you set yourselves, we have spent the past weeks doing something unglamorous that we believe the field needs: an end-to-end independent verification of publicly deposited prion-disease data, using only open-source tooling.

Three results we think may interest you:

1. **Full replication of GCST90001389 from sumstats alone.** All three published loci reproduce exactly: PRNP chr20:4,672,307 (p = 1.6×10⁻¹⁵), GAL3ST1 chr22:30,950,360 (p = 6.2×10⁻¹⁰), STX6 chr1:180,961,245 (p = 7.5×10⁻⁹); λ = 1.059 with a MAF-stratified gradient of only 0.016. Zero malformed records across 6.3M variants.

2. **A numerical bridge between the 2020 GWAS and your Brain 2025 multi-omic finding.** rs3747957 — the index variant nominated functionally in 2025 — is present in the 2020 sumstats at p = 9.7×10⁻⁹ with identical effect direction (β = −0.148), ranking 11th of 162 regional variants. With Ensembl/1000G LD we show it sits at r² ≈ 0.99 with our lead; the lead cluster carries 90.5% of regional posterior mass. The 2020 data already contained the evidence your functional work later validated.

3. **A cautionary biomarker result.** Reanalyzing GSE140069 (blood miRNA, Nat Commun 2020) with standard OLS adjustment for age/sex/RIN collapses the signature from 84 nominally significant miRNAs to 1; directionality and nominal significance of the four discovery miRNAs persist. Cases were 12.8 years older than controls — a textbook confounding structure quantified explicitly for future pipelines.

A preprint draft (~2,000 words, letter format) is written; code is pure-Python stdlib, reports include every intermediate number, and an adversarial statistical audit of our own pipeline (R-anchored Welch/BH validation, permutation calibration) is included.

We are not asking for funding, positions, or collaboration commitments — only this: **if you had 20 minutes to look at the draft and tell us where we are wrong or naive, it would materially improve the work before submission to bioRxiv.**

Repository (private until we make it public alongside the preprint): github.com/BlackYuriJDU/dcj-lito — happy to grant read access immediately.

With respect,
[NAME], on behalf of the Projeto DCJ - Lito team
Brazil · [contact email]

---
*NOTA INTERNA (não enviar): preencher [NAME]/[email]; anexar manuscrito em PDF quando existir; enviar SÓ depois do OK do senhor.*
