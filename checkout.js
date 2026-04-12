/**
 * Checkout JS — Importadora Maully
 * 3-step checkout: Datos → Envio → Pago MercadoPago
 */

// API base — cambiar en produccion
const API_BASE = window.location.hostname === 'localhost'
  ? 'http://localhost:8000'
  : 'https://api.importadoramaully.cl';  // Tu backend FastAPI

// ── Cart from localStorage ──
let cart = [];
try {
  cart = JSON.parse(localStorage.getItem('maully_cart') || '[]');
} catch(e) { cart = []; }

if (cart.length === 0 && !window.location.search.includes('status=')) {
  // Show empty cart msg instead of silent redirect
  document.addEventListener('DOMContentLoaded', () => {
    document.body.innerHTML = `
      <div style="max-width:500px;margin:100px auto;text-align:center;padding:40px;font-family:system-ui,sans-serif">
        <i class="fas fa-shopping-cart" style="font-size:4rem;color:#d4af37;margin-bottom:20px"></i>
        <h1 style="color:#1a1a2e;margin-bottom:12px">Tu carrito esta vacio</h1>
        <p style="color:#666;margin-bottom:24px">Agrega fardos al carrito antes de pagar.</p>
        <a href="/" style="background:#d4af37;color:#1a1a2e;padding:14px 28px;border-radius:50px;text-decoration:none;font-weight:700;display:inline-block">← Volver al catalogo</a>
      </div>`;
  });
}

let config = {};
let selectedShipping = 'starken';
let shippingCost = 0;
let currentStep = 1;

// ── Format helpers ──
function fmtPrice(n) {
  return '$' + Math.round(n).toLocaleString('es-CL');
}

// ── Init ──
async function init() {
  // Check URL params for payment result
  const params = new URLSearchParams(window.location.search);
  const status = params.get('status');
  const orderNum = params.get('order');

  if (status) {
    document.querySelectorAll('.ck-panel').forEach(p => p.style.display = 'none');
    document.querySelector('.ck-sidebar').style.display = 'none';
    document.querySelector('.ck-progress').style.display = 'none';

    if (status === 'success') {
      document.getElementById('resultSuccess').style.display = 'block';
      document.getElementById('successOrderNum').textContent = orderNum || '';
      localStorage.removeItem('maully_cart');
    } else if (status === 'pending') {
      document.getElementById('resultPending').style.display = 'block';
      document.getElementById('pendingOrderNum').textContent = orderNum || '';
    } else {
      document.getElementById('resultFailure').style.display = 'block';
    }
    return;
  }

  // Load config
  try {
    const resp = await fetch(API_BASE + '/api/config');
    config = await resp.json();
  } catch(e) {
    console.warn('Could not load config, using defaults');
    config = { regiones: [
      "Arica y Parinacota","Tarapaca","Antofagasta","Atacama","Coquimbo",
      "Valparaiso","Region Metropolitana","O'Higgins","Maule","Nuble",
      "Biobio","Araucania","Los Rios","Los Lagos","Aysen","Magallanes"
    ]};
  }

  renderCart();
  populateRegions();
  setupRadios();
  renderShippingOptions();
  setupInputFormatters();
}

// ── Input auto-format ──
function setupInputFormatters() {
  const rut = document.getElementById('ckRut');
  if (rut) {
    rut.addEventListener('input', (e) => {
      let v = e.target.value.replace(/[^0-9kK]/g, '').toUpperCase();
      if (v.length > 1) {
        const body = v.slice(0, -1);
        const dv = v.slice(-1);
        // Format: 12.345.678-9
        const fmt = body.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        e.target.value = fmt + '-' + dv;
      } else {
        e.target.value = v;
      }
    });
  }

  const phone = document.getElementById('ckPhone');
  if (phone) {
    phone.addEventListener('input', (e) => {
      let v = e.target.value.replace(/[^\d+]/g, '');
      // Chilean mobile format: +56 9 1234 5678
      if (v.startsWith('+56') && v.length > 3) {
        const rest = v.slice(3);
        if (rest.length <= 1) v = '+56 ' + rest;
        else if (rest.length <= 5) v = '+56 ' + rest[0] + ' ' + rest.slice(1);
        else v = '+56 ' + rest[0] + ' ' + rest.slice(1, 5) + ' ' + rest.slice(5, 9);
      }
      e.target.value = v;
    });
    // Prefill with +56
    if (!phone.value) phone.value = '+56 9 ';
  }

  // Business RUT too
  const bizRut = document.getElementById('ckBizRut');
  if (bizRut) {
    bizRut.addEventListener('input', (e) => {
      let v = e.target.value.replace(/[^0-9kK]/g, '').toUpperCase();
      if (v.length > 1) {
        const body = v.slice(0, -1);
        const dv = v.slice(-1);
        e.target.value = body.replace(/\B(?=(\d{3})+(?!\d))/g, '.') + '-' + dv;
      } else {
        e.target.value = v;
      }
    });
  }
}

// ── Render cart sidebar ──
function renderCart() {
  const container = document.getElementById('ckCartItems');
  if (!container) return;

  container.innerHTML = cart.map(item => {
    const subtotal = item.price * (item.qty || 1);
    return `<div class="ck-cart-item">
      <div class="ck-cart-item-name">
        ${item.name}
        <span>${item.weight || ''} × ${item.qty || 1}</span>
      </div>
      <div class="ck-cart-item-price">${fmtPrice(subtotal)}</div>
    </div>`;
  }).join('');

  updateTotals();
}

function updateTotals() {
  const totals = document.getElementById('ckTotals');
  if (!totals) return;

  const subtotal = cart.reduce((s, i) => s + i.price * (i.qty || 1), 0);
  const total = subtotal + shippingCost;

  totals.innerHTML = `
    <div class="ck-total-row"><span>Subtotal</span><span>${fmtPrice(subtotal)}</span></div>
    <div class="ck-total-row"><span>Envio (${selectedShipping.replace('_',' ')})</span><span>${selectedShipping === 'starken' || selectedShipping === 'dhl' ? 'Por pagar' : 'Gratis'}</span></div>
    <div class="ck-total-row"><span>IVA incluido</span><span>-</span></div>
    <div class="ck-total-row total"><span>Total</span><span>${fmtPrice(total)}</span></div>
  `;
}

// ── Populate regions select ──
function populateRegions() {
  const sel = document.getElementById('ckRegion');
  if (!sel) return;
  const regiones = config.regiones || [];
  regiones.forEach(r => {
    const opt = document.createElement('option');
    opt.value = r;
    opt.textContent = r;
    sel.appendChild(opt);
  });

  sel.addEventListener('change', () => calcShipping());
}

// ── Setup radio buttons ──
function setupRadios() {
  document.querySelectorAll('.ck-radio').forEach(label => {
    label.addEventListener('click', () => {
      label.closest('.ck-radio-group').querySelectorAll('.ck-radio').forEach(r => r.classList.remove('active'));
      label.classList.add('active');
      label.querySelector('input').checked = true;

      // Toggle factura fields
      const val = label.querySelector('input').value;
      const facturaFields = document.querySelector('.ck-factura-fields');
      if (facturaFields) {
        facturaFields.style.display = val === 'factura' ? 'block' : 'none';
      }
    });
  });
}

// ── Shipping options ──
function renderShippingOptions() {
  const container = document.getElementById('shippingOptions');
  if (!container) return;

  const methods = config.shipping_methods || [
    {id:'starken', name:'Starken', desc:'Envio economico, 5-10 dias habiles. Flete por pagar.', icon:'fa-truck', por_pagar:true},
    {id:'dhl', name:'DHL Express', desc:'Envio rapido, 2-5 dias habiles. Flete por pagar.', icon:'fa-shipping-fast', por_pagar:true},
    {id:'coordinar_whatsapp', name:'Coordinar por WhatsApp', desc:'Conversemos el mejor envio para ti', icon:'fab fa-whatsapp', free:true},
    {id:'retiro_santiago', name:'Retiro Santiago', desc:'Av. La Florida 9421, Santiago', icon:'fa-store', free:true},
    {id:'retiro_pichilemu', name:'Retiro Pichilemu', desc:'Av. Millaco 1172, Pichilemu', icon:'fa-store', free:true},
  ];

  container.innerHTML = methods.map((m, i) => `
    <label class="ck-ship-option${i === 0 ? ' active' : ''}" data-method="${m.id}">
      <input type="radio" name="shipping" value="${m.id}" ${i === 0 ? 'checked' : ''}>
      <div class="ck-ship-icon"><i class="${m.icon && (m.icon.includes('fab') || m.icon.includes('fas')) ? '' : 'fas '}${m.icon}"></i></div>
      <div class="ck-ship-info">
        <strong>${m.name}</strong>
        <small>${m.desc}</small>
      </div>
      <div class="ck-ship-price${m.free ? ' free' : ''}${m.por_pagar ? ' por-pagar' : ''}" data-method="${m.id}">
        ${m.free ? 'Gratis' : m.por_pagar ? 'Por pagar' : 'Calculando...'}
      </div>
    </label>
  `).join('');

  container.querySelectorAll('.ck-ship-option').forEach(opt => {
    opt.addEventListener('click', () => {
      container.querySelectorAll('.ck-ship-option').forEach(o => o.classList.remove('active'));
      opt.classList.add('active');
      opt.querySelector('input').checked = true;
      selectedShipping = opt.dataset.method;

      // Toggle address fields — hide for retiro and coordinar WhatsApp
      const addrFields = document.getElementById('addressFields');
      if (addrFields) {
        const hideAddr = selectedShipping.startsWith('retiro') || selectedShipping === 'coordinar_whatsapp';
        addrFields.style.display = hideAddr ? 'none' : 'block';
      }

      calcShipping();
    });
  });

  calcShipping();
}

async function calcShipping() {
  // Starken/DHL van "por pagar" (el cliente paga al courier directo)
  // Retiro y coordinar WhatsApp son gratis en el checkout
  shippingCost = 0;
  updateTotals();
}

// ── Step navigation ──
function goStep(step) {
  // Validate current step
  if (step > currentStep) {
    if (currentStep === 1 && !validateStep1()) return;
    if (currentStep === 2 && !validateStep2()) return;
  }

  currentStep = step;

  // Show/hide panels
  for (let i = 1; i <= 3; i++) {
    const panel = document.getElementById('step' + i);
    if (panel) panel.style.display = i === step ? 'block' : 'none';
  }

  // Update progress
  document.querySelectorAll('.ck-step').forEach(s => {
    const n = parseInt(s.dataset.step);
    s.classList.remove('active', 'done');
    if (n === step) s.classList.add('active');
    else if (n < step) s.classList.add('done');
  });

  // Build summary on step 3
  if (step === 3) buildSummary();

  window.scrollTo({top: 0, behavior: 'smooth'});
}

function validateStep1() {
  const name = document.getElementById('ckName').value.trim();
  const rut = document.getElementById('ckRut').value.trim();
  const email = document.getElementById('ckEmail').value.trim();
  const phone = document.getElementById('ckPhone').value.trim();

  let valid = true;

  if (!name) { highlight('ckName'); valid = false; }
  if (!rut || !validateRut(rut)) {
    highlight('ckRut');
    document.getElementById('rutError').textContent = rut ? 'RUT invalido' : 'Requerido';
    valid = false;
  } else {
    document.getElementById('rutError').textContent = '';
  }
  if (!email || !email.includes('@')) { highlight('ckEmail'); valid = false; }
  if (!phone) { highlight('ckPhone'); valid = false; }

  return valid;
}

function validateStep2() {
  if (selectedShipping.startsWith('retiro') || selectedShipping === 'coordinar_whatsapp') return true;

  const region = document.getElementById('ckRegion').value;
  const address = document.getElementById('ckAddress').value.trim();
  const comuna = document.getElementById('ckComuna').value.trim();

  let valid = true;
  if (!region) { highlight('ckRegion'); valid = false; }
  if (!address) { highlight('ckAddress'); valid = false; }
  if (!comuna) { highlight('ckComuna'); valid = false; }
  return valid;
}

function highlight(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.classList.add('error');
  el.focus();
  setTimeout(() => el.classList.remove('error'), 3000);
}

function validateRut(rut) {
  rut = rut.replace(/\./g, '').replace('-', '').trim().toUpperCase();
  if (rut.length < 8) return false;
  const body = rut.slice(0, -1);
  const dv = rut.slice(-1);
  if (!/^\d+$/.test(body)) return false;
  let sum = 0, mul = 2;
  for (let i = body.length - 1; i >= 0; i--) {
    sum += parseInt(body[i]) * mul;
    mul = mul < 7 ? mul + 1 : 2;
  }
  const rem = 11 - (sum % 11);
  const expected = rem === 10 ? 'K' : rem === 11 ? '0' : String(rem);
  return dv === expected;
}

// ── Build order summary (step 3) ──
function buildSummary() {
  const summary = document.getElementById('orderSummary');
  if (!summary) return;

  const name = document.getElementById('ckName').value;
  const email = document.getElementById('ckEmail').value;
  const phone = document.getElementById('ckPhone').value;
  const docType = document.querySelector('input[name="docType"]:checked')?.value || 'boleta';
  const shipLabel = document.querySelector('.ck-ship-option.active .ck-ship-info strong')?.textContent || selectedShipping;
  const region = document.getElementById('ckRegion').value;
  const address = document.getElementById('ckAddress')?.value || '';
  const comuna = document.getElementById('ckComuna')?.value || '';

  const subtotal = cart.reduce((s, i) => s + i.price * (i.qty || 1), 0);
  const total = subtotal + shippingCost;

  summary.innerHTML = `
    <div class="ck-summary-section">
      <h4>Cliente</h4>
      <div class="ck-summary-row"><span>${name}</span><span>${email}</span></div>
      <div class="ck-summary-row"><span>${phone}</span><span>Documento: ${docType.toUpperCase()}</span></div>
      ${docType === 'factura' ? `<div class="ck-summary-row"><span>${document.getElementById('ckBizName')?.value || ''} (${document.getElementById('ckBizRut')?.value || ''})</span><span>Giro: ${document.getElementById('ckBizGiro')?.value || ''}</span></div>` : ''}
    </div>
    <div class="ck-summary-section">
      <h4>Envio</h4>
      <div class="ck-summary-row"><span>${shipLabel}</span><span>${selectedShipping === 'starken' || selectedShipping === 'dhl' ? 'Por pagar' : 'Gratis'}</span></div>
      ${!selectedShipping.startsWith('retiro') ? `<div class="ck-summary-row"><span>${address}, ${comuna}, ${region}</span></div>` : ''}
    </div>
    <div class="ck-summary-section">
      <h4>Productos (${cart.length})</h4>
      ${cart.map(i => `<div class="ck-summary-row"><span>${i.name} × ${i.qty || 1}</span><span>${fmtPrice(i.price * (i.qty || 1))}</span></div>`).join('')}
    </div>
    <div class="ck-summary-section" style="border-top:2px solid var(--dark);padding-top:10px;margin-top:8px">
      <div class="ck-summary-row"><span>Subtotal</span><span>${fmtPrice(subtotal)}</span></div>
      <div class="ck-summary-row"><span>Envio</span><span>${shippingCost > 0 ? fmtPrice(shippingCost) : 'Gratis'}</span></div>
      <div class="ck-summary-row" style="font-weight:700;font-size:1.1rem"><span>Total a Pagar</span><span style="color:var(--gold)">${fmtPrice(total)}</span></div>
    </div>
  `;
}

// ── Submit checkout → MercadoPago ──
async function submitCheckout() {
  const btn = document.getElementById('payBtn');
  btn.disabled = true;
  btn.innerHTML = '<span class="ck-spinner"></span> Procesando...';

  const docType = document.querySelector('input[name="docType"]:checked')?.value || 'boleta';

  const payload = {
    name: document.getElementById('ckName').value.trim(),
    rut: document.getElementById('ckRut').value.trim(),
    email: document.getElementById('ckEmail').value.trim(),
    phone: document.getElementById('ckPhone').value.trim(),
    address: document.getElementById('ckAddress')?.value.trim() || '',
    comuna: document.getElementById('ckComuna')?.value.trim() || '',
    region: document.getElementById('ckRegion')?.value || '',
    doc_type: docType,
    business_name: document.getElementById('ckBizName')?.value.trim() || '',
    business_rut: document.getElementById('ckBizRut')?.value.trim() || '',
    business_giro: document.getElementById('ckBizGiro')?.value.trim() || '',
    business_address: document.getElementById('ckBizAddress')?.value.trim() || '',
    shipping_method: selectedShipping,
    items: cart.map(i => ({
      id: i.id,
      name: i.name,
      price: i.price,
      qty: i.qty || 1,
      weight: i.weight || '20kg',
      cat: i.cat || '',
    })),
  };

  try {
    const resp = await fetch(API_BASE + '/api/checkout', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload),
    });

    if (!resp.ok) {
      const err = await resp.json();
      throw new Error(err.detail || 'Error al crear orden');
    }

    const data = await resp.json();

    // Redirect to MercadoPago
    if (data.mp_init_point) {
      window.location.href = data.mp_init_point;
    } else {
      throw new Error('No se obtuvo URL de pago');
    }

  } catch(e) {
    // Show inline error box instead of alert
    const errBox = document.getElementById('ckErrorBox') || (() => {
      const d = document.createElement('div');
      d.id = 'ckErrorBox';
      d.style.cssText = 'background:#fee;border:1px solid #f88;color:#c00;padding:14px;border-radius:8px;margin-top:12px;font-size:.9rem';
      document.getElementById('payBtn').parentNode.insertBefore(d, document.getElementById('payBtn'));
      return d;
    })();
    errBox.innerHTML = `<strong>No se pudo procesar el pago.</strong><br>${e.message}<br><br>Intenta de nuevo o escribenos por WhatsApp: <a href="https://wa.me/56990565137" style="color:#c00;text-decoration:underline">+56 9 9056 5137</a>`;
    btn.disabled = false;
    btn.innerHTML = '<i class="fas fa-lock"></i> Pagar con MercadoPago';
  }
}

// ── Start ──
init();
