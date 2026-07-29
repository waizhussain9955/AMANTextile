const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace 1500 + to 1000 +
  content = content.replace(
    /1500 \+ \(index \* 200\)/g,
    '1000 + (index * 200)'
  );
  
  // Replace the comment if necessary
  content = content.replace(
    /1\.5 seconds base delay \(1500ms\)/g,
    '1 second base delay (1000ms)'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Reduced animation delay to 1s in ' + f);
  }
});
