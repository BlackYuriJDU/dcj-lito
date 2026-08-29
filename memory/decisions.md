# Decisões arquiteturais e de projeto

Formato: data | decisão | racional

- Sessão 1 | Projeto é SIMULAÇÃO com dados públicos reais; caso "Caso Referência" é fictício | Necessário por ética (nenhum dado novo de pacientes) e pelo pedido explícito do senhor.
- Sessão 1 | Dossiê organizado em caso_lito/, research/, pipeline/, colaboracao/ | Separação clara entre o caso simulado, o conhecimento de base, o processamento e o produto final para laboratórios.
## 2025 — Catálogo datasets priônicos
- DECISÃO: listar só o que foi verificado via API/URL respondendo; registrar explicitamente o que NÃO existe (OpenNeuro/EBRAINS/Kaggle/UK Data Service sem datasets priônicos) para evitar alucinação de catálogo.
- DECISÃO: PRJEB57852 (RNA-seq do estudo italiano sCJD) declarado no artigo mas com 0 runs visíveis na ENA → reportado como "declarado, ainda não liberado".

## 2025 — Validação cruzada GSE140069 × Nat Commun 2020 (PMID 32769986)
- DECISÃO: validação feita contra o texto completo (PMC7414116) + Supplementary Data 1 oficial (xlsx dos 101 miRNAs testados). Veredicto: os 4 hits da descoberta (miR-16-5p, miR-93-5p, miR-106b-3p, let-7i-5p) estão todos entre nossos significativos, mesma direção — núcleo reproduzido (r=+0.64, direção 80%).
- DESCOBERTA CRÍTICA: `relatorio_gse140069.md` foi gerado pelo script v1 (Welch em escala LINEAR + "log2FC" como razão de médias — escalas misturadas). O script atual (v2, log2(x+1) antes do teste) nunca regenerou o relatório: v2 dá 84 sig (10↑/74↓), não 60 (8↑/52↓). PENDENTE: rodar `analise_gse140069.py` para regenerar o relatório com números consistentes.
  **[RESOLVIDO 2026-08-24 14:29]**: o relatório foi regenerado como v3 (log2 + OLS idade+sexo+RIN: 84/69/1/1/5). Auditoria de 2026-08-29 re-executou o script e confirmou reprodução byte-a-byte; pendência encerrada.
- REGRA registrada: depois de corrigir metodologia num script, REGENERAR imediatamente os relatórios derivados; relatório antigo + script novo = inconsistência silenciosa.
- REGRA: comparar com publicação exige espelhar o universo testado deles (eles filtraram 939→101 por cobertura ≥5000; Partek GSA com idade como covariável — nem DESeq2 nem limma).
