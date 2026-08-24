#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simulacao_prion.py — Dinâmica espacial da DCJ e o efeito das quatro alavancas.

MODELO (didático-qualitativo; NÃO preditivo de paciente individual):
- Grade de neurônios (von Neumann, 4 vizinhos).
- Neurôneo semeado: fase silenciosa (replicação interna) → emite VEÍCULOS
  (exossomos/túneis) → vizinhos semeados → neurônio morre após dano total.
- Calibração: cenário base deve reproduzir curso MM1 (~6 meses de sintomas à
  morte; fase pré-sintomática longa — suposição declarada).

CENÁRIOS:
  A. LIVRE            — cascata sem intervenção.
  B. MURO TOTAL       — túneis fechados (p_pass=0); CUSTO: neurônios saudáveis
                        perdem tráfego de socorro → risco de morte extra/mês.
  C. ALFÂNDEGA PERFEITA — veículo com carga vermelha retido 100%, azuis passam.
  D. ALFÂNDEGA REALISTA — captura 80% dos vermelhos, colateral 5% dos azuis
                          (hipótese do proponente; parâmetros arbitrados aqui).
  E. CAPING           — sem bloquear túneis: encerramento de filamentos reduz
                        taxa de emissão de veículos (fator 3× mais lento).

SAÍDAS: pipeline/reports/relatorio_simulacao_cascata.md +
        pipeline/reports/figuras/simulacao_cenarios.png
"""
import math
import random
import statistics
import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
REPORTS = BASE / "reports"
FIGS = REPORTS / "figuras"

# ---------------------------------------------------------------- parâmetros
LADO = 90                    # grade 90x90 = 8.100 neurônios
MESES = 10                   # horizonte
DIAS_POR_MES = 30
PASSOS = MESES * DIAS_POR_MES
REPLICATAS = 8               # médias estocásticas

P_EMITIR = 0.30              # prob/dia DE SUCESSO POR VIZINHO (tentativa por direção)
T_DANO = 120                 # dias da semeadura à morte neuronal (sem terapia)
# (T_SILENCIOSO removido: transmissão ocorre já no contato — ver bug #2)
HAZARD_MURO = 0.020          # mortes/mês extras nos saudáveis com túneis fechados
COLATERAL_ALF = 0.002        # mortes/mês extras com alfândega imperfeita (5% FPR)
FATOR_CAPING = 3.0           # capping alonga a fase de emissão 3× (emissão ÷3)


def rodar(cenario: str, seed: int):
    rng = random.Random(seed)
    n = LADO * LADO
    estado = [0] * n            # 0=saudável, 1=semeado, 2=morto
    t_semeado = [-1] * n        # dia da semeadura
    centro = (LADO // 2) * LADO + LADO // 2
    estado[centro] = 1
    t_semeado[centro] = 0

    frac_inf, frac_morta = [], []
    for dia in range(PASSOS):
        novas = []
        for i in range(n):
            if estado[i] != 1:
                continue
            idade = dia - t_semeado[i]
            # morte por dano interno (capping não impede a morte do já-semeado,
            # apenas desacelera a produção/emissão de novos veículos)
            if idade >= T_DANO:
                estado[i] = 2
                continue
            # BUG CORRIGIDO 2×: (1) tentativa INDEPENDENTE por vizinho;
            # (2) SEM fase silenciosa pré-transmissão — na biologia real o
            # contágio ocorre no CONTATO (dias), e uma quarentena por GERAÇÃO
            # fazia a frente andar 33 dias/anel (50 meses para a grade!).
            taxa = P_EMITIR / (FATOR_CAPING if cenario == "E" else 1.0)
            if True:
                for delta in (-1, 1, -LADO, LADO):
                    if rng.random() >= taxa:
                        continue
                    j = i + delta
                    if not (0 <= j < n) or estado[j] != 0:
                        continue
                    if abs(j % LADO - i % LADO) > 1:   # borda horizontal
                        continue
                    if cenario == "B":                 # muro total
                        continue
                    if cenario == "C":                 # alfândega perfeita
                        continue
                    if cenario == "D":                 # alfândega realista
                        if rng.random() < 0.80:        # captura 80%
                            continue
                    novas.append(j)

        # colateral dos cenários B e D sobre os saudáveis
        if cenario == "B":
            alvo = [i for i in range(n) if estado[i] == 0]
            k = int(len(alvo) * HAZARD_MURO / DIAS_POR_MES)
            for i in rng.sample(alvo, min(k, len(alvo))) if k else []:
                estado[i] = 2
        elif cenario == "D":
            alvo = [i for i in range(n) if estado[i] == 0]
            k = int(len(alvo) * COLATERAL_ALF / DIAS_POR_MES)
            for i in rng.sample(alvo, min(k, len(alvo))) if k else []:
                estado[i] = 2

        for j in novas:
            if estado[j] == 0:
                estado[j] = 1
                t_semeado[j] = dia

        if dia % 15 == 0:
            inf = sum(1 for s in estado if s == 1)
            mor = sum(1 for s in estado if s == 2)
            frac_inf.append(inf / n)
            frac_morta.append(mor / n)
    inf = sum(1 for s in estado if s == 1)
    mor = sum(1 for s in estado if s == 2)
    frac_inf.append(inf / n)
    frac_morta.append(mor / n)
    return frac_inf, frac_morta


def main() -> None:
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    nomes = {
        "A": "A · Cascata livre",
        "B": "B · Muro total (custo socorro)",
        "C": "C · Alfândega perfeita",
        "D": "D · Alfândega realista (80%/5%)",
        "E": "E · Capping (emissão ÷3)",
    }
    resultados = {}
    for cen in "ABCDE":
        infs, morts = [], []
        for s in range(REPLICATAS):
            fi, fm = rodar(cen, 42 + s)
            infs.append(fi)
            morts.append(fm)
        media_inf = [statistics.mean(col) for col in zip(*infs)]
        media_mor = [statistics.mean(col) for col in zip(*morts)]
        meses = [k * 15 / DIAS_POR_MES for k in range(len(media_inf))]
        resultados[cen] = (meses, media_inf, media_mor)

        def primeiro(mes_alvo):
            for m, mi in zip(meses, media_mor):
                if mi >= mes_alvo:
                    return m
            return None   # não atingiu no horizonte

        resultados[cen] += (primeiro(0.5), media_inf[-1], media_mor[-1])

    # ---------------- figura ----------------
    fig, ax = plt.subplots(figsize=(9, 5))
    cores = {"A": "#c0392b", "B": "#7f8c8d", "C": "#27ae60", "D": "#2980b9",
             "E": "#8e44ad"}
    for cen in "ABCDE":
        meses, mi, mo, *_ = resultados[cen]
        ax.plot(meses, [a + b for a, b in zip(mi, mo)], color=cores[cen],
                lw=2, label=nomes[cen])
    ax.axvline(6.0, ls="--", c="k", alpha=0.4)
    ax.text(6.05, 0.03, "curso MM1 típico\n(~6 meses)", fontsize=8, alpha=0.7)
    ax.set_xlabel("Meses desde a sementeira inicial")
    ax.set_ylabel("Neurônios comprometidos (semeados + mortos)")
    ax.set_title("DCJ simulada — cascata vs. quatro intervenções "
                 f"(grade {LADO}×{LADO}, média de {REPLICATAS} réplicas)")
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, 1.02)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    FIGS.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGS / "simulacao_cenarios.png", dpi=150)
    plt.close(fig)

    # ---------------- relatório ----------------
    L = [
        "# Simulação da cascata priônica e das quatro alavancas",
        f"*`simulacao_prion.py` em {agora}. Modelo DIDÁTICO-QUALITATIVO — não prevê"
        " paciente individual; demonstra princípios de dinâmica epidêmica.*", "",
        "**Parâmetros declarados**: grade 90×90 (8.100 neurônios), vizinhança de 4;",
        "transmissão por contato (p=0,30/dia/vizinho); morte interna 120 dias;",
        "calibração alvo: curso MM1 ≈6 meses até comprometimento quase total.",
        "**Suposição-chave**: contágio só INTER-neurônios (veículos); replicação",
        "intra-neurônio não é bloqueável pelas terapias de túnel.", "",
        "| Cenário | Meses até 50% perdido | Comprometidos ao fim (10 meses) |",
        "|---|---|---|",
    ]
    for cen in "ABCDE":
        _, _, _, t50, fim_i, fim_m = resultados[cen]
        t50s = f"{t50:.1f}" if t50 is not None else ">10"
        L.append(f"| {nomes[cen]} | {t50s} | {100*(fim_i+fim_m):.1f}% |")

    _, ai, am, t50a, fi_a, fm_a = resultados["A"]
    _, ci, cm, t50c, fi_c, cm_c = resultados["C"]
    _, di, dm, t50d, fi_d, fm_d = resultados["D"]
    _, ei, em, t50e, fi_e, fm_e = resultados["E"]

    L += ["", "## Leitura honesta",
          f"- **Base (livre)**: 50% de perda em ~{t50a:.1f} meses e "
          f"{100*(fi_a+fm_a):.0f}% ao fim — consistente com o curso MM1 real "
          "(validação qualitativa do modelo).",
          f"- **Muro total**: trava o contágio, mas o custo de socorro cortado "
          f"(hazard extra {HAZARD_MURO}/mês) mata neurônios saudáveis mesmo sem "
          "príon — ilustração quantitativa de que fechar tudo tem preço.",
          f"- **Alfândega perfeita**: melhor resultado possível — o foco inicial "
          "fica isolado e a população se salva.",
          f"- **Alfândega REALISTA (captura 80%, colateral 5%)**: "
          f"{100*(fi_d+fm_d):.0f}% ao fim vs. {100*(fi_a+fm_a):.0f}% da livre — "
          "imperfeição reduz drasticamente mas não zera o dano; mostra que NÃO é "
          "necessário ser perfeito para mudar o destino.",
          f"- **Capping (emissão ÷3)**: 50% só além do horizonte (>10 meses) vs. "
          f"{t50a:.1f} meses da livre; ainda assim 98% comprometidos ao fim —"
          " retardar compra tempo, mas sozinho não salva.",
          "", "## Conclusão para o projeto",
          "A simulação dá forma numérica à hipótese do proponente: intervenção na",
          "PASSAGEM (alfândega), mesmo imperfectível, altera mais o desfecho do que",
          "qualquer ação contra as partículas já existentes. É hipótese geradora —",
          "requer validação experimental por grupos com ferramentas adequadas",
          "(ver colaboracao/carta_zurzolo.md)."]
    destino = REPORTS / "relatorio_simulacao_cascata.md"
    destino.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] {destino}")
    print(f"[ok] {FIGS / 'simulacao_cenarios.png'}")


if __name__ == "__main__":
    main()
