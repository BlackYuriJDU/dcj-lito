#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analise_gse160208.py — Primeira análise sobre dados REAIS e anonimizados.

Dataset: GSE160208 (GEO/NCBI) — NanoString nCounter, painel neuroinflamação+,
córtex frontal (FC) e cerebelo (CB) de pacientes com sCJD vs. controles.
Fonte: Litman T. et al., Univ. Copenhagen, PMID 33375642. Licença: público NCBI.

Gera pipeline/reports/relatorio_gse160208.md com:
- composição das amostras; 
- top genes diferencialmente expressos (diferença de médias) em FC;
- verificação específica de PRNP;
- nota honesta: diferença de médias simples, sem teste estatístico formal
  (t-teste virá em versão futura; aqui o objetivo é curadoria + triagem).
"""
import gzip
import math
import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
REPORTS = BASE / "reports"
MATRIX = DATA / "GSE160208_series_matrix.txt.gz"


def tcdf_p(t: float, df: float) -> float:
    """p bicaudal da distribuição t via beta incompleta regularizada."""
    def betacf(a: float, b: float, x: float) -> float:
        MAXIT, EPS, FPMIN = 200, 3e-12, 1e-300
        qab, qap, qam = a + b, a + 1.0, a - 1.0
        c, d = 1.0, 1.0 - qab * x / qap
        if abs(d) < FPMIN:
            d = FPMIN
        d = 1.0 / d
        h = d
        for m in range(1, MAXIT + 1):
            m2 = 2 * m
            aa = m * (b - m) * x / ((qam + m2) * (a + m2))
            d = 1.0 + aa * d
            if abs(d) < FPMIN:
                d = FPMIN
            c = 1.0 + aa / c
            if abs(c) < FPMIN:
                c = FPMIN
            d = 1.0 / d
            h *= d * c
            aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
            d = 1.0 + aa * d
            if abs(d) < FPMIN:
                d = FPMIN
            c = 1.0 + aa / c
            if abs(c) < FPMIN:
                c = FPMIN
            d = 1.0 / d
            dele = d * c
            h *= dele
            if abs(dele - 1.0) < EPS:
                break
        return h

    def ibeta(a: float, b: float, x: float) -> float:
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
        if x < (a + 1) / (a + b + 2):
            return front * betacf(a, b, x) / a
        return 1.0 - front * betacf(b, a, 1 - x) / b

    return ibeta(df / 2.0, 0.5, df / (df + t * t))


def welch(xs: list[float], ys: list[float]) -> tuple[float, float]:
    """Teste t de Welch bicaudal: retorna (t, p)."""
    n1, n2 = len(xs), len(ys)
    m1, m2 = sum(xs) / n1, sum(ys) / n2
    v1 = sum((x - m1) ** 2 for x in xs) / (n1 - 1)
    v2 = sum((y - m2) ** 2 for y in ys) / (n2 - 1)
    se2 = v1 / n1 + v2 / n2
    if se2 == 0:
        return 0.0, 1.0
    t = (m1 - m2) / math.sqrt(se2)
    df = se2 ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1))
    return t, min(1.0, tcdf_p(abs(t), df))


def extrair_tabela() -> tuple[list[str], list[list[float]], dict]:
    """Lê a série matrix e retorna (genes, valores[genes][amostras], metadados)."""
    meta: dict = {}
    genes: list[str] = []
    linhas_vals: list[list[float]] = []
    amostras: list[str] = []          # títulos na ordem das colunas da tabela
    gsms: list[str] = []
    covs_raw: list[list[str]] = []    # cada linha !Sample_characteristics_ch1
    em_tabela = False
    with gzip.open(MATRIX, "rt", encoding="utf-8") as fh:
        for linha in fh:
            if linha.startswith("!Series_title"):
                meta["titulo"] = linha.split("\t")[1].strip().strip('"')
            elif linha.startswith("!Sample_title\t"):
                titulos = [s.strip('"') for s in linha.rstrip("\n").split("\t")[1:]]
            elif linha.startswith("!Sample_geo_accession\t"):
                gsms = [s.strip('"') for s in linha.rstrip("\n").split("\t")[1:]]
            elif linha.startswith("!Sample_characteristics_ch1\t"):
                covs_raw.append([s.strip('"') for s
                                 in linha.rstrip("\n").split("\t")[1:]])
            elif linha.startswith("!series_matrix_table_begin"):
                em_tabela = True
            elif linha.startswith("!series_matrix_table_end"):
                break
            elif em_tabela:
                partes = [c.strip().strip('"') for c in linha.rstrip("\n").split("\t")]
                if partes[0] in ("ID_REF", ""):
                    continue  # cabeçalho interno
                try:
                    nums = [float(x) for x in partes[1:]]
                except ValueError:
                    continue  # linha malformada: pula SEM desalinhar
                genes.append(partes[0])
                linhas_vals.append(nums)
    # Mapear colunas GSM -> título clínico (ordem da tabela = ordem dos GSMs)
    mapa = dict(zip(gsms, titulos))
    amostras = [mapa.get(gsm, gsm) for gsm in gsms]
    # Covariáveis: extrair "chave: valor" por amostra
    covs: list[dict[str, str]] = []
    for j in range(len(gsms)):
        d: dict[str, str] = {}
        for linha_c in covs_raw:
            if j < len(linha_c) and ":" in linha_c[j]:
                k, v = linha_c[j].split(":", 1)
                d[k.strip()] = v.strip()
        covs.append(d)
    return amostras, genes, linhas_vals, meta, covs


def main() -> None:
    amostras, genes, vals, meta, covs = extrair_tabela()

    # --- Classificação das amostras pelo título: FFCJD-*_FC etc. ----------
    grupos: dict[str, list[int]] = {"CJD_FC": [], "CT_FC": [],
                                    "CJD_CB": [], "CT_CB": []}
    for i, nome in enumerate(amostras):
        doenca = "CJD" if "CJD" in nome else ("CT" if "CT" in nome else None)
        regiao = "FC" if "_FC" in nome else ("CB" if "_CB" in nome else None)
        if doenca and regiao:
            grupos[f"{doenca}_{regiao}"].append(i)

    # --- Covariáveis por amostra (sexo, códon 129, subtipo) --------------
    def cov(i: int, chave: str) -> str:
        return covs[i].get(chave, "NA") if i < len(covs) else "NA"

    resumo_covs: dict[str, dict[str, int]] = {}
    for k_chave in ("gender", "codon 129", "cjd subtype"):
        contagem: dict[str, int] = {}
        for i in range(len(amostras)):
            contagem[cov(i, k_chave)] = contagem.get(cov(i, k_chave), 0) + 1
        resumo_covs[k_chave] = contagem

    # Subtipos presentes apenas em CJD (controles são NA)
    subtipos_cjd_fc: dict[str, list[int]] = {}
    for i in grupos["CJD_FC"]:
        st = cov(i, "cjd subtype")
        subtipos_cjd_fc.setdefault(st, []).append(i)

    # --- Diferença de médias por gene no córtex frontal -------------------
    def media(gi: int, idxs: list[int]) -> float:
        col = vals[gi]
        sel = [col[i] for i in idxs]
        return sum(sel) / len(sel) if sel else float("nan")

    fc_diffs = []
    for gi, g in enumerate(genes):
        m_cjd, m_ct = media(gi, grupos["CJD_FC"]), media(gi, grupos["CT_FC"])
        fc_diffs.append((g, m_cjd - m_ct, m_cjd, m_ct))
    fc_diffs.sort(key=lambda t: t[1])

    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = [
        "# Relatório — Análise de dados REAIS: GSE160208",
        f"*Gerado por `analise_gse160208.py` em {agora}.*",
        "",
        f"- Dataset: {meta.get('titulo', 'GSE160208')}",
        "- Fonte: GEO/NCBI GSE160208 · PMID 33375642 · Univ. Copenhagen (dados públicos anonimizados)",
        f"- Amostras totais processadas: **{len(amostras)}** · Genes no painel: **{len(genes)}**",
        "",
        "## Composição das amostras",
    ]
    for k in sorted(grupos):
        L.append(f"- {k}: {len(grupos[k])}")

    L += ["", "## Covariáveis disponíveis (metadados reais)", ""]
    for k_chave, contagem in resumo_covs.items():
        partes = ", ".join(f"{v}: {n}" for v, n in sorted(contagem.items()))
        L.append(f"- {k_chave}: {partes}")

    # --- Estratificação por subtipo (MM1 = subtipo do caso Lito) ---------
    mm1_fc = subtipos_cjd_fc.get("MM1", [])
    L += ["", "## Estratificação por subtipo — córtex frontal CJD",
          f"- Grupos CJD-FC por subtipo: "
          + ", ".join(f"{st}: {len(ix)}" for st, ix in sorted(subtipos_cjd_fc.items()))]
    if mm1_fc:
        # Top 5 genes MM1 vs controles (Δ de médias) — foco no subtipo do Lito
        diffs_mm1 = []
        for gi, g in enumerate(genes):
            m_mm1 = media(gi, mm1_fc)
            diffs_mm1.append((g, m_mm1 - media(gi, grupos["CT_FC"])))
        diffs_mm1.sort(key=lambda t: t[1])
        L += ["", f"### Subgrupo MM1 (n={len(mm1_fc)}) vs. controles — top 5 up/down",
              "", "| Gene | Δ(MM1−CT) |", "|---|---|"]
        for g, d in reversed(diffs_mm1[-5:]):
            L.append(f"| {g} | +{d:.2f} |")
        for g, d in diffs_mm1[:5]:
            L.append(f"| {g} | {d:.2f} |")

    L += ["", "## Top 10 genes MAIS expressos em CJD (córtex frontal)",
          "", "| Gene | Média CJD | Média CT | Δ |", "|---|---|---|---|"]
    for g, d, mc, mt in reversed(fc_diffs[-10:]):
        L.append(f"| {g} | {mc:.1f} | {mt:.1f} | +{d:.1f} |")

    L += ["", "## Top 10 genes MENOS expressos em CJD (córtex frontal)",
          "", "| Gene | Média CJD | Média CT | Δ |", "|---|---|---|---|"]
    for g, d, mc, mt in fc_diffs[:10]:
        L.append(f"| {g} | {mc:.1f} | {mt:.1f} | {d:.1f} |")

    prnp = [(g, d) for g, d, *_ in fc_diffs if "PRNP" in g.upper()]
    L += ["", "## Verificação específica"]
    L.append(f"- PRNP presente no painel: {'sim → Δ(CJD−CT) = %+.2f' % prnp[0][1] if prnp else 'não (painel é de neuroinflamação)'}")

    # --- Estatística inferencial: Welch t-test + BH-FDR -------------------
    resultado = []
    for gi, g in enumerate(genes):
        xs = [vals[gi][i] for i in grupos["CJD_FC"]]
        ys = [vals[gi][i] for i in grupos["CT_FC"]]
        _, p = welch(xs, ys)
        resultado.append((g, p))
    m = len(resultado)
    ordenado = sorted(resultado, key=lambda t: t[1])
    fdr = [0.0] * m
    prev = 1.0
    for k in range(m - 1, -1, -1):
        val = min(prev, ordenado[k][1] * m / (k + 1))
        fdr[k] = val
        prev = val
    qmap = dict(zip((g for g, _ in ordenado), fdr))
    sig = [(g, p, qmap[g]) for g, p in ordenado if qmap[g] < 0.05]

    L += ["", "## Estatística inferencial (Welch + BH-FDR, córtex frontal)",
          f"- Genes testados: {m} · Significativos com FDR<0.05: **{len(sig)}**"]
    if sig:
        L += ["", "| Gene | p | q(FDR) |", "|---|---|---|"]
        L += [f"| {g} | {p:.2e} | {q:.2e} |" for g, p, q in sig[:15]]

    L += ["", "## Nota de honestidade científica",
          "- Welch t-test bicaudal implementado em stdlib; FDR Benjamini–Hochberg.",
          "- Painel dirigido (800 genes neuroinflamatórios), não transcriptoma total.",
          "- Sem correção para covariáveis (idade, PMI) — os metadados brutos não as trazem."]

    destino = REPORTS / "relatorio_gse160208.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] {destino}")
    print(f"[ok] amostras={len(amostras)} genes={len(genes)} "
          f"CJD_FC={len(grupos['CJD_FC'])} CT_FC={len(grupos['CT_FC'])}")


if __name__ == "__main__":
    main()
