# Hypothesis note — A selective biophysical "checkpoint" for intercellular prion traffic

*Projeto DCJ - Lito (independent data-organization initiative, Brazil) · 2026-08-24*
*Proposed concept by the project founder; formalized, simulated and documented openly.*

---

## 1. Background

Prion propagation between cells occurs through at least three routes: tunneling
nanotubes (TNTs), extracellular vesicles (exosomes) and synaptic transfer
(Gousset & Zurzolo, *Cell Adh Migr* 2009; Zhu et al., *Front Immunol* 2021).
Pharmacological regulation of vesicle *loading* — e.g. nSMase2/ESCRT inhibition —
reduces extracellular-vesicle-mediated spread (Tallon et al., *Drug Discov Today*
2021). However, no strategy has been proposed that inspects **individual
intercellular transfers** and discriminates infectious from physiological cargo.

The core discrimination problem: PrPC and PrPSc share identical sequence; only
conformation differs. Sequence-based recognition fails by design.

## 2. Hypothesis

A junctional "checkpoint" that (i) transiently retains **all** intercellular
transfer events, (ii) applies a **biophysical pattern test** to each transfer
(cargo density, vesicle rigidity, conformational-probe fluorescence — PrPSc
aggregates are measurably denser and conformationally distinct), and
(iii) degrades or returns only test-positive transfers, would suppress prion
spread while preserving physiological traffic (mitochondrial donation,
lysosomal exchange). This mirrors innate-immunity logic (pattern recognition,
accepted collateral damage) transplanted to the intercellular-traffic level.

Key conceptual distinction from existing approaches: **regulate the tunnel,
do not close it.** Total blockade abolishes rescue traffic (documented
mitochondrial transfer through TNTs), creating its own neuronal loss.

## 3. Simulation evidence (qualitative model)

A stochastic spatial model (90×90 neuron grid, contact-based transmission
p = 0.30/day/neighbour, neuronal death 120 days post-seeding) calibrated so the
untreated cascade reproduces the sCJD MM1 clinical course (50% neuronal loss at
~6.5 months; 100% by month 10; 8 stochastic replicates):

| Scenario | 50% loss reached | Compromised at 10 months |
|---|---|---|
| Untreated cascade | 6.5 months | 100% |
| Total tunnel blockade | >10 m | 16.3% — **all** from lost rescue traffic |
| Perfect checkpoint | >10 m | 0.0% |
| **Imperfect checkpoint (80% capture, 5% collateral)** | >10 m | **50.2%** |
| Conversion-rate reduction alone (3× slower emission) | >10 m | 98.3% (delay only) |

Two model conclusions: (1) an imperfect checkpoint still halves the catastrophe
and pushes the 50% threshold beyond the entire disease horizon; (2) total
blockade carries a quantifiable intrinsic cost, arguing for selective regulation
over closure. Code, parameters and every intermediate number are open
(github.com/BlackYuriJDU/dcj-lito). **Limitation**: the model demonstrates
epidemic-dynamics principles, not clinical prediction; parameters are
order-of-magnitude, not fitted to patient data.

## 4. Testable predictions

1. **In vitro**: in microfluidic co-cultures separating TNT-mediated from
   exosome-mediated transfer, a physical/biophysical retention step (density or
   conformational-probe tagging, e.g. luminescent conjugated polymers) that
   spares clean vesicles should reduce PrPSc transfer proportionally to capture
   efficiency, without abolishing mitochondrial transfer.
2. **Pharmacologic**: partial, non-toxic nSMase2/ESCRT modulation should show a
   threshold behaviour predicted by the model (benefit accelerates as capture
   rises above ~50–60%).
3. **In silico**: the model predicts checkpoint efficacy is robust to capture
   rates ≥60% but degrades steeply below ~40% — a directly testable sensitivity
   profile for any candidate implementation.

## 5. Why we are sending this to you

Your laboratory established that TNTs carry prions between cells and continues
to define this field. We have no laboratory, no funding and no claim beyond the
concept, the open simulation and the numbers above. If this synthesis is wrong
or already disproven, we would be grateful to know why. If it is merely
unexplored, it is yours to test — freely, without conditions.

---

*Contact: Projeto DCJ - Lito · github.com/BlackYuriJDU/dcj-lito · [e-mail do responsável]*

---

## ADDENDUM (2026-08-24, v2) — A segunda alavanca: blindagem celular e o limiar de percolação

Exploração complementar proposta pelo mesmo autor: em vez de inspecionar o
tráfego (checkpoint), **blindar uma fração das células** com PrP conversão-resistente
(G127V-like). A genética já provou o conceito: heterozigotos G127V são protegidos
contra kuru E DCJ clássica (PMC4486072); a proteção dominant-negative se estende a
múltiplas cepas (Gatdula et al., Mol Neurodegener 2026); camundongos homozygotos
são absolutamente resistentes (Asante et al.).

**Varredura estocástica** (grade 80×80, 6 réplicas/ponto, mesma dinâmica calibrada):

| Blindagem | 10% | 20% | 30% | 40% | 50% | 60% |
|---|---|---|---|---|---|---|
| Comprometidos (10 m) | 90% | 80% | 57% | **23%** | **1,3%** | 0,2% |

**Achado central**: o colapso do espalhamento não é linear — é uma transição de
**percolação de sítios** (limiar teórico p_c ≈ 0,593 suscetível ⇒ ~41% blindado),
confirmada numericamente (degrau 40→50%). Abaixo do limiar a epidemia só desacelera;
acima, o surto fica confinado ao foco. Blindagem aleatória (o padrão típico de
entrega de terapia gênica) desempenha igual ou melhor que blindagem agrupada.

**Previsão testável adicional**: em co-cultura com frações crescentes de células
resistentes, o espalhamento deve colapsar não-linearmente perto de ~40% — um
"smoking gun" de percolação, verificável em microfluídica.

**Ressalva de tradução honesta**: instalar G127V exige EDIÇÃO gênica cerebral
(base editing — pré-clínico), não silenciamento. A entrega atual (siRNA/ASO) já
alcança 50–70% dos neurônios em camundongos — a cobertura exigida (~41%) é
alcançável; o método de edição ainda não é clínico.

**Síntese das duas alavancas**: checkpoint de tráfego (regulação) e blindagem
(percolação) são complementares — uma reduz o fluxo infeccioso, a outra fragmenta
o substrato suscetível. O modelo sugere que combinadas, frações menores de cada
podem bastar (não simulado ainda; próximo passo natural).
