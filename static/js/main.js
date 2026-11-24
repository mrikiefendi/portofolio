const toggle = document.getElementById("menuToggle");
const nav = document.getElementById("nav");

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });

  nav.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

function initScrollReveal() {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    return;
  }

  if (!("IntersectionObserver" in window)) return;

  const selectors = [
    ".about > .eyebrow",
    ".about > h2",
    ".about .info-card",
    "#skills .section-heading",
    "#skills .skill",
    "#works .section-heading",
    "#works .project-card",
    ".resume > .eyebrow",
    ".resume > h2",
    ".resume-grid > div",
    ".contact > .eyebrow",
    ".contact > h2",
    ".contact > .muted",
    ".socials > a",
  ];

  const elements = document.querySelectorAll(selectors.join(","));

  elements.forEach((element) => {
    element.classList.add("scroll-reveal");

    const group = element.parentElement;

    const staggered =
      group &&
      group.matches(
        ".two-cards, .skill-grid, .project-grid, .resume-grid, .socials",
      );

    if (staggered) {
      const index = Array.from(group.children).indexOf(element);

      element.style.setProperty(
        "--reveal-delay",
        `${Math.min(index, 4) * 75}ms`,
      );
    }
  });

  const observer = new IntersectionObserver(
    (entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");
        currentObserver.unobserve(entry.target);
      });
    },
    {
      threshold: 0.12,
      rootMargin: "0px 0px -45px 0px",
    },
  );

  elements.forEach((element) => observer.observe(element));
}

initScrollReveal();

const hero = document.querySelector(".hero-luxe");
const modeButtons = document.querySelectorAll(".switch-btn");

if (hero) {
  const cursorLayers = [
    {
      element: hero.querySelector(".hero-left"),
      x: -22,
      y: -12,
    },
    {
      element: hero.querySelector(".hero-right"),
      x: 22,
      y: 12,
    },
    {
      element: hero.querySelector(".hero-portrait"),
      x: 13,
      y: 9,
    },
    {
      element: hero.querySelector(".hero-outline"),
      x: -30,
      y: -18,
    },
    {
      element: hero.querySelector(".portrait-ring"),
      x: 20,
      y: 14,
    },
  ]
.filter((layer) => layer.element);

  if (window.matchMedia("(pointer: fine)").matches) {
    hero.addEventListener("pointermove", (event) => {
      const rect = hero.getBoundingClientRect();

      const mouseX = (event.clientX - rect.left) / rect.width - 0.5;

      const mouseY = (event.clientY - rect.top) / rect.height - 0.5;

      cursorLayers.forEach((layer) => {
        const moveX = mouseX * layer.x;
        const moveY = mouseY * layer.y;

        layer.element.style.translate = `${moveX}px ${moveY}px`;
      });
    });

    hero.addEventListener("pointerleave", () => {
      cursorLayers.forEach((layer) => {
        layer.element.style.translate = "0px 0px";
      });
    });
  }
}

function setHeroMode(mode) {
  if (!hero) return;

  hero.dataset.mode = mode;

  const outline = document.getElementById("heroOutline");

  if (outline) {
    outline.textContent = mode === "creative" ? "CREATIVE" : "ASPIRING";
  }

  modeButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.mode === mode);
  });
}

modeButtons.forEach((button) => {
  button.addEventListener("click", () => setHeroMode(button.dataset.mode));
});

const canvas = document.getElementById("particles");
const ctx = canvas?.getContext("2d");

if (canvas && ctx) {
  let particles = [];
  let width = 0;
  let height = 0;
  let animationId;

  function resizeCanvas() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    width = canvas.clientWidth;
    height = canvas.clientHeight;

    canvas.width = width * dpr;
    canvas.height = height * dpr;

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const count = Math.min(
      Math.max(Math.floor((width * height) / 6500), 65),
      170,
    );

    particles = [];

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.7,
        vy: (Math.random() - 0.5) * 0.7,
        radius: Math.random() * 2 + 1,
      });
    }
  }

  function animateParticles() {
    ctx.clearRect(0, 0, width, height);

    const creative = hero?.dataset.mode === "creative";

    const color = creative ? "255, 1, 1" : "0, 201, 232";

    particles.forEach((p) => {
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0 || p.x > width) p.vx *= -1;
      if (p.y < 0 || p.y > height) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);

      ctx.fillStyle = `rgba(${color}, 0.9)`;
      ctx.shadowBlur = 15;
      ctx.shadowColor = `rgba(${color}, 0.8)`;
      ctx.fill();
      ctx.shadowBlur = 0;
    });

    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i];
        const b = particles[j];

        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 125) {
          const opacity = 1 - distance / 125;

          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);

          ctx.strokeStyle = `rgba(${color}, ${opacity * 0.22})`;

          ctx.lineWidth = 0.7;
          ctx.stroke();
        }
      }
    }

    animationId = requestAnimationFrame(animateParticles);
  }

  window.addEventListener("resize", resizeCanvas);

  resizeCanvas();
  animateParticles();
}

function initAboutGlow() {
  const cards = document.querySelectorAll(".about .info-card");

  console.log("About Glow:", cards.length, "cards");

  cards.forEach((card) => {
    if (card.querySelector(".about-glow-canvas")) return;

    const canvas = document.createElement("canvas");
    canvas.className = "about-glow-canvas";
    canvas.setAttribute("aria-hidden", "true");

    card.prepend(canvas);

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const isRed = card.classList.contains("red-line");

    const color = isRed ? "255, 1, 1" : "0, 201, 232";

    let width = 0;
    let height = 0;
    let angle = 0;
    let mouse = null;

    function resize() {
      const rect = card.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);

      width = rect.width;
      height = rect.height;

      canvas.width = Math.round(width * dpr);
      canvas.height = Math.round(height * dpr);

      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function draw() {
      ctx.clearRect(0, 0, width, height);

      const x = 2;
      const y = 2;
      const w = width - 4;
      const h = height - 4;
      const radius = 26;

      if (mouse) {
        const glow = ctx.createRadialGradient(
          mouse.x,
          mouse.y,
          0,
          mouse.x,
          mouse.y,
          180,
        );

        glow.addColorStop(0, `rgba(${color}, 0.15)`);
        glow.addColorStop(1, `rgba(${color}, 0)`);

        ctx.fillStyle = glow;
        ctx.fillRect(0, 0, width, height);
      }

      ctx.beginPath();
      ctx.roundRect(x, y, w, h, radius);
      ctx.strokeStyle = "rgba(120, 140, 150, 0.22)";
      ctx.lineWidth = 1;
      ctx.stroke();

      const gradient = ctx.createConicGradient(angle, width / 2, height / 2);

      gradient.addColorStop(0, "transparent");
      gradient.addColorStop(0.7, "transparent");
      gradient.addColorStop(0.82, `rgba(${color}, 0.25)`);
      gradient.addColorStop(0.88, `rgba(${color}, 1)`);
      gradient.addColorStop(0.94, `rgba(${color}, 0.25)`);
      gradient.addColorStop(1, "transparent");

      ctx.beginPath();
      ctx.roundRect(x, y, w, h, radius);
      ctx.strokeStyle = gradient;
      ctx.lineWidth = 3;

      ctx.shadowBlur = 18;
      ctx.shadowColor = `rgb(${color})`;
      ctx.stroke();
      ctx.shadowBlur = 0;

      angle += 0.018;

      requestAnimationFrame(draw);
    }

    card.addEventListener("pointermove", (event) => {
      const rect = card.getBoundingClientRect();

      mouse = {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top,
      };
    });

    card.addEventListener("pointerleave", () => {
      mouse = null;
    });

    resize();
    draw();

    if ("ResizeObserver" in window) {
      new ResizeObserver(resize).observe(card);
    } else {
      window.addEventListener("resize", resize);
    }
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAboutGlow);
} else {
  initAboutGlow();
}

(() => {
  const showcase = document.querySelector(".mobile-showcase");

  if (!showcase) return;

  const choices = showcase.querySelectorAll(".mobile-choice");

  let startX = 0;
  let startY = 0;

  function setMobileMode(mode) {
    showcase.dataset.mode = mode;

    choices.forEach((button) => {
      button.classList.toggle("active", button.dataset.mobileMode === mode);
    });
  }

  choices.forEach((button) => {
    button.addEventListener("click", () => {
      setMobileMode(button.dataset.mobileMode);
    });
  });

  showcase.addEventListener(
    "touchstart",
    (event) => {
      startX = event.changedTouches[0].clientX;
      startY = event.changedTouches[0].clientY;
    },
    { passive: true },
  );

  showcase.addEventListener(
    "touchend",
    (event) => {
      const endX = event.changedTouches[0].clientX;
      const endY = event.changedTouches[0].clientY;

      const deltaX = endX - startX;
      const deltaY = endY - startY;

      if (Math.abs(deltaX) < 45 || Math.abs(deltaX) < Math.abs(deltaY)) {
        return;
      }

      if (deltaX < 0) {
        setMobileMode("developer");
      } else {
        setMobileMode("creative");
      }
    },
    { passive: true },
  );
})();