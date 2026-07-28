import urllib.request
import re
import os
from urllib.parse import urljoin

base_url = "http://www.naeementerprise.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

html_files = [
    'homepage.html', 'index.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'social-responsibility.html', 'contact-us.html', 
    'manufacturing.html', 'knits-woven.html', 'design.html'
]

all_assets = set()

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        css_files = re.findall(r'href=["\']([^"\']+\.css(?:\?[^"\']*)?)["\']', html)
        js_files = re.findall(r'src=["\']([^"\']+\.js(?:\?[^"\']*)?)["\']', html)
        img_files = re.findall(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^"\']*)?)["\']', html)
        bg_imgs = re.findall(r'data-awam-background=["\']([^"\']+)["\']', html)
        link_imgs = re.findall(r'href=["\']([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^"\']*)?)["\']', html)

        for item in css_files + js_files + img_files + bg_imgs + link_imgs:
            if not item.startswith('http') and not item.startswith('//') and not item.startswith('data:'):
                all_assets.add(item)

print(f"Total unique relative assets found across all pages: {len(all_assets)}")

downloaded = 0
failed = 0

for asset in all_assets:
    clean_path = asset.split('?')[0].split('#')[0]
    if not clean_path:
        continue
    
    full_url = urljoin(base_url, asset)
    local_path = os.path.normpath(os.path.join('.', clean_path))
    
    dirname = os.path.dirname(local_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
        
    try:
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(local_path, 'wb') as out:
            out.write(resp.read())
        downloaded += 1
    except Exception as e:
        failed += 1
        print(f"Failed to download {asset}: {e}")

print(f"Asset Download Summary: Downloaded={downloaded}, Failed={failed}")
