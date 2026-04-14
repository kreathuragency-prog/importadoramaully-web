// ============ MAULLY ADMIN PANEL ============
const API = '/api';

// ============ AUTH ============
async function checkAuth(){
  try{
    const res = await fetch(API+'/me',{credentials:'include'});
    const data = await res.json();
    return data.authenticated;
  }catch(e){return false}
}

async function login(password){
  const res = await fetch(API+'/login',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    credentials:'include',
    body:JSON.stringify({password})
  });
  if(!res.ok){
    const err = await res.json().catch(()=>({detail:'Error'}));
    throw new Error(err.detail || 'Error al ingresar');
  }
  return res.json();
}

async function logout(){
  await fetch(API+'/logout',{method:'POST',credentials:'include'});
  location.reload();
}

// ============ PRODUCTS ============
let allProducts = [];
let currentEditId = null;

async function loadProducts(){
  const res = await fetch(API+'/products');
  allProducts = await res.json();
  renderProducts();
  populateCatFilter();
  document.getElementById('productCount').textContent = allProducts.length;
}

function populateCatFilter(){
  const sel = document.getElementById('filterCat');
  const cats = [...new Set(allProducts.map(p=>p.cat))].sort();
  sel.innerHTML = '<option value="">Todas las categorías</option>' +
    cats.map(c=>`<option value="${c}">${c}</option>`).join('');
}

function renderProducts(){
  const search = document.getElementById('searchProduct').value.toLowerCase();
  const cat = document.getElementById('filterCat').value;
  let filtered = allProducts;
  if(cat) filtered = filtered.filter(p=>p.cat===cat);
  if(search) filtered = filtered.filter(p=>p.name.toLowerCase().includes(search));

  const tbody = document.getElementById('productsTableBody');
  if(filtered.length===0){
    tbody.innerHTML = '<tr><td colspan="9" style="text-align:center;padding:40px;color:var(--text-muted)">No hay productos</td></tr>';
    return;
  }
  tbody.innerHTML = filtered.map(p=>`
    <tr>
      <td>#${p.id}</td>
      <td><span class="tier-badge ${p.tier||'primera'}">${p.cat}</span></td>
      <td>${escapeHtml(p.name)}</td>
      <td>${p.weight}</td>
      <td class="price-cell">$${p.price.toLocaleString('es-CL')}</td>
      <td class="orig-price-cell">$${p.origPrice.toLocaleString('es-CL')}</td>
      <td><span class="tier-badge ${p.tier}">${p.tier}</span></td>
      <td>${p.isNew?'<span class="badge-new">NEW</span>':''}</td>
      <td>
        <button class="action-btn" onclick="editProduct(${p.id})"><i class="fas fa-edit"></i></button>
      </td>
    </tr>
  `).join('');
}

function openProductModal(product=null){
  currentEditId = product ? product.id : null;
  document.getElementById('modalTitle').textContent = product ? 'Editar Producto' : 'Nuevo Producto';
  document.getElementById('deleteBtn').style.display = product ? 'inline-flex' : 'none';
  document.getElementById('productId').value = product?.id || '';
  document.getElementById('productName').value = product?.name || '';
  document.getElementById('productCat').value = product?.cat || 'chaquetas';
  document.getElementById('productWeight').value = product?.weight || '25kg';
  document.getElementById('productPrice').value = product?.price || '';
  document.getElementById('productOrigPrice').value = product?.origPrice || '';
  document.getElementById('productTier').value = product?.tier || 'primera';
  document.getElementById('productBadge').value = product?.badge || 'primera';
  document.getElementById('productIsNew').checked = product?.isNew || false;
  document.getElementById('productImg').value = product?.img || 'fardo-maully.jpg';
  document.getElementById('productModal').style.display = 'flex';
}

function closeProductModal(){
  document.getElementById('productModal').style.display = 'none';
  currentEditId = null;
}

window.editProduct = function(id){
  const p = allProducts.find(x=>x.id===id);
  if(p) openProductModal(p);
};

async function saveProduct(e){
  e.preventDefault();
  const payload = {
    cat: document.getElementById('productCat').value,
    name: document.getElementById('productName').value.trim(),
    price: parseInt(document.getElementById('productPrice').value,10),
    origPrice: parseInt(document.getElementById('productOrigPrice').value,10),
    weight: document.getElementById('productWeight').value.trim(),
    tier: document.getElementById('productTier').value,
    badge: document.getElementById('productBadge').value,
    isNew: document.getElementById('productIsNew').checked,
    img: document.getElementById('productImg').value.trim()
  };
  try{
    const url = currentEditId ? `${API}/products/${currentEditId}` : `${API}/products`;
    const method = currentEditId ? 'PUT' : 'POST';
    const res = await fetch(url,{
      method,
      headers:{'Content-Type':'application/json'},
      credentials:'include',
      body:JSON.stringify(payload)
    });
    if(!res.ok) throw new Error('Error al guardar');
    toast(currentEditId ? 'Producto actualizado' : 'Producto creado','success');
    closeProductModal();
    await loadProducts();
  }catch(e){
    toast(e.message,'error');
  }
}

async function deleteProduct(){
  if(!currentEditId) return;
  if(!confirm('¿Eliminar este producto? Esta acción no se puede deshacer.')) return;
  try{
    const res = await fetch(`${API}/products/${currentEditId}`,{
      method:'DELETE',
      credentials:'include'
    });
    if(!res.ok) throw new Error('Error al eliminar');
    toast('Producto eliminado','success');
    closeProductModal();
    await loadProducts();
  }catch(e){
    toast(e.message,'error');
  }
}

// ============ ORDERS ============
let allOrders = [];

async function loadOrders(){
  try{
    const res = await fetch(API+'/orders',{credentials:'include'});
    if(!res.ok) throw new Error('Error al cargar pedidos');
    allOrders = await res.json();
    renderOrders();
    document.getElementById('orderCount').textContent = allOrders.length;
  }catch(e){
    toast(e.message,'error');
  }
}

function renderOrders(){
  const status = document.getElementById('filterStatus').value;
  let list = allOrders;
  if(status) list = list.filter(o=>o.status===status);
  list = [...list].sort((a,b)=>b.created_at-a.created_at);

  const wrap = document.getElementById('ordersList');
  if(list.length===0){
    wrap.innerHTML = '<div class="orders-empty"><i class="fas fa-inbox"></i><p>No hay pedidos aún</p></div>';
    return;
  }
  wrap.innerHTML = list.map(o=>{
    const date = new Date(o.created_at*1000).toLocaleString('es-CL');
    const itemsHtml = (o.items||[]).map(i=>
      `<div class="order-item-line"><span>${escapeHtml(i.name)} × ${i.qty}</span><span>$${(i.price*i.qty).toLocaleString('es-CL')}</span></div>`
    ).join('');
    const c = o.customer||{};
    const s = o.shipping||{};
    return `<div class="order-card ${o.status}">
      <div class="order-header">
        <div>
          <div class="order-id">Pedido #${o.id}</div>
          <div class="order-date">${date}</div>
        </div>
        <select class="order-status-select" onchange="updateOrderStatus(${o.id},this.value)">
          <option value="pending" ${o.status==='pending'?'selected':''}>Pendiente</option>
          <option value="paid" ${o.status==='paid'?'selected':''}>Pagado</option>
          <option value="shipped" ${o.status==='shipped'?'selected':''}>Enviado</option>
          <option value="delivered" ${o.status==='delivered'?'selected':''}>Entregado</option>
          <option value="cancelled" ${o.status==='cancelled'?'selected':''}>Cancelado</option>
        </select>
      </div>
      <div class="order-customer">
        <strong>Cliente</strong>
        ${escapeHtml(c.name||'')} · ${escapeHtml(c.email||'')} · ${escapeHtml(c.phone||'')}<br>
        RUT: ${escapeHtml(c.rut||'-')}
      </div>
      <div class="order-customer">
        <strong>Envío</strong>
        ${escapeHtml(s.method||'-')} · ${escapeHtml(s.address||'')} ${escapeHtml(s.city||'')} ${escapeHtml(s.region||'')}
      </div>
      <div class="order-items">
        <strong>Productos</strong>
        ${itemsHtml}
      </div>
      <div class="order-total">Total: $${(o.total||0).toLocaleString('es-CL')} CLP</div>
    </div>`;
  }).join('');
}

window.updateOrderStatus = async function(id, status){
  try{
    const res = await fetch(`${API}/orders/${id}`,{
      method:'PATCH',
      headers:{'Content-Type':'application/json'},
      credentials:'include',
      body:JSON.stringify({status})
    });
    if(!res.ok) throw new Error('Error al actualizar');
    toast('Estado actualizado','success');
    await loadOrders();
  }catch(e){
    toast(e.message,'error');
  }
};

// ============ UI HELPERS ============
function escapeHtml(s){
  if(s==null) return '';
  return String(s).replace(/[&<>"']/g,c=>({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  })[c]);
}

let toastTimer;
function toast(msg, type=''){
  const el = document.getElementById('toast');
  el.textContent = msg;
  el.className = 'toast '+type+' show';
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>{el.className = 'toast '+type},2500);
}

function switchTab(tab){
  document.querySelectorAll('.nav-btn[data-tab]').forEach(b=>b.classList.toggle('active',b.dataset.tab===tab));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.getElementById(tab+'Tab').classList.add('active');
  if(tab==='orders') loadOrders();
}

// ============ INIT ============
async function init(){
  const isAuth = await checkAuth();
  if(isAuth){
    document.getElementById('loginScreen').style.display='none';
    document.getElementById('adminPanel').style.display='block';
    await loadProducts();
  }else{
    document.getElementById('loginScreen').style.display='flex';
    document.getElementById('adminPanel').style.display='none';
  }
}

document.getElementById('loginForm').addEventListener('submit', async (e)=>{
  e.preventDefault();
  const pwd = document.getElementById('loginPassword').value;
  const errEl = document.getElementById('loginError');
  errEl.textContent = '';
  try{
    await login(pwd);
    await init();
  }catch(err){
    errEl.textContent = err.message;
  }
});

document.getElementById('logoutBtn').addEventListener('click', logout);
document.getElementById('newProductBtn').addEventListener('click', ()=>openProductModal());
document.getElementById('modalClose').addEventListener('click', closeProductModal);
document.getElementById('cancelBtn').addEventListener('click', closeProductModal);
document.getElementById('deleteBtn').addEventListener('click', deleteProduct);
document.getElementById('productForm').addEventListener('submit', saveProduct);
document.getElementById('searchProduct').addEventListener('input', renderProducts);
document.getElementById('filterCat').addEventListener('change', renderProducts);
document.getElementById('filterStatus').addEventListener('change', renderOrders);
document.getElementById('refreshOrdersBtn').addEventListener('click', loadOrders);
document.querySelectorAll('.nav-btn[data-tab]').forEach(btn=>{
  btn.addEventListener('click', ()=>switchTab(btn.dataset.tab));
});
document.getElementById('productModal').addEventListener('click', (e)=>{
  if(e.target.id==='productModal') closeProductModal();
});

init();
