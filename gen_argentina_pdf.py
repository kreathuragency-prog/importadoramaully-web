#!/usr/bin/env python3
"""
Genera el PDF EXCLUSIVO Argentina:
  catalogo-maully-argentina-mayo-2026.pdf

Contiene SOLO los 34 productos puestos en Argentina (lista de Claudio +15%),
con condiciones de envío, pago y la explicación de ganchos.
"""
from fpdf import FPDF
import os, json, re, unicodedata

WA_NUM = "+56 9 7515 5745"
WA_LINK = "https://wa.me/56975155745"
BASE_URL = "https://www.importadoramaully.cl"

# Paleta
C_DARK    = (18, 18, 28)
C_NAVY    = (22, 33, 62)
C_GOLD    = (212, 175, 55)
C_GOLD_LT = (232, 200, 100)
C_WHITE   = (255, 255, 255)
C_CREAM   = (250, 247, 240)
C_GRAY2   = (220, 215, 205)
C_GRAY3   = (160, 155, 145)
C_GRAY5   = (60, 58, 52)
C_CELESTE = (117, 170, 219)


def fmt_clp(n): return f"$ {n:,.0f}".replace(",", ".")


class ArgentinaPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=18)
        self.l_margin = 14
        self.r_margin = 14
        self.content_w = 210 - 28
        font_dir = "C:/Windows/Fonts"
        self.add_font("Body", "", os.path.join(font_dir, "DejaVuSans.ttf"))
        self.add_font("Body", "B", os.path.join(font_dir, "DejaVuSans-Bold.ttf"))
        self.add_font("Body", "I", os.path.join(font_dir, "DejaVuSans-Oblique.ttf"))
        self.add_font("Body", "BI", os.path.join(font_dir, "DejaVuSans-BoldOblique.ttf"))

    def header(self):
        if self.page_no() == 1:
            return
        self.set_y(6)
        self.set_font("Body", "", 6.5)
        self.set_text_color(*C_GRAY3)
        self.cell(60, 5, "IMPORTADORA MAULLY · ARGENTINA", link=BASE_URL)
        self.cell(62, 5, "importadoramaully.cl", align="C", link=BASE_URL)
        self.cell(60, 5, WA_NUM, align="R", link=WA_LINK)
        self.set_draw_color(*C_CELESTE)
        self.set_line_width(0.4)
        self.line(14, 13, 196, 13)
        self.set_y(16)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(*C_GRAY2)
        self.set_line_width(0.2)
        self.line(14, self.get_y(), 196, self.get_y())
        self.ln(2)
        self.set_font("Body", "", 6)
        self.set_text_color(*C_GRAY3)
        pg = self.page_no()
        self.cell(60, 5, "Catálogo Argentina · Mayo 2026")
        self.cell(62, 5, f"Pago 100% adelantado · Global66 o USD", align="C")
        self.cell(60, 5, f"Página {pg}", align="R")

    def cover(self):
        self.add_page()
        # Background
        self.set_fill_color(*C_DARK)
        self.rect(0, 0, 210, 297, "F")
        # Top celeste stripe
        self.set_fill_color(*C_CELESTE)
        self.rect(0, 0, 210, 60, "F")
        # Brand mark
        self.set_y(20)
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_WHITE)
        self.cell(0, 6, "IMPORTADORA MAULLY", align="C")
        self.ln(8)
        self.set_font("Body", "", 8)
        self.cell(0, 4, "+40 años importando ropa premium · Chile", align="C")

        # Center title
        self.set_y(95)
        self.set_font("Body", "B", 36)
        self.set_text_color(*C_GOLD)
        self.cell(0, 14, "CATÁLOGO", align="C")
        self.ln(14)
        self.set_font("Body", "B", 36)
        self.set_text_color(*C_WHITE)
        self.cell(0, 14, "ARGENTINA", align="C")
        self.ln(14)
        self.set_font("Body", "", 12)
        self.set_text_color(*C_CELESTE)
        self.cell(0, 6, "Productos puestos en Argentina · Mayo 2026", align="C")
        self.ln(10)

        # Gold divider
        self.set_fill_color(*C_GOLD)
        self.rect(85, self.get_y() + 4, 40, 1, "F")
        self.ln(20)

        # Tagline
        self.set_x(30)
        self.set_font("Body", "I", 11)
        self.set_text_color(*C_WHITE)
        self.multi_cell(150, 6,
            "Lista de fardos exportados a Argentina con precios "
            "puestos en destino. Pago 100% adelantado vía Global66 o USD.",
            align="C")

        # Footer cover
        self.set_y(-50)
        self.set_x(20)
        self.set_font("Body", "B", 11)
        self.set_text_color(*C_GOLD)
        self.cell(170, 6, "Coordinación y cotizaciones por WhatsApp", align="C")
        self.ln(6)
        self.set_font("Body", "", 10)
        self.set_text_color(*C_WHITE)
        self.cell(170, 5, WA_NUM, align="C", link=WA_LINK)
        self.ln(8)
        self.set_font("Body", "", 8)
        self.set_text_color(*C_CELESTE)
        self.cell(170, 4, "Av. La Florida 9421, Santiago · Berna 767, Pichilemu", align="C")

    def conditions_page(self):
        self.add_page()
        self.set_fill_color(*C_CREAM)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*C_CELESTE)
        self.rect(0, 0, 210, 5, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(0, 5, 210, 1, "F")
        self.set_y(20)

        # Eyebrow
        self.set_font("Body", "", 8)
        self.set_text_color(*C_CELESTE)
        self.cell(0, 4, "CONDICIONES DE COMPRA · ARGENTINA", align="C")
        self.ln(6)
        self.set_font("Body", "B", 26)
        self.set_text_color(*C_DARK)
        self.cell(0, 12, "Cómo comprar desde Argentina", align="C")
        self.ln(14)
        self.set_fill_color(*C_CELESTE)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(10)

        # 4 boxes
        items = [
            ("PAGO", "100% por adelantado siempre. Aceptamos Global66 (transferencia internacional) o USD (efectivo o transferencia)."),
            ("ENVÍOS HASTA 10 KG", "Con Starken según las tarifas del courier. Starken cobra el flete al retirar el cliente en Argentina."),
            ("ENVÍOS SOBRE 10 KG", "Con transportistas privados que cobran por fardo según volumen y destino. Cotizamos por WhatsApp a la medida."),
            ("VISÍTANOS EN CHILE", "Av. La Florida 9421, Santiago · Berna 767, Pichilemu. Atendemos lun-vie 11:00-19:00."),
        ]
        for title, body in items:
            box_y = self.get_y()
            self.set_fill_color(*C_GOLD_LT)
            self.rect(20, box_y, 170, 22, "F")
            self.set_fill_color(*C_CELESTE)
            self.rect(20, box_y, 4, 22, "F")
            # Title
            self.set_y(box_y + 4)
            self.set_x(30)
            self.set_font("Body", "B", 11)
            self.set_text_color(*C_DARK)
            self.cell(160, 6, title)
            # Body
            self.set_y(box_y + 11)
            self.set_x(30)
            self.set_font("Body", "", 9.5)
            self.set_text_color(*C_GRAY5)
            self.multi_cell(155, 4.5, body)
            self.set_y(box_y + 26)

        # Bea CTA
        self.ln(4)
        self.set_x(20)
        self.set_font("Body", "B", 11)
        self.set_text_color(*C_GOLD)
        self.cell(170, 6, "Coordina con Bea por WhatsApp", align="C", link=WA_LINK)
        self.ln(6)
        self.set_x(20)
        self.set_font("Body", "", 10)
        self.set_text_color(*C_GRAY5)
        self.cell(170, 5, WA_NUM, align="C", link=WA_LINK)

    def ganchos_explained(self):
        self.add_page()
        self.set_fill_color(*C_CREAM)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(0, 0, 210, 3, "F")
        self.set_y(20)

        self.set_font("Body", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(0, 4, "MODALIDAD DE COMPRA", align="C")
        self.ln(6)
        self.set_font("Body", "B", 28)
        self.set_text_color(*C_DARK)
        self.cell(0, 12, "¿Qué es un \"Gancho\"?", align="C")
        self.ln(14)
        self.set_fill_color(*C_GOLD)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(10)

        self.set_font("Body", "", 11)
        self.set_text_color(*C_GRAY5)
        self.set_x(20)
        self.multi_cell(170, 6,
            "Un GANCHO es un fardo de menor exclusividad que el cliente compra "
            "junto a un fardo top muy demandado. Algunos productos exclusivos "
            "se venden con la condición de sumar 1 o 2 ganchos en la misma compra.",
            align="C")
        self.ln(8)

        # Why box
        box_y = self.get_y()
        self.set_fill_color(*C_GOLD_LT)
        self.rect(20, box_y, 170, 50, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(20, box_y, 4, 50, "F")
        self.set_y(box_y + 5)
        self.set_x(30)
        self.set_font("Body", "B", 11)
        self.set_text_color(*C_DARK)
        self.cell(160, 5, "¿Por qué funciona así?")
        self.ln(7)
        bullets = [
            ("Para Maully:", "rotamos bodega de variedad de stock y productos."),
            ("Para ti:", "accedes a fardos exclusivos que no salen sueltos y diversificas tu mix."),
            ("Beneficio mutuo:", "menor costo por kilo total combinando exclusivos + ganchos."),
        ]
        for label, txt in bullets:
            self.set_x(30)
            self.set_font("Body", "B", 9.5)
            self.set_text_color(*C_DARK)
            self.cell(40, 5, "• " + label)
            self.set_font("Body", "", 9.5)
            self.set_text_color(*C_GRAY5)
            self.multi_cell(120, 5, txt)

        self.set_y(box_y + 56)
        self.set_x(20)
        self.set_font("Body", "", 10)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(170, 5,
            "REGLA ESTRICTA: los ganchos NUNCA son fardos PREMIUM ni MARCA puros. "
            "Sirven solo: fardos SEGUNDA, combos MARCA SEGUNDA o PREMIUM SEGUNDA, "
            "y fardos sin las palabras \"marca\" ni \"premium\" en el título. "
            "En la tabla verás +1 gancho o +2 ganchos junto a cada fardo top.",
            align="C")

    def products_table(self, productos):
        self.add_page()
        self.set_y(18)
        # Title
        self.set_font("Body", "", 8)
        self.set_text_color(*C_CELESTE)
        self.cell(0, 4, "LISTA DE PRECIOS · MAYO 2026", align="C")
        self.ln(6)
        self.set_font("Body", "B", 22)
        self.set_text_color(*C_DARK)
        self.cell(0, 10, "Productos puestos en Argentina", align="C")
        self.ln(12)
        self.set_fill_color(*C_CELESTE)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(8)

        # Header table
        self.set_fill_color(*C_DARK)
        self.set_text_color(*C_WHITE)
        self.set_font("Body", "B", 7.5)
        self.set_x(14)
        self.cell(98, 7, "  PRODUCTO", fill=True)
        self.cell(18, 7, "PESO", align="C", fill=True)
        self.cell(36, 7, "PRECIO ARG", align="R", fill=True)
        self.cell(30, 7, "GANCHOS  ", align="R", fill=True)
        self.ln(9)

        for i, p in enumerate(productos):
            if self.get_y() > 268:
                self.add_page()
                self.set_y(18)
                self.set_fill_color(*C_DARK)
                self.set_text_color(*C_WHITE)
                self.set_font("Body", "B", 7.5)
                self.set_x(14)
                self.cell(98, 7, "  PRODUCTO", fill=True)
                self.cell(18, 7, "PESO", align="C", fill=True)
                self.cell(36, 7, "PRECIO ARG", align="R", fill=True)
                self.cell(30, 7, "GANCHOS  ", align="R", fill=True)
                self.ln(9)

            y = self.get_y()
            row_h = 7
            if i % 2 == 0:
                self.set_fill_color(252, 250, 246)
                self.rect(14, y, self.content_w, row_h, "F")
            self.set_draw_color(*C_GRAY2)
            self.set_line_width(0.1)
            self.line(14, y + row_h, 14 + self.content_w, y + row_h)

            name = p["name"]
            if len(name) > 56:
                name = name[:54] + ".."
            self.set_x(14)
            self.set_font("Body", "", 8)
            self.set_text_color(*C_DARK)
            self.cell(98, row_h, "  " + name)

            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_GRAY3)
            self.cell(18, row_h, p["weight"], align="C")

            self.set_font("Body", "B", 8)
            self.set_text_color(*C_DARK)
            self.cell(36, row_h, fmt_clp(p["price"]), align="R")

            ganchos = p.get("ganchos", 0)
            if ganchos > 0:
                self.set_font("Body", "B", 8)
                self.set_text_color(234, 88, 12)
                txt_g = f"+{ganchos} gancho{'s' if ganchos > 1 else ''}"
            else:
                self.set_font("Body", "", 7.5)
                self.set_text_color(*C_GRAY3)
                txt_g = "—"
            self.cell(30, row_h, txt_g + "  ", align="R")
            self.ln(row_h)

        # Footer note
        self.ln(6)
        self.set_x(20)
        self.set_font("Body", "I", 9)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(170, 5,
            "Precios en CLP. Pago 100% adelantado vía Global66 o USD para activar el "
            "despacho. El envío va aparte: hasta 10 kg con Starken, sobre 10 kg con "
            "transportistas privados (cotización por WhatsApp).",
            align="C")
        self.ln(4)
        self.set_x(20)
        self.set_font("Body", "B", 10)
        self.set_text_color(*C_GOLD)
        self.cell(170, 5, "Te invitamos a conocernos en Av. La Florida 9421 (Santiago) o Berna 767 (Pichilemu)",
                  align="C")


def main():
    here = os.path.dirname(__file__)
    data = json.load(open(os.path.join(here, "_claudio_prices.json"), encoding="utf-8"))
    margin = data["_meta"].get("margen_aplicado", 1.15)

    productos = []
    for c in data["productos"]:
        productos.append({
            "name": c["name_claudio"],
            "weight": c["weight"].upper(),
            "price": int(round(c["price_costo"] * margin / 100)) * 100,
            "ganchos": c.get("ganchos", 0),
        })
    productos.sort(key=lambda p: (-p["ganchos"], p["name"].lower()))

    pdf = ArgentinaPDF()
    pdf.alias_nb_pages()
    pdf.cover()
    pdf.conditions_page()
    pdf.ganchos_explained()
    pdf.products_table(productos)

    out = os.path.join(here, "catalogo-maully-argentina-mayo-2026.pdf")
    pdf.output(out)
    print(f"PDF Argentina: {out}")
    print(f"Productos: {len(productos)}")
    print(f"Páginas: {pdf.page_no()}")


if __name__ == "__main__":
    main()
