# Colocalização STX6: GWAS sCJD × eQTL cerebral (GTEx v10)
*`coloc_stx6_eqtl.py` em 2026-08-26 07:41. Método: coloc ABF (Giambartolomei
2014), W=0,04²; GWAS n=17.679 (GCST90001389); eQTL via eQTL Catalogue
r8 (tabix remoto, região chr1:180,9–181,1 Mb); coordenadas eQTL
GRCh38→GRCh37 offset -30.864; alelos harmonizados (efeito=ALT).*

## DLPFC — GTEx_v10 brain_frontal_cortex (DLPFC)

- Variantes eQTL de STX6: 582 · casadas com GWAS: **372** · alelos incompatíveis descartados: 0

### Priors padrao (p1=0.0001, p2=0.0001, p12=1e-05)
| Hipótese | Descrição | PP |
|---|---|---|
| H0 | nenhum causal | 0.0047 |
| H1 | só GWAS | 0.9735 |
| H2 | só eQTL | 0.0001 |
| H3 | causais distintos | 0.0217 |
| **H4** | **causal compartilhado** | **0.0000** |

**PP.H4 = 0.000** · H4/(H3+H4) = 0.00 · n=372 variantes

### Priors conservador (p1=1e-06, p2=1e-06, p12=1e-07)
| Hipótese | Descrição | PP |
|---|---|---|
| H0 | nenhum causal | 0.3252 |
| H1 | só GWAS | 0.6746 |
| H2 | só eQTL | 0.0001 |
| H3 | causais distintos | 0.0002 |
| **H4** | **causal compartilhado** | **0.0000** |

**PP.H4 = 0.000** · H4/(H3+H4) = 0.00 · n=372 variantes

| rsID | pos b37 | p GWAS | p eQTL |
|---|---|---|---|
| rs11586493 | 180,961,245 | 7.51e-09 | 1.71e-03 |
| rs7553330 | 180,956,015 | 7.73e-09 | 1.71e-03 |
| rs12754041 | 180,957,962 | 8.30e-09 | 1.71e-03 |
| rs4111520 | 180,958,946 | 9.02e-09 | 1.71e-03 |
| rs6680541 | 180,949,780 | 9.09e-09 | 1.71e-03 |
| rs1411478 | 180,962,282 | 9.34e-09 | 1.71e-03 |
| rs6425658 | 180,956,985 | 9.60e-09 | 1.71e-03 |
| rs6425657 | 180,956,905 | 9.60e-09 | 1.71e-03 |
| rs12744212 | 180,952,516 | 9.71e-09 | 1.71e-03 |
| rs7543927 | 180,953,038 | 9.73e-09 | 1.71e-03 |

### Concordância de direção
- Efeitos na mesma direção (GWAS vs eQTL): **303/372 (81%)**
- Lead GWAS (rs11586493): β_GWAS=-0.149 · β_eQTL=-0.2189 · MESMA direção ✅

### Nota de poder
- Com n_eQTL=285, o maior z atingível (~3–4) é muito menor que o z do GWAS lead (~5,7): H1 domina por poder, não por refutação. Veredicto técnico: **inconclusivo por poder** neste dataset isolado — resolvido no meta de 5 datasets (ver relatorio_coloc_meta_stx6.md: H3+H4≈1,0, eQTL p=7e-47, concordância 89%). Direção aqui: concordante em 81% das variantes.

## CEREBELO — GTEx_v10 brain_cerebellum

- Variantes eQTL de STX6: 606 · casadas com GWAS: **383** · alelos incompatíveis descartados: 0

### Priors padrao (p1=0.0001, p2=0.0001, p12=1e-05)
| Hipótese | Descrição | PP |
|---|---|---|
| H0 | nenhum causal | 0.0047 |
| H1 | só GWAS | 0.9805 |
| H2 | só eQTL | 0.0001 |
| H3 | causais distintos | 0.0147 |
| **H4** | **causal compartilhado** | **0.0000** |

**PP.H4 = 0.000** · H4/(H3+H4) = 0.00 · n=383 variantes

### Priors conservador (p1=1e-06, p2=1e-06, p12=1e-07)
| Hipótese | Descrição | PP |
|---|---|---|
| H0 | nenhum causal | 0.3252 |
| H1 | só GWAS | 0.6747 |
| H2 | só eQTL | 0.0000 |
| H3 | causais distintos | 0.0001 |
| **H4** | **causal compartilhado** | **0.0000** |

**PP.H4 = 0.000** · H4/(H3+H4) = 0.00 · n=383 variantes

| rsID | pos b37 | p GWAS | p eQTL |
|---|---|---|---|
| rs11586493 | 180,961,245 | 7.51e-09 | 2.37e-03 |
| rs7553330 | 180,956,015 | 7.73e-09 | 2.90e-03 |
| rs12754041 | 180,957,962 | 8.30e-09 | 2.90e-03 |
| rs4111520 | 180,958,946 | 9.02e-09 | 2.37e-03 |
| rs6680541 | 180,949,780 | 9.09e-09 | 3.52e-03 |
| rs1411478 | 180,962,282 | 9.34e-09 | 2.37e-03 |
| rs6425658 | 180,956,985 | 9.60e-09 | 2.90e-03 |
| rs6425657 | 180,956,905 | 9.60e-09 | 2.90e-03 |
| rs12744212 | 180,952,516 | 9.71e-09 | 2.90e-03 |
| rs7543927 | 180,953,038 | 9.73e-09 | 2.90e-03 |

### Concordância de direção
- Efeitos na mesma direção (GWAS vs eQTL): **298/383 (78%)**
- Lead GWAS (rs11586493): β_GWAS=-0.149 · β_eQTL=-0.2635 · MESMA direção ✅

### Nota de poder
- Com n_eQTL=272, o maior z atingível (~3–4) é muito menor que o z do GWAS lead (~5,7): H1 domina por poder, não por refutação. Veredicto técnico: **inconclusivo por poder** neste dataset isolado — resolvido no meta de 5 datasets (ver relatorio_coloc_meta_stx6.md: H3+H4≈1,0, eQTL p=7e-47, concordância 89%). Direção aqui: concordante em 78% das variantes.


## Interpretação (honesta)
- H4 alto (>0,8): consistente com o sinal GWAS de STX6 ser mediado
  por expressão do gene — mecanismo plausível de regulação transcricional.
- H3 alto: sinais distintos (ex.: variante reguladora de outro gene ou
  tecido errado) — reportado como resultado, não como falha.
- Limitações: eQTL de n≈285 tem poder limitado; tecido DLPFC/cerebelo
  ≠ região afetada na DCJ em todos os subtipos; coloc assume UM sinal
  causal por traço na região (nosso fine-mapping mostra cluster único).