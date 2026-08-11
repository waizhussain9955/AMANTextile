import re

files = ['basic-apparel.html', 'baby-product.html', 'home-textile.html', 'gallery.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # count occurrences of class="product-gallery"
        pg_count = content.count('class="product-gallery"')
        
        # count occurrences of class="product-title"
        pt_count = content.count('class="product-title"')
        
        # count occurrences of img-thumbnail
        img_count = content.count('img-thumbnail')
        
        print(f"{f}:")
        print(f"  img-thumbnail count: {img_count}")
        print(f"  product-gallery count: {pg_count}")
        print(f"  product-title count: {pt_count}")
        print()
