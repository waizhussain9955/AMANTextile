import re

baby_names = {
    'baby-2.jpg': 'BATHROBE SET',
    'baby-4.jpg': 'BABY BATHROBE',
    'baby-5.jpg': 'FLUNNEL RECIEVING BLANKETS',
    'baby-7.jpg': 'BABY BURP',
    'baby-8.jpg': 'BABY BIPS'
}

def update_buttons(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove the `<p class="product-subtitle">...` lines
    content = re.sub(r'\n\s*<p class="product-subtitle"[^>]*>.*?</p>', '', content)

    # Step 2: Replace button text and hover text based on image src
    # The structure:
    # <div class="img-wrapper">
    #     <img class="img-fluid img-thumbnail" src="assets/images/baby-2.jpg" alt="...">
    #     <div class="hover-overlay">
    #         <h4 class="overlay-category">Baby Item</h4>
    #     </div>
    # </div>
    # <a href="..." title="..." class="product-title" ...>Baby Item 2</a>
    
    # We can search for the whole block and replace the texts.
    pattern = r'(<img[^>]+src="assets/images/(baby-\d+\.jpg)"[^>]*>.*?<h4 class="overlay-category">)(.*?)(</h4>.*?<a[^>]+class="product-title"[^>]*>)(.*?)(</a>)'
    
    def replacer(match):
        img_tag_to_h4 = match.group(1)
        filename = match.group(2)
        old_h4 = match.group(3)
        h4_to_a = match.group(4)
        old_a = match.group(5)
        a_close = match.group(6)
        
        new_name = baby_names.get(filename, None)
        
        if new_name:
            return f"{img_tag_to_h4}{new_name}{h4_to_a}{new_name}{a_close}"
        else:
            return match.group(0)

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

update_buttons('baby-product.html')
update_buttons('gallery.html')
