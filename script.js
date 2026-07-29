
document.addEventListener('DOMContentLoaded', function() {
  const toggleBtn = document.getElementById('mobile-nav-toggle');
  const navContainer = document.getElementById('nav-menu-container');
  let overlay = document.getElementById('mobile-nav-overlay');

  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = 'mobile-nav-overlay';
    document.body.appendChild(overlay);
  }

  function closeNav() {
    if (navContainer) navContainer.classList.remove('nav-menu-active');
    if (toggleBtn) toggleBtn.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
  }

  function openNav() {
    if (navContainer) navContainer.classList.add('nav-menu-active');
    if (toggleBtn) toggleBtn.classList.add('open');
    if (overlay) overlay.classList.add('active');
  }

  if (toggleBtn && navContainer) {
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      if (navContainer.classList.contains('nav-menu-active')) {
        closeNav();
      } else {
        openNav();
      }
    });

    overlay.addEventListener('click', closeNav);

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeNav();
    });
  }

  // Mobile Submenu Accordion Toggle
  const dropdownLinks = document.querySelectorAll('#nav-menu-container .menu-has-children > a');
  dropdownLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      if (window.innerWidth <= 991) {
        e.preventDefault();
        const parent = this.parentElement;
        parent.classList.toggle('active');
      }
    });
  });

  // Animated Counter for 1 to 600 Happy Customers
  const counterEl = document.getElementById('happy-customer-counter');
  if (counterEl) {
    let started = false;
    const startCounter = () => {
      const rect = counterEl.getBoundingClientRect();
      if (rect.top <= window.innerHeight && rect.bottom >= 0 && !started) {
        started = true;
        let count = 1;
        const target = 600;
        const duration = 2000;
        const increment = Math.ceil(target / (duration / 16));
        const timer = setInterval(() => {
          count += increment;
          if (count >= target) {
            count = target;
            counterEl.textContent = target + ' +';
            clearInterval(timer);
          } else {
            counterEl.textContent = count + ' +';
          }
        }, 16);
      }
    };
    window.addEventListener('scroll', startCounter);
    startCounter();
  }
});
