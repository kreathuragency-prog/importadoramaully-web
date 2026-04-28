#!/usr/bin/env python3
"""
Genera el PDF de MARCAS EXCLUSIVAS puestas en Argentina.
Filtra solo los productos con `exclusivo: true` en _claudio_prices.json.
Output: catalogo-maully-marcas-exclusivas-argentina.pdf
"""
from fpdf import FPDF
import os, json

WA_NUM = "+56 9 7515 5745"
WA_LINK = "https://wa.me/56975155745"
BASE_URL = "https://www.importadoramaully.cl"

C_DARK    = (18, 18, 28)
C_GOLD    = (212, 175, 55)
C_GOLD_LT = (232, 200, 100)
C_WHITE   = (255, 255, 255)
C_CREAM   = (250, 247, 240)
C_GRAY2   = (220, 215, 205)
C_GRAY3   = (160, 155, 145)
C_GRAY5   = (60, 58, 52)
C_CELESTE = (117, 170, 219)


def fmt_clp(n): return f"$ {n:,.0f}".replace(",", ".")
def fmt_usd(n, rate): return f"USD {round(n / rate):,}".replace(",", ".")


class MarcasExclusivasPDF(FPDF):
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
        self.cell(70, 5, "MAULLY · MARCAS EXCLUSIVAS · ARGENTINA", link=BASE_URL)
        self.cell(52, 5, "importadoramaully.cl", align="C", link=BASE_URL)
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
        self.cell(60, 5, "Marcas Exclusivas Argentina · Mayo 2026")
        self.cell(62, 5, "Pago 100% adelantado · Global66 / USD", align="C")
        self.cell(60, 5, f"Página {self.page_no()}", align="R")

    def cover(self):
        self.add_page()
        # Bandera Argentina: 3 franjas
        self.set_fill_color(*C_CELESTE)
        self.rect(0, 0, 210, 99, "F")
        self.set_fill_color(*C_WHITE)
        self.rect(0, 99, 210, 99, "F")
        self.set_fill_color(*C_CELESTE)
        self.rect(0, 198, 210, 99, "F")
        # Sol dorado en la franja blanca
        self.set_fill_color(*C_GOLD)
        # círculo aproximado
        self.ellipse(95, 130, 20, 20, "F")

        self.set_y(20)
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_WHITE)
        self.cell(0, 6, "IMPORTADORA MAULLY · CHILE", align="C")
        self.ln(8)
        self.set_font("Body", "", 8)
        self.cell(0, 4, "+40 años importando marcas premium", align="C")

        # Title central
        self.set_y(58)
        self.set_font("Body", "B", 30)
        self.set_text_color(*C_WHITE)
        self.cell(0, 12, "MARCAS", align="C")
        self.ln(12)
        self.cell(0, 12, "EXCLUSIVAS", align="C")
        self.ln(10)

        # Subtítulo en la franja blanca (debajo del sol)
        self.set_y(160)
        self.set_font("Body", "B", 18)
        self.set_text_color(*C_DARK)
        self.cell(0, 10, "Puestas en Argentina", align="C")
        self.ln(10)
        self.set_font("Body", "I", 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 5, "Mayo 2026", align="C")

        # Footer cover
        self.set_y(-50)
        self.set_x(20)
        self.set_font("Body", "B", 11)
        self.set_text_color(*C_WHITE)
        self.cell(170, 6, "Coordinación y cotizaciones por WhatsApp", align="C")
        self.ln(6)
        self.set_font("Body", "", 10)
        self.cell(170, 5, WA_NUM, align="C", link=WA_LINK)
        self.ln(8)
        self.set_font("Body", "", 8)
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

        self.set_font("Body", "", 8)
        self.set_text_color(*C_CELESTE)
        self.cell(0, 4, "CONDICIONES · ARGENTINA", align="C")
        self.ln(6)
        self.set_font("Body", "B", 24)
        self.set_text_color(*C_DARK)
        self.cell(0, 12, "Cómo comprar marcas exclusivas", align="C")
        self.ln(14)
        self.set_fill_color(*C_CELESTE)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(10)

        items = [
            ("PAGO 100% ADELANTADO", "Aceptamos Global66 (transferencia internacional) o USD (efectivo o transferencia)."),
            ("ENVÍO A ARGENTINA", "Solo con empresas privadas desde Chile. $100.000 CLP/fardo si pides 10 fardos o más · $150.000 CLP/fardo si pides hasta 9 fardos."),
            ("STARKEN NO APLICA", "Starken solo se usa para envíos dentro de Chile. Para Argentina siempre transporte privado."),
            ("VISÍTANOS EN CHILE", "Av. La Florida 9421, Santiago · Berna 767, Pichilemu. Lun-Vie 11:00-19:00."),
        ]
        for title, body in items:
            box_y = self.get_y()
            self.set_fill_color(*C_GOLD_LT)
            self.rect(20, box_y, 170, 22, "F")
            self.set_fill_color(*C_CELESTE)
            self.rect(20, box_y, 4, 22, "F")
            self.set_y(box_y + 4)
            self.set_x(30)
            self.set_font("Body", "B", 11)
            self.set_text_color(*C_DARK)
            self.cell(160, 6, title)
            self.set_y(box_y + 11)
            self.set_x(30)
            self.set_font("Body", "", 9.5)
            self.set_text_color(*C_GRAY5)
            self.multi_cell(155, 4.5, body)
            self.set_y(box_y + 26)

        # Sección dedicada al gancho
        self.ln(2)
        box_y = self.get_y()
        self.set_fill_color(255, 237, 213)  # naranja claro
        self.rect(20, box_y, 170, 56, "F")
        self.set_fill_color(234, 88, 12)  # naranja
        self.rect(20, box_y, 4, 56, "F")
        self.set_y(box_y + 5)
        self.set_x(30)
        self.set_font("Body", "B", 12)
        self.set_text_color(124, 45, 18)  # marrón oscuro
        self.cell(160, 6, "PRECIOS DE FARDOS CON GANCHO (clave para Argentina)")
        self.ln(8)
        self.set_x(30)
        self.set_font("Body", "", 9.5)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(155, 4.5,
            "Algunos fardos top exclusivos requieren \"+1 gancho\" o \"+2 ganchos\". "
            "El precio publicado es solo el del fardo top. Para calcular el TOTAL "
            "PUESTO EN ARGENTINA, se suma:")
        self.ln(2)
        self.set_x(35)
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_DARK)
        self.multi_cell(150, 4.5,
            "= Precio del fardo top  +  Precio del fardo gancho (CLP, Chile)  +  Envío de ambos fardos")
        self.ln(3)
        self.set_x(30)
        self.set_font("Body", "", 9.5)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(155, 4.5,
            "El envío por fardo es: $100.000 CLP si el pedido total supera los 10 fardos · "
            "$150.000 CLP si el pedido es menor a 10 fardos. "
            "Bea te arma la cotización exacta por WhatsApp con tu mix de productos.")

    def products_table(self, productos, usd_rate):
        self.add_page()
        self.set_y(18)
        self.set_font("Body", "", 8)
        self.set_text_color(*C_CELESTE)
        self.cell(0, 4, "MARCAS EXCLUSIVAS · MAYO 2026", align="C")
        self.ln(6)
        self.set_font("Body", "B", 22)
        self.set_text_color(*C_DARK)
        self.cell(0, 10, "Lista de Marcas Exclusivas", align="C")
        self.ln(12)
        self.set_fill_color(*C_CELESTE)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(8)

        # Header
        self.set_fill_color(*C_DARK)
        self.set_text_color(*C_WHITE)
        self.set_font("Body", "B", 7.5)
        self.set_x(14)
        self.cell(82, 7, "  PRODUCTO", fill=True)
        self.cell(16, 7, "PESO", align="C", fill=True)
        self.cell(32, 7, "PRECIO ARG", align="R", fill=True)
        self.cell(28, 7, "USD", align="R", fill=True)
        self.cell(24, 7, "GANCHOS  ", align="R", fill=True)
        self.ln(9)

        for i, p in enumerate(productos):
            if self.get_y() > 268:
                self.add_page()
                self.set_y(18)
                self.set_fill_color(*C_DARK)
                self.set_text_color(*C_WHITE)
                self.set_font("Body", "B", 7.5)
                self.set_x(14)
                self.cell(82, 7, "  PRODUCTO", fill=True)
                self.cell(16, 7, "PESO", align="C", fill=True)
                self.cell(32, 7, "PRECIO ARG", align="R", fill=True)
                self.cell(28, 7, "USD", align="R", fill=True)
                self.cell(24, 7, "GANCHOS  ", align="R", fill=True)
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
            if len(name) > 46:
                name = name[:44] + ".."
            self.set_x(14)
            self.set_font("Body", "", 8)
            self.set_text_color(*C_DARK)
            self.cell(82, row_h, "  " + name)

            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_GRAY3)
            self.cell(16, row_h, p["weight"], align="C")

            self.set_font("Body", "B", 8)
            self.set_text_color(*C_DARK)
            self.cell(32, row_h, fmt_clp(p["price"]), align="R")

            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_GRAY5)
            self.cell(28, row_h, fmt_usd(p["price"], usd_rate), align="R")

            ganchos = p.get("ganchos", 0)
            if ganchos > 0:
                self.set_font("Body", "B", 8)
                self.set_text_color(234, 88, 12)
                txt_g = f"+{ganchos} gancho{'s' if ganchos > 1 else ''}"
            else:
                self.set_font("Body", "", 7.5)
                self.set_text_color(*C_GRAY3)
                txt_g = "—"
            self.cell(24, row_h, txt_g + "  ", align="R")
            self.ln(row_h)

        self.ln(6)
        self.set_x(20)
        self.set_font("Body", "I", 9)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(170, 5,
            f"Precios convertidos a USD a tasa referencial de ${usd_rate} CLP/USD. "
            "El tipo de cambio definitivo se confirma al cierre del pedido. Pago 100% "
            "adelantado vía Global66 o USD.",
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

    # Filtro: SOLO los exclusivos = true
    productos = []
    for c in data["productos"]:
        if not c.get("exclusivo"):
            continue
        productos.append({
            "name": c["name_claudio"],
            "weight": c["weight"].upper(),
            "price": int(round(c["price_costo"] * margin / 100)) * 100,
            "ganchos": c.get("ganchos", 0),
        })
    productos.sort(key=lambda p: (-p["ganchos"], p["name"].lower()))

    # USD rate referencial (puede ser dinámico desde mindicador.cl en producción web)
    USD_REF = 950

    pdf = MarcasExclusivasPDF()
    pdf.alias_nb_pages()
    pdf.cover()
    pdf.conditions_page()
    pdf.products_table(productos, USD_REF)

    out = os.path.join(here, "catalogo-maully-marcas-exclusivas-argentina.pdf")
    pdf.output(out)
    print(f"PDF Marcas Exclusivas Argentina: {out}")
    print(f"Productos exclusivos: {len(productos)}")
    print(f"Páginas: {pdf.page_no()}")


if __name__ == "__main__":
    main()
