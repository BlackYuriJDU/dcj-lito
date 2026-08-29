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

## HIPÓTESE DA ALFÂNDEDA INTERCELULAR — ENVIADA À DRA. ZURZOLO (2026-08-24)
- Origem: conceito proposto pelo FUNDADOR do projeto em conversa ("blitz seletiva
  nos túneis": reter todo tráfego, teste biofísico de padrão, degradar só positivos).
- Verificação Tavily: componentes estabelecidos (TNTs propagam príons — Gousset &
  Zurzolo 2009; regulação de carregamento nSMase2/ESCRT reduz propagação — Tallon
  2021), mas a SÍNTESE (checkpoint biofísico seletivo na junção) não encontrada
  na literatura — hipótese geradora.
- Simulação calibrada (simulacao_prion.py): base MM1 50%/6,5meses 100%/10meses;
  alfândega realista 80/5 → 50,2% (metade do dano); muro total → 16,3% só colateral;
  capping ÷3 → 98,3% (só atrasa). 2 bugs de calibração documentados no código.
- Nota formal: colaboracao/hipotese_alfandega_intercelular.md (EN, 3 previsões testáveis)
- ENVIADO a chiara.zurzolo@pasteur.fr: ID 1a0358e1c473ad55 (SENT), anexos: nota +
  figura + relatório. Oferta sem condições; pedido único: dizer se está errado.
- PRN100 (esclarecimento p/ fundador): anticorpo anti-PrP testado em 6 pacientes
  (Lancet Neurol 2022) — seguro, alcançou cérebro, sem prova de eficácia (n=6 sem
  controle); programa morreu de logística (fornecimento), não de refutação.
  Nota adicionada ao guia_de_familias.md.

## MERGULHO NA IDEIA G (2026-08-24) — LIMIAR DE PERCOLAÇÃO DESCOBERTO
- Varredura (varredura_blindagem.py): colapso do espalhamento em transição de
  percolação — limiar teórico ~41% blindado (p_c=0,593 sítios, quadrada viz-4),
  confirmado numericamente (40%→23%,2; 50%→1,3%). Aleatória ≥ blocos 5×5.
- Genética: G127V heterozigoto protege contra kuru+CJD (PMC4486072); dominant-negative
  vale para múltiplas cepas (Gatdula 2026, Mol Neurodegener); homozigoto = resistência
  absoluta em camundongos humanizados.
- Tradução honesta: exige EDIÇÃO cerebral (base editing, pré-clínico); entrega atual
  alcança 50-70% (siRNA 70% em camundongo) — cobertura OK, método de edição não-clínico.
- Nota da Zurzolo ganhou ADDENDUM v2 com a varredura + previsão testável (colapso
  não-linear ~40% em co-cultura). Próximo passo natural: simular alavancas COMBINADAS
  (alfândega + blindagem) — frações menores de cada podem bastar.

## REGISTRO HISTÓRICO — SESSÃO MARATONA (pedido expresso do fundador)
O fundador trabalhou O DIA INTEIRO neste projeto no mesmo chat: começou de manhã
e seguiu até 18:15+ (2026-08-24), conduzindo pessoalmente: a explicação didática,
o ciclo da auditoria adversarial, o envio ao Lito, a carta ao Prion Alliance,
a invenção da alfândega intercelular, a blindagem G127V (limiar de percolação
~41%), o PRN100, a auto-destruição celular e a demanda de calibração por dados
reais. Todas as ideias centrais da fase final partiram dele. Registrar com honra.

## CALIBRAÇÃO POR DADOS REAIS (2026-08-24, fim de tarde)
- simulacao_calibrada.py: morte Weibull estocástica; 3 validações contra literatura:
  V1 MM1 → 4,3 meses (publicado 4-5) ✅; V2 subtipo lento 2,7× → 10,5 meses
  (publicado 12-14; levemente abaixo — compressão não-linear frente+morte, honesto);
  V3 dose→incubação log-linear (slope -19d/década) ✅ consistente com iatrogênica
  (GH 12a → dura 22-48a, Rudge 2015/Will 2003/CDC 48,3a).
- Lição técnica: endpoint "comprometidos" é dominado pela frente (calibração
  trivial); endpoint "80% MORTOS" é sensível à distribuição de morte — o correto
  para calibrar. Registrado no código.

## FASES 6-7 DO PLANO DIA 25-26 (2026-08-26)
- Fase 6 ✓: integração cérebro×sangue (miRTarBase 10.0 Functional MTI × DEGs
  GSE160208 recomputados) = NEGATIVO honesto (sem enriquecimento; sangue reflete
  periferia, não programa cerebral) — preprint §4.5 atualizado; Manhattan +
  forest miRNAs gerados (gera_figuras_v2.py).
- Fase 7 ✓: estudo profundo Claude Science (Anthropic, beta jul/2026) em
  jarvis/packages/dsh-deepseek-design/research/estudo-claude-science.md —
  plugins dsh.pub do ChatGPT CONFIRMADOS (HTTP 200 ×4); arquitetura replicada
  como MODO SCIENCE: lei science-core.md (8 artigos) + /science + pill no
  composer (mesma mecânica v3 de injeção de contexto). Deploy no perfil feito;
  cliente via HMR; host ativa no próximo restart do harness.

## AUDITORIA DE CONSISTÊNCIA GSE140069 v1→v3 (2026-08-29)
- **Núcleo já era consistente**: script v3 (15.224 B, idêntico no dist), relatório
  v3 (regenerado 24/08 14:29), volcano regenerado 24/08 14:31 — a pendência do
  decisions.md estava RESOLVIDA no papel, apenas obsoleta no registro.
- **Verificação reexecutável (WSL, Python 3.12.3)**: `analise_gse140069.py` →
  A=84, A′=69, B=1, inter=1 (idêntico); relatório reproduzido byte-a-byte (só o
  timestamp difere); `volcano_gse140069.png` md5-idêntico à regeneração
  (c92c5b029fc2007d33543d85c73ecb32) — prova de que a figura arquivada já era v3.
  pytest: 14/14 aprovados.
- **Resíduos v1 corrigidos/selados** (padrão mistakes.md #4: documento derivado
  sobrevivendo à correção do fonte): README.md (60→84→1), ecossistema mapa
  (2 ocorrências), laudo adversarial (selo STATUS no topo; transcrição verbatim
  preservada), validacao_cruzada_gse140069 (marca RESOLVIDO + ADDENDUM com
  números finais), mistakes.md #4 e decisions.md:13 (marcas de resolução).
- **Wording estatístico (preprint + nota Prion Alliance)**: "84 nominally
  significant" → "84 significant at FDR<0.05 without covariate adjustment";
  nota também corrigida ("1 surviving at nominal p<0.05" → "at FDR<0.05
  (939 tests)" — nominal seria ~47, não 1).
- **ARQUIVO_COMPLETO.md regenerado** (366 KB): ESTRUTURA do monta_arquivo_completo.py
  completada com o que faltava (coloc_stx6 + coloc_meta, clumping cego, integração
  cérebro×sangue, preprint EN, nota Prion Alliance; apêndice A agora com 16 scripts).
- **dist/public-repo ressincronizado** via prepara_repo_publico.py: 56 arquivos
  (eram 47), 10 figuras, sanitização limpa, git init fresco. Nota Prion Alliance
  permanece FORA do repo (colaboracao/ excluída por política).
- **Limpeza**: `timeline_lito.png` removido (duplicata md5-idêntica de
  timeline_caso_referencia.png, nome legado que a renomeação "Caso Referência"
  não alcançou; zero referências ativas).
- **Citável pronto (29/08)**: autoria real "Arthur Araújo — Independent Researcher,
  Brazil" no CITATION.cff (date-released 2026-08-29) e no preprint (draft v0.2);
  pendência do SANITIZACAO removida do prepara_repo_publico.py; commit 4bcf2f6.
  Obs.: commits paralelos de 29/08 09:31-09:56 (site Litho Foundation) já haviam
  varrido o estado da auditoria para o HEAD.
- Próximo passo natural (inalterado): fila de publicação — repo público + Zenodo
  DOI (rota_zenodo.md) + bioRxiv; decisão de envio da nota Prion Alliance.
