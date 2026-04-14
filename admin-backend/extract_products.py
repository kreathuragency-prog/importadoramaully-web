"""Extract products array from script.js to products.json"""
import re
import json
import sys

# Read script.js
with open('../script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Match from "const products = [" to first "];"
match = re.search(r'const products = \[(.*?)\n\];', content, re.DOTALL)
if not match:
    print("ERROR: products array not found")
    sys.exit(1)

body = match.group(1)

# Each product is a JS object literal; convert to JSON
products = []
# Match {...} blocks
for m in re.finditer(r'\{([^{}]+)\}', body):
    obj_str = m.group(1)
    # Parse key:value pairs
    obj = {}
    # Split by comma, but careful with strings
    # Use a simple state parser
    pairs = []
    current = ''
    in_string = False
    string_char = None
    for ch in obj_str:
        if in_string:
            if ch == string_char:
                in_string = False
            current += ch
        else:
            if ch in ('"', "'"):
                in_string = True
                string_char = ch
                current += ch
            elif ch == ',':
                pairs.append(current.strip())
                current = ''
            else:
                current += ch
    if current.strip():
        pairs.append(current.strip())

    for pair in pairs:
        if ':' not in pair:
            continue
        key, value = pair.split(':', 1)
        key = key.strip()
        value = value.strip()
        # Parse value
        if value == 'true':
            obj[key] = True
        elif value == 'false':
            obj[key] = False
        elif value == 'MAULLY_IMG':
            obj[key] = 'fardo-maully.jpg'
        elif value.startswith("'") and value.endswith("'"):
            obj[key] = value[1:-1]
        elif value.startswith('"') and value.endswith('"'):
            obj[key] = value[1:-1]
        else:
            try:
                obj[key] = int(value)
            except ValueError:
                try:
                    obj[key] = float(value)
                except ValueError:
                    obj[key] = value
    products.append(obj)

print(f"Extracted {len(products)} products")

# Write JSON
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("Written to products.json")
