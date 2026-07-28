import os
import re

html_files = [
    'homepage.html', 'index.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'social-responsibility.html', 'contact-us.html', 
    'manufacturing.html', 'knits-woven.html', 'design.html'
]

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = re.sub(r'href=["\']nav/([^"\']+\.css(?:\?[^"\']*)?)["\']', r'href="assets/css/\1"', html)
        html = re.sub(r'src=["\']nav/([^"\']+\.js(?:\?[^"\']*)?)["\']', r'src="assets/js/\1"', html)
        html = re.sub(r'src=["\']wp-content/images/logo\.svg["\']', r'src="assets/images/logo.svg"', html)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Cleaned nav links in {hfile}")
