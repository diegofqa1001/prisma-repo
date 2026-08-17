# Protocolo de búsqueda

## Fecha de ejecución

2026-08-04 a 2026-08-07 (rango en el que se ejecutaron y refinaron ambas búsquedas).

## Bases de datos

- **Scopus** (acceso institucional vía proxy, Universidad Nacional de Colombia)
- **Web of Science Core Collection** (acceso institucional)

## Decisión metodológica: reconstrucción desde cero

La ecuación usada en una versión anterior de la tesis no pudo verificarse (no
había registro reproducible del equation string, los filtros aplicados, ni el
número exacto de resultados en cada paso), así que se descartó por completo y
se reconstruyó una ecuación nueva, documentada en cada etapa.

## Estructura conceptual (3 bloques + filtro temporal)

**Bloque 1 — Sujeto (inversionista):**
investor* OR individual investor* OR retail investor* OR investment decision* OR portfolio

**Bloque 2 — Dimensiones de riesgo conductual (7 dimensiones):**
risk tolerance OR risk profil* OR risk perception OR loss aversion OR
financial self-efficacy OR ambiguity toleran* OR investment horizon OR
emotional regulation OR social influence

**Bloque 3 — Marco de clasificación/perfilado:**
behavioral finance OR behavioural finance OR classification OR typology OR
profiling OR segmentation OR taxonomy

**Filtro temporal:** PUBYEAR/año 2019–2027 (ventana de 8 años, documentada
formalmente en el protocolo — no un "barrido total" sin acotar).

## Ecuación exacta ejecutada en Scopus (TITLE-ABS-KEY)

```
TITLE-ABS-KEY(
  ( "investor*" OR "individual investor*" OR "retail investor*" OR
    "investment decision*" OR "portfolio" )
  AND
  ( "risk tolerance" OR "risk profil*" OR "risk perception" OR "loss aversion" OR
    "financial self-efficacy" OR "ambiguity toleran*" OR "investment horizon" OR
    "emotional regulation" OR "social influence" )
  AND
  ( "behavioral finance" OR "behavioural finance" OR "classification" OR
    "typology" OR "profiling" OR "segmentation" OR "taxonomy" )
)
AND PUBYEAR > 2018 AND PUBYEAR < 2028
```

Resultado: **438 documentos** (Documents tab, sin filtro adicional de tipo de
documento ni idioma — ver decisión abajo).

## Ecuación equivalente ejecutada en Web of Science Core Collection

Misma lógica de 3 bloques, traducida a sintaxis WoS (campo Topic, `TS=`), con
el mismo filtro de años de publicación 2019–2027:

```
TS=(
  ("investor*" OR "individual investor*" OR "retail investor*" OR
   "investment decision*" OR "portfolio")
  AND
  ("risk tolerance" OR "risk profil*" OR "risk perception" OR "loss aversion" OR
   "financial self-efficacy" OR "ambiguity toleran*" OR "investment horizon" OR
   "emotional regulation" OR "social influence")
  AND
  ("behavioral finance" OR "behavioural finance" OR "classification" OR
   "typology" OR "profiling" OR "segmentation" OR "taxonomy")
)
```
Filtro de años de publicación: 2019–2027.

Resultado: **289 documentos** (export completo en `02-exports-crudos/wos_289_savedrecs.bib`).

> **Nota de trazabilidad:** la cadena exacta de WoS no quedó capturada en texto
> plano durante la ejecución interactiva (a diferencia de Scopus, cuyo query
> string sí se extrajo literalmente de la interfaz — ver
> `02-exports-crudos/scopus_query_string.txt`). La cadena de arriba es la
> traducción funcionalmente equivalente de la misma lógica booleana. Se
> recomienda que el autor de la tesis vuelva a ejecutar la búsqueda en WoS y
> capture pantalla del query string exacto para dejar el protocolo 100 %
> verificado en ambas bases antes de someter la tesis.

## Decisiones metodológicas documentadas

- **Filtro de fecha (2019–2027) aplicado a nivel de base de datos.** Se evaluó
  y se descartó explícitamente un "barrido total" sin límite de fecha, para
  mantener un protocolo formalmente acotado y defendible ante un jurado.
- **Filtros de tipo de documento e idioma NO aplicados a nivel de base de
  datos** — se difieren deliberadamente a la etapa de cribado (título/resumen),
  donde se documentan como criterios de exclusión explícitos. Esto es una
  decisión metodológica válida y común en revisiones PRISMA, no un descuido.
- **Filtro de área temática (SUBJAREA) evaluado y NO aplicado.** Se detectó
  ruido temático (ingeniería sísmica, energía, ciberseguridad — términos como
  "risk profiling" y "risk assessment" son genéricos y aparecen fuera de
  finanzas conductuales) pero se decidió dejar ese descarte para el cribado
  manual en lugar de un filtro automático de base de datos, para no excluir
  falsos negativos de forma no auditable.
