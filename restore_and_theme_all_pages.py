import urllib.request
import re
import os

base_url = "http://www.naeementerprise.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

pages = [
    'about-us.html', 'fabric.html', 'basic-apparel.html', 'baby-product.html', 
    'home-textile.html', 'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

# 1. Download original Awam Elementor theme files for all pages
for p in pages:
    url = base_url + p
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Downloaded original theme page: {p} ({len(content)} bytes)")
    except Exception as e:
        print(f"Failed downloading {p}: {e}")

# 2. Clean asset links to assets/ directory across all downloaded files
font_awesome_cdn = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
social_icons_css = """
<style id="social-icons-custom-style">
  .elementor-social-icons-wrapper {
    display: flex !important;
    gap: 12px !important;
    align-items: center !important;
    margin-top: 10px !important;
  }
  .elementor-social-icon {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 42px !important;
    height: 42px !important;
    border-radius: 50% !important;
    background: #010a29 !important;
    color: #ffffff !important;
    font-size: 18px !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
  }
  .elementor-social-icon i {
    color: #ffffff !important;
    font-size: 18px !important;
  }
  .elementor-social-icon:hover {
    background: #D4AF37 !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 6px 15px rgba(212,175,55,0.4) !important;
  }
  .elementor-social-icon:hover i {
    color: #010a29 !important;
  }
</style>
"""

new_social_html = """<div class="elementor-social-icons-wrapper elementor-grid">
  <span class="elementor-grid-item">
    <a class="elementor-icon elementor-social-icon" href="https://www.linkedin.com/company/amantextile" target="_blank" title="LinkedIn">
      <i class="fa-brands fa-linkedin-in"></i>
    </a>
  </span>
  <span class="elementor-grid-item">
    <a class="elementor-icon elementor-social-icon" href="https://www.instagram.com/amantextile" target="_blank" title="Instagram">
      <i class="fa-brands fa-instagram"></i>
    </a>
  </span>
  <span class="elementor-grid-item">
    <a class="elementor-icon elementor-social-icon" href="https://www.facebook.com/amantextile" target="_blank" title="Facebook">
      <i class="fa-brands fa-facebook-f"></i>
    </a>
  </span>
  <span class="elementor-grid-item">
    <a class="elementor-icon elementor-social-icon" href="https://twitter.com/amantextile" target="_blank" title="Twitter">
      <i class="fa-brands fa-x-twitter"></i>
    </a>
  </span>
  <span class="elementor-grid-item">
    <a class="elementor-icon elementor-social-icon" href="https://wa.me/923008223945" target="_blank" title="WhatsApp">
      <i class="fa-brands fa-whatsapp"></i>
    </a>
  </span>
</div>"""

all_pages = ['index.html', 'homepage.html'] + pages

for p in all_pages:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # Fix CSS / JS / Images asset paths
        html = re.sub(r'href=["\'](?:wp-content|nav|wp-includes)/[^"\']*/([^"\']+\.css(?:\?[^"\']*)?)["\']', r'href="assets/css/\1"', html)
        html = re.sub(r'href=["\']nav/([^"\']+\.css(?:\?[^"\']*)?)["\']', r'href="assets/css/\1"', html)
        html = re.sub(r'src=["\'](?:wp-content|nav|wp-includes)/[^"\']*/([^"\']+\.js(?:\?[^"\']*)?)["\']', r'src="assets/js/\1"', html)
        html = re.sub(r'src=["\']nav/([^"\']+\.js(?:\?[^"\']*)?)["\']', r'src="assets/js/\1"', html)
        html = re.sub(r'src=["\'](?:wp-content|nav|wp-includes)/[^"\']*/([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^"\']*)?)["\']', r'src="assets/images/\1"', html)
        html = re.sub(r'data-awam-background=["\'](?:wp-content|nav|wp-includes)/[^"\']*/([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp))["\']', r'data-awam-background="assets/images/\1"', html)
        html = re.sub(r'href=["\'](?:wp-content|nav|wp-includes)/[^"\']*/([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^"\']*)?)["\']', r'href="assets/images/\1"', html)

        # Branding updates
        html = re.sub(r'Naeem\s*<br\s*/?>\s*Enterprise', 'AMAN<br>Textile', html, flags=re.IGNORECASE)
        html = re.sub(r'Naeem\s+Enterprise', 'AMAN Textile', html, flags=re.IGNORECASE)
        html = re.sub(r'Naeem\s+Enterprises', 'AMAN Textiles', html, flags=re.IGNORECASE)
        html = re.sub(r'NaeemEnterprise', 'AMAN Textile', html, flags=re.IGNORECASE)
        html = re.sub(r'naeementerprise\.com', 'amantextile.com', html, flags=re.IGNORECASE)

        # Remove Social Responsibility menu link
        html = re.sub(r'<\s*li[^>]*>\s*<\s*a[^>]*href=["\']social-responsibility\.html["\'][^>]*>.*?<\s*/a\s*>\s*<\s*/li\s*>', '', html, flags=re.IGNORECASE | re.DOTALL)

        # Update Header Logo tag styling
        html = re.sub(r'<img\s+src=["\']assets/images/logo\.svg["\'][^>]*>', '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', html)

        # Update Footer Logo tag styling
        html = re.sub(r'<img\s+src=["\']assets/images/footer-logo\.svg["\'][^>]*>', '<img src="assets/images/footer-logo.svg" style="margin: 0; max-height: 58px; width: auto; display: block;" alt="AMAN Textile" />', html)
        html = re.sub(r'style=["\']margin:\s*0\s+0\s+0\s+-30px;?["\']', '', html)

        # Need a Custom Quote white text style
        html = re.sub(
            r'(<h2[^>]*class=["\'][^"\']*elementor-heading-title[^"\']*["\'][^>]*>\s*Need a Custom Quote\??)',
            r'<h2 class="elementor-heading-title elementor-size-default" style="color: #ffffff !important; -webkit-text-stroke: none !important; opacity: 1 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.5);">Need a Custom Quote?',
            html,
            flags=re.IGNORECASE
        )

        # FontAwesome 6 & Social Icons
        if 'cdnjs.cloudflare.com/ajax/libs/font-awesome' not in html:
            html = html.replace('</head>', f'{font_awesome_cdn}\n{social_icons_css}\n</head>')
        elif 'social-icons-custom-style' not in html:
            html = html.replace('</head>', f'{social_icons_css}\n</head>')

        pattern = r'<\s*div[^>]*class=["\'][^"\']*elementor-social-icons-wrapper[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>'
        html = re.sub(pattern, new_social_html, html, flags=re.DOTALL | re.IGNORECASE)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Synchronized theme and assets for {p}")

print("All theme pages restored and synchronized successfully!")
