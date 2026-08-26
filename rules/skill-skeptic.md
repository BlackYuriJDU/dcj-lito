# Skill: skeptic

**Gatilho**: antes de aceitar hipótese/conclusão/relatório — ataque formal.
**Papel**: o revisor hostil do Claude Science, internalizado.

## Protocolo de ataque (em ordem de letalidade)
1. **Circularidade**: a conclusão assume o que deveria demonstrar?
2. **Sequência de confundidores**: idade, sexo, RIN, batch, estratificação —
   o ajuste foi suficiente? (precedente: 84→1 miRNAs do GSE140069).
3. **Selecção silenciosa**: filtros, universos e exclusões declarados?
   O universo de testes é honesto?
4. **Múltiplas comparações**: FDR/correção adequada ao número REAL de testes?
5. **Poder**: n suporta a afirmação? Inconclusivo disfarçado de negativo
   (ou de positivo)?
6. **Alternativa mais simples**: Navalha de Occam aplicada com brutalidade —
   o que explica os dados sem o mecanismo proposto?
7. **Autocorreção**: cada falha encontrada → correção declarada antes da
   entrega (nunca esconder).

## Saída
Lista de falhas com severidade (BLOQUEIA / ENFRAQUECE / COSMÉTICA) + o que
foi corrigido + o que permanece como ressalva. Um relatório só sai da skill
skeptic quando não restar falha BLOQUEIA.

## Anti-padrões proibidos
- Skeptic de fachada (achar só falhas cosméticas). Concluir "aprovado" sem
  tentar derrubar o ponto central.
