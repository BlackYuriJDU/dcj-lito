#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
monta_arquivo_completo.py — Monta o ARQUIVO_COMPLETO.md definitivo: a ÍNTEGRA
de todos os documentos do projeto, em ordem narrativa, + apêndice técnico com
código-fonte, checksums dos dados brutos e inventário.

Idempotente: roda quantas vezes quiser; sempre reconstrói do zero.
"""
import hashlib
import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]

# (título da seção, [arquivos]) — ordem narrativa
ESTRUTURA = [
    ("DIÁRIO DA SESSÃO — CRONOLOGIA COMPLETA",
     ["MEMORIA.md"]),
    ("CONTEXTO DO CASO REAL E LIMITES ÉTICOS",
     ["research/caso_real_contexto.md"]),
    ("CASO REFERÊNCIA (SIMULADO) — DOSSIÊ, EXAMES, LINHA DO TEMPO E FONTES",
     ["caso_referencia/dossie_clinico.md", "caso_referencia/exames_simulados.csv",
      "caso_referencia/linha_do_tempo.csv", "caso_referencia/fontes.md",
      "pipeline/reports/relatorio_caso_referencia.md"]),
    ("ESTADO DA ARTE — TUDO O QUE A CIÊNCIA SABE (2024–2026)",
     ["research/estado_da_arte_dcj.md"]),
    ("CATÁLOGOS DE DADOS PÚBLICOS E MAPA DO ECOSSISTEMA",
     ["research/catalogo_datasets_prionicas_CJD.md", "research/datasets_publicos.md",
      "research/ecossistema_ciencia_aberta_mapa.md"]),
    ("ANÁLISE 1 — CÉREBRO GSE160208 (r=1.000 vs. artigo)",
     ["pipeline/reports/relatorio_gse160208.md"]),
    ("ANÁLISE 2 — SANGUE GSE140069 v3 (pós-auditoria C2)",
     ["pipeline/reports/relatorio_gse140069.md"]),
    ("PONTE CASO SIMULADO × COORTE REAL",
     ["pipeline/reports/relatorio_ponte_caso_referencia.md"]),
    ("GWAS GCST90001389 — QC INDEPENDENTE (réplica 3/3 dos loci)",
     ["pipeline/reports/relatorio_qc_gwas_gcst90001389.md"]),
    ("FINE-MAPPING DESCRITIVO DOS LOCI",
     ["pipeline/reports/relatorio_finemap_loci.md"]),
    ("VALIDAÇÕES CRUZADAS CONTRA AS PUBLICAÇÕES ORIGINAIS",
     ["pipeline/reports/validacao_cruzada_gse160208_artigo_original.md",
      "pipeline/reports/validacao_cruzada_gse140069.md"]),
    ("AUDITORIAS DE TERCEIROS — UTILIDADE E ESTATÍSTICA ADVERSARIAL",
     ["colaboracao/auditoria_cetica_utilidade.md",
      "colaboracao/laudo_estatistico_adversarial.md"]),
    ("SIMULAÇÃO DA CASCATA PRIÔNICA — 7 CENÁRIOS DE INTERVENÇÃO",
     ["pipeline/reports/relatorio_simulacao_cascata.md"]),
    ("VARREDURA DE BLINDAGEM — LIMIAR DE PERCOLAÇÃO (~41%)",
     ["pipeline/reports/relatorio_varredura_blindagem.md"]),
    ("SIMULAÇÃO CALIBRADA POR DADOS EPIDEMIOLÓGICOS REAIS (V1-V3)",
     ["pipeline/reports/relatorio_simulacao_calibrada.md"]),
    ("HIPÓTESE GERADORA — ALFÂNDEGA INTERCELULAR SELETIVA",
     ["colaboracao/hipotese_alfandega_intercelular.md"]),
    ("MATERIAL PARA FAMÍLIAS E PARA LABORATÓRIOS",
     ["colaboracao/guia_de_familias.md", "colaboracao/carta_lito.md",
      "colaboracao/carta_projeto.md", "colaboracao/carta_prion_alliance.md",
      "colaboracao/carta_hc_usp.md", "colaboracao/centros_alvo.md"]),
    ("MEMÓRIA DO PROJETO — ERROS, DECISÕES E PADRÕES",
     ["memory/mistakes.md", "memory/decisions.md", "memory/successful-patterns.md"]),
    ("APÊNDICE A — CÓDIGO-FONTE COMPLETO DOS 11 SCRIPTS",
     ["pipeline/scripts/analise_caso_referencia.py", "pipeline/scripts/analise_gse160208.py",
      "pipeline/scripts/analise_gse140069.py", "pipeline/scripts/ponte_caso_referencia.py",
      "pipeline/scripts/qc_gwas_gcst90001389.py", "pipeline/scripts/finemap_stx6.py",
      "pipeline/scripts/finemap_ld.py", "pipeline/scripts/simulacao_prion.py",
      "pipeline/scripts/varredura_blindagem.py",
      "pipeline/scripts/simulacao_calibrada.py",
      "pipeline/scripts/gera_figuras.py"]),
]


def md5(caminho: Path) -> str:
    h = hashlib.md5()
    with open(caminho, "rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def main() -> None:
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = [
        "# ARQUIVO COMPLETO TOTAL — Projeto DCJ - Lito",
        "## A íntegra de tudo: contexto, dossiês, pesquisas, análises, validações,",
        "## auditorias, cartas, memória e código-fonte — num único documento",
        f"*Montado por `monta_arquivo_completo.py` em {agora}*",
        "",
        "**ÍNDICE**",
        "",
    ]
    n = 0
    for titulo, _ in ESTRUTURA:
        n += 1
        L.append(f"{n}. {titulo}")
    L += [f"{n+1}. APÊNDICE B — METADADOS: dados brutos, figuras e inventário", "",
          "---", ""]

    # Seções com arquivos inline
    for titulo, arquivos in ESTRUTURA:
        n = ESTRUTURA.index((titulo, arquivos)) + 1
        L += [f"# {n}. {titulo}", ""]
        for rel in arquivos:
            caminho = BASE / rel
            if not caminho.exists():
                L += [f"### ⚠️ arquivo ausente: `{rel}`", ""]
                continue
            conteudo = caminho.read_text(encoding="utf-8").strip()
            fence = "```"
            if rel.endswith((".csv", ".py")):
                L += [f"### 📄 `{rel}` (íntegra)", "", f"{fence}{rel.split('.')[-1]}",
                      conteudo, fence, ""]
            else:
                # markdown inline: rebaixa headings 1 nível p/ não quebrar estrutura
                rebaixado = "\n".join(
                    ("#" + ln if ln.startswith("#") else ln)
                    for ln in conteudo.splitlines())
                L += [f"### 📄 `{rel}` (íntegra)", "", "---", "", rebaixado,
                      "", "---", ""]

    # Apêndice B: metadados
    L += [f"# {len(ESTRUTURA)+1}. APÊNDICE B — METADADOS", "",
          "## Dados brutos baixados (grandes demais para embutir; checksums garantem integridade)",
          "", "| Arquivo | Bytes | MD5 | Fonte oficial |", "|---|---|---|---|"]
    fontes_dados = {
        "GCST90001389_buildGRCh37.tsv.gz": "GWAS Catalog / EBI (Lancet Neurol 2020, PMID 32949544)",
        "GSE140069_dados_processados.xlsx": "GEO GSE140069 suplemento (Nat Commun 2020, PMID 32769986)",
        "GSE140069_series_matrix.txt.gz": "NCBI GEO GSE140069",
        "GSE160208_series_matrix.txt.gz": "NCBI GEO GSE160208 (PMID 33375642)",
        "exames_simulados.csv": "produção própria (Caso Referência simulado)",
        "linha_do_tempo.csv": "produção própria (Caso Referência simulado)",
    }
    for nome, fonte in fontes_dados.items():
        c = BASE / "pipeline" / "data" / nome
        if c.exists():
            L.append(f"| pipeline/data/{nome} | {c.stat().st_size:,} | "
                     f"`{md5(c)}` | {fonte} |")
    L += ["", "## Figuras (`pipeline/reports/figuras/`)",
          "", "| PNG | Conteúdo |", "|---|---|",
          "| volcano_gse160208.png | Córtex frontal sCJD×CT, FDR<0.05 destacado |",
          "| volcano_gse140069.png | Sangue, modelo OLS ajustado idade+sexo+RIN (v3) |",
          "| heatmap_top_genes.png | Top 25 genes × 24 amostras FC (z-score por gene) |",
          "| timeline_caso_referencia.png | Progressão típica sCJD MM1 (simulado) |", "",
          "## Regras éticas (repetidas no fim, porque importa)",
          "- Somente dados públicos/anonimizados; nenhum dado novo de pacientes.",
          "- 'Caso Referência' é perfil genérico de treino, sem correspondente real.",
          "- Sobre o caso real público: apenas fatos de imprensa como contexto.",
          "- Este material NÃO é informação médica sobre pessoa alguma.", "",
          "*Fim do arquivo completo.*"]

    destino = BASE / "ARQUIVO_COMPLETO.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    kb = destino.stat().st_size / 1024
    print(f"[ok] {destino} — {kb:.0f} KB, {len(L)} linhas")


if __name__ == "__main__":
    main()
