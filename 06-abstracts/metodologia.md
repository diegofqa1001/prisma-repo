# Extracción de abstracts y DOI nativo de Scopus — metodología

## Qué se hizo

Se navegó directamente la interfaz de Scopus (no Crossref, no WoS) con la
ecuación de búsqueda documentada en
[`01-protocolo-busqueda/ecuaciones-busqueda.md`](../01-protocolo-busqueda/ecuaciones-busqueda.md),
en la vista de resultados (lista, 200 registros por página) que expone en
el DOM: título, autores, fuente, año, veces citado, el abstract completo
(colapsado visualmente bajo "Show abstract" pero presente en el HTML), y un
botón "View at Publisher" cuyo destino es el DOI resuelto por Scopus.

Para los 438 registros se extrajeron: título, autores, fuente, año, veces
citado, **abstract completo** y **DOI nativo de Scopus** (cuando el botón
"View at Publisher" estaba disponible).

Los 438 títulos extraídos coinciden exactamente (match 1:1, sin diferencias)
con los 438 títulos ya presentes en
[`02-exports-crudos/scopus_438_extraido.csv`](../02-exports-crudos/scopus_438_extraido.csv),
confirmando que se trata del mismo conjunto de resultados.

## Bug de alineación detectado y corregido (2026-08-07)

**Qué pasó:** la primera extracción (abstracts y, por separado, un primer
intento de DOI nativo) emparejaba dos listas obtenidas por separado del DOM
— `document.querySelectorAll('tr.TableItems_content__g7iNF')` (fila con
título/autores/fuente/año) y `document.querySelectorAll('tr.TableItems_footer__35snp')`
(fila siguiente, con el abstract y el botón "View at Publisher") — **por
posición en el array**, asumiendo que ambas listas tenían el mismo largo y
el mismo orden relativo.

Esa asunción es falsa: algunos registros (justamente los que tienen el
abstract vacío en Scopus) renderizan una fila `footer` **extra/duplicada**.
A partir de la primera duplicación, todos los emparejamientos por posición
quedan corridos en uno: el abstract y el DOI del registro *N* terminan
asociados al título del registro *N+1*, en cascada, hasta el siguiente
desfase (o hasta el final de la página).

**Cómo se detectó:** al revisar manualmente un ejemplo concreto — el
registro *"Behaviorally informed deep reinforcement learning for
portfolio..."* (fuente: *Scientific Reports*) aparecía con abstract vacío y
DOI nulo, mientras el *siguiente* registro en la lista, *"Islamic Values and
Gen Z's Investment Behavior..."* (fuente: *Munaddhomah*, una revista sin
relación temática con deep reinforcement learning), aparecía con el
abstract y el DOI que evidentemente pertenecían al primero. Esa
inconsistencia (fuente/tema no coincide con el contenido del abstract) fue
la señal que disparó la revisión.

**Impacto medido:** al comparar la extracción corregida contra la original,
**429 de los 438 registros (98%)** tenían un abstract distinto al
correcto — es decir, el desfase de una posición se propagó a casi todo el
corpus desde el primer registro con footer duplicado. De esos 429, en 3
casos el abstract original estaba vacío (registros sin resumen indexado en
Scopus) y quedó completado en la versión corregida; en los otros 426, el
texto estaba simplemente desplazado a un título vecino.

Esto también afectó el análisis exploratorio (`analisis-preliminar.md`):
la distribución por año no se vio afectada (viene de la fila de contenido,
no de la de abstract), pero la señal de contaminación temática sísmica sí
cambió de forma material (de 24 a 15 registros con términos sísmicos, de 4
a 10 casos de ruido puro) porque algunos títulos financieros habían quedado
marcados falsamente como contaminados y viceversa. El detalle está en
`analisis-preliminar.md`, sección 3.

**Corrección aplicada:** se reemplazó el emparejamiento por índice de
array por emparejamiento **por relación de hermano en el DOM**
(`contentRow.nextElementSibling`, verificando que tenga la clase de
footer esperada). Esto es inmune a filas duplicadas porque solo mira el
hermano inmediato de cada fila de contenido, sin depender de la posición
global en ninguna lista. Con esta corrección se repitió la extracción
completa de los tres páginas (200 + 200 + 38 registros) y se verificó:

- 438/438 títulos coinciden exactamente con `scopus_all_438.json` (el
  primer listado, extraído solo con título/autores/fuente/año/citedBy, no
  afectado por el bug porque no dependía de la fila de footer).
- 438/438 registros quedaron con abstract no vacío.
- 407/438 registros (92.9%) quedaron con DOI nativo de Scopus (el resto no
  tiene botón "View at Publisher" disponible en la interfaz).

El archivo `scopus_438_abstracts.json` que acompaña este repositorio ya
corresponde a la versión corregida. Una versión anterior de este archivo,
con el bug descrito arriba, fue distribuida brevemente antes de detectarse
el error; si alguien conserva una copia previa a 2026-08-07, debe
descartarla.

## DOI nativo de Scopus: cómo se extrajo

El botón "View at Publisher" no tiene un atributo `href` — es un manejador
`onClick` de React que abre la URL de destino mediante `window.open()`.
Para capturar esa URL sin abrir cientos de pestañas físicas, se
sobrescribió temporalmente `window.open` antes de simular el clic:

```js
let captured = null;
const origOpen = window.open;
window.open = (url) => { captured = url; return { closed: true, close() {} }; };
publisherButton.click();
const doiUrl = captured;
window.open = origOpen;
```

Las URL capturadas tienen la forma
`https://doi.unalproxy.elogim.com/10.xxxx/...` (resolución vía el proxy
institucional). El DOI nativo se obtiene quitando el prefijo del dominio
proxy (todo lo anterior a `.com/`).

**Propósito de esta extracción:** verificación cruzada, no reemplazo. El
DOI nativo de Scopus se agrega como columna adicional (`doi_native_scopus`
en `PRISMA_master_final.csv`, ver `scripts/merge_native_doi.py`) junto a
una columna `doi_agreement` que compara ese valor contra el DOI ya resuelto
por Crossref o tomado del `.bib` de WoS (columna `doi`). Resultado sobre
los 560 registros:

| doi_agreement | n | % |
|---|---|---|
| MATCH | 373 | 66.6% |
| NO_NATIVE (registro sin botón "View at Publisher") | 153 | 27.3% |
| NO_DOI (sin DOI resuelto previamente) | 23 | 4.1% |
| MISMATCH | 11 | 2.0% |

Los 11 casos `MISMATCH` están documentados en la salida de
`scripts/merge_native_doi.py` y quedan marcados para revisión manual en
`PRISMA_master_final.csv`. La mayoría corresponde a que el DOI resuelto por
Crossref apuntaba a una versión preprint (p.ej. `10.2139/ssrn.xxxxxxx`,
SSRN) mientras el DOI nativo de Scopus apunta a la versión publicada final
— un hallazgo útil en sí mismo, ya que para la bibliografía de la tesis
corresponde preferir la versión publicada (el DOI nativo de Scopus) sobre
el preprint.

## Cobertura

| Origen | Registros | Con abstract | Con DOI nativo |
|---|---|---|---|
| Scopus only | 271 | sí (Scopus UI) | parcial (ver arriba) |
| Scopus + WoS | 167 | sí (Scopus UI) | parcial (ver arriba) |
| WoS only | 122 | sí (`.bib` de WoS, ver abajo) | no aplica (no está en Scopus) |
| **Total (`PRISMA_master_final.csv`)** | **560** | **560 (100%)** | **407 (72.7%)** |

De los 438 registros con origen Scopus, los 438 tienen texto de abstract
tras la corrección (3 quedaron con abstract vacío en la extracción
original por no tener resumen indexado en Scopus — ver bug arriba; se
recuperaron en la re-extracción y resultaron efectivamente vacíos también,
confirmando que no era un artefacto del bug sino falta real de resumen en
la fuente).

Los 122 registros "WoS only" no tienen DOI nativo de Scopus (no están en
Scopus, no hay nada que extraer de esa interfaz), pero sí tienen abstract
desde 2026-08-12: el `.bib` original de WoS
(`02-exports-crudos/wos_289_savedrecs.bib`) trae un campo `Abstract` para
los 289 registros de ese origen (100%), extraído por
`scripts/extract_wos_abstracts.py` y fusionado por
`scripts/merge_wos_abstracts.py`. A diferencia de la extracción de Scopus,
este paso **sí es reproducible por script** — el abstract viene incluido
en el export estándar de WoS, no requiere navegar la interfaz.

## Archivos de datos

- [`scopus_438_abstracts.json`](scopus_438_abstracts.json): array de 438
  objetos `{title, authors, source, year, citedBy, abstract, doiUrl,
  doi_native_scopus}`, uno por registro Scopus, en el orden de extracción
  (paginado de 200+200+38 en la vista de 200 resultados por página).
  `doiUrl` es la URL completa capturada (incluye el proxy institucional);
  `doi_native_scopus` es el DOI limpio derivado de esa URL.
- [`wos_289_abstracts.json`](wos_289_abstracts.json): array de 289 objetos
  `{wos_id, title, abstract}` extraídos directamente del `.bib` de WoS
  (sin automatización de navegador — parseo de texto plano).

## Reproducibilidad — limitación conocida (solo Scopus)

A diferencia del resto del pipeline (dedup, resolución DOI, abstracts de
WoS), la extracción de abstracts y DOI nativo **de Scopus** **no es
reproducible por script**: se hizo navegando manualmente la interfaz de
Scopus con automatización de navegador, leyendo el DOM directamente. No
hay una llamada de API pública equivalente disponible con las credenciales
institucionales usadas. Cualquier persona que audite este repositorio y
quiera reproducir ese paso debe repetir la búsqueda en Scopus (con acceso
institucional propio), extraer los campos `abstract` y el destino de "View
at Publisher" de cada registro, **emparejando cada fila de contenido con
su fila de footer por relación de hermano en el DOM (`nextElementSibling`),
no por posición en un array**, para evitar el bug descrito arriba. El
archivo `scopus_438_abstracts.json` se deja como evidencia congelada de lo
obtenido el 2026-08-07 (versión corregida).

Los abstracts de WoS (`wos_289_abstracts.json`), en cambio, sí son
reproducibles con un simple `python3 scripts/extract_wos_abstracts.py`
sobre el `.bib` crudo — no requieren automatización de navegador.

## Scripts de fusión

Orden de ejecución completo del pipeline de abstracts/DOI (después de
`merge_doi_resolution.py`):

1. `scripts/merge_abstracts.py` — fusiona el campo `abstract` de
   `scopus_438_abstracts.json` en `PRISMA_master_final.csv`, agregando las
   columnas `abstract` y `abstract_source` (`SCOPUS_UI` o `NOT_AVAILABLE`).
2. `scripts/extract_wos_abstracts.py` — parsea `wos_289_savedrecs.bib` y
   escribe `wos_289_abstracts.json`.
3. `scripts/merge_wos_abstracts.py` — completa `abstract`/`abstract_source`
   (`WOS_BIB`) para los registros que quedaron sin abstract en el paso 1
   (los 122 "WoS only").
4. `scripts/merge_native_doi.py` — fusiona `doi_native_scopus` y agrega la
   columna de verificación cruzada `doi_agreement`.
