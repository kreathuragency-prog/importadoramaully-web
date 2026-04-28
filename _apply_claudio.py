"""
Aplica los precios y la metadata de ganchos de Claudio sobre el catálogo Maully:
- Actualiza precios de los 34 productos de la lista de Claudio (precio_costo * 1.10)
- Marca requires_ganchos: 0/1/2 según la lista
- Agrega los 3 productos NUEVOS (JORDAN, realtree 1, realtree 1 prem)
- Marca todos los premium/marca/segunda con gancho_eligible: true (pueden servir de gancho)
- Reinjecta arrays en script.js y gen_catalogo.py
"""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
MARGIN = 1.15

def round_100(x):
    return int(round(x / 100.0)) * 100

def norm(s):
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def find_match(maully_list, claudio_name, claudio_weight):
    cn = norm(claudio_name)
    cw_kg = int(re.match(r"(\d+)", claudio_weight).group(1))
    tokens = set(t for t in cn.split() if len(t) > 2 and t not in {"con","sin","las","los","del","una","mas","ml"})
    best = None
    best_score = 0
    best_idx = -1
    for i, p in enumerate(maully_list):
        pn = norm(p["name"])
        pw_kg = int(re.match(r"(\d+)", p["weight"]).group(1)) if re.match(r"(\d+)", p["weight"]) else 0
        ptokens = set(pn.split())
        common = tokens & ptokens
        score = len(common)
        if pw_kg == cw_kg:
            score += 1.5
        elif abs(pw_kg - cw_kg) <= 5:
            score += 0.5
        if score > best_score:
            best_score = score
            best = p
            best_idx = i
    return best, best_score, best_idx


def determine_cat(name):
    n = name.lower()
    if "jeans" in n or "denim" in n or "mezclilla" in n: return "jeans"
    if "ski" in n or "snowboard" in n: return "ski"
    if "chaqueta" in n or "parka" in n or "abrigo" in n or "cortaviento" in n: return "chaquetas"
    if "poleron" in n or "polar" in n or "hoodie" in n: return "polerones"
    if "polera" in n or "blusa" in n or "camisa" in n or "remera" in n: return "poleras"
    if "vestido" in n or "falda" in n: return "vestidos"
    if "sweater" in n or "sweter" in n or "chaleco" in n: return "sweaters"
    if "calzado" in n or "zapato" in n or "zapatilla" in n or "bota" in n or "jordan" in n: return "calzado"
    if "niño" in n or "nino" in n or "kid" in n: return "ninos"
    return "deportiva"


# ── Carga catálogo + Claudio ──
maully = json.loads((ROOT / "products_eurotextile.json").read_text(encoding="utf-8"))
claudio = json.loads((ROOT / "_claudio_prices.json").read_text(encoding="utf-8"))["productos"]

# ── Set defecto: gancho_eligible = true para premium/marca/primera/calzado ──
for p in maully:
    p["gancho_eligible"] = bool(p.get("premium"))  # ya lo calculamos antes
    p["requires_ganchos"] = 0

# ── Aplica precios y ganchos de Claudio ──
print("=== Aplicando lista Claudio ===")
nuevos = []
actualizados = 0
for c in claudio:
    if c.get("es_nuevo"):
        nuevos.append(c)
        continue
    match, score, idx = find_match(maully, c["name_claudio"], c["weight"])
    if match and score >= 2:
        nuevo_precio = round_100(c["price_costo"] * MARGIN)
        nuevo_orig = round_100(c["price_costo"] * MARGIN * 1.18)  # 18% extra para mostrar dcto
        viejo = match["price"]
        match["price"] = nuevo_precio
        match["origPrice"] = nuevo_orig
        match["requires_ganchos"] = c.get("ganchos", 0)
        match["gancho_eligible"] = match.get("gancho_eligible", False) or c.get("exclusivo", False)
        actualizados += 1
        delta = nuevo_precio - viejo
        sign = "+" if delta >= 0 else "−"
        print(f"  ✓ {c['name_claudio'][:40]:<40} ${viejo:>8,} → ${nuevo_precio:>8,} {sign}${abs(delta):>8,} | g={c.get('ganchos',0)}")
    else:
        print(f"  ✗ NO MATCH: {c['name_claudio']}")

print(f"\nActualizados: {actualizados}/{len(claudio) - len(nuevos)}")

# ── Agrega productos nuevos ──
print(f"\n=== Productos NUEVOS ({len(nuevos)}) ===")
next_id = max(p["id"] for p in maully) + 1
for c in nuevos:
    name = c["name_claudio"].title()
    if "jordan" in name.lower():
        name = "Jordan Calzado 25 Kg"
    elif "realtree 1 prem" in name.lower():
        name = "Realtree 1 Premium 25 Kg"
    elif "realtree 1" in name.lower():
        name = "Realtree 1 25 Kg"
    cat = determine_cat(name)
    nuevo = {
        "id": next_id,
        "cat": cat,
        "name": name,
        "desc": "Producto premium nuevo en catálogo. Selección directa con stock.",
        "price": round_100(c["price_costo"] * MARGIN),
        "origPrice": round_100(c["price_costo"] * MARGIN * 1.18),
        "weight": c["weight"],
        "tier": "premium",
        "badge": "premium",
        "isNew": True,
        "premium": True,
        "gancho_eligible": True,
        "requires_ganchos": c.get("ganchos", 0),
    }
    maully.append(nuevo)
    print(f"  + {name:<40} ${nuevo['price']:>8,} | g={nuevo['requires_ganchos']}")
    next_id += 1

# ── Stats finales ──
total = len(maully)
exclusivos_g1 = sum(1 for p in maully if p.get("requires_ganchos") == 1)
exclusivos_g2 = sum(1 for p in maully if p.get("requires_ganchos") == 2)
elegibles = sum(1 for p in maully if p.get("gancho_eligible"))
print(f"\n=== STATS ===")
print(f"Total productos: {total}")
print(f"Requieren 1 gancho: {exclusivos_g1}")
print(f"Requieren 2 ganchos: {exclusivos_g2}")
print(f"Pueden ser ganchos (elegibles): {elegibles}")

# ── Guarda JSON limpio ──
(ROOT / "products_eurotextile.json").write_text(
    json.dumps(maully, ensure_ascii=False, indent=2), encoding="utf-8"
)

# ── Genera bloques JS y Python ──
def js_escape(s):
    return s.replace("\\", "\\\\").replace("'", "\\'")

js_lines = ["let products = ["]
for p in maully:
    js_lines.append(
        f"  {{id:{p['id']},cat:'{p['cat']}',name:'{js_escape(p['name'])}',"
        f"desc:'{js_escape(p.get('desc',''))}',"
        f"price:{p['price']},origPrice:{p['origPrice']},"
        f"weight:'{p['weight']}',tier:'{p['tier']}',badge:'{p['badge']}',"
        f"isNew:{'true' if p.get('isNew') else 'false'},"
        f"premium:{'true' if p.get('premium') else 'false'},"
        f"ganchos:{p.get('requires_ganchos', 0)},"
        f"esGancho:{'true' if p.get('gancho_eligible') else 'false'},"
        f"img:MAULLY_IMG}},"
    )
js_lines.append("];")
(ROOT / "_products_js_block.js").write_text("\n".join(js_lines), encoding="utf-8")

py_lines = ["products = ["]
for p in maully:
    new_flag = ',"new":True' if p.get("isNew") else ""
    g = p.get("requires_ganchos", 0)
    g_flag = f',"ganchos":{g}' if g > 0 else ""
    name_safe = p["name"].replace('"', '\\"')
    py_lines.append(
        f'    {{"cat":"{p["cat"]}","name":"{name_safe}","price":{p["price"]},'
        f'"weight":"{p["weight"]}","tier":"{p["tier"]}"{new_flag}{g_flag}}},'
    )
py_lines.append("]")
(ROOT / "_products_py_block.py").write_text("\n".join(py_lines), encoding="utf-8")

# ── Reinjecta en script.js y gen_catalogo.py ──
js = (ROOT / "script.js").read_text(encoding="utf-8")
js_new = re.sub(r'let products = \[.*?\n\];', (ROOT / "_products_js_block.js").read_text(encoding="utf-8"),
                js, count=1, flags=re.DOTALL)
(ROOT / "script.js").write_text(js_new, encoding="utf-8")

py = (ROOT / "gen_catalogo.py").read_text(encoding="utf-8")
py_new = re.sub(r'^products = \[.*?\n\]\s*$', (ROOT / "_products_py_block.py").read_text(encoding="utf-8"),
                py, count=1, flags=re.MULTILINE | re.DOTALL)
(ROOT / "gen_catalogo.py").write_text(py_new, encoding="utf-8")

print("\nArchivos actualizados: script.js, gen_catalogo.py, products_eurotextile.json")
