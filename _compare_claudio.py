"""
Compara la lista de precios que envió Claudio (de Eurotextile) contra los precios
que tengo actualmente en la web Maully (products_eurotextile.json con +10%).

Output: tabla por consola y CSV con:
  Producto Claudio | Precio Claudio (CLP) | Precio Maully sugerido +10% | Producto en web | Precio web actual | Diferencia
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent

# ── Lista del WhatsApp de Claudio (transcrita del screenshot) ──
CLAUDIO = [
    ("adidas nike", "25KG", 555000),
    ("CAMISA MARCA OFERTA", "25KG", 365000),
    ("champion fila reebook puma", "25KG", 485000),
    ("CHAQ JEANS", "45KG", 280000),
    ("deportivo inv marca xl", "25KG", 490000),
    ("jeans marca retorno mujer 50 u", "25KG", 585000),
    ("JORDAN", "25KG", 815000),
    ("mix columbia inv oferta", "25KG", 485000),
    ("MIXTO FRIO ECO", "45KG", 290000),
    ("OUTDOR MARCA", "25KG", 625000),
    ("pantalon buzo marca ci", "25KG", 480000),
    ("pantalon buzo marca PREM", "25KG", 485000),
    ("pantalon raquelado marca", "25KG", 715000),
    ("parka chaq marca oferta", "25KG", 485000),
    ("polar marca ci", "25KG", 430000),
    ("polera dibujos animados", "25KG", 370000),
    ("poleron deportivo prem", "25KG", 375000),
    ("POLERON MARCA CI", "25KG", 480000),
    ("POLERON MARCA POLAR prem", "25KG", 490000),
    ("poleron polar", "45KG", 230000),
    ("poleron sin gorro", "45KG", 230000),
    ("realtree 1", "25KG", 420000),
    ("realtree 1 prem", "25KG", 435000),
    ("REMERA ADIDAS NIKE / OTRAS", "25KG", 615000),
    ("REMERA HOMBRE MULTIMARCA 1RA", "25KG", 625000),
    ("REMERA MARCA algodón y vestir oferta", "25KG", 330000),
    ("REMERA MARCA deportiva 1ra", "25KG", 545000),
    ("REMERA MARCA ml hombre 1RA", "25KG", 430000),
    ("REMERA MARCA ml hombre oferta", "25KG", 330000),
    ("sweter hombre marca", "25KG", 450000),
    ("sweter printed hombre", "45KG", 385000),
    ("under armour", "25KG", 535000),
    ("POLERON CON GORRO MARCA ANT", "25KG", 495000),
    ("POLERON CON GORRO MARCA NEW", "25KG", 495000),
]

MARGIN = 1.10

def norm(s):
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def round_100(x):
    return int(round(x / 100.0)) * 100

# ── Carga catálogo Maully actual ──
maully = json.loads((ROOT / "products_eurotextile.json").read_text(encoding="utf-8"))

def find_match(claudio_name, claudio_weight):
    """Busca el producto Maully más parecido por palabras + peso."""
    cn = norm(claudio_name)
    cw_kg = int(re.match(r"(\d+)", claudio_weight).group(1))
    tokens = set(t for t in cn.split() if len(t) > 2 and t not in {"con","sin","las","los","del","una","mas","ml"})
    best = None
    best_score = 0
    for p in maully:
        pn = norm(p["name"])
        pw_kg = int(re.match(r"(\d+)", p["weight"]).group(1)) if re.match(r"(\d+)", p["weight"]) else 0
        # Score = tokens en común
        ptokens = set(pn.split())
        common = tokens & ptokens
        score = len(common)
        # Bonus si peso coincide
        if pw_kg == cw_kg:
            score += 1.5
        elif abs(pw_kg - cw_kg) <= 5:
            score += 0.5
        if score > best_score:
            best_score = score
            best = p
    return best, best_score

# ── Comparación ──
print(f"{'Producto Claudio':<40} {'Peso':<6} {'Claudio':>10} {'+10% sug.':>10} | {'Match Maully':<45} {'Web':>10} {'Δ':>8}")
print("─" * 145)

rows = []
for name, weight, price_claudio in CLAUDIO:
    sug = round_100(price_claudio * MARGIN)
    match, score = find_match(name, weight)
    if match and score >= 2:
        web_price = match["price"]
        diff = web_price - sug
        diff_pct = (diff / sug * 100) if sug else 0
        match_name = match["name"][:43]
    else:
        web_price = 0
        diff = 0
        diff_pct = 0
        match_name = "(no encontrado)"
    sign = "+" if diff > 0 else ("−" if diff < 0 else " ")
    print(f"{name[:39]:<40} {weight:<6} {price_claudio:>10,} {sug:>10,} | {match_name:<45} {web_price:>10,} {sign}{abs(diff_pct):>5.1f}%")
    rows.append({
        "claudio_name": name,
        "weight": weight,
        "price_claudio": price_claudio,
        "price_sugerido_+10": sug,
        "maully_match_name": match_name if match and score >= 2 else "",
        "maully_web_price": web_price,
        "diff_pct_vs_sug": round(diff_pct, 1),
    })

# CSV para abrir en Excel
import csv
with open(ROOT / "_compare_claudio.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

# Resumen
nuevos = [r for r in rows if not r["maully_match_name"]]
mas_caros = [r for r in rows if r["maully_match_name"] and r["diff_pct_vs_sug"] > 5]
mas_baratos = [r for r in rows if r["maully_match_name"] and r["diff_pct_vs_sug"] < -5]

print()
print(f"Total productos en lista de Claudio: {len(CLAUDIO)}")
print(f"  - SIN match en web Maully (productos nuevos no listados): {len(nuevos)}")
print(f"  - Web cobra >5% MÁS que sugerencia +10%: {len(mas_caros)}")
print(f"  - Web cobra >5% MENOS que sugerencia +10% (subir): {len(mas_baratos)}")
print()
print("CSV: _compare_claudio.csv")
