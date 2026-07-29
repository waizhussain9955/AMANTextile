const fs = require('fs');
const path = require('path');

const newFooter = `  <footer class="awam-elementor-footer footer-4264" style="background: #ffffff; padding: 80px 0 0 0; color: #333333; font-family: 'Poppins', sans-serif; border-top: 1px solid #eaeaea; overflow: hidden;">
    <div class="container">
      <div class="row" style="margin-bottom: 50px;">
        <!-- Column 1: Logo & Social -->
        <div class="col-lg-4 col-md-12 custom-anim custom-anim-1" style="margin-bottom: 30px;">
          <a href="index.html">
            <img src="assets/images/AT_LOGO_DARK.png" alt="AMAN Textile" style="width: 260px; height: auto; max-height: none; margin-bottom: 30px; transition: transform 0.3s ease;">
          </a>
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 20px; color: #010a29;">Social</h6>
          <div class="footer-social-icons" style="display: flex; gap: 15px;">
            <a href="https://www.linkedin.com/company/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-linkedin-in"></i></a>
            <a href="https://www.instagram.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-instagram"></i></a>
            <a href="https://www.facebook.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="https://twitter.com/amantextile" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-x-twitter"></i></a>
            <a href="https://wa.me/923008223945" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 42px; height: 42px; border-radius: 50%; background: #010a29; color: #fff; transition: all 0.3s ease; text-decoration: none;"><i class="fa-brands fa-whatsapp"></i></a>
          </div>
        </div>
        
        <!-- Column 2: Contact -->
        <div class="col-lg-4 col-md-6 custom-anim custom-anim-2" style="margin-bottom: 30px;">
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 30px; color: #010a29;">Contact</h6>
          <div style="margin-bottom: 25px;">
            <a href="mailto:info1@AMANTextile.com" style="color: #555; text-decoration: none; font-size: 15px; transition: color 0.3s ease; font-weight: 500;">info1@AMANTextile.com</a>
          </div>
          <div style="margin-bottom: 25px;">
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 8px;">Toronto Number</strong>
            <span style="color: #555; font-size: 15px; font-weight: 500;">TEL: +1 647 979 4479</span>
          </div>
          <div>
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 8px;">New York Number</strong>
            <span style="color: #555; font-size: 15px; font-weight: 500;">TEL: +1 646 475 8363</span>
          </div>
        </div>

        <!-- Column 3: Address -->
        <div class="col-lg-4 col-md-6 custom-anim custom-anim-3" style="margin-bottom: 30px;">
          <h6 style="font-weight: 700; letter-spacing: 2px; text-transform: uppercase; font-size: 14px; margin-bottom: 30px; color: #010a29;">Address</h6>
          <div style="margin-bottom: 25px;">
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 8px;">Pakistan</strong>
            <span style="color: #555; font-size: 15px; line-height: 1.6; display: block; font-weight: 500; max-width: 250px;">A-25/B SITE, Karachi, Pakistan.</span>
          </div>
          <div>
            <strong style="display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #010a29; margin-bottom: 8px;">New York</strong>
            <span style="color: #555; font-size: 15px; line-height: 1.6; display: block; font-weight: 500; max-width: 250px;">104 W 40 Street, Suite #431, New York NY 10018.</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Copyright Bar -->
    <div class="custom-anim custom-anim-4" style="background: #010a29; color: rgba(255,255,255,0.7); padding: 25px 0; text-align: center; font-size: 13px; letter-spacing: 1px;">
      <div class="container">
        Copyright &copy; 2026 AMAN Textile. All Rights Reserved.
      </div>
    </div>
    
    <style>
      @keyframes customFadeInUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
      }
      .custom-anim {
        opacity: 0;
        animation: customFadeInUp 0.8s ease forwards;
      }
      .custom-anim-1 { animation-delay: 0.2s; }
      .custom-anim-2 { animation-delay: 0.4s; }
      .custom-anim-3 { animation-delay: 0.6s; }
      .custom-anim-4 { animation-delay: 0.8s; }
      
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
  </footer>`;

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace Header Logo Size (using robust regex)
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_LIGHT\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_LIGHT.png" style="width: 220px; height: auto; max-height: none;" alt="AMAN Textile" />'
  );

  // Replace entire footer block
  const footerRegex = /<footer class="awam-elementor-footer footer-4264"[^>]*>[\s\S]*?<\/footer>/i;
  if (footerRegex.test(content)) {
    content = content.replace(footerRegex, newFooter);
  }

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed logos and animations in ' + f);
  }
});
