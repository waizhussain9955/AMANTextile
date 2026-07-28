import os
import re

# 1. Create dark-text footer logo for white/light backgrounds
dark_footer_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 50" width="280" height="50">
  <defs>
    <linearGradient id="goldGradFooter" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#112b82" />
      <stop offset="100%" stop-color="#D4AF37" />
    </linearGradient>
  </defs>
  
  <!-- Monogram Mark 'A' -->
  <g transform="translate(5, 5)">
    <polygon points="20,2 2,38 12,38 16,29 28,29 32,38 42,38" fill="url(#goldGradFooter)" />
    <polygon points="22,9 26,21 18,21" fill="#FFFFFF" />
    <circle cx="22" cy="18" r="2.5" fill="#D4AF37" />
  </g>

  <!-- Clean Brand Name (Dark Navy for White Background) -->
  <text x="55" y="28" font-family="'Poppins', 'Inter', sans-serif" font-weight="800" font-size="22" fill="#010a29" letter-spacing="1.5">AMAN</text>
  <text x="55" y="42" font-family="'Quicksand', 'Inter', sans-serif" font-weight="600" font-size="10" fill="#D4AF37" letter-spacing="4">TEXTILE</text>
</svg>"""

footer_paths = [
    'assets/images/footer-logo.svg',
    'wp-content/images/footer-logo.svg'
]

for fpath in footer_paths:
    os.makedirs(os.path.dirname(fpath), exist_ok=True)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(dark_footer_logo_svg)
    print(f"Updated dark text footer logo SVG at {fpath}")

# 2. Fix "Need a Custom Quote?" visibility across all HTML files
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

        # Fix Need a Custom Quote text visibility
        html = re.sub(
            r'(Need a Custom Quote\??)', 
            r'\1', 
            html, 
            flags=re.IGNORECASE
        )
        
        # Replace heading style for Need a Custom Quote
        html = re.sub(
            r'(<h2[^>]*class=["\'][^"\']*elementor-heading-title[^"\']*["\'][^>]*>\s*Need a Custom Quote\??)',
            r'<h2 class="elementor-heading-title elementor-size-default" style="color: #ffffff !important; -webkit-text-stroke: none !important; opacity: 1 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.5);">Need a Custom Quote?',
            html,
            flags=re.IGNORECASE
        )

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed visibility in {hfile}")
