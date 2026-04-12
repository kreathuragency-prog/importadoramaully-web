const fs = require('fs');
const products = JSON.parse(fs.readFileSync('C:/Users/matia/importadoramaully web/fardos_products.json','utf8'));

const catMap = {
  'chaquetas-parkas': 'chaquetas',
  'jeans-denim-mezclilla': 'jeans',
  'poleras-blusas-camisas': 'poleras',
  'polerones-polar': 'polerones',
  'deportivo-outdoor': 'deportiva',
  'vestidos-faldas': 'vestidos',
  'ninos-ninas': 'ninos',
  'ski': 'ski',
  'calzado-acc-disfraces': 'calzado',
  'hogar': 'hogar',
  'sweater-chalecos': 'sweaters',
  'pantalones-buzos': 'pantalones',
  'plus-size-talla-grande': 'plussize',
  'shorts-trajes-de-bano': 'pantalones',
  'adulto-mixto': 'deportiva',
  'mujer': 'vestidos',
  'hombre': 'poleras',
  'hospital-trabajo-otros': 'hogar',
  'ropa-interior': 'hogar'
};

function getTier(name) {
  const n = name.toUpperCase();
  if (n.includes('PREM') || n.includes('EXTRA LIND')) return 'premium';
  if (n.includes('1RA')) return 'primera';
  if (n.includes('OFERTA') || n.includes('RETORNO')) return 'oferta';
  return 'primera';
}

function getWeight(name) {
  const m = name.match(/(\d+)\s*KG/i);
  if (m) return m[1] + 'kg';
  const u = name.match(/(\d+)\s*U\b/i);
  if (u) return u[1] + 'u';
  return '25kg';
}

function parsePrice(p) {
  if (!p) return 0;
  return parseInt(p.replace(/[^0-9]/g, '')) || 0;
}

function titleCase(str) {
  return str.split(' ').map(w => {
    if (['KG','U','1RA','MIX','XL','GAP','CK','HYM','UGG','ZARA','LEVIS','NIKE','ADIDAS','PUMA','FILA','COLUMBIA','NORTHFACE','REEBOK','CHAMPION'].includes(w.toUpperCase())) {
      return w.charAt(0).toUpperCase() + w.slice(1).toLowerCase();
    }
    return w.charAt(0).toUpperCase() + w.slice(1).toLowerCase();
  }).join(' ');
}

const seen = new Set();
const result = [];
let id = 1;

products.forEach(p => {
  const cat = catMap[p.category];
  if (!cat) return;

  const normName = p.name.toUpperCase().replace(/[^A-Z0-9]/g, '');
  if (seen.has(normName)) return;
  seen.add(normName);

  const salePrice = parsePrice(p.salePrice);
  const regPrice = parsePrice(p.regularPrice);
  if (!salePrice || salePrice === 0) return;

  const price = Math.round(salePrice * 1.1);
  const tier = getTier(p.name);
  const weight = getWeight(p.name);
  const isNew = id <= 8 || Math.random() < 0.12;

  const name = titleCase(p.name).replace(/'/g, "\\'");

  result.push(
    `{id:${id},cat:'${cat}',name:'${name}',price:${price},origPrice:${regPrice},weight:'${weight}',tier:'${tier}',badge:'${tier}'${isNew?',isNew:true':''},img:MAULLY_IMG}`
  );
  id++;
});

console.log('Total unique products:', result.length);

const js = `const MAULLY_IMG = '/img/fardo-maully.png';\nconst products = [\n${result.join(',\n')}\n];`;
fs.writeFileSync('C:/Users/matia/importadoramaully web/products_generated.js', js);
console.log('Written to products_generated.js');
