/* =========================================================
   CarniCore — app.js
   Navegación e interacciones puramente visuales.
   No contiene lógica de negocio ni persistencia real.
   ========================================================= */

// Estructura del menú lateral (icono, etiqueta, archivo, grupo)
const NAV_ITEMS = [
  { group: "Panel" },
  { href: "dashboard.html",       icon: "fa-grid-2",           label: "Dashboard" },
  { href: "inicio.html",          icon: "fa-house",             label: "Inicio" },

  { group: "Recepción" },
  { href: "proveedores.html",     icon: "fa-truck-field",       label: "Proveedores" },
  { href: "guias-origen.html",    icon: "fa-file-shield",       label: "Guías de origen" },
  { href: "ingreso-lotes.html",   icon: "fa-boxes-stacked",     label: "Ingreso de lotes" },

  { group: "Pesaje y despiece" },
  { href: "pesaje.html",          icon: "fa-weight-scale",      label: "Pesaje inteligente" },
  { href: "ticket-pesaje.html",   icon: "fa-receipt",           label: "Comprobante de pesaje" },
  { href: "despiece.html",        icon: "fa-knife",             label: "Despiece y clasificación" },

  { group: "Almacenamiento" },
  { href: "camaras.html",         icon: "fa-snowflake",         label: "Cámaras frigoríficas" },
  { href: "inventario.html",      icon: "fa-warehouse",         label: "Inventario" },
  { href: "vida-util.html",       icon: "fa-hourglass-half",    label: "Vida útil" },
  { href: "alertas.html",         icon: "fa-bell",              label: "Alertas" },
  { href: "baja-productos.html",  icon: "fa-triangle-exclamation", label: "Baja de productos" },

  { group: "Comercial" },
  { href: "ventas.html",          icon: "fa-cash-register",     label: "Ventas" },
  { href: "movimientos.html",     icon: "fa-right-left",        label: "Movimientos de inventario" },
  { href: "trazabilidad.html",    icon: "fa-route",             label: "Trazabilidad" },
  { href: "conteo-inventario.html", icon: "fa-clipboard-list",  label: "Conteo de inventario" },

  { group: "Gestión" },
  { href: "reportes.html",        icon: "fa-chart-column",      label: "Reportes" },
  { href: "panel-gerencial.html", icon: "fa-chart-line",        label: "Panel gerencial" },
  { href: "usuarios.html",        icon: "fa-users",             label: "Usuarios" },
  { href: "roles.html",           icon: "fa-user-shield",       label: "Roles" },
  { href: "configuracion.html",   icon: "fa-gear",              label: "Configuración" },
];

function currentFile() {
  const parts = window.location.pathname.split("/");
  return parts[parts.length - 1] || "dashboard.html";
}

function buildSidebar() {
  const mount = document.getElementById("sidebar-mount");
  if (!mount) return;

  const file = currentFile();
  let linksHtml = "";

  NAV_ITEMS.forEach((item) => {
    if (item.group) {
      linksHtml += `<div class="nav-group-label">${item.group}</div>`;
    } else {
      const active = item.href === file ? "active" : "";
      linksHtml += `
        <a class="nav-link ${active}" href="${item.href}">
          <i class="fa-solid ${item.icon}"></i><span>${item.label}</span>
        </a>`;
    }
  });

  mount.innerHTML = `
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-brand">
        <div class="mark">CC</div>
        <div class="name">CarniCore<small>Trazabilidad &amp; Pesaje</small></div>
      </div>
      <nav class="sidebar-scroll">
        ${linksHtml}
      </nav>
      <div class="sidebar-foot">
        <a class="nav-link" href="login.html">
          <i class="fa-solid fa-right-from-bracket"></i><span>Cerrar sesión</span>
        </a>
      </div>
    </aside>`;
}

function buildTopbar() {
  const mount = document.getElementById("topbar-mount");
  if (!mount) return;

  const title = mount.dataset.title || "Módulo";
  const eyebrow = mount.dataset.eyebrow || "CarniCore";

  mount.innerHTML = `
    <header class="topbar">
      <div class="flex items-center gap-12">
        <button class="menu-toggle" id="menuToggle" aria-label="Abrir menú">
          <i class="fa-solid fa-bars"></i>
        </button>
        <div class="topbar-title">
          <span class="eyebrow">${eyebrow}</span>
          <h1>${title}</h1>
        </div>
      </div>
      <div class="topbar-right">
        <div class="search-mini">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" placeholder="Buscar en CarniCore..." />
        </div>
        <button class="icon-btn" title="Alertas" onclick="window.location.href='alertas.html'">
          <i class="fa-solid fa-bell"></i><span class="dot"></span>
        </button>
        <button class="icon-btn" title="Ayuda">
          <i class="fa-solid fa-circle-question"></i>
        </button>
        <div class="user-chip" onclick="window.location.href='configuracion.html'">
          <div class="avatar">GI</div>
          <div class="u-meta">
            <div class="u-name">Gisela Ibáñez</div>
            <div class="u-role">Propietaria</div>
          </div>
          <i class="fa-solid fa-chevron-down small text-dim"></i>
        </div>
      </div>
    </header>`;

  const toggle = document.getElementById("menuToggle");
  const sidebar = document.getElementById("sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
    document.addEventListener("click", (e) => {
      if (window.innerWidth > 900) return;
      if (!sidebar.contains(e.target) && !toggle.contains(e.target)) {
        sidebar.classList.remove("open");
      }
    });
  }
}

// Alterna visibilidad de contraseña (solo interacción visual)
function togglePassword(btn, inputId) {
  const input = document.getElementById(inputId);
  if (!input) return;
  const isPw = input.type === "password";
  input.type = isPw ? "text" : "password";
  btn.innerHTML = isPw
    ? '<i class="fa-solid fa-eye-slash"></i>'
    : '<i class="fa-solid fa-eye"></i>';
}

// Simula el cálculo de pesaje inteligente (solo visual, sin persistencia)
function simularPesaje() {
  const peso = document.getElementById("pesoInput");
  const precio = document.getElementById("precioInput");
  const total = document.getElementById("totalOutput");
  if (!peso || !precio || !total) return;
  const p = parseFloat(peso.value) || 0;
  const pr = parseFloat(precio.value) || 0;
  total.textContent = "$" + (p * pr).toFixed(2);
}

// Filtro simple de filas de tabla por texto (solo UI, no backend)
function filterTable(inputEl, tableId) {
  const table = document.getElementById(tableId);
  if (!table) return;
  const q = inputEl.value.toLowerCase();
  table.querySelectorAll("tbody tr").forEach((row) => {
    row.style.display = row.textContent.toLowerCase().includes(q) ? "" : "none";
  });
}

// Reloj / fecha decorativos para el ticket de pesaje
function stampNow(elId) {
  const el = document.getElementById(elId);
  if (!el) return;
  const d = new Date();
  el.textContent = d.toLocaleString("es-EC", {
    day: "2-digit", month: "2-digit", year: "numeric",
    hour: "2-digit", minute: "2-digit",
  });
}

document.addEventListener("DOMContentLoaded", () => {
  buildSidebar();
  buildTopbar();
  stampNow("ticketDate");
});
