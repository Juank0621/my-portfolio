import reflex as rx
from rxconfig import config
from .ui.base import base_page
from .ui.about import about_content
from .ui.resume import resume_content
from .ui.contact import contact_content
from .ui.home import home_section

def my_portfolio() -> rx.Component:
    return base_page(
        rx.box(
            rx.vstack(
                # HOME SECTION
                home_section(),

                # Typed.js para efecto de escritura
                rx.script(src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"),
                rx.script(
                    """
                    setTimeout(function () {
                        if (window.Typed) {
                            new Typed("#typed-role", {
                                strings: [
                                    "Machine Learning Engineer",
                                    "Computer Vision Engineer",
                                    "AI Developer",
                                    "Data Scientist"
                                ],
                                typeSpeed: 80,
                                backSpeed: 50,
                                loop: true,
                                showCursor: true,
                                cursorChar: "|"
                            });
                        }
                    }, 500);
                    """
                ),

                # Script de animaciones para todas las secciones
                rx.script(
                    """
                    if (!window._observerSetupDone) {
                        window._observerSetupDone = true;

                        // Establece el dataset con la clase original
                        document.querySelectorAll('.slide-in-left').forEach(el => el.dataset.animateClass = 'slide-in-left');
                        document.querySelectorAll('.slide-in-right').forEach(el => el.dataset.animateClass = 'slide-in-right');
                        document.querySelectorAll('.slide-in-bottom').forEach(el => el.dataset.animateClass = 'slide-in-bottom');

                        const observer = new IntersectionObserver((entries) => {
                            entries.forEach(entry => {
                                if (entry.isIntersecting) {
                                    entry.target.querySelectorAll('[data-animate-class]').forEach(el => {
                                        const animateClass = el.dataset.animateClass;
                                        if (animateClass) {
                                            el.classList.remove(animateClass);
                                            void el.offsetWidth;
                                            el.classList.add(animateClass);
                                        }
                                    });
                                }
                            });
                        }, { threshold: 0.4 });

                        ['home', 'about', 'resume', 'contact'].forEach(id => {
                            const section = document.getElementById(id);
                            if (section) observer.observe(section);
                        });
                    }
                    """
                ),

                # ABOUT SECTION
                rx.center(
                    rx.box(
                        about_content(),
                        max_width="1500px",
                        width="100%",
                        padding_top="5em",
                    ),
                    id="about",
                    width="100%",
                ),

                # RESUME SECTION
                rx.center(
                    rx.box(
                        resume_content(),
                        max_width="1200px",
                        width="100%",
                        padding_top="5em",
                    ),
                    id="resume",
                    width="100%",
                ),

                # CONTACT SECTION
                rx.center(
                    rx.box(
                        contact_content(),
                        max_width="1200px",
                        width="100%",
                        padding_top="5em",
                    ),
                    id="contact",
                    width="100%",
                ),
            ),
            width="100%",
        )
    )

app = rx.App(stylesheets=["/style.css"])
app.add_page(my_portfolio, route="/")
