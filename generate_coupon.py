from reportlab.lib.pagesizes import A5, landscape
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Output path
output_path = r"C:\Users\matia\importadoramaully web\cupon-maully2026.pdf"

# Colors
NAVY = HexColor("#1a1a2e")
GOLD = HexColor("#d4af37")
DARK_GOLD = HexColor("#b8960c")
LIGHT_GOLD = HexColor("#f0d060")
WHITE = HexColor("#ffffff")
CREAM = HexColor("#faf5e4")
SOFT_WHITE = HexColor("#e8e8e8")

# Page size - landscape A5 (wide banner format)
page_w, page_h = landscape(A5)

c = canvas.Canvas(output_path, pagesize=landscape(A5))
c.setTitle("Cupon Importadora Maully 2026")
c.setAuthor("Importadora Maully")

# ============================================================
# BACKGROUND - Full dark navy
# ============================================================
c.setFillColor(NAVY)
c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

# ============================================================
# DECORATIVE BORDER - Triple gold frame
# ============================================================
margin = 8 * mm

# Outer border
c.setStrokeColor(GOLD)
c.setLineWidth(2.5)
c.rect(margin, margin, page_w - 2 * margin, page_h - 2 * margin, fill=0, stroke=1)

# Middle border
c.setStrokeColor(DARK_GOLD)
c.setLineWidth(0.8)
c.rect(margin + 4 * mm, margin + 4 * mm, page_w - 2 * (margin + 4 * mm), page_h - 2 * (margin + 4 * mm), fill=0, stroke=1)

# Inner border
c.setStrokeColor(GOLD)
c.setLineWidth(1.5)
c.rect(margin + 6 * mm, margin + 6 * mm, page_w - 2 * (margin + 6 * mm), page_h - 2 * (margin + 6 * mm), fill=0, stroke=1)

# ============================================================
# CORNER DECORATIONS - Gold diamond accents at corners
# ============================================================
def draw_corner_accent(cx, cy, size=5*mm):
    """Draw a small gold diamond at a corner."""
    c.setFillColor(GOLD)
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.5)
    path = c.beginPath()
    path.moveTo(cx, cy + size)
    path.lineTo(cx + size, cy)
    path.lineTo(cx, cy - size)
    path.lineTo(cx - size, cy)
    path.close()
    c.drawPath(path, fill=1, stroke=1)

corner_offset = margin + 5 * mm
diamond_s = 3.5 * mm
draw_corner_accent(corner_offset, corner_offset, diamond_s)
draw_corner_accent(page_w - corner_offset, corner_offset, diamond_s)
draw_corner_accent(corner_offset, page_h - corner_offset, diamond_s)
draw_corner_accent(page_w - corner_offset, page_h - corner_offset, diamond_s)

# ============================================================
# DECORATIVE HORIZONTAL LINES (gold separators)
# ============================================================
def draw_ornamental_line(y, width_pct=0.7):
    """Draw a centered ornamental gold line with end dots."""
    line_w = page_w * width_pct
    x_start = (page_w - line_w) / 2
    x_end = x_start + line_w
    
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.7)
    c.line(x_start + 8*mm, y, x_end - 8*mm, y)
    
    # End circles
    c.setFillColor(GOLD)
    c.circle(x_start + 6*mm, y, 1.5*mm, fill=1, stroke=0)
    c.circle(x_end - 6*mm, y, 1.5*mm, fill=1, stroke=0)
    
    # Smaller inner circles
    c.circle(x_start + 2*mm, y, 0.8*mm, fill=1, stroke=0)
    c.circle(x_end - 2*mm, y, 0.8*mm, fill=1, stroke=0)

# ============================================================
# TOP SECTION - "IMPORTADORA MAULLY" header
# ============================================================
y_cursor = page_h - 32 * mm

# Small stars / decorative text above header
c.setFillColor(GOLD)
c.setFont("Helvetica", 9)
stars_text = "- - -   E S T .   2 0 2 4   - - -"
c.drawCentredString(page_w / 2, y_cursor + 14 * mm, stars_text)

# Main header
c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 30)
c.drawCentredString(page_w / 2, y_cursor, "IMPORTADORA MAULLY")

# Ornamental line below header
draw_ornamental_line(y_cursor - 6 * mm, 0.65)

# ============================================================
# COUPON LABEL
# ============================================================
y_cursor -= 18 * mm

c.setFillColor(SOFT_WHITE)
c.setFont("Helvetica", 11)
c.drawCentredString(page_w / 2, y_cursor, "C U P O N   D E   D E S C U E N T O")

# ============================================================
# BIG COUPON CODE with gold background banner
# ============================================================
y_cursor -= 20 * mm

# Gold banner behind the code
banner_h = 18 * mm
banner_w = 180 * mm
banner_x = (page_w - banner_w) / 2
banner_y = y_cursor - 3 * mm

# Draw gold rounded rectangle
c.setFillColor(GOLD)
c.roundRect(banner_x, banner_y, banner_w, banner_h, 4 * mm, fill=1, stroke=0)

# Inner dark rectangle for contrast
inner_pad = 1.5 * mm
c.setFillColor(NAVY)
c.roundRect(banner_x + inner_pad, banner_y + inner_pad, 
            banner_w - 2 * inner_pad, banner_h - 2 * inner_pad, 
            3 * mm, fill=1, stroke=0)

# Gold border on inner
c.setStrokeColor(GOLD)
c.setLineWidth(1)
c.roundRect(banner_x + inner_pad, banner_y + inner_pad, 
            banner_w - 2 * inner_pad, banner_h - 2 * inner_pad, 
            3 * mm, fill=0, stroke=1)

# Coupon code text
c.setFillColor(GOLD)
c.setFont("Courier-Bold", 36)
c.drawCentredString(page_w / 2, banner_y + 4.5 * mm, "MAULLY2026")

# ============================================================
# DISCOUNT PERCENTAGE
# ============================================================
y_cursor -= 22 * mm

c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 22)
c.drawCentredString(page_w / 2, y_cursor, "10% DE DESCUENTO")

# ============================================================
# MAIN MESSAGE
# ============================================================
y_cursor -= 14 * mm

c.setFillColor(SOFT_WHITE)
c.setFont("Helvetica", 11)
msg = "Presenta este cupon en bodega y obten inmediatamente un 10% de descuento"
c.drawCentredString(page_w / 2, y_cursor, msg)

# Ornamental line
draw_ornamental_line(y_cursor - 6 * mm, 0.55)

# ============================================================
# SUBTITLE - Location info
# ============================================================
y_cursor -= 17 * mm

c.setFillColor(GOLD)
c.setFont("Helvetica", 9)
subtitle = "Valido en todas las compras presenciales  -  Av. La Florida 9421, Santiago"
c.drawCentredString(page_w / 2, y_cursor, subtitle)

# ============================================================
# CONTACT INFO
# ============================================================
y_cursor -= 11 * mm

c.setFillColor(SOFT_WHITE)
c.setFont("Helvetica", 8)
contact = "www.importadoramaully.cl  |  WhatsApp: +56 9 7515 5745  |  Fijo: 22 8332 667"
c.drawCentredString(page_w / 2, y_cursor, contact)

# ============================================================
# FOOTER NOTE - Terms
# ============================================================
y_cursor -= 10 * mm

c.setFillColor(HexColor("#888888"))
c.setFont("Helvetica-Oblique", 7)
footer = "Cupon valido hasta agotar stock. No acumulable con otras promociones."
c.drawCentredString(page_w / 2, y_cursor, footer)

# ============================================================
# SAVE
# ============================================================
c.save()

# Verify
if os.path.exists(output_path):
    size_kb = os.path.getsize(output_path) / 1024
    print(f"PDF generado exitosamente: {output_path}")
    print(f"Tamano: {size_kb:.1f} KB")
else:
    print("ERROR: No se pudo generar el PDF")
