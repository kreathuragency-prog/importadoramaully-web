"""
Genera token permanente de System User para WhatsApp Bot
Paso 1: Edita las dos variables de abajo
Paso 2: Ejecuta: python generar_token.py
"""
import hmac, hashlib, urllib.request, json

APP_ID = "848955881568728"
SYSTEM_USER_ID = "61573338221946"

# === PEGA TUS VALORES AQUI ===
APP_SECRET = "PEGA_TU_APP_SECRET_AQUI"
ACCESS_TOKEN = "PEGA_TU_ACCESS_TOKEN_AQUI"
# ==============================

if "PEGA_TU" in APP_SECRET or "PEGA_TU" in ACCESS_TOKEN:
    print("ERROR: Edita el archivo generar_token.py y pega tu App Secret y Access Token")
    print("Archivo: C:\\Users\\matia\\importadoramaully web\\generar_token.py")
    exit(1)

proof = hmac.new(APP_SECRET.encode(), ACCESS_TOKEN.encode(), hashlib.sha256).hexdigest()

url = (
    f"https://graph.facebook.com/v25.0/{SYSTEM_USER_ID}/access_tokens"
    f"?business_app={APP_ID}"
    f"&scope=whatsapp_business_messaging,whatsapp_business_management"
    f"&appsecret_proof={proof}"
    f"&access_token={ACCESS_TOKEN}"
)

req = urllib.request.Request(url, method="POST")
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
        if "access_token" in data:
            print("\n" + "="*50)
            print("TOKEN PERMANENTE GENERADO!")
            print("="*50)
            print(f"\n{data['access_token']}\n")
        else:
            print(f"\nRespuesta: {json.dumps(data, indent=2)}")
except Exception as e:
    print(f"\nError: {e}")
    try:
        print(f"Detalle: {e.read().decode()}")
    except:
        pass
