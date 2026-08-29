# -*- coding: utf-8 -*-
"""test_consistencia_docs.py — Institucionaliza a auditoria de 2026-08-29:
checa coerência relatório↔script↔figuras↔citável em arquivos de TEXTO
(rastreáveis no git; dados grandes ficam fora do CI por design).

Regra do projeto (memory/decisions.md): depois de corrigir um script,
REGENERAR os relatórios derivados; relatório antigo + script novo =
inconsistência silenciosa. Este teste transforma essa regra em gate.
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
REPORTS = BASE / "pipeline" / "reports"
FIGS = REPORTS / "figuras"
SCRIPTS = BASE / "pipeline" / "scripts"


def ler(rel: str) -> str:
    p = BASE / rel
    assert p.exists(), f"arquivo ausente: {rel}"
    return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------- GSE140069
def test_relatorio_gse140069_e_v3():
    txt = ler("pipeline/reports/relatorio_gse140069.md")
    assert "v3" in txt.splitlines()[0] + txt.splitlines()[1], \
        "relatório GSE140069 não é v3"
    script = ler("pipeline/scripts/analise_gse140069.py")
    assert "v3" in script[:1200], "script analise_gse140069.py não declara v3"
    for numero in ("84", "**1**", "0.048"):
        assert numero in txt, f"número-chave v3 ausente no relatório: {numero}"


# ---------------------------------------------------------------- coloc STX6
def test_coloc_meta_tem_h2_e_validacao():
    txt = ler("pipeline/reports/relatorio_coloc_meta_stx6.md")
    assert "H2" in txt, "relatório coloc não exibe H2 (correção 29/08)"
    assert "0.9950" in txt, "H3 padrão (0.9950) ausente"
    valid = ler("pipeline/reports/relatorio_validacao_coloc_R.md")
    assert "0.994997" in valid, "validação R (0.994997) ausente"


def test_validacao_eur_existe():
    txt = ler("pipeline/reports/relatorio_finemap_loci_EUR.md")
    assert "phase_3:EUR" in txt
    assert "90.5%" in txt, "massa STX6 (90.5%) ausente no run EUR"


# ---------------------------------------------------------------- figuras
def test_figuras_principais_existem():
    for png in ("volcano_gse160208.png", "volcano_gse140069.png",
                "heatmap_top_genes.png", "timeline_caso_referencia.png",
                "manhattan_gwas.png", "forest_mirnas.png",
                "coloc_stx6_regional.png"):
        assert (FIGS / png).exists(), f"figura ausente: {png}"


def test_sem_figura_legado_timeline_lito():
    assert not (FIGS / "timeline_lito.png").exists(), \
        "timeline_lito.png (legado) voltou ao repo"


# ---------------------------------------------------------------- citável
def test_citation_tem_doi_e_autor():
    txt = ler("CITATION.cff")
    assert "10.5281/zenodo.22164910" in txt, "DOI ausente no CITATION.cff"
    assert "Araújo" in txt and "Arthur" in txt


def test_preprint_v03_assinado():
    txt = ler("preprint/manuscrito_preprint.md")
    assert "v0.3" in txt, "preprint não está em v0.3"
    assert "Arthur Araújo" in txt
    assert "FDR<0.05 without covariate adjustment" in txt, \
        "wording FDR (correção 29/08) reverteu"


def test_readme_badge_doi():
    for readme in ("README.md", "README.en.md"):
        txt = ler(readme)
        assert "zenodo.22164910" in txt, f"badge DOI ausente em {readme}"
    assert not re.search(r"60 miRNAs sig\b", ler("README.md")), \
        "número v1 (60 miRNAs sig) voltou ao README"


# ---------------------------------------------------------------- scripts
def test_finemap_parametriza_populacao():
    txt = ler("pipeline/scripts/finemap_ld.py")
    assert "LD_POP" in txt, "finemap_ld.py perdeu a parametrização de população"
    assert "POP_TAG" in txt, "cache de LD não é chaveado por população"
