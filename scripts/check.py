from pathlib import Path
from html.parser import HTMLParser
import json,subprocess,sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/"build.py")],check=True)
class Check(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in d:self.ids.add(d['id'])
  if tag=='a':self.links.append(d.get('href',''))
pages=[p for p in root.rglob('index.html') if 'preview-dist' not in p.parts]
assert len(pages)==8
for page in pages:
 c=Check();c.feed(page.read_text());assert c.h1==1,(page,c.h1)
 for link in c.links:
  if link.startswith('/'):
   path,_,frag=link.partition('#')
   target=root/path.lstrip('/')/'index.html'
   assert target.is_file(),(page,link)
   if frag:
    other=Check();other.feed(target.read_text());assert frag in other.ids,(page,link)
cfg=json.loads((root/'assets/shop-links.json').read_text())
assert len(cfg['categories'])==12 and len(cfg['digital'])==9
assert sum(bool(v.get('publiclyVisible')) for v in cfg['categories'].values() if isinstance(v,dict))==5
assert len(cfg['etsyStoreSetup'])==3
services=(root/'services/index.html').read_text()
for url in cfg['etsyStoreSetup'].values():
 assert url not in services, 'Owner-only package links must stay off the public page'
for package in cfg['etsyStoreSetup']:
 assert package in services
assert services.count('https://everydayessentials4-orders.webflow.io/website-inquiry') >= 3
print('PASS: eight pages, one H1 each, internal navigation and anchor targets, five active categories and safe pending states.')
