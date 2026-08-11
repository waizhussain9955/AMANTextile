from bs4 import BeautifulSoup

files = ['baby-product.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        images = soup.find_all('img', class_='img-thumbnail')
        for i, img in enumerate(images):
            print(f"Image {i+1}: src={img.get('src')}")
            parent = img.parent
            print(f"  Parent: {parent.name} class={parent.get('class', [])}")
            grandparent = parent.parent if parent else None
            print(f"  Grandparent: {grandparent.name if grandparent else 'None'} class={grandparent.get('class', []) if grandparent else 'None'}")
            print()
