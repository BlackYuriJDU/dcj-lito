# DCJ - Lito — Projeto de Pesquisa Simulada

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22164910.svg)](https://doi.org/10.5281/zenodo.22164910)

> Simulação de pesquisa sobre **Doença de Creutzfeldt-Jakob esporádica (DCJ)**,
> centrada no caso fictício **"Caso Referência"**, usando apenas dados públicos reais
> e anonimizados que já existem.

## Missão
Obter, administrar, gerir e gerar valor a partir de dados priônicos públicos —
curados e analisados da melhor forma possível — para produzir materiais úteis
a laboratórios reais de pesquisa em príons.

## Mapa do projeto
| Caminho | Conteúdo | Status |
|---|---|---|
| [`MEMORIA.md`](MEMORIA.md) | Diário de sessão — contexto e pendências | vivo |
| `caso_referencia/dossie_clinico.md` | Dossiê clínico simulado (sCJD MM1) validado por fontes | ✅ v0.2 |
| `caso_referencia/linha_do_tempo.csv` · `exames_simulados.csv` · `fontes.md` | Dados estruturados + citações | ✅ |
| `research/estado_da_arte_dcj.md` | Estado da arte 2024–2025 completo com URLs | ✅ |
| `research/datasets_publicos.md` | Catálogo GEO (curadoria direta via E-utilities) | ✅ |
| `research/catalogo_datasets_prionicas_CJD.md` | Catálogo completo verificado: WGS/ENA, GWAS, proteômica PRIDE + o que NÃO existe | ✅ |
| `pipeline/data/GSE160208_series_matrix.txt.gz` | Dataset REAL baixado (47 amostras sCJD/CT, Copenhagen) | ✅ |
| `pipeline/scripts/tavily_search.sh` | Busca padrão via API Tavily | ✅ |
| `pipeline/scripts/analise_caso_referencia.py` → `reports/relatorio_caso_referencia.md` | Validação + critérios CDC/NPDPSC sobre o caso simulado | ✅ |
| `pipeline/scripts/analise_gse160208.py` → `reports/relatorio_gse160208.md` | Análise REAL: covariáveis + Welch/FDR + estratificação MM1 vs. VV2 | ✅ v3 |
| `pipeline/scripts/ponte_caso_referencia.py` → `reports/relatorio_ponte_caso_referencia.md` | Tabela-ponte: cada achado do caso de referência × evidência na coorte real | ✅ |
| `pipeline/scripts/analise_gse140069.py` → `reports/relatorio_gse140069.md` | Cross-modal REAL: miRNA SANGUE (57 sCJD vs. 48 CT) — 84 sig. brutos → 1 após ajuste idade/sexo/RIN; direção ↓ e núcleo nominal preservados | ✅ v3 |
| `pipeline/scripts/gera_figuras.py` → `reports/figuras/` | Volcanos ×2, heatmap top-25, timeline do caso de referência | ✅ 4 figuras |
| `colaboracao/centros_alvo.md` | NPDPSC, UCL, vigilância BR — contatos e estratégia | ✅ |
| `colaboracao/carta_projeto.md` | Carta de apresentação (rascunho — não enviar sem revisão) | ✍️ |
| `memory/` | Aprendizados (decisões, erros, padrões) | vivo |

> **Nota de privacidade (2026-08-29)**: `MEMORIA.md`, `memory/`, `colaboracao/` e
> `ARQUIVO_COMPLETO.md` continuam a existir localmente, mas deixaram de ser
> rastreados neste repo público — a face pública do projeto é o código,
> relatórios, preprint e este README.

## Destaques científicos
- **Tratamento**: frente mais promissora = redução do alvo PrP (ASO ION717, NCT06153966; siRNA Broad, NCT07444580); quinacrina/doxiciclina/pentosano: capítulos encerrados.
- **Dados reais**: GSE160208 confirma neuroinflamação massiva na sCJD (MYD88, TLR2, C1QA, CSF1 com FDR<10⁻⁴).

## Regras invioláveis
1. **Sem pacientes reais ou novos.** Somente datasets públicos, anonimizados.
2. **Honestidade científica**: distinguir evidência estabelecida de experimento preliminar.
3. Tudo documentado em PT-BR, rastreável à fonte original.
