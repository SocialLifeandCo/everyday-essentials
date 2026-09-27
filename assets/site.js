const menuButton = document.getElementById('menu');
const nav = document.getElementById('nav');

menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
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
  document.querySelector('meta[name="description"]')?.setAttribute('content', page.description);
  document.querySelector('link[rel="canonical"]')?.setAttribute('href', location.origin + path);
  nav?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  shopCards();
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
