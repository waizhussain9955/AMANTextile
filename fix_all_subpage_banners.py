import os
import shutil
import re

# 1. Ensure any banners in wp-content/images are copied to assets/images/
if os.path.exists('wp-content/images'):
    for root, dirs, files in os.walk('wp-content/images'):
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join('assets/images', file)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            try:
                shutil.copy2(src, dst)
            except Exception:
                pass

print("Copied all wp-content images to assets/images")

# 2. Clean all HTML files
html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # Replace any remaining wp-content/images or nav/ image paths to assets/images/
        html = re.sub(r'wp-content/images/banner/', 'assets/images/', html)
        html = re.sub(r'wp-content/images/', 'assets/images/', html)
        html = re.sub(r'nav/images/', 'assets/images/', html)

        # Fix duplicate style/alt attributes on logo tags
        html = re.sub(
            r'<img\s+src=["\']assets/images/logo\.svg["\'][^>]*>', 
            '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', 
            html
        )

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Cleaned banner & image paths in {hfile}")
