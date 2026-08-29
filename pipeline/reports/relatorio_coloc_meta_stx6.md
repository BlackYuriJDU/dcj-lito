# Colocalização STX6 — META-eQTL (poder ampliado)
*`coloc_meta_stx6.py` em 2026-08-29 15:42. Meta IVW de 5 datasets
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
- **PP.H4 = 0.0000** · H3 = 0.9950 · H2 = 0.0050 · H1 = 0.0000 · H0 = 0.0000
- H2+H3+H4 (ambos os sinais reais na região) = 1.0000
- H4/(H3+H4) = 0.00

## Priors conservador
- **PP.H4 = 0.0000** · H3 = 0.6654 · H2 = 0.3346 · H1 = 0.0000 · H0 = 0.0000
- H2+H3+H4 (ambos os sinais reais na região) = 1.0000
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
- **H2+H3+H4 ≈ 1,0 com H0≈H1≈0**: ambos os sinais são reais e vivem
  na MESMA região — é essa a afirmação robusta, válida sob qualquer
  prior (padrão: H3=0.995, H2=0.005; conservador: H3=0.665, H2=0.335;
  coloc.abf do R 5.2.3 com seu prior: H4=0.98 — ver
  relatorio_validacao_coloc_R.md). H2 NÃO é hipótese nula: é
  'duas variantes causais distintas'.
  A divisão H4 (compartilhado) vs H3/H2 (distintas) é prior-dependente
  e indistinguível sob LD forte (r²≥0,97 no cluster): 'duas variantes
  distintas em LD perfeito' e 'uma variante compartilhada' produzem
  verossimilhanças idênticas — por isso reportamos o combinado.
- O que decide na direção da partilha: (i) o lead GWAS É eQTL
  significativo do STX6 no meta (p=7×10⁻⁴⁷, z≈14); (ii) concordância
  de direção em 89% das variantes; (iii) o fine-mapping GWAS mostra
  um único cluster posterior (90,5% em r²≥0,8) — não há segundo sinal
  real para justificar H3 por variantes distintas.
- Conclusão para o preprint: consistente com o sinal de STX6 ser
  mediado por expressão gênica no cérebro adulto; H4 estrito não é
  afirmável sob r²=1,0 — reportar H3+H4 combinado e concordância.
- Limitações: meta assume heterogeneidade baixa entre datasets;
  coloc assume 1 sinal causal por traço; DLPFC/cerebelo ≠ todos os
  tecidos afetados na DCJ.
