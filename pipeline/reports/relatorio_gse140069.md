# Relatório — GSE140069 (SANGUE) — v3 com ajuste de idade/sexo/RIN
*`analise_gse140069.py` v3 em 2026-08-29 09:40. Correções da auditoria adversarial C2/M3/M4.*

- Amostras: 57 sCJD vs. 48 controles · miRNAs: 939
- Covariáveis do series matrix: idade (casos ~66 vs. controles ~54 anos — confusão grave), sexo, RIN
- Amostras com idade+RIN completos (usadas no modelo ajustado): 105 (0 excluídas)
- Filtro de detecção (≥25% das amostras acima do piso): **269 de 939** miRNAs testáveis

## A vs. B — o número honesto

| Análise | miRNAs significativos (FDR<0.05) | Interpretação |
|---|---|---|
| A: Welch log2(x+1), SEM covariáveis | 84 (10↑/74↓) | triagem não-ajustada — INFLADA pela idade/RIN |
| A′: A ∩ filtro de detecção | 69 | triagem em miRNAs bem medidos |
| B: OLS ajustado (idade+sexo+RIN) | **1** (0↑/1↓) | **o número que vale** |
| A ∩ B | 1 | núcleo robusto às covariáveis |
| B no universo filtrado (n=269, espelha o artigo) | **5** | sensibilidade com correção menor |

**Veredicto (auditoria C2 confirmada): o '60' da v1/v2 não sobrevive ao ajuste — a maior parte do sinal bruto era confundimento por idade/RIN.**
O que sobrevive é a assinatura DIRECIONAL (down-dominante) e o núcleo do artigo
em significância NOMINAL (não em FDR) — ver tabela abaixo.

## Núcleo da assinatura do artigo original (Nat Commun 2020)

| miRNA | p nominal (ajustado) | q A (939 testes) | q B (939) | q B (universo filtrado) |
|---|---|---|---|---|
| hsa-miR-16-5p | 0.0060 | 4.17e-04 | 1.71e-01 | 1.46e-01 |
| hsa-miR-93-5p | 0.0007 | 5.29e-04 | 1.40e-01 | 4.80e-02 |
| hsa-let-7i-5p | 0.0404 | 1.26e-03 | 2.60e-01 | 2.47e-01 |
| hsa-miR-106b-3p | 0.0079 | 1.01e-03 | 1.71e-01 | 1.46e-01 |

**Leitura**: todos os 4 mantêm direção ↓ e p nominal significativo; após FDR,
apenas miR-93-5p sobrevive no universo filtrado (q=0.048). A assinatura publicada
é mais FRÁGIL sob ajuste padrão do que a apresentação original sugere — diferenças
plausíveis: Partek GSA (correção de variância gene-específica) vs. OLS comum, e
universo de testes (101 deles vs. 269/939 nossos). Esta fragilidade documentada é
em si uma contribuição de verificação independente.

## Top 15 do modelo ajustado (B) — com tamanho de efeito (Cohen's d)

| miRNA | β grupo (log2) | p | q(FDR) | d |
|---|---|---|---|---|
| hsa-miR-500a-3p | -7.94 | 8.03e-06 | 7.54e-03 | -1.20 |

## Nota de honestidade científica
- v1 (linear) e v2 (log2 sem covariáveis) estão documentadas no histórico; esta v3 é a análise definitiva.
- O artigo original usou Partek GSA com idade como covariável sobre 101 miRNAs filtrados;
  nós rodamos os 939 (triagem) + filtro de detecção — universos diferentes, declarados.
- Nossa lista ajustada NÃO é 'assinatura': assinatura validada do artigo = 3 miRNAs com qPCR.
- Sexo codificado M=1; RIN como qualidade de RNA; modelo linear padrão, sem interações.