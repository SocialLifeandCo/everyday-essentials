# Everyday Essentials

Production-oriented, dependency-free static website. No product checkout is handled by the site. The exact Payhip category destinations and public-visibility flags are configured in assets/shop-links.json. Empty and pending categories show a non-clickable coming-soon label.

## Preview and checks

From this directory run: python3 -m http.server 4173
Open http://localhost:4173/
Run: python3 scripts/check.py

Do not open the files through file:// because shop links load from JSON over HTTP.

## Sitemap

Home /, Shop /shop/, Custom Orders /custom-orders/, Done-For-You Services /services/, About /about/, Contact /contact/, FAQ & Policies /faq/, Current Clients /current-clients/.

## Deployment

Commit this directory to a GitHub repository. For Cloudflare Pages, select no framework, no build command, and the repository root as output. For Vercel, import as an Other static project with no build command. Confirm clean directory URLs resolve on the chosen host. Connect the domain and enable HTTPS through the host.

Before launch: replace REPLACE_WITH_DOMAIN in HTML, sitemap.xml, and robots.txt with the real domain; add any new verified exact Payhip category links to assets/shop-links.json and set publiclyVisible only once listings are actually public; verify the three website-related Webflow form destinations and test submissions; test the active Custom Order Request form; verify the working Facebook business page URL and add it to the footer; add approved real product photos, valid testimonials if available, business contact details if desired, and customer visibility and purchase readiness of the three Etsy Store Setup products (previous Payhip spec recorded them as Invisible). Review final privacy, refund, fulfillment, and digital product policies. Check Payhip checkout and mobile widths 375, 768, 1024, and 1440 px.

## External links used

Custom orders: https://everydayessentials4-orders.webflow.io/ (Webflow homepage Custom Order Request form; user confirmed this is the order form to use).
Business inquiry: https://everydayessentials4-orders.webflow.io/website-inquiry
Client onboarding: https://everydayessentials4-orders.webflow.io/website-client-onboarding
Client approval: https://everydayessentials4-orders.webflow.io/website-review-approval
Instagram: https://www.instagram.com/everydayessentials_4/
Facebook: omitted until a working page URL is verified.
Payhip Etsy Store Setup packages: Mini Launch https://payhip.com/b/F0wuT ; Store Launch https://payhip.com/b/Fq8uv ; Business Launch https://payhip.com/b/QxYnj . Shop All and five active categories supplied: Digital Products (11), Party & Events (10), Seasonal Products (10), Custom Gifts (2), Business & Branding (1). Four category URLs are configured but their listings are currently empty or nonpublic: Beauty, Memorial Products, Custom Apparel, Done-For-You Etsy Stores. Drinkware, Flags & Banners, Graduation & Prom, and nine digital subcategories still need exact URLs.
# Everyday Essentials

Production-oriented, dependency-free static website. No product checkout is handled by the site. The exact Payhip category destinations and public-visibility flags are configured in assets/shop-links.json. Empty and pending categories show a non-clickable coming-soon label.

## Preview and checks

From this directory run: python3 build.py, then python3 -m http.server 4173
Open http://localhost:4173/
Run: python3 scripts/check.py

Do not open the files through file:// because shop links load from JSON over HTTP.

## Sitemap

Home /, Shop /shop/, Custom Orders /custom-orders/, Done-For-You Services /services/, About /about/, Contact /contact/, FAQ & Policies /faq/, Current Clients /current-clients/.

## Deployment

Commit this directory to a GitHub repository. The HTML committed to this repository is a snapshot; `build.py` is the source of truth. For Cloudflare Pages, select no framework, set build command to `python3 build.py`, and output directory to `.`. For Vercel, configure an equivalent build command. Confirm clean directory URLs resolve on the chosen host. Connect the domain and enable HTTPS through the host. The GitHub Pages project preview uses `scripts/build_preview.py` and carries a noindex tag; use a production build for the final domain.

Before launch: replace REPLACE_WITH_DOMAIN in HTML, sitemap.xml, and robots.txt with the real domain; add any new verified exact Payhip category links to assets/shop-links.json and set publiclyVisible only once listings are actually public; verify the three website-related Webflow form destinations and test submissions; test the active Custom Order Request form; verify the working Facebook business page URL and add it to the footer; add approved real product photos, valid testimonials if available, business contact details if desired, and customer visibility and purchase readiness of the three Etsy Store Setup products. Their public service cards currently route to the Website Inquiry form because the Payhip products are owner-only. Review final privacy, refund, fulfillment, and digital product policies. Check Payhip checkout and mobile widths 375, 768, 1024, and 1440 px.

## External links used

Custom orders: https://everydayessentials4-orders.webflow.io/ (Webflow homepage Custom Order Request form; user confirmed this is the order form to use).
Business inquiry: https://everydayessentials4-orders.webflow.io/website-inquiry
Client onboarding: https://everydayessentials4-orders.webflow.io/website-client-onboarding
Client approval: https://everydayessentials4-orders.webflow.io/website-review-approval
Instagram: https://www.instagram.com/everydayessentials_4/
Facebook: omitted until a working page URL is verified.
Payhip Etsy Store Setup packages: Mini Launch https://payhip.com/b/F0wuT ; Store Launch https://payhip.com/b/Fq8uv ; Business Launch https://payhip.com/b/QxYnj . Shop All and five active categories supplied: Digital Products (11), Party & Events (10), Seasonal Products (10), Custom Gifts (2), Business & Branding (1). Four category URLs are configured but their listings are currently empty or nonpublic: Beauty, Memorial Products, Custom Apparel, Done-For-You Etsy Stores. Drinkware, Flags & Banners, Graduation & Prom, and nine digital subcategories still need exact URLs.
