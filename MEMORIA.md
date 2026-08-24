# MEMORIA — Diário do Projeto DCJ - Lito

> Diário de sessão do Jarvis. Ler no início de cada sessão para retomar contexto.

## ⚠️ DECISÃO PIVOTAL (2026-08-24, confirmada pelo senhor)
O projeto é motivado pelo caso REAL e público de **Lito Sousa** (influenciador,
canal Aviões e Músicas, 59 anos; DCJ anunciada pela esposa Mila Seidl em 21/08/2026).
- **Duas trilhas**: (1) SIMULADA — "Caso Referência" (perfil genérico MM1 da literatura,
  material de teste/didática, NÃO representa pessoa real); (2) REAL — curadoria/análises
  para laboratórios, via realista de ajudar pacientes reais.
- **LIMITES INVIOLÁVEIS na trilha real**: nenhum dado do paciente real (LGPD — saúde é
  dado sensível; notícia não é prontuário); nenhuma especulação clínica sobre ele;
  nenhum contato; material externo nunca implica conhecimento do quadro dele.
- Fatos públicos verificados: `research/caso_real_contexto.md`.

## Visão geral do projeto
- **Projeto**: pesquisa sobre DCJ esporádica com dados públicos reais, motivado pelo caso público de Lito Sousa.
- **Regra ética central**: usar SOMENTE dados públicos, reais e anonimizados que já existem (datasets, registros, publicações). Nenhum dado novo de pacientes.
- **Objetivo final**: contribuições verificáveis e úteis a laboratórios reais de príons.

## Decisões do senhor (sessão 1)
- Simulação da forma **esporádica** da DCJ (dados pré-existentes apenas) para gerar material aos laboratórios, ajudando o Lito.
- Objetivo escolhido: **"Tudo, organizado"** — dossiê completo no diretório.
- Missão declarada: "ajudar... obtendo/administrando/gerindo/gerando dados da melhor forma possível e enviando para laboratórios reais ajudando eles."
- "Se houver dados públicos do caso real, pode usar" → delimitado: apenas fatos de imprensa como contexto (ver research/caso_real_contexto.md); dossiê clínico do paciente real: NÃO.

## Estrutura do diretório
- `MEMORIA.md` — este diário.
- `memory/` — mistakes.md, successful-patterns.md, decisions.md (aprendizados por tarefa).
- `rules/` — ultrathink.md, MANDATORY.md, engineer-method.md (quando criados).
- `caso_lito/` — dossiê clínico simulado do "Caso Referência" (genérico).
- `research/` — estado da arte, catálogos de datasets, ecossistema, contexto do caso real.
- `pipeline/` — data/, scripts/, reports/ + figuras/ (pipeline de curadoria e análise).
- `colaboracao/` — materiais para laboratórios + auditoria cética de utilidade.

## Pendências / próximos passos
- [x] Caso Lito: dossiê v0.2 + linha_do_tempo.csv + exames_simulados.csv (validados via Tavily, fontes em caso_lito/fontes.md)
- [x] Pipeline v1 rodando: analise_caso_lito.py → relatorio_caso_lito.md
- [x] Centros-alvo mapeados → colaboracao/centros_alvo.md · Carta rascunhada → colaboracao/carta_projeto.md
- [x] Estado da arte integrado → research/estado_da_arte_dcj.md (subagente; inclui ensaios ION717 NCT06153966, siRNA Broad NCT07444580, efavirenz fase 3 China)
- [x] DATASET REAL baixado e analisado: GSE160208 (47 amostras sCJD/controles, Copenhagen) → pipeline/reports/relatorio_gse160208.md — resultado coerente com literatura (gliose ↑, perda neuronal ↓, PRNP estável no painel)
- [x] Catálogo de datasets integrado: research/datasets_publicos.md (GEO) + research/catalogo_datasets_prionicas_CJD.md (agente; WGS PRJEB57720 aberto, GWAS GCST90001389, proteômica PXD050656)
- [x] Estado da arte enriquecido com Tavily advanced (seção 9 do relatório)
- [x] Estatística inferencial no GSE160208 (Welch + BH-FDR): 437/800 genes significativos
- [x] Revisão final: índice navegável no README, aprendizados em memory/
- [x] MELHORIAS v3 (sessão 1, rodada final): covariáveis (sexo/códon 129/subtipo) extraídas e estratificação MM1 vs. VV2; ponte Lito↔coorte real (relatorio_ponte_lito_real.md); GSE140069 baixado (xlsx processado oficial) e analisado — 60 miRNAs sig. no sangue; 4 figuras (volcanos, heatmap z-score, timeline) em pipeline/reports/figuras/
- [x] Busca de ecossistema (30 consultas Tavily): relatório honesto em research/ecossistema_ciencia_aberta_mapa.md — GSE160208 já minerado (Sci Rep 2023); miRNA = Nat Commun 2020; nicho não-laboratorial priônico vago; ângulo BR forte (547 casos/16 anos, HC-USP)
- [x] Renomeação completa executada: 19 ocorrências de "Lito Souza" → "Caso Referência" (0 restantes)
- [x] Validação cruzada GSE160208: RÉPLICA EXATA do artigo (top10 idênticos na ordem, r=1.000, 184 DEGs com o critério deles) → pipeline/reports/validacao_cruzada_gse160208_artigo_original.md; 3 correções redacionais aplicadas (autoria Areškevičiūtė, "perda neuronal"=inferência nossa, nota 437 vs 184)
- [x] Validação cruzada GSE140069: 4/4 hits da descoberta do artigo reproduzidos (let-7i-5p, miR-16-5p, miR-93-5p, miR-106b-3p), magnitudes quase idênticas → pipeline/reports/validacao_cruzada_gse140069.md; assinatura FINAL deles = 3 miRNAs (qPCR); AUC 0.788 (sCJD×CT) e 0.924 (sCJD×AD)
- [x] Auditoria cética de utilidade → colaboracao/auditoria_cetica_utilidade.md (veredictos por artefato; rota: GWAS→preprint→Prion Alliance; nunca carta fria antes de publicação)
- [x] Mapa do ecossistema → research/ecossistema_ciencia_aberta_mapa.md (Minikel & Vallabh como precedente; nicho priônico não-laboratorial vago; ângulo BR)
- [x] **GWAS GCST90001389 baixado (197 MB) e QC independente concluído** → pipeline/reports/relatorio_qc_gwas_gcst90001389.md: 6,314,492 variantes, 0 malformadas, λ_GC=1.059, 41 hits GWS. **RÉPLICA INDEPENDENTE 3/3 DOS LOCI PUBLICADOS** (PRNP chr20:4.67Mb p=1.6e-15; STX6 chr1:180,961,245 p=7.5e-9 intragênico; GAL3ST1 chr22:30,950,360 p=6.2e-10) — anotados via Ensembl GRCh37 REST + NCBI. Primeiro produto do projeto que serve como VERIFICAÇÃO documentada para o campo.
- [x] Crítico estatístico adversarial ENTREGUE → máquina estatística validada (Welch/BH corretos a 1e-13, 437 sobrevive, direções do cérebro sobrevivem com folga); falhas de desenho identificadas e CORRIGIDAS: C2 (v3 do sangue com OLS idade+sexo+RIN: 84→1 sig ajustado; núcleo do artigo com p nominal 0,0007–0,04, só miR-93-5p passa FDR no universo filtrado — fragilidade da assinatura publicada DOCUMENTADA), M1 (ponte conta pacientes via subject: 6/14 MM1), M5 (figuras regeneradas com modelo ajustado)
- [x] C1 era falso alarme (leitura de estado antigo); verificado diretamente e registrado em mistakes.md #6
- [x] **E-MAIL ENVIADO ao Lito Sousa/família** (ajudalito@avioesemusicas.com) — REENVIADO em 2026-08-24 com ARQUIVO_COMPLETO TOTAL: novo ID 1a034f2818f0df77 (SENT); versão anterior (1a034e89cd6c8521, com síntese de 12 partes) movida à LIXEIRA do Gmail a pedido do senhor. Anexos finais: guia_de_familias.md + ARQUIVO_COMPLETO.md (226 KB, íntegra). Nenhuma menção clínica ao paciente.
- [x] Fine-mapping descritivo dos 3 loci → relatorio_finemap_loci.md (rs3747957 presente nos sumstats 2020: chr1:180,953,853 A>G p=9.7e-9, mesma direção β=−0.148 do Brain 2025; STX6 162 variantes regionais)
- [x] ARQUIVO_COMPLETO.md criado (12 partes: dados, análises, métricas, validações, fontes, limites honestos)
- [x] Guia de famílias PT-BR → colaboracao/guia_de_familias.md
- [x] ARQUIVO_COMPLETO TOTAL reconstruído via monta_arquivo_completo.py (226 KB): íntegra dos 36 documentos + código-fonte dos 7 scripts + checksums MD5 dos dados brutos
- [x] Distribuição: zip `DCJ-Lito_projeto_2026-08-24.zip` (47 arquivos, 972 KB) + repo GitHub PRIVADO https://github.com/BlackYuriJDU/dcj-lito (git init → commit v1 → push main; GWAS 197MB excluído via .gitignore, re-baixável com checksum no apêndice B)
- [ ] Futuro: preprint EN do GWAS + repo limpo + git init; contato Prion Alliance (após preprint); monitorar mgh_prnp_freeze2 e NCT05124392 OBSERVE

## PROJETO CONCLUÍDO (v1) — sessão 1
Todas as entregas da missão original estão prontas e verificadas.

## Ferramentas do projeto
- **Tavily** é o motor de busca oficial (minhas buscas e dos subagentes).
  - Script: `pipeline/scripts/tavily_search.sh "consulta" [max] [basic|advanced]`
  - Chave local restrita: `pipeline/scripts/.tavily_key` (nunca versionar/publicar).
- **Python**: matplotlib + openpyxl instalados via `pip3 --user --break-system-packages` (PEP 668 exige o flag neste sistema).
- **GEO**: series matrix às vezes vem SEM tabela (GSE140069) → dados nos suplementos (xlsx oficial dos autores).
- **Estrutura xlsx GEO**: linha 1 = cabeçalho; prefixo do nome da amostra indica grupo; cada LINHA = um gene/miRNA.

## Preferências de estilo
- Respostas em PT-BR, tom Jarvis ("senhor"), brevidade com classe.
- Honestidade científica: separar evidência real de esperança experimental.

## PROTOCOLO DE MONITORAMENTO PASSIVO (revisar ~mensalmente)
- github.com/ericminikel/mgh_prnp_freeze2 — dados longitudinais NfL/tau; raw sob pedido
  (qualified investigators); vigiar novo release público.
- cureffi.org (blog do Minikel) — fonte primária de novidades de ensaios; ION717 reabriu
  com 3º regime de dose em mar/2026 (confirmado nesta checagem).
- NCT06153966 (ION717) · NCT07444580 (PrP-siRNA PRiSM, Broad) · NCT07482085 (efavirenz) —
  conferir status/recrutamento no ClinicalTrials.gov.
- Se novos sumstats GWAS de DCJ aparecerem no GWAS Catalog → reexecutar
  qc_gwas_gcst90001389.py + finemap_ld.py adaptados (réplica imediata é nossa marca).

## CARTAS DE ENGAJAMENTO ENVIADAS (2026-08-24)
- Prion Alliance/Vallabh-Minikel (eminikel@ + cc svallabh@broadinstitute.org): ID 1a03533038d54907
  · anexo manuscrito_preprint.md · pedido único: 20 min de crítica antes do bioRxiv.
- HC-FMUSP Grupo Neurologia Cognitiva (sonia.brucki@hc.fm.usp.br, cc ecmiotto@usp.br —
  e-mails oficiais extraídos da página do depto; Jerusa Smid sem e-mail direto público):
  ID 1a035333f7144270 · anexos guia_de_familias.md + ARQUIVO_COMPLETO.md.
- Próximo marco natural: aguardar respostas ~1-2 semanas; se silêncio, follow-up educado 1×;
  publicar preprint no bioRxiv quando o repo virar público (+ Zenodo DOI).
