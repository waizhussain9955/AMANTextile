import os
import re

# 1. Create a compact, super sleek vector SVG logo for AMAN Textile (Height 50px)
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

logo_paths = [
    'assets/images/logo.svg',
    'wp-content/images/logo.svg',
    'assets/images/footer-logo.svg',
    'wp-content/images/footer-logo.svg'
]

for lpath in logo_paths:
    os.makedirs(os.path.dirname(lpath), exist_ok=True)
    with open(lpath, 'w', encoding='utf-8') as f:
        f.write(sleek_logo_svg)
    print(f"Updated sleek logo at {lpath}")


# 2. Remove Social Responsibility section block from index.html & homepage.html
def remove_sr_section(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern to match the Social Responsibility section container in index.html
    pattern = r'<\s*div[^>]*class=["\'][^"\']*elementor-element-20fd7e7[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>\s*<\s*/\s*div\s*>'
    cleaned = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

    # Fallback search if elementor ID differs
    if "Social Responsibility" in cleaned:
        cleaned = re.sub(r'<\s*div[^>]*>\s*<\s*h3[^>]*>\s*Social Responsibility\s*<\s*/h3\s*>.*?cert-line\.jpg.*?<\s*/\s*div\s*>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
        # Also clean any remaining blocks containing Social Responsibility heading
        lines = cleaned.split('\n')
        new_lines = []
        skip = False
        for line in lines:
            if "Social Responsibility" in line and "<h3>" in line:
                skip = True
                continue
            if skip and "cert-line" in line:
                skip = False
                continue
            if not skip:
                new_lines.append(line)
        cleaned = '\n'.join(new_lines)

    # Ensure logo image tag has max-height: 40px
    cleaned = re.sub(r'<img\s+src=["\']assets/images/logo\.svg["\'][^>]*>', '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', cleaned)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"Cleaned {filepath}")

remove_sr_section('index.html')
remove_sr_section('homepage.html')

# Also update logo tag styling across all HTML files
html_files = [
    'about-us.html', 'fabric.html', 'basic-apparel.html', 'baby-product.html', 
    'home-textile.html', 'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        html = re.sub(r'<img\s+src=["\']assets/images/logo\.svg["\'][^>]*>', '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', html)
        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated logo sizing in {hfile}")
