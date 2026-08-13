import re

file_path = 'baby-product.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of product-album.html links in baby-product.html
# with a link that has exactly 4 images and the baby-product.jpg banner.
# The original links look like:
# href="product-album.html?title=Baby%20Item%204&images=assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg%2Cassets/images/baby-5.jpg%2Cassets/images/baby-6.jpg%2Cassets/images/baby-7.jpg%2Cassets/images/baby-8.jpg%2Cassets/images/baby-9.jpg%2Cassets/images/baby-10.jpg"

pattern = r'href="product-album\.html\?title=([^&]+)&images=[^"]+"'

# We replace it with:
# href="product-album.html?title=\1&images=assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg&banner=assets/images/baby-product.jpg"

new_href = r'href="product-album.html?title=\1&images=assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg&banner=assets/images/baby-product.jpg"'

new_content, count = re.subn(pattern, new_href, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {count} links in baby-product.html")
