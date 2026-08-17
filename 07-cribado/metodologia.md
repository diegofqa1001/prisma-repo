# Cribado título/resumen — metodología

## Qué se hizo

Se aplicaron los criterios formales definidos en
[`criterios-cribado.md`](criterios-cribado.md) a los 560 registros únicos de
`PRISMA_master_final.csv` (título + abstract, ya al 100% de cobertura — ver
`06-abstracts/`). Cada registro fue clasificado como `INCLUDE`, `EXCLUDE` o
`UNCERTAIN`, con el criterio específico citado (I1-I4 para inclusión, E1-E7
para exclusión, `AMBIGUO` para incierto) y un motivo de una frase.

## Resultado del cribado IA (antes de resolución de inciertos)

| Decisión (IA) | n | % |
|---|---|---|
| INCLUDE (provisional) | 351 | 62.7% |
| EXCLUDE | 161 | 28.8% |
| UNCERTAIN | 48 | 8.6% |
| **Total** | **560** | **100%** |

## Resolución de los 48 casos `UNCERTAIN` (2026-08-16)

El autor de la tesis revisó los 48 casos inciertos (agrupados por patrón de
ambigüedad: población institucional/profesional en ~7 casos, activo no
financiero en ~8-9, constructo conductual mencionado solo tangencialmente
en ~15, dinámica agregada de mercado/firma en ~8, mezcla genuina con otro
dominio en ~5, abstract insuficiente en 3) y **decidió excluir los 48 por
precaución**: ante la duda razonable sobre si un registro cumple los
criterios de población (I1), constructo (I2/I3) o alcance de activos (I4),
se prefiere un corpus más estricto y defendible sobre uno más amplio pero
con ajuste dudoso.

Esta decisión no sobrescribe la clasificación original de la IA: en
`resultados-cribado.csv` y en `PRISMA_master_final.csv`, la columna
`decision`/`cribado_decision_ia` conserva `UNCERTAIN` para estos 48
registros, y una columna nueva `decision_final`/`cribado_decision_final`
registra `EXCLUDE` con el motivo de la resolución en la columna
`resolucion`/`cribado_resolucion`. Así queda trazable qué propuso la IA y
qué decidió finalmente el autor, y los 48 registros quedan identificados
por si en una fase posterior (p.ej. al escribir el capítulo de discusión)
conviene reconsiderar alguno.

## Validación por muestreo (2026-08-16)

Además de resolver los 48 inciertos, se ejecutó una segunda pasada de
cribado ciega e independiente sobre una muestra del 20% de los registros
que la IA sí había decidido, para medir el acuerdo entre pasadas (Kappa de
Cohen = 0.799, "sustancial"). Los 10 desacuerdos encontrados se resolvieron
con la misma regla de precaución. Ver el detalle completo en
[`validacion.md`](validacion.md).

## Resultado final (decisión operativa)

| Decisión final | n | % |
|---|---|---|
| INCLUDE (provisional) | 343 | 61.3% |
| EXCLUDE (161 por criterio + 48 por inciertos + 10 por validación) | 217 | 38.8% |
| **Total** | **560** | **100%** |

### Desglose de exclusiones por criterio

| Criterio | Descripción | n |
|---|---|---|
| E6 | Fuera de dominio (falso positivo de la ecuación) | 74 |
| E4 | Riesgo corporativo/institucional puro | 45 |
| E1 | Riesgo de infraestructura física (sísmico/estructural) | 20 |
| E2 | Riesgo de sistemas energéticos/de red | 7 |
| E5 | Actuarial/seguros | 7 |
| E7 | Sin contenido sustantivo propio | 2 |
| E3 | Ciberseguridad | 2 |
| I1 / I4 (fallo de inclusión, sin criterio E específico) | Población o alcance de activos no cumple | 5 |

El criterio E6 (falsos positivos por polisemia de "risk profile", "portfolio",
"classification") es el más frecuente, seguido de E4 (estudios de riesgo a
nivel de firma/institución, no de inversionista individual) — consistente
con el trade-off de recall alto / precisión menor documentado en
`01-protocolo-busqueda/ecuaciones-busqueda.md` para la ecuación de búsqueda.
E1 (contaminación sísmica/estructural) confirma cuantitativamente el
hallazgo de `06-abstracts/analisis-preliminar.md` (15 registros con términos
sísmicos, 10 de ruido puro — coincide con el orden de magnitud de los 20
excluidos por E1 aquí, que incluye además los 5 casos mixtos que requerían
lectura de contenido, no solo detección de términos).

## Cómo se ejecutó (metodología y limitación central)

El cribado fue **asistido por IA**, no por dos revisores humanos
independientes como exige el estándar PRISMA 2020 para minimizar el sesgo
de un único revisor. Se ejecutó dividiendo los 560 registros en 8 lotes de
70, procesados por agentes de IA independientes, cada uno con:

1. El mismo documento de criterios (`criterios-cribado.md`), leído
   completo antes de decidir.
2. Instrucción explícita de leer el contenido del abstract y no limitarse a
   coincidencia de palabras clave.
3. La instrucción de usar la categoría `UNCERTAIN` en vez de forzar una
   decisión cuando el caso es genuinamente ambiguo, en lugar de "resolver"
   la ambigüedad de forma arbitraria.

Cada decisión quedó documentada con su criterio y motivo en
[`resultados-cribado.csv`](resultados-cribado.csv), permitiendo auditar
registro por registro por qué se incluyó o excluyó cada uno — a diferencia
de un cribado que solo reportara los conteos finales.

### Por qué esto NO reemplaza el cribado formal de la tesis

Esta es una limitación declarada, no un detalle menor:

- **No hay doble revisión humana independiente.** El estándar PRISMA
  recomienda ≥2 revisores humanos y una medida de acuerdo (p.ej. Kappa de
  Cohen). Este cribado tiene revisión IA-IA validada (Kappa 0.799, ver
  `validacion.md`) y resolución humana de los casos dudosos (48 inciertos +
  10 desacuerdos de la validación = 58 registros), pero ningún humano ha
  revisado todavía los 454 registros restantes donde ambas pasadas de IA
  coincidieron.
- **Las decisiones `INCLUDE`/`EXCLUDE` de esos 454 registros siguen siendo
  provisionales** hasta que el autor valide al menos una submuestra
  humana. Se recomienda revisar especialmente los casos marcados con
  criterio `E4` (riesgo corporativo/institucional) y `E6` (fuera de
  dominio), que son los más numerosos y los que más dependen de una
  lectura matizada del abstract.

## Próximo paso recomendado

1. Idealmente, el autor de la tesis revisa una submuestra humana (p.ej.
   20-30 registros) de los 454 donde las dos pasadas de IA coincidieron,
   para tener también una medida de acuerdo humano-IA, no solo IA-IA.
2. Una vez el cribado título/resumen se considere suficientemente validado,
   sigue la fase de evaluación a texto completo (PRISMA fase 3) sobre los
   343 registros `INCLUDE` confirmados.

## Archivo de datos

[`resultados-cribado.csv`](resultados-cribado.csv): 560 filas, columnas
`title`, `origin`, `year`, `decision` (clasificación original de la IA),
`criterio`, `motivo`, `decision_final` (decisión operativa, solo
INCLUDE/EXCLUDE), `resolucion` (motivo de la resolución del autor, solo
para los 48 antes `UNCERTAIN`) — una fila por registro de
`PRISMA_master_final.csv`, en el mismo orden.
