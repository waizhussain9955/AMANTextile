import re

files_to_update = ['baby-product.html', 'gallery.html']

def remove_unnamed_baby_items(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The pattern will find the entire thumb div.
    # We use a non-greedy match that doesn't cross another thumb div.
    # Pattern: <div class="col-lg-3 col-md-4 col-xs-6 thumb">(?:(?!<div class="col-lg-3).)*?assets/images/baby-(1|3|6|9|10)\.jpg.*?</div>\s*</div>
    # Actually, the closing tags are exactly </div>\s*</div> at the end.
    
    # Let's just do a regex that matches the thumb block.
    # We will use re.finditer to find all thumb blocks, then remove the ones with the target images.
    
    pattern = r'<div class="col-lg-3 col-md-4 col-xs-6 thumb">.*?</div>\s*</div>'
    
    # Wait, the structure inside has nested divs, so .*?</div>\s*</div> might stop too early (e.g. at the end of hover-overlay).
    # Let's split by '<div class="col-lg-3 col-md-4 col-xs-6 thumb">'
    
    parts = content.split('<div class="col-lg-3 col-md-4 col-xs-6 thumb">')
    
    new_parts = [parts[0]] # The first part doesn't start with a thumb div
    
    deleted_count = 0
    for part in parts[1:]:
        # Re-attach the split string
        full_thumb = '<div class="col-lg-3 col-md-4 col-xs-6 thumb">' + part
        
        # Check if it has a baby image that we want to delete
        if re.search(r'assets/images/baby-(1|3|6|9|10)\.jpg', full_thumb):
            # This is a thumb we want to delete!
            # But wait, `part` contains the REST of the file until the NEXT thumb div!
            # Oh, split() breaks it into chunks. The end of `part` contains the closing tags of the row/container/etc.
            # NO, `part` contains everything up to the next thumb div. That means the closing tags of this thumb div AND any HTML between this thumb div and the next one (like whitespace, or maybe closing </div> for the row if this is the last thumb).
            
            # To do this correctly: Find the exact bounds of the thumb div.
            pass
            
def safe_delete(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to match:
    # [whitespace]<div class="col-lg-3 col-md-4 col-xs-6 thumb">
    # ... any content not containing <div class="col-lg-3 ...
    # assets/images/baby-(1|3|6|9|10).jpg
    # ... any content up to the matching closing divs.
    
    # Instead of full HTML parsing, we can just use BeautifulSoup to find the exact string indices!
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    to_remove_texts = []
    
    for thumb in soup.find_all('div', class_='thumb'):
        img = thumb.find('img')
        if img and img.get('src'):
            src = img.get('src')
            if re.search(r'baby-(1|3|6|9|10)\.jpg', src):
                # We want to remove this thumb.
                # BS4's string representation might differ slightly, but usually we can just find it in the original string.
                # Let's just use re.sub with a careful regex.
                pass
                
    # Careful Regex:
    # \s*<div class="col-lg-3 col-md-4 col-xs-6 thumb">\s*<div class="product-gallery">\s*<div class="img-wrapper">\s*<img[^>]*src="assets/images/baby-(?:1|3|6|9|10)\.jpg"[^>]*>.*?</a>\s*</div>\s*</div>
    
    pattern = r'[ \t]*<div class="col-lg-3 col-md-4 col-xs-6 thumb">\s*<div class="product-gallery">\s*<div class="img-wrapper">\s*<img[^>]*src="assets/images/baby-(?:1|3|6|9|10)\.jpg"[^>]*>.*?</a>\s*</div>\s*</div>\n?'
    
    new_content, count = re.subn(pattern, '', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Deleted {count} unnamed baby items from {file_path}")

safe_delete('baby-product.html')
safe_delete('gallery.html')
