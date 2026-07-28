import os
import re

html_files = [
    'homepage.html', 'index.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'social-responsibility.html', 'contact-us.html', 
    'manufacturing.html', 'knits-woven.html', 'design.html'
]

if os.path.exists('homepage.html'):
    with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

replacements = [
    (r'Naeem\s*<br\s*/?>\s*Enterprise', 'AMAN<br>Textile'),
    (r'Naeem\s+Enterprise', 'AMAN Textile'),
    (r'Naeem\s+Enterprises', 'AMAN Textiles'),
    (r'NaeemEnterprise', 'AMAN Textile'),
    (r'naeementerprise\.com', 'amantextile.com'),
    (r'info@naeementerprise\.com', 'info@amantextile.com'),
    (r'sales@naeementerprise\.com', 'sales@amantextile.com'),
]

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

        for pattern, repl in replacements:
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"Updated branding in {hfile}")
