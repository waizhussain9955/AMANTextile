import re

file_path = 'basic-apparel.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# For basic-apparel.html, the structure is:
# <div class="hover-overlay">
# 	<h4 class="overlay-category">KITCHEN ITEM</h4>
# </div>
# </div>
# <a href="..." title="..." class="product-title" style="...">KITCHEN GLOVES</a>

# We can match the entire block and replace KITCHEN ITEM with the name found in the a tag.
pattern = r'(<h4 class="overlay-category">)KITCHEN ITEM(</h4>\s*</div>\s*</div>\s*<a[^>]+class="product-title"[^>]*>)(.*?)(</a>)'

def replacer(match):
    name = match.group(3)
    return match.group(1) + name + match.group(2) + name + match.group(3)

new_content, count = re.subn(pattern, replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print(f"Updated {count} hover overlays in basic-apparel.html")
