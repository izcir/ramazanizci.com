(function() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    if (savedTheme === 'dark' && !document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.add('dark');
    }
})();

class ThemeManager {
    constructor() {
        this.initTheme();
        this.bindEvents();
        this.ensureVisibility();
    }    initTheme() {
        const html = document.documentElement;
        const savedTheme = localStorage.getItem('theme') || 'dark';
        const isDark = savedTheme === 'dark';

        if (isDark && !html.classList.contains('dark')) {
            html.classList.add('dark');
        } else if (!isDark && html.classList.contains('dark')) {
            html.classList.remove('dark');
        }

        const sunIcon = document.getElementById('sun-icon');
        const moonIcon = document.getElementById('moon-icon');

        if (sunIcon && moonIcon) {
            if (isDark) {
                sunIcon.classList.add('hidden');
                moonIcon.classList.remove('hidden');
            } else {
                sunIcon.classList.remove('hidden');
                moonIcon.classList.add('hidden');
            }
        }
    }

    ensureVisibility() {
    }

    toggleTheme() {
        const html = document.documentElement;
        const isDark = html.classList.contains('dark');

        if (isDark) {
            html.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        } else {
            html.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        }

        this.initTheme();
    }

    bindEvents() {
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }
}

class TypingEffect {
    constructor(element, texts, speed = 100) {
        this.element = element;
        this.texts = texts;
        this.speed = speed;
        this.textIndex = 0;
        this.charIndex = 0;
        this.isDeleting = false;

        if (this.element) {
            this.type();
        }
    }

    type() {
        const currentText = this.texts[this.textIndex];

        if (this.isDeleting) {
            this.element.textContent = currentText.substring(0, this.charIndex - 1);
            this.charIndex--;
        } else {
            this.element.textContent = currentText.substring(0, this.charIndex + 1);
            this.charIndex++;
        }

        let typeSpeed = this.speed;

        if (this.isDeleting) {
            typeSpeed /= 2;
        }

        if (!this.isDeleting && this.charIndex === currentText.length) {
            typeSpeed = 2000;
            this.isDeleting = true;
        } else if (this.isDeleting && this.charIndex === 0) {
            this.isDeleting = false;
            this.textIndex = (this.textIndex + 1) % this.texts.length;
            typeSpeed = 500;
        }

        setTimeout(() => this.type(), typeSpeed);
    }
}

class CounterAnimation {
    constructor() {
        this.initCounters();
    }

    initCounters() {
        const counters = document.querySelectorAll('.stat-number[data-count]');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            observer.observe(counter);
        });
    }

    animateCounter(element) {
        const target = parseInt(element.dataset.count);
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                element.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        };

        updateCounter();
    }
}

class SmoothScroll {
    constructor() {
        this.bindEvents();
    }

    bindEvents() {
        document.querySelectorAll('a[href^="#"]:not([href="#about"]):not([href="#projects"]):not([href="#skills"]):not([href="#contact"])').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = anchor.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }

                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu) {
                    mobileMenu.classList.add('hidden');
                }
            });
        });
    }
}

class MobileMenu {
    constructor() {
        this.bindEvents();
    }

    bindEvents() {
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        if (mobileMenuButton && mobileMenu) {
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });

            document.addEventListener('click', (e) => {
                if (!mobileMenuButton.contains(e.target) && !mobileMenu.contains(e.target)) {
                    mobileMenu.classList.add('hidden');
                }
            });
        }
    }
}

class NavbarScroll {
    constructor() {
        this.bindEvents();
    }

    bindEvents() {
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('nav');
            if (navbar) {
                if (window.scrollY > 100) {
                    navbar.classList.add('shadow-lg');
                } else {
                    navbar.classList.remove('shadow-lg');
                }
            }
        });
    }
}

class AnimationObserver {
    constructor() {
        this.initObserver();
    }

    initObserver() {
        const options = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-slide-up');
                }
            });
        }, options);

        document.querySelectorAll('.card-hover, .skill-card, .project-card').forEach(el => {
            observer.observe(el);
        });
    }
}

class ContactForm {
    constructor() {
        this.bindEvents();
    }

    bindEvents() {
        const form = document.querySelector('form[action*="contact"]');
        if (form) {
            form.addEventListener('submit', (e) => {
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Gönderiliyor...';
                    submitBtn.disabled = true;
                }
            });
        }
    }
}

class LazyLoader {
    constructor() {
        this.initLazyLoading();
    }

    initLazyLoading() {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

class ScrollProgress {
    constructor() {
        this.createProgressBar();
        this.bindEvents();
    }

    createProgressBar() {
        const progressBar = document.createElement('div');
        progressBar.className = 'fixed top-0 left-0 h-1 bg-gradient-to-r from-blue-500 to-purple-600 transition-all duration-300 z-50';
        progressBar.id = 'scroll-progress';
        document.body.prepend(progressBar);
    }

    bindEvents() {
        window.addEventListener('scroll', () => {
            const progressBar = document.getElementById('scroll-progress');
            if (progressBar) {
                const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
                progressBar.style.width = `${scrollPercent}%`;
            }
        });
    }
}

class ClipboardManager {
    static copy(text) {
        navigator.clipboard.writeText(text).then(() => {
            this.showToast('Kopyalandı!');
        }).catch(() => {
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showToast('Kopyalandı!');
        });
    }

    static showToast(message) {
        const toast = document.createElement('div');
        toast.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-4 py-2 rounded-lg shadow-lg z-50 transition-all duration-300';
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(toast);
            }, 300);
        }, 2000);
    }
}

class KeyboardShortcuts {
    constructor() {
        this.bindEvents();
    }

    bindEvents() {
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                const themeManager = new ThemeManager();
                themeManager.toggleTheme();
            }

            if (e.key === 'Escape') {
                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu) {
                    mobileMenu.classList.add('hidden');
                }
            }
        });
    }
}

class HeroAnimationOptimizer {
    constructor() {
        this.initHeroAnimations();
        this.optimizeFloatingShapes();
    }

    initHeroAnimations() {
        const heroContent = document.querySelector('.hero-content');

        if (heroContent) {
        }
    }

    optimizeFloatingShapes() {
        const shapes = document.querySelectorAll('.shape');
        const floatingShapes = document.querySelector('.floating-shapes');

        if (floatingShapes && shapes.length > 0) {
            floatingShapes.style.opacity = '0';

            setTimeout(() => {
                floatingShapes.style.transition = 'opacity 1s ease-out';
                floatingShapes.style.opacity = '1';

                shapes.forEach((shape, index) => {
                    shape.style.animationDelay = `${index * 0.3}s`;
                });
            }, 500);
        }
    }
}

class ProjectCardEnhancer {
    constructor() {
        this.initProjectCards();
    }

    initProjectCards() {
        const projectCards = document.querySelectorAll('.project-card-enhanced');

        projectCards.forEach(card => {
            this.addHoverEffects(card);
            this.addClickEffects(card);
        });
    }

    addHoverEffects(card) {
        let hoverTimeout;

        card.addEventListener('mouseenter', () => {
            clearTimeout(hoverTimeout);
            card.style.transform = 'translateY(-8px) scale(1.02)';
        });

        card.addEventListener('mouseleave', () => {
            hoverTimeout = setTimeout(() => {
                card.style.transform = 'translateY(0) scale(1)';
            }, 100);
        });
    }

    addClickEffects(card) {
        card.addEventListener('click', (e) => {
            if (e.target.closest('a')) return;
              const detailLink = card.querySelector('a[href*="proje/"]');
            if (detailLink) {
                detailLink.click();
            }
        });
    }
}

class LoadingOptimizer {
    constructor() {
        this.optimizeInitialLoad();
        this.addLoadingStates();
    }

    optimizeInitialLoad() {
        document.body.style.visibility = 'hidden';

        window.addEventListener('load', () => {
            document.body.style.visibility = 'visible';
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease-out';

            requestAnimationFrame(() => {
                document.body.style.opacity = '1';
            });
        });
    }

    addLoadingStates() {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            if (!img.complete) {
                img.style.opacity = '0';
                img.addEventListener('load', () => {
                    img.style.transition = 'opacity 0.3s ease-out';
                    img.style.opacity = '1';
                });
            }
        });
    }
}

class ReadMoreToggle {
    constructor() {
        this.init();
    }

    init() {
        const readMoreBtn = document.getElementById('read-more-btn');
        const fullText = document.getElementById('full-text');

        if (readMoreBtn && fullText) {
            readMoreBtn.addEventListener('click', () => {
                const isHidden = fullText.classList.contains('hidden');

                if (isHidden) {
                    fullText.classList.remove('hidden');
                    readMoreBtn.innerHTML = 'Küçült <i class="fas fa-chevron-up ml-1"></i>';
                } else {
                    fullText.classList.add('hidden');
                    readMoreBtn.innerHTML = 'Devamını oku <i class="fas fa-chevron-down ml-1"></i>';
                }
            });
        }
    }
}

class SkillProgressBars {
    constructor() {
        this.init();
    }

    init() {
        const progressBars = document.querySelectorAll('.progress-bar');

        progressBars.forEach(bar => {
            const level = bar.getAttribute('data-level');
            let width = '50%';

            switch(level) {
                case 'beginner':
                    width = '50%';
                    break;
                case 'intermediate':
                    width = '70%';
                    break;
                case 'advanced':
                    width = '85%';
                    break;
                case 'expert':
                    width = '95%';
                    break;
            }

            setTimeout(() => {
                bar.style.width = width;
            }, 500);
        });
    }
}

class NavigationHandler {
    constructor() {
        this.init();
    }

    init() {
        this.updateNavigationLinks();
        this.bindEvents();
    }

    updateNavigationLinks() {
        const currentPath = window.location.pathname;
        const isHomePage = currentPath === '/' || currentPath === '';

        const navSections = ['#about', '#projects', '#skills', '#contact'];

        navSections.forEach(section => {
            const desktopLink = document.querySelector(`a[href="${section}"]`);
            if (desktopLink) {
                if (!isHomePage) {
                    desktopLink.href = `/${section}`;
                    desktopLink.addEventListener('click', (e) => {
                        e.preventDefault();
                        this.navigateToHomeWithSection(section);
                    });
                } else {
                    desktopLink.href = section;
                }
            }
        });

        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenu) {
            navSections.forEach(section => {
                const mobileLink = mobileMenu.querySelector(`a[href="${section}"]`);
                if (mobileLink) {
                    if (!isHomePage) {
                        mobileLink.href = `/${section}`;
                        mobileLink.addEventListener('click', (e) => {
                            e.preventDefault();
                            this.navigateToHomeWithSection(section);
                        });
                    } else {
                        mobileLink.href = section;
                    }
                }
            });
        }
    }

    navigateToHomeWithSection(section) {
        sessionStorage.setItem('scrollTarget', section);

        window.location.href = '/';
    }

    scrollToSection(section) {
        const targetElement = document.querySelector(section);
        if (targetElement) {
            const offsetTop = targetElement.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    }

    bindEvents() {
        window.addEventListener('load', () => {
            const scrollTarget = sessionStorage.getItem('scrollTarget');
            if (scrollTarget) {
                setTimeout(() => {
                    this.scrollToSection(scrollTarget);
                    sessionStorage.removeItem('scrollTarget');
                }, 100);
            }
        });

        window.addEventListener('popstate', () => {
            this.updateNavigationLinks();
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.documentElement.classList.add('loaded');

    new ThemeManager();
    new SmoothScroll();
    new MobileMenu();
    new NavbarScroll();
    new AnimationObserver();
    new ContactForm();
    new LazyLoader();
    new KeyboardShortcuts();
    new LoadingOptimizer();
    new ReadMoreToggle();
    new SkillProgressBars();
    new NavigationHandler();

    document.querySelectorAll('[data-copy]').forEach(element => {
        element.addEventListener('click', () => {
            ClipboardManager.copy(element.dataset.copy);
        });
    });

    const shapes = document.querySelectorAll('.shape');
    shapes.forEach((shape, index) => {
        shape.style.animationDelay = `${index * 0.5}s`;
    });

    console.log('🚀 Ramazan İzci Portfolio initialized successfully!');
});

if ('performance' in window) {
    window.addEventListener('load', () => {
        const loadTime = performance.now();
        console.log(`⚡ Page loaded in ${Math.round(loadTime)}ms`);
    });
}

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

const navigationHandler = new NavigationHandler();
