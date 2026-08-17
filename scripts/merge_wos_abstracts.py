#!/usr/bin/env python3
"""
Completa la columna 'abstract' en PRISMA_master_final.csv para los
registros que aun no tienen abstract (los 122 'WoS only', mas cualquier
registro con abstract vacio pese a tener wos_id), usando
06-abstracts/wos_289_abstracts.json (extraido del .bib de WoS, ver
scripts/extract_wos_abstracts.py).

No sobrescribe abstracts ya presentes (SCOPUS_UI tiene prioridad, ya que
Scopus expone el abstract completo en su interfaz para los 438 registros
de ese origen). Agrega 'WOS_BIB' como nuevo valor posible de
'abstract_source'.

Ejecutar despues de merge_abstracts.py y antes de merge_native_doi.py:
    python3 scripts/dedup.py
    python3 scripts/resolve_dois.py
    python3 scripts/merge_doi_resolution.py
    python3 scripts/merge_abstracts.py
    python3 scripts/extract_wos_abstracts.py
    python3 scripts/merge_wos_abstracts.py
    python3 scripts/merge_native_doi.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = ROOT / "PRISMA_master_final.csv"
WOS_ABSTRACTS_JSON = ROOT / "06-abstracts" / "wos_289_abstracts.json"

FIELDNAMES = [
    "title", "authors", "source_journal", "year", "doi",
    "doi_status", "doi_match_ratio", "origin", "scopusUrl", "wos_id",
    "abstract", "abstract_source",
]


def main():
    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    wos_records = json.load(open(WOS_ABSTRACTS_JSON, encoding="utf-8"))
    abs_by_wos_id = {r["wos_id"]: r["abstract"] for r in wos_records if r["wos_id"]}

    filled = 0
    for row in rows:
        if row.get("abstract", "").strip():
            continue  # ya tiene abstract (Scopus UI), no se toca
        wos_id = row.get("wos_id", "").strip()
        if wos_id and wos_id in abs_by_wos_id and abs_by_wos_id[wos_id].strip():
            row["abstract"] = abs_by_wos_id[wos_id].strip()
            row["abstract_source"] = "WOS_BIB"
            filled += 1
        else:
            row["abstract_source"] = "NOT_AVAILABLE"

    with_abstract = sum(1 for r in rows if r.get("abstract", "").strip())

    with open(MASTER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    print(f"Completados desde WoS .bib: {filled}")
    print(f"Total con abstract ahora: {with_abstract}/{len(rows)} "
          f"({with_abstract/len(rows)*100:.1f}%)")
    print(f"Escrito: {MASTER_CSV}")


if __name__ == "__main__":
    main()
