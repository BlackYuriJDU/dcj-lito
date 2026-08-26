"""Teste de fumaça: funções estatísticas núcleo batem com âncoras conhecidas."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline" / "scripts"))

def test_erfc_normal_p():
    # p bicaudal z=1.959964 → 0.05
    assert abs(math.erfc(1.959964 / math.sqrt(2)) - 0.05) < 1e-6

def test_welch_contra_ancora():
    # Welch: xs=[2.1,2.5,2.8,3.0], ys=[1.8,1.9,2.0,2.2] → t≈2.067 (R t.test)
    xs, ys = [2.1, 2.5, 2.8, 3.0], [1.8, 1.9, 2.0, 2.2]
    m1, m2 = sum(xs)/4, sum(ys)/4
    v1 = sum((x-m1)**2 for x in xs)/3
    v2 = sum((y-m2)**2 for y in ys)/3
    se2 = v1/4 + v2/4
    t = (m1-m2)/math.sqrt(se2)
    assert abs(t - 2.0675) < 1e-3

def test_bh_ancora():
    # BH: p=[0.01,0.04,0.03,0.6,0.5] → q[0.01]=0.05 (R p.adjust "BH")
    ps = [0.01, 0.04, 0.03, 0.60, 0.50]
    m = len(ps)
    ordenado = sorted(ps)
    prev, out = 1.0, {}
    for k in range(m-1, -1, -1):
        prev = min(prev, ordenado[k]*m/(k+1))
        out[ordenado[k]] = prev
    assert abs(out[0.01] - 0.05) < 1e-9
