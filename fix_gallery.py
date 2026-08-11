import re

def fix_gallery(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The user's broken code looks like this:
    '''
    <a href="assets/images/baby-6.jpg">
        <div class="img-wrapper">
            <img class="img-fluid img-thumbnail" src="assets/images/baby-6.jpg" alt="Random Image">
            <div class="hover-overlay">
                <h4 class="overlay-category">View Image</h4>
            </div>
        </div>
    </a>
    '''
    
    # We want to replace it with:
    '''
    <div class="product-gallery">
        <div class="img-wrapper">
            <img class="img-fluid img-thumbnail" src="assets/images/baby-6.jpg" alt="Random Image">
            <div class="hover-overlay">
                <h4 class="overlay-category">BABY ITEM</h4>
            </div>
        </div>
        <a href="assets/images/baby-6.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">BABY ITEM</a>
    </div>
    '''
    
    # Regex to find these broken wrappers.
    # The pattern should match:
    # <a href="(.*?)">\s*<div class="img-wrapper">\s*<img class="img-fluid img-thumbnail" src="(.*?)" alt="Random Image">\s*<div class="hover-overlay">\s*<h4 class="overlay-category">View Image</h4>\s*</div>\s*</div>\s*</a>
    
    pattern = r'<a href="([^"]+)">\s*<div class="img-wrapper">\s*<img class="img-fluid img-thumbnail" src="([^"]+)" alt="Random Image">\s*<div class="hover-overlay">\s*<h4 class="overlay-category">View Image</h4>\s*</div>\s*</div>\s*</a>'
    
    def replacer(match):
        href = match.group(1)
        src = match.group(2)
        
        # Determine category based on src
        if 'baby' in src.lower():
            cat = "BABY ITEM"
        elif 'ht' in src.lower() or 'home' in src.lower():
            cat = "HOME TEXTILE"
        else:
            cat = "KITCHEN ITEM"
            
        return f'''<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="{src}" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">{cat}</h4>
										</div>
									</div>
									<a href="{href}" title="View Image" class="product-title" style="text-decoration: none !important;">{cat}</a>
								</div>'''

    new_content = re.sub(pattern, replacer, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Fixed {file_path}")

fix_gallery('gallery.html')
