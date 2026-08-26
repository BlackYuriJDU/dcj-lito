# Skills Científicas — índice (Fase 7 do plano dia 25)

Protocolos formais inspirados na arquitetura do Claude Science (ver
jarvis/packages/dsh-deepseek-design/research/estudo-claude-science.md):
o "agente revisor" e o "especialista de domínio" viram skills acionáveis.

| Skill | Arquivo | Quando usar |
|---|---|---|
| literature-review | `rules/skill-literature-review.md` | "revise a literatura de X" — busca multi-fonte → triagem → síntese com citações |
| evidence-check | `rules/skill-evidence-check.md` | "verifique esta afirmação" — pró/contra rastreado → veredicto calibrado |
| skeptic | `rules/skill-skeptic.md` | "ataque esta hipótese" — adversarial formal antes de aceitar conclusão |
| (workflow) deep_research | `jarvis/workflows/deep_research_cjd.js` | pesquisa profunda multi-agente de ponta a ponta |

Uso com o Modo Science ativo: estes protocolos são a materialização do
"revisor embutido" (artigo 4 da lei science-core.md).
