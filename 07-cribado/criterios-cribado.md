# Criterios de cribado título/resumen — PRISMA fase 2

Criterios formales para el cribado título/resumen de los 560 registros
únicos de `PRISMA_master_final.csv`, definidos **antes** de aplicar el
cribado, siguiendo la recomendación PRISMA 2020 de fijar los criterios de
elegibilidad de forma explícita y previa. Informados por el análisis
exploratorio de `06-abstracts/analisis-preliminar.md` (señal de
contaminación temática) y por las decisiones ya documentadas en
`01-protocolo-busqueda/ecuaciones-busqueda.md` (filtros de tipo de
documento e idioma deliberadamente diferidos a esta etapa).

## Decisiones metodológicas previas (confirmadas con el autor de la tesis)

- **Tipo de documento:** no se aplica como criterio de exclusión
  automático. Las actas de conferencia (56/438 registros Scopus, 12.8%) se
  evalúan por contenido igual que artículos de revista — el tipo de
  documento no determina relevancia temática.
- **Idioma:** no se aplica un filtro explícito de idioma. Solo 3/438
  títulos muestran script no latino (títulos bilingües), evaluados caso a
  caso por contenido.
- **Ejecución:** cribado completo asistido por IA sobre los 560 registros,
  con motivo documentado por registro (trazable), y los casos `UNCERTAIN`
  separados para decisión final del autor de la tesis.

## Criterios de inclusión (deben cumplirse todos)

- **I1 — Población:** el estudio trata sobre inversionistas individuales o
  minoristas (retail/individual investors), o sobre inversionistas en
  general cuando el objeto es la decisión de inversión en mercados
  financieros — no gestión de riesgo puramente corporativa/institucional.
- **I2 — Constructo conductual:** examina alguna dimensión de riesgo
  conductual del inversionista (tolerancia al riesgo, perfil de riesgo,
  percepción de riesgo, aversión a la pérdida, autoeficacia financiera,
  tolerancia a la ambigüedad, horizonte de inversión, regulación
  emocional, influencia social) u otros sesgos conductuales relacionados
  con la decisión de inversión (exceso de confianza, efecto manada, efecto
  disposición, anclaje, teoría de las perspectivas).
- **I3 — Marco:** aporta clasificación, tipología, perfilamiento,
  segmentación o taxonomía de inversionistas por riesgo conductual, **o**
  aporta evidencia empírica/teórica sustantiva sobre un constructo
  conductual de riesgo aplicable a inversionistas individuales — no es
  necesario que el estudio proponga una taxonomía explícita para calificar
  como literatura de soporte válida para el capítulo.
- **I4 — Alcance de activos:** el objeto de inversión son activos
  financieros (renta variable, criptoactivos, fondos, activos digitales) —
  no activos físicos ni de infraestructura.

## Criterios de exclusión (cualquiera de estos excluye)

- **E1 — Riesgo de infraestructura física:** ingeniería sísmica,
  estructural, geotécnica, o reaseguro de activos físicos, sin relación
  con perfiles conductuales de inversionistas.
- **E2 — Riesgo de sistemas energéticos/de red:** transición energética o
  riesgo de red eléctrica a nivel de sistema, sin ángulo de comportamiento
  del inversionista individual.
- **E3 — Ciberseguridad:** riesgo de red informática o ciberataques sin
  relación con decisiones de inversión.
- **E4 — Riesgo corporativo/institucional puro:** gestión de riesgo de la
  firma, riesgo crediticio corporativo, cadena de suministro, sin ángulo
  de comportamiento del inversionista individual.
- **E5 — Actuarial/seguros:** ratemaking, underwriting o clasificación de
  riesgo de pólizas, sin relación con comportamiento de inversión.
- **E6 — Fuera de dominio:** no trata sobre riesgo conductual ni sobre
  inversionistas/inversión en absoluto — falso positivo puro de la
  ecuación de búsqueda (polisemia de "portfolio", "risk profile",
  "classification").
- **E7 — Sin contenido sustantivo propio:** nota editorial, fe de erratas,
  retractación, comentario breve sin aporte de contenido propio.

## Categoría `UNCERTAIN`

Se marca `UNCERTAIN` (no se decide automáticamente) cuando:
- El abstract mezcla genuinamente dominio financiero y no financiero (p.ej.
  riesgo de cartera inmobiliaria con componente conductual explícito) y no
  es claro si el enfoque principal es la inversión financiera.
- El abstract disponible es demasiado corto o genérico para decidir con
  confianza razonable.
- El registro cumple los criterios de inclusión de forma marginal o
  discutible (p.ej. población mixta institucional/individual sin
  distinguir).

Todos los casos `UNCERTAIN` quedan documentados con su motivo en
`07-cribado/resultados-cribado.csv` para que el autor de la tesis tome la
decisión final — no se asume una resolución por defecto.

## Metodología de aplicación

Cribado ejecutado por lote sobre título + abstract de los 560 registros de
`PRISMA_master_final.csv`, aplicando los criterios anteriores registro por
registro, con motivo documentado citando el código de criterio
correspondiente (I1-I4 para inclusión, E1-E7 para exclusión). Resultado en
`07-cribado/resultados-cribado.csv` (columnas: `title`, `decision`
[`INCLUDE`/`EXCLUDE`/`UNCERTAIN`], `criterio`, `motivo`).

**Limitación declarada:** este cribado fue asistido por IA (no por dos
revisores humanos independientes como exige el estándar PRISMA para
minimizar sesgo), por lo que se reporta explícitamente como un cribado
preliminar. El autor de la tesis debe: (a) revisar todos los casos
`UNCERTAIN`, y (b) idealmente validar una muestra aleatoria de las
decisiones `INCLUDE`/`EXCLUDE` antes de usar el conteo final en el
diagrama de flujo PRISMA del capítulo metodológico.
