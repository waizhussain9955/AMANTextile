import os
import re

special_services_html = """
        <section class="special-services-section" style="background: linear-gradient(rgba(10, 15, 30, 0.88), rgba(10, 15, 30, 0.92)), url('assets/images/factory-1.jpg'); background-size: cover; background-position: center; padding: 90px 0; color: #ffffff; position: relative; margin: 60px 0;">
          <div class="container">
            <div class="row align-items-center">
              <!-- Left Column: Title & Intro -->
              <div class="col-lg-4 col-md-12 mb-4 mb-lg-0">
                <div style="font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #D4AF37; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                  SPECIAL SERVICES <span style="font-size: 0.7rem; color: #D4AF37;">▲</span>
                </div>
                <h2 style="font-size: 2.5rem; font-weight: 800; color: #ffffff; line-height: 1.15; border-left: 5px solid #ffffff; padding-left: 18px; margin-bottom: 20px; text-transform: uppercase; font-family: 'Poppins', sans-serif;">
                  WE TAKE SAFETY<br>MEASUREMENTS
                </h2>
                <p style="color: rgba(255, 255, 255, 0.75); font-size: 0.95rem; line-height: 1.6; max-width: 320px;">
                  It can be very well produced using fiber, yarn, texture and dispatched safely.
                </p>
              </div>

              <!-- Middle Column: Progress Skill Bars -->
              <div class="col-lg-4 col-md-6 mb-4 mb-lg-0">
                <div style="padding: 0 15px;">
                  <!-- Finishing -->
                  <div style="margin-bottom: 25px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1rem; margin-bottom: 8px;">
                      <span>Finishing</span>
                      <span>99%</span>
                    </div>
                    <div style="width: 100%; height: 10px; background: rgba(255, 255, 255, 0.15); border-radius: 6px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.3);">
                      <div style="width: 99%; height: 100%; background: linear-gradient(90deg, #056eb9, #D4AF37); border-radius: 6px;"></div>
                    </div>
                  </div>

                  <!-- Quality -->
                  <div style="margin-bottom: 25px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1rem; margin-bottom: 8px;">
                      <span>Quality</span>
                      <span>99%</span>
                    </div>
                    <div style="width: 100%; height: 10px; background: rgba(255, 255, 255, 0.15); border-radius: 6px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.3);">
                      <div style="width: 99%; height: 100%; background: linear-gradient(90deg, #056eb9, #D4AF37); border-radius: 6px;"></div>
                    </div>
                  </div>

                  <!-- Packaging -->
                  <div>
                    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 1rem; margin-bottom: 8px;">
                      <span>Packaging</span>
                      <span>99%</span>
                    </div>
                    <div style="width: 100%; height: 10px; background: rgba(255, 255, 255, 0.15); border-radius: 6px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.3);">
                      <div style="width: 99%; height: 100%; background: linear-gradient(90deg, #056eb9, #D4AF37); border-radius: 6px;"></div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Right Column: Animated Counter Card (1 to 600) -->
              <div class="col-lg-4 col-md-6 text-center">
                <div style="background: rgba(255, 255, 255, 0.22); backdrop-filter: blur(10px); border-radius: 12px; padding: 35px 25px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); margin-bottom: 15px;">
                  <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 5px;">
                    <svg width="55" height="55" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <circle cx="32" cy="32" r="26" stroke="#ffffff" stroke-width="3" stroke-dasharray="4 4" />
                      <path d="M20 44 L44 20 M24 20 L20 24 M40 40 L44 44" stroke="#ffffff" stroke-width="3" stroke-linecap="round" />
                      <path d="M18 32 C 18 20, 46 20, 46 32 C 46 44, 18 44, 18 32 Z" stroke="#D4AF37" stroke-width="3" fill="none" />
                    </svg>
                    <div style="text-align: left;">
                      <div id="happy-customer-counter" style="font-size: 3.2rem; font-weight: 800; color: #ffffff; line-height: 1; font-family: 'Poppins', sans-serif;">1 +</div>
                      <div style="font-size: 0.95rem; font-weight: 700; color: #ffffff; margin-top: 4px;">Happy Customer</div>
                    </div>
                  </div>
                </div>
                <div style="font-size: 0.88rem; color: rgba(255,255,255,0.85); line-height: 1.4;">
                  The Largest Exporter of <strong style="color: #ffffff; font-weight: 800; text-transform: uppercase;">AMAN TEXTILE INDUSTRIES</strong>
                </div>
              </div>
            </div>
          </div>
        </section>

        <script id="customer-counter-script">
          document.addEventListener("DOMContentLoaded", function() {
            var counterEl = document.getElementById("happy-customer-counter");
            if (!counterEl) return;
            
            var started = false;
            var targetCount = 600;
            var duration = 2500;

            function animateCounter() {
              var startTime = null;

              function updateNumber(timestamp) {
                if (!startTime) startTime = timestamp;
                var progress = Math.min((timestamp - startTime) / duration, 1);
                var easeOut = 1 - Math.pow(1 - progress, 3);
                var currentNum = Math.floor(easeOut * (targetCount - 1) + 1);
                counterEl.innerText = currentNum + " +";

                if (progress < 1) {
                  requestAnimationFrame(updateNumber);
                } else {
                  counterEl.innerText = targetCount + " +";
                }
              }

              requestAnimationFrame(updateNumber);
            }

            var observer = new IntersectionObserver(function(entries) {
              entries.forEach(function(entry) {
                if (entry.isIntersecting && !started) {
                  started = true;
                  animateCounter();
                }
              });
            }, { threshold: 0.3 });

            observer.observe(counterEl);
          });
        </script>
"""

# Replace Our Partners section in index.html and homepage.html
for hfile in ['index.html', 'homepage.html']:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # Match Our Partners section
        pattern = r'<\s*section[^>]*class=["\'][^"\']*m-t-100[^"\']*["\'][^>]*>.*?Our Partners.*?<\s*/\s*section\s*>'
        html = re.sub(pattern, special_services_html, html, flags=re.DOTALL | re.IGNORECASE)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Replaced Our Partners with Special Services in {hfile}")
