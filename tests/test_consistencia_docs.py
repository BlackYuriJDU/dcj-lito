# -*- coding: utf-8 -*-
"""test_consistencia_docs.py — turning the project's consistency rule into a CI gate.

Project rule: after correcting a script, regenerate the derived reports. A stale
report plus a new script is a silent inconsistency. This file turns that rule —
and, since 2026-10-04, a set of scientific-integrity invariants — into gates that
fail the build.

Text files only (tracked in git); large datasets stay out of CI by design.
"""
import json
import re
import subprocess
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


def test_offset_genomico_verificado_sem_exagero():
    """O offset GRCh38→GRCh37 de STX6 foi medido em 2026-10-04 contra a API de
    assembly map do Ensembl (relatorio_validacao_offset_genomico.md).

    Isso torna FALSOS os dois extremos que o texto já afirmou em versões
    diferentes: "não foi validado" (docstring de 2026-10-03) e "validado por
    Ensembl MAP" (manuscrito, que sugeria uma validação de cadeia inexistente —
    o parser de chain file próprio foi escrito, provado defeituoso e
    descartado). O que é verdade hoje é estreito: verificação por assembly map,
    sem cadeia. O gate prende os dois lados.
    """
    alvos = [f"pipeline/scripts/{n}" for n in
             ("coloc_stx6_eqtl.py", "coloc_meta_stx6.py",
              "coloc_sqtl_stx6.py", "crosscheck_coloc_R.py")]

    # (1) não afirmar validação por chain/liftOver — nunca foi feita
    for rel in alvos:
        txt = ler(rel)
        for padrao in (r"validad\w*.{0,60}(chain|liftOver)",
                       r"(chain|liftOver).{0,60}validad"):
            assert not re.search(padrao, txt, re.I), \
                f"{rel} afirma validação por chain/liftOver, que não ocorreu"

    # (2) não continuar chamando de suposição não validada — deixou de ser verdade
    for rel in alvos:
        txt = ler(rel)
        assert not re.search(r"n[aã]o (foi )?validad|n[aã]o validada",
                             txt, re.I), \
            f"{rel} ainda chama o offset de não validado"

    # (3) o manuscrito não pode superdeclarar: assembly map não é liftOver
    ms = ler("preprint/manuscrito_preprint.md")
    assert not re.search(r"validad\w*.{0,60}(chain|liftOver)", ms, re.I), \
        "manuscrito afirma validação por chain/liftOver, que não ocorreu"

    # (4) a medição existe e registra o veredito
    rel = ler("pipeline/reports/relatorio_validacao_offset_genomico.md")
    for marca in ("+30,864", "9/9", "30/30"):
        assert marca in rel, f"marcador da validação ausente no relatório: {marca}"

    # (5) o manuscrito reflete o estado verificado
    assert "verified this offset against the Ensembl" in ms, \
        "manuscrito não registra a verificação do offset"


def test_cache_ensembl_consistente_com_a_constante():
    """O cache em disco guarda pares b37→b38 do Ensembl; o script regenerate o
    relatório a partir dele.

    Bug real de 2026-10-04: o cache continha pares com delta +30.865 (um +1 a
    mais). Como §1 calcula `p38 - p37` direto, um re-run teria reescrito o
    veredito do relatório de "+30.864, correto" para "+30.865, incorreto" sem
    erro, sem aviso e sem rede — o ensaio inteiro passaria. E o par errado era
    plausível à vista: 180941860→180972725 é o mapeamento *correto* de
    180941861, então a inspeção visual não pegaria.

    O cache é descartável (o script o reconstrói); se um dia for commitado, tem
    de concordar com a constante.
    """
    p = BASE / "pipeline" / "data" / "offset_ensembl_cache.json"
    if not p.exists():
        return                      # cache opcional; o script reconstrói
    d = json.loads(p.read_text(encoding="utf-8"))
    for k, v in d.items():
        assert v is not None, f"cache Ensembl com falha em b37={k}"
        delta = v - int(k)
        assert delta == 30_864, (
            f"cache Ensembl inconsistente com OFFSET_CONSTANTE: b37 {k} -> "
            f"b38 {v} (delta {delta}, esperado 30864). Um re-run trocaria o "
            f"veredito do relatório em silêncio.")


# ---------------------------------------------------------------- figuras
def test_figuras_principais_existem():
    for png in ("volcano_gse160208.png", "volcano_gse140069.png",
                "heatmap_top_genes.png", "timeline_caso_referencia.png",
                "manhattan_gwas.png", "forest_mirnas.png",
                "coloc_stx6_regional.png"):
        assert (FIGS / png).exists(), f"figura ausente: {png}"


def test_sem_figura_legada_com_nome_de_pessoa():
    """A linha do tempo de um caso real foi substituída por uma versão genérica.

    O guard não hardcoda o nome da pessoa (seria reintroduzi-la no repo): ele
    exige que a figura saneada exista e seja a ÚNICA da série timeline, de modo
    que a versão pessoal não possa voltar sem que este teste caia.
    """
    series = sorted(FIGS.glob("timeline_*.png"))
    assert [p.name for p in series] == ["timeline_caso_referencia.png"], (
        f"série timeline deve conter só a figura saneada; encontrada: "
        f"{[p.name for p in series]}")


# ---------------------------------------------------------------- privacidade
def test_nome_do_caso_ausente_do_repo():
    """O nome do caso real não pode reaparecer em arquivo versionado.

    Existe um motivo histórico: a lista de renomeação de 2026-10-04 cobriu o
    manuscrito, CITATION.cff, LICENSE e READMEs, mas não varreu os relatórios
    do "caso de referência" nem as linhas de proveniência — que ainda citavam
    scripts já renomeados (`analise_caso_referencia.py`). O guard é por substantivo,
    para pegar tanto "Caso Referência" quanto o slug antigo.
    """
    substantivo = re.compile(r"\bcaso_referencia\b|\bdcj ?- ?caso_referencia\b", re.I)
    extensoes = (".md", ".cff", ".py", ".sh", ".yml", ".yaml", ".txt",
                 ".csv", ".R", ".html", ".js", ".css", ".svg", ".json",
                 ".gitignore", ".cff")
    alvos = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True,
        encoding="utf-8", cwd=BASE).stdout.splitlines()
    # Só texto. Binários (.pdf, .gz, .xlsx, .png, .tbi) ficam de fora: o título
    # do PDF vai em metadata comprimida e se verifica descompactando; o resto
    # não tem onde esconder texto legível.
    vazamentos = []
    for rel in alvos:
        if not rel.endswith(extensoes):
            continue
        # Este próprio arquivo contém o termo (é o padrão do guard); autoexcluir.
        if Path(rel) == Path(__file__).relative_to(BASE):
            continue
        try:
            txt = (BASE / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if substantivo.search(txt):
            vazamentos.append(rel)
    assert not vazamentos, (
        f"nome do caso real reapareceu em: {vazamentos}")


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