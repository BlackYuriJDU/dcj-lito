# Biomarcadores fluidos na DCJ como endpoints de ensaio — inventário rastreável + lacuna de desenho

*`relatorio_biomarcadores_nfl_tau.md` — 2026-08-29. Primeira passada (P4 do
plano de 29/08): números extraídos de ABSTRACTS verificados via PubMed
(buscador biomcp/PubMed); cada número cita PMID/DOI. Nada foi extraído de
figuras ainda — v2 exige digitalização de suplementos. Objetivo: responder
"qual efeito um fármaco anti-prion precisa produzir em NfL/tau para ser
detectável?" com o que o campo já publicou — e onde está o vazio.*

## 1. Inventário de coortes (todos os números do abstract primário)

| Estudo | PMID | Desenho | n | Matriz | Marcadores | Números-chave (verbatim) |
|---|---|---|---|---|---|---|
| Thompson 2018, JNNP | [29487167](https://pubmed.ncbi.nlm.nih.gov/29487167/) · [PMC6109239](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6109239/) (texto completo lido) | casos×controles + **longitudinal em 6 pacientes (16 amostras, 49–685 dias)** | **45 sCJD / 24 controles** (National Prion Monitoring Cohort, UCL) | **soro** (Simoa) | tau, NfL | NfL: mediana **296.6 (IQR 193–436) vs 14.52 (8.04–20.4) pg/mL**, AUC **1.00** (valida cut-off Steinacker 44.7 com 100%/100%); tau: 6.22 (3.26–19.6) vs 1.56 (1.32–1.97), AUC 0.905; progressão: log-tau **R²=0.552 (p<0.001)** vs log-NfL **R²=0.004 (p=0.77)**; tau ↑ em MM códon 129 (19.6 vs 3.27/4.05 pg/mL); longitudinal: tau e NfL sobem no último ano em 3/6 pacientes |
| Bentivenga 2023, Alzheimers Res Ther | [37684653](https://pubmed.ncbi.nlm.nih.gov/37684653/) | RPD consecutivos, retrospectivo | 220 CJD vs 213 np-RPD | LCR | SNAP-25, Ng, 14-3-3, t-tau, NfL, p-tau181 | SNAP-25 582 (240–1250) vs 115 (78–157) pg/ml; AUC SNAP-25 **0.902** > 14-3-3 0.853 ≈ t-tau 0.878; **NfL AUC 0.649**; Cox: SNAP-25 HR **1.71** (1.40–2.09) |
| Bentivenga 2024, Alzheimers Dement | [39641397](https://pubmed.ncbi.nlm.nih.gov/39641397/) | 4 grupos, transversal | 100 CJD / 100 np-RPD / 92 AD-MCI / 55 HC | LCR + plasma | BD-tau, p-tau217, p-tau181, t-tau, NfL, 14-3-3 | **BD-tau associa com sobrevida (p<0.001), superando t-tau e NfL**; razão plasma BD-tau/p-tau217 ≈ acurácia do 14-3-3 no LCR; p-tau217 LCR ↑ = "tauopatia secundária prião-específica" |
| Chen 2026, CNS Neurosci Ther | [41574640](https://pubmed.ncbi.nlm.nih.gov/41574640/) | prospectivo, inclui **pré-clínicos** | 130 CJD / 145 FTD / 70 HC / **16 portadores PRNP (4–6 anos, 4 conversores)** / 16 controles familiares | plasma (16 proteínas) | NfL, t-tau, GFAP, VCAM-1… | NfL/t-tau/GFAP AUC **>0.93** (vs HC), **>0.82** (vs FTD); portadores pré-sintomáticos estáveis; elevações leves só perto do onset em G114V |
| Shimamura 2024, Biomolecules | [39858404](https://pubmed.ncbi.nlm.nih.gov/39858404/) | transversal + prognóstico | casos Japão + NA/UE (n no texto) | LCR + soro (Ella) | 14-3-3, t-tau, NfL | **NfL NÃO correlaciona com sobrevida** neste estudo (discordância Japão×NA/UE atribuída a política de tratamento e método) |
| Hermann & Zerr 2024, Prion (revisão) | [38734978](https://pubmed.ncbi.nlm.nih.gov/38734978/) | revisão | — | — | panorama | "extremely important in the near future, when new therapeutics are clinically evaluated" — lacuna: biomarcadores que prevejam onset/reflitam progressão |
| Xu 2026, IJMS (revisão) | [41516424](https://pubmed.ncbi.nlm.nih.gov/41516424/) | revisão | — | — | 14-3-3, tau, NfL, pNFH, RT-QuIC |framework em 3 camadas: RT-QuIC confirmatório (>90% sens); tau/NfL/pNFH = severidade de lesão; multi-ômica para detecção precoce |

## 2. O que isso significa para um ensaio PrP-lowering (ION717/PRiSM)

**Papel por função do endpoint** (com base na tabela):

1. **Diagnóstico/estratificação de entrada** — resolvido no plasma: NfL
   (100/100, Thompson), NfL/t-tau/GFAP (>0.93 vs HC, Chen) — perfeito para
   confirmar lesão neuronal ativa no screening.
2. **Farmacodinâmica (o que o fármaco deveria mover)** — NfL é o candidato
   biológico óbvio (lesão axonal). PORÉM: a evidência longitudinal pública
   inteira que encontramos se resume a **"longitudinal sample sets from six
   patients"** (Thompson 2018) + trajetórias qualitativas em portadores
   (Chen 2026). **A variância do slope de NfL em sCJD não está publicada.**
3. **Prognóstico** — heterogêneo: BD-tau > t-tau/NfL (Bentivenga 2024);
   SNAP-25 HR 1.71 (Bentivenga 2023); **NfL falha em sobrevida no Japão**
   (Shimamura 2024) — aviso de heterogeneidade entre plataformas/coortes
   que qualquer readout farmacodinâmico precisa considerar.

**Consequência de desenho (a contribuição desta nota):** o campo tem ensaios
em andamento cujo readout farmacodinâmico depende de um biomarcador cuja
variância longitudinal em sCJD NÃO foi quantificada publicamente em coorte
adequada. Três recomendações rastreáveis:

- **R1**: endpoint primário clínico (sobrevida/MRC scale-slope); NfL como
  secundário/PD — alinhado ao que os protocolos publicados já sinalizam.
- **R2**: quantificar SD do slope de NfL (e BD-tau, que supera NfL em
  prognóstico) em coorte longitudinal ≥50 pacientes — é a lacuna que
  decide o tamanho de efeito detectável; sem ela, MDE é chuto.
- **R3**: antes de comparar NfL entre estudos, checar plataforma (Simoa×
  Ella×automatizado) e matriz — a discordância Shimamura×Thompson é o
  contraexemplo.

## 3. MDE — moldura analítica com dispersão REAL publicada

Dispersão log-NfL estimada do IQR de Thompson (IQR=1.349·σ no log):
σ_log(NfL) ≈ ln(436/193)/1.349 = **0.604** (ln) — aproximação declarada
(IQR-casos); tau: ln(19.6/3.26)/1.349 = 1.33 — a dispersão maior do tau
explica por que o tau correlaciona com taxa e o NfL não (Thompson).

**MDE de mudança entre grupos (α=0.05 bilateral, potência 80%, fator 2.80)**
para um ensaio com braços pareados por baseline, medindo razão de NfL:

MDE = 2.80 · σ_log · √(2/n) por braço, usando σ=0.604:

| n/braço | MDE (ln) | razão detectável |
|---|---|---|
| 25 | 0.479 | **+61%** |
| 50 | 0.339 | **+40%** |
| 100 | 0.239 | **+27%** |

Leitura honesta: isso usa dispersão TRANSVERSAL caso−controle; um endpoint
longitudinal (mudança intra-sujeito) tem dispersão tipicamente MENOR
(tira a variância entre sujeitos) — ou seja, estes n são CONSERVADORES se o
desenho for por mudança-de-baseline. A estimativa definitiva exige o SD de
slope publicado — que não existe na literatura aberta que auditamos (R2).

## 4. Limites honestos

- Todos os números vêm de abstracts PubMed (verificáveis no link); n exatos,
  SDs de slope e ICs completos exigem texto completo/suplemento → v2.
- Não buscamos literaturas não-inglesas nem registros de ensaio internos
  (dados longitudinais NfL do Minikel: mgh_prnp_freeze2 — sob pedido;
  monitorado no protocolo do MEMORIA).
- "Millesi 2024" (Sci Transl Med, NfL longitudinal sCJD) foi identificado
  como alvo da v2 — abstrato não recuperado nesta passada; será baixado e
  dimerizado antes de qualquer citação numérica.

## 5. Fontes

Todas inline na tabela (PMID + DOI). Busca: biomcp/PubMed, termos
NEFL+prion+longitudinal, tau+CSF+trial, longitudinal+doubling+natural
history (29/08/2026).
