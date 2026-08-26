#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analise_integrada_cerebro_sangue.py — PONTE CÉREBRO × SANGUE (análise nova,
não feita por nenhum dos artigos originais).

Pergunta: os miRNAs down-regulados no SANGUE de pacientes sCJD (GSE140069)
têm alvos validados sobre-representados entre os genes UP-regulados no
CÉREBRO (GSE160208)? Mecanismo proposto: perda de freio miRNA no sangue
espelha desregulação no cérebro — ou é mero marcador de dano.

Método: alvos validados do miRTarBase 10.0 (evidência FORTE, humano) ×
DEGs do GSE160208 recomputados da série matrix (FDR<0.05, split up/down);
teste hipergeométrico com universo = painel NanoString (800 genes testados).
"""
import gzip
import math
import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
REPORTS = BASE / "reports"
MATRIX = DATA / "GSE160208_series_matrix.txt.gz"
MTI = DATA / "mirtarbase_MTI.csv"

MIRNAS_SANGUE = [  # 4 do artigo original (todos ↓) + nosso sobrevivente FDR
    "hsa-miR-16-5p", "hsa-miR-93-5p", "hsa-let-7i-5p", "hsa-miR-106b-3p",
    "hsa-miR-500a-3p",
]
UNIVERSO = 800  # painel NanoString testado no GSE160208


def carregar_degs_cerebro():
    """Recomputa DEGs do GSE160208: (up, down) com FDR<0.05 (nossa análise v1)."""
    sys_path = Path(__file__).resolve().parent
    sys_path_str = str(sys_path)
    if sys_path_str not in __import__("sys").path:
        __import__("sys").path.insert(0, sys_path_str)
    import analise_gse160208 as g  # funções canônicas do projeto

    amostras, genes, valores, meta, covs = g.extrair_tabela()
    idx_cjd = [i for i, s in enumerate(amostras) if "CJD" in s and "_FC" in s]
    idx_ct = [i for i, s in enumerate(amostras) if "CT" in s and "_FC" in s]
    pares = []
    for gi, gname in enumerate(genes):
        xs = [valores[gi][i] for i in idx_cjd]
        ys = [valores[gi][i] for i in idx_ct]
        t, p = g.welch(xs, ys)
        delta = sum(xs) / len(xs) - sum(ys) / len(ys)
        pares.append((gname, p, delta))
    # fdr_bh local (mesma implementação do projeto — lib/stats_core)
    _m = len(pares)
    _ord = sorted([(gn, p) for gn, p, _ in pares], key=lambda x: x[1])
    _prev, qmap = 1.0, {}
    for _k in range(_m - 1, -1, -1):
        _prev = min(_prev, _ord[_k][1] * _m / (_k + 1))
        qmap[_ord[_k][0]] = _prev
    up = {g for g, p, d in pares if qmap[g] < 0.05 and d > 0}
    down = {g for g, p, d in pares if qmap[g] < 0.05 and d < 0}
    return up, down, len(pares)


def alvos_mirtarbase():
    """{miRNA: set(genes)} — Functional MTI (validação forte), humano→humano."""
    out = {}
    with open(MTI, encoding="utf-8-sig", errors="replace") as fh:
        hdr = fh.readline().rstrip("\n").split(",")
        ci = {n.strip().strip('"').lower(): i for i, n in enumerate(hdr)}
        for line in fh:
            f = line.rstrip("\n").split(",")
            if len(f) < len(hdr):
                continue
            mirna = f[ci["mirna"]].strip()
            if mirna not in MIRNAS_SANGUE:
                continue
            if f[ci["species (mirna)"]].strip() != "hsa":
                continue
            if f[ci["support type"]].strip() != "Functional MTI":
                continue
            alvo = f[ci["target gene"]].strip()
            if alvo:
                out.setdefault(mirna, set()).add(alvo)
    return out


def hipergeometrico(k, K, n, N):
    """P(X≥k) — log-gamma, sem dependências."""
    def lnchoose(a, b):
        return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)
    p = 0.0
    for i in range(k, min(K, n) + 1):
        p += math.exp(lnchoose(K, i) + lnchoose(N - K, n - i) - lnchoose(N, n))
    return min(1.0, p)


def main() -> None:
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("[1/3] recomputando DEGs do cérebro (GSE160208)...")
    up, down, n_test = carregar_degs_cerebro()
    print(f"      FDR<0.05: {len(up)} up · {len(down)} down (de {n_test})")

    print("[2/3] alvos validados miRTarBase 10.0 (Strong, humano)...")
    alvos = alvos_mirtarbase()

    L = ["# Ponte cérebro × sangue: alvos de miRNAs sanguíneos nos DEGs cerebrais",
         f"*`analise_integrada_cerebro_sangue.py` em {agora}. Análise NOVA —",
         "nenhum dos artigos originais fez a integração.*", "",
         "**Desenho**: miRNAs ↓ no sangue de sCJD (GSE140069) → alvos validados",
         "(miRTarBase 10.0, evidência forte, humano) → sobre-representação entre",
         "genes ↑ no córtex frontal sCJD (GSE160208, FDR<0.05). Hipergeométrico,",
         f"universo = painel NanoString (N={UNIVERSO}).", "",
         f"DEGs cerebrais recomputados: {len(up)} up · {len(down)} down.", "",
         "| miRNA (sangue) | Alvos validados (Strong) | ∩ DEGs ↑ | Esperado | p (hipergeom.) |",
         "|---|---|---|---|---|"]
    resultados = []
    for mirna in MIRNAS_SANGUE:
        tgt = alvos.get(mirna, set())
        inter = tgt & up
        esperado = len(tgt) * len(up) / UNIVERSO
        p = hipergeometrico(len(inter), len(tgt), len(up), UNIVERSO) if tgt else 1.0
        resultados.append((mirna, len(tgt), len(inter), esperado, p))
        L.append(f"| {mirna} | {len(tgt)} | {len(inter)} | {esperado:.1f} | "
                 f"{p:.2e} |")

    # correção BH sobre os 5 testes
    ordenado = sorted(resultados, key=lambda r: r[4])
    prev, qmap = 1.0, {}
    for k in range(len(ordenado) - 1, -1, -1):
        prev = min(prev, ordenado[k][4] * len(ordenado) / (k + 1))
        qmap[ordenado[k][0]] = prev
    L += ["", "| miRNA | q (BH, 5 testes) |", "|---|---|"]
    for mirna, *_ in resultados:
        L.append(f"| {mirna} | {qmap[mirna]:.3f} |")

    L += ["", "## Leitura honesta",
          "- Sobre-representação significativa = consistente com eixo miRNA→alvo",
          "  compartilhado sangue-cérebro (biomarcador mecanístico, não só",
          "  marcador passivo de dano).",
          "- NÃO significativo = os miRNAs sanguíneos provavelmente refletem",
          "  processos periféricos (imunidade) distintos da transcrição cerebral —",
          "  também é achado: desmonta inferência causal ingênua sangue→cérebro.",
          "- Viés declarado: o painel NanoString (800 genes) é focado em",
          "  neuroinflamação — enriquece DEGs de vias imunes, o que pode inflar",
          "  o overlap com alvos de miRNAs imunes. Universo honesto declarado.",
          "- miRNAs ↓ no sangue com alvos ↑ no cérebro é a direção testada;",
          "  direção oposta (alvos ↓) testada como controle negativo."]

    # controle negativo: alvos ∩ DEGs DOWN
    L += ["", "### Controle negativo — alvos ∩ DEGs ↓ (deveria ser ~nulo)", "",
          "| miRNA | ∩ DEGs ↓ |", "|---|---|"]
    for mirna in MIRNAS_SANGUE:
        L.append(f"| {mirna} | {len(alvos.get(mirna, set()) & down)} |")

    destino = REPORTS / "relatorio_integracao_cerebro_sangue.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"[3/3] {destino}")


if __name__ == "__main__":
    import sys
    main()
