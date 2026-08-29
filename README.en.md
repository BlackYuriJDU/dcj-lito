# DCJ - Lito Project — Independent verification of prion-disease data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22164910.svg)](https://doi.org/10.5281/zenodo.22164910)

Open reanalysis of publicly deposited sporadic Creutzfeldt–Jakob disease (sCJD) datasets, run by a non-laboratory independent initiative in Brazil. **Everything here is reproducible from standard-library Python.**

## Headline results

| Result | Number |
|---|---|
| GWAS GCST90001389 variants parsed | 6,314,492 (0 malformed) |
| Published loci independently replicated | **3/3** — PRNP p=1.6e-15 · GAL3ST1 p=6.2e-10 · STX6 p=7.5e-9 |
| Genomic inflation λ | 1.0587 (MAF-stratum gradient 0.016) |
| rs3747957 (*Brain* 2025 index) already in 2020 sumstats | p=9.7e-9, same β direction |
| STX6 lead-cluster posterior mass (r²≥0.8) | 90.5% |
| Brain expression GSE160208 vs original paper | exact replication: 184 DEGs, r = 1.000 |
| Blood miRNA GSE140069 after age/sex/RIN adjustment | 84 → 1 significant (direction preserved) |

## Repository map

```
ARQUIVO_COMPLETO.md      ← EVERYTHING: all reports + code inline (start here)
preprint/                ← English manuscript draft
research/                ← state of the art, dataset catalogs, ecosystem map
caso_referencia/               ← simulated reference case (training/didactic; not a real patient)
pipeline/scripts/        ← all analysis code (pure stdlib + matplotlib/openpyxl)
pipeline/reports/        ← every generated report with intermediate numbers
colaboracao/             ← family guide (PT-BR), engagement letters, audit reports
memory/                  ← mistakes, decisions, successful patterns
```

## Reproducibility

```bash
# data (public, checksummed — see ARQUIVO_COMPLETO.md Appendix B)
# GCST90001389 from GWAS Catalog; GSE160208/GSE140069 from GEO

python3 pipeline/scripts/qc_gwas_gcst90001389.py   # GWAS QC + 3-loci replication
python3 pipeline/scripts/finemap_ld.py              # LD fine-mapping + λ strata
python3 pipeline/scripts/analise_gse160208.py       # brain expression
python3 pipeline/scripts/analise_gse140069.py       # blood miRNA (adjusted model)
python3 pipeline/scripts/gera_figuras.py            # figures
python3 pipeline/scripts/monta_arquivo_completo.py  # rebuild the master file
```

Statistics implemented from first principles (Welch t-test, Benjamini–Hochberg FDR,
Wakefield ABF); validated against R anchors to ≤1e-13 and by permutation calibration.
An adversarial statistical audit of this pipeline ships with the repo.

## Ethics

Public, de-identified data only. The "Caso Referência" dossier is a **simulated**
generic training profile, not any real person. No clinical claims are made about
any individual.

## License & citation

MIT — see `LICENSE`. Cite via `CITATION.cff` (DOI minted on first Zenodo release).
