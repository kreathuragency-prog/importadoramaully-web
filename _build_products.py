#!/usr/bin/env python3
"""
Importa los 255 productos de fardoseurotextile.com (WooCommerce Store API)
y genera:
  - products_eurotextile.json  -> data limpia para referencia
  - _products_js_block.js      -> bloque a pegar en script.js
  - _products_py_block.py      -> bloque a pegar en gen_catalogo.py

Reglas:
  - Precios = regular_price * 1.10, redondeado a $100
  - origPrice = regular_price * 1.10, sale_price * 1.10 si on_sale
  - Categoría: prioriza chaquetas/jeans/etc. en orden Maully
  - Tier: detectado del nombre (1RA, PREM, OFERTA, EXTRA)
  - Weight: regex \\d+\\s*kg
"""

import json
import re
import html
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
MARGIN = 1.15  # +15% (regla oficial Maully sobre precios Eurotextile)

# ── Carga datos ──
products_raw = []
for page in [1, 2, 3]:
    f = ROOT / f"_tmp_wc_p{page}.json"
    products_raw.extend(json.loads(f.read_text(encoding="utf-8")))

print(f"Total productos descargados: {len(products_raw)}")

# ── Mapeos ──

# Slug Eurotextile -> Maully cat (prioridad: las primeras matchean primero)
CAT_PRIORITY = [
    ("ski",                       "ski"),
    ("jeans-denim-mezclilla",     "jeans"),
    ("chaquetas-parkas",          "chaquetas"),
    ("polerones-polar",           "polerones"),
    ("poleras-blusas-camisas",    "poleras"),
    ("vestidos-faldas",           "vestidos"),
    ("sweater-chalecos",          "sweaters"),
    ("deportivo-outdoor",         "deportiva"),
    ("hogar",                     "hogar"),
    ("ninos-ninas",               "ninos"),
]

TIER_RULES = [
    (r"\bEXTRA\b",                  "extra",   "extra"),
    (r"\bPREM(IUM)?\b|\b1RA\s*PREM", "premium", "premium"),
    (r"\bOFERTA\b",                 "oferta",  "oferta"),
    (r"\b1RA\b|\bPRIMERA\b",        "primera", "primera"),
]


def strip_html(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def clean_name(name: str) -> str:
    """Title-case respetando palabras técnicas + tildes/ñ correctos."""
    name = strip_html(name).strip()
    # Tokens que quedan en mayúscula
    keep_upper = {"1RA", "2DA", "PREM", "EXTRA", "MIX", "CK", "NF", "GAP",
                  "USA", "UK", "EU", "XL", "XXL", "USD", "CLP", "DEP"}
    # Restauración tildes/ñ (palabras frecuentes en nombres)
    spanish_fixes = {
        "Nino": "Niño", "Ninos": "Niños", "Nina": "Niña", "Ninas": "Niñas",
        "Canada": "Canadá", "Sudamerica": "Sudamérica",
        "Polizon": "Polizón", "Algodon": "Algodón", "Termico": "Térmico",
        "Termicos": "Térmicos", "Pantalon": "Pantalón", "Chaqueton": "Chaquetón",
        "Cinturon": "Cinturón", "Calzon": "Calzón", "Polizon": "Polizón",
        "Anos": "Años",
    }
    out = []
    for w in name.split():
        if w.upper() in keep_upper:
            out.append(w.upper())
        elif re.fullmatch(r"\d+\s*KG|\d+KG", w, re.IGNORECASE):
            out.append(w.upper())
        elif w.upper() == "KG":
            out.append("Kg")
        else:
            cap = w.capitalize()
            out.append(spanish_fixes.get(cap, cap))
    return " ".join(out)


def detect_tier(name: str):
    n = name.upper()
    for pat, tier, badge in TIER_RULES:
        if re.search(pat, n):
            return tier, badge
    return "primera", "primera"  # default


def detect_weight(name: str):
    m = re.search(r"(\d{1,3})\s*KG", name.upper())
    return f"{m.group(1)}kg" if m else "20kg"


def detect_category(slugs, name):
    s = set(slugs)
    n = name.lower()
    # Prioridad por slug
    for euro_slug, maully in CAT_PRIORITY:
        if euro_slug in s:
            return maully
    # Fallback por nombre
    if "jeans" in n or "mezclilla" in n or "denim" in n:
        return "jeans"
    if "ski" in n or "snowboard" in n:
        return "ski"
    if "chaqueta" in n or "parka" in n or "abrigo" in n or "cortaviento" in n or "gamulan" in n:
        return "chaquetas"
    if "poleron" in n or "polerón" in n or "polar" in n or "hoodie" in n:
        return "polerones"
    if "polera" in n or "blusa" in n or "camisa" in n or "tshirt" in n or "t-shirt" in n:
        return "poleras"
    if "vestido" in n or "falda" in n:
        return "vestidos"
    if "sweater" in n or "chaleco" in n:
        return "sweaters"
    if "calzado" in n or "zapato" in n or "zapatilla" in n or "bota" in n:
        return "calzado"
    if "niño" in n or "nino" in n or "kid" in n or "infantil" in n:
        return "ninos"
    return "deportiva"


def round_price(p):
    """Redondea a múltiplo de $100 para precios limpios."""
    return int(round(p / 100.0)) * 100


# ── Procesa cada producto ──
processed = []
seen_names = set()
skipped_no_price = 0
skipped_dup = 0

for p in products_raw:
    if p.get("status") and p.get("status") != "publish":
        continue
    name_raw = strip_html(p.get("name", ""))
    if not name_raw:
        continue

    cat_slugs = [c.get("slug", "") for c in p.get("categories", [])]
    cat = detect_category(cat_slugs, name_raw)

    prices = p.get("prices") or {}
    try:
        reg = int(prices.get("regular_price") or 0)
        sale = int(prices.get("sale_price") or 0) if p.get("on_sale") else 0
    except (ValueError, TypeError):
        reg = sale = 0
    if reg <= 0:
        skipped_no_price += 1
        continue

    # +10% margin sobre el precio actual de Eurotextile (sale_price si está en oferta, sino regular)
    base_price = sale if (sale and sale > 0 and sale < reg) else reg
    price = round_price(base_price * MARGIN)
    orig_price = round_price(reg * MARGIN) if (sale and sale < reg) else round_price(reg * MARGIN * 1.15)

    name_clean = clean_name(name_raw)
    if name_clean.lower() in seen_names:
        skipped_dup += 1
        continue
    seen_names.add(name_clean.lower())

    tier, badge = detect_tier(name_raw)
    weight = detect_weight(name_raw)
    desc = strip_html(p.get("short_description") or p.get("description") or "")
    desc = re.sub(r"^\s*" + re.escape(name_raw) + r"\.?\s*", "", desc, flags=re.IGNORECASE).strip()
    if not desc:
        desc = f"Fardo de {weight} - Selección {tier}"

    # Flag PREMIUM: productos con keywords premium/crema/primera/marca/marcas
    # o calzado (todos), o tier premium/extra/primera, o "1ra" en nombre/desc
    full_text = (name_clean + " " + (desc or "")).lower()
    premium_kw = any(k in full_text for k in ["premium", "crema", "primera", "marca", "marcas",
                                               "columbia", "northface", "north face", "nike", "adidas",
                                               "calvin klein", "ck ", "tommy", "levis", "ugg", "patagonia",
                                               "1ra", "1ra+", "extra"])
    # Excluir explícitamente productos de OFERTA pura
    is_only_oferta = "oferta" in full_text and not premium_kw
    is_premium = (
        (premium_kw or cat == "calzado" or tier in ("premium", "extra", "primera"))
        and not is_only_oferta
    )

    processed.append({
        "cat": cat,
        "name": name_clean,
        "desc": desc[:300],
        "price": price,
        "origPrice": orig_price,
        "weight": weight,
        "tier": tier,
        "badge": badge,
        "isNew": bool(p.get("on_sale")),
        "premium": is_premium,
    })

# Ordenar: primero por categoría (orden Maully), luego por precio
CAT_ORDER = ["chaquetas", "jeans", "poleras", "polerones", "deportiva",
             "sweaters", "vestidos", "ski", "ninos", "hogar", "calzado", "plussize"]
def cat_key(p):
    try:
        return CAT_ORDER.index(p["cat"])
    except ValueError:
        return 99
processed.sort(key=lambda p: (cat_key(p), p["price"]))

# Asignar IDs incrementales
for i, p in enumerate(processed, start=1):
    p["id"] = i

print(f"Procesados: {len(processed)}")
print(f"Saltados sin precio: {skipped_no_price}, duplicados: {skipped_dup}")

# Resumen por categoría
from collections import Counter
cnt = Counter(p["cat"] for p in processed)
print("\nDistribución por categoría:")
for c, n in cnt.most_common():
    print(f"  {c:12s} {n:3d}")

# ── 1. JSON limpio ──
(ROOT / "products_eurotextile.json").write_text(
    json.dumps(processed, ensure_ascii=False, indent=2), encoding="utf-8"
)

# ── 2. Bloque JS para script.js ──
def js_escape(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

js_lines = ["let products = ["]
for p in processed:
    js_lines.append(
        f"  {{id:{p['id']},cat:'{p['cat']}',name:'{js_escape(p['name'])}',"
        f"desc:'{js_escape(p['desc'])}',"
        f"price:{p['price']},origPrice:{p['origPrice']},"
        f"weight:'{p['weight']}',tier:'{p['tier']}',badge:'{p['badge']}',"
        f"isNew:{'true' if p['isNew'] else 'false'},"
        f"premium:{'true' if p['premium'] else 'false'},img:MAULLY_IMG}},"
    )
js_lines.append("];")
(ROOT / "_products_js_block.js").write_text("\n".join(js_lines), encoding="utf-8")

# ── 3. Bloque Python para gen_catalogo.py ──
py_lines = ["products = ["]
for p in processed:
    new_flag = ',"new":True' if p["isNew"] else ""
    name_safe = p["name"].replace('"', '\\"')
    # Conservar tildes/ñ - el PDF ahora usa fuente Unicode (DejaVuSans)
    py_lines.append(
        f'    {{"cat":"{p["cat"]}","name":"{name_safe}","price":{p["price"]},'
        f'"weight":"{p["weight"]}","tier":"{p["tier"]}"{new_flag}}},'
    )
py_lines.append("]")
(ROOT / "_products_py_block.py").write_text("\n".join(py_lines), encoding="utf-8")

print("\nGenerado:")
print("  products_eurotextile.json")
print("  _products_js_block.js")
print("  _products_py_block.py")
