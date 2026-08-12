import re

baby_names = {
    'baby-2.jpg': 'BATHROBE SET',
    'baby-4.jpg': 'BABY BATHROBE',
    'baby-5.jpg': 'FLUNNEL RECIEVING BLANKETS',
    'baby-7.jpg': 'BABY BURP',
    'baby-8.jpg': 'BABY BIPS'
}

def add_names_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The structure is:
    # <div class="product-gallery">
    #     <div class="img-wrapper">
    #         <img ... src="assets/images/baby-X.jpg" ...>
    #         ...
    #     </div>
    #     <a ... class="product-title" ...>...</a>
    # </div>
    
    # We will use regex to find the product-gallery div containing baby images,
    # and insert the <p> tag before the closing </div> of product-gallery.
    
    def replacer(match):
        full_match = match.group(0)
        img_src = match.group(1)
        
        # Get filename from src
        filename = img_src.split('/')[-1]
        
        name = baby_names.get(filename, '&nbsp;')
        
        # Check if we already added it
        if 'class="product-subtitle"' in full_match:
            return full_match
            
        p_tag = f'\n\t\t\t\t\t\t\t\t\t<p class="product-subtitle" style="color: white; text-align: center; margin-top: 15px; font-weight: 600; font-size: 14px; text-transform: uppercase;">{name}</p>'
        
        # Insert right before the last </div>
        # But wait, regex might match too much. Let's find the </a> instead.
        # Actually, let's just do a string replacement if possible.
        pass
        
    # Better approach: parse with BeautifulSoup or use a very targeted regex.
    # We can match:
    # ( <img[^>]+src="assets/images/baby-\d+\.jpg"[^>]*> .*? <a[^>]+class="product-title"[^>]*>.*?</a> )
    # using re.DOTALL and insert the <p> after the </a>
    
    pattern = r'(<img[^>]+src="assets/images/(baby-\d+\.jpg)"[^>]*>.*?<a[^>]+class="product-title"[^>]*>.*?</a>)'
    
    def replacer2(match):
        content_block = match.group(1)
        filename = match.group(2)
        name = baby_names.get(filename, '&nbsp;')
        
        if 'class="product-subtitle"' in content_block:
            return content_block
            
        p_tag = f'\n\t\t\t\t\t\t\t\t\t<p class="product-subtitle" style="color: white; text-align: center; margin-top: 5px; font-weight: 600; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">{name}</p>'
        
        return content_block + p_tag

    new_content = re.sub(pattern, replacer2, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

add_names_to_html('baby-product.html')
add_names_to_html('gallery.html')
