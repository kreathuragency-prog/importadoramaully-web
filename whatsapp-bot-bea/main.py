"""
Bot WhatsApp — Bea, Importadora Maully
Webhook + Panel CRM + Respuesta manual
"""

import sys, os, site
_usp = site.getusersitepackages()
if _usp not in sys.path:
    sys.path.insert(0, _usp)
import jinja2  # noqa: F401

import asyncio
import random
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import PlainTextResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

from whatsapp import parsear_mensaje, enviar_mensaje
from brain import generar_respuesta, cargar_info_web
from scraper import scrape_maully
from checkout import router as checkout_router
from admin_panel import router as admin_router
from database import init_db
from db_ops import (
    get_or_create_contact,
    get_or_create_conversation,
    save_message, get_conversation_messages,
    get_or_create_lead,
    get_all_conversations, get_conversation_detail,
    get_all_leads, get_dashboard_stats,
)

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("bot")

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "maully-bea-token")
PORT = int(os.getenv("PORT", 8000))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    info_web = await scrape_maully()
    cargar_info_web(info_web)
    logger.info("Bea Bot (Importadora Maully) iniciado en puerto %d", PORT)
    yield


app = FastAPI(title="Importadora Maully — Bea WhatsApp Bot + E-Commerce", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.importadoramaully.cl", "https://importadoramaully.cl", "http://localhost:3002"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(checkout_router)
app.include_router(admin_router)

os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
jinja_env = Environment(loader=FileSystemLoader("templates"), autoescape=True)


def render(template_name: str, **context) -> HTMLResponse:
    template = jinja_env.get_template(template_name)
    return HTMLResponse(template.render(**context))


# ══════════════════════════════════════════════════════════════
# WEBHOOK
# ══════════════════════════════════════════════════════════════

@app.get("/")
async def health():
    return {"status": "ok", "service": "maully-bea-bot"}


@app.get("/webhook")
async def verificar_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        logger.info("Webhook verificado OK")
        return PlainTextResponse(challenge)
    raise HTTPException(status_code=403, detail="Token invalido")


@app.post("/webhook")
async def recibir_mensaje(request: Request):
    try:
        body = await request.json()
    except Exception:
        return {"status": "ok"}

    mensajes = parsear_mensaje(body)

    for msg in mensajes:
        telefono = msg["telefono"]
        texto = msg["texto"]
        if not texto:
            continue

        logger.info(f"[{telefono}] -> {texto}")

        try:
            contact = await get_or_create_contact(telefono)
            conv = await get_or_create_conversation(contact.id)
            await save_message(conv.id, "inbound", texto)
            await get_or_create_lead(contact.id, "maully")

            historial = await get_conversation_messages(conv.id)
            respuesta = await generar_respuesta(texto, historial)

            # Delay humano: 7-10 seg primer mensaje, 3-5 seg siguientes
            es_primer_mensaje = len(historial) == 0
            if es_primer_mensaje:
                delay = random.uniform(7, 10)
            else:
                delay = random.uniform(3, 5)
            await asyncio.sleep(delay)

            await save_message(conv.id, "outbound", respuesta)

            ok = await enviar_mensaje(telefono, respuesta)
            if ok:
                logger.info(f"[{telefono}] <- {respuesta[:80]}...")
            else:
                logger.error(f"[{telefono}] Error enviando")

        except Exception as e:
            logger.error(f"Error procesando [{telefono}]: {e}")

    return {"status": "ok"}


# ══════════════════════════════════════════════════════════════
# PANEL CRM (conversaciones de WhatsApp)
# Nota: /admin esta reservado para el panel e-commerce (admin_panel.py)
# El panel de conversaciones de Bea vive en /crm
# ══════════════════════════════════════════════════════════════

@app.get("/crm", response_class=HTMLResponse)
async def crm_dashboard(request: Request):
    stats = await get_dashboard_stats()
    convs = await get_all_conversations(limit=10)
    return render("admin.html", active="dashboard", stats=stats, conversations=convs)


@app.get("/crm/conversations", response_class=HTMLResponse)
async def crm_conversations(request: Request):
    convs = await get_all_conversations(limit=100)
    return render("conversations.html", active="conversations", conversations=convs)


@app.get("/crm/conversation/{conv_id}", response_class=HTMLResponse)
async def crm_conversation_detail(request: Request, conv_id: int):
    detail = await get_conversation_detail(conv_id)
    if not detail:
        raise HTTPException(status_code=404)
    return render("conversation_detail.html", active="conversations", conv=detail)


@app.post("/crm/conversation/{conv_id}/reply")
async def crm_reply(conv_id: int, message: str = Form(...)):
    detail = await get_conversation_detail(conv_id)
    if not detail:
        raise HTTPException(status_code=404)
    await save_message(conv_id, "outbound", message)
    ok = await enviar_mensaje(detail["phone"], message)
    if ok:
        logger.info(f"[MANUAL] [{detail['phone']}] <- {message[:80]}...")
    return RedirectResponse(url=f"/crm/conversation/{conv_id}", status_code=303)


@app.get("/crm/leads", response_class=HTMLResponse)
async def crm_leads(request: Request):
    leads = await get_all_leads(limit=100)
    return render("leads.html", active="leads", leads=leads)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
