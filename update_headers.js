const fs = require('fs');

const pages = [
  'about-us.html',
  'baby-product.html',
  'basic-apparel.html',
  'contact-us.html',
  'design.html',
  'fabric.html',
  'gallery.html',
  'home-textile.html',
  'knits-woven.html',
  'manufacturing.html'
];

const homeHeader = [
  '<header id="header">',
  '  <div class="container main-menu">',
  '    <div class="row align-items-center justify-content-between d-flex">',
  '      <div id="logo">',
  '        <a href="index.html"><img src="assets/images/logo.svg" style="max-height: 42px; width: auto;" alt="AMAN Textile" /></a>',
  '      </div>',
  '      <nav id="nav-menu-container">',
  '        <ul class="nav-menu">',
  '          <li><a href="index.html">Home</a></li>',
  '          <li><a href="about-us.html">About Us</a></li>',
  '          <li class="menu-has-children"><a href="#">Products</a>',
  '            <ul>',
  '              <li><a href="fabric.html">Fabrics</a></li>',
  '              <li><a href="basic-apparel.html">Apparel</a></li>',
  '              <li><a href="baby-product.html">Baby Garments</a></li>',
  '              <li><a href="home-textile.html">Home Textile</a></li>',
  '            </ul>',
  '          </li>',
  '          <li><a href="gallery.html">Gallery</a></li>',
  '          <li><a href="manufacturing.html">Manufacturing</a></li>',
  '          <li><a href="contact-us.html">Contact Us</a></li>',
  '        </ul>',
  '      </nav>',
  '    </div>',
  '  </div>',
  '</header>'
].join('\n');

pages.forEach(page => {
  let html = fs.readFileSync(page, 'utf8');
  const before = html;
  html = html.replace(/<header id="header">[\s\S]*?<\/header>/, homeHeader);
  if (html !== before) {
    fs.writeFileSync(page, html, 'utf8');
    console.log('Updated: ' + page);
  } else {
    console.log('No change (header pattern not matched): ' + page);
  }
});

console.log('\nDone!');
