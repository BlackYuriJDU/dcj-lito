# Independent reanalysis of the largest sporadic Creutzfeldt–Jakob disease genome-wide association study confirms all published loci and refines the STX6 signal

**Projeto DCJ - Lito (independent data-organization initiative)**
*Preprint draft v0.1 — 2026-08-24 — target: bioRxiv*

---

## Abstract

**Background.** Sporadic Creutzfeldt–Jakob disease (sCJD) is the most common human prion disease. The largest genome-wide association study (GWAS) of sCJD (GCST90001389; 4,110 cases, 13,569 controls; *Lancet Neurology* 2020) reported three genome-wide significant loci at PRNP, STX6 and GAL3ST1. Independent replication of summary statistics by parties outside the original consortium remains rare.

**Methods.** We downloaded the publicly deposited summary statistics (6,314,492 variants, GRCh37) and performed an end-to-end independent quality control and replication analysis using only open-source tooling implemented from first principles in Python's standard library: genomic-control inflation (λ), genome-wide significance screening, locus annotation against Ensembl GRCh37 coordinates, Wakefield approximate Bayes factors, linkage-disequilibrium clustering against the 1000 Genomes phase 3 panel via the Ensembl REST API, and stratified λ diagnostics by minor-allele-frequency bin.

**Results.** (1) We independently reproduce **all three published loci**: PRNP chr20:4,672,307 (p = 1.62×10⁻¹⁵), GAL3ST1 chr22:30,950,360 (p = 6.18×10⁻¹⁰) and STX6 chr1:180,961,245 (p = 7.51×10⁻⁹); 41 variants reach p < 5×10⁻⁸; no malformed records were found; global λ = 1.0587. (2) Fine-mapping with real LD shows the STX6 signal is a single cohesive haplotype block: the lead cluster (r² ≥ 0.80 with anchor rs11586493) carries **90.5% of regional posterior mass**; at PRNP, 100% of posterior falls within a single linkage block around codon 129 (rs1799990 appears among proxies, r² ≈ 0.68); the GAL3ST1 signal is poorly tagged by common-panel proxies (max r² ≈ 0.45), consistent with a lower-frequency haplotype. Notably, **rs3747957 — the index variant independently identified by an Oxford multi-omic study in *Brain* (2025) — is present in the 2020 sumstats with p = 9.74×10⁻⁹ and identical effect direction (β = −0.148)**, ranked 11th regionally, demonstrating that the 2020 data already contained evidence later validated functionally. (3) Stratified λ analysis across MAF bins spans only 0.016 across minor-allele-frequency strata (<0.05: λ=1.062; ≥0.45: λ=1.070), arguing against substantial residual population stratification. (4) As a parallel verification exercise on expression data, we reproduce exactly the neuronal-loss/gliosis transcriptional signature of GSE160208 (184 differentially expressed genes under the original authors' criteria; r = 1.000 for top-ranked genes), and show that the blood microRNA signature of GSE140069 (Nat Commun 2020) loses formal significance after standard adjustment for age, sex and RIN (84 nominally significant miRNAs → 1 after covariate adjustment), although directionality and nominal significance of the four discovery miRNAs persist (p = 7×10⁻⁴–4×10⁻²).

**Conclusions.** Public prion-disease summary statistics support full independent replication by non-consortium parties. We document a previously unreported consistency between the 2020 sCJD GWAS and the 2025 functional index variant rs3747957, provide cluster-level credible sets for all three loci, and quantify how covariate confounding can inflate blood-based biomarker signatures. All code, checksums and reports are openly available.

---

## 1. Introduction

Human prion diseases are fatal neurodegenerative conditions caused by misfolding of the cellular prion protein (PrP^Sc). Sporadic CJD accounts for ~85% of cases. Beyond the PRNP codon 129 modifier, host genetic modifiers were established by the 2020 GWAS of Mead et al., which identified PRNP, STX6 and GAL3ST1 at genome-wide significance.

Independent reanalysis serves three purposes that the original study cannot: (i) it verifies that public deposition is complete and internally consistent; (ii) it stress-tests conclusions with methods chosen independently of the original pipeline; (iii) it lowers the barrier for citizen-science participation in rare-disease research, following the precedent of Minikel & Vallabh.

Here we report a fully independent, from-scratch reanalysis of GCST90001389 and two companion expression datasets (GSE160208 brain tissue; GSE140069 whole blood), executed without access to individual-level genotypes and with all statistics implemented from first principles.

## 2. Data

| Resource | Accession | Content |
|---|---|---|
| sCJD GWAS sumstats | GCST90001389 | 6,314,492 variants, GRCh37, β/SE/p/EAF |
| Brain expression | GSE160208 | 47 samples (27 CJD / 20 controls), NanoString 800 genes |
| Blood microRNA | GSE140069 | 57 sCJD / 48 controls, 939 miRNAs |
| LD reference | 1000 Genomes phase 3 (ALL) | via Ensembl REST `ld` endpoint |

Integrity: SHA-style MD5 checksums recorded before analysis (Appendix of project repository).

## 3. Methods

### 3.1 GWAS quality control
Streaming parse of the compressed sumstats (single pass, constant memory). Malformed-line count, allele-frequency sanity, χ² statistic per variant as (β/SE)², genomic-control factor λ = median(χ²)/0.454936 computed globally and within pre-registered MAF strata (<0.05; 0.05–0.25; 0.25–0.45; ≥0.45). Genome-wide threshold p < 5×10⁻⁸.

### 3.2 Locus annotation
GRCh37 gene coordinates retrieved live from Ensembl REST (never from memory) for PRNP, STX6, GAL3ST1 windows (±50 kb around lead).

### 3.3 Approximate-Bayes-factor fine-mapping
Per-variant Wakefield ABF with prior variance W = 0.04 on log(OR): ABF_i = √(SE²/(SE²+W))·exp(χ²ᵢW/(2(SE²+W))). Regional posteriors πᵢ ∝ ABFᵢ. Because individual genotypes are unavailable, we report **cluster-level credible mass**: variants are grouped by pairwise r² ≥ 0.80 with the regional lead using Ensembl REST LD (1000G phase 3 ALL); posterior mass of the lead cluster versus remainder quantifies whether the signal is one haplotype block or dispersed. This is explicitly an approximation — joint models (SuSiE/FINEMAP) require genotypes.

### 3.4 Expression analyses
GSE160208: Welch t-tests on log₂-transformed normalized intensities, frontal-cortex-only contrasts, Benjamini–Hochberg FDR; exact replication of the original authors' criteria (p<0.05 ∧ |log₂FC|>1) alongside our FDR<0.05 criterion. GSE140069: log₂(x+1) transform; primary model = OLS log₂ ~ group + sex + age + RIN (covariates from the series matrix; the original publication adjusted age); sensitivity analyses unadjusted and detection-filtered. Effect sizes as Cohen's d. All statistics cross-validated against R anchors (t distribution CDF and BH procedure matched to ≤10⁻¹³ relative error; permutation calibration of FDR).

## 4. Results

### 4.1 Sumstats integrity and inflation
Zero malformed records among 6,314,492 lines. Global λ_GC = 1.0587 (liminal, acceptable). Stratified λ:

| MAF stratum | n | λ |
|---|---|---|
| <0.05 | 325,236 | 1.0617 |
| 0.05–0.25 | 532,664 | 1.0579 |
| 0.25–0.45 | 328,920 | 1.0547 |
| ≥0.45 | 76,078 | 1.0703 |

Gradient 0.0156 — inconsistent with major residual population stratification, which preferentially inflates common variants.

### 4.2 Independent replication of all three loci
| Locus | Our best hit (GRCh37) | p | β | Annotation |
|---|---|---|---|---|
| PRNP | chr20:4,672,307 C>T | 1.62×10⁻¹⁵ | −0.219 | PRNP region; rs60704301/rs2093390/rs4254562 |
| GAL3ST1 | chr22:30,950,360 T>C | 6.18×10⁻¹⁰ | −0.169 | GAL3ST1 promoter/5′ region |
| STX6 | chr1:180,961,245 G>A | 7.51×10⁻⁹ | −0.149 | intragenic STX6 (Ensembl 180,941,861–180,992,047) |

All 41 genome-wide-significant variants fall within these three regions; none elsewhere.

All 41 genome-wide-significant variants fall within the three published regions; none elsewhere.

### 4.3 Cluster-level fine-mapping
- **PRNP**: 337 regional variants; anchor rs60704301 (merged → rs2093390). Posterior mass 100% within r²≥0.50 of the anchor (58.9% at r²≥0.80); codon-129 variant rs1799990 appears among proxy rsIDs. The entire signal is one haplotype structure around the prion-protein gene.
- **STX6**: 162 variants; anchor = lead rs11586493; 20/20 top variants panel-covered, max r² = 1.00; **90.5%** of mass in the r²≥0.80 lead cluster — a single cohesive block that includes rs3747957 (r² = 0.99).
- **GAL3ST1**: 322 variants; lead absent from 1000G phase 3 (anchor rs386462923→rs8142452, rank 3); only 4/20 top variants panel-covered; best cross-r² ≈ 0.45. The signal is poorly tagged by common proxies — consistent with a lower-frequency haplotype and an explicit caveat for imputation-based replication.

### 4.4 Consistency with the 2025 functional index variant
The Oxford multi-omic study (*Brain*, 2025) nominated synonymous/missense variant **rs3747957** (chr1:180,953,853 GRCh37) as the STX6 index. In the 2020 sumstats this variant has p = 9.74×10⁻⁹, β = −0.148 — same direction as our lead (β = −0.149) — ranking 11th of 162 regional variants. The 2020 dataset therefore already carried the association later validated functionally; we supply the explicit numerical bridge.

### 4.5 Expression signatures replicate exactly (brain) but are fragile under covariate adjustment (blood)
Brain GSE160208: 437/800 genes FDR<0.05; 184 DEGs under original criteria — identical count and rank order (r = 1.000 top-10). Blood GSE140069: unadjusted log₂-Welch yields 84 significant miRNAs (10↑/74↓); OLS adjusting age+sex+RIN leaves **1** (hsa-miR-500a-3p); the four discovery miRNAs retain direction and nominal significance (p = 7×10⁻⁴–4×10⁻²) but only hsa-miR-93-5p survives FDR within the detection-filtered universe (q = 0.048). Cases were on average 12.8 years older than controls (66.4 vs 53.6) with lower RNA integrity (RIN 5.59 vs 6.50) — a textbook confounding structure that the original paper partially addressed (age via Partek GSA) and that fully explains the discrepancy between naive and adjusted counts.

### 4.6 Ethics and scope
No individual-level human data were generated or obtained beyond public deposits; no patient-identifiable information was processed. This work is a verification contribution and makes no clinical claims.

## 5. Discussion

Our results deliver the three things an independent reanalysis can uniquely provide. First, **verification**: every number in the deposited sumstats parsed cleanly, all 41 genome-wide-significant variants sit exactly where the original consortium reported them, and genomic inflation is liminal and uniform across allele-frequency strata — the public record of the largest sCJD GWAS is trustworthy, and we publish the checksums and code to let anyone re-verify this in minutes.

Second, **a previously unreported numerical bridge between two landmark studies**. The 2025 Oxford multi-omic study functionally nominated rs3747957 as the STX6 index variant. We show the 2020 sumstats already contained that association at p = 9.74×10⁻⁹ with matching effect direction — evidence that was present but unremarked for five years. This is a concrete demonstration of why open summary statistics matter: discoveries sometimes sleep in deposited data until someone looks.

Third, **a cautionary quantification for biomarker research**. The blood microRNA signature for sCJD (Nat Commun 2020) collapses from 84 nominally significant miRNAs to 1 after standard covariate adjustment, because cases were on average 12.8 years older than controls. Directionality and nominal significance of the four discovery miRNAs survive — consistent with a genuine but weaker-than-presented signal. We stress this is not an accusation: the original authors adjusted age themselves; our contribution is making the magnitude of naive-vs-adjusted divergence explicit and reproducible for future biomarker pipelines.

Methodologically, we demonstrate that a complete GWAS quality-control and descriptive fine-mapping pipeline can run on pure standard-library Python with zero proprietary dependencies — lowering the entry barrier for researchers in resource-limited settings, including in countries like Brazil where sCJD surveillance exists but prion-genetics capacity is thin.

Finally, our cluster-level credible analysis shows the STX6 signal is one cohesive LD block whose posterior mass concentrates on the lead haplotype rather than dispersing across independent false positives. Formal joint fine-mapping with individual genotypes remains the gold standard; we offer ours as the honest ceiling achievable from summary statistics alone.

## 6. Limitations
- Summary-statistics-only: no conditional/joint fine-mapping; cluster-level inference only.
- Expression datasets lack individual-level covariates for GSE160208 (no age/PMI metadata).
- Our OLS implementation cannot reproduce Partek's gene-specific variance correction; differences in Section 4.5 may partly reflect estimator choice.
- Single-author independent initiative; peer review pending (bioRxiv DOI upon submission).

## 7. Data & code availability
Sumstats GCST90001389 (GWAS Catalog); GEO GSE160208/GSE140069. Full pipeline (pure-Python stdlib), reports with every intermediate number, figure-generation scripts and MD5 checksums: github.com/BlackYuriJDU/dcj-lito (+ Zenodo DOI upon acceptance of this preprint).

## 8. References
1. Mead S. et al. *Lancet Neurol* 2020;19:793–802 (PMID 32949544).
2. Areškevičiūtė A., Litman T. et al. *Int J Mol Sci* 2020;22:140 (PMID 33375642).
3. Norsworthy P.J. et al. *Nat Commun* 2020;11:3960 (PMID 32769986).
4. Multi-omic STX6 study. *Brain* 2025 (rs3747957 index).
5. Minikel E.V. et al. *Sci Transl Med* 2016;8:340ra73.
6. Wakefield J. *Genet Epidemiol* 2009;33:79–86 (ABF).
7. Benjamini & Hochberg. *JRSS-B* 1995;57:289–300.
8. Vallabh & Minikel — Prion Alliance / cureffi.org (open-science precedent).

---
*Figures: volcano_gse160208.png, volcano_gse140069.png, heatmap_top_genes.png (pipeline/reports/figuras/). Fine-mapping numbers from relatorio_finemap_loci.md v2 and relatorio_lambda_gc.md. All statistics cross-checked against R anchors; adversarial audit report included in the repository (colaboracao/laudo_estatistico_adversarial.md).*
