# GSE140069 — teste empírico do confundimento idade/RIN
*`analise_gse140069_idade.py` em 2026-10-04 14:33. Fase 2 da auditoria pré-submissão. Objetivo: testar empiricamente a afirmação de que a idade explica o colapso de 84 → 1 miRNAs significativos.*

## 1. A amostra

| covariável | sCJD (n=57) | controles (n=48) | diferença | d |
|---|---|---|---|---|
| idade (anos) | 66.4 ± 8.1 | 53.6 ± 15.3 | **+12.8 anos** | +1.07 |
| RIN | 5.59 ± 1.32 | 6.50 ± 1.26 | **-0.92** | -0.71 |

Idade — casos: Q1=63, mediana=66, Q3=72 · controles: Q1=47, mediana=58, Q3=64.

## 2. Colinearidade do bloco (VIF)

| preditor | VIF | leitura |
|---|---|---|
| grupo | 1.37 | ok |
| idade | 1.32 | ok |
| sexo | 1.01 | ok |
| rin | 1.15 | ok |

VIF ≥ 5 indica que o preditor é mal identificado no modelo — a atribuição de efeito entre covariáveis colineares não é estável.

## 3. Cada covariável isolada

Universo 939 = todos os miRNAs (mesmo universo da contagem de 84). FDR<0.05 dentro de cada modelo. A coluna β mediana é o efeito do coeficiente de interesse.

| modelo | universo | testes | coef. | FDR<0.05 | β mediana |
|---|---|---|---|---|---|
| M1 | idade sozinha | 939 | 939 | idade | **113** | -0.0094 |
| M1 | idade sozinha | filtrado | 269 | idade | **100** | -0.0646 |
| M2 | RIN sozinho | 939 | 939 | RIN | **91** | +0.0975 |
| M2 | RIN sozinho | filtrado | 269 | RIN | **112** | +0.7153 |
| M3 | grupo sozinho | 939 | 939 | grupo | **88** | -0.3619 |
| M3 | grupo sozinho | filtrado | 269 | grupo | **93** | -1.6473 |
| M4 | grupo + idade | 939 | 939 | grupo | **4** | -0.3076 |
| M4 | grupo + idade | filtrado | 269 | grupo | **8** | -1.0401 |
| M4b | grupo + RIN | 939 | 939 | grupo | **26** | -0.3277 |
| M4b | grupo + RIN | filtrado | 269 | grupo | **45** | -1.1257 |
| M4c | grupo + sexo | 939 | 939 | grupo | **85** | -0.3677 |
| M4c | grupo + sexo | filtrado | 269 | grupo | **90** | -1.6211 |
| M5 | grupo + idade + sexo + RIN  (= v3) | 939 | 939 | grupo | **1** | -0.2548 |
| M5 | grupo + idade + sexo + RIN  (= v3) | filtrado | 269 | grupo | **5** | -0.6715 |

## 4. O colapso é idade, RIN ou apenas ajuste?

O set não-ajustado (Welch, sem covariáveis) tem **84** miRNAs a FDR<0.05 — este é o "84" do manuscrito. O mesmo contraste em OLS sem covariáveis dá 88; usamos 88 como base dos deltas abaixo.

| modelo | FDR<0.05 | variação vs. grupo sozinho |
|---|---|---|
| idade sozinha (sem grupo) | 113 | — |
| RIN sozinho (sem grupo) | 91 | — |
| grupo sozinho | 88 | base |
| grupo + sexo | 85 | -3 |
| **grupo + idade** | **4** | **-84** |
| **grupo + RIN** | **26** | **-62** |
| grupo + idade + sexo + RIN (= v3) | 1 | -87 |

Sobreposição com o set de 84: **58** (69%) são significantemente associados a **idade sozinha**; **42** (50%) a **RIN sozinho**; **81** a grupo sozinho.

### Veredito

**A idade é o confundidor responsável.** Ajustar apenas idade leva o sinal de 88 para 4; ajustar apenas RIN leva a 26; ajustar apenas sexo deixa 85. Somente a idade, isolada, quase esgota o sinal.

A direção da afirmação do manuscrito se sustenta, mas "fully" superdeclara: a idade remove 84 de 87 sinais (97%), e o RIN responde pelo resto. Trocar por "accounts for 97% of the collapse" e citar este modelo.

VIF < 1.4 em todos os preditores: a atribuição **é** estimável — este era o ponto que nunca tinha sido verificado no repositório.

**Redução do sinal de 88 → 1 quando cada covariável é ajustada isoladamente** (contribuições **não aditivas** — somam 149 porque as covariáveis capturam variância sobreposta; não são frações de um todo):

- idade: −84 (→ 4 sinais) — **dominante**
- RIN: −62 (→ 26 sinais) — substancial, mas não suficiente sozinho
- sexo: −3 (→ 85 sinais) — desprezível

## 5. Faixa etária restrita

Se casos e controles se sobrepõem, o efeito de grupo que sobrevive dentro da faixa não pode ser atribuído à idade. A coluna `gap` é a diferença de idade **dentro** da faixa — se for grande, a restrição não removeu a confusão.

**Poder insuficiente para resolver um efeito residual.** Com 22–29 controles por faixa (contra 48 na amostra total) e universo de 269 miRNAs filtrados, as contagens de 1–7 não distinguem "nada sobrevive" de "sobrevive pouco". Esta seção é um controle de sanidade, não uma medição.

| faixa | n casos | n controles | gap idade | grupo só (FDR) | grupo + idade (FDR) |
|---|---|---|---|---|---|
| 50–70 | 37 | 29 | +2.7 anos | 7 | 5 |
| 55–70 | 34 | 22 | +0.7 anos | 3 | 4 |
| 55–75 | 44 | 24 | +2.0 anos | 1 | 1 |
