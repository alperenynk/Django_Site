document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body");
    const darkButton = document.querySelector(".bb8-toggle__checkbox");
    const header = document.querySelector(".header");
    const hiText = document.querySelector(".up");
    const paragraphs = document.querySelectorAll("p");
    const header1 = document.querySelectorAll(".header-title");
    const testimonialTitles = document.querySelectorAll(".testimonial-card-title");
    const testimonialSubtitles = document.querySelectorAll(".testimonial-card-subtitle");
    const testimonialCards = document.querySelectorAll(".testimonial-card-body");
    const testimonialImages = document.querySelectorAll(".testimonial-card-img-holder");
    const testimonialImageHolder = document.querySelectorAll(".testimonial-card-img");
    const navbar = document.querySelector(".custom-navbar");
    const DevCRUD = document.querySelector("#p1");
    const ThemeWagon = document.querySelector("#p2");
    const footerTexts = document.querySelectorAll(".footer p");

    // Input ve textarea alanlarını seçelim
    const inputFields = document.querySelectorAll("input, textarea");

    function updateNavbarBackground() {
        if (window.scrollY > 0) {
            if (darkButton.classList.contains("dark")) {
                navbar.style.backgroundColor = "#222831";
            } else {
                navbar.style.backgroundColor = "#fff";
            }
        } else {
            navbar.style.backgroundColor = "transparent";
        }
    }

    function updateInputFieldColors() {
        if (darkButton.classList.contains("dark")) {
            inputFields.forEach(input => {
                input.style.color = "#fff";
            });
        } else {
            inputFields.forEach(input => {
                input.style.color = "#212529";
            });
        }
    }

    function updatePlaceholderColor() {
        if (darkButton.classList.contains("dark")) {
            inputFields.forEach(input => {
                const placeholderText = input.getAttribute("placeholder");
                if (placeholderText) {
                    input.setAttribute("data-placeholder", placeholderText);
                    input.setAttribute("placeholder", placeholderText.replace("#212529", "#f0f0f0"));
                }
            });
        } else {
            inputFields.forEach(input => {
                const placeholderText = input.getAttribute("data-placeholder");
                if (placeholderText) {
                    input.setAttribute("placeholder", placeholderText.replace("#f0f0f0", "#212529"));
                }
            });
        }
    }

    darkButton.addEventListener("click", () => {
        darkButton.classList.toggle("dark");
        if (darkButton.classList.contains("dark")) {
            body.style.backgroundColor = "#222831";
            body.style.color = "#ffffff";
            header.style.backgroundColor = "#222831";
            hiText.style.color = "#f0f0f0";
            paragraphs.forEach(p => p.style.color = "#f0f0f0");
            header1.forEach(p => p.style.color = "#f0f0f0");
            testimonialTitles.forEach(title => title.style.color = "#f0f0f0");
            testimonialSubtitles.forEach(subtitle => subtitle.style.color = "#f0f0f0");
            testimonialCards.forEach(card => card.style.backgroundColor = "#222831");
            testimonialImages.forEach(card => card.style.backgroundColor = "#222831");
            testimonialImageHolder.forEach(card => card.style.backgroundColor = "#222831");
            DevCRUD.style.color = "#fff";
            ThemeWagon.style.color = "#fff";
            footerTexts.forEach(footerText => footerText.style.color = "#f0f0f0");
        } else {
            body.style.backgroundColor = "#fff";
            body.style.color = "#212529";
            header.style.backgroundColor = "#fff";
            hiText.style.color = "#212529";
            paragraphs.forEach(p => p.style.color = "#212529");
            header1.forEach(p => p.style.color = "#212529");
            testimonialTitles.forEach(title => title.style.color = "#695aa6");
            testimonialSubtitles.forEach(subtitle => subtitle.style.color = "#212529");
            testimonialCards.forEach(card => card.style.backgroundColor = "#fff");
            testimonialImages.forEach(card => card.style.backgroundColor = "#fff");
            testimonialImageHolder.forEach(card => card.style.backgroundColor = "#fff");
            DevCRUD.style.color = "#222831";
            ThemeWagon.style.color = "#222831";
            footerTexts.forEach(footerText => footerText.style.color = "#212529");
        }
        updateNavbarBackground();
        updateInputFieldColors();
        updatePlaceholderColor(); // Placeholder renklerini güncelle
    });

    window.addEventListener("scroll", updateNavbarBackground);
    updateNavbarBackground();
    updateInputFieldColors(); // Başlangıçta input renklerini güncelle
    updatePlaceholderColor(); // Başlangıçta placeholder renklerini güncelle
});
