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

pages.forEach(page => {
  let html = fs.readFileSync(page, 'utf8');
  const before = html;

  // Remove conflicting script.js that fights with main.js
  html = html.replace(/<script src="script\.js"><\/script>/g, '');
  html = html.replace(/<script src="\.\/script\.js"><\/script>/g, '');

  if (html !== before) {
    fs.writeFileSync(page, html, 'utf8');
    console.log('Removed script.js from: ' + page);
  } else {
    console.log('No script.js found in: ' + page);
  }
});

console.log('\nDone!');
