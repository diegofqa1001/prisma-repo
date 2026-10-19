# Diagrama de flujo PRISMA 2020 — estado actual

Cubre identificación, cribado por título y resumen (asistido por IA, con doble revisión humana independiente de la totalidad de las decisiones realizada el 19 de septiembre de 2026 por Diego Fernando Quintero Avellaneda y Jhon Wilder Sánchez Obando; ver `07-cribado/validacion.md`), elegibilidad a texto completo y síntesis temática.

Versión renderizada lista para incrustar en el capítulo metodológico (Word,
LaTeX, PowerPoint): [`prisma_diagrama.png`](prisma_diagrama.png) (raster,
alta resolución) o [`prisma_diagrama.svg`](prisma_diagrama.svg) (vectorial).
Ambas se generan con `08-sintesis/fig_3_4_prisma_flujo.py` (Figura 3.4 de la tesis); el código Mermaid de abajo es una versión esquemática equivalente.

```mermaid
flowchart TD
    A["Registros identificados en Scopus\n(n = 438)"] --> C["Total identificados\n(n = 727)"]
    B["Registros identificados en Web of Science\n(n = 289)"] --> C
    C --> D["Duplicados eliminados\n(cruce Scopus × WoS, título normalizado + similitud ≥ 0,90)\n(n = 167)"]
    C --> E["Registros únicos cribados (título y resumen)\n(n = 560)"]
    E --> F["Registros excluidos (n = 217)\n161 por criterios E1–E7, 48 inciertos\ny 8 incluidos que pasaron a excluidos tras la validación"]
    E --> G["Registros incluidos (nivel resumen)\n(n = 343)\nAcuerdo entre pasadas (20 %): κ = 0,799"]
    G --> H["Evaluación a texto completo\n(n = 343)"]
    H --> I["Síntesis temática: 343 codificados\n→ 7 dimensiones retenidas"]
```

## Tabla de conteos

| Fase | n | Fuente / script |
|---|---|---|
| Identificados — Scopus | 438 | `02-exports-crudos/scopus_438_extraido.csv` |
| Identificados — WoS | 289 | `02-exports-crudos/wos_289_savedrecs.bib` |
| Total identificados | 727 | suma directa |
| Duplicados eliminados | 167 | `scripts/dedup.py` → `03-deduplicacion/metodologia.md` |
| **Únicos para cribado** | **560** | `PRISMA_master_final.csv` |
| Excluidos en cribado título/resumen por criterio (IA, primera pasada) | 161 (28.8%) | `07-cribado/resultados-cribado.csv` |
| Inciertos (IA), resueltos EXCLUDE por el autor | 48 (8.6%) | `07-cribado/resultados-cribado.csv` (columna `resolucion`) |
| Desacuerdos IA-IA en validación por muestreo, resueltos EXCLUDE | 10 (de una muestra de 102): 8 eran INCLUDE en la primera pasada y 2 ya eran EXCLUDE, de modo que suman 8 excluidos nuevos | `07-cribado/validacion.md` |
| **Excluidos, total (decisión final)** | **217 (38.8%)** | `cribado_decision_final` en `PRISMA_master_final.csv` |
| **Incluidos (decisión final)** | **343 (61.3%)** | `cribado_decision_final` en `PRISMA_master_final.csv` |
| Evaluados a texto completo | 343 | doble revisión humana (`07-cribado/validacion.md`) |
| Incluidos en síntesis final | 343 | `08-sintesis/codificacion_final_343.csv` |

**Sobre la resolución de los 48 inciertos:** el cribado asistido por IA no
decidió esos 48 casos por ambigüedad genuina (población institucional vs.
individual, activo físico vs. financiero, constructo conductual mencionado
solo tangencialmente, etc. — ver `07-cribado/metodologia.md`). El autor de
la tesis revisó los motivos documentados para cada uno y aplicó la regla de exclusión del protocolo y **excluyó
los 48**: ante la duda sobre si un registro cumple los
criterios de población, constructo o alcance de activos definidos para la
taxonomía de la tesis, se prefiere un corpus más estricto y defendible
sobre uno más amplio pero con ajuste dudoso.

**Sobre la validación por muestreo:** se ejecutó una segunda pasada de
cribado, ciega e independiente, sobre una muestra estratificada del 20%
(102/512) de los registros que la IA sí había decidido. El acuerdo fue
90.2% (Kappa de Cohen = 0.799, "sustancial" según Landis & Koch). Los 10
desacuerdos se resolvieron con la misma regla de exclusión del protocolo (excluir ante
duda) — ver el detalle completo, la tabla de contingencia y la lista de
los 10 casos en `07-cribado/validacion.md`.

Ninguna de estas resoluciones sobrescribe la clasificación original de la
IA: la columna `cribado_decision_ia` en el CSV maestro conserva siempre la
propuesta original (`INCLUDE`/`EXCLUDE`/`UNCERTAIN`), y `cribado_resolucion`
documenta el motivo de cada ajuste — por si en una fase posterior conviene
reconsiderar alguno de estos 58 registros (48 + 10) que requirieron
resolución.

**Revisión humana:** el conteo de incluidos (343) es el definitivo. La validación por segunda pasada (Kappa 0.799) mide la consistencia IA-IA, y la doble revisión humana independiente que exige PRISMA 2020 la realizaron el 19 de septiembre de 2026 Diego Fernando Quintero Avellaneda y Jhon Wilder Sánchez Obando sobre la totalidad de las decisiones y sobre la elegibilidad a texto completo de los 343 registros — ver `07-cribado/validacion.md`.

Todo número de identificación/deduplicación es recalculable ejecutando
`scripts/dedup.py` sobre los archivos de `02-exports-crudos/`. Los conteos
de cribado no son recalculables por script (requieren juicio de contenido
por registro); `07-cribado/resultados-cribado.csv` es la evidencia
congelada del cribado del 2026-08-12, con la resolución de inciertos y de
la validación por muestreo del autor del 2026-08-16.
