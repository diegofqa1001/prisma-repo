#!/usr/bin/env python3
"""
Fusiona el resultado de resolve_dois.py (04-resolucion-doi/crossref_resolution.json)
de vuelta en PRISMA_master_final.csv, agregando las columnas doi_status y
doi_match_ratio, y completando el DOI de los registros 'Scopus only' que
Crossref sí pudo resolver.

Ejecutar en este orden:
    python3 scripts/dedup.py
    python3 scripts/resolve_dois.py
    python3 scripts/merge_doi_resolution.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = ROOT / "PRISMA_master_final.csv"
CKPT = ROOT / "04-resolucion-doi" / "crossref_resolution.json"

FIELDNAMES = [
    "title", "authors", "source_journal", "year", "doi",
    "doi_status", "doi_match_ratio", "origin", "scopusUrl", "wos_id",
]


def main():
    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    resolved = json.load(open(CKPT))

    for row in rows:
        if row["origin"] == "Scopus only":
            info = resolved.get(row["title"], {})
            row["doi"] = info.get("doi", "")
            row["doi_status"] = info.get("status", "NOT_ATTEMPTED")
            row["doi_match_ratio"] = info.get("match_ratio", 0)
        else:
            row["doi_status"] = "FROM_WOS"
            row["doi_match_ratio"] = 1.0 if row["doi"] else 0

    with open(MASTER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    with_doi = sum(1 for r in rows if r["doi"])
    print(f"Total: {len(rows)}, con DOI: {with_doi} ({with_doi/len(rows)*100:.1f}%), "
          f"sin DOI: {len(rows)-with_doi}")
    print(f"Escrito: {MASTER_CSV}")


if __name__ == "__main__":
    main()
