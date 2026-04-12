"""
WhatsApp — Parser de mensajes entrantes + envio via Graph API
"""

import os
import logging
import httpx
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("bot")

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("META_PHONE_NUMBER_ID")
API_VERSION = "v21.0"


def parsear_mensaje(body: dict) -> list[dict]:
    """
    Extrae mensajes de texto del payload de Meta Cloud API.
    Retorna lista de {"telefono": "...", "texto": "...", "msg_id": "..."}
    """
    mensajes = []

    for entry in body.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            for msg in value.get("messages", []):
                if msg.get("type") == "text":
                    mensajes.append({
                        "telefono": msg.get("from", ""),
                        "texto": msg.get("text", {}).get("body", ""),
                        "msg_id": msg.get("id", ""),
                    })

    return mensajes


async def enviar_mensaje(telefono: str, texto: str) -> bool:
    """Envia un mensaje de texto via Meta WhatsApp Cloud API."""
    if not ACCESS_TOKEN or not PHONE_NUMBER_ID:
        logger.error("META_ACCESS_TOKEN o META_PHONE_NUMBER_ID no configurados")
        return False

    url = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": telefono,
        "type": "text",
        "text": {"body": texto},
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=payload, headers=headers)
        if r.status_code != 200:
            logger.error(f"Error Graph API [{r.status_code}]: {r.text}")
            return False
        return True
