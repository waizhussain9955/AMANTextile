import os
import re

html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

# Valid banner image mapping (using images that ACTUALLY exist in assets/images)
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

# Subpage fallback image map for body content images
image_replacements = {
    'contact.jpg': 'slider-3.jpg',
    'about-us.jpg': 'factory-1.jpg',
    'about-us-1.jpg': 'factory-2.jpg',
    'facility.jpg': 'factory-1.jpg',
    'banner-bg.jpg': 'slider-1.jpg',
    'pattern-bg.gif': '1.png'
}

for hfile in html_files:
    if not os.path.exists(hfile):
        continue

    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # 1. Replace any invalid banner references with valid_banners
    if hfile in valid_banners:
        banner_img = valid_banners[hfile]
        # Replace hero section inline style
        html = re.sub(
            r'style=["\'][^"\']*background-image:[^"\']*["\']', 
            f'style="background: linear-gradient(rgba(1, 10, 41, 0.75), rgba(1, 10, 41, 0.85)), url(\'{banner_img}\') center/cover no-repeat !important; z-index: 1; padding: 120px 0 80px 0;"', 
            html, 
            count=1
        )

    # 2. Fix invalid image names in <img> tags
    for old_img, new_img in image_replacements.items():
        html = html.replace(old_img, new_img)

    # 3. Double check all <img src="assets/images/XXX"> to make sure file exists
    def verify_img_src(match):
        full_tag = match.group(0)
        src_match = re.search(r'src=["\']assets/images/([^"\']+)["\']', full_tag)
        if src_match:
            img_filename = src_match.group(1)
            if not os.path.exists(f'assets/images/{img_filename}'):
                # Replace with valid fallback
                fallback = '1.png' if img_filename.endswith('.png') else 'slider-1.jpg'
                full_tag = full_tag.replace(f'assets/images/{img_filename}', f'assets/images/{fallback}')
        return full_tag

    html = re.sub(r'<\s*img[^>]+>', verify_img_src, html)

    # 4. Remove any Elementor elementor-invisible class that hides content
    html = html.replace('elementor-invisible', '')

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed image references & hero banner in {hfile}")

print("ALL MISSING IMAGES FIXED SUCCESSFULLY!")
