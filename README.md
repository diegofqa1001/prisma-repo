# Corpus PRISMA — Perfiles de riesgo conductual de inversionistas

Repositorio de soporte para la revisión sistemática (PRISMA 2020) que sustenta la
taxonomía de perfiles de riesgo conductual propuesta en la tesis doctoral
*"Modelo adaptativo de recomendación para el diseño de portafolios de inversión
en renta variable bajo incertidumbre, mediante el operador OWA y perfiles
conductuales de riesgo"*. Contiene la ecuación de búsqueda, los exports crudos
de Scopus y Web of Science, el proceso de deduplicación y resolución de DOI, y
el primer conteo auditable del diagrama de flujo PRISMA.

Se publica para que cualquier persona — director de tesis, jurado, par evaluador,
lector— pueda reproducir la búsqueda y verificar cada número reportado en el
capítulo metodológico, sin tener que confiar en la palabra de nadie.

## Por qué existe este repositorio

Una revisión anterior asociada a este proyecto (Artículo 2, sometido a IBERAMIA 2026)
fue rechazada tras detectarse que 32 de 47 referencias citadas no existían o tenían
metadatos inventados. Ese hallazgo obligó a reconstruir desde cero, con evidencia
verificable en cada paso, el corpus bibliográfico que sustenta la taxonomía de
perfiles de riesgo conductual de la tesis. Este repositorio es esa reconstrucción.

Todo dato aquí es trazable a su fuente: cada registro tiene su DOI (resuelto contra
Crossref cuando la base de datos de origen no lo entregaba), cada script es
ejecutable, y cada número del diagrama de flujo se puede recalcular desde los
archivos crudos.

## Estado actual (2026-08-16)

| Etapa | Cantidad |
|---|---|
| Identificados en Scopus | 438 |
| Identificados en Web of Science | 289 |
| **Total identificados** | **727** |
| Duplicados eliminados (cruce Scopus × WoS) | 167 |
| **Registros únicos para cribado título/resumen** | **560** |
| Registros con DOI verificado (Crossref o WoS) | 502 (89.6 %) |
| Registros sin DOI resoluble en Crossref | 58 (10.4 %) |
| Registros con abstract (438 Scopus UI + 122 WoS .bib) | **560 (100 %)** |
| Registros con DOI nativo de Scopus (verificación cruzada) | 407 (72.7 % del total) |
| DOI nativo vs. DOI resuelto: coinciden (`MATCH`) | 373 (66.6 %) |
| DOI nativo vs. DOI resuelto: discrepancia (`MISMATCH`, revisión manual) | 11 (2.0 %) |
| Cribado título/resumen — incluidos (provisional) | 343 (61.3 %) |
| Cribado título/resumen — excluidos (161 criterio + 48 inciertos + 10 validación) | 217 (38.8 %) |
| Validación por muestreo del cribado (Kappa de Cohen, IA-IA) | 0.799 ("sustancial") |

El cribado título/resumen (ver `07-cribado/`) ya se ejecutó, los 48 casos
que la IA marcó inciertos fueron resueltos por el autor de la tesis
(decisión: excluir por precaución), y se validó con una segunda pasada
ciega e independiente sobre una muestra del 20% (Kappa de Cohen = 0.799,
acuerdo "sustancial" — ver `07-cribado/validacion.md`), resolviendo los 10
desacuerdos encontrados con la misma regla de precaución. Los 343
incluidos siguen siendo **provisionales**: la validación mide consistencia
IA-IA, no reemplaza la doble revisión humana independiente que exige
PRISMA 2020. Se recomienda que el autor revise una submuestra humana antes
de reportar el número en el capítulo metodológico — ver
`07-cribado/metodologia.md` y `07-cribado/validacion.md` para el detalle
completo. La evaluación a texto completo (fase siguiente de PRISMA) aún no
se ha ejecutado.

## Estructura

```
01-protocolo-busqueda/   Ecuaciones de búsqueda exactas y fecha de ejecución
02-exports-crudos/       Exports originales de Scopus y WoS, sin modificar
03-deduplicacion/        Script y metodología de deduplicación cruzada
04-resolucion-doi/       Script y resultados de resolución de DOI vía Crossref
05-diagrama-flujo/       Diagrama de flujo PRISMA y conteos
06-abstracts/            Abstracts (Scopus + WoS) + análisis exploratorio mínimo
07-cribado/              Criterios de cribado y resultados título/resumen (preliminar, IA)
scripts/                 Copia consolidada de todos los scripts (reproducibilidad)
PRISMA_master_final.csv  Lista maestra: 560 registros, con DOI, abstract, procedencia y cribado
```

## Cómo reproducir

1. **Búsqueda**: ejecutar las ecuaciones de `01-protocolo-busqueda/ecuaciones-busqueda.md`
   en Scopus y Web of Science Core Collection (requiere acceso institucional).
2. **Export**: descargar resultados completos (todos los campos, todo el rango).
   Los exports usados en esta versión están en `02-exports-crudos/`.
3. **Deduplicación**: `python3 scripts/dedup.py` reproduce `PRISMA_master_final.csv`
   a partir de los exports crudos.
4. **Resolución de DOI**: `python3 scripts/resolve_dois.py` consulta la API pública
   de Crossref (sin autenticación) para completar el DOI de los registros que
   Scopus no entrega nativamente. Luego `python3 scripts/merge_doi_resolution.py`.
5. **Abstracts y DOI nativo**: `python3 scripts/merge_abstracts.py` fusiona los
   abstracts de `06-abstracts/scopus_438_abstracts.json` (extraídos directamente
   de la interfaz de Scopus, ver `06-abstracts/metodologia.md` — este paso
   puntual no es reproducible por script, requiere repetir la navegación en
   Scopus). Luego `python3 scripts/extract_wos_abstracts.py` +
   `python3 scripts/merge_wos_abstracts.py` completan el abstract de los 122
   registros "WoS only" desde el `.bib` (este paso sí es reproducible por
   script). Luego `python3 scripts/merge_native_doi.py` fusiona el DOI
   nativo de Scopus como columna de verificación cruzada frente al DOI
   resuelto en el paso 4.
6. **Cribado título/resumen**: los criterios están en
   `07-cribado/criterios-cribado.md`. El cribado en sí **no es reproducible
   por script** (requiere juicio de contenido por registro, ver
   `07-cribado/metodologia.md` sobre su naturaleza preliminar asistida por
   IA); `07-cribado/resultados-cribado.csv` es la evidencia congelada del
   cribado del 2026-08-12. `python3 scripts/merge_cribado.py` fusiona ese
   resultado (mecánicamente, reproducible) en `PRISMA_master_final.csv`.

## Metodología de deduplicación (resumen)

Cruce por título normalizado (minúsculas, sin tildes/puntuación) entre Scopus y
WoS, complementado con una pasada de similitud difusa (`difflib.SequenceMatcher`,
umbral ≥ 0.90, bloqueada por año de publicación ±1) para capturar duplicados con
diferencias menores de formato. Detalle completo en
`03-deduplicacion/metodologia.md`.

## Limitaciones conocidas

- El export de Scopus se obtuvo por extracción directa de la interfaz web
  (la función "Export" de Scopus exige una cuenta personal que no estaba
  disponible), no por el botón de exportación nativo. Los datos fueron
  verificados campo por campo contra la interfaz antes de usarse.
- 58 registros (10.4 %) no tienen DOI resoluble automáticamente contra Crossref
  — mayoritariamente capítulos de libro muy recientes o actas de conferencia con
  indexación irregular. Están marcados como `NOT_FOUND` en
  `04-resolucion-doi/crossref_resolution.json` para verificación manual.
- El conteo de WoS (289) difiere en 1 registro del conteo mostrado por el panel
  "Refine" de WoS en una consulta anterior (288) — variación esperable por
  actualización continua del índice entre una consulta y otra.
- Los 122 registros "WoS only" no tienen DOI nativo de Scopus en esta
  versión (no están en Scopus, no hay nada que extraer de esa interfaz).
  Sí tienen abstract desde 2026-08-12, tomado del `.bib` de WoS.
- La extracción de abstracts y DOI nativo **de Scopus** (`06-abstracts/`)
  no es reproducible por script como el resto del pipeline: se hizo
  leyendo el DOM de la interfaz de Scopus con automatización de
  navegador, no vía una API. El archivo `scopus_438_abstracts.json` es la
  evidencia congelada de esa extracción. Los abstracts de WoS sí son
  reproducibles por script (`scripts/extract_wos_abstracts.py`), porque
  vienen incluidos en el export `.bib` estándar.
- 11 registros (2.0 %) tienen discrepancia entre el DOI resuelto por
  Crossref/WoS y el DOI nativo de Scopus (columna `doi_agreement =
  MISMATCH` en `PRISMA_master_final.csv`); en la mayoría de los casos
  Crossref había resuelto a una versión preprint (SSRN) en vez de la
  versión publicada. Quedan marcados para revisión manual antes de la
  redacción de la bibliografía — ver `06-abstracts/metodologia.md`.
- Una versión anterior de la extracción de abstracts (commit `db0b492`)
  tenía un error de alineación que asociaba el abstract de cada registro
  con el título equivocado en 429 de los 438 casos. Fue detectado y
  corregido antes de esta versión; el detalle completo del bug, cómo se
  detectó y cómo se corrigió está documentado en
  `06-abstracts/metodologia.md` (sección "Bug de alineación detectado y
  corregido") por transparencia metodológica.
- **El cribado título/resumen (`07-cribado/`) es preliminar**: fue
  ejecutado por IA (8 lotes de 70 registros, cada uno con los mismos
  criterios formales), no por dos revisores humanos independientes. Los 48
  registros que la IA marcó `UNCERTAIN` (8.6%) fueron resueltos por el
  autor de la tesis el 2026-08-16 (decisión: excluir por precaución, ante
  ajuste dudoso con los criterios de población/constructo/activo). Se
  validó además con una segunda pasada ciega e independiente sobre una
  muestra del 20% de los 512 registros restantes (Kappa de Cohen = 0.799,
  acuerdo "sustancial"), resolviendo los 10 desacuerdos con la misma
  regla de precaución. La clasificación original de la IA se conserva sin
  sobrescribir (columna `cribado_decision_ia` en `PRISMA_master_final.csv`;
  la decisión operativa está en `cribado_decision_final`). Sigue
  recomendándose que el autor revise una submuestra humana de los 454
  registros donde ambas pasadas de IA coincidieron, antes de citar estos
  números en el capítulo metodológico. Ver `07-cribado/metodologia.md` y
  `07-cribado/validacion.md`.

## Licencia

Datos y documentación: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Código: [MIT](LICENSE).
