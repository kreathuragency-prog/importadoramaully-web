#!/usr/bin/env python3
"""Genera el catálogo PDF premium de Importadora Maully."""

from fpdf import FPDF
import os

# ── Config ──
USD_RATE = 950
BASE_URL = "https://www.importadoramaully.cl"
WA_LINK = "https://wa.me/56975155745"
WA_NUM = "+56 9 7515 5745"
MAPS_STGO = "https://www.google.com/maps/search/Av+La+Florida+9421+Santiago+Chile"
MAPS_PICH = "https://www.google.com/maps/search/Av+Millaco+1172+Pichilemu+Chile"

# ── Color palette ──
C_DARK    = (18, 18, 28)
C_NAVY    = (22, 33, 62)
C_GOLD    = (212, 175, 55)
C_GOLD_LT = (232, 200, 100)
C_WHITE   = (255, 255, 255)
C_CREAM   = (250, 247, 240)
C_GRAY1   = (245, 243, 238)
C_GRAY2   = (220, 215, 205)
C_GRAY3   = (160, 155, 145)
C_GRAY4   = (100, 95, 88)
C_GRAY5   = (60, 58, 52)
C_GREEN   = (37, 180, 90)
C_GREEN_D = (28, 120, 65)
C_BLUE    = (45, 100, 160)
C_RED     = (190, 50, 50)

# ── Category styling ──
CAT_INFO = {
    'chaquetas':  ('CHAQUETAS Y PARCAS',  (22, 33, 62)),
    'jeans':      ('JEANS',               (40, 55, 85)),
    'poleras':    ('POLERAS Y BLUSAS',    (95, 50, 120)),
    'polerones':  ('POLERONES Y POLAR',   (55, 45, 70)),
    'deportiva':  ('ROPA DEPORTIVA',      (160, 55, 40)),
    'sweaters':   ('SWEATERS',            (90, 65, 50)),
    'vestidos':   ('VESTIDOS Y FALDAS',   (140, 30, 70)),
    'calzado':    ('CALZADO Y OTROS',     (70, 50, 42)),
    'hogar':      ('HOGAR',               (60, 85, 95)),
    'plussize':   ('PLUS SIZE',           (120, 25, 65)),
    'ski':        ('ROPA SKI Y NIEVE',    (13, 71, 161)),
    'ninos':      ('ROPA NIÑOS Y NIÑAS',  (0, 150, 136)),
}

# ── All products ──
products = [
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion 20 Kg","price":97700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion 1RA 20 Kg","price":97700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 3/4 Mujer 1RA 20 Kg","price":106900,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion Verano 20 Kg","price":109200,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Trench Coat Chaqueta Trench 1RA 20 Kg","price":138000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaquetas Cuero 25 Kg","price":138000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo Hombre 3/4 Y Largo 1ra+ 25 Kg","price":143800,"weight":"25kg","tier":"primera","new":True,"ganchos":1},
    {"cat":"chaquetas","name":"Gamulan Piloto 20 Kg","price":143800,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 35 Kg","price":149500,"weight":"35kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka Chaqueta 1RA 40 Kg","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Gamulan 40KG","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 3/4 Mujer + Blazer / Chaqueta Fashion 2x20 Kg","price":179400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 1ra+ 25 Kg","price":207000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Piloto Y Gamulan 1RA 20 Kg","price":253000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Bomber 1ra+ 25 Kg","price":299000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Marca Superdry 1ra+ 25 Kg","price":299000,"weight":"25kg","tier":"primera","new":True,"ganchos":1},
    {"cat":"chaquetas","name":"Columbia MIX Oferta 20 Kg","price":357600,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Chaquetas Solo Marcas Deportivas Niño Juv 1RA 25 Kg","price":358800,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 45 Kg","price":368000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Calvin Klein Chaquetas 1ra+ 25 Kg","price":379500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Oferta 25KG","price":379500,"weight":"25kg","tier":"oferta","new":True,"ganchos":1},
    {"cat":"chaquetas","name":"Chaqueta Marca Zara Hym 1ra+ 25 Kg","price":417400,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX Oferta 25KG","price":417400,"weight":"25kg","tier":"oferta","new":True,"ganchos":1},
    {"cat":"chaquetas","name":"Parka/chaq Polar Marca Columbia 1RA Directa 20 Kg","price":451900,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Outdoor / Trekking Columbia 1RA Seleccionado 10 Kg","price":453100,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia Oferta 20 Kg","price":453100,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq Oferta 20 Kg","price":453100,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Poleron Algodón Y Deportivo Columbia 10 Kg","price":465700,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Pantalones Outdoor Marca Columbia 10 Kg","price":465700,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX 1RA 20KG","price":567000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia Northface MIX 1RA Directo 25 Kg","price":596800,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia/ Northface 1RA 20 Kg","price":662400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia 1RA 20 Kg","price":678500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX 1RA 25KG","price":686600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Cortaviento Marca 25KG","price":692300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia/ Northface MIX Inv Oferta 40 Kg","price":716400,"weight":"40kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq 1RA 20 Kg","price":793500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq 1RA 25 Kg","price":954500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia/ Northface MIX Inv 1RA Can 45 Kg","price":1133900,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Pescador Jeans Juvenil Mujer 1RA 40 Kg","price":69000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jardineras De Jeans 40 Kg","price":138000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Plus Size 1RA 40 Kg","price":138000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Blusa Jeans 1RA 22 Kg","price":155200,"weight":"22kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Chaqueta Mezclilla 1RA 45 Kg","price":189700,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Hombre Plus Size 1RA 45 Kg","price":212700,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Blusa Jeans 1RA 45 Kg","price":253000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Marca PREM Retorno 24 U","price":269100,"weight":"20kg","tier":"premium","new":True,"ganchos":1},
    {"cat":"jeans","name":"Jeans Levis Mujer 25 Kg","price":276000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Hombre 1RA 25KG","price":280600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Zara Mango Guess 24 U","price":430100,"weight":"20kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Levis Hombre 1RA 30 Kg","price":471500,"weight":"30kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Levis Mujer 50 Kg","price":517500,"weight":"50kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Marca PREM Retorno 50 U","price":534800,"weight":"20kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Poleras Y Blusas Marca Ardene Retorno 50 U","price":51700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Poleras Manga Larga Mujer 1RA 45 Kg","price":109200,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Poleras Y Blusas Marca Ardene Retorno 150 U","price":115000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Blusa Mixta XL 45KG","price":115000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Blusa Franela 45 Kg 1RA","price":161000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Camisa Franela 45 Kg 1RA","price":161000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Manga Larga Hombre 1RA 40 Kg","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 10 Kg","price":172500,"weight":"10kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Tie Dye 1ra+ 22 Kg","price":207000,"weight":"22kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/la Oferta","price":212700,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co Oferta 25KG","price":224200,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Oferta 25KG","price":224200,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Hombre 1RA 10 Kg","price":239200,"weight":"10kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Dibujos Animados 1ra+/prem 20 Kg","price":241500,"weight":"20kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Camisa Marca Hombre Oferta","price":253000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Hombre Dibujos Animados 1ra+/prem 25 Kg","price":287500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Niño 1ra+/prem 25 Kg","price":322000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/la 1ra+/prem 25KG","price":351900,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 22 Kg","price":357600,"weight":"22kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre S/ma 1RA 25 Kg","price":368000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Cervezas 1ra+","price":394400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Starwars / Marvel 1ra+ 20 Kg","price":394400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"MIX Verano Marca (poleras Y Short) Oferta 50 Kg","price":417400,"weight":"50kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Hombre 1RA 25 Kg","price":489900,"weight":"25kg","tier":"primera","new":True,"ganchos":1},
    {"cat":"poleras","name":"Polera Hombre Marca M/co Multi Marca 25 Kg","price":517500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co C/cuello 1ra+/prem 25 Kg","price":517500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co Adidas Nike 1ra+/prem 25 Kg","price":537000,"weight":"25kg","tier":"premium","new":True,"ganchos":1},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 45 Kg","price":656600,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron C/ Gorro 2DA 40 Kg","price":69000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro 45KG","price":92000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Oferta 45 Kg","price":97700,"weight":"45kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Polar 45 Kg","price":103500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Pijama Polar 1RA 45 Kg","price":143800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Pantalón Polar 1RA 45 Kg","price":143800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Heavy 1RA 40 Kg","price":161000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar 1RA Canadá 45 Kg","price":166800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Chaqueta 45KG Kg","price":166800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron C/ Gorro Talla Grande 1RA 45 Kg","price":184000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro Hombre 40 Kg","price":212700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro Marca Oferta 25 Kg","price":212700,"weight":"25kg","tier":"oferta","new":True,"ganchos":1},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia Oferta 12KG","price":220800,"weight":"12kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Poleron Canguro Marca Oferta 25 Kg","price":224200,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro 1RA Canadá 45 Kg","price":224200,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polerones Calvin Klein 20 U","price":230000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Corderito 1RA 45 Kg","price":230000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia 1RA 12KG","price":241500,"weight":"12kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Deportivo Premium 25KG","price":264500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"polerones","name":"Térmico Ski Columbia 1RA 10 Kg","price":269100,"weight":"10kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Marca 1RA 25 Kg","price":351900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Deportivo Marca 23KG","price":381800,"weight":"23kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Marcas PREM 1RA 25 Kg","price":405900,"weight":"25kg","tier":"premium","new":True},
    {"cat":"polerones","name":"Poleron Marca GAP Adulto 25 Kg","price":405900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Solo Marca 1RA 25KG","price":405900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Marca 1ra+ 25 Kg","price":430100,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia 1RA 20KG","price":442700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar / Parka/ Chaq Marca Columbia 1RA 25 Kg","price":686600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Sweter Oferta 20 Kg","price":46000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"MIX Surtido Verano, Todo Producto 20 Kg Calidad Oferta","price":51700,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 10 Kg","price":51700,"weight":"10kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Hombre Y Mujer Verano 1RA Plus Size 20 Kg","price":92000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Ropa Mascota 10 Kg","price":92000,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 20 Kg","price":92000,"weight":"20kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Traje Bano Mujer Entero 1ra+ 20 Kg","price":97700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Traje Bano Mujer Entero Surtido 45 Kg","price":97700,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Calza Y Pantalón Lycra 40 Kg","price":109200,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Columbia/ Northface 3ra 10 Kg","price":109200,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalón / Short 3/4 Outdoor 1RA 40 Kg","price":138000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hospital 25 Kg","price":143800,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Marca Vestir Y Outdoor 15 Kg","price":155200,"weight":"15kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Juv Verano 20 Kg","price":155200,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 40 Kg","price":161000,"weight":"40kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Camisa Hombre 1RA 40 Kg","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzo Algodón 45KG","price":166800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Corset / Calzón Faja / Modeladores Otros 20KG","price":166800,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hombre Verano 1RA Plus Size 40 Kg","price":172500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hombre Y Mujer Verano 1RA Plus Size 40 Kg","price":172500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Deportivo 1RA 20 Kg","price":172500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzos Plus Size 45 Kg","price":184000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Chaqueta Militar 20 Kg","price":189700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Abrigo 3/4 Mujer 1RA 2x20 Kg","price":190900,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 10 Kg","price":196600,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Premium Under Armour 10 Kg","price":196600,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ropa Moto 1ra+ 15-18 Kg","price":212700,"weight":"18kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Marca Surtido 25 Kg","price":212700,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzo Algodón 40KG","price":212700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Oferta 25 Kg","price":218500,"weight":"25kg","tier":"oferta","new":True,"ganchos":1},
    {"cat":"deportiva","name":"Mixto Marca Hombre Oferta","price":218500,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"Mujer EXTRA Linda Verano 45 Kg","price":218500,"weight":"45kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Cortaviento Y Poleron Deportivo Mixto 45 Kg","price":218500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Running 1RA 20 Kg","price":230000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hospital Marca 1RA 20 Kg","price":230000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Brillo / Lentejuela 1ra+/prem 20 Kg","price":230000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"MIX Verano Pluz Size PREM 24 Kg","price":230000,"weight":"24kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 20 Kg","price":230000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marca Columbia 10 Kg","price":239200,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Brillo / Lentejuela 1ra+/prem 25 Kg","price":264500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 25 Kg","price":264500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marca Vestir Y Outdoor 25KG","price":274800,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Old Navy Nba, Nfl, Nhl, Russel,starter, Otras 1ra+ 25 Kg","price":287500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Surf / Playero Hombre 1RA 25 Kg","price":287500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Running 1RA 25 Kg","price":287500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Lino MIX 40 Kg","price":292100,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Deportivo Niños / Juvenil 25 Kg","price":299000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Deportivo Mujer Premium 25KG","price":310500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ropa Caza Y Pesca 1RA 25 Kg","price":316200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Corset / Calzón Faja / Modeladores Otros 45KG","price":322000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Deportivo 1RA 40 Kg","price":322000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalón Raquelado 1RA 45 Kg","price":322000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Nike Adidas Surtido 20 Kg","price":327800,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Ropa Caza Y Pesca 1RA PREM 25 Kg","price":339200,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Pink 1RA 25 Kg","price":339200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Poleron Con Gorro Solo Marca 1RA 20KG","price":357600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 20 Kg","price":357600,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marcas Premium Unisex 1RA 25 Kg","price":368000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Calvin Klein MIX 22-23 Kg","price":381800,"weight":"23kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Deportivo Solo Marcas 1ra+/prem 20 Kg","price":391000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Buzos Marca Algodón 1RA 23-25kg","price":394400,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzos Marca Deportivos 25 Kg","price":405900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Oferta 2x25kg (50 Kg Total)","price":414000,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"Buzos Marca 1RA 25 Kg","price":417400,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 25 Kg","price":417400,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Mujer Verano","price":442700,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Michael Kors 1RA 25KG","price":454200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Deportivo Solo Marcas 1ra+/prem 25 Kg","price":454200,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Premium Under Armour 25 Kg","price":471500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Under Armour Verano 25 Kg","price":471500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Marcas Premium 1ra-prem 20 Kg","price":471500,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Deportivo Verano Solo Marcas 1RA 25 Kg","price":477200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Nike Adidas Deportivo 1RA 25 Kg","price":489900,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Premium Nike Adidas Deportivo 20 Kg","price":489900,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marcas Deportivas 1RA 25 Kg","price":517500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalón Trekking / Senderismo Inv 1RA 40 Kg","price":537000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Marcas Premium 1ra-prem 25 Kg","price":552000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Columbia/ Northface MIX Inv 1RA Can 22 Kg","price":596800,"weight":"22kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalón Trekking / Senderismo Verano 1RA 40 Kg","price":656600,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalón Raquelado Marca 25KG","price":692300,"weight":"25kg","tier":"primera","new":True,"ganchos":2},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Columbia The Northface 1ra+/prem 25 Kg","price":811900,"weight":"25kg","tier":"premium","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Oferta 2x20 Kg","price":69000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"sweaters","name":"Sweater Grueso 20 Kg","price":74800,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1RA 20 Kg","price":80500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Largo 20KG","price":80500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1RA 45 Kg","price":143800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Cardigan Largo 1RA 20 Kg","price":155200,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Cardigan 1RA 45 1RA Kg","price":166800,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Ruana Poncho Fashion 1RA 45 Kg","price":195500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Poncho Fashion 1RA 45 Kg","price":212700,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweater Shaggy 40 Kg","price":218500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweater Marca Hombre 1RA 25KG","price":322000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Marca Mujer Premium 25KG","price":417400,"weight":"25kg","tier":"premium","new":True},
    {"cat":"vestidos","name":"Enteritos 1RA 20 Kg","price":97700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Sweter Largo 45KG","price":143800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Verano Juv 1ra+ 20 Kg","price":149500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Y Faldas 1ra+ EXTRA Linda 20 Kg","price":155200,"weight":"20kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Trench Coat Chaqueta Trench 1RA 25 Kg","price":178200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos EXTRA Linda 1RA 45 Kg","price":184000,"weight":"45kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Enteritos 1RA 40 Kg","price":184000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"MIX Brillo / Lentejuelas 25 Kg","price":258700,"weight":"25kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Y Faldas 1ra+ EXTRA Linda 40 Kg","price":264500,"weight":"40kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Vestidos Fiesta PREM / Retorno 20 Kg","price":287500,"weight":"20kg","tier":"premium","new":True},
    {"cat":"ski","name":"Parkas Sin Manga 1RA 25 Kg","price":149500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"ski","name":"Pantalón Ski Y Térmicos Niños 1RA 40 Kg","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Térmico Ski Niños 1RA 40 Kg","price":166800,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Calzado Termico/nieve Adulto Mixto 20 Kg","price":167900,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Coreana 1RA 20 Kg","price":179400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Plus Size 45KG","price":184000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Térmico Ski Adulto 1RA 45 Kg","price":218500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Pantalón Ski Y Térmicos Adulto Can 45 Kg","price":224200,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Calzado Termico/nieve Adulto 1RA 20 Kg","price":226500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Largas 1RA 40 Kg","price":226500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Ski Alta Montana (parkas Chaq Y Termicos) 1ra+ 20 Kg","price":230000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parka Alta Montana 20 Kg","price":253000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parka Treking / Alta Montana 25 Kg","price":299000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Coreana 1RA 40 Kg","price":346200,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ninos","name":"MIX Niña Toda Estacion 1RA 10 Kg","price":51700,"weight":"10kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Disfraces Y Accesorios 20 Kg","price":103500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Parka Y Chaq Niño 1RA 40KG","price":161000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Disfraces 45 Kg","price":172500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Chaquetas Solo Marcas Deportivas Niño Juv 1RA 20 Kg","price":293200,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Poleron Y Buzo Marca GAP Niño 25 Kg","price":316200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Funda Cobertor 18 U Retorno","price":69000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"hogar","name":"MIX Hogar 45 Kg","price":92000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"MIX Hogar 1RA 40 Kg Euro","price":115000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cobertor 45 Kg","price":115000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Frazada 1RA 40kg.","price":119600,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Funda Cobertor 36 U Retorno","price":138000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cobertor 1ra-prem 40KG","price":166800,"weight":"40kg","tier":"premium","new":True},
    {"cat":"hogar","name":"MIX Hogar 2x45kg","price":172500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Bata Toalla 1RA 45KG","price":184000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Toalla 25 Kg","price":196600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabanas Franela 1RA 45 Kg","price":201200,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cubrecolchon 1RA 45KG","price":212700,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabana Color 40 Kg","price":226500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabana Blanca 40 Kg","price":226500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Toalla 1RA 45 Kg","price":274800,"weight":"45kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Mixto 18 Kg","price":57500,"weight":"18kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg Oferta 10KG","price":167900,"weight":"10kg","tier":"oferta","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg 1RA 10 Kg","price":308200,"weight":"10kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg 1RA 20 Kg","price":575000,"weight":"20kg","tier":"primera","new":True},
]
def fmt_clp(n):
    s = f"{n:,.0f}".replace(",", ".")
    return f"${s}"

def fmt_usd(n):
    usd = n / USD_RATE
    return f"US${usd:,.0f}"

# ── Helpers ──
def draw_rounded_rect(pdf, x, y, w, h, r, fill_color=None, draw_color=None):
    """Draw a rounded rectangle using arcs."""
    if fill_color:
        pdf.set_fill_color(*fill_color)
    if draw_color:
        pdf.set_draw_color(*draw_color)
    style = "DF" if fill_color and draw_color else ("F" if fill_color else "D")
    # Simplified: just use regular rect with small radius simulation
    pdf.rect(x, y, w, h, style)


class CatalogoPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=18)
        # Margin config
        self.l_margin = 14
        self.r_margin = 14
        self.content_w = 210 - 28  # 182mm usable
        # Unicode-capable font (soporta ñ y acentos)
        font_dir = "C:/Windows/Fonts"
        self.add_font("Body", "", os.path.join(font_dir, "DejaVuSans.ttf"))
        self.add_font("Body", "B", os.path.join(font_dir, "DejaVuSans-Bold.ttf"))
        self.add_font("Body", "I", os.path.join(font_dir, "DejaVuSans-Oblique.ttf"))
        self.add_font("Body", "BI", os.path.join(font_dir, "DejaVuSans-BoldOblique.ttf"))

    def header(self):
        if self.page_no() <= 2:
            return
        # Elegant thin header
        self.set_y(6)
        self.set_font("Body", "", 6.5)
        self.set_text_color(*C_GRAY3)
        self.cell(60, 5, "IMPORTADORA MAULLY", link=BASE_URL)
        self.cell(62, 5, "importadoramaully.cl", align="C", link=BASE_URL)
        self.cell(60, 5, WA_NUM, align="R", link=WA_LINK)
        self.ln(2)
        # Gold hairline
        self.set_draw_color(*C_GOLD)
        self.set_line_width(0.3)
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
        self.cell(60, 4, "Precios en CLP  |  Abril 2026")
        self.cell(62, 4, f"- {pg} -", align="C")
        self.cell(60, 4, "Sujeto a disponibilidad", align="R")

    # ══════════════════════════════════════════════
    #  COVER PAGE
    # ══════════════════════════════════════════════
    def cover_page(self):
        self.add_page()
        # Full dark background
        self.set_fill_color(*C_DARK)
        self.rect(0, 0, 210, 297, "F")

        # Top gold accent bar
        self.set_fill_color(*C_GOLD)
        self.rect(0, 0, 210, 3, "F")

        # Decorative vertical gold line left
        self.set_fill_color(*C_GOLD)
        self.rect(20, 30, 0.6, 90, "F")

        # Title block
        self.set_y(38)
        self.set_x(28)
        self.set_font("Body", "", 11)
        self.set_text_color(*C_GOLD)
        self.cell(0, 6, "CATALOGO MAYORISTA  2026")
        self.ln(14)

        self.set_x(28)
        self.set_font("Body", "B", 44)
        self.set_text_color(*C_WHITE)
        self.cell(0, 18, "IMPORTADORA")
        self.ln(18)
        self.set_x(28)
        self.set_font("Body", "B", 52)
        self.set_text_color(*C_GOLD)
        self.cell(0, 22, "MAULLY")
        self.ln(28)

        # Tagline
        self.set_x(28)
        self.set_font("Body", "", 10)
        self.set_text_color(180, 178, 170)
        self.multi_cell(140, 5.5,
            "Fardos de ropa americana y europea de primera calidad.\n"
            "Más de 40 años de experiencia en el rubro textil.\n"
            "Venta al por mayor para emprendedores de Chile y Latinoamerica.")
        self.ln(6)

        # Product image with frame
        img_path = os.path.join(os.path.dirname(__file__), "fardo-maully.jpg")
        if os.path.exists(img_path):
            ix, iy, iw = 30, self.get_y(), 150
            # Gold border frame
            self.set_draw_color(*C_GOLD)
            self.set_line_width(0.8)
            self.rect(ix - 1, iy - 1, iw + 2, 72, "D")
            self.image(img_path, x=ix, y=iy, w=iw)
            self.set_y(iy + 76)

        # Contact cards at bottom
        y = self.get_y() + 2
        card_h = 20

        # Web card
        self.set_fill_color(30, 30, 48)
        self.rect(20, y, 54, card_h, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(20, y, 54, 1, "F")  # gold top accent
        self.set_xy(22, y + 4)
        self.set_font("Body", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "WEB")
        self.set_xy(22, y + 9)
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_GOLD)
        self.cell(50, 4, "importadoramaully.cl", link=BASE_URL)

        # WhatsApp card
        self.set_fill_color(30, 30, 48)
        self.rect(78, y, 54, card_h, "F")
        self.set_fill_color(*C_GREEN)
        self.rect(78, y, 54, 1, "F")
        self.set_xy(80, y + 4)
        self.set_font("Body", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "WHATSAPP")
        self.set_xy(80, y + 9)
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_GREEN)
        self.cell(50, 4, WA_NUM, link=WA_LINK)

        # Products count card
        self.set_fill_color(30, 30, 48)
        self.rect(136, y, 54, card_h, "F")
        self.set_fill_color(*C_WHITE)
        self.rect(136, y, 54, 1, "F")
        self.set_xy(138, y + 4)
        self.set_font("Body", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "CATALOGO")
        self.set_xy(138, y + 9)
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_WHITE)
        self.cell(50, 4, f"{len(products)} productos")

        # Bottom gold bar
        self.set_fill_color(*C_GOLD)
        self.rect(0, 294, 210, 3, "F")

    # ══════════════════════════════════════════════
    #  ABOUT PAGE
    # ══════════════════════════════════════════════
    def about_page(self):
        self.add_page()
        # Page background cream
        self.set_fill_color(*C_CREAM)
        self.rect(0, 0, 210, 297, "F")
        # Header gold bar
        self.set_fill_color(*C_GOLD)
        self.rect(0, 0, 210, 3, "F")
        self.set_y(16)

        # Section title
        self.set_font("Body", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(0, 4, "SOBRE NOSOTROS", align="C")
        self.ln(6)
        self.set_font("Body", "B", 22)
        self.set_text_color(*C_DARK)
        self.cell(0, 10, "Conoce Importadora Maully", align="C")
        self.ln(12)

        # Gold divider
        self.set_fill_color(*C_GOLD)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(8)

        # Description
        self.set_font("Body", "", 10)
        self.set_text_color(*C_GRAY5)
        self.set_x(24)
        self.multi_cell(162, 5.5,
            "Somos una empresa familiar chilena con más de 40 años de experiencia en el rubro textil "
            "y más de 20 años importando ropa directamente desde Canadá, Estados Unidos y Europa. "
            "Nos hemos consolidado como referentes en el mercado de prendas importadas de calidad "
            "en Chile y Sudamérica, atendiendo a más de 2.500 emprendedores y comerciantes.",
            align="C")
        self.ln(6)

        # Image
        img_path = os.path.join(os.path.dirname(__file__), "fardo-maully.jpg")
        if os.path.exists(img_path):
            self.set_draw_color(*C_GOLD)
            self.set_line_width(0.5)
            ix = 35
            self.rect(ix - 1, self.get_y() - 1, 142, 57, "D")
            self.image(img_path, x=ix, y=self.get_y(), w=140)
            self.ln(60)

        # Features - 3x2 grid with icons
        features = [
            ("Importación Directa",  "Canadá, EEUU y Europa"),
            ("Calidad Garantizada",  "Selección rigurosa"),
            ("Envio a Todo Chile",   "Todas las regiones"),
            ("Atención WhatsApp",    "Asesoria personalizada"),
            ("Precios Mayoristas",   "Los mejores del mercado"),
            ("+2.500 Clientes",      "Emprendedores satisfechos"),
        ]
        col_w = 57
        gap = 5.5
        for i, (title, desc) in enumerate(features):
            col = i % 3
            x = 14 + col * (col_w + gap)
            if i % 3 == 0 and i > 0:
                self.set_y(self.get_y() + 2)
            y = self.get_y()

            # Card bg
            self.set_fill_color(255, 255, 255)
            self.rect(x, y, col_w, 16, "F")
            # Left gold accent
            self.set_fill_color(*C_GOLD)
            self.rect(x, y, 1.2, 16, "F")
            # Title
            self.set_xy(x + 4, y + 2)
            self.set_font("Body", "B", 7.5)
            self.set_text_color(*C_DARK)
            self.cell(col_w - 6, 4, title)
            # Desc
            self.set_xy(x + 4, y + 7.5)
            self.set_font("Body", "", 6.5)
            self.set_text_color(*C_GRAY4)
            self.cell(col_w - 6, 4, desc)
            if col == 2:
                self.set_y(y + 18)

        self.ln(6)

        # ── TIMELINE ──
        self.set_fill_color(*C_DARK)
        self.rect(14, self.get_y(), self.content_w, 10, "F")
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_GOLD)
        self.set_x(14)
        self.cell(self.content_w, 10, "NUESTRA HISTORIA", align="C")
        self.ln(13)

        history = [
            ("1986", "Inicio en el rubro textil como empresa familiar."),
            ("2005", "Rutas directas desde Canadá, EEUU y Europa."),
            ("2015", "Consolidacion nacional, envios a todo Chile."),
            ("2020", "Tienda online, YouTube y asesora Bea por WhatsApp."),
            ("2026", "+40 años, +2.500 clientes, Chile y Sudamérica."),
        ]
        for i, (year, text) in enumerate(history):
            y = self.get_y()
            # Year circle
            self.set_fill_color(*C_DARK)
            self.rect(14, y, 20, 8, "F")
            self.set_font("Body", "B", 7.5)
            self.set_text_color(*C_GOLD)
            self.set_xy(14, y + 1)
            self.cell(20, 6, year, align="C")
            # Connector line
            self.set_fill_color(*C_GOLD)
            self.rect(36, y + 3.5, 4, 0.4, "F")
            # Text
            self.set_font("Body", "", 8)
            self.set_text_color(*C_GRAY5)
            self.set_xy(42, y + 1)
            self.cell(150, 6, text)
            self.ln(10)

        # ── LOCATIONS ──
        self.ln(2)
        self.set_fill_color(*C_DARK)
        self.rect(14, self.get_y(), self.content_w, 10, "F")
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_GOLD)
        self.set_x(14)
        self.cell(self.content_w, 10, "NUESTRAS UBICACIONES", align="C")
        self.ln(14)

        y = self.get_y()
        card_w = 86

        # Santiago card
        self.set_fill_color(255, 255, 255)
        self.rect(14, y, card_w, 32, "F")
        self.set_fill_color(*C_DARK)
        self.rect(14, y, card_w, 8, "F")
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_GOLD)
        self.set_xy(18, y + 1.5)
        self.cell(78, 5, "SANTIAGO")
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_DARK)
        self.set_xy(18, y + 12)
        self.cell(78, 4, "Av. La Florida 9421")
        self.set_font("Body", "", 7.5)
        self.set_text_color(*C_GRAY4)
        self.set_xy(18, y + 18)
        self.cell(78, 4, "Santiago de Chile")
        self.set_font("Body", "B", 7)
        self.set_text_color(*C_BLUE)
        self.set_xy(18, y + 24)
        self.cell(78, 4, "Abrir en Google Maps  >", link=MAPS_STGO)

        # Pichilemu card
        self.set_fill_color(255, 255, 255)
        self.rect(110, y, card_w, 32, "F")
        self.set_fill_color(*C_DARK)
        self.rect(110, y, card_w, 8, "F")
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_GREEN)
        self.set_xy(114, y + 1.5)
        self.cell(78, 5, "PICHILEMU")
        self.set_font("Body", "B", 9)
        self.set_text_color(*C_DARK)
        self.set_xy(114, y + 12)
        self.cell(78, 4, "Av. Millaco 1172")
        self.set_font("Body", "", 7.5)
        self.set_text_color(*C_GRAY4)
        self.set_xy(114, y + 18)
        self.cell(78, 4, "Pichilemu, Chile")
        self.set_font("Body", "B", 7)
        self.set_text_color(*C_BLUE)
        self.set_xy(114, y + 24)
        self.cell(78, 4, "Abrir en Google Maps  >", link=MAPS_PICH)

        self.set_y(y + 36)

    # ══════════════════════════════════════════════
    #  CATEGORY HEADER
    # ══════════════════════════════════════════════
    def category_header(self, name, count, color):
        y = self.get_y()
        # Dark background
        self.set_fill_color(*color)
        self.rect(14, y, self.content_w, 11, "F")
        # Gold left accent
        self.set_fill_color(*C_GOLD)
        self.rect(14, y, 2, 11, "F")
        # Category name
        self.set_font("Body", "B", 11)
        self.set_text_color(*C_WHITE)
        self.set_xy(20, y + 1)
        self.cell(120, 9, name)
        # Count
        self.set_font("Body", "", 7.5)
        self.set_text_color(*C_GOLD_LT)
        self.cell(46, 9, f"{count} productos", align="R")
        self.ln(13)

    # ══════════════════════════════════════════════
    #  TABLE HEADER
    # ══════════════════════════════════════════════
    def table_header(self):
        self.set_fill_color(*C_GRAY1)
        self.set_draw_color(*C_GRAY2)
        self.set_line_width(0.2)
        y = self.get_y()
        self.rect(14, y, self.content_w, 6.5, "F")
        self.line(14, y + 6.5, 14 + self.content_w, y + 6.5)

        self.set_font("Body", "B", 6)
        self.set_text_color(*C_GRAY4)
        self.set_x(14)
        self.cell(78, 6.5, "  PRODUCTO")
        self.cell(16, 6.5, "PESO", align="C")
        self.cell(22, 6.5, "CALIDAD", align="C")
        self.cell(34, 6.5, "CLP", align="R")
        self.cell(32, 6.5, "USD  ", align="R")
        self.ln(7)

    # ══════════════════════════════════════════════
    #  PRODUCT ROW
    # ══════════════════════════════════════════════
    def product_row(self, p, idx):
        if self.get_y() > 268:
            self.add_page()
            self.table_header()

        y = self.get_y()
        even = idx % 2 == 0
        row_h = 6.5

        if even:
            self.set_fill_color(252, 250, 246)
            self.rect(14, y, self.content_w, row_h, "F")

        # Thin bottom line
        self.set_draw_color(*C_GRAY2)
        self.set_line_width(0.1)
        self.line(14, y + row_h, 14 + self.content_w, y + row_h)

        # Product name (clickable)
        name = p["name"]
        ganchos = p.get("ganchos", 0)
        # Tag de gancho compacto al lado del nombre
        gancho_suffix = f"  +{ganchos}g" if ganchos > 0 else ""
        max_name = 42 - len(gancho_suffix)
        if len(name) > max_name:
            name = name[:max_name - 2] + ".."
        is_new = p.get("new", False)

        pid = p.get("id", 0)
        link_url = f"{BASE_URL}/#producto-{pid}"

        self.set_x(14)
        if is_new:
            # NEW dot indicator
            self.set_fill_color(*C_RED)
            self.rect(16, y + 2.2, 2, 2, "F")
            self.set_x(14)
            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_DARK)
            self.cell(78, row_h, f"     {name}{gancho_suffix}", link=link_url)
        else:
            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_GRAY5)
            self.cell(78, row_h, f"  {name}{gancho_suffix}", link=link_url)
        # Indicador de gancho en color
        if ganchos > 0:
            self.set_text_color(234, 88, 12)  # naranja

        # Weight
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY3)
        self.cell(16, row_h, p["weight"], align="C")

        # Tier badge
        tier = p["tier"]
        if tier == "premium":
            bg, label = C_GOLD, "Premium"
        elif tier == "oferta":
            bg, label = C_GREEN, "Oferta"
        else:
            bg, label = C_NAVY, "1ra"

        bx = self.get_x()
        self.set_fill_color(*bg)
        self.set_font("Body", "B", 5.5)
        self.set_text_color(*C_WHITE)
        bw = self.get_string_width(label) + 5
        self.set_x(bx + (22 - bw) / 2)
        self.cell(bw, 4.5, label, fill=True, align="C")
        self.set_x(bx + 22)

        # Price CLP
        self.set_font("Body", "B", 8)
        self.set_text_color(*C_DARK)
        self.cell(34, row_h, fmt_clp(p["price"]), align="R")

        # Price USD
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY3)
        self.cell(32, row_h, fmt_usd(p["price"]) + "  ", align="R")
        self.ln(row_h)

    # ══════════════════════════════════════════════
    #  PÁGINA DEL CONCEPTO "GANCHO"
    # ══════════════════════════════════════════════
    def ganchos_page(self):
        self.add_page()
        # Page background cream
        self.set_fill_color(*C_CREAM)
        self.rect(0, 0, 210, 297, "F")
        # Top bar gold
        self.set_fill_color(*C_GOLD)
        self.rect(0, 0, 210, 3, "F")
        self.set_y(20)

        # Section eyebrow
        self.set_font("Body", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(0, 4, "MODALIDAD DE COMPRA", align="C")
        self.ln(6)

        # Title
        self.set_font("Body", "B", 28)
        self.set_text_color(*C_DARK)
        self.cell(0, 12, "¿Qué es un \"Gancho\"?", align="C")
        self.ln(14)

        # Gold divider
        self.set_fill_color(*C_GOLD)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(10)

        # Definición
        self.set_font("Body", "", 11)
        self.set_text_color(*C_GRAY5)
        self.set_x(20)
        self.multi_cell(170, 6,
            "Un GANCHO es un fardo de menor exclusividad que el cliente compra "
            "junto a un fardo top muy demandado. Algunos productos exclusivos "
            "de Maully se venden con la condición de sumar 1 o 2 ganchos en "
            "la misma compra.",
            align="C")
        self.ln(8)

        # Box "Por qué funciona así"
        box_y = self.get_y()
        self.set_fill_color(*C_GOLD_LT)
        self.rect(20, box_y, 170, 56, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(20, box_y, 4, 56, "F")
        self.set_y(box_y + 6)
        self.set_x(30)
        self.set_font("Body", "B", 12)
        self.set_text_color(*C_DARK)
        self.cell(160, 6, "¿Por qué funciona así?")
        self.ln(8)

        bullets = [
            ("Para Maully:", "rotamos bodega de variedad de stock y productos."),
            ("Para ti:", "accedes a fardos exclusivos que no salen sueltos y diversificas tu mix."),
            ("Beneficio mutuo:", "menor costo por kilo total combinando exclusivos + ganchos."),
        ]
        for label, txt in bullets:
            self.set_x(30)
            self.set_font("Body", "B", 10)
            self.set_text_color(*C_DARK)
            self.cell(40, 5, "• " + label)
            self.set_font("Body", "", 10)
            self.set_text_color(*C_GRAY5)
            self.multi_cell(120, 5, txt)
            self.ln(1)

        self.set_y(box_y + 64)

        # Qué fardos sirven como gancho
        self.set_x(20)
        self.set_font("Body", "B", 12)
        self.set_text_color(*C_DARK)
        self.cell(170, 6, "¿Qué fardos sirven como gancho?", align="C")
        self.ln(8)

        self.set_x(20)
        self.set_font("Body", "", 10.5)
        self.set_text_color(*C_GRAY5)
        self.multi_cell(170, 5.5,
            "Cualquier fardo etiquetado PREMIUM, MARCA, SEGUNDA o MARCA SEGUNDA. "
            "Son productos de excelente calidad — no son saldos. En el catálogo, "
            "los fardos top que requieren ganchos vienen marcados con \"+1 gancho\" "
            "o \"+2 ganchos\" junto a su precio.",
            align="C")
        self.ln(10)

        # Ejemplos box
        ex_y = self.get_y()
        self.set_fill_color(245, 235, 220)
        self.rect(30, ex_y, 150, 38, "F")
        self.set_y(ex_y + 5)
        self.set_x(30)
        self.set_font("Body", "B", 10)
        self.set_text_color(*C_DARK)
        self.cell(150, 5, "Ejemplos del catálogo:", align="C")
        self.ln(7)
        examples = [
            "JORDAN 25 kg  →  + 2 ganchos",
            "Pantalón Raquelado Marca 25 kg  →  + 2 ganchos",
            "REMERA HOMBRE MULTIMARCA 1RA  →  + 1 gancho",
            "OUTDOR MARCA 25 kg  →  + 1 gancho",
        ]
        self.set_font("Body", "", 9.5)
        self.set_text_color(*C_GRAY5)
        for ex in examples:
            self.set_x(30)
            self.cell(150, 5, ex, align="C")
            self.ln(5)

        # CTA
        self.ln(10)
        self.set_x(20)
        self.set_font("Body", "I", 10)
        self.set_text_color(*C_GOLD)
        self.multi_cell(170, 5,
            "Bea te ayuda a armar el combo perfecto según tu presupuesto. "
            "WhatsApp: " + WA_NUM,
            align="C")

    # ══════════════════════════════════════════════
    #  SECCIÓN ARGENTINA — productos puestos en Argentina
    # ══════════════════════════════════════════════
    def argentina_section(self, productos_arg):
        """productos_arg: lista de dicts {name, weight, price, ganchos}"""
        self.add_page()
        # Background sky-blue accent (Argentina colors hint)
        self.set_fill_color(*C_CREAM)
        self.rect(0, 0, 210, 297, "F")
        # Top stripe sky blue (Argentina flag)
        self.set_fill_color(117, 170, 219)  # celeste
        self.rect(0, 0, 210, 8, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(0, 8, 210, 1, "F")
        self.set_y(20)

        # Eyebrow
        self.set_font("Body", "", 8)
        self.set_text_color(117, 170, 219)
        self.cell(0, 4, "EXPORTACIÓN A ARGENTINA", align="C")
        self.ln(6)

        # Title
        self.set_font("Body", "B", 28)
        self.set_text_color(*C_DARK)
        self.cell(0, 12, "Productos puestos en Argentina", align="C")
        self.ln(14)

        self.set_fill_color(117, 170, 219)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(10)

        # Intro
        self.set_font("Body", "", 11)
        self.set_text_color(*C_GRAY5)
        self.set_x(20)
        self.multi_cell(170, 6,
            "Estos precios incluyen el costo del producto puesto en Argentina. "
            "El envío va aparte: hasta 10 kg con Starken, sobre 10 kg con "
            "transportistas privados que cobran por fardo. Pago 100% adelantado.",
            align="C")
        self.ln(6)

        # Box condiciones
        box_y = self.get_y()
        self.set_fill_color(*C_GOLD_LT)
        self.rect(20, box_y, 170, 50, "F")
        self.set_fill_color(117, 170, 219)
        self.rect(20, box_y, 4, 50, "F")
        self.set_y(box_y + 6)
        self.set_x(30)
        self.set_font("Body", "B", 12)
        self.set_text_color(*C_DARK)
        self.cell(160, 6, "Condiciones para Argentina")
        self.ln(8)

        bullets_arg = [
            ("Pago:", "100% por adelantado siempre. Aceptamos Global66 y USD."),
            ("Hasta 10 kg:", "envío con Starken, tarifa del courier (cobrada al retirar)."),
            ("Sobre 10 kg:", "transportistas privados — cobran por fardo, cotizar por WhatsApp."),
            ("Despacho:", "el flete lo paga el cliente; nosotros coordinamos desde Chile."),
            ("Visítanos:", "Av. La Florida 9421 (Santiago) o Berna 767 (Pichilemu)."),
        ]
        for label, txt in bullets_arg:
            self.set_x(30)
            self.set_font("Body", "B", 10)
            self.set_text_color(*C_DARK)
            self.cell(28, 5, "• " + label)
            self.set_font("Body", "", 10)
            self.set_text_color(*C_GRAY5)
            self.multi_cell(132, 5, txt)
            self.ln(0.5)

        self.set_y(box_y + 56)

        # Tabla de productos Argentina
        self.set_x(20)
        self.set_font("Body", "B", 13)
        self.set_text_color(*C_DARK)
        self.cell(170, 7, "Lista de precios — puestos en Argentina", align="C")
        self.ln(10)

        # Tabla header
        self.set_fill_color(*C_DARK)
        self.set_text_color(*C_WHITE)
        self.set_font("Body", "B", 7)
        self.set_x(14)
        self.cell(98, 6.5, "  PRODUCTO", fill=True)
        self.cell(18, 6.5, "PESO", align="C", fill=True)
        self.cell(36, 6.5, "PRECIO ARG", align="R", fill=True)
        self.cell(30, 6.5, "GANCHOS  ", align="R", fill=True)
        self.ln(8)

        # Filas
        for i, p in enumerate(productos_arg):
            if self.get_y() > 268:
                self.add_page()
                # repetir header
                self.set_fill_color(*C_DARK)
                self.set_text_color(*C_WHITE)
                self.set_font("Body", "B", 7)
                self.set_x(14)
                self.cell(98, 6.5, "  PRODUCTO", fill=True)
                self.cell(18, 6.5, "PESO", align="C", fill=True)
                self.cell(36, 6.5, "PRECIO ARG", align="R", fill=True)
                self.cell(30, 6.5, "GANCHOS  ", align="R", fill=True)
                self.ln(8)

            y = self.get_y()
            row_h = 6.5
            if i % 2 == 0:
                self.set_fill_color(252, 250, 246)
                self.rect(14, y, self.content_w, row_h, "F")

            self.set_draw_color(*C_GRAY2)
            self.set_line_width(0.1)
            self.line(14, y + row_h, 14 + self.content_w, y + row_h)

            # Name
            name = p["name"]
            if len(name) > 56:
                name = name[:54] + ".."
            self.set_x(14)
            self.set_font("Body", "", 7.5)
            self.set_text_color(*C_DARK)
            self.cell(98, row_h, "  " + name)

            # Weight
            self.set_font("Body", "", 7)
            self.set_text_color(*C_GRAY3)
            self.cell(18, row_h, p["weight"], align="C")

            # Price ARG
            self.set_font("Body", "B", 8)
            self.set_text_color(*C_DARK)
            self.cell(36, row_h, fmt_clp(p["price"]), align="R")

            # Ganchos
            ganchos = p.get("ganchos", 0)
            if ganchos > 0:
                self.set_font("Body", "B", 7.5)
                self.set_text_color(234, 88, 12)
                txt_g = f"+{ganchos} gancho{'s' if ganchos > 1 else ''}"
            else:
                self.set_font("Body", "", 7)
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
            "Precios en CLP. Conversión USD informativa al cierre de pedido. "
            "Pago 100% adelantado vía Global66 o USD para activar el despacho. "
            "Ganchos: producto adicional (premium / marca / segunda) que acompaña al fardo top.",
            align="C")
        # CTA visit
        self.ln(4)
        self.set_x(20)
        self.set_font("Body", "B", 10)
        self.set_text_color(*C_GOLD)
        self.cell(170, 5, "Te invitamos a conocernos en Av. La Florida 9421 (Santiago) o Berna 767 (Pichilemu)",
                  align="C", link=MAPS_STGO)

    # ══════════════════════════════════════════════
    #  LEGEND + CTA
    # ══════════════════════════════════════════════
    def legend_and_cta(self):
        if self.get_y() > 230:
            self.add_page()

        self.ln(6)
        y = self.get_y()

        # Legend box
        self.set_fill_color(*C_GRAY1)
        self.rect(14, y, self.content_w, 28, "F")
        self.set_fill_color(*C_GOLD)
        self.rect(14, y, self.content_w, 0.5, "F")

        self.set_xy(18, y + 3)
        self.set_font("Body", "B", 7)
        self.set_text_color(*C_DARK)
        self.cell(30, 4, "REFERENCIAS")

        # Badge legends
        self.set_xy(18, y + 9)
        self.set_fill_color(*C_NAVY)
        self.set_font("Body", "B", 5.5)
        self.set_text_color(*C_WHITE)
        self.cell(10, 4, "1ra", fill=True, align="C")
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(35, 4, "  Primera selección")

        self.set_fill_color(*C_GOLD)
        self.set_text_color(*C_WHITE)
        self.set_font("Body", "B", 5.5)
        self.cell(14, 4, "Premium", fill=True, align="C")
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(35, 4, "  Marcas selecciónadas")

        self.set_fill_color(*C_GREEN)
        self.set_text_color(*C_WHITE)
        self.set_font("Body", "B", 5.5)
        self.cell(12, 4, "Oferta", fill=True, align="C")
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(30, 4, "  Precio especial")

        # NEW indicator + click note
        self.set_xy(18, y + 16)
        self.set_fill_color(*C_RED)
        self.rect(18, y + 17.5, 2.5, 2.5, "F")
        self.set_font("Body", "", 7)
        self.set_text_color(*C_GRAY5)
        self.set_x(23)
        self.cell(50, 4, "Producto nuevo")
        self.set_font("Body", "B", 7)
        self.set_text_color(*C_BLUE)
        self.cell(0, 4, "Click en cada producto para ver detalles en la web")

        self.set_xy(18, y + 22)
        self.set_font("Body", "", 6.5)
        self.set_text_color(*C_GRAY3)
        self.cell(0, 4, f"Tipo de cambio referencial: 1 USD = ${USD_RATE} CLP  |  Precios sujetos a disponibilidad y stock")

        self.set_y(y + 34)

        # ── CTA Box ──
        self.ln(4)
        y = self.get_y()
        self.set_fill_color(*C_DARK)
        self.rect(14, y, self.content_w, 36, "F")
        # Gold top bar
        self.set_fill_color(*C_GOLD)
        self.rect(14, y, self.content_w, 1.5, "F")

        self.set_xy(14, y + 6)
        self.set_font("Body", "B", 16)
        self.set_text_color(*C_WHITE)
        self.cell(self.content_w, 8, "Cotiza tu fardo ahora", align="C")

        self.set_xy(14, y + 16)
        self.set_font("Body", "B", 12)
        self.set_text_color(*C_GREEN)
        self.cell(self.content_w, 7, f"WhatsApp: {WA_NUM}", align="C", link=WA_LINK)

        self.set_xy(14, y + 25)
        self.set_font("Body", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(self.content_w, 6, "www.importadoramaully.cl  |  Envios a todo Chile y Latinoamerica", align="C", link=BASE_URL)


def main():
    for i, p in enumerate(products):
        p["id"] = i + 1

    pdf = CatalogoPDF()
    pdf.alias_nb_pages()

    pdf.cover_page()
    pdf.about_page()
    pdf.ganchos_page()

    cat_order = ['chaquetas', 'jeans', 'poleras', 'polerones', 'deportiva',
                 'sweaters', 'vestidos', 'ski', 'ninos', 'calzado', 'hogar', 'plussize']

    for cat_id in cat_order:
        cat_products = [p for p in products if p["cat"] == cat_id]
        if not cat_products:
            continue

        cat_name, cat_color = CAT_INFO.get(cat_id, (cat_id.upper(), C_NAVY))

        if pdf.get_y() > 235:
            pdf.add_page()

        pdf.category_header(cat_name, len(cat_products), cat_color)
        pdf.table_header()

        for i, p in enumerate(cat_products):
            pdf.product_row(p, i)

        pdf.ln(8)

    # ── Sección Argentina ──
    try:
        import json as _json
        claudio = _json.load(open(os.path.join(os.path.dirname(__file__), "_claudio_prices.json"),
                                  encoding="utf-8"))
        margin_arg = claudio["_meta"].get("margen_aplicado", 1.15)
        productos_arg = []
        for c in claudio["productos"]:
            productos_arg.append({
                "name": c["name_claudio"],
                "weight": c["weight"].upper(),
                "price": int(round(c["price_costo"] * margin_arg / 100)) * 100,
                "ganchos": c.get("ganchos", 0),
            })
        # Ordenar: top exclusivos primero, luego alfabético
        productos_arg.sort(key=lambda p: (-p["ganchos"], p["name"].lower()))
        pdf.argentina_section(productos_arg)
    except Exception as e:
        print(f"AVISO: sección Argentina no agregada — {e}")

    pdf.legend_and_cta()

    out_dir = os.path.dirname(__file__)
    out_main = os.path.join(out_dir, "catalogo-maully-mayo-2026.pdf")
    pdf.output(out_main)
    # mantener alias estable para compatibilidad con links existentes
    import shutil
    shutil.copy(out_main, os.path.join(out_dir, "catalogo-maully.pdf"))
    print(f"PDF generado: {out_main} (+ alias catalogo-maully.pdf)")
    print(f"Total productos: {len(products)}")
    print(f"Paginas: {pdf.page_no()}")

if __name__ == "__main__":
    main()