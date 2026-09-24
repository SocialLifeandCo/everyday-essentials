"""Build a GitHub Pages project preview without changing the root-hostable source."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
out = root / 'preview-dist'
base = '/everyday-essentials/'
site_url = 'https://sociallifeandco.github.io/everyday-essentials/'
if out.exists():
    shutil.rmtree(out)
out.mkdir()
for path in root.rglob('*'):
    if not path.is_file() or any(part in {'.git', '.github', 'preview-dist', '__pycache__'} for part in path.parts):
        continue
    if path.suffix not in {'.html', '.css', '.js', '.json', '.svg', '.txt', '.xml'}:
        continue
    relative = path.relative_to(root)
    dest = out / relative
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = path.read_text()
    if path.suffix == '.html':
        content = content.replace('href="/', f'href="{base}').replace('src="/', f'src="{base}')
        content = content.replace('<head>', '<head><meta name="robots" content="noindex,nofollow">', 1)
    elif relative.as_posix() == 'assets/site.js':
        content = content.replace("fetch('/assets/shop-links.json')", f"fetch('{base}assets/shop-links.json')")
    elif relative.as_posix() in {'robots.txt', 'sitemap.xml'}:
        content = content.replace('https://REPLACE_WITH_DOMAIN/', site_url)
    dest.write_text(content)
(out / '.nojekyll').touch()
print(f'Built preview at {out}')
