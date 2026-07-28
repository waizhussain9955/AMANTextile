import os
import re

# 1. Update footer logo SVG with bolder typography & high visibility (ViewBox 320 x 60)
footer_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 60" width="320" height="60">
  <defs>
    <linearGradient id="footerGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#112b82" />
      <stop offset="100%" stop-color="#D4AF37" />
    </linearGradient>
  </defs>
  
  <!-- Monogram Mark 'A' -->
  <g transform="translate(5, 5)">
    <polygon points="24,2 2,46 14,46 19,35 34,35 39,46 51,46" fill="url(#footerGoldGrad)" />
    <polygon points="26,11 31,25 21,25" fill="#FFFFFF" />
    <circle cx="26" cy="22" r="3" fill="#D4AF37" />
  </g>

  <!-- High Contrast Brand Name (Dark Navy for Light Footer) -->
  <text x="65" y="34" font-family="'Poppins', 'Inter', sans-serif" font-weight="800" font-size="26" fill="#010a29" letter-spacing="1.5">AMAN</text>
  <text x="65" y="50" font-family="'Quicksand', 'Inter', sans-serif" font-weight="700" font-size="12" fill="#D4AF37" letter-spacing="5">TEXTILE</text>
</svg>"""

footer_paths = [
    'assets/images/footer-logo.svg',
    'wp-content/images/footer-logo.svg'
]

for fpath in footer_paths:
    os.makedirs(os.path.dirname(fpath), exist_ok=True)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(footer_logo_svg)
    print(f"Updated footer logo SVG at {fpath}")

# 2. Fix footer logo tag alignment and size across all HTML files
html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

old_tag_pattern = r'<img\s+src=["\']assets/images/footer-logo\.svg["\'][^>]*>'
new_tag = '<img src="assets/images/footer-logo.svg" style="margin: 0; max-height: 58px; width: auto; display: block;" alt="AMAN Textile" />'

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = re.sub(old_tag_pattern, new_tag, html, flags=re.IGNORECASE)
        # Also clean any negative margin inline styling inside elementor-heading-title container
        html = re.sub(r'style=["\']margin:\s*0\s+0\s+0\s+-30px;?["\']', '', html)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed footer logo alignment in {hfile}")
