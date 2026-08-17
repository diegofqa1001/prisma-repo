# Análisis mínimo del corpus (basado en abstracts) — actualizado 2026-08-12

Análisis exploratorio de los **560 registros únicos** (438 de origen Scopus
con abstract nativo de la interfaz + 122 "WoS only" con abstract tomado del
`.bib` de WoS), como insumo para diseñar los criterios de cribado
título/resumen (la siguiente fase PRISMA, aún pendiente). No sustituye el
cribado formal; sirve para calibrar los criterios de inclusión/exclusión
antes de aplicarlos al corpus completo.

> **Historial de correcciones:**
> - *2026-08-07:* la primera versión de este análisis (n=438, solo Scopus)
>   se calculó sobre un archivo de abstracts con un error de alineación
>   (abstract pegado al título equivocado en 429/438 casos — ver
>   `metodologia.md`). Se corrigió ese día mismo.
> - *2026-08-12:* se completó el abstract de los 122 registros "WoS only"
>   (antes sin abstract, ver `metodologia.md`) y se recalculó todo este
>   análisis sobre el corpus completo de 560 registros, no solo los 438 de
>   Scopus. Los hallazgos no cambiaron de forma cualitativa respecto a la
>   versión del 07-08 (mismos 15 registros con contaminación sísmica: los
>   122 registros WoS-only agregados no aportan casos nuevos de esa
>   categoría), pero ahora el análisis cubre el 100% del corpus en lugar
>   del 78%.

## 1. Distribución por año (corpus completo, n=560)

| Año | n |
|---|---|
| 2027 (in press) | 1 |
| 2026 | 110 |
| 2025 | 133 |
| 2024 | 78 |
| 2023 | 69 |
| 2022 | 49 |
| 2021 | 44 |
| 2020 | 45 |
| 2019 | 31 |

El 69.6% de los registros (390/560) son de 2023-2026. Esto queda por debajo
de la meta del 80% fijada para la tesis, pero esa meta aplica a las
referencias *citadas en el capítulo final*, no al universo identificado
antes de cribar. El cribado título/resumen que sigue reducirá el corpus
reteniendo preferentemente los estudios más pertinentes; si la proporción
2023-2026 no sube lo suficiente de forma natural en ese proceso, es una
señal a vigilar (no a forzar) al momento de seleccionar qué referencias
citar en el capítulo.

## 2. Frecuencia de términos clave (título + abstract, n=560)

Conteo de menciones totales (no de documentos) sobre el texto de todos los
títulos + abstracts concatenados, con expresiones regulares simples
(insensibles a mayúsculas).

| Término / dimensión | Menciones |
|---|---|
| Behavioral / behavioural finance | 349 |
| Loss aversion | 232 |
| Risk tolerance | 224 |
| Machine learning / IA | 201 |
| Risk perception | 197 |
| Overconfidence | 176 |
| Financial literacy | 159 |
| Herding | 142 |
| Risk profile / profiling | 129 |
| Profiling / segmentation | 107 |
| Classification | 105 |
| Cryptocurrency / bitcoin | 104 |
| Robo-advisor* | 96 |
| PLS-SEM / SEM | 75 |
| Anchoring | 67 |
| Prospect theory | 61 |
| Disposition effect | 52 |
| Investment horizon | 37 |
| Taxonomy | 24 |
| Social influence | 23 |
| Typology | 12 |
| Financial self-efficacy | 10 |
| Emotional regulation | 7 |
| **Ambiguity tolerance** | **0** |

**Hallazgo relevante (se sostiene con el corpus completo):** ninguno de los
560 registros usa literalmente "ambiguity tolerance" (ni variantes). El
término sí aparece en la ecuación de búsqueda (como disyunción con otros 8
términos dentro del segundo bloque AND), por lo que no afecta el conteo de
resultados, pero confirma que esa dimensión conductual específica no tiene
tracción terminológica directa en la literatura indexada reciente — se
discute bajo otros nombres (p.ej. "uncertainty avoidance", "tolerance for
ambiguity" como constructo psicométrico) o simplemente no aparece como
palabra clave explícita. Igual sucede, en menor medida, con "financial
self-efficacy" (10) y "emotional regulation" (7). Esto es útil para el
capítulo de discusión: la taxonomía de 7 perfiles conductuales de la tesis
integra constructos con desigual desarrollo empírico en la literatura
Scopus/WoS reciente.

## 3. Señal de contaminación temática (ruido fuera de dominio)

Se buscaron términos de ingeniería civil/sísmica (seismic, earthquake,
bridge network, masonry, building stock, liquefaction, reinforced concrete,
geotechnical) en título+abstract del corpus completo:

- **15 de 560 registros (2.7%)** contienen al menos uno de estos términos
  (todos de origen Scopus; los 122 registros WoS-only no aportan casos
  nuevos de esta categoría).
- De esos 15, **10 no mencionan ningún término financiero/de inversión** en
  absoluto (ni "invest*", "financ*", "portfolio optimi/selecti/managem*",
  "stock market", "trading", "asset alloc*", "equity", "mutual fund") — son
  casi con certeza ruido temático puro:
  - *Seismic Exposure Modelling of the Romanian Residential Building Stock
    for (Re)Insurance Applications*
  - *SEISMIC RISK PROFILE DEFINITION FOR VULNERABLE HOUSING STOCK IN
    COLOMBIA*
  - *BUILDING FOOTPRINT ANALYSIS FOR SEISMIC VULNERABILITY & LARGE SCALE
    HIGH-RESOLUTION RISK ASSESSMENT*
  - *Modeling damage accumulation during ground-motion sequences for
    portfolio seismic loss assessment*
  - *Impacts on catastrophe risk assessments from multi-segment and
    multi-fault ruptures*
  - *Machine-learning based vulnerability analysis of existing buildings*
  - *Nonlinear static characterisation of masonry-infilled RC building
    portfolios*
  - *Analytical fragility curves for masonry school building portfolios in
    Nepal*
  - *Large-scale simplified seismic risk mapping of residential buildings
    through rapid visual screening*
  - *A high-performance computational platform to assess
    liquefaction-induced damage at critical infrastructure*
- Los otros 5 sí mezclan vocabulario financiero (p.ej. "portfolio",
  "investment decisions") con vocabulario sísmico — típicamente porque
  tratan riesgo de carteras de activos físicos/inmobiliarios o reaseguro
  (no inversión bursátil bajo perfiles conductuales), por lo que requieren
  revisión manual en el cribado título/resumen, no exclusión automática.

**Causa raíz:** la polisemia de "portfolio" y "risk profile" — términos
centrales de la ecuación de búsqueda para capturar literatura de finanzas
conductuales — también recupera literatura de ingeniería estructural sobre
"portafolios de puentes/edificios" y "perfil de riesgo sísmico". Es un
trade-off esperable de una ecuación amplia (recall alto, precisión menor) y
exactamente el tipo de ruido que el cribado título/resumen debe filtrar.

Se buscaron además otros dominios de ruido potencial mencionados en
`01-protocolo-busqueda/ecuaciones-busqueda.md` (energía, ciberseguridad):
energía aparece en 10 registros (solo 1 sin vocabulario financiero:
*"Applying risk tolerance and socio-technical dynamics for more realistic
energy transition..."*, sobre modelado de transición energética, no de
inversionistas) y ciberseguridad en apenas 2 registros (ambos con
vocabulario financiero, no ruido puro). No se detectó un tercer dominio de
contaminación significativo aparte del sísmico/estructural.

**Recomendación para el cribado:** los criterios de exclusión de la fase
de cribado deben incluir explícitamente: *"estudios sobre riesgo de
infraestructura física (sísmico, estructural, de reaseguro de activos
físicos) o de sistemas energéticos/de red sin relación con perfiles
conductuales de inversionistas individuales"*.

## 4. Cómo se generó

Script ad hoc ejecutado sobre `PRISMA_master_final.csv` (columnas `title` +
`abstract`, corpus completo de 560 registros). No incluido como script
reproducible en `scripts/` porque es exploratorio, no parte del pipeline
PRISMA formal. Los conteos son reproducibles con expresiones regulares
simples sobre esos dos campos; ver el detalle de patrones en este
documento si se desea replicar.
