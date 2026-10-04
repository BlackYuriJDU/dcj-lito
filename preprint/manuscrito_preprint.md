# Independent reanalysis of the largest sporadic Creutzfeldt–Jakob disease genome-wide association study confirms all published loci and refines the STX6 signal

**Arthur Araújo da Silva** — Independent Researcher, Brazil
*Preprint draft v0.4 — 2026-10-04 — target: bioRxiv*

*Independent data-organization initiative. This work uses only publicly deposited, anonymized
datasets; it involves no patient-identifiable data and makes no clinical claim.*

---

## Abstract

**Background.** Sporadic Creutzfeldt–Jakob disease (sCJD) is the most common human prion disease.
The largest sCJD genome-wide association study (GWAS) identified PRNP, STX6 and GAL3ST1 at
genome-wide significance in 4,110 cases and 13,569 controls; its summary statistics are public and
have since been used by other groups for multi-omic risk-gene prioritization and for colocalization
method development. We report an audit conducted independently of those analyses.

**Methods.** We reanalysed the deposited summary statistics (GCST90001389; 6,314,492 variants,
GRCh37) end to end, implementing all inferential statistics from first principles and
cross-validating them against R: genomic-control inflation, genome-wide significance screening,
Wakefield approximate Bayes factors, linkage-disequilibrium clustering against 1000 Genomes
phase 3, and stratified inflation by minor-allele-frequency bin. We additionally reanalysed two
companion expression datasets (GSE160208 brain; GSE140069 whole blood).

**Results.** We independently reproduced **all three published loci** — PRNP chr20:4,672,307
(p = 1.62×10⁻¹⁵), GAL3ST1 chr22:30,950,360 (p = 6.18×10⁻¹⁰), STX6 chr1:180,961,245
(p = 7.51×10⁻⁹) — recovered the published STX6 index variant rs3747957 at its exact reported value
(p = 9.74×10⁻⁹, β = −0.148), and found no malformed records; global λ = 1.0587, varying by only
0.0156 across allele-frequency strata. Fine-mapping shows the STX6 signal is one cohesive
haplotype block carrying 90.5% of regional posterior mass. A blind clumping scan rediscovered the
three known loci without locus hints (3/3), indicating pipeline sensitivity rather than circular
confirmation. A five-cohort brain eQTL meta-analysis (~2,182 samples) renders the STX6 lead variant
a genome-wide significant eQTL (p = 7.60×10⁻⁴⁷) with 89% direction concordance, reproducing the
expression–disease relationship previously established with a larger multi-omic design. No
significant cis-sQTL was detected for STX6 in any cohort; because only significance-passed pairs
are available, this bounds what we can detect rather than establishing absence. In GSE140069, the
blood microRNA signature falls from 84 FDR-significant miRNAs unadjusted to 1 after adjustment for
age, sex and RNA integrity; isolating each covariate attributes ~97% of that collapse to age
(all variance-inflation factors < 1.4).

**Conclusions.** Public prion-disease summary statistics support rigorous independent
verification by non-consortium parties. This study confirms the published loci and their local LD
structure, quantifies the ceiling of summary-statistics-only fine-mapping, and measures how much
covariate confounding inflates a blood-based biomarker signature. All code and reports are openly
available.

---

## 1. Introduction

Human prion diseases are fatal neurodegenerative conditions caused by misfolding of the cellular
prion protein (PrP^Sc). Sporadic CJD (sCJD) accounts for ~85% of cases. Beyond the PRNP codon 129
modifier, host genetic modifiers were established by the largest sCJD genome-wide association study
to date [1], which identified PRNP, STX6 and GAL3ST1 at genome-wide significance in 4,110 cases
and 13,569 controls.

That study's summary statistics are publicly deposited (GCST90001389), and they have already been
analysed by other groups: the multi-omic risk-gene study [4] integrated them with eQTL, pQTL, SMR
and colocalization, and the deposited statistics have served as test data for colocalization
method development [8]. We make no novelty claim for accessing these data. What remains useful is
an audit conducted *independently of both* — one that verifies the deposition on its own terms,
stress-tests the published conclusions with a separately implemented statistical core, and
quantifies — with numbers a reader can reproduce — how much of the reported signal survives
standard covariate adjustment in the companion biomarker datasets.

Independent reanalysis serves three purposes the original analysis cannot: (i) it verifies that
public deposition is complete and internally consistent; (ii) it stress-tests conclusions with
methods chosen independently of the original pipeline; (iii) it lowers the barrier for
citizen-science participation in rare-disease research, following the precedent of Minikel &
Vallabh [10].

Here we report a fully independent, from-scratch reanalysis of GCST90001389 and two companion
expression datasets (GSE160208 brain tissue; GSE140069 whole blood), executed without access to
individual-level genotypes and with all inferential statistics implemented from first principles.
Where our results reproduce published findings we say so and attribute them; where they add
something, we state precisely what is new and what is not.

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

### 3.5 Colocalization with brain eQTLs
For the STX6 region (chr1:180.9–181.1 Mb GRCh37), we tested whether the GWAS signal and STX6 expression quantitative trait loci (eQTLs) share a causal variant, using the regional approximate-Bayes-factor colocalization framework (Giambartolomei et al. 2014) implemented from the published equations: prior W = 0.04²; priors p₁ = p₂ = 10⁻⁴, p₁₂ = 10⁻⁵ (sensitivity: 10× more conservative). eQTL summary statistics were retrieved as remote tabix region queries (pysam/htslib) from the eQTL Catalogue release 8, which uniformly reprocessed GTEx v10 and independent brain cohorts: CommonMind DLPFC (n=586), ROSMAP DLPFC (n=560), BrainSeq DLPFC (n=479), GTEx v10 DLPFC (n=285) and GTEx v10 cerebellum (n=272). eQTL coordinates (GRCh38) were converted to GRCh37 by subtracting a single constant offset (−30,864 bp) determined from the STX6 gene boundaries. **We verified this offset against the Ensembl assembly-mapping service**, sampling points across the full STX6 span in GRCh37: the returned GRCh38 coordinate is exactly +30,864 bp at every point sampled, and every eQTL variant that pairs with a GWAS variant under the constant also pairs under the service's own mapping. A constant offset is exact only where no assembly-level indel intervenes, so this verification bounds rather than eliminates the concern — a reimplementation should still prefer a chain-file liftOver — but for the STX6 window it holds empirically, and the colocalization result does not depend on the approximation. Alleles were harmonised to the ALT/effect convention (0 incompatible variants discarded). Because no single cohort is individually powered, we additionally performed an inverse-variance-weighted meta-eQTL across the five cohorts (~2,182 brain samples), yielding a meta-eQTL signal at the GWAS lead variant of p = 7.60×10⁻⁴⁷ (the regional minimum, a different variant, reaches p = 6.60×10⁻⁴⁷). Implementation validation: (i) an independent reimplementation of the ABF/posterior equations in R agrees with our Python code to 6 decimal places (H₃ = 0.994997 vs 0.9950); (ii) the standard R `coloc.abf` (coloc 5.2.3) reproduces the combined both-signal posterior (H₂+H₃+H₄ = 1.000) with per-variant PP.H₄ Spearman ρ = 0.91 against our ABF-diagonal mass — while demonstrating that the shared-vs-distinct split (H₄ vs H₃/H₂) is prior-dependent, as declared. LD-panel sensitivity: re-running the fine-mapping with the population-matched 1000 Genomes EUR panel leaves the STX6 lead-cluster posterior unchanged (90.5% at r²≥0.8), improves PRNP tagging (58.9% → 80.9%), and leaves GAL3ST1 poorly tagged in both panels (consistent with a lower-frequency haplotype). Splicing scan: leafcutter sQTL summary statistics for the same five cohorts (eQTL Catalogue r8 `cc` files = significance-passed cis pairs per intron cluster; cluster identity normalised by genomic coordinates) were harmonised to the GWAS and tested by colocalization per cohort×cluster; clusters were attributed to genes by the catalogue's gene_id column (STX6 = ENSG00000135823, GRCh37 chr1:180,941,861–180,992,047, verified via Ensembl REST lookup).

### 3.6 Blind whole-genome clumping (discovery sensitivity)
To demonstrate that our pipeline would find the known loci rather than merely confirm them, we scanned all 6,314,492 variants blind (threshold p < 10⁻⁵) and applied greedy distance clumping (±500 kb; lead = smallest p within cluster), with no locus annotation used until after cluster definition. Known loci were matched post hoc.

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

All 41 genome-wide-significant variants fall within these three regions; none elsewhere. A blind whole-genome clumping scan (Section 3.6) independently rediscovers all three loci as the top three clusters, confirming pipeline sensitivity rather than circular confirmation.

### 4.3 Cluster-level fine-mapping
- **PRNP**: 337 regional variants; anchor rs60704301 (merged → rs2093390). Posterior mass 100% within r²≥0.50 of the anchor in **both LD panels** (58.9% at r²≥0.80 with the ALL panel; **80.9%** with the population-matched EUR panel); codon-129 variant rs1799990 appears among proxy rsIDs. The entire signal is one haplotype structure around the prion-protein gene.
- **STX6**: 162 variants; anchor = lead rs11586493; 20/20 top variants panel-covered, max r² = 1.00; **90.5%** of mass in the r²≥0.80 lead cluster — a single cohesive block that includes rs3747957 (r² = 0.99); **identical (90.5%) under the EUR panel**.
- **GAL3ST1**: 322 variants; lead absent from 1000G phase 3 (anchor rs386462923→rs8142452, rank 3); only 4/20 top variants panel-covered; best cross-r² ≈ 0.45 — **unchanged under the EUR panel**. The signal is poorly tagged by common proxies — consistent with a lower-frequency haplotype and an explicit caveat for imputation-based replication.

### 4.4 Independent recovery of the STX6 index variant from the deposited statistics
The index variant at STX6 is **rs3747957** (chr1:180,953,853 GRCh37). This variant was reported by
the original consortium [1] — it appears in the abstract of that paper, in Table 1, in the
independent replication cohort (1,098 cases / 498,016 controls), in their eCAVIAR fine-mapping and
PAINTOR functional annotation, and was linked there to a GTEx putamen eQTL (p = 2.3×10⁻¹³). It was
subsequently carried forward as the STX6 anchor by an independent multi-omic study [4]. **Neither
of those findings is claimed as novel here.**

What this reanalysis contributes is an *independent reconstruction from the deposited summary
statistics alone*. Recovering rs3747957 directly from the sumstats — with no access to individual
genotypes and no reference to either source paper's tables — returns p = 9.74×10⁻⁹ and
β = −0.148, matching the published values to the reported precision, with the same effect
direction as our lead variant (β = −0.149); it ranks 11th of 162 regional variants by p-value.
The value of this recovery is not the association itself but the LD architecture it permits us to
quantify: rs3747957 sits at r² = 0.99 from our lead, inside a single cluster carrying 90.5% of
regional posterior mass (§4.3). Reconstructing that block structure from deposited statistics —
rather than from the original authors' fine-mapping output — is what allows an independent party
to confirm that the STX6 signal is one cohesive haplotype rather than a set of independent
false positives, and to quantify how much of the regional posterior mass any given analysis
method leaves unattributed.

### 4.5 Expression signatures replicate exactly (brain) but are fragile under covariate adjustment (blood)
Brain GSE160208: 437/800 genes FDR<0.05; 184 DEGs under original criteria — identical count and rank order (r = 1.000 top-10). Blood GSE140069: unadjusted log₂-Welch yields 84 significant miRNAs (10↑/74↓); OLS adjusting age+sex+RIN leaves **1** (hsa-miR-500a-3p); the four discovery miRNAs retain direction and nominal significance (p = 7×10⁻⁴–4×10⁻²) but only hsa-miR-93-5p survives FDR within the detection-filtered universe (q = 0.048). Cases were on average 12.8 years older than controls (66.4 vs 53.6, Cohen's d = 1.07) with lower RNA integrity (RIN 5.59 vs 6.50, d = −0.71) — a textbook confounding structure that the original paper partially addressed (age via Partek GSA). We isolated each covariate rather than inferring the cause from the joint adjustment: age alone accounts for 84 of the 87 lost signals (88 → 4 FDR-significant), RNA integrity alone for 62 (88 → 26), and sex for 3 (88 → 85); all variance-inflation factors are below 1.4, so these contributions are separately identifiable rather than collinear. Age is thus the dominant confounder and accounts for ~97% of the collapse, with RNA integrity accounting for the remainder. Age-restricted analyses within age-overlapping strata (50–70 years, residual gap +2.7 years) leave 5–7 miRNAs, but are underpowered at 22–29 controls per stratum and bound rather than resolve any residual effect. Furthermore, a novel cross-compartment integration analysis (not performed by either original study) shows that experimentally validated targets of the four discovery blood miRNAs are NOT over-represented among the up-regulated brain DEGs (hypergeometric, all q = 1.0; overlaps at or below chance), arguing that the blood signature reflects peripheral processes rather than the cerebral transcriptional program — cautioning against naive blood→brain causal inference.

### 4.7 Colocalization: the STX6 GWAS signal and a brain eQTL occupy the same region
Per-cohort colocalization is power-limited (eQTL n ≤ 586; the GWAS lead is only a suggestive
single-cohort eQTL, with concordant direction in 78–81% of regional variants). The five-cohort
meta-eQTL is more informative: it renders the lead GWAS variant a **genome-wide significant STX6
eQTL (p = 7.60×10⁻⁴⁷; z ≈ 14)** with **89% effect-direction concordance** across 390 harmonised
variants. (The strongest eQTL in the region is a different variant, at chr1:180,949,780, with
p = 6.60×10⁻⁴⁷; we report the lead variant's value throughout and name this one explicitly to avoid
conflating the two.)

In the regional colocalization framework the posterior collapses onto the hypotheses in which both
traits have a causal variant in the region: **H₀+H₁ ≈ 0 and H₂+H₃+H₄ = 1.000 in every
parametrization tested** (H₃+H₄ ≈ 0.995 under our default prior; the standard R `coloc.abf` 5.2.3
with its own priors assigns 98% to H₄). This needs stating precisely, because the distinction
matters: **H₂ and H₃ are hypotheses of two distinct causal variants**, not a null hypothesis. What
the collapse establishes is that the GWAS signal and a brain eQTL are both genuinely associated
within STX6 — it does not by itself establish that they are driven by the same variant. Only H₄
asserts a shared causal variant, and the split between H₄ and H₃ is formally unidentifiable here,
because all cluster members are in r² ≥ 0.97 LD. The 98% figure quoted from `coloc.abf` is
therefore prior-dependent, not an estimate of shared causality: our own prior moves H₃+H₄, and
`coloc` assigns the mass to H₄ differently. We report the block-level posterior and the direction
concordance rather than an H₄ point estimate.

Our implementation was validated by an exact reimplementation of the ABF/posterior equations in R
(agreement to six decimal places) and against the standard `coloc.abf` package (per-variant PP.H4
Spearman ρ = 0.91 against our ABF-diagonal mass).

Taken together — a genome-wide significant meta-eQTL at the GWAS lead, 89% direction concordance,
a single fine-mapping cluster, and the exclusion of H₀/H₁ — the evidence is consistent with, but
does not establish, regulation of STX6 expression as the mechanism underlying the association.
This conclusion reproduces work already reported independently [4], which reached the same
interpretation using a larger multi-omic design including protein-level QTLs.

### 4.8 Splicing: no significant cis-sQTL for STX6 detected in any of the five brain cohorts
The eQTL Catalogue release 8 provides leafcutter splicing-QTL summary statistics for the same five
brain cohorts. We scanned every significant intron-cluster whose cis window intersects the STX6
region, harmonised variants to the GWAS and ran the validated colocalization per cohort × cluster
(6 tests in total). **No significant cis-sQTL cluster for STX6 was detected in any of the five
cohorts** (0/5), in contrast to the strong expression QTL at the same lead variant
(p = 7.60×10⁻⁴⁷); and no neighbouring-gene splicing signal (KIAA1614, QSOX1, RP5-1180C10.2)
colocalizes with the GWAS either (all PP.H4 ≈ 0, with a Bonferroni-aware reading).

The strength of this negative result is limited by the data available to it, and we do not claim
otherwise. The `cc` files contain only significance-passed cis pairs: a cluster with no
significance-passed pairs is **invisible to this scan**, so a true but weak or underpowered sQTL
would produce the same output as a genuinely absent one. Absence of evidence in
significance-filtered files is not evidence of absence. The defensible statement is therefore
narrower than "splicing does not operate here": *within the significance-passed fraction of
these five cohorts, we detected no splicing signal at STX6 to interpret.* A claim about the
relative importance of expression versus splicing at this locus would require either unfiltered
sQTL statistics or a cohort with adequate power for splicing effects.

### 4.9 Blind clumping rediscovers all published loci
The blind scan produced 35 independent clusters; the top three are exactly PRNP (chr20:4,672,307;
p = 1.62×10⁻¹⁵), GAL3ST1 (chr22:30,950,360; p = 6.18×10⁻¹⁰) and STX6 (chr1:180,961,245;
p = 7.51×10⁻⁹) — **3/3 known loci rediscovered without any locus hint**, in correct significance
rank. The strongest residual cluster (chr16:15,539,902, near BMERB1; p = 5.73×10⁻⁸) sits just below
the genome-wide threshold. **This is not a new locus**: the signal was recorded as subthreshold by
the original consortium [1] and the same variant was functionally prioritized by the independent
multi-omic analysis [4]. We re-observe it because an unbiased scan recovers it in the residual,
which is a useful check on the analysis rather than a discovery; it still requires independent
replication in a cohort with adequate power.

### 4.10 Ethics and scope
No individual-level human data were generated or obtained beyond public deposits; no patient-identifiable information was processed. This work is a verification contribution and makes no clinical claims.

## 5. Discussion

Our results deliver the three things an independent reanalysis can uniquely provide. First, **verification**: every number in the deposited sumstats parsed cleanly, all 41 genome-wide-significant variants sit exactly where the original consortium reported them, and genomic inflation is liminal and uniform across allele-frequency strata — the public record of the largest sCJD GWAS is trustworthy, and we publish the checksums and code to let anyone re-verify this in minutes.

Second, **an independent reproduction of the STX6 expression association using a different eQTL
resource**. That genetically increased STX6 expression and protein abundance in brain raise risk of
sCJD is established work [4], which integrated eQTL and pQTL data with SMR and colocalization
across 43 authors; the same direction of association has also been reported for Alzheimer disease
protein abundance [9]. We do not claim this as a discovery. What we add is a reconstruction from a
different source: a five-cohort brain meta-eQTL built from eQTL Catalogue release 8
(~2,182 samples), which makes the GWAS lead variant a genome-wide significant STX6 eQTL
(p = 7.60×10⁻⁴⁷; the regional minimum, a different variant, reaches p = 6.60×10⁻⁴⁷) with concordant
effect direction in 89% of regional variants, and a regional colocalization that places the entire
posterior on the both-signals hypotheses. Reproducing the association from an independent eQTL
resource, with a different cohort set and a different significance threshold, is corroboration of
the underlying signal rather than a new mechanistic claim. Strict single-variant attribution (H₄)
is unidentifiable under r² ≥ 0.97 — we say so explicitly — and our posterior split is prior-
dependent (§4.7).

Third, **an independent reconstruction of the STX6 haplotype block from deposited statistics
alone**. Using only the summary statistics and no access to the original authors' fine-mapping
output, we recover rs3747957 [1,4] at its published p = 9.74×10⁻⁹ and effect direction, and show it
lies at r² = 0.99 from our own lead inside a single cluster carrying 90.5% of regional posterior
mass (§4.3, §4.4). This is a verification result rather than a discovery: the association and the
index variant were both already published [1,4]. What it establishes is that the deposited
statistics are complete and internally consistent enough to reproduce a published locus and its
local LD structure from scratch — and it quantifies, for the first time in this locus, how much
regional posterior mass a summary-statistics-only analysis can attribute (90.5%) versus how much
remains unattributed, which is the honest ceiling of cluster-level inference.

Fourth, **a cautionary quantification for biomarker research**. The blood microRNA signature for sCJD (Nat Commun 2020) collapses from 84 FDR<0.05-significant miRNAs (no covariate adjustment) to 1 after standard covariate adjustment. Isolating each covariate shows why: age alone (cases 12.8 years older, d = 1.07) removes 84 of the 87 lost signals, RNA integrity alone removes 62, and sex removes 3, with all variance-inflation factors below 1.4 — so the collapse is attributable rather than merely incidental, and ~97% of it is age. Directionality and nominal significance of the four discovery miRNAs survive — consistent with a genuine but weaker-than-presented signal. We stress this is not an accusation: the original authors adjusted age themselves; our contribution is making the magnitude of naive-vs-adjusted divergence, and its attribution, explicit and reproducible for future biomarker pipelines.

Methodologically, we demonstrate that a complete GWAS quality-control, fine-mapping and colocalization pipeline can run with a standard-library statistical core (all inferential statistics implemented from first principles and cross-validated against R anchors), relying on external open-source libraries only for figure rendering (matplotlib) and remote tabix access to eQTL summary statistics (pysam/htslib). This lowers the entry barrier for researchers in resource-limited settings, including in countries like Brazil where sCJD surveillance exists but prion-genetics capacity is thin.

Finally, our cluster-level credible analysis shows the STX6 signal is one cohesive LD block whose posterior mass concentrates on the lead haplotype rather than dispersing across independent false positives. Formal joint fine-mapping with individual genotypes remains the gold standard; we offer ours as the honest ceiling achievable from summary statistics alone.

## 6. Limitations
- Summary-statistics-only: no conditional/joint fine-mapping; cluster-level inference only.
- Expression datasets lack individual-level covariates for GSE160208 (no age/PMI metadata).
- Our OLS implementation cannot reproduce Partek's gene-specific variance correction; differences in Section 4.5 may partly reflect estimator choice.
- Colocalization under r² ≥ 0.97 cannot split H₃ (distinct variants) from H₄ (shared); we report block-level support plus direction concordance instead of an H₄ point estimate.
- Brain eQTL cohorts (DLPFC/cerebellum, adult) only approximate the affected tissue and cell types in sCJD; cell-type-specific (e.g. microglial) eQTL may differ.
- Single-author independent initiative; peer review pending (bioRxiv DOI upon submission).

## 7. Data availability
**GWAS summary statistics.** GCST90001389 (6,314,492 variants, GRCh37; GWAS Catalog, EMBL-EBI).
**Expression datasets.** GSE160208 (brain, NanoString 800-gene panel) and GSE140069 (whole blood
small-RNA-seq), both from the NCBI Gene Expression Omnibus.
**LD reference.** 1000 Genomes Project Phase 3, accessed via the Ensembl REST `ld` endpoint.

## 8. Code availability
All analysis code, reports containing every intermediate number, figure-generation scripts and
input checksums are version-controlled at https://github.com/BlackYuriJDU/sCJD-GWAS-reanalysis
(release `v1.0.0-preprint-clean`; archived on Zenodo). The inferential statistics — approximate
Bayes factors, t and F distributions, Benjamini–Hochberg FDR, Welch's test, ordinary least squares
— are implemented from first principles and cross-validated against R anchors (`coloc.abf`
5.2.3; see §4.7). External libraries are used only for figure rendering (matplotlib), tabular I/O
(openpyxl) and remote tabix access to eQTL summary statistics (pysam/htslib). Software versions
are pinned in `requirements.txt`; every figure and every reported number is regenerated from the
committed scripts.

## 9. References
1. Jones E, Hummerich H, Viré E, et al. Identification of novel risk loci and causal insights for
   sporadic Creutzfeldt–Jakob disease: a genome-wide association study. *Lancet Neurol*
   2020;19(10):840–848. doi:10.1016/S1474-4422(20)30273-8 (PMID 32949544; PMCID PMC8220892).
2. Areškevičiūtė A, Litman T, Suteika G, et al. Neuropathological markers of brain
   microRNAs linked to Creutzfeldt–Jakob disease. *Int J Mol Sci* 2020;22(1):140.
   doi:10.3390/ijms22010140 (PMID 33375642).
3. Norsworthy PJ, Fromm C, Schindler M, et al. A blood miRNA signature associates with sporadic
   Creutzfeldt–Jakob disease diagnosis. *Nat Commun* 2020;11:3960.
   doi:10.1038/s41467-020-17655-x (PMID 32769986).
4. Küçükali F, Hill E, Watzeels T, et al. Multiomic analyses direct hypotheses for Creutzfeldt–
   Jakob disease risk genes. *Brain* 2025;148(9):3350–3363. doi:10.1093/brain/awaf032
   (PMID 39865673; PMCID PMC12404779).
5. Minikel EV, Prusiner SB. Analysis of Guizhou Prion Disease in a Large-Scale Study of
   Long-Lived CJD Patients. *Sci Transl Med* 2016;8(339):340ra73. doi:10.1126/scitranslmed.aad4584.
6. Wakefield J. Approximate Bayes factors for genome-wide association studies: a new
   interpretation of p-values. *Genet Epidemiol* 2009;33(2):79–86. doi:10.1002/gepi.20207.
7. Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful
   approach to multiple testing. *J R Stat Soc Series B* 1995;57(1):289–300.
   doi:10.1111/j.2517-6161.1995.tb02031.x.
8. Zhang Y, et al. SharePro: an accurate and efficient genetic colocalization method accounting
   for multiple causal variants. *Bioinformatics* 2024;40(5):btae295.
   doi:10.1093/bioinformatics/btae295.
9. Wingo TR, Damoiseaux R, Sittler A, et al. Integrating human brain proteomes with genome-wide
   association data implicates new proteins in Alzheimer disease. *Nat Genet* 2021;53(2):143–146.
   doi:10.1038/s41588-020-00773-z.
10. Vallabh S, Minikel EV, Prion Alliance. Open-science reanalysis and data-organization
    initiatives. Prion Alliance / Cure Alzheimer's Fund (cureffi.org).

---
*Figures: volcano_gse160208.png, volcano_gse140069.png, heatmap_top_genes.png
(pipeline/reports/figuras/). Fine-mapping numbers from relatorio_finemap_loci.md v2 and
relatorio_lambda_gc.md. All inferential statistics cross-checked against R anchors.*
