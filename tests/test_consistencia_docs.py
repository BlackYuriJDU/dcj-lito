# -*- coding: utf-8 -*-
"""test_consistencia_docs.py — turning the project's consistency rule into a CI gate.

Project rule: after correcting a script, regenerate the derived reports. A stale
report plus a new script is a silent inconsistency. This file turns that rule —
and, since 2026-10-04, a set of scientific-integrity invariants — into gates that
fail the build.

Text files only (tracked in git); large datasets stay out of CI by design.
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


def test_offset_genomico_declarado_como_nao_validado():
    """A conversão GRCh38→GRCh37 por offset constante é a maior suposição não
    validada da colocalização. Os scripts NÃO podem afirmar que ela foi validada."""
    proibido = re.compile(r"validado por Ensembl MAP", re.I)
    for nome in ("coloc_stx6_eqtl.py", "coloc_meta_stx6.py",
                 "coloc_sqtl_stx6.py", "crosscheck_coloc_R.py"):
        txt = ler(f"pipeline/scripts/{nome}")
        assert not proibido.search(txt), \
            f"{nome} superdeclara validação do offset GRCh38→GRCh37"


# ---------------------------------------------------------------- figuras
def test_figuras_principais_existem():
    for png in ("volcano_gse160208.png", "volcano_gse140069.png",
                "heatmap_top_genes.png", "timeline_caso_referencia.png",
                "manhattan_gwas.png", "forest_mirnas.png",
                "coloc_stx6_regional.png"):
        assert (FIGS / png).exists(), f"figura ausente: {png}"


def test_sem_figura_legada_com_nome_de_pessoa():
    legado = FIGS / "timeline_caso_referencia.png"
    assert not legado.exists(), "figura legada com nome de pessoa voltou ao repo"


# ---------------------------------------------------------------- citável
def test_citation_tem_doi_e_autor():
    txt = ler("CITATION.cff")
    assert "10.5281/zenodo.22164910" in txt, "DOI ausente no CITATION.cff"
    assert "Araújo" in txt and "Arthur" in txt


def test_readme_badge_doi():
    for readme in ("README.md", "README.en.md"):
        txt = ler(readme)
        assert "zenodo.22164910" in txt, f"badge DOI ausente em {readme}"
    assert not re.search(r"60 miRNAs sig\b", ler("README.md")), \
        "número v1 (60 miRNAs sig) voltou ao README"


# ------------------------------------------------- integridade científica
# Gates adicionados em 2026-10-04 após auditoria que encontrou alegações de
# ineditismo falsas e números atribuídos à variante errada. Cada regra abaixo
# existiu porque o erro correspondente já aconteceu uma vez.

def test_preprint_nao_afirma_ineditismo():
    """rs3747957 e a mediação de expressão por STX6 já foram publicadas [1,4].
    O manuscrito não pode reapresentá-las como descobertas próprias."""
    txt = ler("preprint/manuscrito_preprint.md")
    for proibido in ("previously unreported", "unremarked for five years",
                     "sleep in deposited data"):
        assert proibido not in txt, \
            f"alegação de ineditismo reintroduzida: {proibido!r}"
    # a ressalva do locus chr16 precisa continuar presente, em qualquer redação
    assert re.search(r"not a new locus|as an observation", txt), \
        "ressalva de que chr16 não é locus novo foi removida"


def test_preprint_cita_primeiro_autor_coreto():
    """Jones E é o primeiro autor; Mead S é o último dos 65 (autor sênior)."""
    txt = ler("preprint/manuscrito_preprint.md")
    assert "Jones E" in txt, "citação primária correta (Jones E) ausente"
    assert "Mead S" not in txt, "manuscrito voltou a citar 'Mead S' como primeiro autor"


def test_preprint_referencia_4_completa():
    txt = ler("preprint/manuscrito_preprint.md")
    assert "10.1093/brain/awaf032" in txt, \
        "referência 4 (Brain 2025) sem DOI verificado"


def test_p_eqtl_atribuido_a_variante_certa():
    """O lead (chr1:180,961,245) tem p = 7.60e-47. O valor 6.60e-47 pertence a
    outra variante (180,949,780, mínimo regional). Atribuir o menor ao lead é
    um erro que já ocorreu e foi corrigido uma vez."""
    txt = ler("preprint/manuscrito_preprint.md")
    assert "7.60×10⁻⁴⁷" in txt, "p do eQTL do lead (7.60e-47) ausente"
    # toda menção a 6.60e-47 precisa ser qualificada como mínimo regional, seja
    # antes ("the regional minimum ... reaches p = 6.60e-47") ou depois
    # ("a different variant, at chr1:180,949,780, with p = 6.60e-47")
    qualificadores = ("180,949,780", "regional minimum", "mínimo regional",
                      "different variant", "outra variante")
    for m in re.finditer(r"6\.60×10⁻⁴⁷", txt):
        janela = txt[max(0, m.start() - 220): m.end() + 220]
        assert any(q in janela for q in qualificadores), \
            f"6.60e-47 sem qualificação de mínimo regional: ...{janela[:120]}..."


def test_pvals_de_headline_preservados():
    txt = ler("preprint/manuscrito_preprint.md")
    for pv in ("1.62×10⁻¹⁵", "6.18×10⁻¹⁰", "7.51×10⁻⁹"):
        assert pv in txt, f"p-valor de headline ausente: {pv}"


def test_sqtl_tem_ressalva_de_poder():
    txt = ler("preprint/manuscrito_preprint.md")
    assert "not evidence of absence" in txt, \
        "ressalva de poder do sQTL removida (zero detecção ≠ ausência)"
    assert "exist in any cohort" not in txt, \
        "sQTL: 'exist' (prova negativa) reintroduzido"


def test_preprint_v04_e_assinado():
    txt = ler("preprint/manuscrito_preprint.md")
    assert "v0.4" in txt, "preprint não está em v0.4"
    assert "Arthur Araújo" in txt
    assert "84 FDR-significant miRNAs" in txt, \
        "wording FDR (correção 29/08) reverteu"


def test_confundimento_idade_atribuido():
    """Fase 2 (2026-10-04): o colapso 84→1 é atribuído a idade ~97% (88→4),
    RIN 62 (88→26), sexo 3 (88→85), com VIF < 1.4. O manuscrito não pode voltar
    a dizer "fully explains" (superdeclara) nem omitir a atribuição medida."""
    txt = ler("preprint/manuscrito_preprint.md")
    assert "fully explains" not in txt, \
        "\"fully explains\" reintroduzido: a idade responde por ~97%, não 100%"
    assert "97%" in txt, "atribuição medida (~97%) ausente do manuscrito"
    assert "variance-inflation" in txt, \
        "VIF não citado: sem ele a atribuição não é identificável"

    rel = ler("pipeline/reports/relatorio_gse140069_idade.md")
    for numero in ("113", "91", "88", "26", "1.37", "1.32"):
        assert numero in rel, f"número-chave do teste de idade ausente: {numero}"
    assert "não aditivas" in rel, \
        "contribuições de covariáveis apresentadas como aditivas (somariam >100%)"


# ---------------------------------------------------------------- scripts
def test_oraculos_estatisticos_disponiveis():
    """test_stats_core.py faz pytest.importorskip("scipy.stats") — sem scipy a
    regressão de welch/tcdf_p/fdr_bh/cohen_d contra as implementações de
    referência é silenciosamente pulada. Este gate falha alto em vez de deixar
    o build verde sem validar o núcleo estatístico."""
    faltando = []
    for mod, pkg in (("scipy.stats", "scipy"), ("statsmodels.stats.multitest",
                                                "statsmodels"), ("numpy", "numpy")):
        try:
            import importlib
            importlib.import_module(mod)
        except ImportError:
            faltando.append(pkg)
    assert not faltando, (
        f"pacotes ausentes: {', '.join(faltando)} — "
        "pip install numpy scipy statsmodels")


def test_finemap_parametriza_populacao():
    txt = ler("pipeline/scripts/finemap_ld.py")
    assert "LD_POP" in txt, "finemap_ld.py perdeu a parametrização de população"
    assert "POP_TAG" in txt, "cache de LD não é chaveado por população"


# ---------------------------------------------------------------- privacidade
def test_arquivos_privados_nao_rastreados():
    """Nenhum arquivo de caso real pode voltar ao índice do git."""
    import subprocess
    r = subprocess.run(["git", "ls-files"], cwd=BASE, capture_output=True, text=True)
    rastreados = set(r.stdout.split("\n"))
    for proibido in ("pasted.txt", "pasted.png", "MEMORIA.md",
                     "ARQUIVO_COMPLETO.md", "research/caso_real_contexto.md",
                     "research/ecossistema_ciencia_aberta_mapa.md",
                     "research/verificacao_ensaios_ion717_prism_2026-08-26.md"):
        assert proibido not in rastreados, \
            f"arquivo privado rastreado de novo: {proibido}"