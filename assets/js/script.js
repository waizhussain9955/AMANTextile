/**
 * Naeem Enterprise - Master Client Script
 * Handles Interactive Navigation, Hero Slider, Gallery Filtering, Lightbox & Contact Form
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initHeroSlider();
  initGalleryFilter();
  initLightbox();
  initContactForm();
});

/* --- 1. Mobile Navigation & Dropdowns --- */
function initNavigation() {
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navItems = document.querySelectorAll('.nav-item.has-dropdown');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      const icon = mobileToggle.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-bars');
        icon.classList.toggle('fa-times');
      }
    });
  }

  navItems.forEach(item => {
    const link = item.querySelector('.nav-link');
    if (link) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 992) {
          e.preventDefault();
          item.classList.toggle('open');
        }
      });
    }
  });

  // Sticky Header Effect
  const header = document.getElementById('main-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.style.padding = '0';
        header.style.boxShadow = '0 10px 30px rgba(0,0,0,0.3)';
      } else {
        header.style.boxShadow = 'none';
      }
    });
  }
}

/* --- 2. Hero Banner Slider --- */
function initHeroSlider() {
  const track = document.querySelector('.slide-track');
  const slides = document.querySelectorAll('.hero-slide');
  const prevBtn = document.querySelector('.slider-prev');
  const nextBtn = document.querySelector('.slider-next');
  const dotsContainer = document.querySelector('.slider-dots');

  if (!track || slides.length === 0) return;

  let currentIndex = 0;
  let autoSlideTimer = null;

  // Build dots
  slides.forEach((_, idx) => {
    const dot = document.createElement('span');
    dot.classList.add('dot');
    if (idx === 0) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(idx));
    if (dotsContainer) dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll('.dot');

  function goToSlide(index) {
    if (index < 0) index = slides.length - 1;
    if (index >= slides.length) index = 0;
    currentIndex = index;
    
    track.style.transform = `translateX(-${currentIndex * 100}%)`;

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentIndex);
    });

    resetTimer();
  }

  if (prevBtn) prevBtn.addEventListener('click', () => goToSlide(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goToSlide(currentIndex + 1));

  function startTimer() {
    autoSlideTimer = setInterval(() => {
      goToSlide(currentIndex + 1);
    }, 5000);
  }

  function resetTimer() {
    clearInterval(autoSlideTimer);
    startTimer();
  }

  startTimer();
}

/* --- 3. Gallery Category Filter --- */
function initGalleryFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  if (filterBtns.length === 0 || galleryItems.length === 0) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const category = item.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* --- 4. Lightbox Modal --- */
function initLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  
  if (galleryItems.length === 0) return;

  // Create lightbox markup
  const lightbox = document.createElement('div');
  lightbox.id = 'lightbox-modal';
  lightbox.style.cssText = `
    position: fixed; inset: 0; z-index: 2000; background: rgba(0,0,0,0.9);
    display: none; align-items: center; justify-content: center; padding: 20px;
  `;
  lightbox.innerHTML = `
    <div style="position: relative; max-width: 900px; width: 100%;">
      <span id="close-lightbox" style="position: absolute; top: -40px; right: 0; color: #fff; font-size: 2rem; cursor: pointer;">&times;</span>
      <img id="lightbox-img" src="" style="width: 100%; max-height: 80vh; object-fit: contain; border-radius: 8px;">
      <h4 id="lightbox-title" style="color: #fff; text-align: center; margin-top: 15px; font-weight: 500;"></h4>
    </div>
  `;
  document.body.appendChild(lightbox);

  const lightboxImg = lightbox.querySelector('#lightbox-img');
  const lightboxTitle = lightbox.querySelector('#lightbox-title');
  const closeBtn = lightbox.querySelector('#close-lightbox');

  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const title = item.querySelector('.gallery-overlay h4')?.innerText || '';
      if (img) {
        lightboxImg.src = img.src;
        lightboxTitle.innerText = title;
        lightbox.style.display = 'flex';
      }
    });
  });

  closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none';
  });

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.style.display = 'none';
    }
  });
}

/* --- 5. Contact Form Submission --- */
function initContactForm() {
  const contactForm = document.getElementById('nae-contact-form');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerText;
    
    submitBtn.innerText = 'Sending Inquiry...';
    submitBtn.disabled = true;

    setTimeout(() => {
      alert('Thank you for reaching out to Naeem Enterprise! Your inquiry has been sent successfully. Our team will contact you shortly.');
      contactForm.reset();
      submitBtn.innerText = originalText;
      submitBtn.disabled = false;
    }, 1200);
  });
}
