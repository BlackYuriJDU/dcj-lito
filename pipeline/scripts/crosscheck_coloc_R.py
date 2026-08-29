#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crosscheck_coloc_R.py — Prepara os dados da região STX6 para validação
cruzada do nosso coloc próprio contra o R `coloc` (padrão do campo).

Reusa EXATAMENTE as funções do pipeline validado (fonte única de verdade):
- carregar_gwas_regiao (GCST90001389, streaming)
- baixar_eqtl (eQTL Catalogue r8, tabix remoto, 5 cohorts)
- meta_analise IVW (importada de coloc_meta_stx6)

Saída: pipeline/data/stx6_crosscheck_input.tsv — uma linha por variante
harmonizada, com colunas que o coloc.abf (R) consome diretamente:
pos_b37, rsid, ref, alt, beta_gwas, se_gwas, p_gwas, maf,
beta_eqtl_meta, se_eqtl_meta, p_eqtl_meta, n_datasets
+ reimprime os nossos H0..H4 (baseline) num TSV de referência.
"""
import math
import sys
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from coloc_stx6_eqtl import (carregar_gwas_regiao, baixar_eqtl,
                             REGIAO_B37, OFFSET_B38_B37)
from coloc_meta_stx6 import DATASETS, meta_analise, p_de_z

BASE = Path(__file__).resolve().parents[1]
SAIDA = BASE / "data" / "stx6_crosscheck_input.tsv"


def main() -> None:
    print("[1/3] GWAS (streaming)...")
    gwas = carregar_gwas_regiao()

    por_dataset, resumo = {}, []
    for qts, qtd, nome, n in DATASETS:
        print(f"[2/3] {nome} (n={n})...")
        rows = baixar_eqtl(qtd, nome, qts)
        d = {}
        for pos38, ref, alt, rsid, p, beta, se, maf in rows:
            d[pos38] = (ref, alt, beta, se)
        por_dataset[qtd] = d
        resumo.append((nome, n, len(rows)))

    print("[3/3] meta IVW + join...")
    meta = meta_analise(por_dataset)
    linhas = []
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
        pos37 = pos38 + OFFSET_B38_B37
        maf = min(gmaf, 1.0 - gmaf) if gmaf is not None else ""
        linhas.append((pos37, other, eff, gb, gse, gp,
                       beta_m, se_m, p_de_z(beta_m / se_m), k, maf))

    with SAIDA.open("w", encoding="utf-8") as fh:
        fh.write("pos_b37\tref\talt\tbeta_gwas\tse_gwas\tp_gwas\t"
                 "beta_eqtl_meta\tse_eqtl_meta\tp_eqtl_meta\tn_datasets\tmaf\t"
                 "dataset_resumo\n")
        for r in linhas:
            fh.write("\t".join(str(x) for x in r[:11]) + "\n")
    print(f"[ok] {SAIDA}: {len(linhas)} variantes harmonizadas")
    for nome, n, npares in resumo:
        print(f"     {nome}: n={n}, {npares} pares")


if __name__ == "__main__":
    main()
