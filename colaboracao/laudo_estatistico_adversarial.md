# Laudo da Auditoria Estatística Adversarial — pipeline "DCJ - Lito"
*Revisor independente automatizado · reexecução verbatim + âncoras do R · 2026-08-24*
*(Transcrito integralmente da entrega do revisor; é o registro oficial da auditoria)*

> **STATUS 2026-08-29**: laudo histórico transcrito verbatim — os números que nele constam
> (ex.: "60 miRNAs", item 4) refletem o estado do pipeline NO MOMENTO da auditoria. Após o
> laudo, as correções C2/M3/M4 foram aplicadas: `analise_gse140069.py` v3 (OLS
> idade+sexo+RIN) regenerou `relatorio_gse140069.md` (84 sig. brutos → 1 ajustado;
> filtrado: 5; miR-93-5p q=0.048). Re-execução em 29/08 confirma reprodução byte-a-byte.
> Ver relatorio_gse140069.md v3 e memoria/mistakes.md.

## O QUE ESTÁ CORRETO (validado numericamente)

1. **Welch à mão CORRETO**: âncora R `sleep` exata (t=-1.860813, df=17.77647, p=0.079394)
   nos 2 scripts; formas fechadas df com erro ≤1e-13; betacf NR e df de
   Welch–Satterthwaite corretos; guard se2==0 correto.
2. **BH-FDR PERFEITO**: âncora `p.adjust` R exata; divergência 0.00 vs força-bruta O(m²) em m=800.
3. **437/800 reproduzido exatamente**; calibração por 2000 permutações (média 1.26 FP;
   2.0% das permutações com ≥1 FP); π̂0≈0.33; validação prévia vs artigo (184 DEGs sob
   critério deles, r=1.000) confirmada.
4. **60 miRNAs (8↑/52↓) reproduzido verbatim** do estado atual do script v2.
5. **FC-only SEM pseudorreplicação**: 24 amostras FC de 24 sujeitos únicos (campo subject);
   correlação intra-sujeito FC-CB r=0.55–0.88 mostra que o pool teria inflado, mas não foi usado.
6. Escala GSE160208 correta ("Normalized, log2-transformed signal intensity", nSolver).
7. Nota "sem idade/PMI nos metadados do 160208" é VERDADEIRA.
8. Heatmap top-25 por |Δ|: 25/25 são FDR<0.05 — viés de seleção não se materializa.

## FALHAS CRÍTICAS

- **C1. REPO INCONSISTENTE (depois verificado = FALSO ALARME por leitura desatualizada)**:
  o revisor leu estado antigo (v1). Verificação direta confirmou script/relatório/figura
  consistentes na v2 (log2 antes do Welch, 84 significativos). Lição registrada em mistakes.md #6.
- **C2. SANGUE sem ajuste de idade/RIN (CONFIRMADA)**: casos 66.4 vs controles 53.6 anos;
  RIN 5.59 vs 6.50; covariáveis EXISTEM no series matrix e o artigo original ajustou idade.
  Sob OLS ajustado (log2 ~ grupo+sexo+idade+RIN): 84→1 significativo; direção robusta;
  núcleo do artigo mantém p nominal (miR-16-5p 0.0060, miR-93-5p 0.0007, let-7i-5p 0.0404,
  miR-106b-3p 0.0079); após FDR apenas miR-93-5p sobrevive no universo filtrado (q=0.048).
  → CORRIGIDO no analise_gse140069.py v3.

## FALHAS MÉDIAS

- **M1 (CONFIRMADA/CORRIGIDA)**: ponte contava AMOSTRAS como PACIENTES
  ("12/27 pacientes MM1" = 12 amostras de 6 pacientes). Corrigido com campo subject:
  agora 6/14 pacientes MM1 [43%]; sexo 7M/7F; códon 129 MM=7/MV=3/VV=4.
- **M2**: GSE160208 tem 21.3% de células no piso; 48 genes 100% piso; mitigante: nos genes
  ≤10% piso, 70% significativos — sinal robusto à censura.
- **M3**: GSE140069: 76.6% das células = piso 1e-4; com filtro ≥25%: 269 testáveis,
  116 sig não-ajustado; top-20 sobrevive 16/20. Incorporado ao relatório v3.
- **M4**: tamanho de efeito inconsistente entre métodos (razão de médias vs geométrica);
  Cohen's d mediano +1.38 adicionado ao modelo ajustado.
- **M5 (CORRIGIDA)**: figuras regeneradas com o modelo ajustado; rótulos/eixos corrigidos.

## VEREDICTO FINAL

"437 SOBREVIVE (apresentar 184 lado a lado); direções do cérebro SOBREVIVEM com folga;
'60 miRNAs' NÃO sobrevive como número — sobrevive como assinatura direcional
down-dominante com núcleo replicado do artigo. Ponte: qualitativa ok, quantitativa
corrigida. Sem p-hacking; maquinaria estatística correta a nível de máquina; falhas eram
de desenho (escala, filtro, covariáveis), higiene de repo e apresentação."
