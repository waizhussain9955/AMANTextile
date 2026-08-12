import re

file_path = 'gallery.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

append_html = """
							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/baby-7.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">BABY BURP</h4>
										</div>
									</div>
									<a href="assets/images/baby-7.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">BABY BURP</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/baby-8.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">BABY BIPS</h4>
										</div>
									</div>
									<a href="assets/images/baby-8.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">BABY BIPS</a>
								</div>
							</div>
"""

# Find the end of the Baby Items section.
# It's marked by baby-5.jpg block ending.
pattern = r'(<a href="assets/images/baby-5\.jpg"[^>]*>.*?</a>\s*</div>\s*</div>)(\s*</div>\s*</div>\s*</section>)'

def replacer(match):
    return match.group(1) + "\n" + append_html + match.group(2)

new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Added baby-7 and baby-8 to {file_path}")
else:
    print("Could not find the target location to insert!")
