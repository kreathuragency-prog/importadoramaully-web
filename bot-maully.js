/* ============================================================
   Importadora Maully - Bea · Asistente web
   Widget auto-contenido. Solo inyectar este script antes de </body>.
   No depende de jQuery ni librerías externas.
   ============================================================ */
(function () {
  'use strict';

  if (window.__maullyBotLoaded) return;
  window.__maullyBotLoaded = true;

  var WA_NUMBER = '56975155745';
  var WA_BASE = 'https://wa.me/' + WA_NUMBER + '?text=';
  var PHONE_TIENDA = '+56228332667';
  var ADDRESS = 'Santiago, Chile';
  var IG = 'https://www.instagram.com/fardos_importadoramaully';
  var EMAIL = 'ventas@importadoramaully.cl';
  var CUPON = 'MAULLY2026';

  // ====== Base de conocimiento (intent -> respuesta) ======
  var KB = [
    {
      id: 'envio',
      kw: ['envio', 'envío', 'envian', 'despacho', 'mandan', 'llegar', 'demora', 'courier', 'starken', 'region', 'flete', 'logistica', 'logística'],
      title: '¿Cómo funcionan los envíos?',
      answer: 'Despachamos a <b>todo Chile con Starken</b>. El plazo es de <b>5 a 15 días hábiles</b> según ciudad.<br><br>📦 <b>Modalidad:</b> Tú pagas el flete a Starken al retirar; nosotros <b>coordinamos y despachamos desde Chile</b> sin costo adicional.<br><br>💡 También puedes <b>retirar en bodega</b> en Santiago coordinando con Bea.<br><br>🌎 Enviamos también a <b>Argentina</b> — pregúntame por las modalidades.'
    },
    {
      id: 'minimo',
      kw: ['minimo', 'mínimo', 'pedido minimo', 'cuanto comprar', 'empezar', 'primera compra', 'probar'],
      title: '¿Cuál es el pedido mínimo?',
      answer: 'No hay mínimo alto. Puedes empezar con <b>1 pack o caluga</b> para probar calidad antes de un fardo grande:<br>• <b>Caluga</b>: desde 5 kg<br>• <b>Pack</b>: 10-15 kg<br>• <b>Fardo</b>: 25 kg o más<br><br>Ideal para emprendedores que recién parten o quieren testear marcas/categorías.'
    },
    {
      id: 'calidad',
      kw: ['calidad', 'niveles', 'nivel', 'oferta', 'primera', 'premium', 'extra linda', 'bueno', 'malo', 'estado', 'condicion', 'condición'],
      title: '¿Qué niveles de calidad manejan?',
      answer: 'Manejamos 4 niveles, todos con prendas <b>importadas y revisadas</b>:<br>• <b>Oferta</b>: buena calidad, precio económico<br>• <b>Primera</b>: excelente calidad, marcas reconocidas<br>• <b>Premium</b>: calidad superior, marcas top<br>• <b>Extra Linda</b>: lo mejor, seleccionado a mano<br><br>Premium y Extra Linda tienen <b>merma mínima o nula</b>.'
    },
    {
      id: 'merma',
      kw: ['merma', 'defecto', 'malo', 'manchado', 'roto', 'imperfecto', 'fallas', 'falladas'],
      title: '¿Qué es la merma y cuánto traen los fardos?',
      answer: 'La <b>merma</b> son prendas con detalles menores (manchas pequeñas, botón faltante, descosidos). Es <b>normal en venta mayorista por peso</b> y ya está reflejado en el precio.<br><br>• <b>Oferta / Primera</b>: hasta ~15-20% de merma<br>• <b>Premium</b>: merma muy baja<br>• <b>Extra Linda</b>: prácticamente sin merma<br><br>Si la merma supera el 20% del lote, te cambiamos o damos nota de crédito (reclamo en 48 hrs).'
    },
    {
      id: 'pago',
      kw: ['pago', 'pagar', 'tarjeta', 'mercadopago', 'transferencia', 'debito', 'credito', 'cuotas', 'webpay', 'medios'],
      title: '¿Qué medios de pago aceptan?',
      answer: 'Aceptamos:<br>• <b>Transferencia bancaria</b> (te pasamos los datos al confirmar el pedido)<br>• <b>MercadoPago</b> directo en el sitio (Webpay, Visa, Mastercard, hasta 12 cuotas)<br>• <b>Efectivo</b> si retiras en bodega<br>• <b>Desde Argentina</b>: <b>Global66</b> y <b>USD</b> 🇦🇷<br><br>Todos los precios <b>incluyen IVA</b> y se emite boleta o factura electrónica.'
    },
    {
      id: 'devolucion',
      kw: ['devolucion', 'devolución', 'devolver', 'cambio', 'garantia', 'garantía', 'reclamo', 'no me sirve', 'retracto', 'arrepentido', 'arrepiento'],
      title: '¿Aceptan devoluciones o cambios?',
      answer: '<b>Estudiamos cada caso para entregar la mejor solución posible.</b><br><br>⚖️ Por ley, la ropa importada por peso (fardos, packs, calugas) <b>no tiene derecho a cambio ni devolución</b> — <a href="https://www.bcn.cl/leychile/Navegar?idNorma=61438" target="_blank" rel="noopener">Ley 19.496 art. 3 bis letra b</a>: "bienes que por su naturaleza no pueden ser devueltos o son de uso personal".<br><br>Toda devolución queda <b>sujeta a evaluación y decisión final de Importadora Maully</b>. En la práctica evaluamos cuando:<br>• El nivel/categoría no corresponde a lo descrito<br>• La merma supera el 20% del lote<br>• Reclamas dentro de <b>48 hrs</b> con fotos por WhatsApp<br><br>📲 Para evaluar tu caso, escríbele a Bea con fotos al +56 9 7515 5745.'
    },
    {
      id: 'gancho',
      kw: ['gancho', 'ganchos', 'mas gancho', 'más gancho', 'que es gancho', 'qué es gancho', 'rotacion stock', 'rotación stock', 'temporada', 'contenedor', 'mezcla fardos'],
      title: '¿Qué es un "gancho"?',
      answer: 'Un <b>gancho</b> es un fardo de menor exclusividad que se compra <b>junto a</b> un fardo top muy demandado.<br><br>📦 <b>Ejemplo:</b> si te llevas un <i>JORDAN 25 kg</i> (top exclusivo), debes sumar 2 ganchos.<br><br>🪝 <b>¿Qué fardos sirven como gancho?</b><br>Cualquier fardo con la palabra <b>SEGUNDA</b> en el título: <b>SEGUNDA</b>, <b>SEGUNDA MARCA</b>, <b>SEGUNDA PREMIUM</b>. También fardos sin "marca" ni "premium" en el título.<br><br>⏰ <b>Importante:</b> los ganchos <b>cambian por temporada</b> — la lista se actualiza según rotación de stock.<br><br>📦 <b>¿Por qué existen?</b><br>Para importar un contenedor desde Canadá/EEUU/Europa, los proveedores nunca aceptan UN solo tipo de fardo: hay que mezclar. Replicamos esa lógica al venderte fardos top + ganchos. Más detalle: <a href="#" onclick="event.preventDefault();document.getElementById(\'ganchoBusinessModal\')?.classList.add(\'open\')"><b>Ver explicación completa</b></a>.<br><br>👉 <a href="#" onclick="event.preventDefault();filterByCategory(\'ganchos\');document.getElementById(\'productos\')?.scrollIntoView({behavior:\'smooth\'})"><b>Ver lista de fardos gancho disponibles</b></a>'
    },
    {
      id: 'marcas',
      kw: ['marca', 'marcas', 'columbia', 'north face', 'nike', 'zara', 'adidas', 'levis', 'tommy', 'que ropa', 'que prendas', 'qué prendas'],
      title: '¿Qué marcas vienen en los fardos?',
      answer: 'Trabajamos con stock importado <b>directo desde Canadá, EEUU y Europa</b>. Marcas frecuentes:<br><br>🏔️ <b>Outdoor</b>: Columbia, The North Face, Patagonia, Helly Hansen<br>👟 <b>Deportivas</b>: Nike, Adidas, Puma, Under Armour<br>👕 <b>Casual</b>: Zara, H&M, Levi\'s, Tommy Hilfiger, GAP, Uniqlo<br><br>Las marcas <b>no se garantizan unidad por unidad</b> en un fardo (es venta por peso), salvo packs Premium / Extra Linda con selección específica.'
    },
    {
      id: 'cupon',
      kw: ['cupon', 'cupón', 'descuento', 'oferta', 'promo', 'codigo', 'código', 'maully2026'],
      title: '¿Hay descuentos o cupones activos?',
      answer: 'Sí 🔥. <b>Cupón ' + CUPON + '</b>: <b>10% de descuento</b> al retirar en bodega.<br><br>Puedes descargarlo en PDF directo desde el banner superior del sitio o pedírselo a Bea por WhatsApp. Válido por temporada.'
    },
    {
      id: 'catalogo',
      kw: ['catalogo', 'catálogo', 'lista', 'precios', 'pdf', 'productos', 'ver todo', 'descargar'],
      title: '¿Tienen catálogo o lista de precios?',
      answer: 'Sí, descárgalo aquí 👇<br><br>📕 <a href="https://importadoramaully.cl/catalogo-maully-mayo-2026.pdf" target="_blank" rel="noopener"><b>Catálogo Maully Mayo 2026 (PDF)</b></a><br>14 páginas — 251 productos + sección Argentina.<br><br>También tenemos:<br>• <b>Tienda online</b> con stock real<br>• <b>Calculadora de retorno</b> para estimar tu ganancia<br><br>Si buscas algo específico (categoría, peso, presupuesto), Bea te arma una <b>cotización personalizada</b> por WhatsApp.'
    },
    {
      id: 'tienda',
      kw: ['tienda', 'bodega', 'direccion', 'dirección', 'ubicacion', 'ubicación', 'donde estan', 'dónde están', 'visitar', 'ver fardos', 'local', 'showroom'],
      title: '¿Puedo ir a ver los fardos a la bodega?',
      answer: 'Sí, atendemos en bodega en <b>' + ADDRESS + '</b> con <b>cita previa</b> (para tenerte los fardos preparados).<br><br>Coordina día y hora con Bea por WhatsApp y te recibimos. Puedes <b>revisar prendas, abrir packs</b> y aprovechar el cupón de retiro.'
    },
    {
      id: 'horario',
      kw: ['horario', 'hora', 'abren', 'abre', 'cerrado', 'cerrada', 'hoy', 'domingo', 'sabado', 'sábado', 'abierto'],
      title: '¿Cuál es el horario de atención?',
      answer: '<b>Lunes a Viernes:</b> 11:00 - 19:00 hrs<br><b>Sábado / Domingo:</b> Solo WhatsApp con Bea<br><br>Bea responde por WhatsApp <b>todos los días</b> y coordina pedidos fuera de horario.'
    },
    {
      id: 'factura',
      kw: ['factura', 'boleta', 'empresa', 'rut empresa', 'iva', 'sii'],
      title: '¿Emiten boleta o factura?',
      answer: 'Sí, emitimos <b>boleta o factura electrónica SII</b>. Al hacer la compra elige "Factura" e ingresa <b>RUT, razón social y giro</b>. Todos los precios incluyen IVA.'
    },
    {
      id: 'retorno',
      kw: ['retorno', 'ganancia', 'cuanto gano', 'cuánto gano', 'rentabilidad', 'utilidad', 'margen', 'revender'],
      title: '¿Cuánto puedo ganar revendiendo?',
      answer: 'El retorno típico de nuestros revendedores es de <b>2x a 3x la inversión</b>, dependiendo del nivel de calidad, plaza y estrategia.<br><br>📊 En la sección <b>Calculadora de Retorno</b> del sitio puedes simular tu ganancia ingresando peso del fardo, precio promedio y % de venta.<br><br>Si quieres asesoría, también dictamos <b>cursos para emprendedores</b> que recién parten.'
    },
    {
      id: 'curso',
      kw: ['curso', 'asesoria', 'asesoría', 'masterclass', 'aprender', 'enseñan', 'capacitacion', 'capacitación', 'mentoria', 'mentoría'],
      title: '¿Tienen cursos o asesorías?',
      answer: 'Sí, tenemos 3 instancias:<br>• <b>Curso para empezar desde cero</b> — selección, clasificación, precios, primeros clientes<br>• <b>Asesoría 1 a 1</b> — para hacer crecer un negocio existente<br>• <b>Masterclass de venta online</b> — Marketplace, Instagram, redes<br><br>Bea te cuenta los detalles, fechas y precios por WhatsApp.'
    },
    {
      id: 'argentina',
      kw: ['argentina', 'mendoza', 'buenos aires', 'cordoba', 'argentino', 'argentina', 'rosario', 'tucuman', 'tucumán', 'salta', 'cruzar frontera', 'global66', 'global 66', 'precio argentina', 'envio argentina', 'envío argentina', 'puesto en argentina', 'puestos en argentina', 'al exterior', 'exportar', 'usd', 'dolares', 'dólares', 'dolar', 'dólar'],
      title: '¿Envían a Argentina? ¿Cuánto cuesta?',
      answer: '🇦🇷 Sí, enviamos a <b>Argentina</b> hace años — Mendoza, Córdoba, Buenos Aires y más.<br><br>📕 <b>Aquí tienes los 2 catálogos PDF</b>:<br>• <a href="https://importadoramaully.cl/catalogo-maully-argentina-mayo-2026.pdf" target="_blank" rel="noopener"><b>Catálogo EXCLUSIVO Argentina</b></a> — solo precios puestos en Argentina<br>• <a href="https://importadoramaully.cl/catalogo-maully-mayo-2026.pdf" target="_blank" rel="noopener"><b>Catálogo completo</b></a> — todos los productos + sección Argentina<br><br>📦 <b>Dos modalidades de envío</b>:<br>• <b>Hasta 10 kg</b>: con <b>Starken</b>, tarifa del courier (cobra Starken al retirar).<br>• <b>Sobre 10 kg</b> (fardos): con <b>transportistas privados</b> que <b>cobran por fardo</b> según volumen y destino.<br><br>💳 <b>Pago</b>: <b>100% adelantado</b> vía <b>Global66</b> o <b>USD</b>.<br><br>Para cotizaciones específicas, <b>hablanos por WhatsApp</b> 💛'
    },
    {
      id: 'pago_arg',
      kw: ['global66', 'global 66', 'pago argentina', 'usd', 'dolar', 'dólar', 'dolares', 'dólares'],
      title: '¿Cómo pago desde Argentina?',
      answer: 'Desde Argentina aceptamos:<br>• <b>Global66</b> (transferencia internacional rápida)<br>• <b>USD</b> en efectivo o transferencia<br><br>Bea te coordina los datos y el tipo de cambio del día por WhatsApp 💛'
    },
    {
      id: 'contacto',
      kw: ['contacto', 'whatsapp', 'telefono', 'teléfono', 'llamar', 'email', 'mail', 'correo', 'instagram'],
      title: '¿Cómo los contacto?',
      answer: '<b>WhatsApp Bea:</b> <a href="' + WA_BASE + encodeURIComponent('Hola Bea! Tengo una consulta') + '" target="_blank" rel="noopener">+56 9 7515 5745</a> (todos los días)<br><b>Teléfono fijo:</b> <a href="tel:' + PHONE_TIENDA + '">22 8332 667</a> (Lun-Vie 11-19h)<br><b>Email:</b> <a href="mailto:' + EMAIL + '">' + EMAIL + '</a><br><b>Instagram:</b> <a href="' + IG + '" target="_blank" rel="noopener">@fardos_importadoramaully</a>'
    }
  ];

  var QUICK = ['envio', 'gancho', 'calidad', 'pago', 'cupon', 'argentina'];

  // ====== Intent matching ======
  function normalize(s) {
    return (s || '')
      .toLowerCase()
      .normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9\s]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function findIntent(text) {
    var t = normalize(text);
    if (!t) return null;
    var best = null, bestScore = 0;
    for (var i = 0; i < KB.length; i++) {
      var kb = KB[i];
      var score = 0;
      for (var j = 0; j < kb.kw.length; j++) {
        var kw = normalize(kb.kw[j]);
        if (t.indexOf(kw) !== -1) score += (kw.length > 4 ? 2 : 1);
      }
      if (score > bestScore) { bestScore = score; best = kb; }
    }
    return bestScore >= 1 ? best : null;
  }

  // ====== Estilos (paleta Maully: navy + rojo + dorado) ======
  var css =
  '.mly-bot-fab{position:fixed;bottom:20px;right:20px;z-index:9999;background:linear-gradient(135deg,#0f0f23,#1a1a3e 60%,#e94560);color:#fff;width:64px;height:64px;border-radius:50%;border:none;box-shadow:0 8px 28px rgba(15,15,35,.45);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:transform .18s ease, box-shadow .18s ease;font-family:"Manrope",system-ui,-apple-system,sans-serif}'+
  '.mly-bot-tooltip{position:fixed;bottom:92px;right:24px;z-index:9998;background:#fff;color:#0f0f23;padding:10px 16px;border-radius:14px;box-shadow:0 6px 18px rgba(0,0,0,.15);font-size:13px;font-weight:500;max-width:230px;animation:mlyTipIn .5s ease 2s both;pointer-events:none}'+
  '.mly-bot-tooltip::after{content:"";position:absolute;bottom:-6px;right:30px;width:12px;height:12px;background:#fff;transform:rotate(45deg)}'+
  '.mly-bot-tooltip b{color:#e94560}'+
  '@keyframes mlyTipIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}'+
  '.mly-bot-fab.mly-bot-active~.mly-bot-tooltip{display:none}'+
  '@media(max-width:480px){.mly-bot-tooltip{display:none}}'+
  '.mly-bot-fab:hover{transform:translateY(-2px) scale(1.05);box-shadow:0 12px 34px rgba(233,69,96,.45)}'+
  '.mly-bot-fab svg{width:30px;height:30px}'+
  '.mly-bot-fab .mly-bot-ping{position:absolute;top:4px;right:6px;width:12px;height:12px;border-radius:50%;background:#d4a853;border:2px solid #fff;animation:mly-ping 1.8s infinite}'+
  '@keyframes mly-ping{0%{transform:scale(.9);opacity:.9}70%{transform:scale(1.6);opacity:0}100%{opacity:0}}'+
  '.mly-bot-panel{position:fixed;bottom:96px;right:20px;width:370px;max-width:calc(100vw - 32px);height:560px;max-height:calc(100vh - 120px);background:#fff;border-radius:18px;box-shadow:0 20px 60px rgba(15,15,35,.28);z-index:9999;display:none;flex-direction:column;overflow:hidden;font-family:"Manrope",system-ui,-apple-system,sans-serif}'+
  '.mly-bot-panel.mly-bot-open{display:flex;animation:mly-slide .24s ease}'+
  '@keyframes mly-slide{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}'+
  '.mly-bot-header{background:linear-gradient(135deg,#0f0f23,#1a1a3e);color:#fff;padding:16px 18px;display:flex;align-items:center;gap:12px;border-bottom:3px solid #d4a853}'+
  '.mly-bot-avatar{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#e94560,#d4a853);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:800;flex-shrink:0;color:#fff;font-family:"Syne","Manrope",sans-serif}'+
  '.mly-bot-head-info{flex:1;min-width:0}'+
  '.mly-bot-title{font-weight:800;font-size:15px;margin:0;letter-spacing:.2px}'+
  '.mly-bot-sub{font-size:12px;opacity:.85;margin:2px 0 0;display:flex;align-items:center;gap:5px}'+
  '.mly-bot-sub::before{content:"";width:8px;height:8px;border-radius:50%;background:#4ade80;display:inline-block;box-shadow:0 0 0 0 rgba(74,222,128,.7);animation:mly-dot 2s infinite}'+
  '@keyframes mly-dot{0%{box-shadow:0 0 0 0 rgba(74,222,128,.7)}70%{box-shadow:0 0 0 8px rgba(74,222,128,0)}100%{box-shadow:0 0 0 0 rgba(74,222,128,0)}}'+
  '.mly-bot-close{background:none;border:none;color:#fff;cursor:pointer;padding:6px;border-radius:50%;display:flex;align-items:center;justify-content:center;opacity:.85}'+
  '.mly-bot-close:hover{background:rgba(255,255,255,.15);opacity:1}'+
  '.mly-bot-messages{flex:1;overflow-y:auto;padding:16px;background:#f7f7fb;display:flex;flex-direction:column;gap:10px}'+
  '.mly-msg{max-width:84%;padding:11px 14px;border-radius:14px;font-size:14px;line-height:1.5;word-wrap:break-word}'+
  '.mly-msg a{color:#e94560;text-decoration:underline;font-weight:600}'+
  '.mly-msg-bot{background:#fff;color:#1f2937;align-self:flex-start;border-bottom-left-radius:4px;box-shadow:0 1px 3px rgba(15,15,35,.08)}'+
  '.mly-msg-user{background:linear-gradient(135deg,#0f0f23,#1a1a3e);color:#fff;align-self:flex-end;border-bottom-right-radius:4px}'+
  '.mly-msg-bot b{color:#0f0f23}'+
  '.mly-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}'+
  '.mly-chip{background:#fff;border:1.5px solid #e94560;color:#e94560;padding:7px 13px;border-radius:999px;font-size:12.5px;font-weight:600;cursor:pointer;transition:all .15s;font-family:inherit}'+
  '.mly-chip:hover{background:#e94560;color:#fff;transform:translateY(-1px);box-shadow:0 3px 10px rgba(233,69,96,.3)}'+
  '.mly-bot-wa-btn{background:#25d366;color:#fff;border:none;padding:11px 18px;border-radius:10px;font-size:13.5px;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:8px;margin-top:4px;text-decoration:none;align-self:flex-start;box-shadow:0 4px 14px rgba(37,211,102,.3)}'+
  '.mly-bot-wa-btn:hover{background:#1ebe57;transform:translateY(-1px);box-shadow:0 6px 18px rgba(37,211,102,.4)}'+
  '.mly-bot-input{display:flex;gap:8px;padding:12px;border-top:1px solid #e5e7eb;background:#fff}'+
  '.mly-bot-input input{flex:1;border:1.5px solid #d1d5db;border-radius:10px;padding:10px 14px;font-size:14px;outline:none;font-family:inherit;transition:border-color .15s}'+
  '.mly-bot-input input:focus{border-color:#e94560}'+
  '.mly-bot-input button{background:linear-gradient(135deg,#e94560,#d4a853);color:#fff;border:none;width:44px;height:44px;border-radius:10px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:transform .15s}'+
  '.mly-bot-input button:hover{transform:scale(1.05)}'+
  '.mly-bot-input button:disabled{opacity:.5;cursor:not-allowed}'+
  '.mly-bot-typing{display:inline-flex;gap:3px;align-items:center;padding:12px 15px}'+
  '.mly-bot-typing span{width:7px;height:7px;border-radius:50%;background:#9ca3af;animation:mly-bounce 1.2s infinite}'+
  '.mly-bot-typing span:nth-child(2){animation-delay:.15s}'+
  '.mly-bot-typing span:nth-child(3){animation-delay:.3s}'+
  '@keyframes mly-bounce{0%,60%,100%{transform:translateY(0);opacity:.5}30%{transform:translateY(-6px);opacity:1}}'+
  '.mly-bot-foot{font-size:11.5px;text-align:center;padding:0;background:#f7f7fb;border-top:1px solid #e5e7eb}'+
  '.mly-foot-wa{display:block;padding:9px 10px;color:#fff;text-decoration:none;background:linear-gradient(135deg,#25d366,#1ebe57);transition:background .2s;font-weight:500}'+
  '.mly-foot-wa:hover{background:linear-gradient(135deg,#1ebe57,#0e9d3f)}'+
  '.mly-foot-wa b{color:#fff;font-weight:700}'+
  '@media(max-width:480px){.mly-bot-panel{bottom:80px;right:8px;left:8px;width:auto;max-width:none;height:calc(100vh - 100px)}.mly-bot-fab{bottom:14px;right:14px;width:58px;height:58px}.mly-bot-fab svg{width:26px;height:26px}}';

  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // El wa-float queda visible a la izquierda; el bot chat va a la derecha (no duplicamos).

  var fab = document.createElement('button');
  fab.className = 'mly-bot-fab';
  fab.setAttribute('aria-label', 'Hablar con Bea, asistente de Importadora Maully');
  fab.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.48 2 2 6.04 2 11c0 2.52 1.18 4.8 3.08 6.43L4 22l4.73-1.28c1 .27 2.07.42 3.27.42 5.52 0 10-4.04 10-9S17.52 2 12 2zM8 12.5c-.83 0-1.5-.67-1.5-1.5S7.17 9.5 8 9.5s1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg><span class="mly-bot-ping"></span>';
  document.body.appendChild(fab);

  var tooltip = document.createElement('div');
  tooltip.className = 'mly-bot-tooltip';
  tooltip.innerHTML = '🤖 ¿Dudas? Soy <b>Bea</b>, tu asistente. Hazme una pregunta o haz click.';
  document.body.appendChild(tooltip);

  var panel = document.createElement('div');
  panel.className = 'mly-bot-panel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Chat con Bea de Importadora Maully');
  panel.innerHTML =
    '<div class="mly-bot-header">'+
      '<div class="mly-bot-avatar">B</div>'+
      '<div class="mly-bot-head-info">'+
        '<p class="mly-bot-title">Bea · Importadora Maully</p>'+
        '<p class="mly-bot-sub">En línea · responde al toque</p>'+
      '</div>'+
      '<button class="mly-bot-close" aria-label="Cerrar chat"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg></button>'+
    '</div>'+
    '<div class="mly-bot-messages" id="mlyBotMessages"></div>'+
    '<form class="mly-bot-input" id="mlyBotForm">'+
      '<input type="text" id="mlyBotInput" placeholder="Escribe tu consulta..." autocomplete="off" maxlength="200">'+
      '<button type="submit" aria-label="Enviar"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg></button>'+
    '</form>'+
    '<div class="mly-bot-foot">'+
      '<a href="' + WA_BASE + encodeURIComponent('Hola Bea! Tengo una consulta') + '" target="_blank" rel="noopener" class="mly-foot-wa">'+
        '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" style="vertical-align:-2px"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.71.306 1.263.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884"/></svg>'+
        ' ¿No encuentras lo que buscas? <b>Te paso con Bea por WhatsApp</b>'+
      '</a>'+
    '</div>';
  document.body.appendChild(panel);

  var msgs = panel.querySelector('#mlyBotMessages');
  var form = panel.querySelector('#mlyBotForm');
  var input = panel.querySelector('#mlyBotInput');

  function scroll() { msgs.scrollTop = msgs.scrollHeight; }

  function addBot(html) {
    var div = document.createElement('div');
    div.className = 'mly-msg mly-msg-bot';
    div.innerHTML = html;
    msgs.appendChild(div);
    scroll();
  }

  function addUser(text) {
    var div = document.createElement('div');
    div.className = 'mly-msg mly-msg-user';
    div.textContent = text;
    msgs.appendChild(div);
    scroll();
  }

  function addTyping() {
    var div = document.createElement('div');
    div.className = 'mly-msg mly-msg-bot mly-bot-typing-wrap';
    div.innerHTML = '<span class="mly-bot-typing"><span></span><span></span><span></span></span>';
    msgs.appendChild(div);
    scroll();
    return div;
  }

  function addQuickChips(ids, label) {
    var wrap = document.createElement('div');
    wrap.className = 'mly-msg mly-msg-bot';
    var html = label ? '<div style="margin-bottom:8px">' + label + '</div>' : '';
    html += '<div class="mly-chips">';
    ids.forEach(function (id) {
      var kb = KB.find(function (k) { return k.id === id; });
      if (kb) html += '<button class="mly-chip" data-intent="' + id + '">' + kb.title.replace(/^¿|¿/g, '') + '</button>';
    });
    html += '</div>';
    wrap.innerHTML = html;
    msgs.appendChild(wrap);
    scroll();
  }

  function addWhatsAppCTA(prefill) {
    var msg = prefill || 'Hola Bea! Tengo una consulta que no encontré en la web';
    var link = WA_BASE + encodeURIComponent(msg);
    var a = document.createElement('a');
    a.className = 'mly-bot-wa-btn';
    a.href = link;
    a.target = '_blank';
    a.rel = 'noopener';
    a.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.71.306 1.263.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/></svg> Hablar con Bea por WhatsApp';
    var wrap = document.createElement('div');
    wrap.style.alignSelf = 'flex-start';
    wrap.appendChild(a);
    msgs.appendChild(wrap);
    scroll();
  }

  function respondIntent(kb) {
    var t = addTyping();
    setTimeout(function () {
      t.remove();
      addBot('<b>' + kb.title + '</b><br>' + kb.answer);
      // Sugerir WhatsApp para temas que requieren cotización personalizada
      if (['catalogo', 'retorno', 'curso', 'argentina', 'tienda', 'marcas'].indexOf(kb.id) !== -1) {
        setTimeout(function () {
          addWhatsAppCTA('Hola Bea! Tengo una consulta sobre ' + kb.title.replace(/^¿|¿/g, '').toLowerCase());
        }, 350);
      }
    }, 500);
  }

  function respondNoMatch(userText) {
    var t = addTyping();
    setTimeout(function () {
      t.remove();
      addBot('No tengo una respuesta exacta para eso 🤔. Te paso directo con <b>Bea</b> — ella responde al toque por WhatsApp y te arma una cotización personalizada.');
      addWhatsAppCTA('Hola Bea! ' + userText);
    }, 600);
  }

  function handleUserMessage(text) {
    text = (text || '').trim();
    if (!text) return;
    addUser(text);
    var kb = findIntent(text);
    if (kb) respondIntent(kb);
    else respondNoMatch(text);
  }

  // Event listeners
  fab.addEventListener('click', function () {
    var open = panel.classList.toggle('mly-bot-open');
    if (open) {
      tooltip.style.display = 'none';
      fab.classList.add('mly-bot-active');
      if (!msgs.childElementCount) {
        addBot('¡Hola! 👋 Soy <b>Bea</b>, asistente de <b>Importadora Maully</b>. Te ayudo con fardos, packs, calugas, envíos y precios. ¿Qué necesitas?');
        addQuickChips(QUICK, 'Preguntas frecuentes — haz click o escribe tu consulta:');
      }
      setTimeout(function () { input.focus(); }, 300);
    } else {
      fab.classList.remove('mly-bot-active');
    }
  });

  panel.querySelector('.mly-bot-close').addEventListener('click', function () {
    panel.classList.remove('mly-bot-open');
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = input.value;
    input.value = '';
    handleUserMessage(v);
  });

  msgs.addEventListener('click', function (e) {
    var chip = e.target.closest('.mly-chip');
    if (!chip) return;
    var intent = chip.getAttribute('data-intent');
    var kb = KB.find(function (k) { return k.id === intent; });
    if (kb) {
      addUser(kb.title);
      respondIntent(kb);
    }
  });

  // Bounce sutil a los 60s para llamar la atención
  setTimeout(function () {
    if (!panel.classList.contains('mly-bot-open') && fab.animate) {
      fab.animate(
        [{ transform: 'scale(1)' }, { transform: 'scale(1.15)' }, { transform: 'scale(1)' }],
        { duration: 900, iterations: 2 }
      );
    }
  }, 60000);
})();
