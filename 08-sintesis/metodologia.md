# 08 — Síntesis temática a nivel de resumen (PRISMA 2020, fase de extracción y síntesis)

**Fecha de ejecución:** 2026-09-02. **Insumo:** los 343 registros con `cribado_decision_final = INCLUDE` en `PRISMA_master_final.csv` (cribado título/resumen del 2026-08-12, casos inciertos resueltos el 2026-08-16, validación Kappa = 0,799 en `07-cribado/validacion.md`).

## Qué responde esta fase

El Capítulo 3 de la tesis afirma que la revisión sistemática identificó catorce dimensiones conductuales candidatas y las redujo a siete mediante tres criterios (independencia empírica, operacionalizabilidad, relevancia para la recomendación). Hasta esta fecha esa síntesis no tenía un artefacto auditable. Esta carpeta lo aporta: una codificación registro por registro de los 343 resúmenes incluidos contra un libro de códigos fijado de antemano (`libro_de_codigos.md`), con doble codificación independiente, medida de acuerdo y adjudicación de desacuerdos.

## Procedimiento

1. **Libro de códigos previo.** Catorce dimensiones candidatas (D1–D14) en cuatro dominios, más cinco metadatos (tipo de estudio, población, región, activo, si el estudio propone una tipología). Las siete retenidas en la tesis son D1, D4, D5, D7, D8, D10 y D12; las siete descartadas, D2, D3, D6, D9, D11, D13 y D14. La percepción del riesgo se codifica dentro de D1 por decisión declarada.
2. **Doble codificación independiente asistida por IA.** Dos pasadas (A y B) sobre los 343 registros, ejecutadas por instancias independientes del mismo modelo de lenguaje, con particiones distintas (A: orden secuencial; B: orden aleatorio, semilla 42) para impedir que una pasada condicione a la otra. Regla: codificar solo lo que el resumen examina, mide o modela explícitamente.
3. **Acuerdo entre codificadores.** Kappa de Cohen por dimensión sobre los 343 registros (columna `kappa_AB` en `tabla_dimensiones_candidatas.csv`): entre 0,764 (D14) y 0,959 (D5); trece de catorce dimensiones con Kappa ≥ 0,80 ("casi perfecto" según Landis y Koch, 1977); acuerdo bruto ≥ 0,95 en todas. Metadatos: tipo 0,904, población 0,898, activo 0,942, propone tipología 0,950.
4. **Adjudicación.** Los 149 registros con al menos un desacuerdo (78 en dimensiones, el resto solo en metadatos) fueron adjudicados por una tercera instancia de mayor capacidad, con acceso al resumen y a ambas codificaciones, y con el motivo de la decisión registrado (`adjudicacion_149.json`, campo `notas`). Los 194 restantes se tomaron por consenso.
5. **Salidas.** `codificacion_final_343.csv` (una fila por registro, D1–D14 binarias, metadatos, fuente consenso/adjudicado), `matriz_evidencia.json` (DOI de los estudios que sustentan cada dimensión), `phi_dimensiones_retenidas.csv` (coeficiente φ entre las siete retenidas) y las tablas de frecuencia.

## Resultados principales

| Código | Dimensión | n | % de 343 | Kappa | Decisión |
|---|---|---:|---:|---:|---|
| D1 | Tolerancia / percepción del riesgo | 189 | 55,1 | 0,924 | Retenida |
| D5 | Aversión a la pérdida / teoría prospectiva | 153 | 44,6 | 0,959 | Retenida |
| D6 | Otros sesgos cognitivos | 102 | 29,7 | 0,874 | Descartada |
| D3 | Exceso de confianza | 98 | 28,6 | 0,934 | Descartada |
| D12 | Influencia social percibida / manada | 96 | 28,0 | 0,949 | Retenida |
| D2 | Alfabetización financiera | 58 | 16,9 | 0,947 | Descartada |
| D7 | Emociones y regulación emocional | 48 | 14,0 | 0,849 | Retenida |
| D14 | Susceptibilidad mediática / información | 21 | 6,1 | 0,764 | Descartada |
| D11 | Valores culturales / identidad | 14 | 4,1 | 0,807 | Descartada |
| D9 | Experiencia inversora | 13 | 3,8 | 0,914 | Descartada |
| D8 | Horizonte de inversión | 12 | 3,5 | 0,853 | Retenida |
| D4 | Autoeficacia financiera | 9 | 2,6 | 0,872 | Retenida |
| D13 | Redes sociales y pares | 7 | 2,0 | 0,765 | Descartada |
| D10 | Tolerancia a la ambigüedad | 6 | 1,7 | 0,922 | Retenida |

Promedio de 2,41 dimensiones por resumen. Tipo de estudio: encuesta 157, datos transaccionales 47, computacional/ML 41, teórico 30, revisión 28, mixto 25, experimento 15. Población: minoristas 197, mixta/no especificada 138, estudiantes 4, asesores 4. Solo 40 de 343 estudios (11,7 %) proponen o validan una tipología o segmentación de inversionistas. Regiones con dato: India 66, China 15, Estados Unidos 12, Indonesia 10; América Latina apenas 4 (todos de Brasil; ningún estudio con datos de Colombia), lo que confirma el vacío regional que motiva la validación con datos colombianos de los Capítulos 5 y 7.

## Lectura honesta de los resultados (lo que sí y lo que no sustenta el corpus)

- El corpus sustenta con fuerza tres de las siete dimensiones retenidas (D1, D5, D12) y de forma moderada una cuarta (D7).
- Tres dimensiones retenidas —autoeficacia financiera (D4), horizonte (D8) y tolerancia a la ambigüedad (D10)— son **infrecuentes en los resúmenes** (< 4 %). Su retención no se apoya en la frecuencia con que la literatura las estudia, sino en (i) su fundamento teórico (Bandura, 1977; Markowitz, 1952; Ellsberg, 1961), (ii) su exigencia regulatoria en los cuestionarios de idoneidad (MiFID II exige horizonte y capacidad; la SFC colombiana, perfil y horizonte) y (iii) su papel en el eje conceptual de la tesis (riesgo vs. incertidumbre). La escasez de D10 en la literatura de perfilamiento minorista es, de hecho, la brecha que la tesis explota.
- Dos de las justificaciones de descarte de la versión anterior del capítulo **no se sostienen empíricamente a nivel de resumen** y se reformulan: el exceso de confianza (D3) casi no co-ocurre con la autoeficacia (1 de 98), sino con la tolerancia al riesgo (32 de 98); y la alfabetización financiera (D2) es cinco veces más frecuente que la autoeficacia (58 vs. 9). El criterio de subsunción D2→D4 se mantiene por razón conceptual (lo que modula la decisión es la confianza en aplicar el conocimiento), no por solapamiento observado. La tesis lo declara así.
- La independencia empírica entre las siete retenidas se verifica en el corpus: |φ| ≤ 0,32 en todos los pares salvo D1–D5 (φ = −0,57), que indica que ambas se estudian en literaturas distintas (co-ocurrencia baja), no que midan lo mismo.

## Limitaciones declaradas

1. La extracción es a **nivel de resumen**, no de texto completo. PRISMA 2020 prevé la evaluación de elegibilidad a texto completo antes de la síntesis; esa fase requiere acceso institucional a los 343 textos y dos revisores humanos independientes, y sigue **pendiente**. Su ejecución podría reducir el número de estudios finalmente incluidos, pero no altera la identificación de las dimensiones candidatas, que es el uso que la tesis hace de esta revisión.
2. La codificación fue asistida por IA con doble pasada y adjudicación; no sustituye a dos revisores humanos. Se recomienda que el autor valide una submuestra aleatoria (p. ej., 35 registros, 10 %) antes de la sustentación; el archivo `codificacion_final_343.csv` está preparado para anotar esa validación en una columna adicional.
3. La percepción del riesgo se codificó junto con la tolerancia (D1); una futura versión puede separarlas.

## Reproducibilidad

Los archivos de esta carpeta son la evidencia congelada de la ejecución del 2026-09-02. Las tablas se regeneran con `python3 08-sintesis/build_sintesis_tables.py` a partir de `codificacion_final_343.csv`. La codificación en sí (pasadas A y B y adjudicación) no es reproducible por script determinista, del mismo modo que el cribado de `07-cribado/`; se conserva íntegra en `codificacion_pasadas_A_B.json` y `adjudicacion_149.json`.
