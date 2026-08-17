const menuToggle = document.querySelector("[data-menu-toggle]");
const menuDrawer = document.querySelector("[data-mobile-drawer]");
const menuBackdrop = document.querySelector("[data-mobile-backdrop]");
const menuClose = document.querySelector("[data-menu-close]");
const faqTriggers = document.querySelectorAll(".faq-trigger");
const lightboxImages = document.querySelectorAll("[data-lightbox]");
const searchInput = document.querySelector("[data-catalog-search]");
const brandFilter = document.querySelector("[data-brand-filter]");
const filterButtons = document.querySelectorAll("[data-filter]");
const filterCards = document.querySelectorAll("[data-product-card]");
const whatsappForms = document.querySelectorAll("[data-wa-form]");

function setMenuState(isOpen) {
  if (!menuDrawer || !menuBackdrop) return;
  menuDrawer.classList.toggle("is-open", isOpen);
  menuBackdrop.classList.toggle("is-open", isOpen);
  menuDrawer.setAttribute("aria-hidden", String(!isOpen));
  menuToggle?.setAttribute("aria-expanded", String(isOpen));
  document.body.classList.toggle("is-menu-open", isOpen);
  if (isOpen) {
    menuClose?.focus();
  }
}

if (menuToggle && menuDrawer && menuBackdrop) {
  menuToggle.addEventListener("click", () => setMenuState(true));
  menuBackdrop.addEventListener("click", () => setMenuState(false));
}

if (menuClose) {
  menuClose.addEventListener("click", () => {
    setMenuState(false);
    menuToggle?.focus();
  });
}

menuDrawer?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => setMenuState(false));
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setMenuState(false);
    closeLightbox();
  }
});

faqTriggers.forEach((trigger) => {
  trigger.addEventListener("click", () => {
    const item = trigger.closest(".faq-item");
    if (!item) return;
    const wasOpen = item.classList.contains("is-active");
    const scope = trigger.closest(".faq-accordion");
    scope?.querySelectorAll(".faq-item").forEach((faqItem) => {
      faqItem.classList.remove("is-active");
      const button = faqItem.querySelector(".faq-trigger");
      if (button) button.setAttribute("aria-expanded", "false");
    });
    if (!wasOpen) {
      item.classList.add("is-active");
      trigger.setAttribute("aria-expanded", "true");
    }
  });
});

let lightbox;
let lightboxImage;
let lightboxCaption;
let lightboxClose;
let lightboxPreviousFocus;

function ensureLightbox() {
  if (lightbox) return;
  lightbox = document.createElement("div");
  lightbox.className = "gallery-lightbox";
  lightbox.setAttribute("role", "dialog");
  lightbox.setAttribute("aria-modal", "true");
  lightbox.setAttribute("aria-hidden", "true");
  lightbox.innerHTML = `
    <button class="gallery-lightbox-close" type="button" aria-label="Close image preview">Close</button>
    <figure class="gallery-lightbox-figure">
      <img class="gallery-lightbox-image" alt="">
      <figcaption class="gallery-lightbox-caption"></figcaption>
    </figure>
  `;
  document.body.appendChild(lightbox);
  lightboxImage = lightbox.querySelector(".gallery-lightbox-image");
  lightboxCaption = lightbox.querySelector(".gallery-lightbox-caption");
  lightboxClose = lightbox.querySelector(".gallery-lightbox-close");
  lightbox.addEventListener("click", (event) => {
    if (
      event.target === lightbox ||
      event.target.classList.contains("gallery-lightbox-close")
    ) {
      closeLightbox();
    }
  });
}

function openLightbox(image) {
  ensureLightbox();
  lightboxPreviousFocus = document.activeElement;
  lightboxImage.src = image.getAttribute("data-lightbox-src") || image.currentSrc || image.src;
  lightboxImage.alt = image.alt || "";
  lightboxCaption.textContent = image.getAttribute("data-lightbox-caption") || image.alt || "";
  lightbox.classList.add("is-open");
  lightbox.setAttribute("aria-hidden", "false");
  document.body.classList.add("is-lightbox-open");
  lightboxClose?.focus();
}

function closeLightbox() {
  if (!lightbox) return;
  lightbox.classList.remove("is-open");
  lightbox.setAttribute("aria-hidden", "true");
  document.body.classList.remove("is-lightbox-open");
  if (lightboxPreviousFocus instanceof HTMLElement) {
    lightboxPreviousFocus.focus();
  }
}

lightboxImages.forEach((image) => {
  image.addEventListener("click", () => openLightbox(image));
  image.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      openLightbox(image);
    }
  });
});

function filterCatalog() {
  const query = (searchInput?.value || "").trim().toLowerCase();
  const activeBrand = (brandFilter?.value || "").trim().toLowerCase();
  const activeFilter = document.querySelector("[data-filter].is-active")?.dataset.filter || "all";
  filterCards.forEach((card) => {
    const searchable = (card.dataset.search || "").toLowerCase();
    const category = card.dataset.category || "";
    const brand = (card.dataset.brand || "").toLowerCase();
    const matchesQuery = query === "" || searchable.includes(query);
    const matchesBrand = activeBrand === "" || brand === activeBrand;
    const matchesFilter = activeFilter === "all" || category === activeFilter;
    card.hidden = !(matchesQuery && matchesBrand && matchesFilter);
  });
}

if (searchInput) {
  searchInput.addEventListener("input", filterCatalog);
}

if (brandFilter) {
  brandFilter.addEventListener("change", filterCatalog);
}

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((other) => other.classList.remove("is-active"));
    button.classList.add("is-active");
    filterCatalog();
  });
});

whatsappForms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const payload = [];
    const heading = form.dataset.formTitle || "New enquiry";
    payload.push(heading);
    for (const [key, value] of formData.entries()) {
      if (typeof value !== "string" || value.trim() === "") continue;
      if (key === "consent") continue;
      payload.push(`${key}: ${value.trim()}`);
    }
    const waUrl = `https://wa.me/918758964040?text=${encodeURIComponent(payload.join("\n"))}`;
    window.open(waUrl, "_blank", "noopener");
  });
});
