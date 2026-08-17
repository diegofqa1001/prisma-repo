#!/usr/bin/env python3
"""
Fusiona el DOI nativo de Scopus (extraido directamente del boton "View at
Publisher" de la interfaz, ver 06-abstracts/metodologia.md) en
PRISMA_master_final.csv, agregando las columnas 'doi_native_scopus' y
'doi_agreement'.

Proposito: verificacion cruzada. El DOI nativo de Scopus NO reemplaza el DOI
ya resuelto (columna 'doi', proveniente de Crossref o del .bib de WoS) — se
agrega como columna adicional para que cualquier persona pueda comparar
ambas fuentes y detectar discrepancias, sin perder trazabilidad de cual DOI
vino de donde.

Cobertura: solo los 438 registros de origen Scopus pueden tener DOI nativo
(los 122 'WoS only' quedan con 'doi_native_scopus' vacio, igual que con el
abstract). De los 438, 407 (92.9%) tienen boton "View at Publisher" con URL
capturable; 31 no lo tienen en la interfaz (se detecta al observar el HTML,
no es un fallo de extraccion).

doi_agreement:
    MATCH     - doi (resuelto) y doi_native_scopus coinciden (normalizado a
                minusculas)
    MISMATCH  - ambos existen pero difieren -> requiere revision manual
    NO_NATIVE - el registro no tiene DOI nativo capturable en Scopus
    NO_DOI    - el registro no tiene ningun DOI resuelto (doi vacio)

Ejecutar despues de merge_abstracts.py:
    python3 scripts/dedup.py
    python3 scripts/resolve_dois.py
    python3 scripts/merge_doi_resolution.py
    python3 scripts/merge_abstracts.py
    python3 scripts/merge_native_doi.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = ROOT / "PRISMA_master_final.csv"
ABSTRACTS_JSON = ROOT / "06-abstracts" / "scopus_438_abstracts.json"

FIELDNAMES = [
    "title", "authors", "source_journal", "year", "doi",
    "doi_status", "doi_match_ratio", "origin", "scopusUrl", "wos_id",
    "abstract", "abstract_source", "doi_native_scopus", "doi_agreement",
]


def main():
    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    records = json.load(open(ABSTRACTS_JSON, encoding="utf-8"))
    native_by_title = {
        r["title"].strip(): r.get("doi_native_scopus", "").strip()
        for r in records
    }

    counts = {"MATCH": 0, "MISMATCH": 0, "NO_NATIVE": 0, "NO_DOI": 0}
    mismatches = []

    for row in rows:
        title = row["title"].strip()
        native = native_by_title.get(title, "")
        resolved = row.get("doi", "").strip()

        row["doi_native_scopus"] = native

        if not native:
            row["doi_agreement"] = "NO_NATIVE"
        elif not resolved:
            row["doi_agreement"] = "NO_DOI"
        elif native.lower() == resolved.lower():
            row["doi_agreement"] = "MATCH"
        else:
            row["doi_agreement"] = "MISMATCH"
            mismatches.append((title, resolved, native))

        counts[row["doi_agreement"]] += 1

    with open(MASTER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    print(f"Total: {len(rows)}")
    for k, v in counts.items():
        print(f"  {k}: {v} ({v/len(rows)*100:.1f}%)")
    if mismatches:
        print(f"\nMISMATCH ({len(mismatches)} registros) - revisar manualmente:")
        for title, resolved, native in mismatches:
            print(f"  - {title[:70]}")
            print(f"      resuelto: {resolved}  |  nativo Scopus: {native}")
    print(f"\nEscrito: {MASTER_CSV}")


if __name__ == "__main__":
    main()
