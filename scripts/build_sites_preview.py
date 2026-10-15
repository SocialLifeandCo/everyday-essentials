"""Build the static Sites preview from the portable Everyday Essentials source."""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
origin = os.environ.get('SITE_ORIGIN', 'https://everyday-essentials-hub-preview.kurvedbeauty.chatgpt.site').rstrip('/')
subprocess.run([sys.executable, str(root / 'build.py')], check=True)
out = root / 'dist'
for name in ('about', 'contact', 'current-clients', 'custom-orders', 'faq', 'services', 'shop', 'assets'):
    shutil.copytree(root / name, out / name, dirs_exist_ok=True)
for name in ('index.html', 'sitemap.xml', 'robots.txt', '_headers'):
    shutil.copy2(root / name, out / name)
pages = {}
for file in out.rglob('index.html'):
    route = '/' if file.parent == out else '/' + str(file.parent.relative_to(out)) + '/'
    doc = file.read_text().replace('https://REPLACE_WITH_DOMAIN', origin)
    doc = doc.replace('<script defer src="/assets/site.js"></script>', '<script defer src="/assets/page-data.js"></script><script defer src="/assets/site.js"></script>')
    doc = re.sub(r'<a([^>]* href="https?://[^"]+"[^>]*)>', lambda match: '<a' + re.sub(r' target="[^"]+"', '', match.group(1)) + ' target="_top">', doc)
    file.write_text(doc)
    pages[route] = {
        'title': re.search(r'<title>(.*?)</title>', doc).group(1),
        'description': re.search(r'<meta name="description" content="(.*?)"', doc).group(1),
        'header': re.search(r'<header>(.*?)</header>', doc, re.S).group(1),
        'area': 'business' if route.startswith('/services/') else 'main',
        'main': re.search(r'<main id="main">(.*?)</main>', doc, re.S).group(1),
    }
for name in ('sitemap.xml', 'robots.txt'):
    file = out / name
    file.write_text(file.read_text().replace('https://REPLACE_WITH_DOMAIN', origin))
links = json.loads((out / 'assets/shop-links.json').read_text())
(out / 'assets/page-data.js').write_text('window.EE_PAGES=' + json.dumps(pages, ensure_ascii=False, separators=(',', ':')) + ';\nwindow.EE_SHOP_LINKS=' + json.dumps(links, ensure_ascii=False, separators=(',', ':')) + ';\n')
assert len(pages) == 18, f'Expected 18 pages, got {len(pages)}'
print(f'Built {len(pages)} pages for Sites')
