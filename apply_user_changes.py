import os
import re
import shutil

# 1. Update logo files
new_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 120" width="450" height="120">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#D4AF37" />
    </linearGradient>
  </defs>
  <g transform="translate(10, 10)">
    <path d="M 45 10 L 10 90 L 28 90 L 37 68 L 73 68 L 82 90 L 100 90 Z M 55 26 L 67 54 L 43 54 Z" fill="url(#goldGrad)" />
    <path d="M 25 24 H 85 V 36 H 61 V 90 H 49 V 36 H 25 Z" fill="#FFFFFF" opacity="0.9" />
  </g>
  <text x="125" y="58" font-family="'Poppins', sans-serif" font-weight="800" font-size="34" fill="#FFFFFF" letter-spacing="3">AMAN</text>
  <text x="125" y="88" font-family="'Quicksand', sans-serif" font-weight="600" font-size="16" fill="#D4AF37" letter-spacing="7">TEXTILE</text>
</svg>"""

logo_paths = [
    'assets/images/logo.svg',
    'wp-content/images/logo.svg',
    'assets/images/footer-logo.svg',
    'wp-content/images/footer-logo.svg'
]

for lpath in logo_paths:
    os.makedirs(os.path.dirname(lpath), exist_ok=True)
    with open(lpath, 'w', encoding='utf-8') as f:
        f.write(new_logo_svg)
    print(f"Updated logo SVG at {lpath}")

# 2. Remove Social Responsibility links across all HTML files
html_files = [
    'homepage.html', 'index.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'social-responsibility.html', 'contact-us.html', 
    'manufacturing.html', 'knits-woven.html', 'design.html'
]

sr_link_patterns = [
    r'<\s*li[^>]*>\s*<\s*a[^>]*href=["\']social-responsibility\.html["\'][^>]*>.*?<\s*/a\s*>\s*<\s*/li\s*>',
    r'<\s*a[^>]*href=["\']social-responsibility\.html["\'][^>]*>.*?<\s*/a\s*>'
]

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        for pattern in sr_link_patterns:
            html = re.sub(pattern, '', html, flags=re.IGNORECASE | re.DOTALL)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Removed Social Responsibility links from {hfile}")

# Delete social-responsibility.html if present
if os.path.exists('social-responsibility.html'):
    os.remove('social-responsibility.html')
    print("Deleted social-responsibility.html file")
