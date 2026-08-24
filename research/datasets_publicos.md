# Catálogo de Datasets Públicos — DCJ e Doenças Priônicas (GEO, via E-utilities)

> **NOTA DE FUSÃO (auditoria de utilidade 2026-08-24)**: este arquivo mantém a
> visão GEO/E-utilities do projeto; o catálogo completo e verificado por agente
> está em `catalogo_datasets_prionicas_CJD.md` (inclui ENA/WGS, GWAS Catalog,
> PRIDE e a seção "o que NÃO existe"). Em caso de dúvida, use o completo.
> Verificado via API oficial do NCBI (E-utilities, db=gds) na sessão 1.
> Todos os acessos são públicos no GEO; nenhum dado novo de pacientes.
> Ordenado por utilidade para curadoria/análise sobre **DCJ humana**.

## Tier 1 — DCJ humana, acesso aberto imediato

| Acessão | Amostras | Descrição | Notas |
|---|---|---|---|
| **GSE160208** | 47 | Córtex frontal + cerebelo, sCJD vs. controles (NanoString, painel neuroinflamação+, 800 genes) | ✅ **JÁ BAIXADO E ANALISADO** pelo projeto → `pipeline/reports/relatorio_gse160208.md`. PMID 33375642, Univ. Copenhagen |
| **GSE156994** | 219 | Metilação de DNA em SANGUE, sCJD vs. controles | Maior n humano; biomarcador epigenético; série matrix disponível |
| **GSE140069** | 105 | Assinatura de miRNA sanguíneo associada ao diagnóstico de sCJD | Potencial teste diagnóstico líquido; PMID 31138815 |
| **GSE124571** | 21 | RNA: vias de tráfego vesicular desreguladas em CJD | Complementar ao GSE160208 |
| **GSE90977** | 16 | Homeostase de Ca²⁺ / eixo calpaína-catepsina em sCJD | Mecanismo neuronal |

## Tier 2 — Modelos experimentais de príon (contexto mecanístico)

| Acessão | Amostras | Descrição | Relevância |
|---|---|---|---|
| GSE330903 | 31 | Depleção de PrP com pequenas moléculas splice-switching | Terapêutica de redução de PrP (mesma frente do ION717) |
| GSE325339 | 24 | Pipeline quêmico-ômico: vias sinaptotóxicas de príon + drogas inibidoras | Triagem terapêutica |
| GSE277577 | 10 | Micróglia Gpnmb⁺ reagindo à perda neuronal induzida por príon | Conecta com achado microglial nosso (C1QA/CSF1 ↑) |
| GSE198063 | 159 | Perfilamento translacional de subtipos neuronais em infecção priônica | Vulnerabilidade neuronal precoce |
| GSE307182 | 24 | Genótipo APOE modula patologia priônica (modelo murino) | Fator de risco/modificador |
| GSE207251 | 6 | Resposta precoce Arc/Arg3.1 em hipocampo infectado | Assinatura precoce |
| GSE245610 | 18 | Scrapie em células-tronco mesenquimais ovinas | Modelo animal não-humano |
| GSE30643 | 2 | Córtex parietal, paciente com DCJ genética G114V | Caso único humano genético |

## Outros repositórios (verificação pendente de acesso)

| Repositório | O que pode ter | Status |
|---|---|---|
| Synapse (Sage Bionetworks) | Dados colaborativos neurodegeneração sob DUA | a verificar |
| EBRAINS (UE) | Neuroimagem e dados clínicos curados | a verificar |
| OpenNeuro | RM aberta — busca por CJD/príon | a verificar |
| NPDPSC (Case Western) | Biobanco tecidual — só sob acordo/autópsia | contato: cjdsurveillance@uhhospitals.org |
| UK NCJDRSU Edimburgo | Vigilância nacional vCJD | dados agregados públicos |
| JCVDB Japão | Coorte nacional >2000 casos | registros agregados |

## Padrões/formatos esperados por laboratórios (FAIR)
- Expressão: séries matrix GEO (formato padrão que já usamos) ou counts brutos + metadata.
- Neuroimagem: **BIDS** (Brain Imaging Data Structure).
- Estudos ômicos: MIAME/MINSEQE; metadados em planilha separada por amostra.
- Boas práticas: DOI/citação do dataset, script de análise versionado junto.

## Como reproduzir esta busca
```bash
# Listar GSEs humanos de CJD:
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=Creutzfeldt-Jakob+AND+gse%5BETYP%5D&retmax=20&retmode=json"
# Baixar series matrix de qualquer GSE (exemplo):
curl -sL -o GSE160208_series_matrix.txt.gz \
  "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE160nnn/GSE160208/matrix/GSE160208_series_matrix.txt.gz"
```
