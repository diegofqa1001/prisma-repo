# Protocolo de búsqueda

## Fecha de ejecución

2026-08-04 a 2026-08-07 (rango en el que se ejecutaron y refinaron ambas búsquedas).

## Bases de datos

- **Scopus** (acceso institucional vía proxy, Universidad Nacional de Colombia)
- **Web of Science Core Collection** (acceso institucional)

## Ecuación documentada en cada etapa

La ecuación, los filtros aplicados y el número de resultados de cada base se
registran a continuación para que la búsqueda pueda repetirse.

## Estructura conceptual (3 bloques + filtro temporal)

**Bloque 1 — Sujeto (inversionista):**
investor* OR individual investor* OR retail investor* OR investment decision* OR portfolio

**Bloque 2 — Dimensiones de riesgo conductual (7 dimensiones):**
risk tolerance OR risk profil* OR risk perception OR loss aversion OR
financial self-efficacy OR ambiguity toleran* OR investment horizon OR
emotional regulation OR social influence

> **Nota metodológica (marco a priori):** el Bloque 2 incluye como términos
> las siete dimensiones del marco conceptual preliminar de la tesis (risk
> tolerance, loss aversion, financial self-efficacy, ambiguity tolerance,
> investment horizon, emotional regulation, social influence), más `risk
> profil*` y `risk perception`. La revisión, por tanto, contrasta y
> caracteriza el sustento empírico de un marco definido a priori; no es un
> procedimiento de descubrimiento de dimensiones. Un registro entra al
> corpus si menciona al menos una de esas nueve expresiones, de modo que la
> frecuencia de cada dimensión en el corpus está condicionada por la propia
> ecuación; las dimensiones que la literatura estudia con otros términos
> quedan infrarrepresentadas. Esta implicación se declara como limitación en
> la tesis (§3.2 y §3.5.1).

**Bloque 3 — Marco de clasificación/perfilado:**
behavioral finance OR behavioural finance OR classification OR typology OR
profiling OR segmentation OR taxonomy

**Filtro temporal:** PUBYEAR/año 2019–2027 (búsquedas ejecutadas entre el 4 y
el 7 de agosto de 2026; un registro con año 2027 corresponde a publicación
anticipada en línea).

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

Resultado: **289 documentos** (export completo `wos_289_savedrecs.bib`, no redistribuido; ver README).

> **Nota de trazabilidad:** la cadena exacta de WoS no quedó capturada en texto
> plano durante la ejecución interactiva (a diferencia de Scopus, cuyo query
> string sí se extrajo literalmente de la interfaz — ver
> `02-exports-crudos/scopus_query_string.txt`). La cadena de arriba es la
> traducción funcionalmente equivalente de la misma lógica booleana.

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
