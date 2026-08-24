# Caso "Caso Referência" — Dossiê Clínico Simulado (v0.2 — valores validados)

> **AVISO**: Paciente fictício. Perfil construído a partir da literatura sobre DCJ
> esporádica (sCJD). Nenhum dado real de paciente identificável.
> Cada valor simulado está embasado nas fontes listadas em `fontes.md` e
> materializado em `linha_do_tempo.csv` e `exames_simulados.csv`.

## 1. Identificação simulada
- Nome: Caso Referência (fictício)
- Idade no início do quadro: 62 anos (mediana de início na sCJD: ~60–65)
- Sexo: masculino
- Forma: esporádica (sem histórico familiar, sem mutação PRNP conhecida)

## 2. Quadro clínico simulado (evolução típica sCJD)
### Mês 0–1 (início inespecífico)
- Queixas sutis: insônia, ansiedade, perda de apetite, dificuldades de concentração.
- Frequentemente atribuído a depressão ou estresse — causa clássica de atraso diagnóstico.

### Mês 1–3 (declínio rápido)
- Demência rapidamente progressiva: desorientação temporoespacial, falhas de memória anterógrada.
- Ataxia cerebelar (marcha instável), disartria.
- Mioclonias (espontâneas ou evocadas por estímulo).
- Alterações visuais (síndrome de Heidenhain possível: neglect visual, cegueira cortical).

### Mês 3+ (fase avançada)
- Mutenismo, acinesia, rigidez, disfagia.
- Dependência total para atividades diárias.

## 3. Exames simulados (valores típicos de sCJD — a validar na literatura)
| Exame | Resultado simulado | Observação |
|---|---|---|
| RM crânio (DWI/FLAIR) | Hiperintensidades em núcleos caudados/putame e córtex ("cortical ribboning") | Achado de maior sensibilidade/especificidade (~90%+) |
| Líquor: RT-QuIC | Positivo | Padrão-ouro atual; especificidade ~99% |
| Líquor: proteína 14-3-3 | Positivo | Menor específico que RT-QuIC |
| Líquor: tau total | Elevada (>1300 pg/mL) | Apoio diagnóstico |
| Soro/plasma: NfL | Marcadamente elevada | Marcador de dano neuronal rápido |
| EEG | Descargas periódicas agudas (PSWC) | Tardias no curso; ausência não exclui |
| Teste genético PRNP | Sem mutação (forma esporádica); códon 129 **Met/Met → subtipo MM1** | MM1 = subtipo mais frequente (~70% dos sCJD); homozygose 129 sobre-representada na doença [Frontiers Neurol 2022] |

**Perfil fixado**: sCJD **MM1** — início ~62 anos, sobrevida mediana ~4–6 meses,
RM com envolvimento de gânglios da base + ribboning, RT-QuIC positivo.

## 4. Critérios diagnósticos aplicáveis
Critérios CDC/OMS e critérios europeus atualizados (2017+) que incorporam RT-QuIC:
provável sCJD = quadro clínico progressivo + ≥2 achados (RM típica, RT-QuIC+, 14-3-3/tau, PSWC).
Confirmação definitiva exige histopatologia/imunohistoquímica ou Western blot PrPSc (autópsia).

## 5. Status (atualizado)
- [x] Valores simulados validados contra fontes Tavily → `fontes.md`
- [x] Codon 129 definido: MM → subtipo MM1 (~70% dos sCJD)
- [x] Linha do tempo clínica estruturada → `linha_do_tempo.csv`
- [x] Exames em formato tabular padronizado (com códigos HL7/LOINC sugeridos) → `exames_simulados.csv`
- [ ] Ajustes finais após integração do estado da arte completo (`research/`)
