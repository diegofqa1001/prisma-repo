#!/usr/bin/env python3
"""
Deduplicación cruzada Scopus x WoS para la revisión PRISMA de perfiles de
riesgo conductual de inversionistas.

Entrada:
  02-exports-crudos/scopus_438_extraido.csv
  02-exports-crudos/wos_289_savedrecs.bib

Salida:
  PRISMA_master_dedup.csv  (560 registros únicos, columna 'origin' indica
                             si vino de Scopus, WoS, o ambos)

Metodología: ver 03-deduplicacion/metodologia.md
"""
import json
import re
import csv
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPUS_CSV = ROOT / "02-exports-crudos" / "scopus_438_extraido.csv"
WOS_BIB = ROOT / "02-exports-crudos" / "wos_289_savedrecs.bib"
OUT_CSV = ROOT / "PRISMA_master_final.csv"

FUZZY_THRESHOLD = 0.90


def normalize_title(t):
    t = t.lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def load_scopus():
    records = []
    with open(SCOPUS_CSV, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row["norm_title"] = normalize_title(row["title"])
            records.append(row)
    return records


def get_field(block, name):
    m = re.search(rf"{name}\s*=\s*\{{(.*?)\}},?\n(?=[A-Za-z-]+\s*=|\Z)", block, re.S)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return ""


def load_wos():
    text = open(WOS_BIB, encoding="utf-8-sig").read()
    raw_records = re.findall(r"@article\{\s*(WOS:\S+),(.*?)\n\}", text, re.S)
    records = []
    for wid, block in raw_records:
        rec = {
            "wos_id": wid,
            "title": get_field(block, "Title"),
            "authors": get_field(block, "Author"),
            "journal": get_field(block, "Journal"),
            "year": get_field(block, "Year"),
            "doi": get_field(block, "DOI"),
        }
        rec["norm_title"] = normalize_title(rec["title"])
        records.append(rec)
    return records


def dedup(scopus, wos):
    wos_by_norm = {}
    for r in wos:
        wos_by_norm.setdefault(r["norm_title"], []).append(r)

    master = []
    matched_wos_ids = set()

    for sr in scopus:
        match = None
        if sr["norm_title"] and sr["norm_title"] in wos_by_norm:
            match = wos_by_norm[sr["norm_title"]][0]
        else:
            # fuzzy fallback, blocked implicitly by full scan (small N here)
            best, best_ratio = None, 0
            for wr in wos:
                if wr["wos_id"] in matched_wos_ids:
                    continue
                ratio = SequenceMatcher(None, sr["norm_title"], wr["norm_title"]).ratio()
                if ratio > best_ratio:
                    best_ratio, best = ratio, wr
            if best and best_ratio >= FUZZY_THRESHOLD:
                match = best

        if match:
            matched_wos_ids.add(match["wos_id"])
            master.append({
                "title": sr["title"],
                "authors": match["authors"] or sr["authors"],
                "source_journal": match["journal"] or sr["source"],
                "year": match["year"] or sr["year"],
                "doi": match["doi"],
                "origin": "Scopus + WoS",
                "scopusUrl": sr["scopusUrl"],
                "wos_id": match["wos_id"],
            })
        else:
            master.append({
                "title": sr["title"],
                "authors": sr["authors"],
                "source_journal": sr["source"],
                "year": sr["year"],
                "doi": "",
                "origin": "Scopus only",
                "scopusUrl": sr["scopusUrl"],
                "wos_id": "",
            })

    for wr in wos:
        if wr["wos_id"] not in matched_wos_ids:
            master.append({
                "title": wr["title"],
                "authors": wr["authors"],
                "source_journal": wr["journal"],
                "year": wr["year"],
                "doi": wr["doi"],
                "origin": "WoS only",
                "scopusUrl": "",
                "wos_id": wr["wos_id"],
            })

    return master


def main():
    scopus = load_scopus()
    wos = load_wos()
    master = dedup(scopus, wos)

    print(f"Scopus: {len(scopus)}")
    print(f"WoS: {len(wos)}")
    print(f"Total identificados: {len(scopus) + len(wos)}")
    print(f"Duplicados eliminados: {len(scopus) + len(wos) - len(master)}")
    print(f"Únicos para cribado: {len(master)}")

    with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=[
            "title", "authors", "source_journal", "year", "doi",
            "origin", "scopusUrl", "wos_id",
        ])
        w.writeheader()
        w.writerows(master)
    print(f"Escrito: {OUT_CSV}")


if __name__ == "__main__":
    main()
