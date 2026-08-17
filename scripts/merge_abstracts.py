#!/usr/bin/env python3
"""
Fusiona los abstracts extraidos directamente de la interfaz de Scopus
(06-abstracts/scopus_438_abstracts.json) en PRISMA_master_final.csv,
agregando las columnas 'abstract' y 'abstract_source'.

Cobertura: los 438 registros con origen Scopus ('Scopus only' y
'Scopus + WoS') quedan con abstract nativo de Scopus. Los 122 registros
'WoS only' NO tienen abstract en esta version (no se accedio a Scopus para
ellos); quedan con abstract_source = 'NOT_AVAILABLE'. Ver
06-abstracts/metodologia.md para el detalle y como completarlos a futuro
usando el campo Abstract del .bib de WoS.

Ejecutar despues de merge_doi_resolution.py:
    python3 scripts/dedup.py
    python3 scripts/resolve_dois.py
    python3 scripts/merge_doi_resolution.py
    python3 scripts/merge_abstracts.py
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
    "abstract", "abstract_source",
]


def main():
    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    abstracts = json.load(open(ABSTRACTS_JSON, encoding="utf-8"))
    abs_by_title = {r["title"].strip(): r["abstract"] for r in abstracts}

    matched = 0
    for row in rows:
        title = row["title"].strip()
        if title in abs_by_title and abs_by_title[title].strip():
            row["abstract"] = abs_by_title[title].strip()
            row["abstract_source"] = "SCOPUS_UI"
            matched += 1
        else:
            row["abstract"] = ""
            row["abstract_source"] = "NOT_AVAILABLE"

    with open(MASTER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    print(f"Total: {len(rows)}, con abstract: {matched} "
          f"({matched/len(rows)*100:.1f}%), sin abstract: {len(rows)-matched}")
    print(f"Escrito: {MASTER_CSV}")


if __name__ == "__main__":
    main()
