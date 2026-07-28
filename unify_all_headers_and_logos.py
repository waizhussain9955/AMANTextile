import os
import re

# 1. Clean sleek logo SVG
sleek_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 50" width="280" height="50">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#D4AF37" />
    </linearGradient>
  </defs>
  
  <!-- Monogram Mark 'A' -->
  <g transform="translate(5, 5)">
    <polygon points="20,2 2,38 12,38 16,29 28,29 32,38 42,38" fill="url(#goldGrad)" />
    <polygon points="22,9 26,21 18,21" fill="#010a29" />
    <circle cx="22" cy="18" r="2.5" fill="#D4AF37" />
  </g>

  <!-- Clean Brand Name -->
  <text x="55" y="28" font-family="'Poppins', 'Inter', sans-serif" font-weight="800" font-size="22" fill="#FFFFFF" letter-spacing="1.5">AMAN</text>
  <text x="55" y="42" font-family="'Quicksand', 'Inter', sans-serif" font-weight="600" font-size="10" fill="#D4AF37" letter-spacing="4">TEXTILE</text>
</svg>"""

# Write logo to all possible logo file names so no cached/old PNG image shows "NE"
logo_filenames = [
    'assets/images/logo.svg',
    'assets/images/logo.png',
    'assets/images/logo-1.png',
    'assets/images/logo-2.png',
    'assets/images/logo-dark.png',
    'assets/images/logo-light.png',
    'wp-content/images/logo.svg',
    'wp-content/images/logo.png'
]

for lf in logo_filenames:
    os.makedirs(os.path.dirname(lf), exist_ok=True)
    with open(lf, 'w', encoding='utf-8') as f:
        f.write(sleek_logo_svg)
    print(f"Overwrote logo at {lf}")

# 2. Extract exact header HTML from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

header_match = re.search(r'(<\s*header[^>]*id=["\']header["\'][^>]*>.*?<\s*/\s*header\s*>)', index_html, re.DOTALL | re.IGNORECASE)
if not header_match:
    header_match = re.search(r'(<\s*header[^>]*>.*?<\s*/\s*header\s*>)', index_html, re.DOTALL | re.IGNORECASE)

exact_header_html = header_match.group(1) if header_match else None
print("Extracted exact header from index.html")

# 3. Replace header in all subpages
subpages = [
    'about-us.html', 'fabric.html', 'basic-apparel.html', 'baby-product.html', 
    'home-textile.html', 'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html', 'homepage.html'
]

for sp in subpages:
    if os.path.exists(sp):
        with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Replace any existing header block with exact_header_html from index.html
        if exact_header_html:
            content = re.sub(r'<\s*header[^>]*id=["\']header["\'][^>]*>.*?<\s*/\s*header\s*>', exact_header_html, content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<\s*header[^>]*class=["\'][^"\']*site-header[^"\']*["\'][^>]*>.*?<\s*/\s*header\s*>', exact_header_html, content, flags=re.DOTALL | re.IGNORECASE)

        # Replace any logo img references to assets/images/logo.svg
        content = re.sub(r'src=["\'][^"\']*(?:logo|logo-1|logo-2)\.(?:png|jpg|svg)["\']', 'src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile"', content)

        # Ensure active class is updated for subpage nav
        if sp in content:
            # Add active highlighting if needed
            pass

        with open(sp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Unified header and logo for {sp}")

print("All subpages unified with index.html header and logo!")
