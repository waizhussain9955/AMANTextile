import os
import re

# Comprehensive global CSS fix stylesheet to be injected into <head> of ALL HTML pages
global_fix_css = """
<style id="global-theme-fix-style">
  /* 1. Permanent Preloader & Spinner Removal */
  #preloader, #nt-preloader, div#nt-preloader, .pace {
    display: none !important;
    opacity: 0 !important;
    visibility: hidden !important;
    pointer-events: none !important;
  }

  /* 2. Force Header Visibility & Contrast */
  #header, header#header {
    background: #010a29 !important;
    position: relative !important;
    width: 100% !important;
    z-index: 99999 !important;
    padding: 12px 0 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
  }
  #header .main-menu {
    max-width: 1200px !important;
    margin: 0 auto !important;
  }
  #header a, #header .nav-menu > li > a {
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    padding: 8px 12px !important;
    text-decoration: none !important;
  }
  #header .nav-menu > li > a:hover {
    color: #D4AF37 !important;
  }
  #header .nav-menu ul {
    background: #010a29 !important;
    border: 1px solid rgba(212,175,55,0.4) !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4) !important;
    padding: 10px 0 !important;
  }
  #header .nav-menu ul li a {
    color: #ffffff !important;
    padding: 8px 20px !important;
    display: block !important;
    text-transform: none !important;
  }
  #header .nav-menu ul li a:hover {
    background: rgba(212,175,55,0.2) !important;
    color: #D4AF37 !important;
  }

  /* 3. Force Section & Text Visibility Across All Pages */
  .elementor-invisible, .wow {
    opacity: 1 !important;
    visibility: visible !important;
    animation: none !important;
    transform: none !important;
  }
  body {
    opacity: 1 !important;
    visibility: visible !important;
    overflow-x: hidden !important;
    background-color: #ffffff !important;
  }

  /* 4. Contrast Fix for Dark Blue Sections */
  .dark-bg, [style*="background: #010a29"], [style*="background-color: #010a29"], [style*="background: rgb(1, 10, 41)"], [style*="background-color: rgb(1, 10, 41)"] {
    color: #ffffff !important;
  }
  .dark-bg h1, .dark-bg h2, .dark-bg h3, .dark-bg h4, .dark-bg h5, .dark-bg h6,
  [style*="#010a29"] h1, [style*="#010a29"] h2, [style*="#010a29"] h3, [style*="#010a29"] h4, [style*="#010a29"] h5, [style*="#010a29"] h6,
  [style*="#010a29"] p, [style*="#010a29"] span, [style*="#010a29"] li, [style*="#010a29"] a {
    color: #ffffff !important;
  }
  [style*="#010a29"] li strong, [style*="#010a29"] a strong {
    color: #D4AF37 !important;
  }

  /* 5. Subpage Hero Banners Typography & Height */
  .subpage-hero-banner {
    background-size: cover !important;
    background-position: center !important;
    min-height: 300px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    padding: 60px 20px !important;
  }
  .subpage-hero-banner h1 {
    font-size: 38px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    text-shadow: 0 4px 15px rgba(0,0,0,0.6) !important;
    margin: 0 !important;
  }

  /* 6. Image Display & Container Alignment */
  img {
    max-width: 100% !important;
    height: auto !important;
    display: inline-block !important;
  }
</style>
"""

html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

page_titles = {
    'about-us.html': 'About AMAN Textile',
    'fabric.html': 'Textile Fabrics',
    'basic-apparel.html': 'Basic & Custom Apparel',
    'baby-product.html': 'Baby Garments & Essentials',
    'home-textile.html': 'Home Textile Collections',
    'gallery.html': 'Product Gallery',
    'contact-us.html': 'Contact Us',
    'manufacturing.html': 'Manufacturing Facility',
    'knits-woven.html': 'Knits & Woven Division',
    'design.html': 'Design & Innovation'
}

page_banners = {
    'about-us.html': 'assets/images/factory-1.jpg',
    'fabric.html': 'assets/images/1.png',
    'basic-apparel.html': 'assets/images/2.jpg',
    'baby-product.html': 'assets/images/3.jpg',
    'home-textile.html': 'assets/images/5.jpg',
    'gallery.html': 'assets/images/slider-1.jpg',
    'contact-us.html': 'assets/images/slider-3.jpg',
    'manufacturing.html': 'assets/images/factory-2.jpg',
    'knits-woven.html': 'assets/images/woven.jpg',
    'design.html': 'assets/images/design.jpg'
}

for hfile in html_files:
    if not os.path.exists(hfile):
        continue

    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Inject global_fix_css into <head>
    if 'global-theme-fix-style' in html:
        html = re.sub(r'<\s*style\s+id=["\']global-theme-fix-style["\'].*?<\s*/\s*style\s*>', global_fix_css, html, flags=re.DOTALL | re.IGNORECASE)
    else:
        html = html.replace('</head>', f'{global_fix_css}\n</head>')

    # Fix subpage top hero banner HTML structure
    if hfile in page_titles and hfile in page_banners:
        title = page_titles[hfile]
        banner = page_banners[hfile]
        hero_html = f"""<section class="subpage-hero-banner" style="background: linear-gradient(rgba(1, 10, 41, 0.75), rgba(1, 10, 41, 0.85)), url('{banner}') center/cover no-repeat !important;">
  <div class="container">
    <div class="row">
      <div class="col-md-12 text-center">
        <h1 style="color: #ffffff !important; font-size: 42px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 2px !important;">{title}</h1>
      </div>
    </div>
  </div>
</section>"""
        
        # Replace hero section
        if 'class="subpage-hero-banner"' in html:
            html = re.sub(r'<\s*section[^>]*class=["\'][^"\']*subpage-hero-banner[^"\']*["\'].*?<\s*/\s*section\s*>', hero_html, html, flags=re.DOTALL | re.IGNORECASE)
        elif 'class="awam-parallax' in html:
            html = re.sub(r'<\s*section[^>]*class=["\'][^"\']*awam-parallax[^"\'].*?<\s*/\s*section\s*>', hero_html, html, flags=re.DOTALL | re.IGNORECASE)

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Applied style & contrast fixes to {hfile}")

print("GLOBAL STYLES & CONTRAST FIXES APPLIED TO ALL PAGES!")
