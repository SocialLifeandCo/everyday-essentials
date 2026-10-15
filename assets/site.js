let menuButton = document.getElementById('menu');
let nav = document.getElementById('nav');

function updateBottomNavigation() {
 document.querySelectorAll('.bottom-nav a').forEach(link => {
  const path = new URL(link.href).pathname;
  const selected = path === '/' ? location.pathname === '/' : location.pathname.startsWith(path);
  if (selected) link.setAttribute('aria-current','page'); else link.removeAttribute('aria-current');
 });
}
document.addEventListener('click', event => {
 const drawer = document.getElementById('site-drawer');
 if (event.target.closest('#bottom-menu')) drawer.showModal();
 if (event.target.closest('#close-drawer') || event.target === drawer) drawer.close();
 if (event.target.closest('#site-drawer a')) drawer.close();
});

function shopCards() {
  const data = window.EE_SHOP_LINKS || {};
  document.querySelectorAll('[data-shop-category]').forEach(card => {
    const entry = data[card.dataset.group]?.[card.dataset.shopCategory];
    const url = typeof entry === 'string' ? entry : entry?.url;
    const visible = typeof entry === 'string' ? true : entry?.publiclyVisible;
    const slot = card.querySelector('.shop-action');
    if (slot && visible && /^https:\/\/(www\.)?payhip\.com\//i.test(url || '')) {
      const link = document.createElement('a');
      link.className = 'button';
      link.href = url;
      link.textContent = 'Shop category ↗';
      slot.replaceChildren(link);
    }
  });
}

function renderPage(path) {
  const page = window.EE_PAGES?.[path];
  if (!page) return false;
  document.getElementById('main').innerHTML = page.main;
  document.title = page.title;
  if (page.header) document.querySelector('header').innerHTML = page.header;
  document.body.dataset.area = page.area || 'main';
  menuButton = document.getElementById('menu');
  nav = document.getElementById('nav');
  document.querySelector('meta[name="description"]')?.setAttribute('content', page.description);
  document.querySelector('link[rel="canonical"]')?.setAttribute('href', location.origin + path);
  nav?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  shopCards();
  updateBottomNavigation();
  window.scrollTo(0, 0);
  return true;
}

document.addEventListener('click', event => {
  const link = event.target.closest('a[href]');
  if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const url = new URL(link.href, location.href);
  if (url.origin !== location.origin) return;
  if (!window.EE_PAGES?.[url.pathname] || url.hash) return;
  event.preventDefault();
  if (url.pathname !== location.pathname) history.pushState({}, '', url.pathname);
  renderPage(url.pathname);
});

window.addEventListener('popstate', () => renderPage(location.pathname));
shopCards();

updateBottomNavigation();
