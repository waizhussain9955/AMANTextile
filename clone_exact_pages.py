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

os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/css', exist_ok=True)
os.makedirs('assets/js', exist_ok=True)

# Helper function to download remote asset if missing
def download_asset(rel_path):
    if not rel_path or rel_path.startswith(('data:', 'http:', 'https:', '#', 'javascript:')):
        return
    filename = os.path.basename(rel_path.split('?')[0])
    if not filename:
        return
    local_path = os.path.join('assets/images', filename)
    if not os.path.exists(local_path):
        remote_url = base_url + rel_path.lstrip('/')
        try:
            req = urllib.request.Request(remote_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                with open(local_path, 'wb') as f:
                    f.write(data)
                print(f"Downloaded missing asset: {filename}")
        except Exception as e:
            print(f"Asset fetch skipped ({filename}): {e}")

# 1. Process each page
for p in pages:
    url = base_url + p
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw_html = resp.read().decode('utf-8', errors='ignore')
            print(f"Fetched raw HTML for {p} ({len(raw_html)} bytes)")
    except Exception as e:
        print(f"Error fetching {p}: {e}")
        continue

    # Find all image URLs in raw_html and attempt download
    img_urls = re.findall(r'(?:src|href|data-lazy-src|data-awam-background)=["\']([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)[^"\']*)["\']', raw_html, re.IGNORECASE)
    for iu in img_urls:
        download_asset(iu)

    # Convert asset paths to clean assets/ structure
    html = raw_html

    # Replace WP Rocket lazyload placeholders with real images
    def fix_lazy(match):
        tag = match.group(0)
        lazy = re.search(r'data-lazy-src=["\']([^"\']+)["\']', tag)
        if lazy:
            real_url = lazy.group(1)
            filename = os.path.basename(real_url.split('?')[0])
            tag = re.sub(r'src=["\'][^"\']*["\']', f'src="assets/images/{filename}"', tag)
        return tag

    html = re.sub(r'<\s*img[^>]+>', fix_lazy, html)

    # Rewrite CSS, JS, Image paths
    html = re.sub(r'(?:href|src|data-lazy-src)=["\'][^"\']*/([^"\']+\.css(?:\?[^"\']*)?)["\']', r'href="assets/css/\1"', html)
    html = re.sub(r'src=["\'][^"\']*/([^"\']+\.js(?:\?[^"\']*)?)["\']', r'src="assets/js/\1"', html)
    html = re.sub(r'src=["\'][^"\']*/([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^"\']*)?)["\']', r'src="assets/images/\1"', html)
    html = re.sub(r'data-awam-background=["\'][^"\']*/([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp))["\']', r'data-awam-background="assets/images/\1"', html)

    # Re-map parallax data imgsrc
    def fix_parallax_img(match):
        img_val = match.group(1)
        filename = os.path.basename(img_val)
        return f'imgsrc&quot;:&quot;assets/images/{filename}&quot;'
    html = re.sub(r'imgsrc&quot;:&quot;([^&"\']+)&quot;', fix_parallax_img, html)

    # Replace branding
    html = re.sub(r'Naeem\s*<br\s*/?>\s*Enterprise', 'AMAN<br>Textile', html, flags=re.IGNORECASE)
    html = re.sub(r'Naeem\s+Enterprise', 'AMAN Textile', html, flags=re.IGNORECASE)
    html = re.sub(r'Naeem\s+Enterprises', 'AMAN Textiles', html, flags=re.IGNORECASE)
    html = re.sub(r'NaeemEnterprise', 'AMAN Textile', html, flags=re.IGNORECASE)
    html = re.sub(r'naeementerprise\.com', 'amantextile.com', html, flags=re.IGNORECASE)

    # Replace logo img tags with logo.svg
    html = re.sub(r'<img\s+src=["\']assets/images/(?:logo|logo-1|logo-2)\.(?:png|jpg|svg)["\'][^>]*>', '<img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" />', html)

    # Replace footer logo
    html = re.sub(r'<img\s+src=["\']assets/images/footer-logo\.(?:png|jpg|svg)["\'][^>]*>', '<img src="assets/images/footer-logo.svg" style="margin: 0; max-height: 58px; width: auto; display: block;" alt="AMAN Textile" />', html)

    # Remove Social Responsibility nav item
    html = re.sub(r'<\s*li[^>]*>\s*<\s*a[^>]*href=["\']social-responsibility\.html["\'][^>]*>.*?<\s*/a\s*>\s*<\s*/li\s*>', '', html, flags=re.DOTALL | re.IGNORECASE)

    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved exact cloned page for {p}")

print("ALL PAGES CLONED AND CONVERTED SUCCESSFULLY!")
