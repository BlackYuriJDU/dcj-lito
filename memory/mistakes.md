# Erros cometidos e lições

## 2026-08 (tarde) · Auditoria adversarial independente do pipeline estatístico
- **REGRESSÃO CONFIRMADA no repo**: os fixes documentados abaixo (ponte com baseline fc_ct; GSE140069 v2 com log2(x+1)) NÃO estão no código atual — `ponte_lito_real.py` ainda usa `ct_idx` (FC+CB) como baseline e `analise_gse140069.py` ainda é v1 linear. A figura `volcano_gse140069.png` arquivada É a v2 (max −log10p=8,17, x∈[−9,+2.9], 84 sig) enquanto script/relatório embarcados são v1 (60 sig). Lição: fix documentado ≠ fix aplicado; auditar o ESTADO ENTREGUE, não a memória; versionar código (git) e checagem automática figura↔relatório↔dados.
- **ERRO MEU evitado a tempo**: reexecutar o Welch do sangue em NUMPY deu 141 "sig" vs 60 verbatim. Causa: 74 miRNAs constantes no piso 0.0001 — `sum()` puro dá média bit-exata (variância exatamente 0 → guard se2==0 do pipeline correto); média numpy errou por 1 ulp → variância fantasma 7e-40 → p≈1e-15 falsos. Lição: antes de acusar bug numérico, rodar o caminho aritmético ORIGINAL verbatim no mesmo processo.
- **Minha quadratura t-CDF quebrou em df=1,5** (singularidade u^(a−1) com a<1; clamp 1e-300 explode). O betacf NR auditado bateu formas fechadas (df=1 Cauchy, df=2) a 1e-13/1e-14. Lição: validar a PRÓPRIA referência contra formas exatas antes de julgar código alheio; Monte Carlo não resolve caudas 10⁻⁷ com 400k sorteios.
- **Confusão por idade/RIN no GSE140069 (GRAVE, não corrigida no código)**: casos 66,4 anos vs controles 53,6; RIN 5,59 vs 6,50 (covariáveis EXISTEM no series matrix; o artigo original ajustou idade via Partek GSA). OLS ajustado (log2 ~ grupo+sexo+idade+RIN, filtro detecção ≥25%): 114→3 sig; dos 60 do relatório v1 só 2 sobrevivem; RIN sozinho→60, idade sozinha→9. Direção robusta (58/66). Claim de "assinatura de N miRNAs" exige esse ajuste.
- **Ponte conta AMOSTRAS como PACIENTES**: "12/27 pacientes MM1" = 12 amostras de apenas 6 pacientes (14 pacientes CJD; sexo por paciente = 7M/7F). Campo `subject` no series matrix resolve.

## Rodada validação cruzada GSE160208 (2026-08)
- **Exagero conceitual corrigido**: relatório nosso tratava "perda neuronal" como conclusão alinhada ao artigo original — o artigo (Areškevičiūtė 2020, PMID 33375642) NUNCA afirma perda neuronal (0 menções a "neuronal loss"); foco deles é regionalidade + microglia/dendritic cells. Lição: distinguir SEMPRE "conclusão dos autores" de "inferência nossa plausível"; genes down neurônio-específicos suportam a inferência, não autorizam atribuí-la ao paper.
- **Citação autoral errada**: citávamos "Litman et al." (Litman é 2º autor; 1ª = Areškevičiūtė A) e título abreviado. Lição: conferir ordem de autores e título completo no PubMed antes de citar — efetch do PMID resolve num passo.
- **Contagem sem contexto**: reportamos "437 significativos" sem nota de que o paper reporta 184 sob outro critério (p<0.05 + q≈0.06 + |log2FC|>1). Comparar contagens sem reconciliar critérios parece divergência quando há concordância total (r=1.000; réplica com o critério deles = 184 exato). Corrigido em pipeline/reports/validacao_cruzada_gse160208_artigo_original.md.

## Rodada 3 (ecossistema) — risco detectado

### 4. Colisão de nome: caso fictício "Caso Referência" vs. paciente REAL "Lito Sousa" (GRAVE, preventivo)
- **Fato**: em 21/08/2026 tornou-se público que o influenciador brasileiro **Lito Sousa**
  (canal Aviões e Música) recebeu diagnóstico real de DCJ (g1, BBC Brasil, Folha;
  internado no Albert Einstein). Nosso caso fictício chama-se "Caso Referência".
- **Risco**: enviar materiais externos com esse nome pode parecer exploração de tragédia
  alheia e queimar credibilidade junto a laboratórios.
- **Ação recomendada**: renomear o caso fictício em TODO o diretório + disclaimers,
  ANTES de qualquer contato externo.
- **Lição**: identidades fictícias em tema sensível e de noticiário ativo exigem checagem
  de colisão com pessoas reais ANTES de nomear.

## Sessão 1

### 1. Ponte Lito-real: baseline errado (GRAVE, corrigido)
- **Erro**: `ponte_lito_real.py` usava os 20 controles TOTAIS (córtex + cerebelo) como baseline
  para os marcadores do córtex frontal → Δ distorcidos (NEFL -0.7 em vez de -2.2).
- **Como peguei**: inconsistência numérica entre relatórios (NEFL -2.2 no principal vs -0.7 na ponte).
  Recomputei à mão e o principal estava certo.
- **Lição**: quando dois artefatos citam a MESMA grandeza, os números DEVEM ser idênticos —
  divergência = bug. Comparar relatórios entre si é teste de regressão barato.
- **Correção**: baseline restrito a fc_ct; regenerado e conferido contra ground truth.

### 2. Welch sobre escala linear com inflação de zeros (GRAVE, corrigido)
- **Erro**: análise v1 do GSE140069 rodou Welch sobre valores LINEARES (77% no piso 0.0001,
  cauda até 3e11) → p-values frágeis.
- **Como peguei**: inspeção da distribuição (log10 histograma) antes de confiar.
- **Lição**: SEMPRE plotar/pensar a distribuição antes do teste. "Normalizado" no nome do
  arquivo não significa log-transformado.
- **Correção**: log2(x+1) antes do Welch (v2); figura regenerada com a mesma transformação.

### 3. Menores (todos corrigidos na hora)
- Parser GEO: campos entre aspas + cabeçalho "ID_REF" desalinhando genes×valores.
- xlsx: linha = gene (não coluna); linhas curtas descartadas inteiras.
- Heatmap sem z-score saturou (tudo +3): padronizar por linha antes de imshow.
- PEP 668: pip exige --break-system-packages neste sistema.

## Padrão geral
Erros graves vieram de ASSUMIR estrutura de dados sem verificar. Verificação explícita
(distribuição, tamanhos, valores de referência) pegou todos antes de virarem conclusões.

### 5. Janela do STX6 errada por 20 Mb (GRAVE, corrigido)
- **Erro**: assumi STX6 em chr1:~160 Mb; o correto é 1q25.3 = chr1:180.94–180.99 Mb (GRCh37).
  Quase concluí falsamente que o sinal STX6 "não estava" nos sumstats de 2020.
- **Como peguei**: os hits GW-significativos em chr1:180.95 Mb não batiam com nenhuma
  anotação minha → consulta ao NCBI Gene + Ensembl GRCh37 REST.
- **Lição**: NUNCA confiar em memória para coordenadas genômicas. Consultar NCBI/Ensembl
  SEMPRE, e na build correta (GRCh37 ≠ GRCh38 — o esummary do NCBI retorna GRCh38;
  usar grch37.rest.ensembl.org para dados build 37).
- **Correção**: janela corrigida, QC re-executado; resultado final = replicação 3/3 dos
  loci publicados (PRNP, STX6, GAL3ST1).

### 6. Auditoria adversarial — lições da rodada de críticas (2026-08-24)
- **C1 (falso alarme com lição real)**: o crítico estatístico leu estado antigo do
  repo (v1) e acusou inconsistência v1/v2 que não existia mais. Lição dupla:
  (a) leitores externos podem ver estado desatualizado — versionar/git resolve;
  (b) SEMPRE verificar a acusação diretamente no arquivo atual antes de aceitar
  OU rejeitar (fiz isso — script/relatório/figura já estavam v2 consistentes).
- **C2 (confirmada e corrigida)**: sem ajuste de idade/sexo/RIN, o sinal do sangue
  colapsa de 84 → 1 significativo (FDR). Casos 66,4 vs controles 53,6 anos.
  Núcleo do artigo mantém direção ↓ e p nominal (0,0007–0,04); só miR-93-5p passa
  FDR no universo filtrado. v3 do analise_gse140069.py documenta tudo.
- **M1 (confirmada e corrigida)**: ponte contava AMOSTRAS como PACIENTES
  (12 "pacientes" MM1 = 6 pacientes × 2 amostras). Corrigido com campo subject.
- **Lição-mestra**: covariáveis de confusão (IDADE acima de tudo) podem fabricar
  um "achado" inteiro. O artigo original sabia disso (ajustou idade); nós não —
  e levamos uma rodada inteira para chegar onde eles já estavam. Humildade.
