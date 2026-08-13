import re
import urllib.parse

file_path = 'baby-product.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find each product block:
# <div class="img-wrapper">
# 	<img class="img-fluid img-thumbnail" src="assets/images/baby-2.jpg" ...>
# 	...
# </div>
# <a href="product-album.html?..." ...>BATHROBE SET</a>

pattern = r'(<img[^>]+src="([^"]+)"[^>]*>.*?<a href=")product-album\.html\?[^"]+("[^>]*>)(.*?)(</a>)'

def replacer(match):
    prefix = match.group(1)
    img_src = match.group(2)
    suffix = match.group(3)
    name = match.group(4).strip()
    
    # URL encode the name for the title parameter
    encoded_title = urllib.parse.quote(name)
    
    # Keep the same 4 images as before for the gallery
    images_param = "assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg"
    
    # The banner will be the thumbnail image
    banner_param = img_src
    
    new_url = f"product-album.html?title={encoded_title}&images={images_param}&banner={banner_param}"
    
    return prefix + new_url + suffix + name + "</a>"

new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {count} links in baby-product.html with dynamic banners and titles")
