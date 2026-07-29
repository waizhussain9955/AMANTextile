const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

const newFooter = `  <footer class="awam-elementor-footer footer-4264" style="background: #ffffff; padding: 70px 0 0 0; color: #333333; font-family: 'Poppins', sans-serif; border-top: 1px solid #eaeaea; overflow: hidden;">
    <div class="container">
      <div class="row" style="margin-bottom: 40px; align-items: flex-start;">
        <!-- Column 1: Logo -->
        <div class="col-lg-3 col-md-6 footer-anim" style="margin-bottom: 30px;">
          <a href="index.html" style="display: block;">
            <img src="assets/images/AT_LOGO_DARK-removebg.png" style="width: 150px; height: auto; display: block; transition: transform 0.3s ease;" alt="AMAN Textile" />
          </a>
        </div>
        
        <!-- Column 2: Social -->
        <div class="col-lg-3 col-md-6 footer-anim" style="margin-bottom: 30px;">
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 25px; color: #010a29;">Social</h6>
          <div class="footer-social-icons" style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="https://www.linkedin.com/company/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-linkedin-in"></i></a>
            <a href="https://www.instagram.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-instagram"></i></a>
            <a href="https://www.facebook.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://twitter.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-x-twitter"></i></a>
            <a href="https://wa.me/923008223945" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-whatsapp"></i></a>
          </div>
        </div>
        
        <!-- Column 3: Contact -->
        <div class="col-lg-3 col-md-6 footer-anim" style="margin-bottom: 30px;">
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 25px; color: #010a29;">Contact</h6>
          <div style="margin-bottom: 20px;">
            <a href="mailto:info1@AMANTextile.com" style="color: #555; text-decoration: none; font-size: 15px; transition: color 0.3s ease; font-weight: 500;">info1@AMANTextile.com</a>
          </div>
          <div style="margin-bottom: 20px;">
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 5px;">Toronto Number</strong>
            <span style="color: #555; font-size: 15px; font-weight: 500;">TEL: +1 647 979 4479</span>
          </div>
          <div>
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 5px;">New York Number</strong>
            <span style="color: #555; font-size: 15px; font-weight: 500;">TEL: +1 646 475 8363</span>
          </div>
        </div>

        <!-- Column 4: Address -->
        <div class="col-lg-3 col-md-6 footer-anim" style="margin-bottom: 30px;">
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 25px; color: #010a29;">Address</h6>
          <div style="margin-bottom: 20px;">
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 5px;">Pakistan</strong>
            <span style="color: #555; font-size: 15px; line-height: 1.6; display: block; font-weight: 500; max-width: 250px;">A-25/B SITE, Karachi, Pakistan.</span>
          </div>
          <div>
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 5px;">New York</strong>
            <span style="color: #555; font-size: 15px; line-height: 1.6; display: block; font-weight: 500; max-width: 250px;">104 W 40 Street, Suite #431, New York NY 10018.</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Copyright Bar -->
    <div class="footer-anim" style="background: #010a29; color: rgba(255,255,255,0.7); padding: 20px 0; text-align: center; font-size: 13px; letter-spacing: 1px;">
      <div class="container">
        Copyright &copy; 2026 AMAN Textile. All Rights Reserved.
      </div>
    </div>
    
    <style>
      .footer-anim {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 2s ease, transform 2s ease; /* Extremely smooth 2s transition */
      }
      .footer-anim.is-visible {
        opacity: 1;
        transform: translateY(0);
      }
      .footer-social-icons a:hover {
        background: #D4AF37 !important;
        transform: translateY(-5px) !important;
        box-shadow: 0 5px 15px rgba(212,175,55,0.4) !important;
      }
      .footer-social-icons a:hover i {
        color: #010a29 !important;
      }
      .awam-elementor-footer a[href^="mailto"]:hover {
        color: #D4AF37 !important;
      }
    </style>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        var footerItems = document.querySelectorAll('.footer-anim');
        if('IntersectionObserver' in window) {
          var footerObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry, index) {
              if (entry.isIntersecting) {
                // 2.5 seconds base delay (2500ms), 200ms stagger between columns
                setTimeout(function() {
                  entry.target.classList.add('is-visible');
                }, 2500 + (index * 200));
                footerObserver.unobserve(entry.target);
              }
            });
          }, { threshold: 0.1 });
          footerItems.forEach(function(item) {
            footerObserver.observe(item);
          });
        } else {
          footerItems.forEach(function(item) {
            item.classList.add('is-visible');
          });
        }
      });
    </script>
  </footer>`;

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace entire footer block
  const footerRegex = /<footer class="awam-elementor-footer footer-4264"[^>]*>[\s\S]*?<\/footer>/i;
  if (footerRegex.test(content)) {
    content = content.replace(footerRegex, newFooter);
  }

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed 4-column alignment and 2.5s animation in ' + f);
  }
});
