"""
Maully Admin Panel - FastAPI backend
- Products CRUD
- Orders list
- Simple password auth via cookie session
"""
import json
import os
import secrets
import time
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException, Request, Response, Depends, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent
PRODUCTS_FILE = BASE_DIR / "products.json"
ORDERS_FILE = BASE_DIR / "orders.json"

# Admin password (change via env var)
ADMIN_PASSWORD = os.environ.get("MAULLY_ADMIN_PASSWORD", "maully2026")

# In-memory sessions
SESSIONS: dict[str, float] = {}
SESSION_TTL = 60 * 60 * 24 * 7  # 7 days

app = FastAPI(title="Maully Admin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://importadoramaully.cl", "https://www.importadoramaully.cl", "http://localhost:3002", "http://localhost:8002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============ HELPERS ============
def load_products() -> list[dict]:
    if not PRODUCTS_FILE.exists():
        return []
    return json.loads(PRODUCTS_FILE.read_text(encoding="utf-8"))


def save_products(products: list[dict]) -> None:
    PRODUCTS_FILE.write_text(
        json.dumps(products, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def load_orders() -> list[dict]:
    if not ORDERS_FILE.exists():
        return []
    return json.loads(ORDERS_FILE.read_text(encoding="utf-8"))


def save_orders(orders: list[dict]) -> None:
    ORDERS_FILE.write_text(
        json.dumps(orders, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def require_auth(request: Request) -> None:
    token = request.cookies.get("maully_session")
    if not token or token not in SESSIONS:
        raise HTTPException(status_code=401, detail="Not authenticated")
    # Check TTL
    if time.time() - SESSIONS[token] > SESSION_TTL:
        del SESSIONS[token]
        raise HTTPException(status_code=401, detail="Session expired")


# ============ MODELS ============
class Product(BaseModel):
    id: Optional[int] = None
    cat: str
    name: str
    price: int
    origPrice: int
    weight: str
    tier: str
    badge: str
    isNew: bool = False
    img: str = "fardo-maully.jpg"


class LoginReq(BaseModel):
    password: str


class OrderItem(BaseModel):
    id: int
    name: str
    price: int
    qty: int


class OrderCreate(BaseModel):
    items: list[OrderItem]
    customer: dict
    shipping: dict
    total: int
    payment_method: str = "mercadopago"


# ============ AUTH ============
@app.post("/api/login")
def login(req: LoginReq, response: Response):
    if req.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    token = secrets.token_urlsafe(32)
    SESSIONS[token] = time.time()
    response.set_cookie(
        key="maully_session",
        value=token,
        max_age=SESSION_TTL,
        httponly=True,
        samesite="lax",
        secure=True,
    )
    return {"ok": True}


@app.post("/api/logout")
def logout(request: Request, response: Response):
    token = request.cookies.get("maully_session")
    if token and token in SESSIONS:
        del SESSIONS[token]
    response.delete_cookie("maully_session")
    return {"ok": True}


@app.get("/api/me")
def me(request: Request):
    try:
        require_auth(request)
        return {"authenticated": True}
    except HTTPException:
        return {"authenticated": False}


# ============ PRODUCTS (public GET, auth for mutations) ============
@app.get("/api/products")
def get_products():
    return load_products()


@app.post("/api/products")
def create_product(product: Product, request: Request):
    require_auth(request)
    products = load_products()
    # Auto-assign ID
    next_id = max([p["id"] for p in products], default=0) + 1
    p_dict = product.model_dump()
    p_dict["id"] = next_id
    products.append(p_dict)
    save_products(products)
    return p_dict


@app.put("/api/products/{product_id}")
def update_product(product_id: int, product: Product, request: Request):
    require_auth(request)
    products = load_products()
    for i, p in enumerate(products):
        if p["id"] == product_id:
            p_dict = product.model_dump()
            p_dict["id"] = product_id
            products[i] = p_dict
            save_products(products)
            return p_dict
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, request: Request):
    require_auth(request)
    products = load_products()
    new_products = [p for p in products if p["id"] != product_id]
    if len(new_products) == len(products):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    save_products(new_products)
    return {"ok": True}


# ============ ORDERS ============
@app.post("/api/orders")
def create_order(order: OrderCreate):
    orders = load_orders()
    next_id = max([o["id"] for o in orders], default=0) + 1
    order_dict = order.model_dump()
    order_dict["id"] = next_id
    order_dict["created_at"] = time.time()
    order_dict["status"] = "pending"
    orders.append(order_dict)
    save_orders(orders)
    return {"ok": True, "order_id": next_id}


@app.get("/api/orders")
def list_orders(request: Request):
    require_auth(request)
    return load_orders()


@app.patch("/api/orders/{order_id}")
def update_order_status(order_id: int, payload: dict, request: Request):
    require_auth(request)
    orders = load_orders()
    for o in orders:
        if o["id"] == order_id:
            if "status" in payload:
                o["status"] = payload["status"]
            save_orders(orders)
            return o
    raise HTTPException(status_code=404, detail="Pedido no encontrado")


# ============ HEALTH ============
@app.get("/api/health")
def health():
    return {"ok": True, "service": "maully-admin"}
