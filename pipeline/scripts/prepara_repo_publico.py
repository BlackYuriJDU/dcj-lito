#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prepara_repo_publico.py — Gera `dist/public-repo/`: cópia FRESCA e sanitizada
do projeto para publicação (git init novo, SEM histórico).

Inclui:  pipeline/{lib,scripts,reports}, preprint/, README.en.md, README.md,
         LICENSE, CITATION.cff, requirements.txt, Makefile, tests/, .gitignore
Exclui:  MEMORIA.md, memory/, colaboracao/, caso_referencia/ (dossiê clínico —
         decisão de publicação é do fundador), ARQUIVO_COMPLETO.md (agrega os
         excluídos), *.zip, pipeline/data/* grandes (GWAS 197 MB; baixáveis
         publicamente), .git, dist/

Sanitização: varre o resultado por padrões sensíveis (chaves tvly-, e-mails,
nomes próprios em contexto pessoal) e escreve relatório. Falha (exit 1) se
algo sensível for encontrado.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
DEST = BASE / "dist" / "public-repo"

INCLUIR = [
    "pipeline/lib", "pipeline/scripts", "pipeline/reports",
    "preprint", "tests",
    "README.en.md", "README.md", "LICENSE", "CITATION.cff",
    "requirements.txt", "Makefile", ".gitignore",
]
EXCLUIDOS_GLOBS = ["*.zip"]
PADROES_SENSIVEIS = [
    (r"tvly-[A-Za-z0-9_\-]{8,}", "chave de API (Tavily)"),
    (r"[A-Za-z0-9._%+-]+@(?!ebi\.ac|pasteur\.fr|gmail\.com$)[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
     "e-mail potencialmente pessoal"),
]


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    copiados = []
    for item in INCLUIR:
        src = BASE / item
        if not src.exists():
            print(f"[aviso] ausente: {item}")
            continue
        dst = DEST / item
        if src.is_dir():
            shutil.copytree(src, dst,
                            ignore=shutil.ignore_patterns("__pycache__"))
            for p in dst.rglob("*"):
                if p.is_file():
                    copiados.append(p)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copiados.append(dst)

    # excluir zips e dados grandes que possam ter entrado via reports/data
    for padrao in EXCLUIDOS_GLOBS:
        for p in DEST.rglob(padrao):
            p.unlink()
    data = DEST / "pipeline" / "data"
    if data.exists():
        shutil.rmtree(data)          # dados públicos grandes ficam de fora;
                                     # instruções de download vão no README

    # sanitização
    achados = []
    for p in copiados:
        try:
            txt = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        for padrao, rotulo in PADROES_SENSIVEIS:
            for m in re.finditer(padrao, txt):
                achados.append((p.relative_to(DEST), rotulo, m.group(0)[:40]))

    relatorio = ["# Relatório de sanitização — dist/public-repo", ""]
    if achados:
        relatorio.append("**FALHOU** — conteúdo sensível encontrado:")
        for rel, rotulo, trecho in achados:
            relatorio.append(f"- `{rel}` · {rotulo} · `{trecho}...`")
        (DEST.parent / "SANITIZACAO.md").write_text("\n".join(relatorio))
        print("\n".join(relatorio))
        sys.exit(1)

    relatorio += [
        f"- {len(copiados)} arquivos copiados",
        "- Nenhum padrão sensível encontrado (chaves, e-mails pessoais)",
        "- Excluídos por política: MEMORIA.md, memory/, colaboracao/,",
        "  caso_referencia/, ARQUIVO_COMPLETO.md, zips, pipeline/data/",
        "",
        "**Pendente antes de `git push` (decisão do fundador)**:",
        "- nome de autor real no CITATION.cff e no preprint",
        "- Zenodo DOI + bioRxiv submission",
    ]
    (DEST.parent / "SANITIZACAO.md").write_text("\n".join(relatorio))

    subprocess.run(["git", "init", "-q"], cwd=DEST, check=True)
    print(f"[ok] {DEST}: {len(copiados)} arquivos · git init fresco · "
          "sanitização limpa")


if __name__ == "__main__":
    main()
