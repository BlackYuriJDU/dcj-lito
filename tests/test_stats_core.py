#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_stats_core.py — Regressão do núcleo estatístico contra scipy/R.

Cada função da lib é comparada com a implementação padrão do campo:
  welch/tcdf_p ↔ scipy.stats.ttest_ind(equal_var=False)
  fdr_bh       ↔ statsmodels multipletests fdr_bh (e âncora R p.adjust)
  cohen_d      ↔ cálculo direto com numpy
Tolerâncias: 1e-9 relativa (bem mais estrito que qualquer decisão do projeto).
"""
import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline" / "lib"))
from stats_core import cohen_d, fdr_bh, tcdf_p, welch  # noqa: E402

scipy_stats = pytest.importorskip("scipy.stats")


CASOS = [
    ([2.1, 2.5, 2.8, 3.0], [1.8, 1.9, 2.0, 2.2]),
    ([10.0, 12.4, 11.9, 9.8, 13.2, 11.1], [9.1, 10.0, 8.7, 9.9]),
    ([0.5, 0.7, 0.3], [1.5, 1.9, 2.2, 1.8, 2.0, 1.6]),
]


@pytest.mark.parametrize("xs,ys", CASOS)
def test_welch_vs_scipy(xs, ys):
    t_nosso, p_nosso = welch(xs, ys)
    r = scipy_stats.ttest_ind(xs, ys, equal_var=False)
    assert math.isclose(t_nosso, r.statistic, rel_tol=1e-9)
    assert math.isclose(p_nosso, r.pvalue, rel_tol=1e-9, abs_tol=1e-15)


@pytest.mark.parametrize("t,df", [(1.5, 10.0), (3.2, 45.7), (0.3, 2.5), (5.0, 120.0)])
def test_tcdf_p_vs_scipy(t, df):
    p_nosso = tcdf_p(t, df)
    p_scipy = 2.0 * scipy_stats.t.sf(t, df)
    assert math.isclose(p_nosso, p_scipy, rel_tol=1e-9, abs_tol=1e-15)


def test_fdr_bh_vs_statsmodels():
    sm = pytest.importorskip("statsmodels.stats.multitest")
    ps = [0.001, 0.008, 0.039, 0.041, 0.042, 0.06, 0.074, 0.205, 0.212, 0.216]
    pares = [(f"g{i}", p) for i, p in enumerate(ps)]
    q_nosso = fdr_bh(pares)
    q_sm = sm.multipletests(ps, method="fdr_bh")[1]
    for i in range(len(ps)):
        assert math.isclose(q_nosso[f"g{i}"], q_sm[i], rel_tol=1e-9, abs_tol=1e-15)


def test_fdr_bh_ancora_r():
    # R: p.adjust(c(.01,.04,.03,.6,.5), "BH")[1] == 0.05
    q = fdr_bh([(str(i), p) for i, p in enumerate([0.01, 0.04, 0.03, 0.6, 0.5])])
    assert abs(q["0"] - 0.05) < 1e-9


def test_cohen_d_vs_numpy():
    np = pytest.importorskip("numpy")
    xs, ys = CASOS[1]
    d_nosso = cohen_d(xs, ys)
    a, b = np.array(xs), np.array(ys)
    sp = math.sqrt(((len(a)-1)*a.var(ddof=1) + (len(b)-1)*b.var(ddof=1)) /
                   (len(a)+len(b)-2))
    assert math.isclose(d_nosso, (a.mean()-b.mean())/sp, rel_tol=1e-12)


def test_casos_degradados():
    assert welch([1.0, 1.0], [1.0, 1.0]) == (0.0, 1.0)   # variância zero
    assert fdr_bh([]) == {}                               # vazio
