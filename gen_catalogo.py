#!/usr/bin/env python3
"""Genera el catálogo PDF premium de Importadora Maully."""

from fpdf import FPDF
import os

# ── Config ──
USD_RATE = 950
BASE_URL = "https://www.importadoramaully.cl"
WA_LINK = "https://wa.me/56968442594"
WA_NUM = "+56 9 6844 2594"
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
    {"cat":"chaquetas","name":"Blazer / Chaqueta Fashion 1ra 20 Kg","price":93500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Calvin Klein Chaquetas 1ra+ 25 Kg","price":363000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 1ra+ 25 Kg","price":198000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Lenadora 45 Kg","price":352000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaqueta Piloto Y Gamulan 1ra 20 Kg","price":242000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Chaquetas Solo Marcas Dep. Nino Juv 1ra 25 Kg","price":341000,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia Mix 1ra 20kg","price":513700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia Mix Inv 1ra 20kg","price":524700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Columbia Mix Oferta 20 Kg","price":331100,"weight":"20kg","tier":"oferta"},
    {"cat":"chaquetas","name":"Columbia Mix Oferta 25kg","price":399300,"weight":"25kg","tier":"oferta"},
    {"cat":"chaquetas","name":"Columbia/ Northface Mix 1ra 10 Kg","price":342100,"weight":"10kg","tier":"primera"},
    {"cat":"chaquetas","name":"Columbia/ Northface Mix 1ra 20 Kg","price":599500,"weight":"20kg","tier":"primera"},
    {"cat":"chaquetas","name":"Cortaviento Chaq Ligera Columbia 1ra 10 Kg","price":427900,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Cortaviento Marca 25kg","price":662200,"weight":"25kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Gamulan 40kg","price":159500,"weight":"40kg","tier":"primera"},
    {"cat":"chaquetas","name":"Mix Columbia/NF Training Dep. 10 Kg","price":228800,"weight":"10kg","tier":"primera"},
    {"cat":"chaquetas","name":"Mix Columbia/NF Poleron Polar Parka 1ra 20 Kg","price":576400,"weight":"20kg","tier":"primera"},
    {"cat":"chaquetas","name":"Northface Mix Polar Parka 1ra 10 Kg","price":393800,"weight":"10kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Northface Mix Polar Parka 1ra 20 Kg","price":748000,"weight":"20kg","tier":"primera"},
    {"cat":"chaquetas","name":"Northface Mix Polar Parka Oferta 20 Kg","price":433400,"weight":"20kg","tier":"oferta"},
    {"cat":"chaquetas","name":"Outdoor / Trekking Columbia 1ra 10 Kg","price":404800,"weight":"10kg","tier":"primera"},
    {"cat":"chaquetas","name":"Pantalones Outdoor Columbia 10 Kg","price":427900,"weight":"10kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parka Alta Montana 20 Kg","price":242000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka Trekking / Alta Montana 25 Kg","price":275000,"weight":"25kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parka/Chaq Columbia Oferta 20 Kg","price":433400,"weight":"20kg","tier":"oferta"},
    {"cat":"chaquetas","name":"Parka/Chaq Columbia 1ra 20 Kg","price":576400,"weight":"20kg","tier":"primera","new":True},
    {"cat":"chaquetas","name":"Parka/Chaq Marca Oferta 25kg","price":363000,"weight":"25kg","tier":"oferta"},
    {"cat":"chaquetas","name":"Parkas Coreana 1ra 20 Kg","price":171600,"weight":"20kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parkas Coreana 1ra 40 Kg","price":331100,"weight":"40kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parkas Largas 1ra 40 Kg","price":222200,"weight":"40kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parkas Plus Size 45kg","price":176000,"weight":"45kg","tier":"primera"},
    {"cat":"chaquetas","name":"Parkas Sin Manga 1ra 25 Kg","price":143000,"weight":"25kg","tier":"primera"},
    {"cat":"chaquetas","name":"Poleron Algodon Y Dep. Columbia 10 Kg","price":404800,"weight":"10kg","tier":"primera"},
    {"cat":"chaquetas","name":"Poleron Polar Columbia 1ra 10 Kg","price":228800,"weight":"10kg","tier":"primera"},
    {"cat":"jeans","name":"Blusa Jeans 1ra 22 Kg","price":148500,"weight":"22kg","tier":"primera","new":True},
    {"cat":"jeans","name":"Blusa Jeans 1ra 45 Kg","price":242000,"weight":"45kg","tier":"primera"},
    {"cat":"jeans","name":"Chaqueta Mezclilla 1ra 45 Kg","price":181500,"weight":"45kg","tier":"primera"},
    {"cat":"jeans","name":"Jardineras De Jeans 40 Kg","price":132000,"weight":"40kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Mujer Plus Size 1ra 40 Kg","price":110000,"weight":"40kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Hombre 1ra 25kg","price":268400,"weight":"25kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Levis Hombre 1ra 30 Kg","price":433400,"weight":"30kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Levis Mujer 25 Kg","price":264000,"weight":"25kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Levis Mujer 50 Kg","price":440000,"weight":"50kg","tier":"primera"},
    {"cat":"jeans","name":"Jeans Mujer Marca Prem Retorno 24 U","price":257400,"weight":"24u","tier":"premium"},
    {"cat":"jeans","name":"Jeans Mujer Marca Prem Retorno 50 U","price":513700,"weight":"50u","tier":"premium"},
    {"cat":"jeans","name":"Pescador Jeans Juvenil Mujer 1ra 40 Kg","price":66000,"weight":"40kg","tier":"primera"},
    {"cat":"jeans","name":"Vestidos De Jeans 45 Kg","price":242000,"weight":"45kg","tier":"primera"},
    {"cat":"jeans","name":"Zara Abrigo 20u 15kg Aprox","price":319000,"weight":"15kg","tier":"primera"},
    {"cat":"poleras","name":"Abrigo Hombre 3/4 Y Largo 1ra+ 25 Kg","price":137500,"weight":"25kg","tier":"primera","new":True},
    {"cat":"poleras","name":"Blusa Franela 45 Kg 1ra","price":154000,"weight":"45kg","tier":"primera"},
    {"cat":"poleras","name":"Blusa Mixta Xl 45kg","price":110000,"weight":"45kg","tier":"primera"},
    {"cat":"poleras","name":"Camisa Franela 45 Kg 1ra","price":154000,"weight":"45kg","tier":"primera"},
    {"cat":"poleras","name":"Camisa Guayabera 1ra 10 Kg","price":165000,"weight":"10kg","tier":"primera"},
    {"cat":"poleras","name":"Camisa Guayabera 1ra 22 Kg","price":342100,"weight":"22kg","tier":"primera"},
    {"cat":"poleras","name":"Camisa Guayabera 1ra 45 Kg","price":628100,"weight":"45kg","tier":"primera"},
    {"cat":"poleras","name":"Camisa Marca Hombre Oferta","price":242000,"weight":"25kg","tier":"oferta"},
    {"cat":"poleras","name":"Mixto Marca Hombre Oferta","price":203500,"weight":"25kg","tier":"oferta"},
    {"cat":"poleras","name":"Polera Hombre Cervezas 1ra+","price":377300,"weight":"25kg","tier":"primera"},
    {"cat":"poleras","name":"Polera H. Dibujos Animados Prem 20 Kg","price":209000,"weight":"20kg","tier":"premium"},
    {"cat":"poleras","name":"Polera H. Dibujos Animados Prem 25 Kg","price":247500,"weight":"25kg","tier":"premium","new":True},
    {"cat":"poleras","name":"Polera H. Marca M/co Multi Marca 25 Kg","price":495000,"weight":"25kg","tier":"primera"},
    {"cat":"poleras","name":"Polera H. Starwars / Marvel 1ra+ 20 Kg","price":377300,"weight":"20kg","tier":"primera"},
    {"cat":"poleras","name":"Polera Marca Algodon Vestir Mixta 1ra 25 Kg","price":456500,"weight":"25kg","tier":"primera"},
    {"cat":"poleras","name":"Polera Marca Dep. Hombre 1ra 10 Kg","price":239800,"weight":"10kg","tier":"primera"},
    {"cat":"poleras","name":"Polera Marca Dep. Hombre 1ra 25 Kg","price":456500,"weight":"25kg","tier":"primera"},
    {"cat":"poleras","name":"Polera Marca Dep. Oferta 25kg","price":214500,"weight":"25kg","tier":"oferta","new":True},
    {"cat":"poleras","name":"Polera M/co Adidas Nike Prem 20 Kg","price":513700,"weight":"20kg","tier":"premium"},
    {"cat":"poleras","name":"Polera M/co C/cuello Prem 25 Kg","price":495000,"weight":"25kg","tier":"premium"},
    {"cat":"poleras","name":"Polera M/co Oferta 25kg","price":214500,"weight":"25kg","tier":"oferta"},
    {"cat":"poleras","name":"Polera M/la Prem 25kg","price":319000,"weight":"25kg","tier":"premium"},
    {"cat":"poleras","name":"Polera M/la Oferta","price":203500,"weight":"25kg","tier":"oferta"},
    {"cat":"poleras","name":"Polera Marca Hombre S/ma 1ra 25 Kg","price":352000,"weight":"25kg","tier":"primera"},
    {"cat":"poleras","name":"Polera Marca Nino Prem 25 Kg","price":275000,"weight":"25kg","tier":"premium"},
    {"cat":"poleras","name":"Polera Tie Dye 1ra+ 22 Kg","price":198000,"weight":"22kg","tier":"primera"},
    {"cat":"poleras","name":"Poleras Blusas Ardene Retorno 150 U","price":110000,"weight":"150u","tier":"oferta","new":True},
    {"cat":"polerones","name":"Pantalon Polar 1ra 45 Kg","price":137500,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Pijama Polar 1ra 45 Kg","price":137500,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Polar 45 Kg","price":99000,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Polar 1ra Canada 45 Kg","price":170500,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Polar Chaqueta 45kg","price":159500,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Polar Corderito 1ra 45 Kg","price":220000,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Polar Oferta 45 Kg","price":99000,"weight":"45kg","tier":"oferta"},
    {"cat":"polerones","name":"Poleron C/ Gorro Oferta 40 Kg","price":66000,"weight":"40kg","tier":"oferta"},
    {"cat":"polerones","name":"Poleron C/ Gorro Talla Grande 1ra 45 Kg","price":176000,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Poleron Con Gorro 1ra Canada 45 Kg","price":214500,"weight":"45kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Heavy 1ra 40 Kg","price":154000,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Con Gorro Solo Marca 1ra 25kg","price":388300,"weight":"25kg","tier":"primera"},
    {"cat":"polerones","name":"Poleron Polar/Parka/Chaq Columbia 1ra 20 Kg","price":559900,"weight":"20kg","tier":"primera"},
    {"cat":"polerones","name":"Poleron Polar Columbia 1ra 20kg","price":456500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Poleron Sin Gorro 20kg","price":44000,"weight":"20kg","tier":"primera"},
    {"cat":"polerones","name":"Poleron Sin Gorro 45kg","price":88000,"weight":"45kg","tier":"primera"},
    {"cat":"polerones","name":"Poleron Sin Gorro Hombre 40 Kg","price":203500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"polerones","name":"Polerones Calvin Klein 20 U","price":209000,"weight":"20u","tier":"primera"},
    {"cat":"polerones","name":"Termico Ski Columbia 1ra 10 Kg","price":239800,"weight":"10kg","tier":"primera"},
    {"cat":"polerones","name":"Zara Retorno Inv Lig 40 U","price":456500,"weight":"40u","tier":"oferta"},
    {"cat":"deportiva","name":"Buzos Marca 1ra 25 Kg","price":399300,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Buzos Marca Algodon 1ra 25kg","price":365200,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Buzos Marca Deportivos 25 Kg","price":388300,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Buzos Plus Size 45 Kg","price":176000,"weight":"45kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Camisa Hombre 1ra 40 Kg","price":159500,"weight":"40kg","tier":"primera"},
    {"cat":"deportiva","name":"Chaqueta Militar 20 Kg","price":181500,"weight":"20kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 20 Kg","price":220000,"weight":"20kg","tier":"premium"},
    {"cat":"deportiva","name":"Ciclismo 1ra/prem 25 Kg","price":258500,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Columbia Mix Inv 1ra 40kg","price":1004300,"weight":"40kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Cortaviento Y Poleron Dep. Mixto 45 Kg","price":209000,"weight":"45kg","tier":"primera"},
    {"cat":"deportiva","name":"Deportivo Mujer Premium 25kg","price":297000,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Deportivo Solo Marcas Prem 20 Kg","price":374000,"weight":"20kg","tier":"premium"},
    {"cat":"deportiva","name":"Deportivo Solo Marcas Prem 25 Kg","price":434500,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Mix Deportivo 1ra 20 Kg","price":165000,"weight":"20kg","tier":"primera"},
    {"cat":"deportiva","name":"Mix Deportivo 1ra 40 Kg","price":308000,"weight":"40kg","tier":"primera"},
    {"cat":"deportiva","name":"Mixto Dep. Marcas Premium 45 Kg","price":828300,"weight":"45kg","tier":"premium"},
    {"cat":"deportiva","name":"Mixto Nike Adidas Surtido 20 Kg","price":330000,"weight":"20kg","tier":"primera"},
    {"cat":"deportiva","name":"Mixto Marca Dep. Oferta 25 Kg","price":209000,"weight":"25kg","tier":"oferta"},
    {"cat":"deportiva","name":"Mixto Under Armour Prem 10 Kg","price":188100,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Under Armour Prem 25 Kg","price":451000,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Mixto Prem Dep. Ninos/Juv 25 Kg","price":286000,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Mixto Fila Champion Puma Reebok 10 Kg","price":177100,"weight":"10kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Mixto Fila Champion Puma Reebok 20 Kg","price":342100,"weight":"20kg","tier":"premium"},
    {"cat":"deportiva","name":"Mixto Fila Champion Puma Reebok 25 Kg","price":399300,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Mixto Nike Adidas Dep. Prem 25 Kg","price":468600,"weight":"25kg","tier":"premium"},
    {"cat":"deportiva","name":"Nino Marca 1ra 25kg","price":258500,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Pantalon Raquelado 1ra 45 Kg","price":297000,"weight":"45kg","tier":"primera"},
    {"cat":"deportiva","name":"Pantalon Raquelado Marca 12kg","price":262900,"weight":"12kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Pantalon Raquelado Marca 25kg","price":599500,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Pantalon Trekking Inv 1ra 40 Kg","price":513700,"weight":"40kg","tier":"primera"},
    {"cat":"deportiva","name":"Pantalon Trekking Verano 1ra 40 Kg","price":628100,"weight":"40kg","tier":"primera"},
    {"cat":"deportiva","name":"Premium Nike Adidas 20 Kg","price":456500,"weight":"20kg","tier":"premium"},
    {"cat":"deportiva","name":"Ropa Caza Y Pesca 1ra 25 Kg","price":302500,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Columbia 5 Kg","price":143000,"weight":"5kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Marca Surtido 25 Kg","price":203500,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Columbia 10 Kg","price":228800,"weight":"10kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Vestir Y Outdoor 15 Kg","price":148500,"weight":"15kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Vestir Y Outdoor 25kg","price":262900,"weight":"25kg","tier":"primera","new":True},
    {"cat":"deportiva","name":"Short Marcas Dep. 1ra 25 Kg","price":495000,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Marcas Prem Unisex 25 Kg","price":330000,"weight":"25kg","tier":"premium","new":True},
    {"cat":"deportiva","name":"Short Running 1ra 20 Kg","price":220000,"weight":"20kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Running 1ra 25 Kg","price":275000,"weight":"25kg","tier":"primera"},
    {"cat":"deportiva","name":"Short Surf / Playero Hombre 25 Kg","price":275000,"weight":"25kg","tier":"primera"},
    {"cat":"sweaters","name":"Cardigan 1ra 45 Kg","price":159500,"weight":"25kg","tier":"primera"},
    {"cat":"sweaters","name":"Cardigan Largo 1ra 20 Kg","price":148500,"weight":"20kg","tier":"primera"},
    {"cat":"sweaters","name":"Poncho Fashion 1ra 45 Kg","price":203500,"weight":"45kg","tier":"primera"},
    {"cat":"sweaters","name":"Ruana Poncho Fashion 1ra 45 Kg","price":187000,"weight":"45kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweater Grueso 20 Kg","price":71500,"weight":"20kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweater Marca Hombre 1ra 25kg","price":308000,"weight":"25kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweter Largo 22kg","price":77000,"weight":"22kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweter Marca Mujer Premium 25kg","price":374000,"weight":"25kg","tier":"premium"},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1ra 20 Kg","price":77000,"weight":"20kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweter Mujer Moderno 1ra 45 Kg","price":137500,"weight":"45kg","tier":"primera"},
    {"cat":"sweaters","name":"Sweter Mujer Oferta 2x20 Kg","price":66000,"weight":"20kg","tier":"oferta"},
    {"cat":"vestidos","name":"Abrigo 3/4 + Blazer Fashion 2x20 Kg","price":165000,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Abrigo 3/4 Mujer 1ra 20 Kg","price":99000,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Blazer / Chaqueta Fashion 20 Kg","price":99000,"weight":"20kg","tier":"primera","new":True},
    {"cat":"vestidos","name":"Brillo / Lentejuela Prem 25 Kg","price":253000,"weight":"25kg","tier":"premium"},
    {"cat":"vestidos","name":"Calza Y Pantalon Lycra 40 Kg","price":104500,"weight":"40kg","tier":"primera"},
    {"cat":"vestidos","name":"Chaqueta Marca Zara Hym 1ra+ 25 Kg","price":401500,"weight":"25kg","tier":"primera"},
    {"cat":"vestidos","name":"Corset / Faja / Modeladores 20kg","price":154000,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Corset / Faja / Modeladores 40kg","price":286000,"weight":"40kg","tier":"primera"},
    {"cat":"vestidos","name":"Enteritos 1ra 40 Kg","price":176000,"weight":"40kg","tier":"primera"},
    {"cat":"vestidos","name":"Enteritos 1ra 20 Kg","price":93500,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Gamulan Piloto 20 Kg","price":132000,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Jeans Zara 10 U","price":188100,"weight":"10u","tier":"primera","new":True},
    {"cat":"vestidos","name":"Michael Kors 1ra 25kg","price":434500,"weight":"25kg","tier":"primera"},
    {"cat":"vestidos","name":"Mix Brillo / Lentejuelas 25 Kg","price":247500,"weight":"25kg","tier":"primera"},
    {"cat":"vestidos","name":"Mix Mujer Juv Verano 20 Kg","price":148500,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Mix Mujer Verano Extra Linda 10 Kg","price":49500,"weight":"10kg","tier":"premium","new":True},
    {"cat":"vestidos","name":"Trench Coat 1ra 25 Kg","price":165000,"weight":"25kg","tier":"primera"},
    {"cat":"vestidos","name":"Vestidos Extra Linda 1ra 45 Kg","price":176000,"weight":"45kg","tier":"premium"},
    {"cat":"vestidos","name":"Vestidos Fiesta Prem 20 Kg","price":264000,"weight":"20kg","tier":"premium"},
    {"cat":"vestidos","name":"Vestidos Verano Juv 1ra+ 20 Kg","price":143000,"weight":"20kg","tier":"primera"},
    {"cat":"vestidos","name":"Vestidos Y Faldas Extra Linda 40 Kg","price":253000,"weight":"40kg","tier":"premium","new":True},
    {"cat":"calzado","name":"Calzado Marca Ugg 1ra 10 Kg","price":275000,"weight":"10kg","tier":"primera"},
    {"cat":"calzado","name":"Calzado Marca Ugg 1ra 20 Kg","price":539000,"weight":"20kg","tier":"primera"},
    {"cat":"calzado","name":"Calzado Marca Ugg Oferta 10kg","price":154000,"weight":"10kg","tier":"oferta"},
    {"cat":"calzado","name":"Calzado Mixto 18 Kg","price":55000,"weight":"18kg","tier":"primera"},
    {"cat":"calzado","name":"Calzado Termico/Nieve 1ra 20 Kg","price":216700,"weight":"20kg","tier":"primera","new":True},
    {"cat":"calzado","name":"Calzado Termico/Nieve Mixto 20 Kg","price":160600,"weight":"20kg","tier":"primera"},
    {"cat":"calzado","name":"Disfraces 45 Kg","price":159500,"weight":"45kg","tier":"primera"},
    {"cat":"calzado","name":"Disfraces Y Accesorios 20 Kg","price":71500,"weight":"20kg","tier":"primera"},
    {"cat":"calzado","name":"Ropa Mascota 10 Kg","price":88000,"weight":"10kg","tier":"primera"},
    {"cat":"calzado","name":"Zapatillas Hombre Marca 1ra 30 U","price":411400,"weight":"30u","tier":"primera"},
    {"cat":"calzado","name":"Zapatillas Jordan Y Basketball 1ra 25u","price":524700,"weight":"25u","tier":"primera"},
    {"cat":"calzado","name":"Buzo Algodon 40kg","price":203500,"weight":"40kg","tier":"primera","new":True},
    {"cat":"hogar","name":"Bata Toalla 1ra 45kg","price":176000,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Cobertor 1ra-prem 40kg","price":159500,"weight":"40kg","tier":"premium"},
    {"cat":"hogar","name":"Cobertor 45 Kg","price":110000,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Cubrecolchon 1ra 45kg","price":203500,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Frazada 1ra 40kg","price":108900,"weight":"40kg","tier":"primera"},
    {"cat":"hogar","name":"Funda Cobertor 18 U Retorno","price":60500,"weight":"18u","tier":"oferta"},
    {"cat":"hogar","name":"Mix Hogar 1ra 40 Kg Euro","price":110000,"weight":"40kg","tier":"primera"},
    {"cat":"hogar","name":"Mix Hogar 2x45kg","price":171600,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Mix Hogar 45 Kg","price":88000,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Sabana Blanca 40 Kg","price":216700,"weight":"40kg","tier":"primera"},
    {"cat":"hogar","name":"Sabana Color 40 Kg","price":216700,"weight":"40kg","tier":"primera"},
    {"cat":"hogar","name":"Sabanas Franela 1ra 45 Kg","price":192500,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Toalla 1ra 45 Kg","price":262900,"weight":"45kg","tier":"primera"},
    {"cat":"hogar","name":"Toalla 25 Kg","price":181500,"weight":"25kg","tier":"primera"},
    {"cat":"plussize","name":"Hombre Verano 1ra Plus Size 40 Kg","price":165000,"weight":"40kg","tier":"primera"},
    {"cat":"plussize","name":"H Y M Verano 1ra Plus Size 20 Kg","price":88000,"weight":"20kg","tier":"primera"},
    {"cat":"plussize","name":"H Y M Verano 1ra Plus Size 40 Kg","price":165000,"weight":"40kg","tier":"primera"},
    {"cat":"plussize","name":"Mix Mujer Verano Extra Linda 20 Kg","price":88000,"weight":"20kg","tier":"premium","new":True},
    {"cat":"plussize","name":"Mix Mujer Verano Extra Linda 40 Kg","price":154000,"weight":"40kg","tier":"premium"},
    {"cat":"plussize","name":"Mix Verano Plus Size Prem 24 Kg","price":220000,"weight":"24kg","tier":"premium"},
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

    out = os.path.join(os.path.dirname(__file__), "catalogo-maully.pdf")
    pdf.output(out)
    print(f"PDF generado: {out}")
    print(f"Total productos: {len(products)}")
    print(f"Paginas: {pdf.page_no()}")

if __name__ == "__main__":
    main()
