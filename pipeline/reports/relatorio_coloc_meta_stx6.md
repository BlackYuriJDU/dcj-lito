# Colocalização STX6 — META-eQTL (poder ampliado)
*`coloc_meta_stx6.py` em 2026-08-26 07:40. Meta IVW de 5 datasets
cerebrais (eQTL Catalogue r8, tabix remoto) vs GWAS sCJD.*

| Dataset | n | pares STX6 |
|---|---|---|
| CommonMind DLPFC | 586 | 887 |
| ROSMAP DLPFC | 560 | 711 |
| BrainSeq DLPFC | 479 | 1167 |
| GTEx_v10 DLPFC | 285 | 582 |
| GTEx_v10 cerebelo | 272 | 606 |

Posições na meta (≥3 datasets): **651** · casadas com GWAS: **390**

## Priors padrao
- **PP.H4 = 0.0000** · H3 = 0.9950 · H1 = 0.0000 · H0 = 0.0000
- H4/(H3+H4) = 0.00

## Priors conservador
- **PP.H4 = 0.0000** · H3 = 0.6654 · H1 = 0.0000 · H0 = 0.0000
- H4/(H3+H4) = 0.00

## Direção
- Mesma direção GWAS×eQTL-meta: **348/390 (89%)**

| pos b37 | p GWAS | p eQTL-meta |
|---|---|---|
| 180,961,245 | 7.51e-09 | 7.60e-47 |
| 180,956,015 | 7.73e-09 | 6.93e-47 |
| 180,957,962 | 8.30e-09 | 8.94e-47 |
| 180,958,946 | 9.02e-09 | 6.82e-47 |
| 180,949,780 | 9.09e-09 | 6.60e-47 |
| 180,962,282 | 9.34e-09 | 1.10e-46 |
| 180,956,985 | 9.60e-09 | 5.79e-47 |
| 180,956,905 | 9.60e-09 | 6.75e-47 |
| 180,952,516 | 9.71e-09 | 6.17e-47 |
| 180,953,038 | 9.73e-09 | 6.86e-47 |

## Interpretação honesta
- Com ~2.182 amostras cerebrais no meta, o eQTL ganha ~1,6× o z do
  maior dataset individual. Se H4 seguir baixo mesmo assim, o sinal
  GWAS de STX6 provavelmente NÃO é mediação simples de expressão em
  tecido adulto — hipótese alternativa: efeito em desenvolvimento,
  splicing (sQTL), ou célula-específico (microglia). Reportar como
  achado, não como falha.
- Limitações: meta assume heterogeneidade baixa entre datasets;
  coloc assume 1 sinal causal por traço.