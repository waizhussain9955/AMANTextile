const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace footer logo style to use normal margins and smaller width
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_DARK-removebg\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_DARK-removebg.png" style="max-width: 160px; height: auto; display: block; margin-bottom: 15px; margin-top: -10px; transition: transform 0.3s ease;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed footer logo alignment without extreme negative margins in ' + f);
  }
});
