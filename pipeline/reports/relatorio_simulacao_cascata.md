# Simulação da cascata priônica e das quatro alavancas
*`simulacao_prion.py` em 2026-08-24 17:42. Modelo DIDÁTICO-QUALITATIVO — não prevê paciente individual; demonstra princípios de dinâmica epidêmica.*

**Parâmetros declarados**: grade 90×90 (8.100 neurônios), vizinhança de 4;
fase silenciosa 45 d; emissão p=0,35/d; morte interna 150 d; MM1 alvo ≈6 meses.
**Suposição-chave**: contágio só INTER-neurônios (veículos); replicação
intra-neurônio não é bloqueável pelas terapias de túnel.

| Cenário | Meses até 50% perdido | Comprometidos ao fim (10 meses) |
|---|---|---|
| A · Cascata livre | >10 | 0.8% |
| B · Muro total (custo socorro) | >10 | 7.4% |
| C · Alfândega perfeita | >10 | 0.0% |
| D · Alfândega realista (80%/5%) | >10 | 0.3% |
| E · Capping (emissão ÷3) | >10 | 0.6% |

## Leitura honesta
- **Base (livre)**: 50% de perda em ~inf meses e 1% ao fim — consistente com o curso MM1 real (validação qualitativa do modelo).
- **Muro total**: trava o contágio, mas o custo de socorro cortado (hazard extra 0.01/mês) mata neurônios saudáveis mesmo sem príon — ilustração quantitativa de que fechar tudo tem preço.
- **Alfândega perfeita**: melhor resultado possível — o foco inicial fica isolado e a população se salva.
- **Alfândega REALISTA (captura 80%, colateral 5%)**: 0% ao fim vs. 1% da livre — imperfeição reduz drasticamente mas não zera o dano; mostra que NÃO é necessário ser perfeito para mudar o destino.
- **Capping (emissão ÷3)**: inf meses até 50% vs. inf da livre — retardar a multiplicação compra tempo mesmo sem bloquear nada.

## Conclusão para o projeto
A simulação dá forma numérica à hipótese do proponente: intervenção na
PASSAGEM (alfândega), mesmo imperfectível, altera mais o desfecho do que
qualquer ação contra as partículas já existentes. É hipótese geradora —
requer validação experimental por grupos com ferramentas adequadas
(ver colaboracao/carta_zurzolo.md).