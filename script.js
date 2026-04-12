// ============ DATA ============
const WA_NUMBER = '56968442594';
const USD_RATE = 950;
const BRAND_TAGS=['Columbia','North Face','Nike','Adidas','Zara','Levis','Calvin Klein','Tommy','Ralph Lauren','Patagonia','Gap','H&M','Puma','Reebok','Under Armour'];
function getProductTags(p){
  const tags=[];const n=(p.name||'').toLowerCase();
  BRAND_TAGS.forEach(b=>{if(n.includes(b.toLowerCase()))tags.push(b);});
  if(n.includes('verano')||n.includes('short'))tags.push('Verano');
  if(n.includes('invierno')||n.includes('ski')||n.includes('polar'))tags.push('Invierno');
  if(n.includes('mujer')||n.includes('dama'))tags.push('Mujer');
  if(n.includes('hombre'))tags.push('Hombre');
  if(n.includes('nino')||n.includes('niña')||n.includes('ninos'))tags.push('Ninos');
  if(n.includes('outdoor')||n.includes('trekking'))tags.push('Outdoor');
  return tags.slice(0,4);
}
const categories = [
{id:'chaquetas',name:'Chaquetas y Parcas',icon:'fa-vest-patches',range:'$45,000 - $250,000',gradient:'linear-gradient(135deg,#2c3e50,#3498db)',img:'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&q=80'},
{id:'jeans',name:'Jeans',icon:'fa-user',range:'$40,000 - $180,000',gradient:'linear-gradient(135deg,#34495e,#2980b9)',img:'https://images.unsplash.com/photo-1542272604-787c3835535d?w=600&q=80'},
{id:'poleras',name:'Poleras y Blusas',icon:'fa-shirt',range:'$35,000 - $150,000',gradient:'linear-gradient(135deg,#8e44ad,#3498db)',img:'https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=600&q=80'},
{id:'polerones',name:'Polerones y Polar',icon:'fa-mitten',range:'$45,000 - $200,000',gradient:'linear-gradient(135deg,#2c3e50,#e74c3c)',img:'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600&q=80'},
{id:'deportiva',name:'Ropa Deportiva',icon:'fa-person-running',range:'$50,000 - $250,000',gradient:'linear-gradient(135deg,#e74c3c,#f39c12)',img:'https://images.unsplash.com/photo-1539185441755-769473a23570?w=600&q=80'},
{id:'vestidos',name:'Vestidos y Faldas',icon:'fa-wand-magic-sparkles',range:'$40,000 - $160,000',gradient:'linear-gradient(135deg,#e91e63,#9c27b0)',img:'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&q=80'},
{id:'ninos',name:'Ropa Ninos',icon:'fa-child-reaching',range:'$35,000 - $150,000',gradient:'linear-gradient(135deg,#00bcd4,#4caf50)',img:'https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=600&q=80'},
{id:'ski',name:'Ropa Ski',icon:'fa-person-skiing',range:'$60,000 - $300,000',gradient:'linear-gradient(135deg,#0d47a1,#42a5f5)',img:'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=600&q=80'},
{id:'calzado',name:'Calzado',icon:'fa-shoe-prints',range:'$50,000 - $250,000',gradient:'linear-gradient(135deg,#5d4037,#8d6e63)',img:'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600&q=80'},
{id:'hogar',name:'Hogar',icon:'fa-house',range:'$35,000 - $120,000',gradient:'linear-gradient(135deg,#607d8b,#90a4ae)',img:'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80'},
{id:'sweaters',name:'Sweaters',icon:'fa-temperature-low',range:'$40,000 - $170,000',gradient:'linear-gradient(135deg,#795548,#d7ccc8)',img:'https://images.unsplash.com/photo-1434389677669-e08b4cda3a5b?w=600&q=80'},
{id:'pantalones',name:'Pantalones',icon:'fa-scissors',range:'$40,000 - $160,000',gradient:'linear-gradient(135deg,#455a64,#78909c)',img:'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&q=80'},
{id:'plussize',name:'Plus Size',icon:'fa-expand',range:'$45,000 - $180,000',gradient:'linear-gradient(135deg,#ad1457,#e91e63)',img:'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600&q=80'},
];

// Product images by category - real stock photos
const CAT_IMGS = {
  chaquetas:'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&q=80',
  jeans:'https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=600&q=80',
  poleras:'https://images.unsplash.com/photo-1562157873-818bc0726f68?w=600&q=80',
  polerones:'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600&q=80',
  deportiva:'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600&q=80',
  vestidos:'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&q=80',
  calzado:'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=600&q=80',
  hogar:'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&q=80',
  sweaters:'https://images.unsplash.com/photo-1434389677669-e08b4cda3a00?w=600&q=80',
  pantalones:'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=600&q=80',
  plussize:'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=600&q=80',
  ski:'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=600&q=80',
  ninos:'https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=600&q=80',
};
function getProductImg(cat){ return CAT_IMGS[cat] || 'https://images.unsplash.com/photo-1558171813-01ed3d751e0c?w=600&q=80'; }
const GALLERY_IMGS = {
  chaquetas:['https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&q=75','https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400&q=75','https://images.unsplash.com/photo-1544923246-77307dd270b1?w=400&q=75'],
  jeans:['https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&q=75','https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400&q=75','https://images.unsplash.com/photo-1604176354204-9268737828e4?w=400&q=75'],
  poleras:['https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&q=75','https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=400&q=75','https://images.unsplash.com/photo-1503341504253-dff4f94032fc?w=400&q=75'],
  polerones:['https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400&q=75','https://images.unsplash.com/photo-1578768079470-0a4536e2b7d3?w=400&q=75','https://images.unsplash.com/photo-1614975059251-992f11792571?w=400&q=75'],
  deportiva:['https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&q=75','https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=400&q=75','https://images.unsplash.com/photo-1544966503-7cc5ac882d5d?w=400&q=75'],
  vestidos:['https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&q=75','https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400&q=75','https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400&q=75'],
  calzado:['https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&q=75','https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&q=75','https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400&q=75'],
  hogar:['https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=400&q=75','https://images.unsplash.com/photo-1616627561839-074385245ff6?w=400&q=75','https://images.unsplash.com/photo-1513694203232-719a280e022f?w=400&q=75'],
  sweaters:['https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=400&q=75','https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=400&q=75','https://images.unsplash.com/photo-1434389677669-e08b4cda3a00?w=400&q=75'],
  pantalones:['https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400&q=75','https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400&q=75','https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400&q=75'],
  plus_size:['https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=400&q=75','https://images.unsplash.com/photo-1559563458-527698bf5295?w=400&q=75','https://images.unsplash.com/photo-1525507119028-ed4c629a60a3?w=400&q=75'],
  ninos:['https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=400&q=75','https://images.unsplash.com/photo-1503944583220-79d8926ad5e2?w=400&q=75','https://images.unsplash.com/photo-1471286174890-9c112ffca5b4?w=400&q=75'],
  ski:['https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&q=75','https://images.unsplash.com/photo-1605540436563-5bca919ae766?w=400&q=75','https://images.unsplash.com/photo-1517483000871-1dbf64a6e1c6?w=400&q=75'],
};
function getProductGallery(cat,name){
  const base = GALLERY_IMGS[cat] || GALLERY_IMGS['chaquetas'];
  // Rotate images based on product name hash for variety
  const hash = name.split('').reduce((a,c)=>a+c.charCodeAt(0),0);
  const offset = hash % base.length;
  return [...base.slice(offset), ...base.slice(0,offset)];
}
const MAULLY_IMG = 'fardo-maully.jpg';
const products = [
{id:1,cat:'chaquetas',name:'Blazer / Chaqueta Fashion 1ra 20 Kg',price:93500,origPrice:100000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:2,cat:'chaquetas',name:'Calvin Klein Chaquetas 1ra+ 25 Kg',price:363000,origPrice:380000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:3,cat:'chaquetas',name:'Chaqueta Lenadora 1ra+ 25 Kg',price:198000,origPrice:220000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:4,cat:'chaquetas',name:'Chaqueta Lenadora 45 Kg',price:352000,origPrice:350000,weight:'45kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:5,cat:'chaquetas',name:'Chaqueta Piloto Y Gamulan 1ra 20 Kg',price:242000,origPrice:300000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:6,cat:'chaquetas',name:'Chaquetas Solo Marcas Deportivas Nino Juv 1ra 25 Kg',price:341000,origPrice:350000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:7,cat:'chaquetas',name:'Columbia Mix 1ra 20kg',price:513700,origPrice:617000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:8,cat:'chaquetas',name:'Columbia Mix Inv 1ra 20kg',price:524700,origPrice:517000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:9,cat:'chaquetas',name:'Columbia Mix Oferta 20 Kg',price:331100,origPrice:361000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:10,cat:'chaquetas',name:'Columbia Mix Oferta 25kg',price:399300,origPrice:413000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:11,cat:'chaquetas',name:'Columbia/ Northface Mix 1ra 10 Kg',price:342100,origPrice:331000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:12,cat:'chaquetas',name:'Columbia/ Northface Mix 1ra 20 Kg',price:599500,origPrice:600000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:13,cat:'chaquetas',name:'Cortaviento Chaq Ligera Columbia 1ra 10 Kg',price:427900,origPrice:564000,weight:'10kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:14,cat:'chaquetas',name:'Cortaviento Marca 25kg',price:662200,origPrice:722000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:15,cat:'chaquetas',name:'Gamulan 40kg',price:159500,origPrice:220000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:16,cat:'chaquetas',name:'Mix Columbia/ Northface Training Deportivo 10 Kg',price:228800,origPrice:358000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:17,cat:'chaquetas',name:'Mix Columbia/ Northface Poleron Polar Parka Chaqueta 1ra 20 Kg',price:576400,origPrice:569000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:18,cat:'chaquetas',name:'Northface Mix Polar Parka Chaq 1ra 10 Kg',price:393800,origPrice:513000,weight:'10kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:19,cat:'chaquetas',name:'Northface Mix Polar Parka Chaq 1ra 20 Kg',price:748000,origPrice:775000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:20,cat:'chaquetas',name:'Northface Mix Polar Parka Chaq Oferta 20 Kg',price:433400,origPrice:414000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:21,cat:'chaquetas',name:'Outdoor / Trekking Columbia 1ra Seleccionado 10 Kg',price:404800,origPrice:423000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:22,cat:'chaquetas',name:'Pantalones Outdoor Marca Columbia 10 Kg',price:427900,origPrice:434000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:23,cat:'chaquetas',name:'Parka Alta Montana 20 Kg',price:242000,origPrice:280000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:24,cat:'chaquetas',name:'Parka Treking / Alta Montana 25 Kg',price:275000,origPrice:320000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:25,cat:'chaquetas',name:'Parka/chaq Marca Columbia Oferta 20 Kg',price:433400,origPrice:494000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:26,cat:'chaquetas',name:'Parka/chaq Marca Columbia 1ra 20 Kg',price:576400,origPrice:619000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:27,cat:'chaquetas',name:'Parka/chaq Marca Oferta 25kg',price:363000,origPrice:360000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:28,cat:'chaquetas',name:'Parkas Coreana 1ra 20 Kg',price:171600,origPrice:186000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:29,cat:'chaquetas',name:'Parkas Coreana 1ra 40 Kg',price:331100,origPrice:361000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:30,cat:'chaquetas',name:'Parkas Largas 1ra 40 Kg',price:222200,origPrice:267000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:31,cat:'chaquetas',name:'Parkas Plus Size 45kg',price:176000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:32,cat:'chaquetas',name:'Parkas Sin Manga 1ra 25 Kg',price:143000,origPrice:145000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:33,cat:'chaquetas',name:'Poleron Algodon Y Deportivo Columbia 10 Kg',price:404800,origPrice:413000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:34,cat:'chaquetas',name:'Poleron Polar Columbia 1ra 10 Kg',price:228800,origPrice:258000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:35,cat:'jeans',name:'Blusa Jeans 1ra 22 Kg',price:148500,origPrice:185000,weight:'22kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:36,cat:'jeans',name:'Blusa Jeans 1ra 45 Kg',price:242000,origPrice:335000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:37,cat:'jeans',name:'Chaqueta Mezclilla 1ra 45 Kg',price:181500,origPrice:180000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:38,cat:'jeans',name:'Jardineras De Jeans 40 Kg',price:132000,origPrice:250000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:39,cat:'jeans',name:'Jeans Mujer Plus Size 1ra 40 Kg',price:110000,origPrice:120000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:40,cat:'jeans',name:'Jeans Hombre 1ra 25kg',price:268400,origPrice:259000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:41,cat:'jeans',name:'Jeans Levis Hombre 1ra 30 Kg',price:433400,origPrice:464000,weight:'30kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:42,cat:'jeans',name:'Jeans Levis Mujer 25 Kg',price:264000,origPrice:300000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:43,cat:'jeans',name:'Jeans Levis Mujer 50 Kg',price:440000,origPrice:550000,weight:'50kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:44,cat:'jeans',name:'Jeans Mujer Marca Prem Retorno 24 U',price:257400,origPrice:259000,weight:'24u',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:45,cat:'jeans',name:'Jeans Mujer Marca Prem Retorno 50 U',price:513700,origPrice:517000,weight:'50u',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:46,cat:'jeans',name:'Pescador Jeans Juvenil Mujer 1ra 40 Kg',price:66000,origPrice:90000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:47,cat:'jeans',name:'Vestidos De Jeans 45 Kg',price:242000,origPrice:300000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:48,cat:'jeans',name:'Zara Abrigo 20u 15kg Aprox',price:319000,origPrice:429000,weight:'15kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:49,cat:'poleras',name:'Blusa Franela 45 Kg 1ra',price:154000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:50,cat:'poleras',name:'Blusa Mixta Xl 45kg',price:110000,origPrice:180000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:51,cat:'poleras',name:'Camisa Franela 45 Kg 1ra',price:154000,origPrice:145000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:52,cat:'poleras',name:'Camisa Guayabera 1ra 10 Kg',price:165000,origPrice:200000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:53,cat:'poleras',name:'Camisa Guayabera 1ra 22 Kg',price:342100,origPrice:361000,weight:'22kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:54,cat:'poleras',name:'Camisa Guayabera 1ra 45 Kg',price:628100,origPrice:671000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:55,cat:'poleras',name:'Polera Hombre Cervezas 1ra+',price:377300,origPrice:368000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:56,cat:'poleras',name:'Polera Hombre Dibujos Animados 1ra+/prem 20 Kg',price:209000,origPrice:230000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:57,cat:'poleras',name:'Polera Hombre Dibujos Animados 1ra+/prem 25 Kg',price:247500,origPrice:270000,weight:'25kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:58,cat:'poleras',name:'Polera Hombre Marca M/co Multi Marca 25 Kg',price:495000,origPrice:480000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:59,cat:'poleras',name:'Polera Hombre Starwars / Marvel 1ra+ 20 Kg',price:377300,origPrice:353000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:60,cat:'poleras',name:'Polera Marca Algodon / Vestir Mixta 1ra 25 Kg',price:456500,origPrice:465000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:61,cat:'poleras',name:'Polera Marca Deportiva Hombre 1ra 10 Kg',price:239800,origPrice:428000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:62,cat:'poleras',name:'Polera Marca Deportiva Hombre 1ra 25 Kg',price:456500,origPrice:435000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:63,cat:'poleras',name:'Polera Marca Deportiva Oferta 25kg',price:214500,origPrice:225000,weight:'25kg',tier:'oferta',badge:'oferta',isNew:true,img:MAULLY_IMG},
{id:64,cat:'poleras',name:'Polera Marca Hombre M/co C/cuello 1ra+/prem 25 Kg',price:495000,origPrice:490000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:65,cat:'poleras',name:'Polera Marca Hombre M/la 1ra+/prem 25kg',price:319000,origPrice:350000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:66,cat:'poleras',name:'Polera Marca Hombre S/ma 1ra 25 Kg',price:352000,origPrice:375000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:67,cat:'poleras',name:'Polera Marca Nino 1ra+/prem 25 Kg',price:275000,origPrice:340000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:68,cat:'poleras',name:'Polera Tie Dye 1ra+ 22 Kg',price:198000,origPrice:260000,weight:'22kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:69,cat:'poleras',name:'Poleras Y Blusas Marca Ardene Retorno 150 U',price:110000,origPrice:170000,weight:'150u',tier:'oferta',badge:'oferta',isNew:true,img:MAULLY_IMG},
{id:70,cat:'poleras',name:'Poleras Y Blusas Marca Ardene Retorno 50 U',price:49500,origPrice:85000,weight:'50u',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:71,cat:'polerones',name:'Pantalon Polar 1ra 45 Kg',price:137500,origPrice:165000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:72,cat:'polerones',name:'Pijama Polar 1ra 45 Kg',price:137500,origPrice:150000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:73,cat:'polerones',name:'Polar 45 Kg',price:99000,origPrice:185000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:74,cat:'polerones',name:'Polar 1ra Canada 45 Kg',price:170500,origPrice:175000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:75,cat:'polerones',name:'Polar Chaqueta 45kg Kg',price:159500,origPrice:170000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:76,cat:'polerones',name:'Polar Corderito 1ra 45 Kg',price:220000,origPrice:250000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:77,cat:'polerones',name:'Polar Oferta 45 Kg',price:99000,origPrice:150000,weight:'45kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:78,cat:'polerones',name:'Poleron C/ Gorro Oferta 40 Kg',price:66000,origPrice:150000,weight:'40kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:79,cat:'polerones',name:'Poleron C/ Gorro Talla Grande 1ra 45 Kg',price:176000,origPrice:230000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:80,cat:'polerones',name:'Poleron Con Gorro 1ra Canada 45 Kg',price:214500,origPrice:280000,weight:'45kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:81,cat:'polerones',name:'Poleron Con Gorro Heavy 1ra 40 Kg',price:154000,origPrice:160000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:82,cat:'polerones',name:'Poleron Con Gorro Solo Marca 1ra 25kg',price:388300,origPrice:363000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:83,cat:'polerones',name:'Poleron Polar / Parka/ Chaq Marca Columbia 1ra 20 Kg',price:559900,origPrice:599000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:84,cat:'polerones',name:'Poleron Polar Marca Columbia 1ra 20kg',price:456500,origPrice:435000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:85,cat:'polerones',name:'Poleron Sin Gorro 20kg',price:44000,origPrice:90000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:86,cat:'polerones',name:'Poleron Sin Gorro 45kg',price:88000,origPrice:150000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:87,cat:'polerones',name:'Poleron Sin Gorro Hombre 40 Kg',price:203500,origPrice:200000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:88,cat:'polerones',name:'Polerones Calvin Klein 20 U',price:209000,origPrice:300000,weight:'20u',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:89,cat:'polerones',name:'Termico Ski Columbia 1ra 10 Kg',price:239800,origPrice:283000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:90,cat:'polerones',name:'Zara Retorno Inv Lig 40 U',price:456500,origPrice:465000,weight:'40u',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:91,cat:'deportiva',name:'Buzos Marca 1ra 25 Kg',price:399300,origPrice:383000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:92,cat:'deportiva',name:'Buzos Marca Algodon 1ra 23-25kg',price:365200,origPrice:342000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:93,cat:'deportiva',name:'Buzos Marca Deportivos 25 Kg',price:388300,origPrice:388000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:94,cat:'deportiva',name:'Buzos Plus Size 45 Kg',price:176000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:95,cat:'deportiva',name:'Camisa Hombre 1ra 40 Kg',price:159500,origPrice:160000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:96,cat:'deportiva',name:'Chaqueta Militar 20 Kg',price:181500,origPrice:180000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:97,cat:'deportiva',name:'Ciclismo 1ra/prem 20 Kg',price:220000,origPrice:230000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:98,cat:'deportiva',name:'Ciclismo 1ra/prem 25 Kg',price:258500,origPrice:260000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:99,cat:'deportiva',name:'Columbia Mix Inv 1ra 40kg',price:1004300,origPrice:1013000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:100,cat:'deportiva',name:'Cortaviento Y Poleron Deportivo Mixto 45 Kg',price:209000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:101,cat:'deportiva',name:'Deportivo Mujer Premium 25kg',price:297000,origPrice:310000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:102,cat:'deportiva',name:'Deportivo Solo Marcas 1ra+/prem 20 Kg',price:374000,origPrice:400000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:103,cat:'deportiva',name:'Deportivo Solo Marcas 1ra+/prem 25 Kg',price:434500,origPrice:450000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:104,cat:'deportiva',name:'Mix Deportivo 1ra 20 Kg',price:165000,origPrice:200000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:105,cat:'deportiva',name:'Mix Deportivo 1ra 40 Kg',price:308000,origPrice:380000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:106,cat:'deportiva',name:'Mixto Deportivo Marcas Premium 45 Kg',price:828300,origPrice:828000,weight:'45kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:107,cat:'deportiva',name:'Mixto Marca Deportivo Nike Adidas Surtido 20 Kg',price:330000,origPrice:320000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:108,cat:'deportiva',name:'Mixto Marca Deportivo Oferta 25 Kg',price:209000,origPrice:250000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:109,cat:'deportiva',name:'Mixto Marca Deportivo Oferta 2x25kg (50 Kg Total)',price:396000,origPrice:420000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:110,cat:'deportiva',name:'Mixto Marca Premium Under Armour 10 Kg',price:188100,origPrice:206000,weight:'10kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:111,cat:'deportiva',name:'Mixto Marca Premium Under Armour 25 Kg',price:451000,origPrice:465000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:112,cat:'deportiva',name:'Mixto Marcas Premium Deportivo Ninos / Juvenil 25 Kg',price:286000,origPrice:300000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:113,cat:'deportiva',name:'Short Running 1ra 20 Kg',price:220000,origPrice:250000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:114,cat:'deportiva',name:'Short Running 1ra 20 Kg (v3)',price:220000,origPrice:250000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:115,cat:'deportiva',name:'Mixto Marcas Premium Fila Champion Puma Reebok 1ra 10 Kg',price:177100,origPrice:856000,weight:'10kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:116,cat:'deportiva',name:'Mixto Marcas Premium Fila Champion Puma Reebok 1ra 20 Kg',price:342100,origPrice:361000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:117,cat:'deportiva',name:'Mixto Marcas Premium Fila Champion Puma Reebok 1ra 25 Kg',price:399300,origPrice:413000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:118,cat:'deportiva',name:'Mixto Marcas Premium Nike Adidas Deportivo 1ra 25 Kg',price:468600,origPrice:466000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:119,cat:'deportiva',name:'Nino Marca 1ra 25kg',price:258500,origPrice:285000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:120,cat:'deportiva',name:'Short Running 1ra 20 Kg (orig)',price:220000,origPrice:250000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:121,cat:'deportiva',name:'Pantalon Raquelado 1ra 45 Kg',price:297000,origPrice:320000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:122,cat:'deportiva',name:'Pantalon Raquelado Marca 12kg',price:262900,origPrice:249000,weight:'12kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:123,cat:'deportiva',name:'Pantalon Raquelado Marca 25kg',price:599500,origPrice:570000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:124,cat:'deportiva',name:'Pantalon Trekking / Senderismo Inv 1ra 40 Kg',price:513700,origPrice:617000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:125,cat:'deportiva',name:'Pantalon Trekking / Senderismo Verano 1ra 40 Kg',price:628100,origPrice:721000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:126,cat:'deportiva',name:'Poleron Con Gorro Solo Marca 1ra 20kg',price:342100,origPrice:361000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:127,cat:'deportiva',name:'Premium Nike Adidas Deportivo 20 Kg',price:456500,origPrice:445000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:128,cat:'deportiva',name:'Ropa Caza Y Pesca 1ra 25 Kg',price:302500,origPrice:290000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:129,cat:'deportiva',name:'Short Columbia 5 Kg',price:143000,origPrice:230000,weight:'5kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:130,cat:'deportiva',name:'Short Marca Surtido 25 Kg',price:203500,origPrice:250000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:131,cat:'deportiva',name:'Short Marca Columbia 10 Kg',price:228800,origPrice:258000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:132,cat:'deportiva',name:'Short Marca Vestir Y Outdoor 15 Kg',price:148500,origPrice:275000,weight:'15kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:133,cat:'deportiva',name:'Short Marca Vestir Y Outdoor 25kg',price:262900,origPrice:309000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:134,cat:'deportiva',name:'Short Marcas Deportivas 1ra 25 Kg',price:495000,origPrice:500000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:135,cat:'deportiva',name:'Short Marcas Premium Unisex 1ra 25 Kg',price:330000,origPrice:360000,weight:'25kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:136,cat:'deportiva',name:'Short Running 1ra 20 Kg (v5)',price:220000,origPrice:250000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:137,cat:'deportiva',name:'Short Running 1ra 20 Kg (v4)',price:220000,origPrice:250000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:138,cat:'deportiva',name:'Short Running 1ra 25 Kg',price:275000,origPrice:260000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:139,cat:'deportiva',name:'Short Surf / Playero Hombre 1ra 25 Kg',price:275000,origPrice:300000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:140,cat:'sweaters',name:'Cardigan 1ra 45 1ra Kg',price:159500,origPrice:180000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:141,cat:'sweaters',name:'Cardigan Largo 1ra 20 Kg',price:148500,origPrice:150000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:142,cat:'sweaters',name:'Poncho Fashion 1ra 45 Kg',price:203500,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:143,cat:'sweaters',name:'Ruana Poncho Fashion 1ra 45 Kg',price:187000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:144,cat:'sweaters',name:'Sweater Grueso 20 Kg',price:71500,origPrice:200000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:145,cat:'sweaters',name:'Sweater Marca Hombre 1ra 25kg',price:308000,origPrice:315000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:146,cat:'sweaters',name:'Sweter Largo 22kg',price:77000,origPrice:220000,weight:'22kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:147,cat:'sweaters',name:'Sweter Marca Mujer Premium 25kg',price:374000,origPrice:360000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:148,cat:'sweaters',name:'Sweter Mujer Moderno 1ra 20 Kg',price:77000,origPrice:75000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:149,cat:'sweaters',name:'Sweter Mujer Moderno 1ra 45 Kg',price:137500,origPrice:150000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:150,cat:'sweaters',name:'Sweter Mujer Oferta 2x20 Kg',price:66000,origPrice:150000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:151,cat:'vestidos',name:'Enteritos 1ra 40 Kg',price:176000,origPrice:250000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:152,cat:'vestidos',name:'Enteritos 1ra 20 Kg',price:93500,origPrice:125000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:153,cat:'vestidos',name:'Mix Brillo / Lentejuelas 25 Kg',price:247500,origPrice:300000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:154,cat:'vestidos',name:'Sweter Largo 45kg',price:137500,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:155,cat:'vestidos',name:'Trench Coat 1ra 25 Kg',price:165000,origPrice:200000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:156,cat:'vestidos',name:'Vestidos Extra Linda 1ra 45 Kg',price:176000,origPrice:250000,weight:'45kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:157,cat:'vestidos',name:'Vestidos Fiesta Prem / Retorno 20 Kg',price:264000,origPrice:280000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:158,cat:'vestidos',name:'Vestidos Verano Juv 1ra+ 20 Kg',price:143000,origPrice:150000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:159,cat:'vestidos',name:'Vestidos Y Faldas 1ra+ Extra Linda 20 Kg',price:148500,origPrice:200000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:160,cat:'vestidos',name:'Vestidos Y Faldas 1ra+ Extra Linda 40 Kg',price:253000,origPrice:380000,weight:'40kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:161,cat:'pantalones',name:'Buzo Algodon 40kg',price:203500,origPrice:260000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:162,cat:'calzado',name:'Calzado Marca Ugg 1ra 10 Kg',price:275000,origPrice:300000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:163,cat:'calzado',name:'Calzado Marca Ugg 1ra 20 Kg',price:539000,origPrice:600000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:164,cat:'calzado',name:'Calzado Marca Ugg Oferta 10kg',price:154000,origPrice:200000,weight:'10kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:165,cat:'calzado',name:'Calzado Mixto 18 Kg',price:55000,origPrice:80000,weight:'18kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:166,cat:'calzado',name:'Calzado Termico/nieve Adulto 1ra 20 Kg',price:216700,origPrice:257000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:167,cat:'calzado',name:'Calzado Termico/nieve Adulto Mixto 20 Kg',price:160600,origPrice:186000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:168,cat:'calzado',name:'Disfraces 45 Kg',price:159500,origPrice:180000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:169,cat:'calzado',name:'Disfraces Y Accesorios 20 Kg',price:71500,origPrice:100000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:170,cat:'calzado',name:'Ropa Mascota 10 Kg',price:88000,origPrice:100000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:171,cat:'calzado',name:'Zapatillas Hombre Marca 1ra 30 U',price:411400,origPrice:380000,weight:'30u',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:172,cat:'calzado',name:'Zapatillas Jordan Y Basketball 1ra 25u',price:524700,origPrice:480000,weight:'25u',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:173,cat:'hogar',name:'Bata Toalla 1ra 45kg',price:176000,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:174,cat:'hogar',name:'Cobertor 1ra-prem 40kg',price:159500,origPrice:200000,weight:'40kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:175,cat:'hogar',name:'Cobertor 45 Kg',price:110000,origPrice:120000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:176,cat:'hogar',name:'Cubrecolchon 1ra 45kg',price:203500,origPrice:200000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:177,cat:'hogar',name:'Frazada 1ra 40kg',price:108900,origPrice:104000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:178,cat:'hogar',name:'Funda Cobertor 18 U Retorno',price:60500,origPrice:75000,weight:'18u',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:179,cat:'hogar',name:'Mix Hogar 1ra 40 Kg Euro',price:110000,origPrice:150000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:180,cat:'hogar',name:'Mix Hogar 2x45kg',price:171600,origPrice:166000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:181,cat:'hogar',name:'Mix Hogar 45 Kg',price:88000,origPrice:85000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:182,cat:'hogar',name:'Sabana Blanca 40 Kg',price:216700,origPrice:247000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:183,cat:'hogar',name:'Sabana Color 40 Kg',price:216700,origPrice:247000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:184,cat:'hogar',name:'Sabanas Franela 1ra 45 Kg',price:192500,origPrice:210000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:185,cat:'hogar',name:'Toalla 1ra 45 Kg',price:262900,origPrice:289000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:186,cat:'hogar',name:'Toalla 25 Kg',price:181500,origPrice:210000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:187,cat:'plussize',name:'Hombre Verano 1ra Plus Size 40 Kg',price:165000,origPrice:210000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:188,cat:'plussize',name:'Hombre Y Mujer Verano 1ra Plus Size 20 Kg',price:88000,origPrice:120000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:189,cat:'plussize',name:'Hombre Y Mujer Verano 1ra Plus Size 40 Kg',price:165000,origPrice:210000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:190,cat:'plussize',name:'Mix Mujer Verano Extra Linda 20 Kg',price:88000,origPrice:100000,weight:'20kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:191,cat:'plussize',name:'Mix Mujer Verano Extra Linda 40 Kg',price:154000,origPrice:270000,weight:'40kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:192,cat:'plussize',name:'Mix Verano Pluz Size Prem 24 Kg',price:220000,origPrice:280000,weight:'24kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:193,cat:'poleras',name:'Abrigo Hombre 3/4 Y Largo 1ra+ 25 Kg',price:137500,origPrice:160000,weight:'25kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:194,cat:'poleras',name:'Camisa Marca Hombre Oferta',price:242000,origPrice:250000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:195,cat:'poleras',name:'Mixto Marca Hombre Oferta',price:203500,origPrice:250000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:196,cat:'poleras',name:'Polera Marca Hombre M/co Adidas Nike 1ra+/prem 20 Kg',price:513700,origPrice:497000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:197,cat:'poleras',name:'Polera Marca Hombre M/co Oferta 25kg',price:214500,origPrice:250000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:198,cat:'poleras',name:'Polera Marca Hombre M/la Oferta',price:203500,origPrice:220000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:199,cat:'vestidos',name:'Abrigo 3/4 Mujer + Blazer / Chaqueta Fashion 2x20 Kg',price:165000,origPrice:180000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:200,cat:'vestidos',name:'Abrigo 3/4 Mujer 1ra 20 Kg',price:99000,origPrice:100000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:201,cat:'vestidos',name:'Blazer / Chaqueta Fashion 20 Kg',price:99000,origPrice:300000,weight:'20kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:202,cat:'vestidos',name:'Brillo / Lentejuela 1ra+/prem 25 Kg',price:253000,origPrice:300000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:203,cat:'vestidos',name:'Calza Y Pantalon Lycra 40 Kg',price:104500,origPrice:140000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:204,cat:'vestidos',name:'Chaqueta Marca Zara Hym 1ra+ 25 Kg',price:401500,origPrice:370000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:205,cat:'vestidos',name:'Corset / Calzon Faja / Modeladores Otros 20kg',price:154000,origPrice:215000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:206,cat:'vestidos',name:'Corset / Calzon Faja / Modeladores Otros 40kg',price:286000,origPrice:400000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:207,cat:'vestidos',name:'Gamulan Piloto 20 Kg',price:132000,origPrice:220000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:208,cat:'vestidos',name:'Jeans Zara 10 U',price:188100,origPrice:406000,weight:'10u',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:209,cat:'vestidos',name:'Michael Kors 1ra 25kg',price:434500,origPrice:500000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:210,cat:'vestidos',name:'Mix Mujer Juv Verano 20 Kg',price:148500,origPrice:180000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:211,cat:'vestidos',name:'Mix Mujer Verano Extra Linda 10 Kg',price:49500,origPrice:55000,weight:'10kg',tier:'premium',badge:'premium',isNew:true,img:MAULLY_IMG},
{id:212,cat:'vestidos',name:'Mixto Marcas Premium Mujer Verano',price:423500,origPrice:420000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:213,cat:'vestidos',name:'Pink 1ra 25 Kg',price:324500,origPrice:350000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:214,cat:'vestidos',name:'Sweter Oferta 20 Kg',price:44000,origPrice:70000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:215,cat:'vestidos',name:'Traje Bano Mujer Entero 1ra+ 20 Kg',price:93500,origPrice:120000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:216,cat:'vestidos',name:'Traje Bano Mujer Entero Surtido 45 Kg',price:93500,origPrice:150000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:217,cat:'vestidos',name:'Trench Coat 1ra 20 Kg',price:132000,origPrice:150000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:218,cat:'vestidos',name:'Zara + Jeans Zara 20 U',price:302500,origPrice:470000,weight:'20u',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:219,cat:'vestidos',name:'Zara Retorno Inv Lig + Heavy 30 U',price:456500,origPrice:465000,weight:'30u',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:220,cat:'ninos',name:'Chaquetas Solo Marcas Deportivas Nino Juv 1ra 20 Kg',price:258500,origPrice:300000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:221,cat:'ninos',name:'Mix Nina Toda Estacion 1ra 10 Kg',price:49500,origPrice:135000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:222,cat:'ninos',name:'Parka Y Chaq Nino 1ra 40kg',price:154000,origPrice:180000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:223,cat:'ninos',name:'Poleron Y Buzo Marca Gap Nino 25 Kg',price:313500,origPrice:320000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:224,cat:'ninos',name:'Termico Ski Ninos 1ra 40 Kg',price:154000,origPrice:200000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:225,cat:'pantalones',name:'Pantalon / Short 3/4 Outdoor 1ra 40 Kg',price:132000,origPrice:180000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:226,cat:'ski',name:'Pantalon Ski Y Termicos Adulto Can 45 Kg',price:214500,origPrice:265000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:227,cat:'ski',name:'Termico Ski Adulto 1ra 45 Kg',price:209000,origPrice:265000,weight:'45kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:228,cat:'deportiva',name:'Abrigo 35 Kg',price:143000,origPrice:150000,weight:'35kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:229,cat:'deportiva',name:'Chaqueta Bomber 1ra+ 25 Kg',price:286000,origPrice:300000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:230,cat:'deportiva',name:'Chaquetas Cuero 25 Kg',price:132000,origPrice:140000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:231,cat:'deportiva',name:'Calvin Klein Mix 22-23 Kg',price:365200,origPrice:362000,weight:'23kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:232,cat:'deportiva',name:'Columbia Verano 20 Kg',price:513700,origPrice:617000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:233,cat:'deportiva',name:'Columbia/ Northface 2da / 3ra 10 Kg',price:104500,origPrice:120000,weight:'10kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:234,cat:'deportiva',name:'Deportivo Verano Solo Marcas 1ra 25 Kg',price:456500,origPrice:435000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:235,cat:'deportiva',name:'Mix Marcas Premium 1ra-prem 20 Kg',price:451000,origPrice:415000,weight:'20kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:236,cat:'deportiva',name:'Mix Marcas Premium 1ra-prem 25 Kg',price:528000,origPrice:550000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:237,cat:'deportiva',name:'Mix Surtido Verano, Todo Producto 20 Kg Calidad Oferta',price:49500,origPrice:75000,weight:'20kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:238,cat:'deportiva',name:'Mix Verano Marca (poleras Y Short) Oferta 50 Kg',price:399300,origPrice:513000,weight:'50kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:239,cat:'deportiva',name:'Mixto Marca Deportivo Old Navy Nba, Nfl, Nhl, Russel,starter, Otras 1ra+ 25 Kg',price:264000,origPrice:300000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:240,cat:'deportiva',name:'Mixto Marca Under Armour Verano 25 Kg',price:440000,origPrice:450000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:241,cat:'deportiva',name:'Parka Chaqueta 1ra 40 Kg',price:159500,origPrice:200000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:242,cat:'deportiva',name:'Polar Marca 1ra 25 Kg',price:388300,origPrice:373000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:243,cat:'deportiva',name:'Polar Marca Oferta 25 Kg',price:220000,origPrice:230000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:244,cat:'deportiva',name:'Poleron Canguro Marca Oferta 25 Kg',price:214500,origPrice:220000,weight:'25kg',tier:'oferta',badge:'oferta',img:MAULLY_IMG},
{id:245,cat:'deportiva',name:'Poleron Con Gorro Marca 1ra+ 25 Kg',price:411400,origPrice:394000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:246,cat:'deportiva',name:'Poleron Deportivo Premium 25kg',price:247500,origPrice:240000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:247,cat:'deportiva',name:'Poleron Marca Gap Adulto 25 Kg',price:399300,origPrice:413000,weight:'25kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:248,cat:'deportiva',name:'Ropa Caza Y Pesca 1ra Prem 25 Kg',price:324500,origPrice:320000,weight:'25kg',tier:'premium',badge:'premium',img:MAULLY_IMG},
{id:249,cat:'deportiva',name:'Ropa Moto 1ra+ 15-18 Kg',price:203500,origPrice:250000,weight:'18kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:250,cat:'deportiva',name:'Ski Alta Montana (parkas Chaq Y Termicos) 1ra+ 20 Kg',price:220000,origPrice:220000,weight:'20kg',tier:'primera',badge:'primera',img:MAULLY_IMG},
{id:251,cat:'deportiva',name:'Sweater Shaggy 40 Kg',price:209000,origPrice:220000,weight:'40kg',tier:'primera',badge:'primera',isNew:true,img:MAULLY_IMG},
{id:252,cat:'hogar',name:'Hospital 40 Kg',price:154000,origPrice:165000,weight:'40kg',tier:'primera',badge:'primera',img:MAULLY_IMG}
];

const badgeLabels={premium:'Premium',primera:'Primera',oferta:'Oferta',extra:'Extra Linda'};
const badgeClasses={premium:'badge-premium',primera:'badge-primera',oferta:'badge-oferta',extra:'badge-extra'};

function getCatInfo(catId){return categories.find(c=>c.id===catId)||{};}
function formatPrice(n){return '$'+n.toLocaleString('es-CL');}
function perKg(price,weight){
  const m=weight.match(/^(\d+)kg$/);
  if(!m)return '';
  return formatPrice(Math.round(price/parseInt(m[1])))+'/kg';
}

// ============ RENDER CATEGORIES ============
function renderCategories(){
  const grid=document.getElementById('catGrid');
  grid.innerHTML=categories.map(c=>`
    <div class="cat-card animate-on-scroll" onclick="filterByCategory('${c.id}')">
      <div class="cat-card-bg" style="background:url('${c.img}') center/cover no-repeat, ${c.gradient}"></div>
      <div class="cat-card-overlay"></div>
      <div class="cat-card-content">
        <div class="cat-card-icon"><i class="fas ${c.icon}"></i></div>
        <h3>${c.name}</h3>
        <p>${c.range}</p>
      </div>
    </div>
  `).join('');
}

// ============ RENDER PRODUCTS ============
let currentFilter='all';
let currentSearch='';
let visibleCount=12;

function getFilteredProducts(){
  let list=products;
  if(currentFilter!=='all')list=list.filter(p=>p.cat===currentFilter);
  if(currentSearch){
    const s=currentSearch.toLowerCase();
    list=list.filter(p=>p.name.toLowerCase().includes(s)||p.cat.toLowerCase().includes(s)||getProductTags(p).some(t=>t.toLowerCase().includes(s)));
  }
  // Price range filter
  list=list.filter(p=>{
    const price=p.price||0;
    return price>=priceMinVal&&(priceMaxVal>=1000000||price<=priceMaxVal);
  });
  return list;
}
function renderFeaturedProducts(){
  const featured=products.filter(p=>p.badge==='premium'||p.isNew).slice(0,2);
  if(!featured.length)return;
  const grid=document.getElementById('productsGrid');
  const featuredHtml='<div class="featured-products" style="grid-column:1/-1">'+featured.map(p=>{
    const cat=getCatInfo(p.cat);
    const tags=getProductTags(p);
    return `<div class="featured-card product-card animate-on-scroll" data-id="${p.id}">
      <div style="padding:12px 16px 0"><span class="featured-badge"><i class="fas fa-crown"></i> Destacado</span></div>
      <div class="product-img" onclick="openProductModal(${p.id})" style="cursor:pointer">
        <div class="product-img-placeholder" style="background:${cat.gradient}">${(()=>{const imgSrc=p.img||getProductImg(p.cat);return imgSrc?'<img src="'+imgSrc+'" alt="'+p.name+'" loading="lazy" style="width:100%;height:100%;object-fit:cover">':'<i class="fas '+cat.icon+'"></i>';})()}</div>
        <div class="product-badges"><span class="badge ${badgeClasses[p.badge]}">${badgeLabels[p.badge]}</span></div>
      </div>
      <div class="product-info">
        <div class="product-cat">${cat.name}</div>
        <div class="product-name">${p.name}</div>
        ${tags.length?'<div class="product-tags">'+tags.map(t=>'<span class="product-tag">'+t+'</span>').join('')+'</div>':''}
        <div class="product-price-row">
          <div class="product-price">${formatPrice(p.price)} <small>CLP</small><span class="product-price-usd">~$${Math.round((p.price||0)/USD_RATE)} USD</span></div>
        </div>
        <div class="product-actions">
          <button class="btn btn-add-cart" onclick="addToCart(${p.id})"><i class="fas fa-plus"></i> Agregar</button>
          <a href="https://wa.me/${WA_NUMBER}?text=${encodeURIComponent('Hola! Me interesa: '+p.name)}" target="_blank" rel="noopener noreferrer" class="btn btn-wa" style="font-size:.82rem"><i class="fab fa-whatsapp"></i> Cotizar</a>
        </div>
      </div>
    </div>`;
  }).join('')+'</div>';
  grid.insertAdjacentHTML('afterbegin',featuredHtml);
}
function getStockStatus(id){
  // Simulated stock based on product id hash for consistency
  const h=(id*2654435761)>>>0;
  const r=h%100;
  if(r<65)return{cls:'stock-available',text:'En Stock'};
  if(r<90)return{cls:'stock-low',text:'Ultimas unidades'};
  return{cls:'stock-available',text:'Disponible por encargo'};
}

function renderProducts(){
  const filtered=getFilteredProducts();
  const toShow=filtered.slice(0,visibleCount);
  const grid=document.getElementById('productsGrid');
  grid.innerHTML=toShow.map(p=>{
    const cat=getCatInfo(p.cat);
    const pkg=perKg(p.price,p.weight);
    return `
    <div class="product-card animate-on-scroll" data-id="${p.id}">
      <div class="product-img" onclick="openProductModal(${p.id})" style="cursor:pointer">
        <div class="product-img-placeholder" style="background:${cat.gradient}">${(()=>{const imgSrc=p.img||getProductImg(p.cat);return imgSrc?'<img src="'+imgSrc+'" alt="'+p.name+'" loading="lazy" style="width:100%;height:100%;object-fit:cover">':'<i class="fas '+cat.icon+'"></i><span>'+cat.name+'</span>';})()}</div>
        <div class="product-badges">
          <span class="badge ${badgeClasses[p.badge]}">${badgeLabels[p.badge]}</span>
          ${p.isNew?'<span class="badge badge-new">Nuevo</span>':''}
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">${cat.name}</div>
        <div class="product-name" onclick="openProductModal(${p.id})" style="cursor:pointer">${p.name}</div>
        ${(()=>{const tags=getProductTags(p);return tags.length?'<div class="product-tags">'+tags.map(t=>'<span class="product-tag">'+t+'</span>').join('')+'</div>':'';})()}
        <div class="product-meta">
          <span><i class="fas fa-weight-hanging"></i> ${p.weight}</span>
          <span><i class="fas fa-star"></i> ${badgeLabels[p.badge]}</span>
        </div>
        <div class="product-price-row">
          ${p.origPrice&&p.origPrice>p.price?`<div class="product-price-old" style="text-decoration:line-through;color:var(--gray-500);font-size:.82rem">${formatPrice(p.origPrice)}</div>`:''}
          <div class="product-price">${formatPrice(p.price)} <small>CLP</small><span class="product-price-usd">~$${Math.round((p.price||0)/USD_RATE)} USD</span></div>
          ${pkg?`<div class="product-per-kg">${pkg}</div>`:''}
        </div>
        <div class="stock-indicator ${getStockStatus(p.id).cls}"><span class="stock-dot"></span> ${getStockStatus(p.id).text}</div>
        <div class="product-shipping-note"><i class="fas fa-truck"></i> Envio no incluido</div>
        <div class="product-calc-mini">
          <small><i class="fas fa-calculator"></i> Si vendes a $5.000/prenda: ~${Math.round(parseInt(p.weight)*5*5000/1000)}k ganancia est.</small>
        </div>
        <div class="product-actions">
          <button class="btn btn-add-cart" onclick="addToCart(${p.id})"><i class="fas fa-plus"></i> Agregar</button>
          <a href="https://wa.me/${WA_NUMBER}?text=${encodeURIComponent('Hola! Me interesa: '+p.name+' - '+formatPrice(p.price)+'. Tienen disponibilidad?')}" target="_blank" rel="noopener noreferrer" class="btn btn-wa" style="font-size:.82rem"><i class="fab fa-whatsapp"></i> Cotizar</a>
        </div>
      </div>
    </div>`;
  }).join('');

  const wrap=document.getElementById('loadMoreWrap');
  wrap.style.display=filtered.length>visibleCount?'block':'none';

  setTimeout(()=>{document.querySelectorAll('.products-grid .animate-on-scroll').forEach(el=>{observer.observe(el)})},50);
}

function renderFilterButtons(){
  const fg=document.getElementById('filterGroup');
  let html='<button class="filter-btn active" data-filter="all" onclick="setFilter(\'all\')">Todos</button>';
  categories.forEach(c=>{html+=`<button class="filter-btn" data-filter="${c.id}" onclick="setFilter('${c.id}')">${c.name}</button>`;});
  fg.innerHTML=html;
}

function setFilter(f){
  currentFilter=f;visibleCount=12;
  document.querySelectorAll('.filter-btn').forEach(b=>{b.classList.toggle('active',b.dataset.filter===f)});
  renderProducts();
  const grid=document.getElementById('productsGrid');
  if(grid)grid.scrollIntoView({behavior:'smooth',block:'start'});
}
function filterByCategory(id){setFilter(id);}

document.getElementById('loadMoreBtn').addEventListener('click',()=>{visibleCount+=12;renderProducts();});
let _searchTimeout;
document.getElementById('searchInput').addEventListener('input',e=>{
  clearTimeout(_searchTimeout);
  _searchTimeout=setTimeout(()=>{
    currentSearch=e.target.value;visibleCount=12;renderProducts();
    if(currentSearch.length>0){
      const grid=document.getElementById('productsGrid');
      if(grid){
        const rect=grid.getBoundingClientRect();
        if(rect.top>window.innerHeight||rect.top<0){
          grid.scrollIntoView({behavior:'smooth',block:'start'});
        }
      }
    }
  },300);
});

// ============ PRICE RANGE FILTER ============
let priceMinVal=0,priceMaxVal=1000000;
const priceMinEl=document.getElementById('priceMin');
const priceMaxEl=document.getElementById('priceMax');
const priceLabel=document.getElementById('priceRangeLabel');
function updatePriceLabel(){
  const minF=priceMinVal>=1000000?'$1.000.000+':formatPrice(priceMinVal);
  const maxF=priceMaxVal>=1000000?'$1.000.000+':formatPrice(priceMaxVal);
  priceLabel.textContent=minF+' - '+maxF;
}
if(priceMinEl&&priceMaxEl){
  priceMinEl.addEventListener('input',e=>{
    priceMinVal=parseInt(e.target.value);
    if(priceMinVal>priceMaxVal-10000){priceMinVal=priceMaxVal-10000;e.target.value=priceMinVal;}
    updatePriceLabel();visibleCount=12;renderProducts();
  });
  priceMaxEl.addEventListener('input',e=>{
    priceMaxVal=parseInt(e.target.value);
    if(priceMaxVal<priceMinVal+10000){priceMaxVal=priceMinVal+10000;e.target.value=priceMaxVal;}
    updatePriceLabel();visibleCount=12;renderProducts();
  });
}

// ============ PRODUCT DETAIL MODAL ============
function openProductModal(id){
  const p=products.find(x=>x.id===id);
  if(!p)return;
  const cat=getCatInfo(p.cat);
  const imgSrc=p.img||getProductImg(p.cat);
  const stock=getStockStatus(p.id);
  const weightNum=parseInt(p.weight)||20;
  const estPieces=Math.round(weightNum*5);
  const costPerPiece=Math.round(p.price/estPieces);
  const existing=document.getElementById('productModal');
  if(existing)existing.remove();
  const modal=document.createElement('div');
  modal.id='productModal';
  modal.className='product-modal-overlay';
  modal.innerHTML=`
    <div class="product-modal">
      <button class="product-modal-close" onclick="closeProductModal()"><i class="fas fa-times"></i></button>
      <div class="product-modal-grid">
        <div class="product-modal-img">
          ${imgSrc?'<img src="'+imgSrc+'" alt="'+p.name+'" loading="lazy" id="modalMainImg">':'<div style="background:'+cat.gradient+';width:100%;height:300px;display:flex;align-items:center;justify-content:center;border-radius:12px"><i class="fas '+cat.icon+'" style="font-size:3rem;color:#fff"></i></div>'}
          <div class="product-modal-gallery" style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap">
            ${imgSrc?'<div class="modal-thumb active" onclick="document.getElementById(\'modalMainImg\').src=\''+imgSrc+'\';document.querySelectorAll(\'.modal-thumb\').forEach(t=>t.classList.remove(\'active\'));this.classList.add(\'active\')" style="width:64px;height:64px;border-radius:8px;overflow:hidden;border:2px solid var(--accent);cursor:pointer;flex-shrink:0"><img src="'+imgSrc+'" style="width:100%;height:100%;object-fit:cover" loading="lazy"></div>':''}
            ${getProductGallery(p.cat,p.name).map((g,i)=>'<div class="modal-thumb" onclick="document.getElementById(\'modalMainImg\').src=\''+g+'\';document.querySelectorAll(\'.modal-thumb\').forEach(t=>t.classList.remove(\'active\'));this.classList.add(\'active\')" style="width:64px;height:64px;border-radius:8px;overflow:hidden;border:2px solid var(--gray-200);cursor:pointer;flex-shrink:0;transition:all .2s"><img src="'+g+'" style="width:100%;height:100%;object-fit:cover" loading="lazy"></div>').join('')}
          </div>
          <a href="#videos" onclick="closeProductModal();setTimeout(()=>document.getElementById('videos')?.scrollIntoView({behavior:'smooth'}),300)" style="display:flex;align-items:center;gap:6px;margin-top:10px;font-size:.82rem;color:var(--accent);font-weight:600;text-decoration:none;cursor:pointer"><i class="fab fa-youtube" style="color:#e74c3c"></i> Ver videos de aperturas de fardos reales</a>
        </div>
        <div class="product-modal-info">
          <div class="product-cat" style="margin-bottom:4px">${cat.name}</div>
          <h3 style="font-size:1.3rem;margin-bottom:12px">${p.name}</h3>
          <div class="product-modal-badges" style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap">
            <span class="badge ${badgeClasses[p.badge]}">${badgeLabels[p.badge]}</span>
            ${p.isNew?'<span class="badge badge-new">Nuevo</span>':''}
            <span class="stock-indicator ${stock.cls}" style="margin:0"><span class="stock-dot"></span> ${stock.text}</span>
          </div>
          <div class="product-price-row" style="margin-bottom:16px">
            ${p.origPrice&&p.origPrice>p.price?'<div class="product-price-old" style="text-decoration:line-through;color:var(--gray-500);font-size:1rem">'+formatPrice(p.origPrice)+'</div>':''}
            <div class="product-price" style="font-size:1.5rem">${formatPrice(p.price)} <small>CLP</small></div>
          </div>
          <div style="background:var(--gray-50);border-radius:8px;padding:16px;margin-bottom:16px">
            <div style="font-weight:600;margin-bottom:8px;font-size:.9rem"><i class="fas fa-info-circle" style="color:var(--accent)"></i> Detalles del Lote</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:.85rem;color:var(--gray-700)">
              <div><i class="fas fa-weight-hanging" style="color:var(--gold);width:18px"></i> Peso: <strong>${p.weight}</strong></div>
              <div><i class="fas fa-star" style="color:var(--gold);width:18px"></i> Calidad: <strong>${badgeLabels[p.badge]}</strong></div>
              <div><i class="fas fa-tshirt" style="color:var(--gold);width:18px"></i> Est. prendas: <strong>~${estPieces} unid.</strong></div>
              <div><i class="fas fa-tag" style="color:var(--gold);width:18px"></i> Costo/prenda: <strong>${formatPrice(costPerPiece)}</strong></div>
            </div>
          </div>
          <div style="background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:8px;padding:12px;margin-bottom:16px;font-size:.82rem;color:#166534;border:1px solid #bbf7d0">
            <i class="fas fa-calculator"></i> <strong>Ganancia estimada:</strong> Si vendes cada prenda a $5.000, tu ganancia seria de ~${formatPrice(estPieces*5000-p.price)} (ROI ${Math.round((estPieces*5000-p.price)/p.price*100)}%)
          </div>
          <div style="font-size:.82rem;color:var(--gray-600);margin-bottom:16px;display:flex;flex-direction:column;gap:4px">
            <div><i class="fas fa-truck" style="color:var(--accent);width:18px"></i> Envio no incluido - Tu eliges el courier</div>
            <div><i class="fas fa-shield-halved" style="color:var(--accent);width:18px"></i> Garantia de calidad segun nivel indicado</div>
            <div><i class="fas fa-box" style="color:var(--accent);width:18px"></i> Prendas variadas en marcas, tallas y modelos</div>
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap">
            <button class="btn btn-primary" onclick="addToCart(${p.id});closeProductModal()" style="flex:1"><i class="fas fa-cart-plus"></i> Agregar al Carrito</button>
            <a href="https://wa.me/${WA_NUMBER}?text=${encodeURIComponent('Hola! Me interesa: '+p.name+' ('+p.weight+') - '+formatPrice(p.price)+'. Tienen disponibilidad?')}" target="_blank" rel="noopener noreferrer" class="btn btn-wa" style="flex:1"><i class="fab fa-whatsapp"></i> Cotizar Directo</a>
          </div>
        </div>
      </div>
    </div>`;
  document.body.appendChild(modal);
  setTimeout(()=>modal.classList.add('open'),20);
  modal.addEventListener('click',e=>{if(e.target===modal)closeProductModal();});
}
function closeProductModal(){
  const m=document.getElementById('productModal');
  if(m){m.classList.remove('open');setTimeout(()=>m.remove(),300);}
}

// ============ CART WITH QUANTITIES ============
let cart=[];
function getCartQty(){return cart.reduce((s,i)=>s+i.qty,0);}
function updateCartUI(){
  document.getElementById('cartBadge').textContent=getCartQty();
  const body=document.getElementById('cartBody');
  if(cart.length===0){
    body.innerHTML='<div class="cart-empty"><i class="fas fa-box-open"></i><p>Tu carrito esta vacio</p><p style="font-size:.82rem;margin-top:8px">Agrega productos para cotizar por WhatsApp</p></div>';
  }else{
    body.innerHTML=cart.map((item,i)=>{
      const cat=getCatInfo(item.cat);
      const subtotal=item.price*item.qty;
      return `<div class="cart-item">
        <div class="cart-item-img" style="background:${cat.gradient}"><i class="fas ${cat.icon}"></i></div>
        <div class="cart-item-info">
          <div class="cart-item-name">${item.name}</div>
          <div class="cart-item-price">${formatPrice(item.price)}</div>
          <div class="cart-qty-controls" style="display:flex;align-items:center;gap:8px;margin-top:6px">
            <button onclick="changeCartQty(${i},-1)" style="width:26px;height:26px;border:1px solid var(--gray-300);border-radius:4px;background:var(--white);cursor:pointer;font-size:.85rem">-</button>
            <span style="font-weight:600;min-width:20px;text-align:center">${item.qty}</span>
            <button onclick="changeCartQty(${i},1)" style="width:26px;height:26px;border:1px solid var(--gray-300);border-radius:4px;background:var(--white);cursor:pointer;font-size:.85rem">+</button>
            ${item.qty>1?'<span style="font-size:.75rem;color:var(--gray-500)">= '+formatPrice(subtotal)+'</span>':''}
          </div>
        </div>
        <button class="cart-item-remove" onclick="removeFromCart(${i})"><i class="fas fa-trash-alt"></i></button>
      </div>`;
    }).join('');
  }
  const total=cart.reduce((s,i)=>s+i.price*i.qty,0);
  const totalWeight=cart.reduce((s,i)=>s+parseInt(i.weight||'20')*i.qty,0);
  document.getElementById('cartTotal').textContent=formatPrice(total);
  // Shipping estimate
  let shippingEl=document.getElementById('cartShippingEst');
  if(!shippingEl){
    const footer=document.querySelector('.cart-footer');
    if(footer){
      const div=document.createElement('div');
      div.id='cartShippingEst';
      div.style.cssText='font-size:.78rem;color:var(--gray-600);padding:8px 0;border-top:1px solid var(--gray-200);margin-top:8px';
      footer.insertBefore(div,footer.firstChild);
      shippingEl=div;
    }
  }
  if(shippingEl){
    if(cart.length===0){
      shippingEl.innerHTML='';
    }else{
      shippingEl.innerHTML='<i class="fas fa-truck" style="color:var(--gray-500)"></i> Envio no incluido. Se cotiza aparte segun destino y peso ('+totalWeight+'kg total)';
    }
  }
}
function showToast(msg){
  const t=document.getElementById('toast');
  const txt=document.getElementById('toastText');
  txt.textContent=msg;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),2500);
}
function _saveCart(){try{localStorage.setItem('maully_cart',JSON.stringify(cart));}catch(e){}}
function addToCart(id){
  const p=products.find(x=>x.id===id);
  if(!p)return;
  const existing=cart.find(c=>c.id===id);
  if(existing){existing.qty++;} else{cart.push({...p,qty:1});}
  updateCartUI();_saveCart();showToast(p.name+' agregado al carrito');openCart();
}
function changeCartQty(i,delta){
  cart[i].qty+=delta;
  if(cart[i].qty<=0)cart.splice(i,1);
  updateCartUI();_saveCart();
}
function removeFromCart(i){cart.splice(i,1);updateCartUI();_saveCart();}
function goToCheckout(){if(cart.length===0)return;_saveCart();window.location.href='/checkout.html';}
function openCart(){document.getElementById('cartOverlay').classList.add('open');document.getElementById('cartDrawer').classList.add('open');}
function closeCart(){document.getElementById('cartOverlay').classList.remove('open');document.getElementById('cartDrawer').classList.remove('open');}
document.getElementById('cartToggle').addEventListener('click',openCart);
document.getElementById('cartClose').addEventListener('click',closeCart);
document.getElementById('cartOverlay').addEventListener('click',closeCart);
document.getElementById('cartWhatsApp').addEventListener('click',()=>{
  if(cart.length===0)return;
  let msg='Hola! Me interesan los siguientes productos:\n\n';
  cart.forEach((p,i)=>{
    msg+=`${i+1}. ${p.name} x${p.qty} - ${formatPrice(p.price*p.qty)}\n`;
  });
  const total=cart.reduce((s,i)=>s+i.price*i.qty,0);
  const totalWeight=cart.reduce((s,i)=>s+parseInt(i.weight||'20')*i.qty,0);
  msg+=`\nTotal estimado: ${formatPrice(total)} (${totalWeight}kg)\n`;
  msg+='\nTienen disponibilidad? Cual es el costo de envio a mi ciudad?';
  window.open('https://wa.me/'+WA_NUMBER+'?text='+encodeURIComponent(msg),'_blank');
});

// ============ FAQ ============
document.querySelectorAll('.faq-question').forEach(q=>{
  q.setAttribute('role','button');
  q.setAttribute('tabindex','0');
  q.setAttribute('aria-expanded','false');
  function toggleFaq(){
    const item=q.parentElement;
    const wasActive=item.classList.contains('active');
    document.querySelectorAll('.faq-item').forEach(i=>{i.classList.remove('active');i.querySelector('.faq-question')?.setAttribute('aria-expanded','false');});
    if(!wasActive){item.classList.add('active');q.setAttribute('aria-expanded','true');}
  }
  q.addEventListener('click',toggleFaq);
  q.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();toggleFaq();}});
});

// ============ TERMS MODAL ============
function openTerms(){document.getElementById('termsModal').classList.add('open');document.body.style.overflow='hidden';}
function closeTerms(){document.getElementById('termsModal').classList.remove('open');document.body.style.overflow='';}
document.getElementById('termsModal').addEventListener('click',e=>{if(e.target===e.currentTarget)closeTerms();});

// ============ MOBILE NAV ============
document.getElementById('mobileToggle').addEventListener('click',()=>{document.getElementById('mobileNav').classList.add('open');});
document.getElementById('mobileClose').addEventListener('click',()=>{document.getElementById('mobileNav').classList.remove('open');});
function closeMobileNav(){document.getElementById('mobileNav').classList.remove('open');}

// ============ SCROLL EFFECTS ============
const navbar=document.getElementById('navbar');
const backToTop=document.getElementById('backToTop');
window.addEventListener('scroll',()=>{
  navbar.classList.toggle('scrolled',window.scrollY>50);
  backToTop.classList.toggle('visible',window.scrollY>400);
});
backToTop.addEventListener('click',()=>{window.scrollTo({top:0,behavior:'smooth'});});

// ============ INTERSECTION OBSERVER ============
const observer=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target);}});
},{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
function observeAll(){document.querySelectorAll('.animate-on-scroll').forEach(el=>observer.observe(el));}

// ============ MOTION LIBRARY INTEGRATION ============
function initMotionAnimations(){
  if(typeof Motion==='undefined'||!Motion.inView||!Motion.animate)return;
  const {animate,inView,stagger,scroll}=Motion;
  // Enhanced scroll reveals with blur-fade
  document.querySelectorAll('.animate-on-scroll').forEach(el=>{
    inView(el,()=>{
      animate(el,{opacity:[0,1],transform:['translateY(28px)','translateY(0)'],filter:['blur(6px)','blur(0px)']},{duration:.6,easing:[.4,0,.2,1]});
      el.classList.add('visible');
    },{margin:'-60px 0px'});
  });
  // Staggered grids
  ['.products-grid','.cat-grid','.tiers-grid','.steps-grid','.classes-grid'].forEach(sel=>{
    const el=document.querySelector(sel);
    if(el)inView(el,()=>{
      const children=el.querySelectorAll('.animate-on-scroll,.product-card,.cat-card,.tier-card,.step-card,.class-card');
      if(children.length)animate(children,{opacity:[0,1],transform:['translateY(20px)','translateY(0)'],filter:['blur(4px)','blur(0px)']},{delay:stagger(.06),duration:.5,easing:[.4,0,.2,1]});
    },{margin:'-40px 0px'});
  });
  // Counter upgrade
  document.querySelectorAll('.hero-stat .num').forEach(el=>{
    const text=el.textContent;const match=text.match(/([\d,]+)/);
    if(!match)return;
    const target=parseInt(match[1].replace(/,/g,''));
    const suffix=text.replace(match[0],'');
    const prefix=text.substring(0,text.indexOf(match[0]));
    el._motionCounter=true;
    animate(0,target,{duration:2,easing:[.4,0,.2,1],onUpdate(v){el.textContent=prefix+Math.round(v).toLocaleString('es-CL')+suffix;}});
  });
}

// ============ COUNTER ANIMATION ============
function animateCounters(){
  document.querySelectorAll('.hero-stat .num').forEach(el=>{
    const text=el.textContent;
    const match=text.match(/([\d,]+)/);
    if(!match)return;
    const target=parseInt(match[1].replace(/,/g,''));
    const suffix=text.replace(match[0],'');
    const prefix=text.substring(0,text.indexOf(match[0]));
    let current=0;
    const step=Math.ceil(target/60);
    const timer=setInterval(()=>{
      current+=step;
      if(current>=target){current=target;clearInterval(timer);}
      el.textContent=prefix+current.toLocaleString('es-CL')+suffix;
    },25);
  });
}

// ============ WA TOOLTIP ============
setTimeout(()=>{
  const tip=document.getElementById('waTooltip');
  if(tip){tip.classList.add('show');setTimeout(()=>tip.classList.remove('show'),4000);}
},3000);

// ============ PROFIT CALCULATOR ============
function calculateProfit() {
  const inv = parseInt(document.getElementById('calcInvestment').value) || 0;
  const weight = parseInt(document.getElementById('calcWeight').value) || 1;
  const piecesPerKg = parseInt(document.getElementById('calcPieces').value) || 1;
  const sellPrice = parseInt(document.getElementById('calcSellPrice').value) || 0;
  const waste = parseInt(document.getElementById('calcWaste').value) || 0;

  const totalPieces = weight * piecesPerKg;
  const sellable = Math.round(totalPieces * (1 - waste / 100));
  const revenue = sellable * sellPrice;
  const costPer = Math.round(inv / totalPieces);
  const profit = revenue - inv;
  const roi = inv > 0 ? Math.round((profit / inv) * 100) : 0;

  document.getElementById('calcTotalPieces').textContent = totalPieces.toLocaleString('es-CL');
  document.getElementById('calcSellable').textContent = sellable.toLocaleString('es-CL');
  document.getElementById('calcRevenue').textContent = formatPrice(revenue);
  document.getElementById('calcCostPer').textContent = formatPrice(costPer);
  document.getElementById('calcProfit').textContent = formatPrice(profit);
  document.getElementById('calcProfit').style.color = profit >= 0 ? 'var(--success)' : 'var(--accent)';
  document.getElementById('calcROI').textContent = roi + '%';
  document.getElementById('calcROI').style.color = roi >= 0 ? 'var(--success)' : 'var(--accent)';
}
// Auto-calculate on input change
document.querySelectorAll('#calcInvestment,#calcWeight,#calcPieces,#calcSellPrice,#calcWaste').forEach(el => {
  el.addEventListener('input', calculateProfit);
});
calculateProfit();

// ============ LANGUAGE SELECTOR ============
document.getElementById('langToggle').addEventListener('click', () => {
  document.getElementById('langDropdown').classList.toggle('open');
});
document.addEventListener('click', e => {
  if (!e.target.closest('.lang-selector')) document.getElementById('langDropdown').classList.remove('open');
});

const translations = {
  es: {},
  en: {
    // Nav
    'Inicio':'Home','Categorias':'Categories','Productos':'Products','Calidad':'Quality',
    'Nosotros':'About Us','Galeria':'Gallery','Videos':'Videos','Contacto':'Contact',
    // History
    history_label:'Our History',history_title:'Over 20 Years in the Textile Industry',
    history_2003_title:'The Beginning',history_2003_text:'Importadora Maully was born in Santiago as a small family business, importing the first bales of American clothing directly from the United States.',
    history_2008_title:'European Expansion',history_2008_text:'We expanded our supplier network to Europe, incorporating merchandise from Italy, Spain and other European countries.',
    history_2015_title:'National Consolidation',history_2015_text:'We consolidated as one of the leading wholesale importers in Chile, shipping to all regions of the country.',
    history_2020_title:'Digital Era',history_2020_text:'We reinvented ourselves with digitalization, launching our online store, YouTube channel and social media. We incorporated Bea, our expert WhatsApp advisor.',
    history_2026_title:'Today and the Future',history_2026_text:'With over 20 years of experience, 2,500+ satisfied customers and presence throughout Chile and South America, we continue to grow.',
    // Calculator
    calc_label:'Profit Calculator',calc_title:'Calculate How Much You Can Earn',
    calc_desc:'Simulate your investment and discover the estimated profit selling imported American and European clothing',
    calc_investment:'Investment in merchandise (CLP)',calc_weight:'Bale weight (kg)',
    calc_pieces:'Estimated pieces per kg',calc_sell_price:'Average selling price per piece (CLP)',
    calc_waste:'Estimated waste (%)',calc_btn:'Calculate Profit',
    calc_total_pieces:'Total pieces',calc_sellable:'Sellable pieces',calc_revenue:'Estimated total revenue',
    calc_cost_per:'Cost per piece',calc_profit:'Estimated net profit',calc_roi:'Return on Investment (ROI)',
    calc_disclaimer:'* Estimated values. Actual results may vary depending on bale quality, location and sales strategy.',
    // Classes
    classes_label:'Classes & Advisory',classes_title:'Learn to Sell Imported Clothing',
    classes_desc:'We teach you everything you need to know to start or grow your imported clothing business',
    class1_title:'Course: Start from Zero',class1_desc:'Learn to select your first bales, classify garments by quality, set prices and find your first customers.',
    class1_f1:'How to choose the right bale',class1_f2:'Quality and size classification',class1_f3:'Pricing strategy for beginners',class1_f4:'Where and how to sell',
    class_popular:'Most Popular',class2_title:'Advisory: Grow Your Business',class2_desc:'For those who already sell and want to scale. Learn inventory management, supplier negotiation, marketing strategies.',
    class2_f1:'Efficient inventory management',class2_f2:'Social media marketing',class2_f3:'Supplier negotiation',class2_f4:'Product diversification',
    class3_title:'Masterclass: Online Sales',class3_desc:'Master online imported clothing sales. Learn to create your online store, photograph garments, manage shipping.',
    class3_f1:'Online store creation',class3_f2:'Product photography',class3_f3:'Logistics and shipping',class3_f4:'Branding and loyalty',
    class_cta:'Ask Bea',
  },
  pt: {
    'Inicio':'Inicio','Categorias':'Categorias','Productos':'Produtos','Calidad':'Qualidade',
    'Nosotros':'Sobre Nos','Galeria':'Galeria','Videos':'Videos','Contacto':'Contato',
    history_label:'Nossa Historia',history_title:'Mais de 20 Anos no Ramo Textil',
    history_2003_title:'O Comeco',history_2003_text:'A Importadora Maully nasceu em Santiago como um pequeno empreendimento familiar, importando os primeiros fardos de roupa americana diretamente dos Estados Unidos.',
    history_2008_title:'Expansao Europeia',history_2008_text:'Ampliamos nossa rede de fornecedores para a Europa, incorporando mercadorias da Italia, Espanha e outros paises europeus.',
    history_2015_title:'Consolidacao Nacional',history_2015_text:'Nos consolidamos como uma das importadoras atacadistas de referencia no Chile, com envios para todas as regioes do pais.',
    history_2020_title:'Era Digital',history_2020_text:'Nos reinventamos com a digitalizacao, lancando nossa loja online, canal no YouTube e redes sociais. Incorporamos a Bea, nossa assessora especialista no WhatsApp.',
    history_2026_title:'Hoje e o Futuro',history_2026_text:'Com mais de 20 años de experiencia, 2.500+ clientes satisfeitos e presenca em todo o Chile e America do Sul, continuamos crescendo.',
    calc_label:'Calculadora de Lucro',calc_title:'Calcule Quanto Voce Pode Ganhar',
    calc_desc:'Simule seu investimento e descubra o lucro estimado vendendo roupas americanas e europeias importadas',
    calc_investment:'Investimento em mercadoria (CLP)',calc_weight:'Peso do fardo (kg)',
    calc_pieces:'Pecas estimadas por kg',calc_sell_price:'Preco medio de venda por peca (CLP)',
    calc_waste:'Perda estimada (%)',calc_btn:'Calcular Lucro',
    calc_total_pieces:'Total de pecas',calc_sellable:'Pecas vendaveis',calc_revenue:'Receita total estimada',
    calc_cost_per:'Custo por peca',calc_profit:'Lucro liquido estimado',calc_roi:'Retorno do Investimento (ROI)',
    calc_disclaimer:'* Valores estimados. Os resultados reais podem variar de acordo com a qualidade do fardo, localizacao e estrategia de venda.',
    classes_label:'Cursos e Assessoria',classes_title:'Aprenda a Vender Roupa Importada',
    classes_desc:'Ensinamos tudo o que voce precisa saber para iniciar ou fazer crescer seu negocio de roupas americanas e europeias',
    class1_title:'Curso: Comecar do Zero',class1_desc:'Aprenda a selecionar seus primeiros fardos, classificar roupas por qualidade, definir precos e encontrar seus primeiros clientes.',
    class1_f1:'Como escolher o fardo certo',class1_f2:'Classificacao por qualidade e tamanho',class1_f3:'Estrategia de precos para iniciantes',class1_f4:'Onde e como vender',
    class_popular:'Mais Popular',class2_title:'Assessoria: Cresca Seu Negocio',class2_desc:'Para quem ja vende e quer escalar. Aprenda gestao de estoque, negociacao com fornecedores, estrategias de marketing.',
    class2_f1:'Gestao eficiente de estoque',class2_f2:'Marketing em redes sociais',class2_f3:'Negociacao com fornecedores',class2_f4:'Diversificacao de produtos',
    class3_title:'Masterclass: Venda Online',class3_desc:'Domine a venda online de roupas importadas. Aprenda a criar sua loja, fotografar pecas, gerenciar envios.',
    class3_f1:'Criacao de loja online',class3_f2:'Fotografia de produto',class3_f3:'Logistica e envios',class3_f4:'Branding e fidelizacao',
    class_cta:'Pergunte a Bea',
  },
  de: {
    'Inicio':'Startseite','Categorias':'Kategorien','Productos':'Produkte','Calidad':'Qualitaet',
    'Nosotros':'Ueber Uns','Galeria':'Galerie','Videos':'Videos','Contacto':'Kontakt',
    history_label:'Unsere Geschichte',history_title:'Ueber 20 Jahre in der Textilbranche',
    history_2003_title:'Die Anfaenge',history_2003_text:'Importadora Maully wurde in Santiago als kleines Familienunternehmen gegruendet und importierte die ersten Ballen amerikanischer Kleidung direkt aus den USA.',
    history_2008_title:'Europaeische Expansion',history_2008_text:'Wir erweiterten unser Lieferantennetzwerk nach Europa mit Ware aus Italien, Spanien und anderen europaeischen Laendern.',
    history_2015_title:'Nationale Konsolidierung',history_2015_text:'Wir haben uns als einer der fuehrenden Grosshandelsimporteure in Chile etabliert, mit Versand in alle Regionen des Landes.',
    history_2020_title:'Digitales Zeitalter',history_2020_text:'Wir haben uns mit der Digitalisierung neu erfunden, unseren Online-Shop, YouTube-Kanal und Social Media gestartet.',
    history_2026_title:'Heute und die Zukunft',history_2026_text:'Mit ueber 20 Jahren Erfahrung, 2.500+ zufriedenen Kunden und Praesenz in ganz Chile und Suedamerika wachsen wir weiter.',
    calc_label:'Gewinnrechner',calc_title:'Berechnen Sie Ihren moeglichen Gewinn',
    calc_desc:'Simulieren Sie Ihre Investition und entdecken Sie den geschaetzten Gewinn beim Verkauf importierter Kleidung',
    calc_investment:'Investition in Ware (CLP)',calc_weight:'Ballengewicht (kg)',
    calc_pieces:'Geschaetzte Stuecke pro kg',calc_sell_price:'Durchschnittlicher Verkaufspreis pro Stueck (CLP)',
    calc_waste:'Geschaetzter Verlust (%)',calc_btn:'Gewinn berechnen',
    calc_total_pieces:'Gesamtstuecke',calc_sellable:'Verkaufbare Stuecke',calc_revenue:'Geschaetzter Gesamtumsatz',
    calc_cost_per:'Kosten pro Stueck',calc_profit:'Geschaetzter Nettogewinn',calc_roi:'Kapitalrendite (ROI)',
    calc_disclaimer:'* Geschaetzte Werte. Die tatsaechlichen Ergebnisse koennen je nach Ballenqualitaet, Standort und Verkaufsstrategie variieren.',
    classes_label:'Kurse und Beratung',classes_title:'Lernen Sie importierte Kleidung zu verkaufen',
    classes_desc:'Wir bringen Ihnen alles bei, was Sie brauchen, um Ihr Geschaeft mit importierter Kleidung zu starten oder auszubauen',
    class1_title:'Kurs: Bei Null anfangen',class1_desc:'Lernen Sie Ihre ersten Ballen auszuwaehlen, Kleidung nach Qualitaet zu klassifizieren, Preise festzulegen und Ihre ersten Kunden zu finden.',
    class1_f1:'Den richtigen Ballen waehlen',class1_f2:'Qualitaets- und Groessenklassifizierung',class1_f3:'Preisstrategie fuer Anfaenger',class1_f4:'Wo und wie verkaufen',
    class_popular:'Am beliebtesten',class2_title:'Beratung: Geschaeft ausbauen',class2_desc:'Fuer diejenigen, die bereits verkaufen und skalieren moechten. Lernen Sie Bestandsmanagement und Marketingstrategien.',
    class2_f1:'Effiziente Bestandsverwaltung',class2_f2:'Social-Media-Marketing',class2_f3:'Lieferantenverhandlung',class2_f4:'Produktdiversifizierung',
    class3_title:'Masterclass: Online-Verkauf',class3_desc:'Meistern Sie den Online-Verkauf importierter Kleidung. Lernen Sie Ihren Online-Shop zu erstellen und Versand zu verwalten.',
    class3_f1:'Online-Shop erstellen',class3_f2:'Produktfotografie',class3_f3:'Logistik und Versand',class3_f4:'Branding und Kundenbindung',
    class_cta:'Bea fragen',
  }
};

let currentLanguage = 'es';

function setLanguage(lang) {
  currentLanguage = lang;
  document.getElementById('currentLang').textContent = lang.toUpperCase();
  document.querySelectorAll('.lang-option').forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  document.getElementById('langDropdown').classList.remove('open');

  if (lang === 'es') {
    // Reset to original Spanish
    document.querySelectorAll('[data-i18n]').forEach(el => {
      if (el.dataset.original) el.textContent = el.dataset.original;
    });
    // Reset nav links
    document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(a => {
      if (a.dataset.original) a.textContent = a.dataset.original;
    });
    return;
  }

  const t = translations[lang] || {};

  // Translate data-i18n elements
  document.querySelectorAll('[data-i18n]').forEach(el => {
    if (!el.dataset.original) el.dataset.original = el.textContent;
    const key = el.getAttribute('data-i18n');
    if (t[key]) el.textContent = t[key];
  });

  // Translate nav links
  document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(a => {
    if (!a.dataset.original) a.dataset.original = a.textContent;
    const text = a.dataset.original.trim();
    if (t[text]) a.textContent = t[text];
  });
}

// ============ VIDEO GALLERY ============
const channelVideos = [
  // Regular Videos (46)
  {id:'LPOKTX3V_0A',title:'Chaqueta Jeans 45 KG',type:'video'},
  {id:'Uj7nJYp8NYg',title:'Mix Mujer Invierno',type:'video'},
  {id:'Uz2of4SmEns',title:'Chaqueta Zipper Liviana',type:'video'},
  {id:'vMeVp1AWAHc',title:'Mix Mujer Invierno',type:'video'},
  {id:'HKeH8y47cIE',title:'Mix Invierno Tallas Grandes',type:'video'},
  {id:'Y5fNlNwWAoQ',title:'Poleron Polar Mixto 38 KG',type:'video'},
  {id:'_pa77QcPvvs',title:'Jeans Hombre Mix',type:'video'},
  {id:'MU-jts-3hoo',title:'Short Hombre 3/4 y Outdoor 40 KG',type:'video'},
  {id:'q4eeJp8yATY',title:'Ropa de Nino Mixta Invierno 40 KG',type:'video'},
  {id:'SOwGgasEUDg',title:'Jeans Hombre Premium 40 KG',type:'video'},
  {id:'jBiDTxrYFDI',title:'Ropa de Trekking Mix Premium 40 KG',type:'video'},
  {id:'VePhdLlD13I',title:'Mix Invierno Mujer Premium 40 KG',type:'video'},
  {id:'p4gIk4_TVHk',title:'Mixto Juvenil Dama Verano Premium',type:'video'},
  {id:'fVAiVxVUQ2M',title:'Ropa Moto Premium 20 KG',type:'video'},
  {id:'UWMH5DbaaJM',title:'Jeans Dama Premium 40 KG',type:'video'},
  {id:'KtmsPcp-gbI',title:'Leggings Mujer 40 KG',type:'video'},
  {id:'-Bjwii0BpWs',title:'Poleras Hombre M/C 40 KG',type:'video'},
  {id:'fONkp7-N_T8',title:'Jeans Hombre 40 KG',type:'video'},
  {id:'9_w8jNMh4fk',title:'Ropa de Nino Mixta Invierno',type:'video'},
  {id:'7uJKk0-5bko',title:'Manteles 40 KG',type:'video'},
  {id:'5aOPzj1V9QY',title:'Seatpant Nino 40 KG',type:'video'},
  {id:'QkcwPX2o9hQ',title:'Ropa de Ciclista Contenedor Italiano',type:'video'},
  {id:'kORyUJndG2E',title:'Ropa Interior Algodon + Nylon Italia',type:'video'},
  {id:'ZLEkMzvujoA',title:'Jeans Mujer Premium Italia',type:'video'},
  {id:'Vwx2K1oxt6A',title:'Chaquetas y Cortavientos Premium',type:'video'},
  {id:'kr_dtaA0tbs',title:'Poleron Con Gorro Adulto - Italia',type:'video'},
  {id:'JPKrkrezqcU',title:'Pescador Tela Mix Hombre y Mujer',type:'video'},
  {id:'z1q8CzxEecQ',title:'Vestido Fashion Juvenil',type:'video'},
  {id:'vw7BlAbwr00',title:'Pescador Mujer',type:'video'},
  {id:'kxnQSg8eC1g',title:'Bikini Mix',type:'video'},
  {id:'lDkSnwjNuVE',title:'Blusa Poliseda 45 KG',type:'video'},
  {id:'I_nsneNbJ7o',title:'Surtido Poleras y Blusas Poly Primera',type:'video'},
  {id:'FINe5vgS7MM',title:'Camisa Extra Plus Size',type:'video'},
  {id:'TIEU-PMsZss',title:'Vestido Fashion Surtido',type:'video'},
  {id:'JAuvXq_SuUQ',title:'Chaqueta Trench Juvenil Vintage',type:'video'},
  {id:'_gVoEJb8lQE',title:'Blusas y Poleras Mix Fashion',type:'video'},
  {id:'vma4r3G6CH0',title:'Vestido Poly Seda 45 KG',type:'video'},
  {id:'UXVJSFazdHo',title:'Vestido Juvenil Estilo Vintage',type:'video'},
  {id:'lj6B9q32hII',title:'Chaqueta Jeans Juvenil 40 KG',type:'video'},
  {id:'QYRFmSfDO7g',title:'Short Sexy Jeans 40 KG',type:'video'},
  {id:'IXP2w750zJI',title:'Mix Adulto Premium 80% Etiqueta',type:'video'},
  {id:'tCwIkwC9CbE',title:'Pescador Jeans Mujer 40 KG',type:'video'},
  {id:'HA0f8tMRTdM',title:'Sostenes Juvenil Primera Premium',type:'video'},
  {id:'HjxD8bQq2Y8',title:'Vestido Jardinera Jeans 40 KG',type:'video'},
  {id:'zW5kJ552JWc',title:'Vestido Juvenil 40 KG',type:'video'},
  {id:'CVPkPHbyGh0',title:'Polera Juvenil Premium Manga Larga',type:'video'},
  // Shorts (26)
  {id:'xuKAqiQIjCk',title:'Parcas y Chaquetas Columbia / TNF',type:'short'},
  {id:'pnl97aKuMVU',title:'Parcas y Chaquetas Columbia / TNF',type:'short'},
  {id:'lIUZVC1BpXY',title:'Parcas y Chaquetas Columbia / TNF',type:'short'},
  {id:'L0UV0ks9uxk',title:'Parcas y Chaquetas Columbia / TNF',type:'short'},
  {id:'z3g0JfMxeBI',title:'Parcas y Chaquetas Mix',type:'short'},
  {id:'eUWoW8tCy6I',title:'Termicos Adulto',type:'short'},
  {id:'F_w3iOu_rXI',title:'Sweater/Chaleco Cardigan',type:'short'},
  {id:'rdJjce3sb5A',title:'Calzado Invierno 35 KG',type:'short'},
  {id:'wzwgtQQ43Mc',title:'Ropa Reciclada Por Kilo',type:'short'},
  {id:'qDQz8VlGo1E',title:'Parcas y Chaquetas Surtidas 45 KG',type:'short'},
  {id:'Yjh-JIZyj48',title:'Chaquetas de Mezclilla 40 KG',type:'short'},
  {id:'45HG9CUZzCA',title:'Vestidos de Mezclilla Dama',type:'short'},
  {id:'o1ghbdTinbM',title:'Sweater Mujer Abiertos Mixtos',type:'short'},
  {id:'_WL9aALgFDU',title:'Vintage Verano Mix Premium',type:'short'},
  {id:'J-DE7ab44Q8',title:'Mix Militar Premium 40 KG',type:'short'},
  {id:'47LnviUG6a0',title:'Sostenes Contenedor Italiano',type:'short'},
  {id:'OO-aRiESSJs',title:'Sweater Mujer Abiertos Mixtos',type:'short'},
  {id:'SnswSpXQaF0',title:'Falda de Mezclilla Europa',type:'short'},
  {id:'efh3itb3Jso',title:'Polera Mujer Manga Corta Italia',type:'short'},
  {id:'Q-SYWZlYo88',title:'Sostenes Proveedor Italiano',type:'short'},
  {id:'nIYuw2LuQ5Q',title:'Poleron Con Gorro Juvenil Mujer',type:'short'},
  {id:'Q9lj3l13sck',title:'Mix Strech Mujer',type:'short'},
  {id:'ds7YTJMaaCY',title:'Chaqueta Fashion Liviana',type:'short'},
  {id:'NPnTzSBlIEU',title:'Surtido Faldas Primera Premium',type:'short'},
  {id:'w_mHlqjkano',title:'Falda Miami Jeans 40 KG',type:'short'},
  {id:'VWwLqH6s3fI',title:'Pescador Juvenil Jeans 40 KG',type:'short'},
];

let visibleVideos = 6;
let videoFilter = 'all';

function renderVideoGallery() {
  const gallery = document.getElementById('videoGallery');
  if (!gallery) return;
  const filtered = videoFilter === 'all' ? channelVideos : channelVideos.filter(v => v.type === videoFilter);
  const toShow = filtered.slice(0, visibleVideos);
  const remaining = filtered.length - visibleVideos;

  gallery.innerHTML = toShow.map(v =>
    '<div class="video-card animate-on-scroll">' +
    '<div class="video-thumb" data-id="' + v.id + '" onclick="playVideo(this)">' +
    '<img src="https://img.youtube.com/vi/' + v.id + '/mqdefault.jpg" alt="' + v.title + '" loading="lazy">' +
    '<div class="video-play-btn"><i class="fas fa-play"></i></div>' +
    (v.type === 'short' ? '<span class="video-badge-short">Short</span>' : '') +
    '</div>' +
    '<div class="video-card-title">' + v.title + '</div>' +
    '</div>'
  ).join('');

  // Load more button
  const loadMoreWrap = document.getElementById('videoLoadMore');
  if (loadMoreWrap) {
    if (remaining > 0) {
      loadMoreWrap.innerHTML = '<button class="btn btn-primary" onclick="visibleVideos+=12;renderVideoGallery()"><i class="fas fa-plus"></i> Ver Mas Videos (' + remaining + ' restantes)</button>';
      loadMoreWrap.style.display = 'block';
    } else {
      loadMoreWrap.style.display = 'none';
    }
  }

  setTimeout(() => {
    document.querySelectorAll('.video-gallery .animate-on-scroll').forEach(el => observer.observe(el));
  }, 50);
}

function playVideo(el) {
  const id = el.dataset.id;
  el.innerHTML = '<iframe src="https://www.youtube.com/embed/' + id + '?autoplay=1" title="Video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
}

function setVideoFilter(f) {
  videoFilter = f;
  visibleVideos = 6;
  document.querySelectorAll('.video-filter-btn').forEach(b => b.classList.toggle('active', b.dataset.filter === f));
  renderVideoGallery();
}

// ============ PHOTO GALLERY ============
const galleryPhotos = [
  {src:'https://img.youtube.com/vi/xuKAqiQIjCk/hqdefault.jpg',title:'Parcas y Chaquetas Columbia / TNF'},
  {src:'https://img.youtube.com/vi/LPOKTX3V_0A/hqdefault.jpg',title:'Chaqueta Jeans 45 KG'},
  {src:'https://img.youtube.com/vi/qDQz8VlGo1E/hqdefault.jpg',title:'Parcas y Chaquetas Surtidas 45 KG'},
  {src:'https://img.youtube.com/vi/Vwx2K1oxt6A/hqdefault.jpg',title:'Chaquetas y Cortavientos Premium'},
  {src:'https://img.youtube.com/vi/VePhdLlD13I/hqdefault.jpg',title:'Mix Invierno Mujer Premium'},
  {src:'https://img.youtube.com/vi/SOwGgasEUDg/hqdefault.jpg',title:'Jeans Hombre Premium 40 KG'},
  {src:'https://img.youtube.com/vi/UWMH5DbaaJM/hqdefault.jpg',title:'Jeans Dama Premium 40 KG'},
  {src:'https://img.youtube.com/vi/jBiDTxrYFDI/hqdefault.jpg',title:'Ropa de Trekking Mix Premium'},
  {src:'https://img.youtube.com/vi/IXP2w750zJI/hqdefault.jpg',title:'Mix Adulto Premium 80% Etiqueta'},
  {src:'https://img.youtube.com/vi/rdJjce3sb5A/hqdefault.jpg',title:'Calzado Invierno 35 KG'},
  {src:'https://img.youtube.com/vi/Y5fNlNwWAoQ/hqdefault.jpg',title:'Poleron Polar Mixto 38 KG'},
  {src:'https://img.youtube.com/vi/Uj7nJYp8NYg/hqdefault.jpg',title:'Mix Mujer Invierno'},
  {src:'https://img.youtube.com/vi/HKeH8y47cIE/hqdefault.jpg',title:'Mix Invierno Tallas Grandes'},
  {src:'https://img.youtube.com/vi/Yjh-JIZyj48/hqdefault.jpg',title:'Chaquetas de Mezclilla 40 KG'},
  {src:'https://img.youtube.com/vi/kr_dtaA0tbs/hqdefault.jpg',title:'Poleron Con Gorro Adulto - Italia'},
  {src:'https://img.youtube.com/vi/ZLEkMzvujoA/hqdefault.jpg',title:'Jeans Mujer Premium Italia'},
  {src:'https://img.youtube.com/vi/z1q8CzxEecQ/hqdefault.jpg',title:'Vestido Fashion Juvenil'},
  {src:'https://img.youtube.com/vi/JAuvXq_SuUQ/hqdefault.jpg',title:'Chaqueta Trench Juvenil Vintage'},
  {src:'https://img.youtube.com/vi/45HG9CUZzCA/hqdefault.jpg',title:'Vestidos de Mezclilla Dama'},
  {src:'https://img.youtube.com/vi/F_w3iOu_rXI/hqdefault.jpg',title:'Sweater/Chaleco Cardigan'},
  {src:'https://img.youtube.com/vi/o1ghbdTinbM/hqdefault.jpg',title:'Sweater Mujer Abiertos Mixtos'},
  {src:'https://img.youtube.com/vi/eUWoW8tCy6I/hqdefault.jpg',title:'Termicos Adulto'},
  {src:'https://img.youtube.com/vi/q4eeJp8yATY/hqdefault.jpg',title:'Ropa de Nino Mixta Invierno'},
  {src:'https://img.youtube.com/vi/fVAiVxVUQ2M/hqdefault.jpg',title:'Ropa Moto Premium 20 KG'},
  {src:'https://img.youtube.com/vi/p4gIk4_TVHk/hqdefault.jpg',title:'Mixto Juvenil Dama Verano Premium'},
  {src:'https://img.youtube.com/vi/J-DE7ab44Q8/hqdefault.jpg',title:'Mix Militar Premium 40 KG'},
  {src:'https://img.youtube.com/vi/lj6B9q32hII/hqdefault.jpg',title:'Chaqueta Jeans Juvenil 40 KG'},
  {src:'https://img.youtube.com/vi/KtmsPcp-gbI/hqdefault.jpg',title:'Leggings Mujer 40 KG'},
];

let visiblePhotos = 8;

function renderPhotoGallery() {
  const gallery = document.getElementById('photoGallery');
  if (!gallery) return;
  const toShow = galleryPhotos.slice(0, visiblePhotos);
  gallery.innerHTML = toShow.map((p, i) =>
    '<div class="photo-gallery-item animate-on-scroll" onclick="openLightbox(' + i + ')">' +
    '<img src="' + p.src + '" alt="' + p.title + '" loading="lazy">' +
    '<div class="photo-gallery-overlay"><span><i class="fas fa-search-plus"></i> ' + p.title + '</span></div>' +
    '</div>'
  ).join('');

  const btn = document.getElementById('loadMorePhotos');
  if (btn) btn.style.display = visiblePhotos >= galleryPhotos.length ? 'none' : 'inline-flex';

  setTimeout(() => {
    document.querySelectorAll('.photo-gallery .animate-on-scroll').forEach(el => observer.observe(el));
  }, 50);
}

document.getElementById('loadMorePhotos').addEventListener('click', () => {
  visiblePhotos += 8;
  renderPhotoGallery();
});

// Lightbox
let lightboxIndex = 0;
function createLightbox() {
  const lb = document.createElement('div');
  lb.className = 'photo-lightbox';
  lb.id = 'photoLightbox';
  lb.innerHTML = '<button class="photo-lightbox-close" onclick="closeLightbox()"><i class="fas fa-times"></i></button>' +
    '<button class="photo-lightbox-nav prev" onclick="navLightbox(-1)"><i class="fas fa-chevron-left"></i></button>' +
    '<img id="lightboxImg" src="" alt="">' +
    '<button class="photo-lightbox-nav next" onclick="navLightbox(1)"><i class="fas fa-chevron-right"></i></button>' +
    '<div class="photo-lightbox-caption" id="lightboxCaption"></div>';
  lb.addEventListener('click', e => { if (e.target === lb) closeLightbox(); });
  document.body.appendChild(lb);
}
createLightbox();

function openLightbox(i) {
  lightboxIndex = i;
  const lb = document.getElementById('photoLightbox');
  document.getElementById('lightboxImg').src = galleryPhotos[i].src;
  document.getElementById('lightboxCaption').textContent = galleryPhotos[i].title;
  lb.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeLightbox() {
  document.getElementById('photoLightbox').classList.remove('open');
  document.body.style.overflow = '';
}
function navLightbox(dir) {
  lightboxIndex = (lightboxIndex + dir + galleryPhotos.length) % galleryPhotos.length;
  document.getElementById('lightboxImg').src = galleryPhotos[lightboxIndex].src;
  document.getElementById('lightboxCaption').textContent = galleryPhotos[lightboxIndex].title;
}
document.addEventListener('keydown', e => {
  const lb = document.getElementById('photoLightbox');
  if (!lb || !lb.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') navLightbox(-1);
  if (e.key === 'ArrowRight') navLightbox(1);
});

// ============ INSTAGRAM GRID ============
function renderInstagramGrid() {
  const grid = document.getElementById('igGrid');
  if (!grid) return;
  const igPhotos = [
    {src:'https://img.youtube.com/vi/xuKAqiQIjCk/mqdefault.jpg',title:'Parcas Columbia/TNF'},
    {src:'https://img.youtube.com/vi/pnl97aKuMVU/mqdefault.jpg',title:'Chaquetas Premium'},
    {src:'https://img.youtube.com/vi/lIUZVC1BpXY/mqdefault.jpg',title:'Parcas Invierno'},
    {src:'https://img.youtube.com/vi/z3g0JfMxeBI/mqdefault.jpg',title:'Chaquetas Mix'},
    {src:'https://img.youtube.com/vi/qDQz8VlGo1E/mqdefault.jpg',title:'Parcas Surtidas'},
    {src:'https://img.youtube.com/vi/Yjh-JIZyj48/mqdefault.jpg',title:'Chaquetas Mezclilla'},
    {src:'https://img.youtube.com/vi/eUWoW8tCy6I/mqdefault.jpg',title:'Termicos Adulto'},
    {src:'https://img.youtube.com/vi/F_w3iOu_rXI/mqdefault.jpg',title:'Sweater Cardigan'},
    {src:'https://img.youtube.com/vi/rdJjce3sb5A/mqdefault.jpg',title:'Calzado Invierno'},
    {src:'https://img.youtube.com/vi/45HG9CUZzCA/mqdefault.jpg',title:'Vestidos Mezclilla'},
    {src:'https://img.youtube.com/vi/o1ghbdTinbM/mqdefault.jpg',title:'Sweater Mujer'},
    {src:'https://img.youtube.com/vi/_WL9aALgFDU/mqdefault.jpg',title:'Vintage Verano'},
  ];
  grid.innerHTML = igPhotos.map(p =>
    '<a href="https://www.instagram.com/fardos_importadoramaully/" target="_blank" rel="noopener noreferrer" class="ig-post">' +
    '<img src="' + p.src + '" alt="' + p.title + '" loading="lazy">' +
    '<div class="ig-post-overlay"><span><i class="fas fa-heart"></i></span><span><i class="fas fa-comment"></i></span></div>' +
    '</a>'
  ).join('');
}

// ============ LIVE EVENT POPUP (March 28, 2026) ============
function showEventPopup() {
  if (sessionStorage.getItem('eventPopupClosed')) return;
  const popup = document.createElement('div');
  popup.id = 'eventPopup';
  popup.innerHTML = `
    <div class="event-popup-overlay" onclick="closeEventPopup()"></div>
    <div class="event-popup-card">
      <button class="event-popup-close" onclick="closeEventPopup()"><i class="fas fa-times"></i></button>
      <div class="event-popup-live"><i class="fas fa-circle"></i> EVENTO EN VIVO</div>
      <div class="event-popup-icon"><i class="fas fa-box-open"></i></div>
      <h3>Apertura de Fardo Premium EN VIVO</h3>
      <p>Este <strong>Lunes 30 de Marzo</strong> abrimos un fardo premium en vivo y en directo. Sin efectos, sin ediciones. 100% real.</p>
      <div class="event-popup-details">
        <div><i class="fas fa-calendar"></i> Lunes 30 de Marzo, 2026</div>
        <div><i class="fas fa-clock"></i> 11:30 AM</div>
        <div><i class="fas fa-map-marker-alt"></i> Berna 767, Pichilemu</div>
      </div>
      <div class="event-popup-btns">
        <a href="https://wa.me/56968442594?text=Hola%20Bea!%20Quiero%20participar%20del%20evento%20en%20vivo%20del%20lunes%2030%20en%20Pichilemu!" target="_blank" rel="noopener noreferrer" class="btn btn-wa"><i class="fab fa-whatsapp"></i> Quiero Participar</a>
        <a href="https://www.youtube.com/@importadoramaully2024" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="border-color:var(--gray-300);color:var(--gray-700)"><i class="fab fa-youtube" style="color:#e74c3c"></i> Ver Canal</a>
      </div>
    </div>`;
  document.body.appendChild(popup);
  setTimeout(() => popup.classList.add('open'), 100);
}
function closeEventPopup() {
  const popup = document.getElementById('eventPopup');
  if (popup) { popup.classList.remove('open'); setTimeout(() => popup.remove(), 300); }
  sessionStorage.setItem('eventPopupClosed', '1');
}
// Event popup shows AFTER tombola is done (not simultaneously)
// Tombola shows first at 4s, event popup shows 20s later if tombola was used
function scheduleEventPopup(){
  if(!sessionStorage.getItem('eventPopupClosed')){
    setTimeout(showEventPopup, 20000);
  }
}
if(sessionStorage.getItem('wheelSpun')){
  // If already spun, show event popup after 5s
  if(!sessionStorage.getItem('eventPopupClosed')){
    setTimeout(showEventPopup, 5000);
  }
}

// ============ SPIN WHEEL / TOMBOLA (fardo.cl style) ============
const wheelPrizes = [
  {text:'Nada Por Hoy',color:'#1a1a2e',textColor:'#fff'},
  {text:'5% Descuento',color:'#e94560',textColor:'#fff'},
  {text:'Intentalo De Nuevo',color:'#2196F3',textColor:'#fff'},
  {text:'10%Off',color:'#d4a853',textColor:'#1a1a2e'},
  {text:'Siga Participando',color:'#16213e',textColor:'#fff'},
  {text:'Invierno 5%Off',color:'#00BCD4',textColor:'#fff'},
  {text:'Para La Proxima!',color:'#9C27B0',textColor:'#fff'},
  {text:'20%Off',color:'#F44336',textColor:'#fff'},
  {text:'Fardo Gratis',color:'#4CAF50',textColor:'#fff'},
  {text:'Otra Oportunidad',color:'#FF9800',textColor:'#1a1a2e'}
];
// Winning indexes: 3 = "10%Off", 2 = "Intentalo De Nuevo"
const WHEEL_WIN_INDEXES = [3, 2];

function showSpinWheel(){
  if(sessionStorage.getItem('wheelSpun'))return;
  if(document.getElementById('spinWheelPopup'))return;
  const popup=document.createElement('div');
  popup.id='spinWheelPopup';
  popup.innerHTML=`
    <style>
      #spinWheelPopup{position:fixed;inset:0;z-index:5000;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.75);backdrop-filter:blur(6px);opacity:0;transition:opacity .5s ease}
      .wheel-container{display:flex;align-items:center;gap:0;max-width:780px;width:95%;position:relative;z-index:1}
      .wheel-left{flex:0 0 auto;position:relative}
      .wheel-right{flex:1;background:#fff;border-radius:0 20px 20px 0;padding:32px 28px;min-height:420px;display:flex;flex-direction:column;justify-content:center;margin-left:-20px;z-index:0}
      .wheel-right h2{font-family:var(--font-heading);font-size:1.6rem;color:var(--primary);margin-bottom:8px;line-height:1.2}
      .wheel-right h2 span{color:var(--accent)}
      .wheel-right p{color:#666;font-size:.9rem;margin-bottom:20px;line-height:1.5}
      .wheel-close{position:absolute;top:-16px;right:-16px;background:var(--accent);border:3px solid #fff;color:#fff;width:40px;height:40px;border-radius:50%;font-size:1.3rem;cursor:pointer;z-index:20;display:flex;align-items:center;justify-content:center;transition:all .2s;box-shadow:0 4px 12px rgba(233,69,96,.4);line-height:1}
      .wheel-close:hover{background:#c73a52;transform:scale(1.15)}
      .wheel-wrapper{position:relative;width:420px;height:420px}
      .wheel-pointer{position:absolute;right:-14px;top:50%;transform:translateY(-50%);z-index:5;font-size:0}
      .wheel-pointer::after{content:'';display:block;width:0;height:0;border-top:18px solid transparent;border-bottom:18px solid transparent;border-right:28px solid #fff;filter:drop-shadow(-3px 0 6px rgba(0,0,0,.4))}
      .wheel-center-btn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:72px;height:72px;background:linear-gradient(135deg,var(--primary),var(--accent));border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 25px rgba(233,69,96,.4);cursor:pointer;z-index:4;border:4px solid #fff;transition:transform .2s}
      .wheel-center-btn:hover{transform:translate(-50%,-50%) scale(1.08)}
      .wheel-center-btn i{color:#fff;font-size:1.4rem;margin-left:4px}
      #wheelResult{display:none;padding:20px;background:linear-gradient(135deg,#e94560,#d4a853);border-radius:14px;color:#fff;text-align:center;margin-top:16px}
      #wheelResult h3{font-size:1.4rem;font-weight:800;margin-bottom:6px}
      #wheelResult p{font-size:.88rem;opacity:.9;margin-bottom:0}
      .wheel-coupon{background:rgba(255,255,255,.2);border-radius:10px;padding:12px 16px;margin-top:12px;font-family:'Courier New',monospace;font-size:1.2rem;font-weight:700;letter-spacing:3px;cursor:pointer;transition:all .2s;border:2px dashed rgba(255,255,255,.4);text-align:center}
      .wheel-coupon:hover{background:rgba(255,255,255,.3)}
      .wheel-email{margin-top:16px;display:flex;gap:8px}
      .wheel-email input{flex:1;padding:10px 14px;border:2px solid var(--gray-200);border-radius:8px;font-size:.88rem;outline:none;transition:border .2s}
      .wheel-email input:focus{border-color:var(--accent)}
      .wheel-email button{padding:10px 20px;background:var(--accent);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer;white-space:nowrap;transition:all .2s}
      .wheel-email button:hover{background:var(--accent-hover)}
      @media(max-width:700px){
        .wheel-container{flex-direction:column;max-width:95vw;gap:0}
        .wheel-left{order:1}
        .wheel-right{order:2;border-radius:0 0 20px 20px;margin-left:0;margin-top:-20px;padding:28px 20px;min-height:auto}
        .wheel-wrapper{width:min(90vw,380px);height:min(90vw,380px)}
        .wheel-wrapper canvas{width:100%!important;height:100%!important}
        .wheel-right h2{font-size:1.3rem}
        .wheel-close{top:-12px;right:-4px}
      }
    </style>
    <div class="wheel-container">
      <button class="wheel-close" onclick="closeSpinWheel()">&times;</button>
      <div class="wheel-left">
        <div class="wheel-wrapper">
          <canvas id="wheelCanvas" width="420" height="420"></canvas>
          <div class="wheel-pointer"></div>
          <div class="wheel-center-btn" onclick="spinWheel()">
            <i class="fas fa-play" id="spinIcon"></i>
          </div>
        </div>
      </div>
      <div class="wheel-right">
        <h2>Que Buena Suerte!<br>Gira y <span>Gana!</span></h2>
        <p>Tienes una oportunidad unica de ganar un descuento especial en tu proximo fardo. Presiona el boton central para girar la ruleta!</p>
        <div class="wheel-email">
          <input type="email" id="wheelEmail" placeholder="Tu email para recibir el premio">
          <button onclick="spinWheel()">GIRAR</button>
        </div>
        <div id="wheelResult">
          <h3 id="wheelPrizeText"></h3>
          <p id="wheelPrizeDesc"></p>
          <div class="wheel-coupon" id="wheelCoupon" style="display:none" onclick="copyWheelCoupon()"></div>
        </div>
      </div>
    </div>`;
  document.body.appendChild(popup);
  setTimeout(()=>popup.style.opacity='1',50);
  drawWheel(0);
}

function drawWheel(rotation){
  const canvas=document.getElementById('wheelCanvas');
  if(!canvas)return;
  const size=canvas.width;
  const ctx=canvas.getContext('2d');
  const cx=size/2,cy=size/2,r=size/2-10;
  ctx.clearRect(0,0,size,size);
  // Outer ring
  ctx.beginPath();ctx.arc(cx,cy,r+6,0,Math.PI*2);ctx.fillStyle='#1a1a2e';ctx.fill();
  ctx.beginPath();ctx.arc(cx,cy,r+3,0,Math.PI*2);ctx.strokeStyle='#d4a853';ctx.lineWidth=2;ctx.stroke();
  ctx.save();
  ctx.translate(cx,cy);
  ctx.rotate(rotation);
  const n=wheelPrizes.length;
  const sliceAngle=2*Math.PI/n;
  wheelPrizes.forEach((p,i)=>{
    // Draw slice
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.arc(0,0,r,i*sliceAngle,(i+1)*sliceAngle);
    ctx.closePath();
    ctx.fillStyle=p.color;
    ctx.fill();
    ctx.strokeStyle='rgba(255,255,255,.3)';
    ctx.lineWidth=1.5;
    ctx.stroke();
    // Draw text
    ctx.save();
    ctx.rotate(i*sliceAngle+sliceAngle/2);
    ctx.fillStyle=p.textColor;
    ctx.font='bold '+Math.round(size/28)+'px Poppins,sans-serif';
    ctx.textAlign='center';
    ctx.textBaseline='middle';
    ctx.shadowColor='rgba(0,0,0,.5)';
    ctx.shadowBlur=4;
    const words=p.text.split(' ');
    const lineH=Math.round(size/26);
    const textR=r*0.65;
    if(words.length<=2){
      words.forEach((w,wi)=>{
        ctx.fillText(w,textR,(wi-(words.length-1)/2)*lineH);
      });
    }else{
      const mid=Math.ceil(words.length/2);
      ctx.fillText(words.slice(0,mid).join(' '),textR,-lineH/2);
      ctx.fillText(words.slice(mid).join(' '),textR,lineH/2);
    }
    ctx.restore();
  });
  // Decorative dots on rim
  for(let i=0;i<n;i++){
    const angle=i*sliceAngle;
    ctx.beginPath();
    ctx.arc(Math.cos(angle)*(r-6),Math.sin(angle)*(r-6),3,0,Math.PI*2);
    ctx.fillStyle='#d4a853';
    ctx.fill();
  }
  ctx.restore();
  // Inner circle shadow
  const grad=ctx.createRadialGradient(cx,cy,0,cx,cy,36);
  grad.addColorStop(0,'rgba(26,26,46,.3)');
  grad.addColorStop(1,'transparent');
  ctx.beginPath();ctx.arc(cx,cy,36,0,Math.PI*2);ctx.fillStyle=grad;ctx.fill();
}

let isSpinning=false;
let wheelAngle=0;
function spinWheel(){
  if(isSpinning)return;
  isSpinning=true;
  const spinBtn=document.getElementById('spinIcon');
  spinBtn.className='fas fa-spinner fa-spin';
  // ALWAYS land on index 3 (10%Off) - ALWAYS wins 10%
  const winIndex=3;
  const n=wheelPrizes.length;
  const sliceAngleDeg=360/n;
  // Canvas draws slices starting at angle 0 (3 o'clock = right).
  // Slice i occupies [i*sliceAngle, (i+1)*sliceAngle] in the UN-rotated wheel.
  // The pointer sits at the RIGHT (0 deg / 3 o'clock).
  // After rotating the wheel by R degrees clockwise, the slice visible at the
  // pointer is the one whose original angle range contains (-R mod 360).
  // To land in the CENTER of slice winIndex we need:
  //   -R mod 360 == winIndex*sliceAngle + sliceAngle/2
  //   R mod 360 == 360 - (winIndex*sliceAngle + sliceAngle/2)
  const targetRemainder=360-(winIndex*sliceAngleDeg+sliceAngleDeg/2);
  // Add random offset within slice (stay away from edges)
  const jitter=(Math.random()-0.5)*sliceAngleDeg*0.5;
  // Multiple full spins for drama
  const fullSpins=360*7;
  const targetAngle=fullSpins+targetRemainder+jitter;
  const startAngle=wheelAngle;
  let startTime=null;
  const duration=6000;
  function animate(ts){
    if(!startTime)startTime=ts;
    const elapsed=ts-startTime;
    const progress=Math.min(elapsed/duration,1);
    // Cubic ease-out for realistic deceleration
    const eased=1-Math.pow(1-progress,3.5);
    wheelAngle=startAngle+eased*targetAngle;
    drawWheel(wheelAngle*Math.PI/180);
    if(progress<1){
      requestAnimationFrame(animate);
    }else{
      isSpinning=false;
      spinBtn.className='fas fa-play';
      spinBtn.style.marginLeft='4px';
      showWheelResult(winIndex);
    }
  }
  requestAnimationFrame(animate);
}

function showWheelResult(idx){
  const result=document.getElementById('wheelResult');
  result.style.display='block';
  // Always show 10% win
  document.getElementById('wheelPrizeText').textContent='Te Ganaste Un 10%Off. Es Tu Dia De Suerte!';
  const code='MAULLY10-'+Math.random().toString(36).substring(2,8).toUpperCase();
  document.getElementById('wheelPrizeDesc').textContent='No Te Olvides De Usar Tu Cupon En El Carrito';
  document.getElementById('wheelCoupon').style.display='block';
  document.getElementById('wheelCoupon').textContent=code;
  sessionStorage.setItem('wheelSpun','1');
  sessionStorage.setItem('wheelCoupon',code);
  // Schedule event popup after wheel is done
  scheduleEventPopup();
}

function copyWheelCoupon(){
  const el=document.getElementById('wheelCoupon');
  const code=el.textContent;
  navigator.clipboard.writeText(code).then(()=>{
    el.textContent='Copiado!';
    setTimeout(()=>el.textContent=code,1500);
  });
}

function closeSpinWheel(){
  const p=document.getElementById('spinWheelPopup');
  if(p){p.style.opacity='0';setTimeout(()=>p.remove(),400);}
}

// Show wheel FIRST at 4s as the primary engagement popup
setTimeout(()=>{
  if(!sessionStorage.getItem('wheelSpun')){
    showSpinWheel();
  }
},4000);
// When wheel popup is closed, schedule event popup
window.closeEventPopup=function(){
  const popup=document.getElementById('eventPopup');
  if(popup){popup.classList.remove('open');setTimeout(()=>popup.remove(),300);}
  sessionStorage.setItem('eventPopupClosed','1');
};

// Purchase notifications removed — replaced with real social proof

// ============ BEA CHATBOT ============
const BEA_WA = 'https://wa.me/56968442594?text=';
const beaChat = document.getElementById('beaChat');
const beaBody = document.getElementById('beaChatBody');
const beaInput = document.getElementById('beaInput');
const beaFab = document.getElementById('beaFab');
let beaOpen = false;
let beaGender = null; // null => must register, 'f', 'm'
let beaUserName = '';
let beaUserContact = '';
let beaTourStep = -1;
let beaAskedBudget = false;
let beaRegistered = false;

// Common female names in Chile/Latam
const femaleNames = ['maria','carolina','andrea','claudia','patricia','francisca','valentina','camila','javiera','catalina','daniela','fernanda','constanza','nicole','paulina','lorena','katherine','karla','alejandra','marcela','gabriela','natalia','veronica','paola','monica','ana','rosa','carmen','laura','sandra','cecilia','silvia','beatriz','teresa','lucia','margarita','elena','sofia','isabella','martina','isidora','josefa','antonia','emilia','florencia','renata','agustina','macarena','barbara','viviana','carla','jimena','ximena','pamela','marisol','roxana','gloria','graciela','pilar','ines','marta','julia','adriana','alicia','diana','milena','rocio','tamara','yesenia','soledad','priscila','fabiola','evelyn','genesis','karen','karina','denisse','jacqueline','maite'];
const maleNames = ['roberto','miguel','carlos','pedro','juan','diego','sebastian','felipe','andres','matias','nicolas','benjamin','vicente','martin','joaquin','tomas','gabriel','daniel','francisco','alejandro','pablo','santiago','cristian','rodrigo','jose','luis','sergio','marcos','rafael','oscar','fernando','raul','hector','alvaro','enrique','alberto','arturo','ricardo','hugo','manuel','eduardo','claudio','gonzalo','patricio','mauricio','jaime','ivan','ignacio','gustavo','mario','esteban','hernan','cesar','camilo','maximiliano','lucas','agustin','emiliano','renato','franco'];

function detectGenderByName(name) {
  const n = name.toLowerCase().trim().split(/\s+/)[0]; // first name only
  if (femaleNames.includes(n)) return 'f';
  if (maleNames.includes(n)) return 'm';
  // Heuristic: names ending in 'a' are usually female in Spanish
  if (n.endsWith('a') && !['joshua','elba'].includes(n)) return 'f';
  if (n.endsWith('o') || n.endsWith('os')) return 'm';
  // Default to female (more common in clothing business)
  return 'f';
}

function _escapeHtml(t){const d=document.createElement('div');d.textContent=t;return d.innerHTML;}
function beaMsg(text, isUser, delay) {
  return new Promise(resolve => {
    setTimeout(() => {
      const div = document.createElement('div');
      div.className = 'bea-msg ' + (isUser ? 'bea-msg-user' : 'bea-msg-bot');
      if(isUser){
        const bubble=document.createElement('div');bubble.className='bea-msg-bubble';bubble.textContent=text;div.appendChild(bubble);
      }else{
        div.innerHTML='<div class="bea-msg-avatar">B</div><div class="bea-msg-bubble">' + text + '</div>';
      }
      beaBody.appendChild(div);
      beaBody.scrollTop = beaBody.scrollHeight;
      resolve();
    }, delay || 0);
  });
}

function beaTyping() {
  const div = document.createElement('div');
  div.className = 'bea-msg bea-msg-bot bea-typing-msg';
  div.innerHTML = '<div class="bea-msg-avatar">B</div><div class="bea-msg-bubble"><div class="bea-typing"><span></span><span></span><span></span></div></div>';
  beaBody.appendChild(div);
  beaBody.scrollTop = beaBody.scrollHeight;
  return div;
}

function beaRemoveTyping(el) { if (el && el.parentNode) el.parentNode.removeChild(el); }

async function beaReply(text) {
  const typing = beaTyping();
  await new Promise(r => setTimeout(r, 600 + Math.random() * 800));
  beaRemoveTyping(typing);
  await beaMsg(text, false);
}

function beaGenderLabel() { return beaGender === 'm' ? 'mi nino' : 'mi nina'; }
function beaNinoName() { return beaGenderLabel() + ' ' + beaUserName.split(' ')[0]; }

function beaProductCard(p) {
  const cat = getCatInfo(p.cat);
  return '<div class="bea-product-card" onclick="scrollToProduct(' + p.id + ')">' +
    '<div class="bea-prod-img" style="background:' + cat.gradient + '">' +
    (p.img ? '<img src="' + p.img + '" alt="' + p.name + '">' : '<i class="fas ' + cat.icon + '"></i>') +
    '</div><div class="bea-prod-info"><strong>' + p.name + '</strong><span>' + formatPrice(p.price) + '</span></div></div>';
}

function scrollToProduct(id) {
  document.getElementById('productos').scrollIntoView({behavior:'smooth'});
  setTimeout(() => {
    const card = document.querySelector('.product-card[data-id="' + id + '"]');
    if (card) { card.scrollIntoView({behavior:'smooth', block:'center'}); card.style.boxShadow='0 0 0 3px var(--gold)'; setTimeout(()=>card.style.boxShadow='',3000); }
  }, 600);
}

function beaSearchProducts(query) {
  const q = query.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const keywords = q.split(/\s+/);
  return products.filter(p => {
    const name = p.name.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
    const catName = getCatInfo(p.cat).name.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
    const tierName = (badgeLabels[p.badge]||'').toLowerCase();
    const combined = name + ' ' + catName + ' ' + tierName + ' ' + p.cat;
    return keywords.some(k => combined.includes(k));
  });
}

function beaDetectGender(text) {
  const t = text.toLowerCase();
  if (/\b(senora|mujer|chica|dama|mama|abuela|tia|ella)\b/.test(t)) return 'f';
  if (/\b(senor|hombre|chico|caballero|papa|abuelo|tio|el)\b/.test(t)) return 'm';
  return null;
}

const tourSections = [
  {id:'inicio',title:'Portada',desc:'Aqui ves nuestro video principal y las estadisticas de Importadora Maully. Mas de 40 años en el rubro textil, ' + beaNinoName() + '!'},
  {id:'categorias',title:'Categorias',desc:'Tenemos 13 categorias de productos: chaquetas, jeans, poleras, polerones, deportiva, vestidos, ninos, ski, calzado, hogar, sweaters, pantalones y plus size.'},
  {id:'productos',title:'Productos',desc:'Aqui puedes ver todo nuestro catalogo con mas de 50 productos. Puedes filtrar por categoria, buscar por nombre y agregar al carrito.'},
  {id:'calidad',title:'Niveles de Calidad',desc:'Manejamos 4 niveles: Oferta, Primera, Premium y Extra Linda. Cada uno pensado para distintos tipos de negocio.'},
  {id:'calculadora',title:'Calculadora de Utilidad',desc:'Esta herramienta te permite calcular cuanto puedes ganar con tu inversion. Pon tus numeros y ve la ganancia estimada!'},
  {id:'clases',title:'Clases y Asesoria',desc:'Ofrecemos cursos para empezar desde cero, asesoria para hacer crecer tu negocio y masterclass de venta online.'},
  {id:'envios',title:'Envios',desc:'Enviamos a todo Chile e internacionalmente a Argentina y otros. El envio NO esta incluido, tu eliges el courier que prefieras.'},
  {id:'videos',title:'Videos de YouTube',desc:'Tenemos mas de 70 videos en nuestro canal mostrando la mercaderia real, sin filtros ni ediciones.'},
  {id:'instagram',title:'Instagram',desc:'Siguenos en @fardos_importadoramaully con mas de 4,400 seguidores. Publicamos mercaderia nueva todos los dias.'},
  {id:'contacto',title:'Contacto',desc:'Puedes contactarnos por WhatsApp al +56 9 6844 2594 o por email a ventas@importadoramaully.cl'},
];

async function beaTour() {
  beaTourStep = 0;
  await beaReply('Perfecto ' + beaNinoName() + '! Te voy a dar un tour por toda nuestra tienda. Vamos paso a paso 😊');
  await beaTourNext();
}

async function beaTourNext() {
  if (beaTourStep >= tourSections.length) {
    await beaReply('Y eso es todo el tour, ' + beaNinoName() + '! Espero que te haya gustado. Si quieres saber mas de algo, preguntame con confianza 💛');
    beaTourStep = -1;
    return;
  }
  const s = tourSections[beaTourStep];
  const el = document.getElementById(s.id);
  if (el) el.scrollIntoView({behavior:'smooth', block:'start'});
  await beaReply('<strong>📍 ' + s.title + '</strong><br>' + s.desc + '<br><br><button class="bea-quick-btn bea-tour-next" onclick="beaContinueTour()"><i class="fas fa-arrow-right"></i> Siguiente</button>');
  beaTourStep++;
}

window.beaContinueTour = async function() {
  document.querySelectorAll('.bea-tour-next').forEach(b => b.disabled = true);
  await beaTourNext();
};

async function beaRecommend() {
  beaAskedBudget = true;
  await beaReply('Con mucho gusto te ayudo, ' + beaNinoName() + '! Para recomendarte lo mejor, dime:<br><br>1. Que tipo de ropa buscas? (chaquetas, jeans, poleras, etc.)<br>2. Cual es tu presupuesto aproximado?<br>3. Que nivel de calidad prefieres? (Oferta, Primera, Premium, Extra Linda)');
}

async function beaHandleMessage(text) {
  const t = text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const g = beaDetectGender(text);
  if (g) beaGender = g;

  // Greetings
  if (/^(hola|hey|buenas|buenos|hi|hello|ola|que tal|saludos)/.test(t)) {
    await beaReply('Hola ' + beaNinoName() + '! Soy Bea, tu asesora personal de Importadora Maully con mas de 40 años de experiencia en el rubro textil 💛<br><br>En que te puedo ayudar? Puedo:<br>• Darte un <strong>tour virtual</strong> por la tienda<br>• <strong>Recomendarte productos</strong> segun tu presupuesto<br>• Responder cualquier duda sobre nuestros fardos y packs');
    return;
  }

  // Tour
  if (/tour|recorr|mostrar|conocer la tienda|ver todo/.test(t)) { await beaTour(); return; }

  // Shipping
  if (/envio|envios|despacho|flete|shipping|transporte|courier|mandan|mandar|llega|llegan|region|regiones|provincia|donde envian|como llega/.test(t)) {
    document.getElementById('envios')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Sobre envios, ' + beaNinoName() + ':<br><br>• El envio <strong>NO esta incluido</strong> en el precio<br>• Enviamos a <strong>todo Chile</strong> (5-15 dias habiles)<br>• Envios internacionales a <strong>Argentina</strong> y otros paises<br>• <strong>Tu eliges</strong> el courier o transporte que prefieras<br>• El costo se cotiza segun destino y peso<br>• Tambien puedes retirar en nuestro local');
    return;
  }

  // Chilean number/budget parser - understands all modismos
  function parseChileanAmount(str) {
    const s = str.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').trim();
    let amount = 0;
    // "100 lucas", "200lucas", "50 lks", "100 lukas", "100lk"
    let m = s.match(/(\d[\d.,]*)\s*(?:lucas?|lukas?|lks?|lukitas?|luquitas?)/);
    if (m) return parseInt(m[1].replace(/[.,]/g,'')) * 1000;
    // "medio palo", "un palo", "2 palos"
    m = s.match(/(?:un|1)\s*palo/); if (m) return 1000000;
    m = s.match(/medio\s*palo/); if (m) return 500000;
    m = s.match(/(\d+)\s*palos?/); if (m) return parseInt(m[1]) * 1000000;
    // "1 millon", "2 millones"
    m = s.match(/(\d[\d.,]*)\s*mill?on(?:es)?/); if (m) return parseInt(m[1].replace(/[.,]/g,'')) * 1000000;
    // "medio millon"
    m = s.match(/medio\s*mill?on/); if (m) return 500000;
    // "cien mil", "doscientos mil", etc - word numbers
    const wordNums = {
      'un':1,'uno':1,'una':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,'ocho':8,'nueve':9,'diez':10,
      'once':11,'doce':12,'trece':13,'catorce':14,'quince':15,'dieciseis':16,'diecisiete':17,'dieciocho':18,'diecinueve':19,
      'veinte':20,'veintiuno':21,'veintidos':22,'veintitres':23,'veinticuatro':24,'veinticinco':25,
      'treinta':30,'cuarenta':40,'cincuenta':50,'sesenta':60,'setenta':70,'ochenta':80,'noventa':90,
      'cien':100,'ciento':100,'doscientos':200,'doscientas':200,'trescientos':300,'trescientas':300,
      'cuatrocientos':400,'cuatrocientas':400,'quinientos':500,'quinientas':500,
      'seiscientos':600,'seiscientas':600,'setecientos':700,'setecientas':700,
      'ochocientos':800,'ochocientas':800,'novecientos':900,'novecientas':900
    };
    // "cien lucas" "doscientas lucas"
    for (const [word, val] of Object.entries(wordNums)) {
      const re = new RegExp(word + '\\s*(?:lucas?|lukas?|lks?|lukitas?)');
      if (re.test(s)) return val * 1000;
    }
    // "cien mil", "doscientos mil"
    for (const [word, val] of Object.entries(wordNums)) {
      const re = new RegExp(word + '\\s+mil');
      if (re.test(s)) return val * 1000;
    }
    // "100 mil", "200 mil", "50 mil"
    m = s.match(/(\d[\d.,]*)\s*mil(?:es)?/); if (m) return parseInt(m[1].replace(/[.,]/g,'')) * 1000;
    // "100k", "200k"
    m = s.match(/(\d[\d.,]*)\s*k\b/); if (m) return parseInt(m[1].replace(/[.,]/g,'')) * 1000;
    // "$100.000", "100.000", "$100000", "100000" (6+ digits = CLP)
    m = s.match(/\$?\s*(\d{1,3}(?:[.,]\d{3})+)/); if (m) return parseInt(m[1].replace(/[.,]/g,''));
    m = s.match(/\$?\s*(\d{5,})/); if (m) return parseInt(m[1]);
    // "como 100" or just a number in context with budget words
    m = s.match(/(\d+)/); if (m) {
      const n = parseInt(m[1]);
      // If small number (1-999) in context of money talk, assume thousands
      if (n >= 10 && n <= 999) return n * 1000;
      if (n >= 1000) return n;
    }
    return 0;
  }

  // Prices / budget - detect any money/budget related intent
  const budgetIntent = /precio|costo|valor|cuanto|barato|economico|presupuesto|plata|lucas?|lukas?|lks?|lukitas?|mil(?:es)?|\bk\b|palo|millon|tengo|dispongo|gasto|gastar|invertir|inversion|comprar por|entre \d/.test(t);
  const parsedAmount = parseChileanAmount(text);

  if (budgetIntent || parsedAmount > 0) {
    if (parsedAmount > 0) {
      const inBudget = products.filter(p => p.price <= parsedAmount).sort((a,b) => b.price - a.price).slice(0,4);
      if (inBudget.length > 0) {
        let html = 'Con un presupuesto de ' + formatPrice(parsedAmount) + ', te recomiendo estos productos, ' + beaNinoName() + ':<br><br>';
        html += inBudget.map(p => beaProductCard(p)).join('');
        await beaReply(html);
      } else {
        await beaReply('Con ' + formatPrice(parsedAmount) + ' no alcanzo a encontrar un producto completo, ' + beaNinoName() + '. Nuestros precios parten desde ' + formatPrice(Math.min(...products.map(p=>p.price))) + '. Quieres que te muestre las opciones mas economicas?');
      }
      return;
    }
    await beaReply(beaNinoName().charAt(0).toUpperCase() + beaNinoName().slice(1) + ', nuestros precios van desde ' + formatPrice(Math.min(...products.map(p=>p.price))) + ' hasta ' + formatPrice(Math.max(...products.map(p=>p.price))) + '. Todos los precios incluyen IVA pero <strong>no incluyen envio</strong>.<br><br>Dime tu presupuesto y te recomiendo lo mejor! Por ejemplo: "tengo 100 lucas" o "200 mil"');
    return;
  }

  // Quality tiers
  if (/calidad|niveles|oferta|primera|premium|extra linda|tier|buena|mala|que tal|como es|wena|weno|fina|piola|bkn|bacana/.test(t)) {
    document.getElementById('calidad')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Manejamos 4 niveles de calidad, ' + beaNinoName() + ':<br><br>⭐ <strong>Oferta</strong> - Buena calidad, precio economico. Ideal para ferias.<br>⭐⭐ <strong>Primera</strong> - Excelente calidad, marcas reconocidas.<br>⭐⭐⭐ <strong>Premium</strong> - Calidad superior, marcas top, estado impecable.<br>⭐⭐⭐⭐ <strong>Extra Linda</strong> - Lo mejor de lo mejor, seleccionadas a mano.');
    return;
  }

  // Calculator
  if (/calcul|ganancia|utilidad|cuanto gano|roi|retorno|inversion|cuanta plata|cuanto saco|cuanto hago|rentab|negocio|conviene|vale la pena/.test(t)) {
    document.getElementById('calculadora')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Te llevo a nuestra calculadora de utilidad, ' + beaNinoName() + '! Ahi puedes simular tu inversion y ver cuanto puedes ganar. En promedio, nuestros clientes obtienen entre 80% y 150% de retorno sobre su inversion. Pruebala!');
    return;
  }

  // Classes
  if (/clase|curso|aprender|ensenar|asesoria|masterclass|capacitacion/.test(t)) {
    document.getElementById('clases')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Tenemos 3 opciones de formacion, ' + beaNinoName() + ':<br><br>🌱 <strong>Empezar desde Cero</strong> - Para quienes recien comienzan<br>🏪 <strong>Haz Crecer tu Negocio</strong> - Para quienes ya venden (la mas popular!)<br>💻 <strong>Masterclass Venta Online</strong> - Para dominar la venta por internet<br><br>Consultame por WhatsApp para mas detalles!');
    return;
  }

  // Merma
  if (/merma|defecto|manchas|roto|dano|devolucion|reclamo|garantia|fallo|falla|malo|mala|rota|cochino|sucio|pasado|trucho/.test(t)) {
    await beaReply(beaNinoName().charAt(0).toUpperCase() + beaNinoName().slice(1) + ', la merma es normal en la venta mayorista. Son prendas con detalles menores (manchas, botones faltantes). Los niveles Premium y Extra Linda tienen merma minima o nula.<br><br>Si la merma supera el 20% del lote, aceptamos devoluciones dentro de 48 horas con fotos por WhatsApp.');
    return;
  }

  // Payment
  if (/pago|pagar|transferencia|mercadopago|tarjeta|cuenta|deposito|webpay|khipu|banco|efectivo|como pago|forma de pago|metodo|debito|credito/.test(t)) {
    await beaReply('Aceptamos estos medios de pago, ' + beaNinoName() + ':<br><br>🏦 <strong>Transferencia bancaria</strong><br>💳 <strong>MercadoPago</strong><br><br>Todos los precios incluyen IVA. Una vez confirmado tu pago, procesamos tu pedido en 1-3 dias habiles.');
    return;
  }

  // Instagram
  if (/instagram|ig|insta|red social|seguir/.test(t)) {
    document.getElementById('instagram')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Siguenos en Instagram ' + beaNinoName() + '! Somos <strong>@fardos_importadoramaully</strong> con mas de 4,400 seguidores. Publicamos mercaderia nueva todos los dias 📸');
    return;
  }

  // YouTube
  if (/youtube|video|canal/.test(t)) {
    document.getElementById('videos')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Tenemos mas de 70 videos en YouTube, ' + beaNinoName() + '! Ahi puedes ver las aperturas de fardos reales, sin ediciones. Todo transparente para que veas exactamente lo que recibes.');
    return;
  }

  // History
  if (/historia|quienes son|sobre ustedes|maully|empresa|fundacion|quien/.test(t)) {
    document.getElementById('historia')?.scrollIntoView({behavior:'smooth'});
    await beaReply('Importadora Maully tiene mas de <strong>40 años en el rubro textil</strong> y mas de 20 años importando directamente desde Canada, Estados Unidos y Europa, ' + beaNinoName() + '. Somos una empresa familiar con tradicion, experiencia y un compromiso real con nuestros clientes.');
    return;
  }

  // Specific product search
  const found = beaSearchProducts(text);
  if (found.length > 0) {
    const show = found.slice(0, 4);
    let html = 'Encontre ' + found.length + ' producto' + (found.length > 1 ? 's' : '') + ' para ti, ' + beaNinoName() + ':<br><br>';
    html += show.map(p => beaProductCard(p)).join('');
    if (found.length > 4) html += '<br><small>Y ' + (found.length - 4) + ' productos mas. Usa el buscador de productos para ver todos!</small>';
    await beaReply(html);
    return;
  }

  // Recommend / suggest
  if (/recomiend|suger|que me|mejor|popular|mas vendido|top|favorit|vendid|hit|exito|bueno bonito|dale|muestram|tirame|dame opciones|que hay|que tienen|lo mas/.test(t)) { await beaRecommend(); return; }

  // WhatsApp fallback
  if (/whatsapp|contacto|hablar|llamar|telefono|humano|persona real|wsp|wts|wapp|wena onda|persona de verdad|alguien real|vendedor|vendedora|quiero hablar/.test(t)) {
    await beaReply(beaNinoName().charAt(0).toUpperCase() + beaNinoName().slice(1) + ', con mucho gusto te conecto con nuestro equipo por WhatsApp!<br><br><a href="' + BEA_WA + encodeURIComponent('Hola Bea! Necesito ayuda personalizada') + '" target="_blank" rel="noopener noreferrer" class="bea-wa-link"><i class="fab fa-whatsapp"></i> Hablar por WhatsApp</a>');
    return;
  }

  // Pedido minimo
  if (/minimo|minima|menor|menos/.test(t)) {
    await beaReply('El pedido minimo es de 1 pack o caluga, ' + beaNinoName() + '. No necesitas comprar grandes cantidades. Tenemos opciones desde 5kg (calugas desde $27.500) hasta fardos de 25kg. Ideal para probar calidad!');
    return;
  }

  // Event
  if (/evento|vivo|live|sabado|28/.test(t)) {
    await beaReply('Este <strong>Lunes 30 de Marzo a las 11:30 AM</strong> tenemos un evento en vivo en <strong>Berna 767, Pichilemu</strong>, ' + beaNinoName() + '! Vamos a abrir un fardo premium en directo, sin efectos ni ediciones. 100% real. Ven a vernos o siguenos en YouTube!');
    return;
  }

  // Fallback - can't help
  await beaReply('Disculpa ' + beaNinoName() + ', no estoy segura de poder ayudarte con eso. Pero no te preocupes! Puedes hablar directamente con nuestro equipo por WhatsApp y te atienden con cariño:<br><br><a href="' + BEA_WA + encodeURIComponent('Hola! Necesito ayuda con: ' + text) + '" target="_blank" rel="noopener noreferrer" class="bea-wa-link"><i class="fab fa-whatsapp"></i> Continuar por WhatsApp</a><br><br>O preguntame sobre: productos, precios, envios, calidad, clases, o pideme un tour virtual!');
}

// Bea Registration
document.getElementById('beaRegisterBtn').addEventListener('click', () => {
  const name = document.getElementById('beaName').value.trim();
  const contact = document.getElementById('beaContact').value.trim();
  if (!name) { document.getElementById('beaName').style.borderColor='var(--accent)'; document.getElementById('beaName').focus(); return; }
  if (!contact) { document.getElementById('beaContact').style.borderColor='var(--accent)'; document.getElementById('beaContact').focus(); return; }
  beaUserName = name;
  beaUserContact = contact;
  beaGender = detectGenderByName(name);
  beaRegistered = true;
  // Save lead to localStorage
  const leads = JSON.parse(localStorage.getItem('beaLeads')||'[]');
  leads.push({name, contact, date: new Date().toISOString()});
  localStorage.setItem('beaLeads', JSON.stringify(leads));
  // Hide register, show chat
  document.getElementById('beaRegister').style.display = 'none';
  document.getElementById('beaChatBody').style.display = 'flex';
  document.getElementById('beaQuickActions').style.display = 'flex';
  document.getElementById('beaChatInput').style.display = 'flex';
  const firstName = name.split(' ')[0];
  beaMsg('Hola ' + beaNinoName() + '! Que alegria conocerte 💛 Soy Bea, tu asesora personal de Importadora Maully con mas de 40 años de experiencia en el rubro textil.<br><br>En que te puedo ayudar hoy?', false, 300);
});
document.getElementById('beaName').addEventListener('keydown', e => { if(e.key==='Enter') document.getElementById('beaContact').focus(); });
document.getElementById('beaContact').addEventListener('keydown', e => { if(e.key==='Enter') document.getElementById('beaRegisterBtn').click(); });

// Bea UI events
beaFab.addEventListener('click', () => {
  beaOpen = !beaOpen;
  beaChat.classList.toggle('open', beaOpen);
  beaFab.classList.toggle('open', beaOpen);
});
document.getElementById('beaChatClose').addEventListener('click', () => {
  beaOpen = false; beaChat.classList.remove('open'); beaFab.classList.remove('open');
});

async function beaSendMsg() {
  const text = beaInput.value.trim();
  if (!text) return;
  beaInput.value = '';
  await beaMsg(text, true);
  await beaHandleMessage(text);
}

beaInput.addEventListener('keydown', e => { if (e.key === 'Enter') beaSendMsg(); });
document.getElementById('beaSend').addEventListener('click', beaSendMsg);

document.querySelectorAll('.bea-quick-btn[data-action]').forEach(btn => {
  btn.addEventListener('click', async () => {
    const action = btn.dataset.action;
    if (action === 'tour') { await beaMsg('Quiero un tour virtual', true); await beaTour(); }
    else if (action === 'products') { await beaMsg('Quiero ver productos', true); document.getElementById('productos')?.scrollIntoView({behavior:'smooth'}); await beaReply('Te llevo al catalogo, ' + beaNinoName() + '! Ahi puedes filtrar por categoria, buscar por nombre y agregar productos al carrito. Tenemos mas de 50 productos disponibles!'); }
    else if (action === 'recommend') { await beaMsg('Recomiendame algo', true); await beaRecommend(); }
    else if (action === 'prices') { await beaMsg('Quiero saber de precios', true); await beaReply(beaNinoName().charAt(0).toUpperCase() + beaNinoName().slice(1) + ', nuestros precios van desde:<br><br>💰 <strong>Calugas (5kg)</strong>: desde $27.500<br>📦 <strong>Packs (10kg)</strong>: desde $60.500<br>📦 <strong>Sacos (15kg)</strong>: desde $82.500<br>📦 <strong>Fardos (25kg)</strong>: desde $143.000<br><br>Todos incluyen IVA. Envio no incluido. Dime tu presupuesto y te recomiendo lo mejor!'); }
  });
});

// Auto-show greeting tooltip
setTimeout(() => {
  if (!beaOpen) { beaFab.classList.add('greeting'); setTimeout(() => beaFab.classList.remove('greeting'), 5000); }
}, 4000);

// ============ FLOATING SEARCH BAR ============
(function(){
  const floatingEl=document.getElementById('floatingSearch');
  const floatingInput=document.getElementById('floatingSearchInput');
  const floatingFilters=document.getElementById('floatingFilters');
  const floatingClose=document.getElementById('floatingSearchClose');
  const mainInput=document.getElementById('searchInput');
  if(!floatingEl||!floatingInput)return;

  // Populate floating filters from categories
  function buildFloatingFilters(){
    let html='<button class="filter-btn active" data-filter="all">Todos</button>';
    categories.forEach(c=>{html+='<button class="filter-btn" data-filter="'+c.id+'">'+c.name+'</button>';});
    floatingFilters.innerHTML=html;
    floatingFilters.querySelectorAll('.filter-btn').forEach(btn=>{
      btn.addEventListener('click',()=>{
        const f=btn.dataset.filter;
        setFilter(f);
        // Sync active states in floating
        floatingFilters.querySelectorAll('.filter-btn').forEach(b=>b.classList.toggle('active',b.dataset.filter===f));
        // Sync original filter buttons
        document.querySelectorAll('#filterGroup .filter-btn').forEach(b=>b.classList.toggle('active',b.dataset.filter===f));
        scrollToProducts();
      });
    });
  }

  function scrollToProducts(){
    const grid=document.getElementById('productsGrid');
    if(grid){
      const offset=floatingEl.offsetHeight+10;
      const top=grid.getBoundingClientRect().top+window.scrollY-offset;
      window.scrollTo({top,behavior:'smooth'});
    }
  }

  // Show/hide floating bar based on scroll
  let productSection=document.getElementById('productos');
  function checkFloatingVisibility(){
    const show=window.scrollY>200;
    if(show){
      floatingEl.classList.add('visible');
      floatingEl.style.top='0';
    }else{
      floatingEl.classList.remove('visible');
      floatingEl.style.top='';
    }
  }
  window.addEventListener('scroll',checkFloatingVisibility,{passive:true});

  // Sync floating input with main search
  floatingInput.addEventListener('input',e=>{
    const val=e.target.value;
    currentSearch=val;
    visibleCount=12;
    // Sync with main input
    if(mainInput)mainInput.value=val;
    renderProducts();
    if(val.length>0)scrollToProducts();
  });

  // Sync main input to floating
  if(mainInput){
    mainInput.addEventListener('input',()=>{
      floatingInput.value=mainInput.value;
    });
  }

  // Close button clears search
  floatingClose.addEventListener('click',()=>{
    floatingInput.value='';
    if(mainInput)mainInput.value='';
    currentSearch='';
    visibleCount=12;
    renderProducts();
  });

  // Sync filter changes from original buttons to floating
  const origObserver=new MutationObserver(()=>{
    const activeFilter=document.querySelector('#filterGroup .filter-btn.active');
    if(activeFilter){
      const f=activeFilter.dataset.filter;
      floatingFilters.querySelectorAll('.filter-btn').forEach(b=>b.classList.toggle('active',b.dataset.filter===f));
    }
  });
  const filterGroup=document.getElementById('filterGroup');
  if(filterGroup)origObserver.observe(filterGroup,{subtree:true,attributes:true,attributeFilter:['class']});

  // Build filters after categories render
  setTimeout(buildFloatingFilters,200);
})();

// ============ DEEP LINK: open product from URL hash ============
function checkProductHash(){
  const h=window.location.hash;
  if(h&&h.startsWith('#producto-')){
    const id=parseInt(h.replace('#producto-',''));
    if(!id)return;
    // Close any popups/overlays
    document.querySelectorAll('[id*="Popup"],[id*="popup"],[class*="popup-overlay"]').forEach(el=>{el.style.display='none';});
    // Show all products so the product exists in DOM
    currentFilter='all';
    currentSearch='';
    visibleCount=999;
    renderProducts();
    // Open product modal
    setTimeout(()=>{
      openProductModal(id);
      history.replaceState(null,'',window.location.pathname);
    },400);
  }
}
window.addEventListener('hashchange',checkProductHash);

// ============ INIT ============
renderCategories();
renderFilterButtons();
renderProducts();
renderPhotoGallery();
renderInstagramGrid();
renderVideoGallery();
renderFeaturedProducts();
setTimeout(observeAll,100);
setTimeout(()=>{
  if(typeof Motion!=='undefined'){initMotionAnimations();}
  else{animateCounters();}
},500);
// Check deep link after init
setTimeout(checkProductHash,800);

// ============ LAZY LOAD HERO VIDEO ============
setTimeout(()=>{
  const bg=document.getElementById('heroBg');
  if(!bg||!bg.dataset.video)return;
  const iframe=document.createElement('iframe');
  iframe.src=bg.dataset.video;
  iframe.frameBorder='0';
  iframe.allow='autoplay; encrypted-media';
  iframe.allowFullscreen=true;
  iframe.loading='lazy';
  bg.innerHTML='';
  bg.appendChild(iframe);
},5000);
