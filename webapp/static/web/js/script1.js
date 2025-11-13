// Navbar scroll behavior
function initNavbarScroll() {
    const navbar = document.querySelector('.main-menu.navbar');
    if (!navbar) return;

    // Get the header section above navbar to calculate offset
    const headerSection = navbar.closest('header');
    const navbarOffset = headerSection ? headerSection.offsetTop : 0;

    let lastScroll = 0;
    const scrollThreshold = 100; // How far to scroll before showing background

    function handleScroll() {
        const currentScroll = window.pageYOffset;

        // Only start sticky behavior after scrolling past the header section
        if (currentScroll > navbarOffset) {
            navbar.classList.add('is-sticky');

            // Add/remove background when scrolled further
            if (currentScroll > (navbarOffset + scrollThreshold)) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        } else {
            // Reset all classes when above the header
            navbar.classList.remove('is-sticky', 'navbar-scrolled');
        }

        lastScroll = currentScroll;
    }

    // Throttle scroll events
    let ticking = false;
    document.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

    // Initial state
    handleScroll();

    // Update offset if window resizes
    window.addEventListener('resize', () => {
        navbarOffset = headerSection ? headerSection.offsetTop : 0;
        handleScroll();
    }, { passive: true });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initNavbarScroll);