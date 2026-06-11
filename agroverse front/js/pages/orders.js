/* pages/orders.js — Мои заказы (покупатель) */

function badgeOrderHtml(status) {
  const map = {
    created:           ['badge-created',    t('order_status_created')],
    paid:              ['badge-paid',        t('order_status_paid')],
    ready_for_pickup:  ['badge-ready',       t('order_status_ready')],
    ready:             ['badge-ready',       t('order_status_ready')],
    completed:         ['badge-completed',   t('order_status_completed')],
    cancelled:         ['badge-cancelled',   t('order_status_cancelled')],
  };
  const [cls, label] = map[status] || ['badge-created', status];
  return `<span class="badge ${cls}">${label}</span>`;
}

async function renderOrders() {
  const app = document.getElementById('app');
  app.innerHTML = pageShell(`
    <div class="page-head">
      <h1 class="page-title">📦 ${t('nav_orders')}</h1>
      <p class="page-desc">${t('orders_desc')}</p>
    </div>
    <div id="orders-wrap"><div class="spinner"></div></div>
  `);
  loadOrdersList();
}

async function loadOrdersList() {
  const wrap = document.getElementById('orders-wrap');
  if (!wrap) return;
  try {
    const data = await API.getMyOrders();
    const orders = data?.orders || data || [];
    if (!orders?.length) {
      wrap.innerHTML = `
        <div class="empty-state big">
          <div class="icon">📦</div>
          <p>${t('orders_empty')}</p>
          <button class="btn btn-primary" onclick="router.go('/market')">${t('go_market')}</button>
        </div>`;
      return;
    }
    wrap.innerHTML = `<div class="orders-list">${orders.map(orderCardHtml).join('')}</div>`;
  } catch (e) {
    wrap.innerHTML = `<div class="empty-state"><p>⚠️ ${e.message}</p></div>`;
  }
}

function orderCardHtml(o) {
  const date  = o.created_at ? new Date(o.created_at).toLocaleDateString() : '—';
  const total = o.total_price != null ? `${Number(o.total_price).toLocaleString()} ${t('currency')}` : '—';
  const canCancel   = ['created', 'paid'].includes(o.status);
  const canComplete = o.status === 'ready_for_pickup' || o.status === 'ready';
  const img = o.product_photo ? `<img src="${API_PHOTO(o.product_photo)}" onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'oc-ph',textContent:'🥬'}))"/>` : '<div class="oc-ph">🥬</div>';
  return `
    <div class="order-card" id="buyer-order-${o.id}">
      <div class="oc-img">${img}</div>
      <div class="oc-main">
        <div class="oc-top">
          <span class="oc-name">${o.product_title || (t('product_word') + ' #' + o.product_id)}</span>
          ${badgeOrderHtml(o.status)}
        </div>
        <div class="oc-meta">🌱 ${o.fermer_name || t('farmer_word')} · ${o.quantity} ${t('pcs')} · ${date}</div>
        ${total !== '—' ? `<div class="oc-total">${total}</div>` : ''}
      </div>
      <div class="oc-actions">
        ${canCancel   ? `<button class="btn btn-danger btn-sm"  onclick="cancelOrder(${o.id})">${t('cancel_order')}</button>` : ''}
        ${canComplete ? `<button class="btn btn-primary btn-sm" onclick="confirmReceived(${o.id})">${t('confirm_received')}</button>` : ''}
      </div>
    </div>
  `;
}

function API_PHOTO(u) {
  if (!u) return '';
  return u.startsWith('http') ? u : (`http://${location.hostname}:8000` + u);
}

async function cancelOrder(id) {
  if (!confirm(t('confirm_cancel_order'))) return;
  try { await API.cancelOrder(id); showToast(t('order_cancelled')); loadOrdersList(); }
  catch (e) { showToast(e.message, 'error'); }
}

async function confirmReceived(id) {
  try { await API.completeOrder(id); showToast('✅ ' + t('order_received')); loadOrdersList(); }
  catch (e) { showToast(e.message, 'error'); }
}

window.renderOrders = renderOrders;
window.cancelOrder  = cancelOrder;
window.confirmReceived = confirmReceived;
