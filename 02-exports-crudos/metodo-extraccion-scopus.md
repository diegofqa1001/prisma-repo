# Cómo se obtuvo el export de Scopus (`scopus_438_extraido.csv`, no redistribuido)

La función nativa "Export" de Scopus exige una cuenta personal de Elsevier
(distinta del acceso institucional por proxy), que no estaba disponible en el
momento de la extracción. En lugar de eso, los 438 registros se extrajeron
directamente de la interfaz de resultados (vista de tabla: título, autores,
revista/fuente, año, enlace del documento) mediante automatización de
navegador, paginando los 438 resultados en 3 páginas de hasta 200 registros
cada una.

**Esta vía no incluye el DOI nativo de Scopus.** Para completar esa columna
sin depender del CSV de exportación, el DOI de cada uno de los 271 registros
que quedaron exclusivamente en Scopus (es decir, sin coincidencia en el export
de WoS, que sí trae DOI nativo) se resolvió después contra la API pública de
Crossref por título — ver `04-resolucion-doi/`.

Cada registro se verificó campo por campo contra la interfaz visual de Scopus
antes de darse por válido (capturas de pantalla de verificación disponibles
bajo solicitud, no incluidas en este repositorio por tamaño).

No se modificó, corrigió, ni omitió ningún registro devuelto por la ecuación
de búsqueda — los 438 son exactamente los que Scopus devolvió.

## Redistribución

Los exports crudos de Scopus (`scopus_438_extraido.csv`) y de Web of Science
(`wos_289_completo.csv`, `wos_289_savedrecs.bib`) no se redistribuyen: los
términos de uso de Elsevier y Clarivate Analytics restringen la redistribución
de exports masivos y los resúmenes son contenido protegido por derechos de los
editores. Para reproducir los pasos 1 a 5 desde cero, el lector ejecuta las
ecuaciones de `01-protocolo-busqueda/` con su propio acceso institucional y
coloca aquí sus exports con esos nombres de archivo. Los metadatos
bibliográficos de identificación (título, autores, fuente, año, DOI e
identificador WoS) y todas las decisiones de deduplicación, resolución de DOI
y cribado se publican en `PRISMA_master_final.csv`.
