"""Check generated pages, navigation targets and safe pending shop links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / 'build.py')], check=True)

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.links = []
        self.ids = set()
        self.descriptions = []
        self.images = []
        self.title = ''
        self._title = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self._title = True
        if 'id' in data:
            self.ids.add(data['id'])
        if tag == 'a':
            self.links.append(data.get('href', ''))
        if tag == 'img':
            self.images.append(data)
        if tag == 'meta' and data.get('name') == 'description':
            self.descriptions.append(data.get('content'))

    def handle_endtag(self, tag):
        if tag == 'title':
            self._title = False

    def handle_data(self, data):
        if self._title:
            self.title += data

pages = {path: Page() for path in root.rglob('index.html') if 'dist' not in path.parts and 'preview-dist' not in path.parts}
for path, parsed in pages.items():
    parsed.feed(path.read_text())
assert len(pages) == 18, len(pages)
assert len({p.title for p in pages.values()}) == len(pages)
for path, parsed in pages.items():
    assert parsed.h1 == 1 and len(parsed.descriptions) == 1 and parsed.descriptions[0], path
    assert all('alt' in image for image in parsed.images), path
    for href in parsed.links:
        if href.startswith(('https://', 'mailto:', 'tel:')):
            continue
        url = urlsplit(href)
        dest = path if not url.path else root / url.path.lstrip('/') / 'index.html'
        assert dest in pages, (path, href, 'missing page')
        if url.fragment:
            assert unquote(url.fragment) in pages[dest].ids, (path, href, 'missing anchor')

config = json.loads((root / 'assets/shop-links.json').read_text())
assert len(config['bundles']) == 40
assert len(config['graduationTemplates']) == 6
assert (root / 'sitemap.xml').read_text().count('<url>') == len(pages)
assert 'PAYHIP_LINK_PENDING' not in (root / 'shop/bundles/index.html').read_text()
assert '$400' in (root / 'services/websites/index.html').read_text()
assert 'https://payhip.com/b/2FdZQ' in (root / 'services/seo/index.html').read_text()
print('PASS: 18 pages, SEO tags, navigation, anchors, images, package links and pending bundles')
