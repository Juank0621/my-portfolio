import reflex as rx
from rxconfig import config
from .ui.base import base_page
from .ui.about import about_content
from .ui.resume import resume_content
from .ui.contact import contact_content

class State(rx.State):
    label = "My Portfolio"

def index() -> rx.Component:
    return base_page(
        rx.box(
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Hi There!", font_size="2em", color="white"),
                            rx.text("👋", font_size="2em", animation="wave 2s infinite"),
                            spacing="1",
                        ),
                        rx.box(height="1em"),
                        rx.link(
                            rx.heading(
                                "Juan Garzon",
                                size="1",
                                color="white",
                                font_weight="bold",
                                font_family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
                                font_size="5.5em",
                                text_align="left",
                            ),
                            href="/about",
                            text_decoration="none",
                            _hover={"text_decoration": "none"},
                        ),
                        rx.box(height="2em"),  
                        rx.html(
                            '<span id="typed-role" style="font-size: 2em; font-weight: bold; color: purple; font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif;"></span>'
                        ),
                        rx.box(height="1em"),  
                        rx.text(
                            "2 Years of Experience",
                            font_size="1.5em",
                            color="white",
                            text_align="left",
                        ),
                        align="start",
                        padding_left="5em",
                    ),
                    width="50%",
                ),
                rx.box(width="50%"),
                height="100%",
                align_items="center",
            ),
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
            background_image="url('/wallpaper.jpg')",
            bg_size="cover",
            bg_position="center",
            bg_repeat="no-repeat",
            height="calc(100vh - 6em)",
            width="100%",
            padding="0",
            margin="0",
            style={
                "@keyframes wave": {
                    "0%": {"transform": "rotate(0deg)"},
                    "10%": {"transform": "rotate(14deg)"},
                    "20%": {"transform": "rotate(-8deg)"},
                    "30%": {"transform": "rotate(14deg)"},
                    "40%": {"transform": "rotate(-4deg)"},
                    "50%": {"transform": "rotate(10deg)"},
                    "60%": {"transform": "rotate(0deg)"},
                    "100%": {"transform": "rotate(0deg)"},
                }
            },
        )
    )

def about_page() -> rx.Component:
    return base_page(about_content())

def resume_page() -> rx.Component:
    return base_page(resume_content())

def contact_page() -> rx.Component:
    return base_page(contact_content())

app = rx.App()
app.add_page(index, route="/")
app.add_page(about_page, route="/about")
app.add_page(resume_page, route="/resume")
app.add_page(contact_page, route="/contact")
