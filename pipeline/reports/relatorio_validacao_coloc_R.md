# Validação cruzada do coloc próprio — R (equações exatas + coloc.abf padrão) e LD EUR

*Executado em 2026-08-29 · R 4.5 / coloc 5.2.3 / susieR 0.14.2 (conda-forge, aarch64)
· dados: `pipeline/data/stx6_crosscheck_input.tsv` (390 variantes STX6 harmonizadas,
geradas por `crosscheck_coloc_R.py` a partir do MESMO pipeline validado).*

## (A) Reimplementação exata das equações em R — ACORDO A 6 DECIMAIS

Mesma fórmula (ABF de Wakefield, W = 0.04² = 0.0016) e mesmos priors
(p1 = p2 = 10⁻⁴, p12 = 10⁻⁵; conservador 10⁻⁶/10⁻⁶/10⁻⁷), reimplementados
independentemente em R (`coloc_crosscheck_R.R`):

| Prior | Hipótese | Python (relatório 26/08) | R (29/08) |
|---|---|---|---|
| padrão | H3 | 0.9950 | **0.994997** |
| padrão | H2 | (não exibido antes) | 0.005002 |
| conservador | H3 | 0.6654 | **0.665429** |
| conservador | H2 | (não exibido antes) | 0.334571 |

A máquina (ABF + combinação H0..H4) está correta — duas implementações
independentes das mesmas equações concordam ao limite da precisão exibida.

## (B) coloc.abf padrão do campo (pacote R) — mesma conclusão, split prior-dependente

`coloc.abf` (R coloc 5.2.3) sobre os mesmos 390 pares, com seus próprios
defaults de parametrização: GWAS type="cc" (s = 4110/17679), eQTL-meta
type="quant" com sdY = 1 e N efetivo por variante (inversão de
Var = sdY²/(2Np(1-p)), MAF do GWAS):

- **PP.H4 = 0.9796 · H3 = 0.0204 · H2 = 7×10⁻⁶ · H1 ≈ 0 · H0 ≈ 0**
- **H2+H3+H4 = 1.0000** — a afirmação "ambos os sinais são reais na região"
  vale sob TODAS as parametrizações testadas (nosso padrão: 1.0000;
  nosso conservador: 1.0000; coloc R: 1.0000).
- A divisão H4 (compartilhado) vs H3/H2 (distintas) **depende do prior**:
  com W = 0.04² a massa vai para H3 (99.5%); com o prior mais restrito do
  coloc R vai para H4 (98.0%). Sob r² ≥ 0.97 dentro do cluster, as duas
  configurações são indistinguíveis em verossimilhança — exatamente a
  limitação já declarada no preprint. O reporte combinado é a escolha certa.
- Ranking por-variante: Spearman ρ = **0.914** entre PP.H4 do coloc R e a
  massa diagonal ABF nossa (`stx6_crosscheck_colocR_output.tsv`).

**Correção honesta incorporada**: o relatório anterior dizia
"H0 = H1 = H2 ≈ 0" — impreciso (H2 = 0.005 no padrão e 0.335 no conservador).
H2 NÃO é hipótese nula: é "duas variantes causais distintas". O relatório
`relatorio_coloc_meta_stx6.md` foi regenerado exibindo H2 e o combinado
H2+H3+H4; a afirmação robusta passou a ser essa massa combinada.

## (C) Sensibilidade do fine-mapping ao painel de LD — ALL vs EUR

`finemap_ld.py` re-executado com `LD_POP=1000GENOMES:phase_3:EUR`
(população-matched à coorte UK do GWAS) vs o painel ALL original:

| Locus | Massa no cluster (r²≥0.8) ALL | EUR | Leitura |
|---|---|---|---|
| STX6 (lead rs11586493) | **90.5%** | **90.5%** | idêntico — bloco coeso em ambos |
| PRNP (âncora rs2093390) | 58.9% | **80.9%** | painel EUR marca melhor o bloco do códon 129 |
| GAL3ST1 (âncora rs8142452) | 0.0% (mal marcado) | 0.0% | haplótipo de baixa frequência em ambos |

- λ_GC reproduzido idêntico (1.0587; mediana imune ao bug de contagem
  duplicada nos estratos de MAF — corrigido; λ por estrato inalterado, `n`
  do relatório agora é o real).
- Conclusão: as afirmações de fine-mapping do preprint são robustas à
  escolha do painel; para PRNP o intervalo honesto de massa no cluster é
  59–81% (r²≥0.8) dependendo do painel, 100% em r²≥0.5 nos dois.

## Ferramentas e reprodutibilidade

- R via micromamba (aarch64), env `rcross`: `r-base`, `r-coloc` 5.2.3,
  `r-susier` 0.14.2 (conda-forge)
- `pipeline/scripts/crosscheck_coloc_R.py` → dados de entrada (390 variantes)
- `pipeline/scripts/coloc_crosscheck_R.R` → validações (A) e (B)
- `LD_POP=... python3 pipeline/scripts/finemap_ld.py` → sensibilidade (C)
