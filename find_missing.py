from bs4 import BeautifulSoup

files = ['gallery.html', 'baby-product.html', 'home-textile.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        images = soup.find_all('img', class_='img-thumbnail')
        print(f"--- {f} ---")
        for img in images:
            parent = img.parent
            if parent.name == 'figure':
                parent = parent.parent
            if parent.name == 'div' and 'img-wrapper' in parent.get('class', []):
                grandparent = parent.parent
                if grandparent.name == 'div' and 'product-gallery' in grandparent.get('class', []):
                    pass
                else:
                    print(f"Missing product-gallery: {img.get('src')}")
            else:
                print(f"Missing img-wrapper/product-gallery: {img.get('src')} - parent is {parent.name} with class {parent.get('class', [])}")

