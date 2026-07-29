const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace header logo size
  content = content.replace(
    /<div id="logo">\s*<a href="index\.html"><img src="assets\/images\/AT_LOGO_LIGHT\.png" style="max-height: [0-9]+px; width: auto;"/g,
    '<div id="logo">\n        <a href="index.html"><img src="assets/images/AT_LOGO_LIGHT.png" style="max-height: 80px; width: auto;"'
  );

  // Replace footer logo src and size
  content = content.replace(
    /<span class="elementor-heading-title "><img src="assets\/images\/AT_LOGO_LIGHT\.png" style="max-height: [0-9]+px; width: auto;"/g,
    '<span class="elementor-heading-title "><img src="assets/images/AT_LOGO_DARK.png" style="max-height: 90px; width: auto;"'
  );

  if (content !== before) {
    fs.writeFileSync(f, content);
    console.log('Updated ' + f);
  }
});
