# Colocalização GWAS sCJD × sQTL (SPLICING) — região STX6
*`coloc_sqtl_stx6.py` em 2026-08-29 16:17. eQTL Catalogue r8 leafcutter, mesmos 5 cohorts do meta-eQTL. Arquivos cc = pares cis SIGNIFICATIVOS por cluster; ausência do STX6 no cc = sem sQTL significativo detectado. Coloc ABF por cohort×cluster (equações validadas em R, relatorio_validacao_coloc_R.md).*

| Cohort sQTL | n | clusters sig. na janela | clusters do STX6 |
|---|---|---|---|
| CommonMind DLPFC | 586 | 1 | **0** |
| ROSMAP DLPFC | 560 | 1 | **0** |
| BrainSeq DLPFC | 479 | 2 | **0** |
| GTEx_v10 DLPFC | 285 | 0 | **0** |
| GTEx_v10 cerebelo | 272 | 2 | **0** |

Testes coloc executados (clusters sig. × cohorts, ≥20 pares): **6** · Bonferroni: limiar H4 nominal para 'H4>0.5 interessante' = 0.5/6 = 8.33e-02

| cohort | gene | cluster | pares | PP.H4 | PP.H3 | PP.H2 | H2+H3+H4 (conserv.) | conc. direção | p mín sQTL |
|---|---|---|---|---|---|---|---|---|---|
| CommonMind DLPFC | ENSG00000135835 | 1:180936513:180938555:clu_46 | 388 | 0.000 | 0.025 | 0.000 | 0.000 | 35% | 7.3e-06 |
| GTEx_v10 cerebelo | ENSG00000135835 | 1:180936513:180938555:clu_51 | 383 | 0.000 | 0.016 | 0.000 | 0.000 | 21% | 1.6e-07 |
| BrainSeq DLPFC | ENSG00000135835 | 1:180936513:180938555:clu_51 | 375 | 0.000 | 0.020 | 0.000 | 0.000 | 32% | 7.3e-06 |
| BrainSeq DLPFC | ENSG00000116260 | 1:180175366:180178794:clu_51 | 375 | 0.000 | 0.015 | 0.000 | 0.000 | 48% | 6.4e-03 |
| ROSMAP DLPFC | ENSG00000135835 | 1:180936513:180938555:clu_10 | 365 | 0.000 | 0.125 | 0.001 | 0.001 | 62% | 3.8e-09 |
| GTEx_v10 cerebelo | ENSG00000230124 | 1:180270423:180273338:clu_10 | 383 | 0.000 | 0.012 | 0.000 | 0.000 | 48% | 2.9e-03 |

## Leitura honesta
- **0 clusters sQTL do próprio STX6 em todo o conjunto** (0 em todos os 5 cohorts): não há sQTL significativo detectado para o STX6 em nenhum cohort — ao contrário do eQTL de expressão, que é forte (p=7×10⁻⁴⁷ no meta).
- 6 testes de coloc em clusters dos genes vizinhos (KIAA1614 etc.); PP.H4 > 0.5 em 0 deles (com 6 testes, interprete com Bonferroni).
- Conclusão: o sinal GWAS de STX6 é associado a EXPRESSÃO do gene sem componente de SPLICING detectável nos mesmos cohorts — refina a interpretação 'expression-mediated' do preprint.
- Limitações: cc = pares significativos (sQTL não-significativos não são testáveis); clusters de splicing têm menos variantes e menos poder que eQTL de expressão; ausência de evidência ≠ evidência de ausência.
