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
}

# ── All products ──
products = [
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion 20 Kg","price":93500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion 1RA 20 Kg","price":93500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 3/4 Mujer 1RA 20 Kg","price":102300,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion Verano 20 Kg","price":104500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Trench Coat Chaqueta Trench 1RA 20 Kg","price":132000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaquetas Cuero 25 Kg","price":132000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo Hombre 3/4 Y Largo 1ra+ 25 Kg","price":137500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Gamulan Piloto 20 Kg","price":137500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 35 Kg","price":143000,"weight":"35kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka Chaqueta 1RA 40 Kg","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Gamulan 40KG","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Abrigo 3/4 Mujer + Blazer / Chaqueta Fashion 2x20 Kg","price":171600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 1ra+ 25 Kg","price":198000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Piloto Y Gamulan 1RA 20 Kg","price":242000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Bomber 1ra+ 25 Kg","price":286000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Marca Superdry 1ra+ 25 Kg","price":286000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX Oferta 20 Kg","price":342100,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Chaquetas Solo Marcas Deportivas Nino Juv 1RA 25 Kg","price":343200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 45 Kg","price":352000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Calvin Klein Chaquetas 1ra+ 25 Kg","price":363000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Oferta 25KG","price":363000,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Chaqueta Marca Zara Hym 1ra+ 25 Kg","price":399300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX Oferta 25KG","price":399300,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Polar Marca Columbia 1RA Directa 20 Kg","price":432300,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Outdoor / Trekking Columbia 1RA Seleccionado 10 Kg","price":433400,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia Oferta 20 Kg","price":433400,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq Oferta 20 Kg","price":433400,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Poleron Algodon Y Deportivo Columbia 10 Kg","price":445500,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Pantalones Outdoor Marca Columbia 10 Kg","price":445500,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX 1RA 20KG","price":542300,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia Northface MIX 1RA Directo 25 Kg","price":570900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia/ Northface 1RA 20 Kg","price":633600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/chaq Marca Columbia 1RA 20 Kg","price":649000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia MIX 1RA 25KG","price":656700,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Cortaviento Marca 25KG","price":662200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia/ Northface MIX Inv Oferta 40 Kg","price":685300,"weight":"40kg","tier":"oferta","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq 1RA 20 Kg","price":759000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Northface MIX Polar Parka Chaq 1RA 25 Kg","price":913000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia/ Northface MIX Inv 1RA Can 45 Kg","price":1084600,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Pescador Jeans Juvenil Mujer 1RA 40 Kg","price":66000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jardineras De Jeans 40 Kg","price":132000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Plus Size 1RA 40 Kg","price":132000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Blusa Jeans 1RA 22 Kg","price":148500,"weight":"22kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Chaqueta Mezclilla 1RA 45 Kg","price":181500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Hombre Plus Size 1RA 45 Kg","price":203500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Blusa Jeans 1RA 45 Kg","price":242000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Marca PREM Retorno 24 U","price":257400,"weight":"20kg","tier":"premium","new":True},
    {"cat":"jeans","name":"Jeans Levis Mujer 25 Kg","price":264000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Hombre 1RA 25KG","price":268400,"weight":"25kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Zara Mango Guess 24 U","price":411400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Levis Hombre 1RA 30 Kg","price":451000,"weight":"30kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Levis Mujer 50 Kg","price":495000,"weight":"50kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Jeans Mujer Marca PREM Retorno 50 U","price":511500,"weight":"20kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Poleras Y Blusas Marca Ardene Retorno 50 U","price":49500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Poleras Manga Larga Mujer 1RA 45 Kg","price":104500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Poleras Y Blusas Marca Ardene Retorno 150 U","price":110000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Blusa Mixta XL 45KG","price":110000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Blusa Franela 45 Kg 1RA","price":154000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Camisa Franela 45 Kg 1RA","price":154000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Manga Larga Hombre 1RA 40 Kg","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 10 Kg","price":165000,"weight":"10kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Tie Dye 1ra+ 22 Kg","price":198000,"weight":"22kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/la Oferta","price":203500,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co Oferta 25KG","price":214500,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Oferta 25KG","price":214500,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Hombre 1RA 10 Kg","price":228800,"weight":"10kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Dibujos Animados 1ra+/prem 20 Kg","price":231000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Camisa Marca Hombre Oferta","price":242000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Hombre Dibujos Animados 1ra+/prem 25 Kg","price":275000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Nino 1ra+/prem 25 Kg","price":308000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/la 1ra+/prem 25KG","price":336600,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 22 Kg","price":342100,"weight":"22kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre S/ma 1RA 25 Kg","price":352000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Cervezas 1ra+","price":377300,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Starwars / Marvel 1ra+ 20 Kg","price":377300,"weight":"20kg","tier":"primera","new":True},
    {"cat":"poleras","name":"MIX Verano Marca (poleras Y Short) Oferta 50 Kg","price":399300,"weight":"50kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera Marca Deportiva Hombre 1RA 25 Kg","price":468600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Hombre Marca M/co Multi Marca 25 Kg","price":495000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co C/cuello 1ra+/prem 25 Kg","price":495000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera Marca Hombre M/co Adidas Nike 1ra+/prem 25 Kg","price":513700,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Camisa Guayabera 1RA 45 Kg","price":628100,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron C/ Gorro 2DA 40 Kg","price":66000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro 45KG","price":88000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Oferta 45 Kg","price":93500,"weight":"45kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Polar 45 Kg","price":99000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Pijama Polar 1RA 45 Kg","price":137500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Pantalon Polar 1RA 45 Kg","price":137500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Heavy 1RA 40 Kg","price":154000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar 1RA Canada 45 Kg","price":159500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Chaqueta 45KG Kg","price":159500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron C/ Gorro Talla Grande 1RA 45 Kg","price":176000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro Hombre 40 Kg","price":203500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro Marca Oferta 25 Kg","price":203500,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia Oferta 12KG","price":211200,"weight":"12kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Poleron Canguro Marca Oferta 25 Kg","price":214500,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro 1RA Canada 45 Kg","price":214500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polerones Calvin Klein 20 U","price":220000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Corderito 1RA 45 Kg","price":220000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia 1RA 12KG","price":231000,"weight":"12kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Deportivo Premium 25KG","price":253000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"polerones","name":"Termico Ski Columbia 1RA 10 Kg","price":257400,"weight":"10kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Marca 1RA 25 Kg","price":336600,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Deportivo Marca 23KG","price":365200,"weight":"23kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polar Marcas PREM 1RA 25 Kg","price":388300,"weight":"25kg","tier":"premium","new":True},
    {"cat":"polerones","name":"Poleron Marca GAP Adulto 25 Kg","price":388300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Solo Marca 1RA 25KG","price":388300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Marca 1ra+ 25 Kg","price":411400,"weight":"25kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar Marca Columbia 1RA 20KG","price":423500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Polar / Parka/ Chaq Marca Columbia 1RA 25 Kg","price":656700,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Sweter Oferta 20 Kg","price":44000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"MIX Surtido Verano, Todo Producto 20 Kg Calidad Oferta","price":49500,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 10 Kg","price":49500,"weight":"10kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Hombre Y Mujer Verano 1RA Plus Size 20 Kg","price":88000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Ropa Mascota 10 Kg","price":88000,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 20 Kg","price":88000,"weight":"20kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Traje Bano Mujer Entero 1ra+ 20 Kg","price":93500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Traje Bano Mujer Entero Surtido 45 Kg","price":93500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Calza Y Pantalon Lycra 40 Kg","price":104500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Columbia/ Northface 3ra 10 Kg","price":104500,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon / Short 3/4 Outdoor 1RA 40 Kg","price":132000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hospital 25 Kg","price":137500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Marca Vestir Y Outdoor 15 Kg","price":148500,"weight":"15kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Juv Verano 20 Kg","price":148500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Mujer Verano EXTRA Linda 40 Kg","price":154000,"weight":"40kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Camisa Hombre 1RA 40 Kg","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzo Algodon 45KG","price":159500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Corset / Calzon Faja / Modeladores Otros 20KG","price":159500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hombre Verano 1RA Plus Size 40 Kg","price":165000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hombre Y Mujer Verano 1RA Plus Size 40 Kg","price":165000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Deportivo 1RA 20 Kg","price":165000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzos Plus Size 45 Kg","price":176000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Chaqueta Militar 20 Kg","price":181500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Abrigo 3/4 Mujer 1RA 2x20 Kg","price":182600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 10 Kg","price":188100,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Premium Under Armour 10 Kg","price":188100,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ropa Moto 1ra+ 15-18 Kg","price":203500,"weight":"18kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Marca Surtido 25 Kg","price":203500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzo Algodon 40KG","price":203500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Oferta 25 Kg","price":209000,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"Mixto Marca Hombre Oferta","price":209000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"Mujer EXTRA Linda Verano 45 Kg","price":209000,"weight":"45kg","tier":"extra","new":True},
    {"cat":"deportiva","name":"Cortaviento Y Poleron Deportivo Mixto 45 Kg","price":209000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Running 1RA 20 Kg","price":220000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Hospital Marca 1RA 20 Kg","price":220000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Brillo / Lentejuela 1ra+/prem 20 Kg","price":220000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"MIX Verano Pluz Size PREM 24 Kg","price":220000,"weight":"24kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 20 Kg","price":220000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marca Columbia 10 Kg","price":228800,"weight":"10kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Brillo / Lentejuela 1ra+/prem 25 Kg","price":253000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 25 Kg","price":253000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marca Vestir Y Outdoor 25KG","price":262900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Old Navy Nba, Nfl, Nhl, Russel,starter, Otras 1ra+ 25 Kg","price":275000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Surf / Playero Hombre 1RA 25 Kg","price":275000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Running 1RA 25 Kg","price":275000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Lino MIX 40 Kg","price":279400,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Deportivo Ninos / Juvenil 25 Kg","price":286000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Deportivo Mujer Premium 25KG","price":297000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Ropa Caza Y Pesca 1RA 25 Kg","price":302500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Corset / Calzon Faja / Modeladores Otros 45KG","price":308000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Deportivo 1RA 40 Kg","price":308000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon Raquelado 1RA 45 Kg","price":308000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Nike Adidas Surtido 20 Kg","price":313500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Ropa Caza Y Pesca 1RA PREM 25 Kg","price":324500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Pink 1RA 25 Kg","price":324500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Poleron Con Gorro Solo Marca 1RA 20KG","price":342100,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 20 Kg","price":342100,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marcas Premium Unisex 1RA 25 Kg","price":352000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Calvin Klein MIX 22-23 Kg","price":365200,"weight":"23kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Deportivo Solo Marcas 1ra+/prem 20 Kg","price":374000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Buzos Marca Algodon 1RA 23-25kg","price":377300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Buzos Marca Deportivos 25 Kg","price":388300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Oferta 2x25kg (50 Kg Total)","price":396000,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"deportiva","name":"Buzos Marca 1RA 25 Kg","price":399300,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Fila Champion Puma Reebok 1RA 25 Kg","price":399300,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Mujer Verano","price":423500,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Michael Kors 1RA 25KG","price":434500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Deportivo Solo Marcas 1ra+/prem 25 Kg","price":434500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Premium Under Armour 25 Kg","price":451000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Marca Under Armour Verano 25 Kg","price":451000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Marcas Premium 1ra-prem 20 Kg","price":451000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Deportivo Verano Solo Marcas 1RA 25 Kg","price":456500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marcas Premium Nike Adidas Deportivo 1RA 25 Kg","price":468600,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Premium Nike Adidas Deportivo 20 Kg","price":468600,"weight":"20kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Marcas Deportivas 1RA 25 Kg","price":495000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon Trekking / Senderismo Inv 1RA 40 Kg","price":513700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"MIX Marcas Premium 1ra-prem 25 Kg","price":528000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Columbia/ Northface MIX Inv 1RA Can 22 Kg","price":570900,"weight":"22kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon Trekking / Senderismo Verano 1RA 40 Kg","price":628100,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon Raquelado Marca 25KG","price":662200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Mixto Marca Deportivo Columbia The Northface 1ra+/prem 25 Kg","price":776600,"weight":"25kg","tier":"premium","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Oferta 2x20 Kg","price":66000,"weight":"20kg","tier":"oferta","new":True},
    {"cat":"sweaters","name":"Sweater Grueso 20 Kg","price":71500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1RA 20 Kg","price":77000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Largo 20KG","price":77000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1RA 45 Kg","price":137500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Cardigan Largo 1RA 20 Kg","price":148500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Cardigan 1RA 45 1RA Kg","price":159500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Ruana Poncho Fashion 1RA 45 Kg","price":187000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Poncho Fashion 1RA 45 Kg","price":203500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweater Shaggy 40 Kg","price":209000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweater Marca Hombre 1RA 25KG","price":308000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"sweaters","name":"Sweter Marca Mujer Premium 25KG","price":399300,"weight":"25kg","tier":"premium","new":True},
    {"cat":"vestidos","name":"Enteritos 1RA 20 Kg","price":93500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Sweter Largo 45KG","price":137500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Verano Juv 1ra+ 20 Kg","price":143000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Y Faldas 1ra+ EXTRA Linda 20 Kg","price":148500,"weight":"20kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Trench Coat Chaqueta Trench 1RA 25 Kg","price":170500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos EXTRA Linda 1RA 45 Kg","price":176000,"weight":"45kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Enteritos 1RA 40 Kg","price":176000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"MIX Brillo / Lentejuelas 25 Kg","price":247500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Vestidos Y Faldas 1ra+ EXTRA Linda 40 Kg","price":253000,"weight":"40kg","tier":"extra","new":True},
    {"cat":"vestidos","name":"Vestidos Fiesta PREM / Retorno 20 Kg","price":275000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"ski","name":"Parkas Sin Manga 1RA 25 Kg","price":143000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"ski","name":"Pantalon Ski Y Termicos Ninos 1RA 40 Kg","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Termico Ski Ninos 1RA 40 Kg","price":159500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Calzado Termico/nieve Adulto Mixto 20 Kg","price":160600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Coreana 1RA 20 Kg","price":171600,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Plus Size 45KG","price":176000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Termico Ski Adulto 1RA 45 Kg","price":209000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Pantalon Ski Y Termicos Adulto Can 45 Kg","price":214500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ski","name":"Calzado Termico/nieve Adulto 1RA 20 Kg","price":216700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Largas 1RA 40 Kg","price":216700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ski","name":"Ski Alta Montana (parkas Chaq Y Termicos) 1ra+ 20 Kg","price":220000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parka Alta Montana 20 Kg","price":242000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parka Treking / Alta Montana 25 Kg","price":286000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"ski","name":"Parkas Coreana 1RA 40 Kg","price":331100,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ninos","name":"MIX Nina Toda Estacion 1RA 10 Kg","price":49500,"weight":"10kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Disfraces Y Accesorios 20 Kg","price":99000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Parka Y Chaq Nino 1RA 40KG","price":154000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Disfraces 45 Kg","price":165000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Chaquetas Solo Marcas Deportivas Nino Juv 1RA 20 Kg","price":280500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"ninos","name":"Poleron Y Buzo Marca GAP Nino 25 Kg","price":302500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Funda Cobertor 18 U Retorno","price":66000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"hogar","name":"MIX Hogar 45 Kg","price":88000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"MIX Hogar 1RA 40 Kg Euro","price":110000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cobertor 45 Kg","price":110000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Frazada 1RA 40kg.","price":114400,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Funda Cobertor 36 U Retorno","price":132000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cobertor 1ra-prem 40KG","price":159500,"weight":"40kg","tier":"premium","new":True},
    {"cat":"hogar","name":"MIX Hogar 2x45kg","price":165000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Bata Toalla 1RA 45KG","price":176000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Toalla 25 Kg","price":188100,"weight":"25kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabanas Franela 1RA 45 Kg","price":192500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Cubrecolchon 1RA 45KG","price":203500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabana Color 40 Kg","price":216700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Sabana Blanca 40 Kg","price":216700,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Toalla 1RA 45 Kg","price":262900,"weight":"45kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Mixto 18 Kg","price":55000,"weight":"18kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg Oferta 10KG","price":160600,"weight":"10kg","tier":"oferta","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg 1RA 10 Kg","price":294800,"weight":"10kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg 1RA 20 Kg","price":550000,"weight":"20kg","tier":"primera","new":True},
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

    def header(self):
        if self.page_no() <= 2:
            return
        # Elegant thin header
        self.set_y(6)
        self.set_font("Helvetica", "", 6.5)
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
        self.set_font("Helvetica", "", 6)
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
        self.set_font("Helvetica", "", 11)
        self.set_text_color(*C_GOLD)
        self.cell(0, 6, "CATALOGO MAYORISTA  2026")
        self.ln(14)

        self.set_x(28)
        self.set_font("Helvetica", "B", 44)
        self.set_text_color(*C_WHITE)
        self.cell(0, 18, "IMPORTADORA")
        self.ln(18)
        self.set_x(28)
        self.set_font("Helvetica", "B", 52)
        self.set_text_color(*C_GOLD)
        self.cell(0, 22, "MAULLY")
        self.ln(28)

        # Tagline
        self.set_x(28)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(180, 178, 170)
        self.multi_cell(140, 5.5,
            "Fardos de ropa americana y europea de primera calidad.\n"
            "Mas de 40 anos de experiencia en el rubro textil.\n"
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
        self.set_font("Helvetica", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "WEB")
        self.set_xy(22, y + 9)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*C_GOLD)
        self.cell(50, 4, "importadoramaully.cl", link=BASE_URL)

        # WhatsApp card
        self.set_fill_color(30, 30, 48)
        self.rect(78, y, 54, card_h, "F")
        self.set_fill_color(*C_GREEN)
        self.rect(78, y, 54, 1, "F")
        self.set_xy(80, y + 4)
        self.set_font("Helvetica", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "WHATSAPP")
        self.set_xy(80, y + 9)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*C_GREEN)
        self.cell(50, 4, WA_NUM, link=WA_LINK)

        # Products count card
        self.set_fill_color(30, 30, 48)
        self.rect(136, y, 54, card_h, "F")
        self.set_fill_color(*C_WHITE)
        self.rect(136, y, 54, 1, "F")
        self.set_xy(138, y + 4)
        self.set_font("Helvetica", "", 6)
        self.set_text_color(*C_GRAY3)
        self.cell(50, 3, "CATALOGO")
        self.set_xy(138, y + 9)
        self.set_font("Helvetica", "B", 8)
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
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(0, 4, "SOBRE NOSOTROS", align="C")
        self.ln(6)
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*C_DARK)
        self.cell(0, 10, "Conoce Importadora Maully", align="C")
        self.ln(12)

        # Gold divider
        self.set_fill_color(*C_GOLD)
        self.rect(85, self.get_y(), 40, 0.8, "F")
        self.ln(8)

        # Description
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*C_GRAY5)
        self.set_x(24)
        self.multi_cell(162, 5.5,
            "Somos una empresa familiar chilena con mas de 40 anos de experiencia en el rubro textil "
            "y mas de 20 anos importando ropa directamente desde Canada, Estados Unidos y Europa. "
            "Nos hemos consolidado como referentes en el mercado de prendas importadas de calidad "
            "en Chile y Sudamerica, atendiendo a mas de 2.500 emprendedores y comerciantes.",
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
            ("Importacion Directa",  "Canada, EEUU y Europa"),
            ("Calidad Garantizada",  "Seleccion rigurosa"),
            ("Envio a Todo Chile",   "Todas las regiones"),
            ("Atencion WhatsApp",    "Asesoria personalizada"),
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
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(*C_DARK)
            self.cell(col_w - 6, 4, title)
            # Desc
            self.set_xy(x + 4, y + 7.5)
            self.set_font("Helvetica", "", 6.5)
            self.set_text_color(*C_GRAY4)
            self.cell(col_w - 6, 4, desc)
            if col == 2:
                self.set_y(y + 18)

        self.ln(6)

        # ── TIMELINE ──
        self.set_fill_color(*C_DARK)
        self.rect(14, self.get_y(), self.content_w, 10, "F")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*C_GOLD)
        self.set_x(14)
        self.cell(self.content_w, 10, "NUESTRA HISTORIA", align="C")
        self.ln(13)

        history = [
            ("1986", "Inicio en el rubro textil como empresa familiar."),
            ("2005", "Rutas directas desde Canada, EEUU y Europa."),
            ("2015", "Consolidacion nacional, envios a todo Chile."),
            ("2020", "Tienda online, YouTube y asesora Bea por WhatsApp."),
            ("2026", "+40 anos, +2.500 clientes, Chile y Sudamerica."),
        ]
        for i, (year, text) in enumerate(history):
            y = self.get_y()
            # Year circle
            self.set_fill_color(*C_DARK)
            self.rect(14, y, 20, 8, "F")
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(*C_GOLD)
            self.set_xy(14, y + 1)
            self.cell(20, 6, year, align="C")
            # Connector line
            self.set_fill_color(*C_GOLD)
            self.rect(36, y + 3.5, 4, 0.4, "F")
            # Text
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*C_GRAY5)
            self.set_xy(42, y + 1)
            self.cell(150, 6, text)
            self.ln(10)

        # ── LOCATIONS ──
        self.ln(2)
        self.set_fill_color(*C_DARK)
        self.rect(14, self.get_y(), self.content_w, 10, "F")
        self.set_font("Helvetica", "B", 9)
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
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*C_GOLD)
        self.set_xy(18, y + 1.5)
        self.cell(78, 5, "SANTIAGO")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*C_DARK)
        self.set_xy(18, y + 12)
        self.cell(78, 4, "Av. La Florida 9421")
        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*C_GRAY4)
        self.set_xy(18, y + 18)
        self.cell(78, 4, "Santiago de Chile")
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*C_BLUE)
        self.set_xy(18, y + 24)
        self.cell(78, 4, "Abrir en Google Maps  >", link=MAPS_STGO)

        # Pichilemu card
        self.set_fill_color(255, 255, 255)
        self.rect(110, y, card_w, 32, "F")
        self.set_fill_color(*C_DARK)
        self.rect(110, y, card_w, 8, "F")
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*C_GREEN)
        self.set_xy(114, y + 1.5)
        self.cell(78, 5, "PICHILEMU")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*C_DARK)
        self.set_xy(114, y + 12)
        self.cell(78, 4, "Av. Millaco 1172")
        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*C_GRAY4)
        self.set_xy(114, y + 18)
        self.cell(78, 4, "Pichilemu, Chile")
        self.set_font("Helvetica", "B", 7)
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
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*C_WHITE)
        self.set_xy(20, y + 1)
        self.cell(120, 9, name)
        # Count
        self.set_font("Helvetica", "", 7.5)
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

        self.set_font("Helvetica", "B", 6)
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
        if len(name) > 44:
            name = name[:42] + ".."
        is_new = p.get("new", False)

        pid = p.get("id", 0)
        link_url = f"{BASE_URL}/#producto-{pid}"

        self.set_x(14)
        if is_new:
            # NEW dot indicator
            self.set_fill_color(*C_RED)
            self.rect(16, y + 2.2, 2, 2, "F")
            self.set_x(14)
            self.set_font("Helvetica", "", 7.5)
            self.set_text_color(*C_DARK)
            self.cell(78, row_h, f"     {name}", link=link_url)
        else:
            self.set_font("Helvetica", "", 7.5)
            self.set_text_color(*C_GRAY5)
            self.cell(78, row_h, f"  {name}", link=link_url)

        # Weight
        self.set_font("Helvetica", "", 7)
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
        self.set_font("Helvetica", "B", 5.5)
        self.set_text_color(*C_WHITE)
        bw = self.get_string_width(label) + 5
        self.set_x(bx + (22 - bw) / 2)
        self.cell(bw, 4.5, label, fill=True, align="C")
        self.set_x(bx + 22)

        # Price CLP
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*C_DARK)
        self.cell(34, row_h, fmt_clp(p["price"]), align="R")

        # Price USD
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*C_GRAY3)
        self.cell(32, row_h, fmt_usd(p["price"]) + "  ", align="R")
        self.ln(row_h)

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
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*C_DARK)
        self.cell(30, 4, "REFERENCIAS")

        # Badge legends
        self.set_xy(18, y + 9)
        self.set_fill_color(*C_NAVY)
        self.set_font("Helvetica", "B", 5.5)
        self.set_text_color(*C_WHITE)
        self.cell(10, 4, "1ra", fill=True, align="C")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(35, 4, "  Primera seleccion")

        self.set_fill_color(*C_GOLD)
        self.set_text_color(*C_WHITE)
        self.set_font("Helvetica", "B", 5.5)
        self.cell(14, 4, "Premium", fill=True, align="C")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(35, 4, "  Marcas seleccionadas")

        self.set_fill_color(*C_GREEN)
        self.set_text_color(*C_WHITE)
        self.set_font("Helvetica", "B", 5.5)
        self.cell(12, 4, "Oferta", fill=True, align="C")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*C_GRAY5)
        self.cell(30, 4, "  Precio especial")

        # NEW indicator + click note
        self.set_xy(18, y + 16)
        self.set_fill_color(*C_RED)
        self.rect(18, y + 17.5, 2.5, 2.5, "F")
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*C_GRAY5)
        self.set_x(23)
        self.cell(50, 4, "Producto nuevo")
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(*C_BLUE)
        self.cell(0, 4, "Click en cada producto para ver detalles en la web")

        self.set_xy(18, y + 22)
        self.set_font("Helvetica", "", 6.5)
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
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*C_WHITE)
        self.cell(self.content_w, 8, "Cotiza tu fardo ahora", align="C")

        self.set_xy(14, y + 16)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*C_GREEN)
        self.cell(self.content_w, 7, f"WhatsApp: {WA_NUM}", align="C", link=WA_LINK)

        self.set_xy(14, y + 25)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*C_GOLD)
        self.cell(self.content_w, 6, "www.importadoramaully.cl  |  Envios a todo Chile y Latinoamerica", align="C", link=BASE_URL)


def main():
    for i, p in enumerate(products):
        p["id"] = i + 1

    pdf = CatalogoPDF()
    pdf.alias_nb_pages()

    pdf.cover_page()
    pdf.about_page()

    cat_order = ['chaquetas', 'jeans', 'poleras', 'polerones', 'deportiva',
                 'sweaters', 'vestidos', 'calzado', 'hogar', 'plussize']

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