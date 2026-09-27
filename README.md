# Everyday Essentials

A static brand hub for Everyday Essentials. Product browsing and checkout use Payhip; custom orders and business inquiries use the existing Webflow forms. There is no backend or payment processing in this repository.

## Site map

- `/` — home and mobile service/product chooser
- `/shop/` — available Payhip collections and product categories
- `/shop/bundles/` — 40 planned digital bundles, grouped by theme; the existing 255+ bundle has a Payhip link
- `/shop/graduation-bundles/` — currently available individual graduation templates
- `/custom-orders/` — custom product request route
- `/services/` — done-for-you service chooser
- `/services/websites/`, `/services/shopify/`, `/services/etsy/`, `/services/payhip/`, `/services/add-ons/` — packages, pricing, policies
- `/about/`, `/contact/`, `/faq/`, `/current-clients/`

## Develop and preview

Run `python3 build.py` and serve the project root with `python3 -m http.server 4173`. Open `http://localhost:4173/`. GitHub Pages uses `.github/workflows/pages-preview.yml` and `scripts/build_preview.py` for a project-path preview, with search indexing disabled there. The Sites version uses its own `scripts/build_sites_preview.py` in the Sites checkout.

`build.py` generates the HTML, `assets/shop-links.json`, sitemap and robots file. Edit `assets/bundles.json` for bundle descriptions. New Payhip bundle URLs belong in `BUNDLE_LINKS` in `build.py` until a separate link source is introduced; use `PAYHIP_LINK_PENDING` until a listing is published. Pending links render as non-clickable labels. Five public Payhip collections and six individual graduation product links are active; 39 new bundle links are pending. Service inquiries go to the existing Website Inquiry form.

## Production hosting

For Cloudflare Pages, use build command `python3 build.py` and output directory `.`. Before connecting the final domain, replace `REPLACE_WITH_DOMAIN` in the generated canonical URLs, sitemap and robots file with the actual production domain; ideally configure that through a build setting. Verify direct loading of every route, Webflow form submissions, Payhip checkout, and mobile interactions on the chosen host. Add the 39 bundle Payhip URLs as those listings become public. The present ChatGPT Sites publication is an interim public preview and does not deploy from this GitHub repository.
