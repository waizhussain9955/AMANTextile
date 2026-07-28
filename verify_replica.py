import os
import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

links = re.findall(r'href=["\']([^"\']+)["\']', html)
scripts = re.findall(r'src=["\']([^"\']+)["\']', html)

missing = []

for item in links + scripts:
    if item.startswith('http') or item.startswith('//') or item.startswith('#') or item.startswith('data:'):
        continue
    clean = item.split('?')[0].split('#')[0]
    if not clean:
        continue
    if not os.path.exists(clean):
        missing.append(clean)

print(f"Total missing local assets: {len(missing)}")
if missing:
    print("Sample missing:", missing[:10])
