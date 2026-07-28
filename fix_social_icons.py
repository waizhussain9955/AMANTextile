import os
import re

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

        # Inject FontAwesome 6 CDN if missing
        if 'cdnjs.cloudflare.com/ajax/libs/font-awesome' not in html:
            html = html.replace('</head>', f'{font_awesome_cdn}\n{social_icons_css}\n</head>')
        elif 'social-icons-custom-style' not in html:
            html = html.replace('</head>', f'{social_icons_css}\n</head>')

        # Replace social icons wrapper HTML
        pattern = r'<\s*div[^>]*class=["\'][^"\']*elementor-social-icons-wrapper[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>'
        html = re.sub(pattern, new_social_html, html, flags=re.DOTALL | re.IGNORECASE)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed social icons in {hfile}")
