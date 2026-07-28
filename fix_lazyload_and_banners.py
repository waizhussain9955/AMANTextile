import os
import re
import shutil

html_files = [
    'index.html', 'homepage.html', 'about-us.html', 'fabric.html', 
    'basic-apparel.html', 'baby-product.html', 'home-textile.html', 
    'gallery.html', 'contact-us.html', 'manufacturing.html', 
    'knits-woven.html', 'design.html'
]

# Ensure fallback images exist in assets/images
available_images = [f for f in os.listdir('assets/images') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))] if os.path.exists('assets/images') else []
print(f"Available images in assets/images: {len(available_images)}")

default_fallback_img = 'assets/images/slider-1.jpg' if 'slider-1.jpg' in available_images else (f'assets/images/{available_images[0]}' if available_images else 'assets/images/logo.svg')

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 1. Un-lazyload all <img> tags: replace data-lazy-src / data-src into src
        # Case A: src has data:image or dummy svg, data-lazy-src has real url
        def fix_img_tag(match):
            img_tag = match.group(0)
            lazy_match = re.search(r'data-lazy-src=["\']([^"\']+)["\']', img_tag)
            if not lazy_match:
                lazy_match = re.search(r'data-src=["\']([^"\']+)["\']', img_tag)
            
            if lazy_match:
                real_src = lazy_match.group(1)
                # Replace src="..." with real_src
                img_tag = re.sub(r'src=["\'][^"\']*["\']', f'src="{real_src}"', img_tag)
                # If no src was present
                if 'src=' not in img_tag:
                    img_tag = img_tag.replace('<img', f'<img src="{real_src}"')
            return img_tag

        html = re.sub(r'<\s*img[^>]+>', fix_img_tag, html)

        # 2. Fix banner section background images from data-awam-parallax / data-awam-background
        def fix_bg_section(match):
            sec_tag = match.group(0)
            bg_match = re.search(r'data-awam-background=["\']([^"\']+)["\']', sec_tag)
            if not bg_match:
                bg_match = re.search(r'imgsrc&quot;:&quot;([^&"\']+)&quot;', sec_tag)
            if not bg_match:
                bg_match = re.search(r'imgsrc":\s*"([^"\']+)"', sec_tag)

            if bg_match:
                bg_url = bg_match.group(1)
                # Clean path to assets/images
                bg_filename = os.path.basename(bg_url)
                real_bg_path = f'assets/images/{bg_filename}'
                
                # Update inline style to force background-image
                if 'style="' in sec_tag:
                    sec_tag = re.sub(
                        r'style=["\']([^"\']*)["\']', 
                        f'style="\\1; background-image: url(\'{real_bg_path}\') !important; background-size: cover !important; background-position: center !important;"', 
                        sec_tag
                    )
                else:
                    sec_tag = sec_tag.replace('>', f' style="background-image: url(\'{real_bg_path}\') !important; background-size: cover !important; background-position: center !important;">', 1)
            return sec_tag

        html = re.sub(r'<\s*(?:section|div)[^>]+(?:data-awam-parallax|data-awam-background)[^>]*>', fix_bg_section, html)

        # 3. Clean any NOSCRIPT tags wrapping images (which created duplicate broken image icons)
        html = re.sub(r'<\s*noscript\s*>\s*<\s*img[^>]+>\s*<\s*/\s*noscript\s*>', '', html, flags=re.IGNORECASE)

        # 4. Remove any remaining WP Rocket lazyload scripts
        html = re.sub(r'<\s*script[^>]*wprocket[^>]*>.*?<\s*/\s*script\s*>', '', html, flags=re.DOTALL | re.IGNORECASE)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed lazyload & background banners in {hfile}")

print("All pages fixed successfully!")
