#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
coloc_meta_stx6.py — Colocalização com PODER AMPLIADO: meta-análise IVW dos
eQTLs de STX6 em 5 datasets cerebrais (CommonMind 586, ROSMAP 560, BrainSeq
479, GTEx DLPFC 285, GTEx cerebelo 272 → ~2.182 amostras) contra o GWAS sCJD
(GCST90001389, n=17.679).

Estratégia: por posição (harmonizada p/ ALT=efeito), z_i = β_i/SE_i;
β_meta = Σ(β/SE²)/Σ(1/SE²); SE_meta = 1/√Σ(1/SE²) (inverse-variance).
p via erfc (stdlib). Depois coloc ABF com o eQTL meta vs GWAS.
"""
import math
import sys
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coloc_stx6_eqtl import (carregar_gwas_regiao, baixar_eqtl, abf,
                             REGIAO_B37, OFFSET_B38_B37, STX6)

REPORTS = Path(__file__).resolve().parents[1] / "reports"
N_GWAS = 17_679
# (QTS, QTD, nome, n) — QTS varia por estudo (caminho FTP correto)
DATASETS = [
    ("QTS000008", "QTD000075", "CommonMind DLPFC", 586),
    ("QTS000025", "QTD000434", "ROSMAP DLPFC", 560),
    ("QTS000005", "QTD000051", "BrainSeq DLPFC", 479),
    ("QTS000015", "QTD000176", "GTEx_v10 DLPFC", 285),
    ("QTS000015", "QTD000166", "GTEx_v10 cerebelo", 272),
]
PRIORS = {"padrao": (1e-4, 1e-4, 1e-5), "conservador": (1e-6, 1e-6, 1e-7)}


def p_de_z(z):
    return math.erfc(abs(z) / math.sqrt(2.0))


def meta_analise(por_dataset):
    """por_dataset: {qtd: {pos38: (ref, alt, beta, se)}} → meta por posição."""
    todas_pos = set()
    for d in por_dataset.values():
        todas_pos |= set(d.keys())
    meta = {}
    for pos in todas_pos:
        betas, ses, refs = [], [], None
        for d in por_dataset.values():
            v = d.get(pos)
            if v is None:
                continue
            ref, alt, beta, se = v
            if se <= 0 or beta == 0:
                continue
            betas.append(beta)
            ses.append(se)
            refs = (ref, alt)
        if len(betas) < 3:
            continue
        w = [1.0 / s**2 for s in ses]
        beta_m = sum(b * wi for b, wi in zip(betas, w)) / sum(w)
        se_m = math.sqrt(1.0 / sum(w))
        meta[pos] = (refs[0], refs[1], beta_m, se_m, len(betas))
    return meta


def main() -> None:
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("[1/4] GWAS...")
    gwas = carregar_gwas_regiao()

    por_dataset, resumo = {}, []
    for qts, qtd, nome, n in DATASETS:
        print(f"[2/4] {nome} (n={n})...")
        rows = baixar_eqtl(qtd, nome, qts)
        d = {}
        for pos38, ref, alt, rsid, p, beta, se, maf in rows:
            d[pos38] = (ref, alt, beta, se)
        por_dataset[qtd] = d
        resumo.append((qtd, nome, n, len(rows)))

    print("[3/4] meta-análise IVW...")
    meta = meta_analise(por_dataset)

    # join com GWAS + coloc
    pares_g, pares_e, rsids = [], [], []
    for pos38, (ref, alt, beta_m, se_m, k) in sorted(meta.items()):
        g = gwas.get(pos38 + OFFSET_B38_B37)
        if g is None:
            continue
        other, eff, gbeta, gse, gmaf, gp = g
        if eff == alt and other == ref:
            gb = gbeta
        elif eff == ref and other == alt:
            gb = -gbeta
        else:
            continue
        pares_g.append((gb, gse))
        pares_e.append((beta_m, se_m))
        rsids.append((pos38 + OFFSET_B38_B37, gp, p_de_z(beta_m / se_m)))

    L = ["# Colocalização STX6 — META-eQTL (poder ampliado)",
         f"*`coloc_meta_stx6.py` em {agora}. Meta IVW de {len(DATASETS)} datasets",
         "cerebrais (eQTL Catalogue r8, tabix remoto) vs GWAS sCJD.*", "",
         "| Dataset | n | pares STX6 |", "|---|---|---|"]
    for qtd, nome, n, npares in resumo:
        L.append(f"| {nome} | {n} | {npares} |")
    L += ["", f"Posições na meta (≥3 datasets): **{len(meta)}** · "
          f"casadas com GWAS: **{len(pares_g)}**", ""]

    abf_g = [abf(b, s) for b, s in pares_g]
    abf_e = [abf(b, s) for b, s in pares_e]
    def coloc(pp_gwas, pp_eqtl, p1, p2, p12):
        sg, se = sum(pp_gwas), sum(pp_eqtl)
        diag = sum(a * b for a, b in zip(pp_gwas, pp_eqtl))
        h = [(1 - p1) * (1 - p2), p1 * (1 - p2) * sg, (1 - p1) * p2 * se,
             p1 * p2 * (1 - p12) * (sg * se - diag), p1 * p2 * p12 * diag]
        s = sum(h)
        return [x / s for x in h], len(pp_gwas)
    for nome_p, (p1, p2, p12) in PRIORS.items():
        h, n = coloc(abf_g, abf_e, p1, p2, p12)
        L += [f"## Priors {nome_p}",
              f"- **PP.H4 = {h[4]:.4f}** · H3 = {h[3]:.4f} · H2 = {h[2]:.4f} · "
              f"H1 = {h[1]:.4f} · H0 = {h[0]:.4f}",
              f"- H2+H3+H4 (ambos os sinais reais na região) = "
              f"{h[2]+h[3]+h[4]:.4f}",
              f"- H4/(H3+H4) = {h[4]/h[3] if h[3]>0 else float('inf'):.2f}", ""]

    conc = sum(1 for (bg, _), (be, _) in zip(pares_g, pares_e) if bg * be > 0)
    L += ["## Direção",
          f"- Mesma direção GWAS×eQTL-meta: **{conc}/{len(pares_g)} "
          f"({conc/len(pares_g):.0%})**", ""]
    L += ["| pos b37 | p GWAS | p eQTL-meta |", "|---|---|---|"]
    for pos37, gp, ep in sorted(rsids, key=lambda x: x[1])[:10]:
        L.append(f"| {pos37:,} | {gp:.2e} | {ep:.2e} |")
    L += ["", "## Interpretação honesta",
          "- **H2+H3+H4 ≈ 1,0 com H0≈H1≈0**: ambos os sinais são reais e vivem",
          "  na MESMA região — é essa a afirmação robusta, válida sob qualquer",
          "  prior (padrão: H3=0.995, H2=0.005; conservador: H3=0.665, H2=0.335;",
          "  coloc.abf do R 5.2.3 com seu prior: H4=0.98 — ver",
          "  relatorio_validacao_coloc_R.md). H2 NÃO é hipótese nula: é",
          "  'duas variantes causais distintas'.",
          "  A divisão H4 (compartilhado) vs H3/H2 (distintas) é prior-dependente",
          "  e indistinguível sob LD forte (r²≥0,97 no cluster): 'duas variantes",
          "  distintas em LD perfeito' e 'uma variante compartilhada' produzem",
          "  verossimilhanças idênticas — por isso reportamos o combinado.",
          "- O que decide na direção da partilha: (i) o lead GWAS É eQTL",
          "  significativo do STX6 no meta (p=7×10⁻⁴⁷, z≈14); (ii) concordância",
          "  de direção em 89% das variantes; (iii) o fine-mapping GWAS mostra",
          "  um único cluster posterior (90,5% em r²≥0,8) — não há segundo sinal",
          "  real para justificar H3 por variantes distintas.",
          "- Conclusão para o preprint: consistente com o sinal de STX6 ser",
          "  mediado por expressão gênica no cérebro adulto; H4 estrito não é",
          "  afirmável sob r²=1,0 — reportar H3+H4 combinado e concordância.",
          "- Limitações: meta assume heterogeneidade baixa entre datasets;",
          "  coloc assume 1 sinal causal por traço; DLPFC/cerebelo ≠ todos os",
          "  tecidos afetados na DCJ.", ""]
    destino = REPORTS / "relatorio_coloc_meta_stx6.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"[4/4] {destino}")


if __name__ == "__main__":
    main()
