import os
import re

html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

valid_banners = {
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

    if hfile in valid_banners:
        banner_img = valid_banners[hfile]
        clean_style = f'style="background: linear-gradient(rgba(1, 10, 41, 0.75), rgba(1, 10, 41, 0.85)), url(\'{banner_img}\') center/cover no-repeat !important; z-index: 1; padding: 120px 0 80px 0; min-height: 380px;"'
        
        # Replace the entire style="..." on the hero section elementor-element-cca5f3b / hero section
        html = re.sub(
            r'<\s*section[^>]*elementor-element-cca5f3b[^>]*>',
            f'<section class="awam-parallax jarallax parallax-yes elementor-section elementor-top-section elementor-element elementor-element-cca5f3b elementor-section-stretched elementor-section-height-min-height elementor-section-boxed elementor-section-height-default elementor-section-items-middle" {clean_style}>',
            html,
            flags=re.IGNORECASE
        )

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Cleaned style attribute in {hfile}")

print("Hero style attributes cleaned successfully!")
