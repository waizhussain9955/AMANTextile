const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace footer logo style to use negative margins to counter transparent space in the image
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_DARK-removebg\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_DARK-removebg.png" style="max-width: 180px; height: auto; display: block; margin-top: -45px; margin-bottom: -25px; margin-left: -20px; transition: transform 0.3s ease;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed footer logo alignment with negative margins in ' + f);
  }
});
