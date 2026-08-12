import re

file_path = 'gallery.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new HTML for the Kitchen items in gallery.html
kitchen_items_html = """
							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-1.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">KITCHEN GLOVES</h4>
										</div>
									</div>
									<a href="assets/images/ba-1.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">KITCHEN GLOVES</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-3.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">GOLOVES AND TOWEL</h4>
										</div>
									</div>
									<a href="assets/images/ba-3.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">GOLOVES AND TOWEL</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-4.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">TERRY KITCHEN TOWELLS</h4>
										</div>
									</div>
									<a href="assets/images/ba-4.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">TERRY KITCHEN TOWELLS</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-5.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">POT HOLDERS SETT</h4>
										</div>
									</div>
									<a href="assets/images/ba-5.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">POT HOLDERS SETT</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-2.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">POT HOLDERS</h4>
										</div>
									</div>
									<a href="assets/images/ba-2.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">POT HOLDERS</a>
								</div>
							</div>

							<div class="col-lg-3 col-md-4 col-xs-6 thumb">
								<div class="product-gallery">
									<div class="img-wrapper">
										<img class="img-fluid img-thumbnail" src="assets/images/ba-8.jpg" alt="Random Image">
										<div class="hover-overlay">
											<h4 class="overlay-category">DISH TOWELS SET</h4>
										</div>
									</div>
									<a href="assets/images/ba-8.jpg" title="View Image" class="product-title" style="text-decoration: none !important;">DISH TOWELS SET</a>
								</div>
							</div>
"""

# Find the Kitchen items section in gallery.html and replace all the ba-* items with the above HTML.
# The kitchen items are between:
# <h3 class="elementor-heading-title elementor-size-default t-center text-white">KITCHEN ITEMS</h3>
# and the closing </div></div></section> before BABY ITEMS.

pattern = r'(<h3 class="elementor-heading-title elementor-size-default t-center text-white">\s*KITCHEN ITEMS\s*</h3>\s*</div>\s*</div>\s*</div>\s*<div class="row gallery">).*?(</div>\s*</div>\s*</section>)'

def replacer(match):
    return match.group(1) + "\n" + kitchen_items_html + "\n" + match.group(2)

new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print(f"Updated {count} kitchen items sections in {file_path}")

