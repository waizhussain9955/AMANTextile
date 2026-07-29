
document.addEventListener('DOMContentLoaded', function() {
  // Mobile Nav Toggle
  const toggleBtn = document.getElementById('mobile-nav-toggle');
  const navContainer = document.getElementById('nav-menu-container');
  
  if (toggleBtn && navContainer) {
    toggleBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      navContainer.classList.toggle('nav-menu-active');
      const icon = toggleBtn.querySelector('i');
      if (icon) {
        if (navContainer.classList.contains('nav-menu-active')) {
          icon.className = 'fa-solid fa-xmark';
        } else {
          icon.className = 'fa-solid fa-bars';
        }
      }
    });

    // Close mobile nav on outside click
    document.addEventListener('click', function(e) {
      if (navContainer.classList.contains('nav-menu-active') && !navContainer.contains(e.target) && !toggleBtn.contains(e.target)) {
        navContainer.classList.remove('nav-menu-active');
        const icon = toggleBtn.querySelector('i');
        if (icon) icon.className = 'fa-solid fa-bars';
      }
    });
  }

  # Mobile Submenu Accordion Toggle
  const dropdownItems = document.querySelectorAll('.menu-has-children > a');
  dropdownItems.forEach(item => {
    item.addEventListener('click', function(e) {
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
