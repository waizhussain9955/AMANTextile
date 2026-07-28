import os
import re

# 1. Define standard, perfect header & footer blocks from index.html
standard_header = """<header id="header">
  <div class="container main-menu">
    <div class="row align-items-center justify-content-between d-flex">
      <div id="logo">
        <a href="index.html"><img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" /></a>
      </div>
      <nav id="nav-menu-container">
        <ul class="nav-menu">
          <li><a href="index.html">Home</a></li>
          <li><a href="about-us.html">About Us</a></li>
          <li class="menu-has-children"><a href="#">Products</a>
            <ul>
              <li><a href="fabric.html">Fabrics</a></li>
              <li><a href="basic-apparel.html">Apparel</a></li>
              <li><a href="baby-product.html">Baby Garments</a></li>
              <li><a href="home-textile.html">Home Textile</a></li>
            </ul>
          </li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact-us.html">Contact Us</a></li>
        </ul>
      </nav>
    </div>
  </div>
</header>"""

standard_footer_logo = '<img src="assets/images/footer-logo.svg" style="margin: 0; max-height: 58px; width: auto; display: block;" alt="AMAN Textile" />'

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

# Map page banner background images
page_banner_map = {
    'about-us.html': 'assets/images/about-us.jpg',
    'fabric.html': 'assets/images/1.png',
    'basic-apparel.html': 'assets/images/2.jpg',
    'baby-product.html': 'assets/images/3.jpg',
    'home-textile.html': 'assets/images/5.jpg',
    'gallery.html': 'assets/images/slider-1.jpg',
    'contact-us.html': 'assets/images/slider-3.jpg',
    'manufacturing.html': 'assets/images/slider-5.jpg',
    'knits-woven.html': 'assets/images/1.png',
    'design.html': 'assets/images/2.jpg'
}

for hfile in html_files:
    if not os.path.exists(hfile):
        continue

    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # A. Replace ANY header tag/div with standard_header
    if '<header' in html:
        html = re.sub(r'<\s*header[^>]*>.*?<\s*/\s*header\s*>', standard_header, html, flags=re.DOTALL | re.IGNORECASE)
    else:
        # Inject standard header right after <body> or at top of body
        html = re.sub(r'(<\s*body[^>]*>)', f'\\1\n{standard_header}\n', html, flags=re.IGNORECASE)

    # B. Remove any custom "NE" badge logos or divs that were hardcoded
    html = re.sub(r'<\s*div[^>]*class=["\'][^"\']*brand-logo[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<\s*div[^>]*class=["\'][^"\']*logo-badge[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'EST\.\s*1995', '', html, flags=re.IGNORECASE)

    # C. Replace all logo img tags
    html = re.sub(r'<img\s+src=["\'][^"\']*(?:logo|logo-1|logo-2)\.(?:png|jpg|svg)["\'][^>]*>', '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', html)

    # D. Replace footer logo
    html = re.sub(r'<img\s+src=["\']assets/images/footer-logo\.svg["\'][^>]*>', standard_footer_logo, html)

    # E. Replace Social Responsibility menu links & pages
    html = re.sub(r'<\s*li[^>]*>\s*<\s*a[^>]*href=["\']social-responsibility\.html["\'][^>]*>.*?<\s*/a\s*>\s*<\s*/li\s*>', '', html, flags=re.DOTALL | re.IGNORECASE)

    # F. Un-lazyload images
    def fix_img_tag(match):
        img_tag = match.group(0)
        lazy_match = re.search(r'data-lazy-src=["\']([^"\']+)["\']', img_tag)
        if not lazy_match:
            lazy_match = re.search(r'data-src=["\']([^"\']+)["\']', img_tag)
        if lazy_match:
            real_src = lazy_match.group(1)
            img_tag = re.sub(r'src=["\'][^"\']*["\']', f'src="{real_src}"', img_tag)
        return img_tag

    html = re.sub(r'<\s*img[^>]+>', fix_img_tag, html)

    # G. Fix banner background image for subpage
    if hfile in page_banner_map:
        banner_img = page_banner_map[hfile]
        # Check for first hero section or section with awam-parallax / page-header
        html = re.sub(
            r'(<\s*section[^>]*class=["\'][^"\']*(?:awam-parallax|page-header|hero)[^"\']*["\'][^>]*style=["\'])',
            f'\\1 background-image: url(\'{banner_img}\') !important; background-size: cover !important; background-position: center !important; ',
            html,
            flags=re.IGNORECASE
        )

    # H. FontAwesome 6 & Social Icons
    if 'cdnjs.cloudflare.com/ajax/libs/font-awesome' not in html:
        html = html.replace('</head>', f'{font_awesome_cdn}\n{social_icons_css}\n</head>')
    elif 'social-icons-custom-style' not in html:
        html = html.replace('</head>', f'{social_icons_css}\n</head>')

    pattern = r'<\s*div[^>]*class=["\'][^"\']*elementor-social-icons-wrapper[^"\']*["\'][^>]*>.*?<\s*/\s*div\s*>'
    html = re.sub(pattern, new_social_html, html, flags=re.DOTALL | re.IGNORECASE)

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Audited & Updated {hfile}")

print("FULL SITE AUDIT AND FIX COMPLETED SUCCESSFULLY!")
