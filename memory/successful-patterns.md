# Padrões bem-sucedidos — Projeto DCJ - Lito

## 2026-08 · Bateria de validação adversarial de pipeline estatístico (funcionou inteira)
- **PADRÃO-OURO para auditar teste à mão**: (1) âncora externa publicada (dataset `sleep` do R: Welch t=−1.860813, df=17.77647, p=0.079394); (2) formas fechadas exatas (df=1 Cauchy: 1−2·arctan|t|/π; df=2: 1−|t|/√(t²+2)) — o betacf NR bateu a 1e-13/1e-14; (3) validar a referência própria ANTES; (4) pares (t,df) reais do dataset. Resultado: Welch+BH do pipeline declarados CORRETOS com confiança máxima.
- **BH-FDR**: validar contra âncora p.adjust do R (c(.01,.04,.03,.005)→(.02,.04,.04,.02)) + força-bruta O(m²) da definição por índice (min_{j≥i} m·p₍ⱼ₎/j) — divergência 0.00e+00 em m=800.
- **Permutação como calibração global**: 2000 permutações de rótulos + BH → média 1.26 FP, 2.0% das permutações com ≥1 FP = BH bem calibrado; explosões raras (max 381) = sintoma de empates por censura de piso, não bug.
- **Escada de sensibilidade**: (a) censura de piso (estratificar genes por fração no piso — no 160208, 70% sig entre genes ≤10% piso = sinal robusto); (b) transformação (linear vs log2-first vs log2(x+1): Jaccard só 0.34-0.44 no sangue = escolha domina o resultado); (c) filtro de detecção (939→311 testáveis); (d) ajuste de covariáveis via OLS pinv vetorizado (Y amostras×genes, hat matrix) — barato e decisivo.
- **Verificação de pseudorreplicação**: cruzar `subject` do series matrix com região — 24 amostras FC de 24 sujeitos únicos = inferência limpa; correlação FC-CB intra-sujeito r=0.55-0.88 mostra o que o pool causaria.
- **Sincronia figura↔dados**: recomputar estatísticas do plot (max −log10p, faixa x, contagens) e comparar com o PNG arquivado; md5 da regeneração em /tmp decide. Pegou figura órfã de versão perdida (v2) vs script v1.
- **Cufflinks/FPKM no GEO**: campo "Data processing" de um GSM individual (não da série) traz o método; "Value definition" às vezes só na amostra. GSE160208 = "Normalized, log2-transformed" (nSolver, 40 housekeeping); GSE140069 = Cufflinks "normalized abundance" LINEAR com piso 1e-4.
- **web_search sem API key**: `bu_run` (Browser Use Cloud) navegando GEO/PMC resolve diligência de métodos.

## 2025 · Pesquisa médica rigorosa (estado da arte DCJ)
- **web_search integrado falhou** (sem DEEPSEEK_API_KEY) → solução: **API Tavily via python/curl** (`api.tavily.com/search`, header Bearer) + **PubMed E-utilities** (`esearch/esummary/efetch`) + **ClinicalTrials.gov API v2** (`/api/v2/studies`). Combinação dá citações verificáveis (PMID/DOI/NCT).
- **Variáveis de ambiente NÃO persistem entre chamadas bash** (shell fresco a cada chamada): embutir a chave/script num único bloco heredoc por execução.
- ClinicalTrials.gov API v2: campo `Conditions` não é válido em `fields=`; omitir `fields` e parsear JSON com python é mais robusto.
- Extração de abstracts: `efetch rettype=abstract` funciona; páginas do PubMed renderizadas precisam de regex no HTML ou Tavily Extract.
- Ordem eficaz: (1) esearch PubMed por tópico+ano → (2) esummary p/ títulos+DOI → (3) efetch só dos essenciais → (4) Tavily para institucional/Brasil/associações → (5) Tavily Extract para posts técnicos (cureffi/Ionis).
- Entrega: relatório íntegra gravada em `research/estado_da_arte_dcj.md` antes do report ao agente pai.

## Sessão 1 — Padrões que funcionaram
- GEO series matrix: campos vêm entre ASPAS; filtrar cabeçalho "ID_REF" após strip de aspas, senão genes desalinham dos valores.
- NCBI E-utilities (esearch db=gds + esummary) é caminho direto e confiável para achar GSEs por doença — melhor que busca genérica.
- Baixar sempre `*_series_matrix.txt.gz` (metadados + tabela juntos, acesso aberto, ~80 KB).
- Tavily API com search_depth=advanced + consultas por bloco temático rende fontes primárias boas.
- Validar valores simulados ANTES de escrever CSV: cada linha ganha coluna fonte_validacao.
## 2025 — Catálogo datasets priônicos
- PADRÃO: quando web_search falha (sem API key DEEPSEEK_API_KEY), usar API REST do Tavily via curl (chave fornecida pelo usuário) + APIs primárias (NCBI eutils, ENA filereport, GWAS Catalog REST, BioStudies). Verificar cada accession direto na fonte antes de citar.
- PADRÃO: lote >60s no bash → rodar python com loop HTTP em run_in_background=true.
- PADRÃO: esummary db=gds traz pubmedid; se vazio, buscar título no pubmed esearch para obter citação.
## Rodada 3 — busca de ecossistema (projetos semelhantes)
- PADRÃO: rodar 4-5 consultas Tavily POR bloco bash em paralelo (prefixos A-E nos arquivos /tmp/tavily/) + digest python único ao final = varredura profunda rápida (30 consultas).
- Tavily Extract (`POST /extract`, campo urls[]) puxa texto completo de medRxiv/preprints — melhor que curl direto (JS bloqueia).
- ACHADOS-CHAVE: GSE160208 já minerado por terceiros (Sci Rep 2023, WGCNA+limma); GSE140069 = Nat Commun 2020 (assinatura miRNA original); préprint ago/2026 agrega 25 anos de história natural priônica (medrxiv 10.64898/2026.08.07.26359973) — nossa curadoria tem sobreposição parcial com ele; NÃO existe projeto não-laboratorial de reanálise priônica ativo (nicho vago); CJD Foundation financia bioinformática (>$6M, editais até $100k); Brasil: 547 casos confirmados 2005-2021, RT-QuIC escasso, grupo HC-USP ativo.
- Relatório completo: research/ecossistema_ciencia_aberta_mapa.md

## Rodada 2 — priorização de download
- PADRÃO: grupo Vallabh-Minikel publica freezes abertos no GitHub (ex.: ericminikel/mgh_prnp_freeze2) — monitorar para NfL/tau pré-sintomático; canal legítimo de contribuição analítica externa.
- PADRÃO: sumstats do GWAS Catalog ficam em http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/<FAIXA>/<GCST>/ com faixa tipo GCST90001001-GCST90002000 (não no path direto); achar via index do dir raiz.
- PADRÃO: grupo Vallabh-Minikel (MGH) publica dados de biomarcadores prion como "freeze" aberto no GitHub (ex.: ericminikel/mgh_prnp_freeze2) — monitorar para NfL/tau pré-sintomático.
- CDC WONDER bloqueia bots (403) mas abre em navegador — anotar nos materiais de colaboração.

## 2026-08 — Validação cruzada GSE160208 vs. artigo original (PMID 33375642)
- PADRÃO-OURO de validação externa: replicar o CRITÉRIO dos autores sobre os dados brutos próprios antes de comparar contagens → réplica Welch+BH com p<0.05 & |Δ|>1 reproduziu EXATAMENTE os 184 DEGs do paper; r=1.000 entre Δ nossos e Log2FC oficiais; direção 183/183. Contagens diferentes ≠ erro: primeiro reconciliar critérios (filtro de magnitude, limiar de FDR).
- Suplementos de artigos PMC: binários do pmc.ncbi.nlm.nih.gov caem em reCAPTCHA; MDPI/CDN dá 403/404; ftp OA utils "Object not found" → endpoint confiável: `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/supplementaryFiles` (zip com figuras + suplementos aninhados).
- xlsx de listas de genes traz no CABEÇALHO o critério exato ("p<0.05, q=0.06, >2-fold") — detalhe que o texto do paper omite.
- Metadados GEO: agrupar amostras por !Sample_characteristics_ch1 (diagnosis/brain region), nunca pelo Sample_title (formatos variam entre GSEs).
- PubMed efetch rettype=xml já entrega PMID→PMC ID + DOI + abstract num passo só.
- Genes com variância zero / valores 'null' na series matrix quebram Welch (ZeroDivisionError) — proteger se se==0 antes de dividir.

## 2026-08 · Auditoria cética de utilidade externa
- PADRÃO: testar cada artefato contra a pergunta **"isso economiza tempo de um PhD do campo?"** — se não economiza, é infraestrutura interna, não produto externo.
- PADRÃO: identidade fictícia em tema sensível exige checagem de colisão com pessoas reais no noticiário ANTES de nomear (caso "Lito Souza" × paciente real Lito Sousa, DCJ ago/2026 — renomear antes de qualquer exposição).
- Relatório completo: `colaboracao/auditoria_cetica_utilidade.md` (veredicto por artefato; rota realista: preprint do GWAS GCST90001389 → canal Prion Alliance/cureffi → só então NPDPSC/UCL/UCSF).
