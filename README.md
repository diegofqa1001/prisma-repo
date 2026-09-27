# Corpus PRISMA — Perfiles de riesgo conductual de inversionistas

Repositorio de soporte para la revisión sistemática (PRISMA 2020) que sustenta la
taxonomía de perfiles de riesgo conductual propuesta en la tesis doctoral
*"Modelo adaptativo de recomendación para el diseño de portafolios de inversión
en renta variable bajo incertidumbre, mediante el operador OWA y perfiles
conductuales de riesgo"*. Contiene la ecuación de búsqueda, los metadatos
bibliográficos de identificación de los registros de Scopus y Web of Science,
el proceso de deduplicación y resolución de DOI, las decisiones de cribado, la
síntesis temática y el diagrama de flujo PRISMA.

Se publica para que cualquier persona — director de tesis, jurado, par evaluador,
lector— pueda repetir la búsqueda y verificar cada número reportado en el
capítulo metodológico.

## Por qué existe este repositorio

Documenta de forma verificable cada paso de la revisión sistemática que
sustenta el Capítulo 3 de la tesis: cada registro tiene su DOI (resuelto contra
Crossref cuando la base de datos de origen no lo entregaba), cada script es
ejecutable, y cada número del diagrama de flujo se recalcula desde
`PRISMA_master_final.csv` (Figura 3.4: `python3 08-sintesis/fig_3_4_prisma_flujo.py`).

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
| Cribado título/resumen — excluidos (161 por criterio + 48 inciertos + 8 incluidos que pasaron a excluidos tras la validación) | 217 (38.8 %) |
| Validación por muestreo del cribado (Kappa de Cohen, IA-IA) | 0.799 ("sustancial") |
| Síntesis temática a nivel de resumen (`08-sintesis/`, 2026-09-02) — registros codificados | 343 |
| Dimensiones candidatas codificadas → retenidas | 14 → 7 |
| Acuerdo entre codificadores por dimensión (Kappa de Cohen, doble pasada) | 0.76–0.96 (149 adjudicaciones) |

El cribado título/resumen (ver `07-cribado/`) se ejecutó con asistencia de
modelos de lenguaje: una primera pasada sobre los 560 registros y una segunda
pasada ciega e independiente sobre una muestra estratificada del 20 % (102 de
los 512 que la primera pasada decidió; Kappa de Cohen = 0.799, acuerdo
"sustancial" — ver `07-cribado/validacion.md`). El autor de la tesis resolvió
los 58 casos dudosos (48 inciertos y 10 desacuerdos) con una regla de
precaución (excluir). Las 502 decisiones automáticas restantes (92 de ellas
confirmadas por la segunda pasada) quedan **provisionales** hasta una
verificación humana por submuestra: la validación mide consistencia IA-IA y
no sustituye la doble revisión humana independiente que exige PRISMA 2020.

**Actualización 2026-09-02 — síntesis temática ejecutada.** La fase de
extracción y síntesis sobre los 343 registros incluidos ya se ejecutó a nivel
de resumen (ver `08-sintesis/`): catorce dimensiones conductuales candidatas
codificadas registro por registro con doble pasada independiente (Kappa de
Cohen por dimensión entre 0.76 y 0.96) y 149 desacuerdos adjudicados, de donde
se derivan las siete dimensiones retenidas en el Capítulo 3 de la tesis
(`08-sintesis/metodologia.md`, `08-sintesis/tabla_dimensiones_candidatas.csv`,
`08-sintesis/matriz_evidencia.json`). La evaluación a texto completo con doble
revisor humano (fase de elegibilidad de PRISMA 2020) sigue pendiente y se
declara como tal en la tesis y en la Figura 3.4 (`08-sintesis/fig_3_4_prisma_flujo.png`).

## Qué no se publica, y por qué

Los exports crudos de Scopus y Web of Science y los resúmenes de los
registros no se redistribuyen: los términos de uso de Elsevier y Clarivate
Analytics restringen la redistribución de exports masivos, y los resúmenes son
contenido protegido por derechos de los editores. Es el mismo criterio que
aplica el repositorio `capitulo2-cienciometria`. Se publican, en cambio, los
metadatos bibliográficos de identificación de cada registro (título, autores,
fuente, año, DOI con enlace `https://doi.org/`, identificador WoS) y todas las
decisiones propias del proceso (deduplicación, resolución y verificación de
DOI, cribado título/resumen, codificación y adjudicación de la síntesis). Los
pasos que leen los exports o los resúmenes (1, 2, 3 y 5 de «Cómo reproducir»)
requieren que el lector obtenga sus propios exports con acceso institucional
y los coloque en `02-exports-crudos/` y `06-abstracts/` con los nombres de
archivo que usan los scripts; el cribado (paso 6) y la extracción de
resúmenes de Scopus son procedimientos manuales documentados en
`07-cribado/metodologia.md` y `06-abstracts/metodologia.md`, cuyo resultado
congelado es `07-cribado/resultados-cribado.csv`.

## Estructura

```
01-protocolo-busqueda/   Ecuaciones de búsqueda exactas y fecha de ejecución
02-exports-crudos/       Método de extracción (los exports crudos no se redistribuyen)
03-deduplicacion/        Script y metodología de deduplicación cruzada
04-resolucion-doi/       Script y resultados de resolución de DOI vía Crossref
05-diagrama-flujo/       Diagrama de flujo PRISMA y conteos
06-abstracts/            Metodología de extracción de resúmenes y análisis exploratorio (los resúmenes no se redistribuyen)
07-cribado/              Criterios de cribado y resultados título/resumen (preliminar, IA)
08-sintesis/             Síntesis temática de los 343 incluidos: libro de códigos, doble codificación, Kappa, adjudicación, matriz de evidencia, Figura 3.4
scripts/                 Copia consolidada de todos los scripts (reproducibilidad)
PRISMA_master_final.csv  Lista maestra: 560 registros, con metadatos de identificación, DOI, procedencia y cribado
```

## Cómo reproducir

1. **Búsqueda**: ejecutar las ecuaciones de `01-protocolo-busqueda/ecuaciones-busqueda.md`
   en Scopus y Web of Science Core Collection (requiere acceso institucional).
2. **Export**: descargar resultados completos (todos los campos, todo el rango).
   Los exports no se redistribuyen (ver «Qué no se publica»): colóquelos en
   `02-exports-crudos/` con los nombres de archivo que leen los scripts.
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
  navegador, no vía una API. El archivo resultante (`scopus_438_abstracts.json`)
  no se redistribuye; la columna `abstract_source` de
  `PRISMA_master_final.csv` registra la procedencia del resumen de cada registro. Los abstracts de WoS sí son
  reproducibles por script (`scripts/extract_wos_abstracts.py`), porque
  vienen incluidos en el export `.bib` estándar.
- 11 registros (2.0 %) tienen discrepancia entre el DOI resuelto por
  Crossref/WoS y el DOI nativo de Scopus (columna `doi_agreement =
  MISMATCH` en `PRISMA_master_final.csv`); en la mayoría de los casos
  Crossref había resuelto a una versión preprint (SSRN) en vez de la
  versión publicada. Quedan marcados para revisión manual antes de la
  redacción de la bibliografía — ver `06-abstracts/metodologia.md`.
- La extracción de abstracts de Scopus empareja título y resumen por fila
  del DOM y se verificó registro por registro (438/438 títulos coincidentes);
  el procedimiento está en `06-abstracts/metodologia.md` (sección
  "Verificación de alineación título–resumen").
- Al re-ejecutar los scripts con exports propios, `PRISMA_master_final.csv`
  vuelve a incluir las columnas `abstract` y `scopusUrl`; esa versión local no
  debe publicarse.
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
  la decisión operativa está en `cribado_decision_final`). Las 502
  decisiones automáticas sin revisión humana (410 con una sola pasada y 92
  confirmadas por la segunda) quedan provisionales hasta una verificación
  humana por submuestra. Ver `07-cribado/metodologia.md` y
  `07-cribado/validacion.md`.

## Licencia

Datos y documentación: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Código: [MIT](LICENSE).
