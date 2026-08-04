const fs = require('fs');

const files = fs.readdirSync('.').filter(file => file.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    // Safe regex for footer social
    const socialRegex = /<h6[^>]*>\s*Social\s*<\/h6>\s*<div class="footer-social-icons"[^>]*>[\s\S]{0,1000}?<\/div>/g;
    
    if (socialRegex.test(content)) {
        content = content.replace(socialRegex, '');
    }

    if (file === 'index.html') {
        // Change delay:7000 to delay:2000 for the project-carousel
        content = content.replace(/"delay":7000/g, '"delay":2000');
        
        // Remove the old padding-bottom: 20px added in the previous commit
        // and replace it with more aggressive spacing fixes
        const oldCss = '.project-carousel .swiper-slide {\n    padding-bottom: 20px; /* Remove extra space at bottom */\n}';
        const newCss = `.project-carousel .swiper-slide {
    padding-bottom: 0px !important;
    height: auto !important;
}
.project-carousel.metro .content {
    margin-bottom: 0 !important;
}
.elementor-element-545311b {
    margin-bottom: -150px !important;
}`;
        content = content.replace(oldCss, newCss);

        // Remove the previous custom script that might be erroring
        content = content.replace(/<script>\s*document\.addEventListener\("DOMContentLoaded", function \(\) {\s*setTimeout\(function\(\) {\s*var prodSwiperEl = document\.querySelector\('\.project-carousel \.swiper-container'\);\s*if \(prodSwiperEl && prodSwiperEl\.swiper\) {\s*prodSwiperEl\.swiper\.params\.autoplay = \{\s*delay: 2500,\s*disableOnInteraction: false\s*\};\s*prodSwiperEl\.swiper\.autoplay\.start\(\);\s*}\s*}, 1500\);\s*}\);\s*<\/script>/g, '');
    }

    fs.writeFileSync(file, content, 'utf8');
});

console.log('Fixed pages safely.');
