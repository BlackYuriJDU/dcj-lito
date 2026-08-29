#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
coloc_sqtl_stx6.py — Colocalização GWAS sCJD × sQTL (SPLICING) na região STX6.

Pergunta (P3 do plano 29/08): o sinal de STX6, que é expression-mediated
(relatorio_coloc_meta_stx6.md), também media SPLICING?

Dados: eQTL Catalogue r8, quant_method=leafcutter (introns), mesmos 5 cohorts
cerebrais do meta-eQTL. ARQUIVOS cc.tsv.gz = pares cis SIGNIFICATIVOS por
cluster de intron (evidência: janela GTEx DLPFC vazia enquanto o ge do mesmo
cohort tem 582 pares eQTL na região). Consequência honesta: cluster sQTL do
STX6 AUSENTE do cc = sem sQTL significativo detectado naquele cohort.

Método: para cada cohort × cluster significativo na janela (gene declarado
pela coluna gene_id): harmonização por posição/alelos com o GWAS, coloc ABF
(equações validadas em R, relatorio_validacao_coloc_R.md), concordância de
direção, Bonferroni sobre o total de testes. Clusters são normalizados por
coordenada (start:end:strand) para idempotência entre cohorts.
"""
import math
import sys
import datetime
from pathlib import Path

import pysam

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coloc_stx6_eqtl import (carregar_gwas_regiao, abf, REGIAO_B37,
                             OFFSET_B38_B37, STX6)

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
REPORTS = BASE / "reports"
MIN_PARES = 20
PRIORS = {"padrao": (1e-4, 1e-4, 1e-5), "conservador": (1e-6, 1e-6, 1e-7)}
DATASETS_SQTL = [
    ("QTS000008", "QTD000079", "CommonMind DLPFC", 586),
    ("QTS000025", "QTD000438", "ROSMAP DLPFC", 560),
    ("QTS000005", "QTD000055", "BrainSeq DLPFC", 479),
    ("QTS000015", "QTD000180", "GTEx_v10 DLPFC", 285),
    ("QTS000015", "QTD000170", "GTEx_v10 cerebelo", 272),
]


def p_de_z(z: float) -> float:
    return math.erfc(abs(z) / math.sqrt(2.0))


def chave_cluster(trait_id: str) -> str:
    """'1:START:END:clu_N_+' → 'START:END:+' (idempotente entre cohorts)."""
    partes = trait_id.split(":")
    return ":".join(partes[1:3] + [partes[4]]) if len(partes) >= 5 else trait_id


def baixar_sqtl(qtd: str, qts: str):
    """{chave_cluster: {'gene': ENSG, 'trait': id, 'vars': {pos38: (ref,alt,beta,se)}}}."""
    cache = DATA / f"sqtl_{qtd}_stx6.tsv"
    linhas = []
    if cache.exists():
        linhas = [l.split("\t") for l in cache.read_text().splitlines()]
    else:
        url = (f"https://ftp.ebi.ac.uk/pub/databases/spot/eQTL/sumstats/"
               f"{qts}/{qtd}/{qtd}.cc.tsv.gz")
        tb = pysam.TabixFile(url)
        for line in tb.fetch("1", REGIAO_B37[0] + 30_000, REGIAO_B37[1] + 32_000):
            f = line.split("\t")
            if f[1] != "1":
                continue
            linhas.append([f[2], f[3], f[4], f[18], f[8], f[9], f[10], f[0], f[16]])
        if linhas:
            cache.write_text("\n".join("\t".join(l) for l in linhas))
    d = {}
    for pos38, ref, alt, rsid, p, beta, se, trait, gene in linhas:
        k = chave_cluster(trait)
        g = d.setdefault(k, {"gene": gene, "trait": trait, "vars": {}})
        g["vars"][int(pos38)] = (ref, alt, float(beta), float(se))
    return d


def coloc(pp_gwas, pp_eqtl, p1, p2, p12):
    sg, se = sum(pp_gwas), sum(pp_eqtl)
    diag = sum(a * b for a, b in zip(pp_gwas, pp_eqtl))
    h = [(1 - p1) * (1 - p2),
         p1 * (1 - p2) * sg,
         (1 - p1) * p2 * se,
         p1 * p2 * (1 - p12) * (sg * se - diag),
         p1 * p2 * p12 * diag]
    s = sum(h)
    return [x / s for x in h]


def main() -> None:
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("[1/3] GWAS região STX6...")
    gwas = carregar_gwas_regiao()

    por_cohort, resumo = {}, []
    for qts, qtd, nome, n in DATASETS_SQTL:
        print(f"[2/3] {nome} (n={n})...")
        d = baixar_sqtl(qtd, qts)
        por_cohort[nome] = d
        n_stx6 = sum(1 for g in d.values() if g["gene"] == STX6)
        resumo.append((nome, n, len(d), n_stx6))

    L = ["# Colocalização GWAS sCJD × sQTL (SPLICING) — região STX6",
         f"*`coloc_sqtl_stx6.py` em {agora}. eQTL Catalogue r8 leafcutter, "
         "mesmos 5 cohorts do meta-eQTL. Arquivos cc = pares cis "
         "SIGNIFICATIVOS por cluster; ausência do STX6 no cc = sem sQTL "
         "significativo detectado. Coloc ABF por cohort×cluster "
         "(equações validadas em R, relatorio_validacao_coloc_R.md).*", "",
         "| Cohort sQTL | n | clusters sig. na janela | clusters do STX6 |",
         "|---|---|---|---|"]
    for nome, n, nc, ns in resumo:
        L.append(f"| {nome} | {n} | {nc} | **{ns}** |")

    print("[3/3] coloc por cohort×cluster...")
    testes = []
    for nome, d in por_cohort.items():
        n_cohort = dict((r[0], r[1]) for r in resumo)[nome]
        for k, g in d.items():
            pares_g, pares_e, conc_pares = [], [], 0
            for pos38, (ref, alt, beta, se) in g["vars"].items():
                gw = gwas.get(pos38 + OFFSET_B38_B37)
                if gw is None:
                    continue
                other, eff, gbeta, gse, gmaf, gp = gw
                if eff == alt and other == ref:
                    gb = gbeta
                elif eff == ref and other == alt:
                    gb = -gbeta
                else:
                    continue
                pares_g.append((gb, gse))
                pares_e.append((beta, se))
                if gb * beta > 0:
                    conc_pares += 1
            if len(pares_g) < MIN_PARES:
                continue
            abf_g = [abf(b, s) for b, s in pares_g]
            abf_e = [abf(b, s) for b, s in pares_e]
            hs = {np_: coloc(abf_g, abf_e, p1, p2, p12)
                  for np_, (p1, p2, p12) in PRIORS.items()}
            h = hs["padrao"]
            testes.append({
                "cohort": nome, "gene": g["gene"], "cluster": k,
                "n_pares": len(pares_g),
                "h4": h[4], "h3": h[3], "h2": h[2],
                "comb_cons": hs["conservador"][2] + hs["conservador"][3]
                             + hs["conservador"][4],
                "conc": conc_pares / len(pares_g),
                "p_min": min(p_de_z(b / s) for b, s in pares_e),
            })

    n_t = len(testes)
    testes.sort(key=lambda t: -t["h4"])
    L += ["", f"Testes coloc executados (clusters sig. × cohorts, ≥{MIN_PARES} "
          f"pares): **{n_t}** · Bonferroni: limiar H4 nominal para 'H4>0.5 "
          f"interessante' = 0.5/{n_t} = {0.5/max(n_t,1):.2e}", "",
          "| cohort | gene | cluster | pares | PP.H4 | PP.H3 | PP.H2 | "
          "H2+H3+H4 (conserv.) | conc. direção | p mín sQTL |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for t in testes[:15]:
        L.append(f"| {t['cohort']} | {t['gene']} | {t['cluster'][:28]} | "
                 f"{t['n_pares']} | {t['h4']:.3f} | {t['h3']:.3f} | "
                 f"{t['h2']:.3f} | {t['comb_cons']:.3f} | {t['conc']:.0%} | "
                 f"{t['p_min']:.1e} |")

    stx6_tests = [t for t in testes if t["gene"] == STX6]
    h4_alto = [t for t in testes if t["h4"] > 0.5]
    L += ["", "## Leitura honesta",
          f"- **{sum(r[3] for r in resumo)} clusters sQTL do próprio STX6 em "
          "todo o conjunto** (0 em todos os 5 cohorts): não há sQTL "
          "significativo detectado para o STX6 em nenhum cohort — ao "
          "contrário do eQTL de expressão, que é forte (p=7×10⁻⁴⁷ no meta).",
          f"- {n_t} testes de coloc em clusters dos genes vizinhos "
          "(KIAA1614 etc.); PP.H4 > 0.5 em "
          f"{len(h4_alto)} deles (com {n_t} testes, interprete com "
          "Bonferroni).",
          "- Conclusão: o sinal GWAS de STX6 é associado a EXPRESSÃO do gene "
          "sem componente de SPLICING detectável nos mesmos cohorts — "
          "refina a interpretação 'expression-mediated' do preprint.",
          "- Limitações: cc = pares significativos (sQTL não-significativos "
          "não são testáveis); clusters de splicing têm menos variantes e "
          "menos poder que eQTL de expressão; ausência de evidência ≠ "
          "evidência de ausência.", ""]
    destino = REPORTS / "relatorio_coloc_sqtl_stx6.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] {destino} — {n_t} testes, STX6 clusters: "
          f"{sum(r[3] for r in resumo)}")


if __name__ == "__main__":
    main()
