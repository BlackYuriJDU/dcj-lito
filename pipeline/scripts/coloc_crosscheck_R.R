#!/usr/bin/env Rscript
# coloc_crosscheck_R.R — Validação cruzada do coloc próprio (Python stdlib)
# contra implementação independente em R, no dataset da região STX6.
# (A) reimplementação EXATA das equações (ABF Wakefield + H0..H4 Giambartolomei)
# (B) coloc.abf do pacote R `coloc` (padrão do campo) com priors padrão
# Entrada: pipeline/data/stx6_crosscheck_input.tsv (390 variantes, gerado por
# crosscheck_coloc_R.py a partir do MESMO pipeline validado).

suppressMessages(library(coloc))

d <- read.delim("pipeline/data/stx6_crosscheck_input.tsv", check.names = FALSE)
cat("variantes:", nrow(d), "\n")

N_GWAS <- 17679
S_GWAS <- 4110 / N_GWAS
P1 <- 1e-4; P2 <- 1e-4; P12 <- 1e-5
W <- 0.04^2   # idêntico ao W_ABF do Python

## ---------------------------------------------------------------- (A) exato
abf_w <- function(beta, se, w = W) {
  r <- w / (se^2 + w)
  sqrt(r) * exp(beta^2 / (2 * se^2) * r)
}
ag <- abf_w(d$beta_gwas, d$se_gwas)
ae <- abf_w(d$beta_eqtl_meta, d$se_eqtl_meta)

h_post <- function(ppg, ppe, p1, p2, p12) {
  sg <- sum(ppg); se <- sum(ppe)
  diag <- sum(ppg * ppe)
  h <- c((1 - p1) * (1 - p2),
         p1 * (1 - p2) * sg,
         (1 - p1) * p2 * se,
         p1 * p2 * (1 - p12) * (sg * se - diag),
         p1 * p2 * p12 * diag)
  h / sum(h)
}

cat("\n== (A) Reimplementação R das equações (deve bater com o Python) ==\n")
ha <- h_post(ag, ae, P1, P2, P12)
cat(sprintf("priors padrao     : H0=%.6f H1=%.6f H2=%.6f H3=%.6f H4=%.6f\n",
            ha[1], ha[2], ha[3], ha[4], ha[5]))
hc <- h_post(ag, ae, 1e-6, 1e-6, 1e-7)
cat(sprintf("priors conservador: H0=%.6f H1=%.6f H2=%.6f H3=%.6f H4=%.6f\n",
            hc[1], hc[2], hc[3], hc[4], hc[5]))
cat("referencia Python (relatorio v. 26/08): H3=0.9950 (padrao) · H3=0.6654 (conservador)\n")

## ------------------------------------------------- (B) coloc.abf padrao R
# N efetivo por variante para o meta-eQTL (NES ~ padronizada, sdY=1):
# Var(beta) = sdY^2 / (2 N p (1-p))  =>  N_i = 1 / (2 Var_i p_i (1-p_i))
p_m <- pmin(d$maf, 1 - d$maf)
n_eff <- 1 / (2 * d$se_eqtl_meta^2 * p_m * (1 - p_m))

D1 <- list(snp = paste0("p", d$pos_b37), position = d$pos_b37,
           beta = d$beta_gwas, varbeta = d$se_gwas^2,
           type = "cc", s = S_GWAS, N = N_GWAS)
D2 <- list(snp = paste0("p", d$pos_b37), position = d$pos_b37,
           beta = d$beta_eqtl_meta, varbeta = d$se_eqtl_meta^2,
           type = "quant", sdY = 1, N = n_eff, MAF = p_m)

res <- coloc.abf(D1, D2, p1 = P1, p2 = P2, p12 = P12)
cat("\n== (B) coloc.abf (pacote R, priors padrao) ==\n")
s <- res$summary
cat(sprintf("nsnps=%d · PP.H0=%.4f H1=%.4f H2=%.4f H3=%.4f H4=%.4f\n",
            s["nsnps"], s["PP.H0.abf"], s["PP.H1.abf"], s["PP.H2.abf"],
            s["PP.H3.abf"], s["PP.H4.abf"]))
cat(sprintf("PP.H3+H4 = %.4f\n", s["PP.H3.abf"] + s["PP.H4.abf"]))

# ranking por-variante: PP.H4 do R vs produto ABF (nossa medida equivalente)
pp4 <- res$results$SNP.PP.H4
nossa <- ag * ae / sum(ag * ae)
r <- cor(pp4, nossa, method = "spearman")
cat(sprintf("correlacao (Spearman) PP.H4(coloc R) × diag-ABF(nosso) = %.6f\n", r))

write.table(data.frame(pos_b37 = d$pos_b37, PP4_colocR = pp4, diagABF_nosso = nossa),
            "pipeline/data/stx6_crosscheck_colocR_output.tsv",
            sep = "\t", row.names = FALSE, quote = FALSE)
cat("[ok] saida: pipeline/data/stx6_crosscheck_colocR_output.tsv\n")
