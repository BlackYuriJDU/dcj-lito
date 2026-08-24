# Varredura de blindagem (G127V-like) — o limiar do corta-fogos
*`varredura_blindagem.py` em 2026-08-24 18:12. Grade 80×80, 300 dias, média de 6 réplicas por ponto. Mesma dinâmica de `simulacao_prion.py` (contato p=0,30/dia/vizinho; morte 120 d).*

**Previsão teórica**: percolação de sítios em rede quadrada com
vizinhança-4 → p_c ≈ 0.5927 suscetível ⇒ limiar ≈ **40.7% blindado**.

| Blindagem | Final (aleatória) | Final (blocos) |
|---|---|---|
| 0% | 100.0% | 100.0% |
| 10% | 90.0% | 89.8% |
| 20% | 79.7% | 78.9% |
| 30% | 56.8% | 63.9% |
| 40% | 23.2% | 30.9% |
| 50% | 1.3% | 8.3% |
| 60% | 0.2% | 2.9% |
| 70% | 0.1% | 0.1% |
| 80% | 0.0% | 0.1% |
| 90% | 0.0% | 0.1% |

## Leitura honesta
- Maior degrau entre 30%→40% blindados (queda de 33.6 pontos) — comparável ao limiar teórico de ~41%.
- Abaixo do limiar: epidemia avança (só mais devagar). Acima: surto local confinado. É a assinatura de PERCOLAÇÃO, não de efeito linear.
- Blindagem em blocos ≈ aleatória neste modelo 2D de vizinhança-4 (a geometria importa mais em redes de contato reais do cérebro).

**Tradução terapêutica (honesta)**: instalar G127V exige EDIÇÃO
gênica no cérebro (base editing — pré-clínico), não silenciamento;
a tecnologia atual de entrega (siRNA/ASO) já alcança 50–70% dos
neurônios em camundongos, então a COBERTURA necessária (~41%+) é
alcançável — o método de edição é que ainda não é clínico.

**Previsão testável in vitro**: co-cultura com frações crescentes
de células resistentes deve mostrar colapso do espalhamento acima de
~40% — diretamente verificável em chip microfluídico.