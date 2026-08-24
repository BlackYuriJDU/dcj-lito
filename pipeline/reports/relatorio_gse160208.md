# Relatório — Análise de dados REAIS: GSE160208
*Gerado por `analise_gse160208.py` em 2026-08-24 12:52.*

- Dataset: Gene expression in the brain of sporadic Creutzfeldt-Jakob disease patients (CJD), and normal controls (CT)
- Fonte: GEO/NCBI GSE160208 · PMID 33375642 · Univ. Copenhagen (dados públicos anonimizados) · Areškevičiūtė A., Litman T. et al. (1ª autora: Areškevičiūtė)
- Amostras totais processadas: **47** · Genes no painel: **800**

## Composição das amostras
- CJD_CB: 13
- CJD_FC: 14
- CT_CB: 10
- CT_FC: 10

## Covariáveis disponíveis (metadados reais)

- gender: F: 23, M: 24
- codon 129: MM: 22, MV: 14, VV: 11
- cjd subtype: MM1: 12, MM1+2: 2, MV1: 4, MV2: 2, NA: 20, VV2: 7

## Estratificação por subtipo — córtex frontal CJD
- Grupos CJD-FC por subtipo: MM1: 6, MM1+2: 1, MV1: 2, MV2: 1, VV2: 4

> **Nota**: estratificação por subtipo é EXTENSÃO EXPLORATÓRIA NOSSA (n=6 no MM1-FC);
> o artigo original não a realiza. Coerente com Llorens et al., citado na discussão deles.
> Descriativa, não inferencial (n pequeno).

### Subgrupo MM1 (n=6) vs. controles — top 5 up/down

| Gene | Δ(MM1−CT) |
|---|---|
| SERPINA3 | +5.18 |
| SOCS3 | +3.75 |
| CD44 | +3.66 |
| FCER1G | +3.48 |
| MSR1 | +3.46 |
| SLC17A6 | -3.08 |
| KIT | -2.72 |
| NEFL | -2.55 |
| BDNF | -2.03 |
| TPD52 | -2.00 |

## Top 10 genes MAIS expressos em CJD (córtex frontal)

| Gene | Média CJD | Média CT | Δ |
|---|---|---|---|
| SERPINA3 | 10.4 | 5.6 | +4.8 |
| CD44 | 9.0 | 5.7 | +3.2 |
| SOCS3 | 8.1 | 4.9 | +3.2 |
| SPP1 | 12.0 | 9.3 | +2.8 |
| MSR1 | 8.0 | 5.3 | +2.7 |
| FCER1G | 8.5 | 5.8 | +2.7 |
| TLR2 | 7.6 | 5.0 | +2.6 |
| EMP1 | 9.0 | 6.5 | +2.6 |
| C1QA | 8.1 | 5.6 | +2.6 |
| GFAP | 16.6 | 14.1 | +2.5 |

## Top 10 genes MENOS expressos em CJD (córtex frontal)

| Gene | Média CJD | Média CT | Δ |
|---|---|---|---|
| SLC17A6 | 5.5 | 8.4 | -2.9 |
| KIT | 5.6 | 8.1 | -2.5 |
| NEFL | 11.1 | 13.3 | -2.2 |
| RELN | 7.5 | 9.4 | -1.9 |
| TUBB3 | 5.5 | 7.3 | -1.8 |
| BDNF | 5.4 | 7.2 | -1.7 |
| HPRT1 | 10.0 | 11.6 | -1.6 |
| PNOC | 5.4 | 7.1 | -1.6 |
| TPD52 | 8.8 | 10.4 | -1.6 |
| GRIN2B | 8.8 | 10.2 | -1.5 |

## Verificação específica
- PRNP presente no painel: sim → Δ(CJD−CT) = -0.42

## Estatística inferencial (Welch + BH-FDR, córtex frontal)
- Genes testados: 800 · Significativos com FDR<0.05: **437**

> **Reconciliação com o artigo original** (validação cruzada de 2026-08-24, ver
> `validacao_cruzada_gse160208_artigo_original.md`): os autores reportam **184 DEGs**
> porque aplicam filtro adicional de magnitude (|log2FC| > 1) e limiar de FDR mais
> frouxo (q≈0.06). Aplicando o critério EXATO deles aos nossos dados: **184 DEGs —
> número idêntico ao publicado** (única divergência: CCL4, caso-limite na borda do corte).
> Nossos 437 incluem modulações finas (|Δ| ≤ 1) que o filtro de magnitude deles exclui.
> Top 10 up/down nossos = top 10 deles, NA MESMA ORDEM; correlação de magnitudes r = 1.000.

## Nota de honestidade científica
- Welch t-test bicaudal implementado em stdlib; FDR Benjamini–Hochberg.
- Painel dirigido (800 genes neuroinflamatórios), não transcriptoma total.
- Sem correção para covariáveis (idade, PMI) — os metadados brutos não as trazem.
- **"Perda neuronal" é INFERÊNCIA NOSSA** (apoiada nos genes down neurônio-específicos
  SLC17A6/NEFL/BDNF/TUBB3/GRIN2B), não conclusão do artigo original — que foca em
  regionalidade, microglia e células dendríticas. Ler como "padrão consistente com
  disfunção neuronal", não como demonstração histológica.