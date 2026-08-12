import re

file_path = 'basic-apparel.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the overlay-category and product-title uppercase for all kitchen items
pattern = r'(<h4 class="overlay-category">)(.*?)(</h4>)'
def replacer_h4(match):
    return match.group(1) + match.group(2).upper() + match.group(3)

content = re.sub(pattern, replacer_h4, content)

pattern_a = r'(class="product-title"[^>]*>)(.*?)(</a>)'
def replacer_a(match):
    return match.group(1) + match.group(2).upper() + match.group(3)

content = re.sub(pattern_a, replacer_a, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated basic-apparel.html to uppercase")
