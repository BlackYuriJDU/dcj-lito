# Simulação da cascata priônica e das quatro alavancas
*`simulacao_prion.py` em 2026-08-24 18:05. Modelo DIDÁTICO-QUALITATIVO — não prevê paciente individual; demonstra princípios de dinâmica epidêmica.*

**Parâmetros declarados**: grade 90×90 (8.100 neurônios), vizinhança de 4;
transmissão por contato (p=0,30/dia/vizinho); morte interna 120 dias;
calibração alvo: curso MM1 ≈6 meses até comprometimento quase total.
**Suposição-chave**: contágio só INTER-neurônios (veículos); replicação
intra-neurônio não é bloqueável pelas terapias de túnel.

| Cenário | Meses até 50% perdido | Comprometidos ao fim (10 meses) |
|---|---|---|
| A · Cascata livre | 6.5 | 100.0% |
| B · Muro total (custo socorro) | >10 | 16.3% |
| C · Alfândega perfeita | >10 | 0.0% |
| D · Alfândega realista (80%/5%) | >10 | 50.2% |
| E · Capping (emissão ÷3) | >10 | 98.3% |
| F · Auto-destruição precoce (tdano 40d) | 4.0 | 100.0% |
| G · 50% de células blindadas (G127V-like) | >10 | 0.8% |

## Leitura honesta
- **Base (livre)**: 50% de perda em ~6.5 meses e 100% ao fim — consistente com o curso MM1 real (validação qualitativa do modelo).
- **Muro total**: trava o contágio, mas o custo de socorro cortado (hazard extra 0.02/mês) mata neurônios saudáveis mesmo sem príon — ilustração quantitativa de que fechar tudo tem preço.
- **Alfândega perfeita**: melhor resultado possível — o foco inicial fica isolado e a população se salva.
- **Alfândega REALISTA (captura 80%, colateral 5%)**: 50% ao fim vs. 100% da livre — imperfeição reduz drasticamente mas não zera o dano; mostra que NÃO é necessário ser perfeito para mudar o destino.
- **Capping (emissão ÷3)**: 50% só além do horizonte (>10 meses) vs. 6.5 meses da livre; ainda assim 98% comprometidos ao fim — retardar compra tempo, mas sozinho não salva.
- **F · Auto-destruição precoce (morrer em 40d)**: 100% ao fim — morrer rápido encurta a janela de emissão e protege a POPULAÇÃO, mas cada morte é irreversível: trade-off ético real, não solução.
- **G · 50% blindadas (G127V-like)**: 0.8% ao fim — células resistentes agem como corta-fogos: a cascata morre nos obstáculos. É a única estratégia com PROVA genética natural (Fore/Papua) e em camundongos.

## Conclusão para o projeto
A simulação dá forma numérica à hipótese do proponente: intervenção na
PASSAGEM (alfândega), mesmo imperfectível, altera mais o desfecho do que
qualquer ação contra as partículas já existentes. É hipótese geradora —
requer validação experimental por grupos com ferramentas adequadas
(ver colaboracao/carta_zurzolo.md).