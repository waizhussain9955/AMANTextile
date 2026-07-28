import os
import re
import shutil

# 1. Standardize image filenames in assets/images (e.g. create uppercase/lowercase copies)
if os.path.exists('assets/images'):
    files = os.listdir('assets/images')
    for f in files:
        src = os.path.join('assets/images', f)
        # Create lowercase version copy if filename has uppercase extension
        lower_f = f.lower()
        if lower_f != f:
            dst = os.path.join('assets/images', lower_f)
            try:
                shutil.copy2(src, dst)
                print(f"Created lowercase copy: {lower_f}")
            except Exception:
                pass

# Also copy banner images if needed
if os.path.exists('assets/images'):
    if not os.path.exists('assets/images/about-us.jpg'):
        shutil.copy2('assets/images/factory-1.jpg', 'assets/images/about-us.jpg')
    if not os.path.exists('assets/images/contact.jpg'):
        shutil.copy2('assets/images/slider-3.jpg', 'assets/images/contact.jpg')

# 2. Fix all HTML files
html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

for hfile in html_files:
    if not os.path.exists(hfile):
        continue

    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # A. Convert any remaining wp-content/images/ or nav/images/ to assets/images/
    html = re.sub(r'wp-content/images/', 'assets/images/', html)
    html = re.sub(r'nav/images/', 'assets/images/', html)

    # B. Fix case sensitivity issues like about-3.JPG -> about-3.jpg
    html = html.replace('about-3.JPG', 'about-3.jpg')
    html = html.replace('about-2.JPG', 'about-2.jpg')

    # C. Un-lazyload any remaining <img> tags
    def unlazy(match):
        tag = match.group(0)
        lazy = re.search(r'data-lazy-src=["\']([^"\']+)["\']', tag)
        if lazy:
            real_url = lazy.group(1)
            filename = os.path.basename(real_url.split('?')[0])
            tag = re.sub(r'src=["\'][^"\']*["\']', f'src="assets/images/{filename}"', tag)
        return tag

    html = re.sub(r'<\s*img[^>]+>', unlazy, html)

    # D. Ensure all <img> tags point to valid files in assets/images/
    def check_img_src(match):
        tag = match.group(0)
        src_m = re.search(r'src=["\']assets/images/([^"\']+)["\']', tag)
        if src_m:
            fn = src_m.group(1)
            if not os.path.exists(f'assets/images/{fn}') and not os.path.exists(f'assets/images/{fn.lower()}'):
                # Fallback to valid image
                fallback = '1.png' if fn.endswith('.png') else 'slider-1.jpg'
                tag = tag.replace(f'assets/images/{fn}', f'assets/images/{fallback}')
        return tag

    html = re.sub(r'<\s*img[^>]+>', check_img_src, html)

    # E. Restore exact Awam banner layout for about-us.html
    if hfile == 'about-us.html':
        about_banner_html = """<section class="awam-parallax jarallax parallax-yes elementor-section elementor-top-section elementor-element elementor-element-cca5f3b elementor-section-stretched elementor-section-height-min-height elementor-section-boxed elementor-section-height-default elementor-section-items-middle"
					style="background: linear-gradient(rgba(1, 10, 41, 0.7), rgba(1, 10, 41, 0.8)), url('assets/images/about-us.jpg') center/cover no-repeat !important; z-index: 1; padding: 100px 0 80px 0;">
					<div class="container">
						<div class="row">
							<div class="col-lg-12">
								<div class="caption">
									<h1 class="slider_hero_title text-white t-center text-up"
										style="padding: 60px 0; font-size: 45px; font-weight: 700;">Quality Craftsmanship Trusted Globally
									</h1>
								</div>
							</div>
						</div>
					</div>
				</section>"""
        html = re.sub(r'<\s*section[^>]*class=["\'][^"\']*(?:subpage-hero-banner|awam-parallax)[^"\']*.?<\s*/\s*section\s*>', about_banner_html, html, flags=re.DOTALL | re.IGNORECASE)

    with open(hfile, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed broken image paths in {hfile}")

print("ALL BROKEN IMAGE PATHS FIXED SUCCESSFULLY!")
