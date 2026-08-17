#!/usr/bin/env python3
"""
Extrae el campo Abstract del .bib original de Web of Science
(02-exports-crudos/wos_289_savedrecs.bib) para los 289 registros de origen
WoS, y lo guarda como 06-abstracts/wos_289_abstracts.json.

A diferencia de la extraccion de Scopus (06-abstracts/scopus_438_abstracts.json),
este paso SI es reproducible por script: el campo Abstract viene incluido en
el export .bib estandar de WoS, no requiere navegar la interfaz.

Uso:
    python3 scripts/extract_wos_abstracts.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = ROOT / "02-exports-crudos" / "wos_289_savedrecs.bib"
OUT_PATH = ROOT / "06-abstracts" / "wos_289_abstracts.json"


def extract_field(entry, field):
    """Extrae el valor de un campo BibTeX 'field = { ... }' respetando
    balance de llaves (algunos abstracts contienen llaves anidadas)."""
    m = re.search(re.escape(field) + r"\s*=\s*\{", entry)
    if not m:
        return ""
    start = m.end()
    depth = 1
    i = start
    while i < len(entry) and depth > 0:
        if entry[i] == "{":
            depth += 1
        elif entry[i] == "}":
            depth -= 1
        i += 1
    raw = entry[start : i - 1]
    # BibTeX envuelve lineas largas con saltos de linea + espacios; normalizar
    return re.sub(r"\s+", " ", raw).strip()


def main():
    content = BIB_PATH.read_text(encoding="utf-8")
    entries = re.split(r"\n(?=@\w+\{)", content)[1:]  # descarta preambulo/BOM

    records = []
    for e in entries:
        wos_id_m = re.match(r"@\w+\{\s*(WOS:\S+?)\s*,", e)
        wos_id = wos_id_m.group(1) if wos_id_m else ""
        title = extract_field(e, "Title")
        abstract = extract_field(e, "Abstract")
        records.append({"wos_id": wos_id, "title": title, "abstract": abstract})

    with_abs = sum(1 for r in records if r["abstract"].strip())
    print(f"Total registros WoS: {len(records)}, con abstract: {with_abs} "
          f"({with_abs/len(records)*100:.1f}%)")

    OUT_PATH.write_text(
        json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"Escrito: {OUT_PATH}")


if __name__ == "__main__":
    main()
