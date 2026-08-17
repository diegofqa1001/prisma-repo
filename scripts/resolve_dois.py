#!/usr/bin/env python3
"""
Resuelve el DOI de los registros 'Scopus only' de PRISMA_master_final.csv
contra la API pública de Crossref (sin autenticación), por búsqueda de título.

Uso:
    python3 scripts/resolve_dois.py

Salida:
    04-resolucion-doi/crossref_resolution.json
    (checkpoint incremental — se puede interrumpir y reanudar sin perder avance)

Clasificación de cada resultado:
    VERIFIED   - similitud de título >= 0.90 contra el mejor candidato de Crossref
    UNCERTAIN  - similitud entre 0.75 y 0.90 (revisar manualmente)
    NOT_FOUND  - sin candidato razonable (similitud < 0.75 o sin resultados)
"""
import json
import os
import re
import time
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = ROOT / "PRISMA_master_final.csv"
CKPT = ROOT / "04-resolucion-doi" / "crossref_resolution.json"

CONTACT_EMAIL = "diego.fqa@gmail.com"  # requerido por la polite pool de Crossref


def normalize_title(t):
    t = t.lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def main():
    import csv

    with open(MASTER_CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    targets = [r for r in rows if r["origin"] == "Scopus only"]

    results = {}
    if CKPT.exists():
        results = json.load(open(CKPT))

    remaining = [r for r in targets if r["title"] not in results]
    print(f"Total a resolver: {len(targets)}, ya resueltos: {len(results)}, "
          f"pendientes: {len(remaining)}")

    session = requests.Session()
    session.headers.update({
        "User-Agent": f"PRISMA-review-tool/1.0 (mailto:{CONTACT_EMAIL})"
    })

    for i, r in enumerate(remaining):
        title = r["title"]
        try:
            resp = session.get(
                "https://api.crossref.org/works",
                params={"query.bibliographic": title, "rows": 3},
                timeout=15,
            )
            resp.raise_for_status()
            items = resp.json()["message"]["items"]
        except Exception as e:
            results[title] = {"doi": "", "status": "ERROR", "match_ratio": 0,
                               "detail": str(e)}
            continue

        norm_target = normalize_title(title)
        best, best_ratio = None, 0
        for it in items:
            cand_titles = it.get("title", [])
            if not cand_titles:
                continue
            ratio = SequenceMatcher(None, norm_target,
                                     normalize_title(cand_titles[0])).ratio()
            if ratio > best_ratio:
                best_ratio, best = ratio, it

        if best and best_ratio >= 0.90:
            status = "VERIFIED"
        elif best and best_ratio >= 0.75:
            status = "UNCERTAIN"
        else:
            status = "NOT_FOUND"

        # DOI solo se registra si el candidato pasó el umbral de confianza
        # (>= 0.75). Un candidato de baja similitud NO debe aportar su DOI:
        # es casi seguro un artículo distinto.
        results[title] = {
            "doi": best.get("DOI", "") if (best and status != "NOT_FOUND") else "",
            "status": status,
            "match_ratio": round(best_ratio, 3) if best else 0,
            "crossref_title": best.get("title", [""])[0] if best else "",
        }

        if (i + 1) % 20 == 0:
            json.dump(results, open(CKPT, "w"), ensure_ascii=False, indent=1)
            print(f"{i + 1}/{len(remaining)} procesados, checkpoint guardado")

        time.sleep(0.15)  # cortesía con la API pública de Crossref

    json.dump(results, open(CKPT, "w"), ensure_ascii=False, indent=1)
    statuses = {}
    for v in results.values():
        statuses[v["status"]] = statuses.get(v["status"], 0) + 1
    print("DONE:", statuses)


if __name__ == "__main__":
    main()
