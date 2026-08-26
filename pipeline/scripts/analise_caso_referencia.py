#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analise_caso_referencia.py — Pipeline v1 de análise do caso simulado "Caso Referência".

Lê os dados tabulares do caso em pipeline/data/, valida consistência,
calcula métricas simples e gera relatório markdown em pipeline/reports/.

Uso:
    python3 analise_caso_referencia.py

Princípios:
- Reproduzível: sem dependências além da stdlib.
- Rastreável: cada conclusão cita o arquivo/fonte de origem.
- Honestidade: dados simulados são rotulados como tal no relatório.
"""
import csv
import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]          # pipeline/
DATA = BASE / "data"
REPORTS = BASE / "reports"
REPORTS.mkdir(exist_ok=True)


def ler_csv(nome: str) -> list[dict]:
    with open(DATA / nome, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    exames = ler_csv("exames_simulados.csv")
    linha = ler_csv("linha_do_tempo.csv")

    # --- Validações de consistência -------------------------------------
    problemas: list[str] = []
    for e in exames:
        if not e.get("resultado_simulado", "").strip():
            problemas.append(f"Exame sem resultado: {e.get('exame')}")
        if not e.get("fonte_validacao", "").strip():
            problemas.append(f"Exame sem fonte: {e.get('exame')}")
    for l in linha:
        if not l.get("sintomas_observados", "").strip():
            problemas.append(f"Mês {l.get('mes_fase')} sem sintomas")

    achados_positivos = [
        e["exame"] for e in exames
        if any(k in e["resultado_simulado"].lower()
               for k in ("positivo", "elevada", "hiperintens"))
    ]

    # --- Critérios diagnósticos (CDC/NPDPSC) aplicados ao caso ----------
    criterios = {
        "Quadro clínico progressivo rápido": True,
        "RM DWI/FLAIR típica (gânglios da base + córtex)": any(
            "RM" in nome for nome in achados_positivos),
        "RT-QuIC positivo": any("RT-QuIC" in nome
                                for nome in achados_positivos),
        "14-3-3 positivo": any("14-3-3" in nome
                               for nome in achados_positivos),
        "EEG com PSWC": any("EEG" in e["exame"] and "PSWC"
                            in e["resultado_simulado"].upper()
                            for e in exames),
    }
    n_apoio = sum(1 for k, v in criterios.items() if v) - 1  # -1 quadro clínico
    diagnostico = ("PROVÁVEL sCJD (≥2 critérios de apoio atendidos)"
                   if n_apoio >= 2 else "INSUFICIENTE para provável")

    # --- Relatório -------------------------------------------------------
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    linhas = [
        "# Relatório automático — Caso Caso Referência (SIMULADO)",
        f"*Gerado por `analise_caso_referencia.py` em {agora}. Dados fictícios.*",
        "",
        "## Consistência dos dados",
        f"- Exames processados: **{len(exames)}** · Marcos clínicos: **{len(linha)}**",
        f"- Problemas encontrados: **{len(problemas)}**"
        + ("" if not problemas else "\n" + "\n".join(f"  - {p}" for p in problemas)),
        "",
        "## Critérios diagnósticos CDC/NPDPSC aplicados",
    ]
    for k, v in criterios.items():
        linhas.append(f"- [{'x' if v else ' '}] {k}")
    linhas += ["", f"## Conclusão diagnóstica simulada: **{diagnostico}**", "",
               "### Achados positivos", ""]
    linhas += [f"- {a}" for a in achados_positivos]
    linhas += ["", "## Próximos passos do pipeline",
               "1. Baixar dataset público real (catálogo em `research/datasets_publicos.md`).",
               "2. Repetir esta análise sobre dados REAIS anonimizados.",
               "3. Comparar perfil do caso simulado vs. distribuição real.",
               "", "---",
               "*Nota: este relatório não constitui diagnóstico médico real.*"]

    destino = REPORTS / "relatorio_caso_referencia.md"
    destino.write_text("\n".join(linhas), encoding="utf-8")
    print(f"[ok] Relatório gerado: {destino}")
    print(f"[ok] {len(exames)} exames, {len(linha)} marcos, {len(problemas)} problemas")


if __name__ == "__main__":
    main()
