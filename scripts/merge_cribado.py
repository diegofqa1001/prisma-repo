#!/usr/bin/env python3
"""
Fusiona el resultado del cribado titulo/resumen (07-cribado/resultados-cribado.csv)
en PRISMA_master_final.csv, agregando las columnas 'cribado_decision_ia',
'cribado_criterio', 'cribado_motivo', 'cribado_decision_final' y
'cribado_resolucion'.

'cribado_decision_ia' es la decision original del cribado asistido por IA
(INCLUDE/EXCLUDE/UNCERTAIN, sin modificar). 'cribado_decision_final' es la
decision operativa (INCLUDE/EXCLUDE unicamente): para los registros que la
IA marco UNCERTAIN, el autor de la tesis tomo la decision final (ver
'cribado_resolucion'); para el resto, decision_final = decision_ia. Esta
separacion conserva la trazabilidad completa: se puede ver que propuso la
IA y que decidio finalmente el autor, sin sobrescribir nada.

El cribado en si NO es reproducible por script (requiere juicio de
contenido por registro, ver 07-cribado/metodologia.md) — este script solo
fusiona el resultado ya generado, de forma mecanica y reproducible.

Ejecutar al final del pipeline, despues de merge_native_doi.py:
    python3 scripts/dedup.py
    python3 scripts/resolve_dois.py
    python3 scripts/merge_doi_resolution.py
    python3 scripts/merge_abstracts.py
    python3 scripts/extract_wos_abstracts.py
    python3 scripts/merge_wos_abstracts.py
    python3 scripts/merge_native_doi.py
    python3 scripts/merge_cribado.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = ROOT / "PRISMA_master_final.csv"
CRIBADO_CSV = ROOT / "07-cribado" / "resultados-cribado.csv"

FIELDNAMES = [
    "title", "authors", "source_journal", "year", "doi",
    "doi_status", "doi_match_ratio", "origin", "scopusUrl", "wos_id",
    "abstract", "abstract_source", "doi_native_scopus", "doi_agreement",
    "cribado_decision_ia", "cribado_criterio", "cribado_motivo",
    "cribado_decision_final", "cribado_resolucion",
]


def main():
    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    with open(CRIBADO_CSV, encoding="utf-8-sig") as f:
        cribado_rows = list(csv.DictReader(f))

    if len(cribado_rows) != len(rows):
        raise SystemExit(
            f"ERROR: {len(rows)} filas en master vs {len(cribado_rows)} en "
            f"cribado — deben corresponder 1 a 1 en el mismo orden."
        )

    mismatches = 0
    for row, cribado in zip(rows, cribado_rows):
        if row["title"].strip() != cribado["title"].strip():
            mismatches += 1
        row["cribado_decision_ia"] = cribado["decision"]
        row["cribado_criterio"] = cribado["criterio"]
        row["cribado_motivo"] = cribado["motivo"]
        row["cribado_decision_final"] = cribado["decision_final"]
        row["cribado_resolucion"] = cribado["resolucion"]

    if mismatches:
        print(f"ADVERTENCIA: {mismatches} filas con titulo no identico "
              f"(diferencias de comillas/mayusculas, ver 07-cribado/metodologia.md); "
              f"se fusiono por posicion, que es la clave confiable.")

    rows = [{k: row.get(k, "") for k in FIELDNAMES} for row in rows]

    with open(MASTER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    counts_ia = Counter(r["cribado_decision_ia"] for r in rows)
    counts_final = Counter(r["cribado_decision_final"] for r in rows)
    print(f"Total: {len(rows)}")
    print("Decision IA (original):")
    for k, v in counts_ia.items():
        print(f"  {k}: {v} ({v/len(rows)*100:.1f}%)")
    print("Decision final (con resolucion del autor):")
    for k, v in counts_final.items():
        print(f"  {k}: {v} ({v/len(rows)*100:.1f}%)")
    print(f"Escrito: {MASTER_CSV}")


if __name__ == "__main__":
    main()
