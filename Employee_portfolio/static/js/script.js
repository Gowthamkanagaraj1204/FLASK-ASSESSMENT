
const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("open");

        const isExpanded = navLinks.classList.contains("open");
        menuToggle.setAttribute("aria-expanded", isExpanded);
    });
}

const contactForm = document.getElementById("contact-form");
const formStatus = document.getElementById("form-status");

if (contactForm && formStatus) {
    contactForm.addEventListener("submit", function (event) {
        event.preventDefault();

        if (!contactForm.checkValidity()) {
            contactForm.reportValidity();
            return;
        }

        formStatus.textContent =
            "Form validated successfully. Backend submission is not configured.";

        contactForm.reset();
    });
}
