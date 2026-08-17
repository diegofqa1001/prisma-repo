# Metodología de deduplicación

## Por qué no se usó DOI como clave primaria

El export de WoS (`wos_289_savedrecs.bib`) trae DOI nativo para la mayoría de
sus 289 registros. El export de Scopus, al haberse obtenido por extracción de
interfaz y no por el botón "Export" nativo (ver
`02-exports-crudos/metodo-extraccion-scopus.md`), no trae DOI en el momento de
la deduplicación. Por eso la deduplicación cruzada Scopus × WoS se hizo por
título, no por DOI — el DOI de los registros exclusivos de Scopus se resolvió
**después**, vía Crossref (`04-resolucion-doi/`), pero eso es una operación
independiente que no afecta el conteo de duplicados.

## Procedimiento

1. **Normalización de título**: minúsculas, sin tildes/diacríticos, sin
   puntuación, espacios colapsados. Ej.: *"Mechanisms Underlying U.S.-China
   Tensions..."* → `mechanisms underlying u s china tensions`.
2. **Cruce exacto** por título normalizado entre el set de Scopus (438) y el
   de WoS (289): **165 coincidencias exactas**.
3. **Pasada de similitud difusa** (`difflib.SequenceMatcher`, umbral ≥ 0.90)
   sobre los registros que no coincidieron exactamente, para capturar
   duplicados con diferencias menores de formato (ej. "U.S." vs "US", un
   artefacto de espaciado). Encontró **2 coincidencias adicionales**:
   - *"Mechanisms Underlying U.S.-China Tensions..."* ↔ *"...US-China
     Tensions..."* (similitud 0.994)
   - *"The Fe ar Z Function..."* ↔ *"The Fear Z Function..."* (similitud
     0.994; el espacio extra es un artefacto de la extracción de Scopus)
4. **Total de duplicados cruzados: 167.**
5. No se encontraron duplicados internos dentro de Scopus ni dentro de WoS
   (cada export es, en sí mismo, ya único).

## Resultado

| | Cantidad |
|---|---|
| Scopus | 438 |
| WoS | 289 |
| Total identificados | 727 |
| Duplicados eliminados | 167 |
| **Únicos para cribado** | **560** |

Desglose de los 560 por procedencia:
- Presentes en ambas bases: 167
- Solo en Scopus: 271
- Solo en WoS: 122

## Limitación reconocida

La deduplicación por título es el método estándar en revisiones PRISMA cuando
no se dispone de DOI en ambas fuentes, pero es susceptible a falsos negativos
si un mismo artículo tiene títulos sustancialmente distintos entre bases (poco
común, pero posible en preprints con título revisado, o erratas). No se hizo
una verificación manual exhaustiva de los 560 registros para descartar este
escenario; se recomienda una revisión muestral antes del cribado final.
