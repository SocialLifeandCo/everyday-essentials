# Everyday Essentials

Static brand hub for products and done-for-you services. Product checkout is handled by Payhip; custom orders and service inquiries use the linked Webflow forms. `build.py` and `visibility.py` are the source of truth. The generated HTML is checked into the project for hosts that serve static files directly.

## Preview and checks

Run `python3 scripts/build_sites_preview.py` to generate the Sites-ready `dist/` folder. Run `python3 scripts/check.py` for 18-page navigation, SEO-tag, anchor, image-alt and pending-link checks. Run `node --check assets/site.js` for the menu and page-navigation script. Serve the output over HTTP, not `file://`.

## Routes

`/`, `/shop/`, `/shop/digital/`, `/shop/bundles/`, `/shop/graduation-bundles/`, `/custom-orders/`, `/services/`, `/services/websites/`, `/services/seo/`, `/services/shopify/`, `/services/etsy/`, `/services/payhip/`, `/services/tax-credit/`, `/services/add-ons/`, `/about/`, `/contact/`, `/faq/`, `/current-clients/`.

## Link configuration

`build.py` centralizes the Payhip category/product URLs, the business-service page URLs, Webflow forms and social links. It writes `assets/shop-links.json` and `assets/bundles.json`. Do not replace pending bundle and category values with guessed links; cards remain non-clickable until an exact public Payhip URL is confirmed. The $99 Google + AI Visibility Audit uses `https://payhip.com/b/2FdZQ`, and the four fixed-price website choices use `https://payhip.com/b/DR2zv`.

## Deployment

The current public Sites address is `https://everyday-essentials-hub-preview.kurvedbeauty.chatgpt.site/`. To deploy to another static host, set `SITE_ORIGIN` to the final HTTPS domain and run `python3 build.py`; this generates canonical URLs, sitemap and robots rules for that domain. Configure the host to serve directory index files at clean paths. The Sites workflow uses `scripts/build_sites_preview.py` and publishes `dist/`.

Before connecting a final domain, confirm the domain and DNS ownership, test Webflow form delivery and a real Payhip purchase/delivery with an authorized transaction, review policies, and replace any still-pending product/bundle links only after their public listings exist. Monthly visibility checkout is not yet available on Payhip; the site directs interested visitors to inquiry. Do not represent a pre-checkout page inspection as a successful payment or delivered inquiry.

## GitHub Pages preview

The repository retains `.github/workflows/pages-preview.yml`. It runs `python3 scripts/build_preview.py` and publishes `preview-dist/` under `/everyday-essentials/` with search indexing disabled. The public Sites publication is maintained separately.
