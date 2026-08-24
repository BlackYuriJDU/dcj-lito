# Ponte Caso↔Real — Caso Referência (simulado) × GSE160208 (real)
*Gerado por `ponte_lito_real.py` em 2026-08-24 14:14.*

Coorte real: 47 amostras — 14 pacientes CJD (14 amostras de córtex frontal) vs. 10 controles. Contagens demográficas são POR PACIENTE (não por amostra).

## Tabela-ponte

| Achado do caso (simulado) | Evidência na coorte real (GSE160208) | Status |
|---|---|---|
| Subtipo molecular **MM1** | 6 pacientes CJD de 14 são MM1 [6/14 (43%)]; amostras MM1 no FC: 6 | ✅ consistente — subtipo mais comum também na coorte |
| Sexo masculino | Coorte CJD: M=7, F=7 | ✅ equilibrada; sem viés |
| Códon 129 Met/Met | Entre CJD: MM=7, MV=3, VV=4 | ✅ homozygose MM predominante, como na literatura |
| Neuroinflamação (GFAP↑, tau↑, NfL↑ no Lito) | Δ médio CJD−CT no córtex frontal: GFAP +2.5, SERPINA3 +4.8, C1QA +2.6, NEFL -2.2, BDNF -1.7, SLC17A6 -2.9 | ✅ gliose↑ e perda neuronal↓ confirmadas nos dados reais |
| RM DWI/FLAIR típica | Não avaliável neste dataset (expressão gênica, não imagem) | ➖ fora do escopo do dataset — embasado na literatura (caso_lito/fontes.md) |
| RT-QuIC positivo / 14-3-3 / EEG PSWC | Idem — dados líquóricos/eletrofisiológicos não fazem parte da série | ➖ idem |

## Leitura honesta
- A ponte cobre o que o dataset REAL pode responder: demografia, genética do hospedeiro
  e assinatura molecular. Exames clínicos do Lito permanecem embasados na literatura.
- O subgrupo MM1-FC real (n=6) é pequeno: diferenças por subtipo aqui são
  descritivas, não inferenciais (n insuficiente para Welch com potência adequada).