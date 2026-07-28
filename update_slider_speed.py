import os
import re

# 1. Update data-slider-settings in index.html & homepage.html
new_slider_settings = 'data-slider-settings=\'{"autoplay":{"delay":7000,"disableOnInteraction":false},"parallax":true,"mobparallax":true,"loop":true,"speed":2500}\''

html_files = ['index.html', 'homepage.html']

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = re.sub(r'data-slider-settings=[\'"][^\'"]*[\'"]', new_slider_settings, html)

        # Inject custom script for scroll-triggered slide transitions and slow autoplay speed
        scroll_slider_script = """
<script id="custom-slider-scroll-fix">
  document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      if (window.Swiper && document.querySelector('.slider .parallax-slider')) {
        var swiperEl = document.querySelector('.slider .parallax-slider').swiper;
        if (swiperEl) {
          swiperEl.params.speed = 2500; // Slow smooth 2.5s transition animation
          swiperEl.params.autoplay = {
            delay: 7000, // 7 seconds delay per slide
            disableOnInteraction: false
          };
          swiperEl.autoplay.start();

          // Optional: Scroll event to trigger slide change on user scroll
          var lastScroll = window.scrollY;
          var scrollTicking = false;
          window.addEventListener('scroll', function() {
            if (!scrollTicking && window.scrollY < 800) {
              window.requestAnimationFrame(function() {
                var currentScroll = window.scrollY;
                if (Math.abs(currentScroll - lastScroll) > 150) {
                  if (currentScroll > lastScroll) {
                    swiperEl.slideNext();
                  } else {
                    swiperEl.slidePrev();
                  }
                  lastScroll = currentScroll;
                }
                scrollTicking = false;
              });
              scrollTicking = true;
            }
          });
        }
      }
    }, 1200);
  });
</script>
"""
        if 'custom-slider-scroll-fix' not in html:
            html = html.replace('</body>', f'{scroll_slider_script}\n</body>')

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated slider speed & scroll script in {hfile}")
