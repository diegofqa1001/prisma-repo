# Resolución de DOI vía Crossref

## Objetivo

Completar el DOI de los 271 registros que quedaron marcados como "Scopus only"
tras la deduplicación (ver `03-deduplicacion/`), para que la lista maestra
tenga trazabilidad completa (DOI resoluble a texto completo / metadatos
oficiales) en la mayor proporción posible de registros.

## Método

Para cada uno de los 271 títulos, se consultó la API pública de Crossref
(`https://api.crossref.org/works`, sin autenticación, con parámetro de
cortesía `mailto` en el User-Agent) con `query.bibliographic=<título>`,
tomando los 3 mejores resultados. Cada candidato se comparó contra el título
original con `difflib.SequenceMatcher` sobre el título normalizado (mismo
método que en la deduplicación).

Clasificación:
- **VERIFIED** — similitud ≥ 0.90: se acepta el DOI del mejor candidato.
- **UNCERTAIN** — similitud entre 0.75 y 0.90: DOI registrado, pero marcado
  para revisión manual antes de usarse en el listado final de referencias.
- **NOT_FOUND** — similitud < 0.75 o sin resultados: sin DOI asignado.

## Resultado (271 registros procesados)

| Estado | Cantidad | % |
|---|---|---|
| VERIFIED | 211 | 77.9 % |
| UNCERTAIN | 12 | 4.4 % |
| NOT_FOUND | 48 | 17.7 % |

Sumado a los 289 registros de WoS (DOI nativo, salvo un puñado marcado
`FROM_WOS` sin DOI en el .bib original) y los 167 que ya tenían DOI por venir
de ambas bases, la lista maestra completa (560 registros) queda con:

- **502 registros con DOI (89.6 %)**
- **58 registros sin DOI (10.4 %)**

## Por qué algunos registros no resuelven

Revisando manualmente los 48 `NOT_FOUND`, el patrón dominante es:
- Capítulos de libro muy recientes (2025-2026) de la colección *"Behavioral
  Finance Strategies for Informed Decision Making"* — probablemente aún no
  indexados en Crossref al momento de la consulta.
- Actas de conferencia con indexación irregular o publicadas por editoriales
  que no registran DOI en Crossref de forma consistente (ej. algunas AIP
  Conference Proceedings, Lecture Notes series de menor tiraje).
- Un caso con título en script no latino mezclado (chino) que probablemente
  requiere búsqueda en el idioma original.

Ver el detalle completo, registro por registro, en `crossref_resolution.json`.
Los `NOT_FOUND` y `UNCERTAIN` deben revisarse manualmente antes de construir
la lista de referencias final de la tesis — no se debe asumir que "sin DOI"
significa "no existe"; en la mayoría de los casos el artículo es real pero
Crossref no lo tiene indexado con metadatos suficientes para un match
automático confiable.
