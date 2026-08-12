import re

files_to_update = ['home-textile.html', 'gallery.html']

home_names = {
    'ht-1.jpg': 'BED SHEET',
    'ht-2.jpg': 'BED SHEET SET',
    'ht-3.jpg': 'TOWELS',
    'ht-6.jpg': 'HAIR WRAP TOWELS'
}

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Update names
    # Similar to how we did it for baby items.
    # The structure:
    # <div class="img-wrapper">
    #     <img class="img-fluid img-thumbnail" src="assets/images/ht-1.jpg" alt="...">
    #     <div class="hover-overlay">
    #         <h4 class="overlay-category">Home Textile 1</h4>
    #     </div>
    # </div>
    # <a href="..." title="..." class="product-title" ...>Home Textile 1</a>
    
    pattern_update = r'(<img[^>]+src="assets/images/(ht-\d+\.jpg)"[^>]*>.*?<h4 class="overlay-category">)(.*?)(</h4>.*?<a[^>]+class="product-title"[^>]*>)(.*?)(</a>)'
    
    def replacer(match):
        img_tag_to_h4 = match.group(1)
        filename = match.group(2)
        old_h4 = match.group(3)
        h4_to_a = match.group(4)
        old_a = match.group(5)
        a_close = match.group(6)
        
        new_name = home_names.get(filename, None)
        
        if new_name:
            return f"{img_tag_to_h4}{new_name}{h4_to_a}{new_name}{a_close}"
        else:
            return match.group(0)

    content = re.sub(pattern_update, replacer, content, flags=re.DOTALL)
    
    # Step 2: Delete unnamed items (ht-4, ht-5, ht-7, ht-8)
    pattern_delete = r'[ \t]*<div class="col-lg-3 col-md-4 col-xs-6 thumb">\s*<div class="product-gallery">\s*<div class="img-wrapper">\s*<img[^>]*src="assets/images/ht-(?:4|5|7|8)\.jpg"[^>]*>.*?</a>\s*</div>\s*</div>\n?'
    
    content, count = re.subn(pattern_delete, '', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated names and deleted {count} unnamed home textile items from {file_path}")

