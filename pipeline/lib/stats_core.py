#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stats_core.py — Núcleo estatístico do Projeto DCJ-Lito.

Implementações de referência em stdlib puro (extraídas VERBATIM dos scripts de
análise que geraram os relatórios v1). Validadas contra scipy/R em
tests/test_stats_core.py (tolerância 1e-9 relativa). Os scripts originais
mantêm suas cópias locais para reproduibilidade byte-a-byte dos relatórios
já publicados; novos scripts devem importar daqui.
"""
import math
from typing import Dict, List, Tuple

__all__ = ["welch", "tcdf_p", "fdr_bh", "cohen_d"]


def welch(xs: List[float], ys: List[float]) -> Tuple[float, float]:
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


def fdr_bh(pares: List[Tuple[str, float]]) -> Dict[str, float]:
    """Benjamini-Hochberg FDR: {id: q}. Equivalente a p.adjust('BH') no R."""
    m = len(pares)
    ordenado = sorted(pares, key=lambda t: t[1])
    prev, out = 1.0, {}
    for k in range(m - 1, -1, -1):
        prev = min(prev, ordenado[k][1] * m / (k + 1))
        out[ordenado[k][0]] = prev
    return out


def cohen_d(xs: List[float], ys: List[float]) -> float:
    """Tamanho de efeito d de Cohen (pooled)."""
    n1, n2 = len(xs), len(ys)
    m1, m2 = sum(xs) / n1, sum(ys) / n2
    v1 = sum((x - m1) ** 2 for x in xs) / (n1 - 1)
    v2 = sum((y - m2) ** 2 for y in ys) / (n2 - 1)
    sp = math.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    return (m1 - m2) / sp if sp > 0 else float("nan")
