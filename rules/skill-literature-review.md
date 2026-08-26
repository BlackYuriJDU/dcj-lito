# Skill: literature-review

**Gatilho**: pedido de revisão de literatura sobre um tópico.
**Fontes (REST direto, sem MCP)**: PubMed E-utilities, Europe PMC, Semantic
Scholar API, OpenAlex, bioRxiv/medRxiv search; Tavily para o cinza.

## Protocolo
1. **Quebra** do tópico em 3–6 sub-questões objetivas.
2. **Busca** por sub-questão (≥2 fontes independentes cada); registrar:
   query, URL, data de acesso.
3. **Triagem**: título/abstract → incluir só o que responde à sub-questão;
   anotar motivo de exclusão dos relevantes-descartados.
4. **Leitura dirigida** dos incluídos (full-text quando aberto).
5. **Síntese**: por sub-questão → consenso, divergência, qualidade da evidência
   (n, desenho, replicação).
6. **Contradições**: tabela explícita A-diz-X / B-diz-Y / quem tem razão e porquê.
7. **Lacunas**: o que ninguém respondeu.
8. **Saída**: relatório md com citações rastreáveis em cada afirmação +
   bibliografia com PMID/DOI. Nada afirmado sem fonte.

## Anti-padrões proibidos
- Citar abstract sem ler (marcar "(só abstract)" quando inevitável).
- Generalizar de n=1. Confundir preprint com revisado por pares (marcar).
