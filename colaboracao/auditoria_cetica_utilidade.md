# Auditoria cética de utilidade prática — Projeto "DCJ - Lito"

**Data:** 2026-08 · **Perspectiva:** consultoria independente, ponto de vista de quem já
trabalhou com laboratórios acadêmicos de doenças raras (MRC Prion Unit, NPDPSC, UCSF MAC)
e sabe o que esses centros fazem com material externo não solicitado.

---

## 0. Sumário executivo

1. **O projeto, como está, não seria usado por nenhum laboratório.** Seria, na melhor
   das hipóteses, lido por 90 segundos e arquivado. Na pior (se enviado hoje, com o nome
   atual do caso simulado), causaria impressão negativa permanente.
2. **Há um problema crítico e inadiável:** "Lito Souza" é o nome de uma **pessoa real,
   viva e publicamente doente** — Joselito "Lito Sousa" (piloto/influenciador), diagnosticado
   com DCJ em 21/08/2026, caso nacionalmente noticiado (Folha, G1, O Globo), com a família
   fazendo apelo público aos mesmos centros-alvo do projeto (Ionis, Broad, Harvard, Mayo).
   A disclaimer "fictício" não sobrevive a uma busca no Google. **Renomear tudo antes de
   qualquer exposição externa.**
3. O valor real do projeto hoje é **interno** (formação do fundador, mapa de dados,
   infraestrutura de análise). O valor **externo** é próximo de zero — e há uma rota
   concreta para mudar isso (§4): uma reanálise independente dos sumstats do GWAS de sCJD
   (GCST90001389, abertos, já identificados no catálogo) publicada como preprint.
4. A porta de entrada mais realista do campo não é NPDPSC/UCL/UCSF por e-mail — é a
   comunidade Prion Alliance / cureffi (Minikel & Vallabh), que responde contribuições
   técnicas sérias de não-acadêmicos.

---

## 1. Respostas às sete perguntas centrais

### P1 — O que um pesquisador do MRC/NPDPSC/UCSF FARIA com nossos materiais?
**Arquivaria, sem resposta.** Motivos, na ordem em que aparecem na primeira leitura:
- "Caso simulado de paciente" → eles têm milhares de casos **reais** com dados completos
  (o NPDPSC é a maior vigilância neuropatológica de príons do mundo; a UCL tem a maior
  coorte naturalística). Um paciente sintético não preenche nenhuma lacuna deles.
- "Catálogo de datasets públicos" → os datasets principais são deles ou dos concorrentes;
  conhecem melhor do que nós.
- "Reanálise de GSE160208/GSE140069" → reanálise mais simples dos artigos originais
  (ver P3). Pós-doc não adota pipeline de terceiros que reproduz o que já publicou.
- Carta pedindo "orientação" → é um pedido de trabalho não remunerado. Em centro com
  volume alto de contato, e-mail que pede tempo e não oferece algo verificável = sem resposta.
**Exceção real:** o ecossistema Prion Alliance/cureffi (Minikel & Vallabh) é conhecido por
responder cidadãos sérios — mas com contribuição técnica específica, não com dossiê geral.

### P2 — A "ponte caso-simulado ↔ coorte real" tem valor para laboratório?
**Não. É exercício didático — e circular.** Os valores do Lito foram construídos a partir
da literatura; "confirmar" que ele é consistente com uma coorte real que segue a mesma
literatura não testa nada. Um revisor experiente identifica a circularidade em uma linha.
Como material de aprendizagem do fundador: legítimo. Como produto: zero. Não enviar.

### P3 — A reanálise de GSE160208/GSE140069 agrega algo além dos originais?
**Não — e é melhor dizer isso abertamente.**
- GSE160208 (Litman et al. 2020): o artigo já fez a análise; nosso Welch+FDR sobre dados
  já normalizados de um painel dirigido reproduz o resultado óbvio (neuroinflamação
  massiva). "437/800 genes significantes" não é descoberta — é o esperado quando o painel
  foi desenhado para conter os genes da resposta e o efeito é enorme.
- GSE140069 (Mead et al., Nat Commun 2020): os autores fizeram mais e melhor (painel
  reduzido de miRNAs, validação); nossa versão é estatística mais simples, sem ajuste de
  covariáveis, sem modelo preditivo.
- A estratificação MM1 vs. VV2 com n=6 vs. n=4 é descritiva (os relatórios admitem — correto).
**O que agregaria valor:** reanálise que resolva uma questão **em aberto** com dados
públicos — a candidata óbvia, já listada no próprio catálogo do projeto, é o GWAS
GCST90001389 (sumstats abertos, 4.110 casos × 13.569 controles): QC, clumping, replicação
do locus STX6, fine-mapping/colocalização com eQTL cerebrais. Isso é trabalho de semanas,
é verificável, e o grupo que produziu os sumstats é exatamente o MRC Prion Unit.

### P4 — O catálogo de datasets: valor na curadoria ou redundante?
**Os laboratórios já conhecem o conteúdo; a curadoria é útil para NÓS, não para eles.**
O que tem valor marginal real (e não é óbvio para todos):
- a seção **"O que NÃO existe"** (achados negativos verificados: sem RM priônica em
  OpenNeuro/EBRAINS, sem RT-QuIC bruto depositado, dbGaP vazio) — raro, útil para
  planejamento de estudo;
- as **notas de acesso** (aberto vs. DUA vs. sob pedido) e o apêndice de **formatos
  esperados** (MIAME, BIDS, mzML).
Mesmo assim: um data manager de qualquer centro faz isso numa tarde. É infraestrutura
interna de excelente qualidade — não é produto para enviar.

### P5 — O que um laboratório REAL aceitaria de um projeto externo não-acadêmico?
Em ordem de probabilidade de aceitação:
1. **Contribuição técnica pontual e verificável**: correção de erro factual com fonte;
   issue bem-documentada em software que usam; reanálise independente de dados que ELES
   depositaram, com crédito explícito e tom de replicação.
2. **Ferramenta que economize trabalho deles** (não temos ainda nenhuma).
3. **Contato humano credível** — médico/cientista que apresente o projeto (não é o caso).
4. **Dados que não têm** (não é o nosso caso).
O que NÃO aceitam: dossiês gerais, pedidos de orientação, "organizei dados públicos",
materiais em português, anexos pesados, quem cita o caso de paciente real em curso.

### P6 — Risco de spam/amadorismo queimando a credibilidade do fundador?
**Sim, e é o risco nº 1 hoje — por causa do nome.** Cenários concretos:
- Enviar a carta atual (que lidera com "caso Lito Souza") para NPDPSC/UCL no momento em
  que essas instituições estão sendo procuradas pela família real do Lito Sousa → leitura
  quase certa: "mais um explorando a tragédia do influenciador" → descarte + memória
  negativa do remetente. Campo pequeno: as pessoas falam entre si.
- Mitigações (em ordem): (1) **renomear o caso em todo o diretório** — não basta disclaimer;
  (2) nunca mencionar o caso real em nenhum material; (3) não enviar nada até existir um
  artefato que passe no teste **"isso economiza tempo de um PhD?"**; (4) um canal por vez,
  contato único e curto, sem insistência; (5) identidade honesta ("independent researcher",
  nome próprio, sem fingir instituição); (6) inglês em todo material externo.

### P7 — O caso "Lito Souza" pode gerar confusão? Os avisos bastam?
**Sim, pode — e os avisos NÃO bastam.** "Lito Sousa/Souza" hoje é uma pessoa real
identificável, em doença ativa e noticiada. Riscos concretos: (a) alguém ler o dossiê
como dados clínicos reais do paciente (os valores são plausíveis: RT-QuIC+, tau 2400,
NfL 4500); (b) divergência entre nossa simulação e a clínica real gerar desinformação;
(c) interpretação de exploração de tragédia alheia; (d) exposição LGPD/ética — dados
sensíveis simulados sobre pessoa real identificável, sem consentimento. **A única
mitigação adequada é renomear o caso** (ex.: "Caso CSJ-001" ou nome sem ressonância
pública) em scripts, relatórios, figuras, carta, README e MEMORIA — e reescrever a
narrativa do projeto sem âncora no caso real.

---

## 2. Veredicto por artefato

| Artefato | Veredicto | Por quê |
|---|---|---|
| `caso_lito/` (dossiê, timeline, exames, fontes) | **Inútil externamente / ativo perigoso** | Paciente sintético não interessa a laboratório; nome colide com paciente real vivo. Valor interno didático: sim. |
| `pipeline/reports/relatorio_caso_lito.md` | **Inútil externamente** | Aplicar critérios CDC a dados construídos para atendê-los é tautologia. |
| `relatorio_ponte_lito_real.md` | **Inútil externamente** | Circularidade (simulado da literatura "confirmado" por coorte da mesma literatura). |
| `relatorio_gse160208.md` + script | **Duvidoso** | Reanálise mais simples do original; estatística correta mas sem pergunta nova. Código honesto — bom sinal de competência interna. |
| `relatorio_gse140069.md` + script | **Duvidoso** | Idem; original fez mais (painel reduzido + validação). |
| Figuras (volcanos, heatmap, timeline) | **Inútil externamente** | Qualidade de triagem interna; timeline do "paciente" deve ser removida (nome real). |
| `research/catalogo_datasets_prionicas_CJD.md` | **Útil (interno)** — melhor artefato | Verificação primária, achados negativos, notas de acesso e formatos. Não é produto: é mapa de trabalho futuro. |
| `research/datasets_publicos.md` | **Útil (interno)** | Redundante com o catálogo completo; consolidar num só. |
| `research/estado_da_arte_dcj.md` | **Duvidoso** | Boa compilação honesta, mas o campo tem revisões de referência (Nat Rev Dis Primers 2024); nenhum especialista precisa dela. Excelente como formação do fundador. |
| `colaboracao/carta_projeto.md` | **Inútil / nociva na forma atual** | Genérica, pede orientação, lidera com o artefato mais fraco e cita o nome do paciente real. Reescrever do zero após renomeação. |
| `colaboracao/centros_alvo.md` | **Duvidoso** | Mapeamento correto mas raso: e-mails institucionais, sem pessoa certa, sem entender o que cada centro não precisa. |
| Scripts (Welch/FDR/parser GEO em stdlib) | **Duvidoso** | Corretos e honestos, mas reinventar limma/sklearn lê-se como amadorismo para olho acadêmico. Migrar para stack padrão (limma/statsmodels) quando o alvo for externo. |
| `pipeline/scripts/.tavily_key` | **Risco operacional** | Chave de API no diretório; vaza no primeiro zip/git. Mover para fora do projeto ou variável de ambiente. |

---

## 3. O que REMOVERIA

1. **O nome "Lito Souza" de todo o projeto** (obrigatório, antes de qualquer exposição):
   dossiê, CSVs, scripts, figuras, relatórios, carta, README, MEMORIA.
2. **A timeline e figuras do "paciente"** (persona clínica não tem consumidor externo).
3. **A ponte caso↔real** como produto (manter como anexo didático interno, se quiser).
4. **A carta atual** (reescrever do zero, em inglês, com oferta específica).
5. **A duplicação de catálogos** (fundir `datasets_publicos.md` no catálogo completo).
6. **Qualquer menção ao caso real do piloto** em materiais externos — para sempre.
7. A chave Tavily da árvore do projeto.

## 4. O que ADICIONARIA (para virar algo que um laboratório aceitaria)

1. **Uma pergunta em aberto, respondida com dados públicos.** Candidata nº 1: reanálise
   independente dos sumstats **GCST90001389** (já identificados no catálogo; 188 MB, URL
   direta): QC → clumping → replicação do locus STX6 → fine-mapping/colocalização eQTL.
   Entregável: preprint no bioRxiv (inglês) + repositório limpo. É o único caminho do
   projeto em que o centro-alvo (MRC Prion Unit, autor dos sumstats) tem interesse
   objetivo no resultado.
2. **Reprodutibilidade de verdade**: `git init`, requirements/environment, dados
   impossíveis de redistribuir → scripts de download; README em inglês.
3. **Stack estatística padrão** (limma/statsmodels/sklearn) nas análises destinadas ao
   exterior — stdlib puro é ótimo exercício, sinal ruim como vitrine.
4. **Formato acadêmico de leitura**: technical report com abstract, métodos, limitações —
   não dossiês narrativos.
5. **Página única pública** (GitHub Pages) com o material — link, nunca anexo.
6. **Identidade clara**: nome do fundador, "independent researcher", contato real.

## 5. Rota realista de engajamento

| Canal | Formato | Expectativa honesta |
|---|---|---|
| **1. Prion Alliance / cureffi (Minikel & Vallabh)** | Contribuição técnica específica: uso dos dados `mgh_prnp_freeze2` com feedback, issue/correção verificada, ou preprint que cite os dados deles | **A mais alta do campo** para não-acadêmicos: eles respondem público sério. Prazo: dias-semanas. |
| **2. Vigilância e grupos universitários BR** (MS/CGZV, HC-FMUSP) | Curadoria de dados de mortalidade DCJ (SIM/DATASUS) em formato que economize trabalho; em PT-BR | Média; barreira menor, idioma comum. O artigo crítico da vigilância (PMC12894216) lista as lacunas — endereçar uma delas. |
| **3. CJD Foundation / CJDSGN** | Voluntariado, conteúdo educativo para famílias | Alta para impacto social real; zero para pesquisa. |
| **4. NPDPSC / UCL / UCSF por e-mail** | Só DEPOIS de preprint ou contribuição aceita: e-mail de 5 linhas, inglês, link | Sem publicação: ~0%. Com preprint sólido: baixa-média, resposta em semanas/meses. |

**Sequência recomendada:** renomear → escolher a pergunta do GWAS → preprint → canal 1 →
só então canais 4. **Nunca** o inverso.

## 6. Riscos de reputação × mitigações

| Risco | Severidade | Mitigação |
|---|---|---|
| Nome do caso = paciente real em doença ativa | **Crítica** | Renomeação total imediata; zero menções ao caso real; nunca enviar nada antes disso. |
| Carta genérica pedindo orientação | Alta | Reescrever: oferta específica de 5 linhas com link; um destinatário por vez; sem follow-up insistente. |
| Amadorismo percebido (sem git, stdlib, PT-BR, dossiês) | Alta | Repositório limpo, inglês, stack padrão, formato acadêmico. |
| "Apropriação" de dados de terceiros | Média | Crédito explícito em toda reanálise ("independent replication of…"), nunca "descobrimos". |
| Tom de "salvadores do campo" | Média | Humildade epistêmica: o projeto ajuda em curadoria/reanálise; a missão do README está bem calibrada — a carta precisa acompanhar. |
| Vazamento da chave Tavily | Média (operacional) | Chave fora da árvore do projeto; nunca versionar. |

---

## 7. Frase final da auditoria

O projeto tem **matéria-prima honesta** (verificação primária, estatística correta,
honestidade declarada) e **um produto que ninguém pediu** (paciente sintético + reanálises
mais simples dos originais). O caminho para utilidade real não é polir o dossiê — é
trocar a pergunta: de "o que podemos mostrar?" para **"qual pergunta em aberto nós
conseguimos responder com dados públicos que ninguém teve tempo de responder?"**. O GWAS
GCST90001389 já está no catálogo do projeto, com URL direta testada. Essa é a porta.
