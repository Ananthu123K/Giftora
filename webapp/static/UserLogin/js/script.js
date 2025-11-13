document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signupForm');
    const submitBtn = document.getElementById('submitBtn');

    // Get all required input elements
    const nameInput = document.getElementById('fullName');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const termsCheckbox = document.getElementById('terms');


    // --- Password Toggle Functionality (for Password and Confirm Password) ---
    function setupPasswordToggle(toggleId, inputId) {
        const toggleBtn = document.getElementById(toggleId);
        const inputField = document.getElementById(inputId);

        if (toggleBtn && inputField) {
            toggleBtn.addEventListener('click', function () {
                const type = inputField.getAttribute('type') === 'password' ? 'text' : 'password';
                inputField.setAttribute('type', type);

                this.querySelector('i').classList.toggle('fa-eye');
                this.querySelector('i').classList.toggle('fa-eye-slash');
            });
        }
    }

    setupPasswordToggle('togglePassword', 'password');
    setupPasswordToggle('toggleConfirmPassword', 'confirmPassword');


    // --- Validation Helper Functions ---
    const setError = (groupId, message) => {
        const group = document.getElementById(groupId);
        group.classList.add('error');
        group.querySelector('.error-message').textContent = message;
        group.querySelector('.error-message').style.display = 'block';
    };

    const clearError = (groupId) => {
        const group = document.getElementById(groupId);
        group.classList.remove('error');
        group.querySelector('.error-message').style.display = 'none';
    };

    const validateEmail = (email) => {
        // Basic email regex
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
    };

    // Note: Phone number validation is highly region-specific. This is a very basic check.
    const validatePhone = (phone) => {
        // Simple check: 10 to 15 digits (removes common non-digit chars first)
        const cleanedPhone = phone.replace(/[^\d]/g, '');
        return cleanedPhone.length >= 10 && cleanedPhone.length <= 15;
    };


    // --- Form Submission and Validation ---
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            let isValid = true;

            // 1. Reset all error states
            document.querySelectorAll('.form-group').forEach(group => clearError(group.id));

            // 2. Username (Name) Validation (Min 4 characters)
            if (!nameInput.value.trim() || nameInput.value.trim().length < 4) {
                setError('name-group', 'Username must be at least 4 characters long.');
                isValid = false;
            }

            // 3. Email Validation
            if (!validateEmail(emailInput.value)) {
                setError('email-group', 'Please enter a valid email address.');
                isValid = false;
            }

            // 4. Phone Validation
            if (!validatePhone(phoneInput.value)) {
                setError('phone-group', 'Please enter a valid phone number (10-15 digits).');
                isValid = false;
            }

            // 5. Password Length Validation (Min 6 characters)
            if (passwordInput.value.length < 6) {
                setError('password-group', 'Password must be at least 6 characters.');
                isValid = false;
            }

            // 6. Confirm Password Match
            if (passwordInput.value !== confirmPasswordInput.value) {
                setError('confirm-password-group', 'Passwords do not match.');
                isValid = false;
            }

            // 7. Terms & Conditions Check
            if (!termsCheckbox.checked) {
                alert("You must agree to the Terms & Conditions.");
                isValid = false;
            }


            // --- Submit if valid ---
            if (isValid) {
                // Add loading animation
                submitBtn.classList.add('loading');
                submitBtn.setAttribute('disabled', 'true');

                // Submit the form to the Django view
                form.submit();
            }
        });
    }
});



var productCarousel = new Swiper('.products-carousel', {
    // Basic settings
    loop: true,
    spaceBetween: 25, // Space between products
    speed: 500,

    // Navigation (using the buttons you included in the HTML)
    navigation: {
        nextEl: '.products-carousel-next',
        prevEl: '.products-carousel-prev',
    },

    // Crucial for Viewability: Responsive Breakpoints
    breakpoints: {
        0: {
            slidesPerView: 1.5, // 1 full item + a peek of the next one on mobile
        },
        576: {
            slidesPerView: 2, // 2 items on small tablets
        },
        768: {
            slidesPerView: 3, // 3 items on standard tablets/small laptops
        },
        992: {
            slidesPerView: 4, // 4 items on desktops
        },
        1200: {
            slidesPerView: 5, // 5 items on larger screens
        }
    },
});