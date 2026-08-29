/* Lithos Foundation — app.js (i18n PT-BR/EN + interações) */
(function () {
  "use strict";

  /* ================= i18n ================= */
  var I18N = {
    pt: {
      _title: "Lithos Foundation — Laboratório aberto de doenças priônicas",
      nav_registro: "Registro", nav_situacao: "Situação", nav_relatorios: "Relatórios",
      nav_operacao: "Operação", nav_roadmap: "A seguir", nav_transp: "Transparência",

      hero_status: "PRiSM (NCT07444580) recrutando — única via anti-PRNP aberta a novos participantes",
      hero_eyebrow: "LABORATÓRIO ABERTO · DOENÇAS PRIÔNICAS · BRASIL",
      hero_h1: "Pedra sobre <em>pedra.</em>",
      hero_lead: "A Lithos Foundation é um laboratório de ciência aberta dedicado às doenças priônicas — incluída a Doença de Creutzfeldt-Jakob. Nascemos da urgência de um caso real e público no Brasil e trabalhamos do único jeito que a janela clínica permite: verificar dados que já existem, replicar o que foi publicado e transformar evidência em caminho navegável para famílias e médicos.",
      hero_cta1: "Ver o registro de pesquisa", hero_cta2: "Situação dos ensaios",
      stat1: "datasets reais analisados", stat2: "loci GWAS replicados", stat3: "r da réplica exata", stat4: "miRNAs significantes",
      hero_logo_nota: "marca provisória — a pedra lapidada é o registro que fica; a faceta laranja, a diferença que procuramos",

      reg_eyebrow: "FEITO · 24—28·08·2026",
      reg_h2: "O registro — o que já fizemos",
      reg_sub: "Cada camada abaixo é datada, rastreada à fonte primária e verificável no repositório. Nada aqui se apaga: o registro é a nossa matéria-prima.",
      reg_como_t: "COMO LER",
      reg_como_p: "O registro é organizado em formações geológicas: o que foi colocado primeiro sustenta o que veio depois. Todas as afirmações apontam para fonte primária, com URL e data de acesso.",
      reg_leg1: "dados & verificação", reg_leg2: "clínica & urgência",

      e1h: "<b>FORMAÇÃO 1 · DADOS REAIS</b><time>24—26·08·2026</time>",
      r11: "<time>24·08</time><b>Fundação do laboratório.</b> Duas trilhas: “caso referência” (simulação didática sCJD MM1, dossiê validado pelos critérios CDC/NPDPSC) e trilha real — somente dados públicos e anonimizados. Pacote completo distribuído: 36 documentos, 7 scripts, checksums MD5.",
      r12: "<time>24·08</time><b>GSE160208</b> (47 amostras sCJD/controles, Copenhagen): análise completa — 437/800 genes significantes (Welch + BH-FDR); neuroinflamação massiva (MYD88, TLR2, C1QA, CSF1 — FDR < 10⁻⁴).",
      r13: "<time>24·08</time><b>Catálogos verificados:</b> GEO, ENA (WGS PRJEB57720), GWAS Catalog (GCST90001389), proteômica PRIDE (PXD050656) — incluindo o que <b>não</b> existe.",
      e2h: "<b>FORMAÇÃO 2 · VERIFICAÇÃO INDEPENDENTE</b><time>24·08·2026</time>",
      r21: "<time>24·08</time><b>Réplica exata do artigo do GSE160208:</b> top-10 de genes idêntico na ordem, r = 1.000 (184 DEGs pelo critério dos autores).",
      r22: "<time>24·08</time><b>GSE140069</b> (miRNA no sangue, 57 sCJD × 48 controles): 60 miRNAs significantes; os 4 achados do artigo replicados (let-7i-5p, miR-16-5p, miR-93-5p, miR-106b-3p); AUC 0.788 (sCJD×CT) e 0.924 (sCJD×AD).",
      r23: "<time>24·08</time><b>GWAS GCST90001389</b> (197 MB): QC de 6.314.492 variantes (0 malformadas, λGC = 1.059) e <b>réplica independente 3/3 dos loci publicados</b> — PRNP p=1,6e-15 · STX6 p=7,5e-9 · GAL3ST1 p=6,2e-10 — com fine-mapping de rs3747957 (mesma direção do Brain 2025).",
      r24: "<time>24·08</time><b>Auditoria cética adversarial:</b> máquina estatística validada (Welch/BH corretos a 1e-13); fragilidades de assinaturas publicadas, documentadas com honestidade.",
      e3h: "<b>FORMAÇÃO 3 · HIPÓTESES & SIMULAÇÃO</b><time>24·08·2026</time>",
      r31: "<time>24·08</time><b>Hipótese geradora “alfândega intercelular”</b> (checkpoint biofísico seletivo nas pontes entre células) submetida ao Institut Pasteur — grupo Chiara Zurzolo — com 3 previsões testáveis.",
      r32: "<time>24·08</time><b>Blindagem G127V:</b> varredura encontrou limiar de percolação em ~41% de cobertura para colapsar o espalhamento priônico.",
      r33: "<time>24·08</time><b>Simulação calibrada por literatura</b> (Weibull estocástico): 3 validações — incluindo sobrevida MM1 de 4,3 meses contra 4–5 publicado.",
      e4h: "<b>FORMAÇÃO 4 · CLÍNICA & REDE</b><time>28·08·2026</time>",
      r41: "<time>28·08</time><b>Cenário de ensaios mapeado e repriorizado:</b> PRiSM (NCT07444580) recrutando → via prioritária; ION717 fechado a novos desde 26·08; efavirenz (NCT07482085) ainda sem recrutamento.",
      r42: "<time>28·08</time><b>Logística internacional:</b> visto B-2 médico, cronograma de deslocamento do PRiSM, contatos dos 5 sites e do sponsor (Broad Institute).",
      r43: "<time>28·08</time><b>Dossiê médico modelo:</b> RM (DWI/FLAIR), LCR (14-3-3/t-tau), RT-QuIC e escala MRC-PDRS — pronto para a decisão dos médicos assistentes.",
      r44: "<time>28·08</time><b>Rede Brasil consolidada:</b> RT-QuIC (HC-FMUSP · A.C. Camargo · UFRJ/LAB3DDI), centros de referência por região e canal oficial do Ministério da Saúde.",
      e5h: "<b>FORMAÇÃO 5 · INSTITUCIONAL</b><time>28·08·2026</time>",
      r51: "<time>28·08</time><b>Engajamento científico:</b> cartas formais ao Prion Alliance (Broad Institute) e ao HC-FMUSP (Neurologia Cognitiva), com o pacote completo do laboratório.",
      r52: "<time>28·08</time><b>Guia de famílias em PT-BR</b> publicado — sem jargão, sem promessa.",
      r53: "<time>28·08</time><b>Batismo: Lithos Foundation</b> — homenagem mineral à origem da missão; terreno verificado (sem colisões de marca, domínios livres).",

      sit_eyebrow: "SITUAÇÃO ATUAL · VERIFICADO 29·08·2026",
      sit_h2: "Ensaios e vias, agora",
      sit_sub: "O cenário muda em dias — esta placa reflete a última verificação viva dos registros oficiais e comunicados das organizações de pacientes.",
      sit1_b: "RECRUTANDO · VIA PRIORITÁRIA",
      sit1_p: "Fase 1, <span class=\"destaque\">dose única intratecal</span> com distribuição pan-cerebral. Em camundongos: −49% de PrP e <span class=\"destaque\">+64% de sobrevida mesmo pós-sintomas</span>. Cinco sites nos EUA; custos de viagem apoiados por doações à Prion Alliance.",
      sit1_n: "fase 1 avalia segurança — participação é pesquisa, não tratamento garantido",
      sit2_b: "FECHADO A NOVOS PARTICIPANTES",
      sit2_p: "“Active, not recruiting” desde 26·08 (regimes 1–2 completos; regime 3 encerrou a inclusão). <span class=\"destaque\">Leitura primária estimada para fev/2027</span> — vigilância semanal para eventual reabertura.",
      sit3_b: "AINDA NÃO RECRUTA",
      sit3_p: "Medicamento reposicionado (anti-HIV), via oral. Xuanwu Hospital / Capital Medical University, Pequim. <span class=\"destaque\">Sem via prática</span> para paciente brasileiro no momento.",
      sit4_t: "Acesso expandido / compassivo",
      sit4_b: "NENHUM PROGRAMA PÚBLICO",
      sit4_p: "Nenhum sponsor anunciou programa público; a droga do PRiSM <span class=\"destaque\">não sai dos EUA</span>. A via realista continua sendo a inclusão direta no ensaio, pelo neurologista assistente.",
      gargalo: "<b>O gargalo decisivo:</b> RT-QuIC+ (ou mutação PRNP documentada) é o passaporte diagnóstico; MRC-PDRS ≥ 15 é o filtro de elegibilidade. Dossiê pronto em <b>dias — não semanas</b> — é o que encurta o caminho.",

      rel_eyebrow: "RELATÓRIOS VISUAIS",
      rel_h2: "Placas de leitura rápida",
      rel_sub: "Cada número aponta para o relatório completo no repositório, com fonte primária, código e checksum. Réplica é verificação para o campo — não descoberta nova.",
      p1_t: "GWAS · réplica independente 3/3",
      p1_aria: "Barras de menos log10 do valor p: PRNP 15,8; GAL3ST1 9,2; STX6 8,1; linha de significância genômica em 7,3",
      p1_badge: "réplica 3/3 dos loci",
      p1_note: "fine-mapping: rs3747957 (chr1) p = 9.7e-9, mesma direção β = −0.148 do Brain 2025 · anotação Ensembl GRCh37",
      p2_t: "Transcriptoma cerebral",
      p2_aria: "Barra: 437 genes significantes de 800 testados, 54,6 por cento",
      p2_note: "neuroinflamação massiva confirmada na sCJD — coerente com a literatura do campo",
      p3_t: "miRNA no sangue",
      p3_aria: "Dois medidores semicirculares: AUC 0,788 para sCJD contra controles; AUC 0,924 para sCJD contra Alzheimer",
      p3_badge: "4/4 hits do artigo replicados",
      p3_note: "honestidade da casa: com covariáveis (idade+sexo+RIN), 1 miRNA sobrevive ao FDR — fragilidade documentada e publicada no relatório",
      p4_t: "Simulação calibrada",
      p4_aria: "Barras de dano esperado: sem intervenção 100 por cento; alfândega intercelular 50,2 por cento; limiar de blindagem em 41 por cento",
      p4_svg1: "sem intervenção · 100%",
      p4_svg2: "alfândega 80/5 · 50,2%",
      p4_svg3: "↑ limiar de blindagem G127V: ~41% de cobertura colapsa o espalhamento",
      p4_svg4: "calibração 3/3 validações",
      p4_chip: "hipótese “alfândega intercelular” → Institut Pasteur",
      p4_chip2: "3 previsões testáveis",
      p4_note: "modelo gerador de hipóteses — não é previsão clínica; a síntese não existia na literatura (verificado)",

      op_eyebrow: "FAZEMOS · SEMPRE",
      op_h2: "Operação contínua",
      op_sub: "O que roda toda semana, sem exceção — porque o cenário muda em dias e a informação atrasada não ajuda ninguém.",
      op1_t: "VIGILÂNCIA DE ENSAIOS",
      op1_p: "Semanal: ClinicalTrials.gov + comunicados da CJD Foundation, CureFFI e Prion Alliance — historicamente mais rápidos que o registro oficial.",
      op2_t: "INTELIGÊNCIA CIENTÍFICA",
      op2_p: "Varredura PubMed de terapia priônica dos últimos 30 dias, a cada sessão de trabalho.",
      op3_t: "DOSSIÊS PARA MÉDICOS",
      op3_p: "Material informativo pronto (imagem, LCR, RT-QuIC, MRC-PDRS) para a decisão dos assistentes — nunca conselho clínico direto.",
      op4_t: "CURADORIA DE DADOS",
      op4_p: "GEO · ENA · PRIDE · GWAS Catalog: o que existe, o que falta e o que não existe — com checksums MD5.",
      op5_t: "REDE BRASIL",
      op5_p: "RT-QuIC (HC-FMUSP · A.C. Camargo · UFRJ/LAB3DDI), centros de referência por região, pesquisadores-chave e canal oficial do MS.",
      op6_t: "GUIA DE FAMÍLIAS",
      op6_p: "PT-BR claro: o que é a doença, o que é um ensaio, o que é promessa — sem jargão e sem esperança vendida.",

      road_eyebrow: "VAMOS FAZER · PRÓXIMO ESTRATO",
      road_h2: "O que vem a seguir",
      road_sub: "A ordem importa: publicar antes de falar, constituir antes de captar, presença antes de promessa.",
      r1_t: "Preprint & DOI",
      r1_p: "Manuscrito em inglês no bioRxiv, arquivo completo no Zenodo (DOI citável) e repositório público com o código de análise.",
      r2_t: "Constituição formal",
      r2_p: "Associação sem fins lucrativos: estatuto, CNPJ, CEBAS e registro de marca no INPI — a fundação sai do papel.",
      r3_t: "Presença própria",
      r3_p: "Reserva dos domínios verificados livres em 28·08 (lithosfoundation.org e afins) e endereço de contato institucional.",
      r4_t: "Plataforma de famílias",
      r4_p: "Navegação em PT-BR: do primeiro sintoma ao ensaio, com checklists de exames, perguntas para o médico e fontes verificadas.",
      r5_t: "Advocacy",
      r5_p: "Ministério da Saúde, ANVISA e Congresso: diagnóstico RT-QuIC acessível no SUS e ensaios clínicos de doenças priônicas no Brasil.",

      tr_eyebrow: "TRANSPARÊNCIA",
      tr_h2: "Regras de casa",
      tr1_t: "SÓ DADOS PÚBLICOS",
      tr1_p: "Nenhum dado de paciente individual. Saúde é dado sensível (LGPD): a trilha real usa somente datasets públicos e anonimizados que já existiam.",
      tr2_t: "EVIDÊNCIA COM NÍVEL",
      tr2_p: "Pré-clínico ≠ humano. Réplica ≠ descoberta. Fase 1 = segurança, não promessa. Cada afirmação carrega o seu nível de evidência.",
      tr3_t: "RASTREÁVEL",
      tr3_p: "Toda afirmação aponta para fonte primária com URL e data de acesso. Dados com checksum MD5; código versionado no repositório.",
      aviso: "ESTA PÁGINA É INFORMATIVA E NÃO SUBSTITUI DECISÃO MÉDICA. Nada aqui é conselho individual; todo material clínico é entregue aos médicos assistentes, que decidem.",

      foot_nota: "Nome provisório. Nasce da urgência de um caso real e público no Brasil, anunciado pela família em 21·08·2026 — e de uma pergunta simples: por que a informação certa chega tarde demais?",
      foot_meta: "registro vivo · atualizado em 29·08·2026<br>contato: em breve, junto da constituição formal<br>feito em PT-BR · tudo verificável"
    },

    en: {
      _title: "Lithos Foundation — Open laboratory for prion diseases",
      nav_registro: "Registry", nav_situacao: "Status", nav_relatorios: "Reports",
      nav_operacao: "Operations", nav_roadmap: "Next", nav_transp: "Transparency",

      hero_status: "PRiSM (NCT07444580) recruiting — the only anti-PRNP route open to new participants",
      hero_eyebrow: "OPEN LABORATORY · PRION DISEASES · BRAZIL",
      hero_h1: "Stone upon <em>stone.</em>",
      hero_lead: "Lithos Foundation is an open-science laboratory dedicated to prion diseases — including Creutzfeldt-Jakob Disease. We were born from the urgency of a real, public case in Brazil, and we work the only way the clinical window allows: verifying data that already exists, replicating what has been published, and turning evidence into a navigable path for families and physicians.",
      hero_cta1: "See the research registry", hero_cta2: "Trial status",
      stat1: "real datasets analyzed", stat2: "GWAS loci replicated", stat3: "r of the exact replication", stat4: "significant miRNAs",
      hero_logo_nota: "provisional mark — the cut stone is the record that remains; the orange facet is the difference we look for",

      reg_eyebrow: "DONE · AUG 24—28, 2026",
      reg_h2: "The registry — what we have done",
      reg_sub: "Every layer below is dated, traced to its primary source and verifiable in the repository. Nothing here is erased: the registry is our raw material.",
      reg_como_t: "HOW TO READ",
      reg_como_p: "The registry is organized as geological formations: what was laid down first supports what came after. Every claim points to a primary source, with URL and access date.",
      reg_leg1: "data & verification", reg_leg2: "clinical & urgency",

      e1h: "<b>FORMATION 1 · REAL DATA</b><time>Aug 24—26, 2026</time>",
      r11: "<time>Aug 24</time><b>Laboratory founded.</b> Two tracks: a “reference case” (didactic sCJD MM1 simulation, dossier validated against CDC/NPDPSC criteria) and the real track — public, anonymized data only. Full package distributed: 36 documents, 7 scripts, MD5 checksums.",
      r12: "<time>Aug 24</time><b>GSE160208</b> (47 sCJD/control samples, Copenhagen): full analysis — 437/800 significant genes (Welch + BH-FDR); massive neuroinflammation (MYD88, TLR2, C1QA, CSF1 — FDR < 10⁻⁴).",
      r13: "<time>Aug 24</time><b>Catalogs verified:</b> GEO, ENA (WGS PRJEB57720), GWAS Catalog (GCST90001389), PRIDE proteomics (PXD050656) — including what does <b>not</b> exist.",
      e2h: "<b>FORMATION 2 · INDEPENDENT VERIFICATION</b><time>Aug 24, 2026</time>",
      r21: "<time>Aug 24</time><b>Exact replication of the GSE160208 paper:</b> top-10 gene list identical in order, r = 1.000 (184 DEGs by the authors' criterion).",
      r22: "<time>Aug 24</time><b>GSE140069</b> (blood miRNA, 57 sCJD × 48 controls): 60 significant miRNAs; all 4 findings of the paper replicated (let-7i-5p, miR-16-5p, miR-93-5p, miR-106b-3p); AUC 0.788 (sCJD×CT) and 0.924 (sCJD×AD).",
      r23: "<time>Aug 24</time><b>GWAS GCST90001389</b> (197 MB): QC of 6,314,492 variants (0 malformed, λGC = 1.059) and an <b>independent 3/3 replication of the published loci</b> — PRNP p=1.6e-15 · STX6 p=7.5e-9 · GAL3ST1 p=6.2e-10 — with fine-mapping of rs3747957 (same direction as Brain 2025).",
      r24: "<time>Aug 24</time><b>Adversarial skeptical audit:</b> statistical machinery validated (Welch/BH correct to 1e-13); fragilities of published signatures documented with honesty.",
      e3h: "<b>FORMATION 3 · HYPOTHESES & SIMULATION</b><time>Aug 24, 2026</time>",
      r31: "<time>Aug 24</time><b>Generative hypothesis “intercellular customs checkpoint”</b> (selective biophysical checkpoint at intercellular bridges) submitted to Institut Pasteur — Chiara Zurzolo's group — with 3 testable predictions.",
      r32: "<time>Aug 24</time><b>G127V shielding:</b> a sweep found a percolation threshold at ~41% coverage that collapses prion spread.",
      r33: "<time>Aug 24</time><b>Literature-calibrated simulation</b> (stochastic Weibull): 3 validations — including MM1 survival of 4.3 months against 4–5 published.",
      e4h: "<b>FORMATION 4 · CLINICAL & NETWORK</b><time>Aug 28, 2026</time>",
      r41: "<time>Aug 28</time><b>Trial landscape mapped and reprioritized:</b> PRiSM (NCT07444580) recruiting → priority route; ION717 closed to new participants since Aug 26; efavirenz (NCT07482085) not yet recruiting.",
      r42: "<time>Aug 28</time><b>International logistics:</b> B-2 medical visa, PRiSM travel schedule, contacts for all 5 sites and the sponsor (Broad Institute).",
      r43: "<time>Aug 28</time><b>Model clinical dossier:</b> MRI (DWI/FLAIR), CSF (14-3-3/t-tau), RT-QuIC and the MRC-PDRS scale — ready for the attending physicians' decision.",
      r44: "<time>Aug 28</time><b>Brazil network consolidated:</b> RT-QuIC (HC-FMUSP · A.C. Camargo · UFRJ/LAB3DDI), referral centers by region and the Ministry of Health's official channel.",
      e5h: "<b>FORMATION 5 · INSTITUTIONAL</b><time>Aug 28, 2026</time>",
      r51: "<time>Aug 28</time><b>Scientific engagement:</b> formal letters to Prion Alliance (Broad Institute) and HC-FMUSP (Cognitive Neurology), with the laboratory's complete package.",
      r52: "<time>Aug 28</time><b>Family guide in PT-BR</b> published — no jargon, no promises.",
      r53: "<time>Aug 28</time><b>Naming: Lithos Foundation</b> — a mineral tribute to the mission's origin; terrain verified (no brand collisions, domains available).",

      sit_eyebrow: "CURRENT STATUS · VERIFIED AUG 29, 2026",
      sit_h2: "Trials and routes, right now",
      sit_sub: "The landscape changes in days — this board reflects the latest live check of official registries and patient-organization statements.",
      sit1_b: "RECRUITING · PRIORITY ROUTE",
      sit1_p: "Phase 1, <span class=\"destaque\">single intrathecal dose</span> with pan-brain distribution. In mice: −49% PrP and <span class=\"destaque\">+64% survival even post-symptom onset</span>. Five US sites; travel costs supported by donations to Prion Alliance.",
      sit1_n: "phase 1 measures safety — participation is research, not guaranteed treatment",
      sit2_b: "CLOSED TO NEW PARTICIPANTS",
      sit2_p: "\"Active, not recruiting\" since Aug 26 (regimens 1–2 complete; regimen 3 finished enrollment). <span class=\"destaque\">Primary readout estimated for Feb 2027</span> — weekly watch for a possible reopening.",
      sit3_b: "NOT YET RECRUITING",
      sit3_p: "Repurposed drug (anti-HIV), oral. Xuanwu Hospital / Capital Medical University, Beijing. <span class=\"destaque\">No practical route</span> for a Brazilian patient right now.",
      sit4_t: "Expanded / compassionate access",
      sit4_b: "NO PUBLIC PROGRAM",
      sit4_p: "No sponsor has announced a public program; the PRiSM drug <span class=\"destaque\">does not leave the US</span>. The realistic route remains direct enrollment, led by the attending neurologist.",
      gargalo: "<b>The decisive bottleneck:</b> RT-QuIC+ (or a documented PRNP mutation) is the diagnostic passport; MRC-PDRS ≥ 15 is the eligibility filter. A dossier ready in <b>days — not weeks</b> — is what shortens the path.",

      rel_eyebrow: "VISUAL REPORTS",
      rel_h2: "Quick-read boards",
      rel_sub: "Every number points to the full report in the repository, with primary source, code and checksum. Replication is verification for the field — not a new discovery.",
      p1_t: "GWAS · independent 3/3 replication",
      p1_aria: "Bars of minus log10 p-value: PRNP 15.8; GAL3ST1 9.2; STX6 8.1; genome-wide significance line at 7.3",
      p1_badge: "3/3 published loci replicated",
      p1_note: "fine-mapping: rs3747957 (chr1) p = 9.7e-9, same direction β = −0.148 as Brain 2025 · Ensembl GRCh37 annotation",
      p2_t: "Brain transcriptome",
      p2_aria: "Bar: 437 significant genes out of 800 tested, 54.6 percent",
      p2_note: "massive neuroinflammation confirmed in sCJD — consistent with the field's literature",
      p3_t: "Blood miRNA",
      p3_aria: "Two semicircular gauges: AUC 0.788 for sCJD versus controls; AUC 0.924 for sCJD versus Alzheimer's",
      p3_badge: "4/4 paper hits replicated",
      p3_note: "house honesty: with covariates (age+sex+RIN), 1 miRNA survives FDR — a fragility documented and published in the report",
      p4_t: "Calibrated simulation",
      p4_aria: "Bars of expected damage: no intervention 100 percent; intercellular customs 50.2 percent; shielding threshold at 41 percent",
      p4_svg1: "no intervention · 100%",
      p4_svg2: "customs 80/5 · 50.2%",
      p4_svg3: "↑ G127V shielding threshold: ~41% coverage collapses the spread",
      p4_svg4: "calibration 3/3 validations",
      p4_chip: "\"intercellular customs\" hypothesis → Institut Pasteur",
      p4_chip2: "3 testable predictions",
      p4_note: "a hypothesis-generating model — not a clinical prediction; the synthesis did not exist in the literature (verified)",

      op_eyebrow: "WE DO · ALWAYS",
      op_h2: "Continuous operation",
      op_sub: "What runs every single week — because the landscape changes in days, and late information helps no one.",
      op1_t: "TRIAL WATCH",
      op1_p: "Weekly: ClinicalTrials.gov + statements from the CJD Foundation, CureFFI and Prion Alliance — historically faster than the official registry.",
      op2_t: "SCIENTIFIC INTELLIGENCE",
      op2_p: "PubMed sweep of prion therapy from the last 30 days, every working session.",
      op3_t: "PHYSICIAN DOSSIERS",
      op3_p: "Ready-to-use informational material (imaging, CSF, RT-QuIC, MRC-PDRS) for the attending physicians' decision — never direct clinical advice.",
      op4_t: "DATA CURATION",
      op4_p: "GEO · ENA · PRIDE · GWAS Catalog: what exists, what is missing and what does not exist — with MD5 checksums.",
      op5_t: "BRAZIL NETWORK",
      op5_p: "RT-QuIC (HC-FMUSP · A.C. Camargo · UFRJ/LAB3DDI), referral centers by region, key researchers and the Ministry of Health's official channel.",
      op6_t: "FAMILY GUIDE",
      op6_p: "Plain PT-BR: what the disease is, what a trial is, what a promise is — no jargon, no sold hope.",

      road_eyebrow: "NEXT · THE UPCOMING STRATUM",
      road_h2: "What comes next",
      road_sub: "Order matters: publish before speaking, incorporate before fundraising, presence before promises.",
      r1_t: "Preprint & DOI",
      r1_p: "English manuscript on bioRxiv, full archive on Zenodo (citable DOI) and a public repository with the analysis code.",
      r2_t: "Formal incorporation",
      r2_p: "Nonprofit association: bylaws, CNPJ, CEBAS and trademark registration with INPI — the foundation leaves the drawing board.",
      r3_t: "Own presence",
      r3_p: "Reserve of the domains verified as available on Aug 28 (lithosfoundation.org and kin) plus an institutional contact address.",
      r4_t: "Family platform",
      r4_p: "PT-BR navigation: from first symptom to trial, with exam checklists, questions for the physician and verified sources.",
      r5_t: "Advocacy",
      r5_p: "Ministry of Health, ANVISA and Congress: accessible RT-QuIC diagnosis in the public system and prion-disease clinical trials in Brazil.",

      tr_eyebrow: "TRANSPARENCY",
      tr_h2: "House rules",
      tr1_t: "PUBLIC DATA ONLY",
      tr1_p: "No individual patient data. Health is sensitive data (LGPD/Brazilian GDPR): the real track uses only public, anonymized datasets that already existed.",
      tr2_t: "EVIDENCE WITH A LEVEL",
      tr2_p: "Preclinical ≠ human. Replication ≠ discovery. Phase 1 = safety, not promise. Every claim carries its own level of evidence.",
      tr3_t: "TRACEABLE",
      tr3_p: "Every claim points to a primary source with URL and access date. Data with MD5 checksums; code versioned in the repository.",
      aviso: "THIS PAGE IS INFORMATIONAL AND DOES NOT REPLACE MEDICAL DECISION-MAKING. Nothing here is individual advice; all clinical material is delivered to the attending physicians, who decide.",

      foot_nota: "A provisional name. It is born from the urgency of a real, public case in Brazil, announced by the family on Aug 21, 2026 — and from a simple question: why does the right information arrive too late?",
      foot_meta: "living registry · updated Aug 29, 2026<br>contact: coming soon, with formal incorporation<br>bilingual PT/EN · everything verifiable"
    }
  };

  /* ================= aplicação do idioma ================= */
  function applyLang(lang) {
    var dict = I18N[lang] || I18N.pt;
    document.documentElement.lang = lang === "pt" ? "pt-BR" : "en";
    document.title = dict._title;

    var nodes = document.querySelectorAll("[data-i18n]");
    for (var i = 0; i < nodes.length; i++) {
      var k = nodes[i].getAttribute("data-i18n");
      if (dict[k] !== undefined) nodes[i].textContent = dict[k];
    }
    var nodesH = document.querySelectorAll("[data-i18n-html]");
    for (var j = 0; j < nodesH.length; j++) {
      var kh = nodesH[j].getAttribute("data-i18n-html");
      if (dict[kh] !== undefined) nodesH[j].innerHTML = dict[kh];
    }
    var nodesA = document.querySelectorAll("[data-i18n-aria]");
    for (var m = 0; m < nodesA.length; m++) {
      var ka = nodesA[m].getAttribute("data-i18n-aria");
      if (dict[ka] !== undefined) nodesA[m].setAttribute("aria-label", dict[ka]);
    }

    var btns = document.querySelectorAll(".lang-sw button");
    for (var b = 0; b < btns.length; b++) {
      var ativo = btns[b].getAttribute("data-lang") === lang;
      btns[b].classList.toggle("ativo", ativo);
      btns[b].setAttribute("aria-pressed", ativo ? "true" : "false");
    }
    try { localStorage.setItem("lithos-lang", lang); } catch (e) {}
  }

  var langSalvo = null;
  try { langSalvo = localStorage.getItem("lithos-lang"); } catch (e) {}
  var langInicial = langSalvo || ((navigator.language || "pt").toLowerCase().indexOf("pt") === 0 ? "pt" : "en");
  applyLang(langInicial);

  var sw = document.querySelectorAll(".lang-sw button");
  for (var s = 0; s < sw.length; s++) {
    sw[s].addEventListener("click", function () { applyLang(this.getAttribute("data-lang")); });
  }

  /* ================= menu móvel ================= */
  var hamb = document.getElementById("hamb");
  var mob = document.getElementById("navmob");
  hamb.addEventListener("click", function () {
    var aberto = mob.classList.toggle("aberta");
    hamb.setAttribute("aria-expanded", aberto ? "true" : "false");
    hamb.setAttribute("aria-label", aberto ? "Fechar menu" : "Abrir menu");
  });
  mob.addEventListener("click", function (e) {
    if (e.target.tagName === "A") { mob.classList.remove("aberta"); hamb.setAttribute("aria-expanded", "false"); }
  });

  /* ================= revelação ao rolar ================= */
  var reduz = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var els = document.querySelectorAll(".reveal");
  if (reduz || !("IntersectionObserver" in window)) {
    for (var i = 0; i < els.length; i++) els[i].classList.add("ok");
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add("ok"); io.unobserve(en.target); }
    });
  }, { threshold: 0.12 });
  for (var k = 0; k < els.length; k++) io.observe(els[k]);
})();
