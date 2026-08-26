# Ponte cérebro × sangue: alvos de miRNAs sanguíneos nos DEGs cerebrais
*`analise_integrada_cerebro_sangue.py` em 2026-08-26 08:54. Análise NOVA —
nenhum dos artigos originais fez a integração.*

**Desenho**: miRNAs ↓ no sangue de sCJD (GSE140069) → alvos validados
(miRTarBase 10.0, evidência forte, humano) → sobre-representação entre
genes ↑ no córtex frontal sCJD (GSE160208, FDR<0.05). Hipergeométrico,
universo = painel NanoString (N=800).

DEGs cerebrais recomputados: 314 up · 123 down.

| miRNA (sangue) | Alvos validados (Strong) | ∩ DEGs ↑ | Esperado | p (hipergeom.) |
|---|---|---|---|---|
| hsa-miR-16-5p | 48 | 6 | 18.8 | 1.00e+00 |
| hsa-miR-93-5p | 16 | 3 | 6.3 | 9.80e-01 |
| hsa-let-7i-5p | 11 | 1 | 4.3 | 9.96e-01 |
| hsa-miR-106b-3p | 0 | 0 | 0.0 | 1.00e+00 |
| hsa-miR-500a-3p | 0 | 0 | 0.0 | 1.00e+00 |

| miRNA | q (BH, 5 testes) |
|---|---|
| hsa-miR-16-5p | 1.000 |
| hsa-miR-93-5p | 1.000 |
| hsa-let-7i-5p | 1.000 |
| hsa-miR-106b-3p | 1.000 |
| hsa-miR-500a-3p | 1.000 |

## Leitura honesta
- Sobre-representação significativa = consistente com eixo miRNA→alvo
  compartilhado sangue-cérebro (biomarcador mecanístico, não só
  marcador passivo de dano).
- NÃO significativo = os miRNAs sanguíneos provavelmente refletem
  processos periféricos (imunidade) distintos da transcrição cerebral —
  também é achado: desmonta inferência causal ingênua sangue→cérebro.
- Viés declarado: o painel NanoString (800 genes) é focado em
  neuroinflamação — enriquece DEGs de vias imunes, o que pode inflar
  o overlap com alvos de miRNAs imunes. Universo honesto declarado.
- miRNAs ↓ no sangue com alvos ↑ no cérebro é a direção testada;
  direção oposta (alvos ↓) testada como controle negativo.

### Controle negativo — alvos ∩ DEGs ↓ (deveria ser ~nulo)

| miRNA | ∩ DEGs ↓ |
|---|---|
| hsa-miR-16-5p | 1 |
| hsa-miR-93-5p | 1 |
| hsa-let-7i-5p | 1 |
| hsa-miR-106b-3p | 0 |
| hsa-miR-500a-3p | 0 |