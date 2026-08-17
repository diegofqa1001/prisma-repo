# Validación del cribado título/resumen — segunda pasada independiente

## Por qué

`07-cribado/metodologia.md` deja declarado que el cribado asistido por IA
no reemplaza el estándar PRISMA de doble revisión independiente. Como
primer paso hacia validar esa limitación (en vez de solo declararla), se
ejecutó una **segunda pasada de cribado, ciega e independiente**, sobre una
muestra del cribado original, y se midió el acuerdo entre ambas con el
Kappa de Cohen — la métrica estándar en revisiones sistemáticas para
reportar fiabilidad entre revisores.

**Limitación que se mantiene:** ambas pasadas fueron ejecutadas por IA
(agentes independientes, mismos criterios, sin ver la decisión de la otra
pasada). Esto mide **fiabilidad IA-IA**, no fiabilidad IA-humano ni
humano-humano. Es una validación de consistencia interna del proceso, no
un reemplazo de la revisión humana que exige PRISMA. Se documenta como tal.

## Metodología del muestreo

- Universo: los 512 registros que la IA sí decidió en el cribado original
  (`INCLUDE` o `EXCLUDE`, excluyendo los 48 `UNCERTAIN` ya resueltos por el
  autor).
- Muestra: 102 registros (~20%), estratificada proporcionalmente — 70 de
  los 351 `INCLUDE` (20%) y 32 de los 161 `EXCLUDE` (20%).
- Semilla aleatoria fija: `20260816` (Python `random.seed`), para que el
  muestreo sea reproducible por cualquiera que audite este repositorio.
- Segunda pasada: 4 lotes de ~26 registros cada uno, procesados por
  agentes de IA independientes de los que hicieron el cribado original,
  con los mismos criterios (`criterios-cribado.md`) pero **sin ver la
  decisión original** — un re-cribado ciego genuino, no una verificación.

## Resultado: tabla de contingencia

| Original ↓ / Segunda pasada → | INCLUDE | EXCLUDE | UNCERTAIN |
|---|---|---|---|
| **INCLUDE** | 62 | 1 | 7 |
| **EXCLUDE** | 0 | 30 | 2 |
| **UNCERTAIN** | — | — | — (no aplica, no estaban en la muestra) |

- Acuerdo observado (Po): 90.2% (92/102)
- Acuerdo esperado por azar (Pe): 51.2%
- **Kappa de Cohen: 0.799**

Según la escala de referencia de Landis & Koch (1977), 0.799 cae en la
banda "acuerdo sustancial" (0.61-0.80), en el límite superior, casi
"acuerdo casi perfecto" (0.81-1.00). Es un resultado sólido para un
proceso de cribado asistido por IA de un solo revisor por pasada.

**Patrón notable:** de los 10 desacuerdos, 9 fueron hacia `UNCERTAIN` (la
segunda pasada dudó donde la primera había decidido, o viceversa) y solo
1 fue un reverso directo `INCLUDE → EXCLUDE`. Ningún caso fue un reverso
directo `EXCLUDE → INCLUDE`. Esto sugiere que las dos pasadas no
discreparon sobre qué está claramente dentro o fuera del dominio — solo
sobre qué tan seguro se puede estar en los casos límite, que es
precisamente donde se esperaría discrepancia legítima entre revisores.

## Resolución de los 10 desacuerdos

Aplicando la misma regla de precaución que el autor de la tesis ya
estableció para los 48 casos `UNCERTAIN` originales (ante duda o
desacuerdo razonable, excluir por precaución en favor de un corpus más
estricto y defendible), los 10 registros con desacuerdo entre pasadas se
resuelven `EXCLUDE`. El detalle de cada caso (título, decisión original,
decisión de la segunda pasada, motivo de la segunda pasada) queda en la
columna `resolucion` de [`resultados-cribado.csv`](resultados-cribado.csv)
— búsqueda por `Validacion por muestreo`.

Los 10 casos:

1. *The future of finance: Artificial intelligence's influence on
   behavioral investment decisions* — INCLUDE → UNCERTAIN
2. *To label or not? A choice experiment testing whether labelled green
   bonds matter to retail investors* — INCLUDE → UNCERTAIN
3. *An Empirical Study on the Influence of the Basic Medical Insurance for
   Urban and Rural Residents...* — INCLUDE → UNCERTAIN
4. *Behavioural Reinforcement Learning (Beyond Rationality: RL under
   Investor Bias)* — INCLUDE → UNCERTAIN
5. *Decoding investor behavior in the age of financial AI...* — EXCLUDE →
   UNCERTAIN
6. *MABStocks: A Stock Market Analysis and Prediction Platform...* —
   EXCLUDE → UNCERTAIN
7. *Investment motives and performance expectations of impact investors*
   — INCLUDE → UNCERTAIN
8. *Mapping the Landscape of Cryptocurrency Investment Decision: A
   Bibliometric Analysis* — INCLUDE → UNCERTAIN
9. *Robust investment strategies with two risky assets* — INCLUDE →
   EXCLUDE (único reverso directo)
10. *Psychological and technological factors shaping cryptocurrency
    investment...* — INCLUDE → UNCERTAIN

## Efecto en el conteo final del corpus

| | Antes de esta validación | Después |
|---|---|---|
| INCLUDE (decisión final) | 351 | **343** |
| EXCLUDE (decisión final) | 209 | **217** |
| Total | 560 | 560 |

## Qué queda pendiente

Esta validación mide consistencia IA-IA, no reemplaza una revisión humana.
Se sigue recomendando que el autor de la tesis (o un segundo revisor
humano) revise al menos una submuestra de las decisiones antes de
reportar el número final en el capítulo metodológico — idealmente
enfocada en los registros con criterio `E4` y `E6` (los más numerosos, ver
`metodologia.md`) y en los 10 casos de desacuerdo listados arriba, que son
los más propensos a beneficiarse de una lectura humana informada por el
contexto completo de la tesis.

## Archivos de esta validación

Los artefactos crudos de la segunda pasada (lotes ciegos y resultados) no
se incluyen en el repositorio por no aportar valor adicional sobre este
resumen — la evidencia consolidada y auditable es este documento más las
columnas `decision`, `decision_final` y `resolucion` de
`resultados-cribado.csv`.
