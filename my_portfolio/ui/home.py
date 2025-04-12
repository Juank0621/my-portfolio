import reflex as rx

def home_section() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Hi There!", font_size="2em", color="white", class_name="slide-in-left"),
                        rx.text("👋", font_size="2em", animation="wave 2s infinite"),
                        rx.text("I'm", font_size="2em", color="white", class_name="slide-in-left"),
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
                            class_name="slide-in-left",
                            _hover={"color": "gray"},
                        ),
                        href="#about",
                        text_decoration="none",
                        _hover={"text_decoration": "none"},
                    ),
                    rx.box(height="2em"),
                    rx.html(
                        '<span id="typed-role" style="font-size: 2em; font-weight: bold; color: #7c3aed; font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif;"></span>'
                    ),
                    rx.box(height="0.3em"),
                    rx.text(
                        "2 Years of Experience",
                        font_size="1.5em",
                        color="white",
                        text_align="left",
                        class_name="slide-in-left",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.flex(
                                rx.image(
                                    src="/GitHub.svg",
                                    width="2.8em",
                                    height="2.8em",
                                    _hover={"filter": "grayscale(100%)"},
                                ),
                                align="center",
                                justify="center",
                            ),
                            href="https://github.com/Juank0621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.flex(
                                rx.image(src="/LinkedIn.svg", width="2.5em", height="2.5em", _hover={"filter": "grayscale(100%)"}),
                                align="center",
                                justify="center",
                            ),
                            href="https://www.linkedin.com/in/juancarlosgarzon",
                            is_external=True,
                        ),
                        rx.link(
                            rx.flex(
                                rx.image(src="/Instagram.svg", width="2.5em", height="2.5em", _hover={"filter": "grayscale(100%)"}),
                                align="center",
                                justify="center",
                            ),
                            href="https://www.instagram.com/juank920621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.flex(
                                rx.image(src="/Kaggle.svg", width="2.5em", height="2.5em", _hover={"filter": "grayscale(100%)"}),
                                align="center",
                                justify="center",
                            ),
                            href="https://www.kaggle.com/juancarlosgarzon",
                            is_external=True,
                        ),
                        spacing="5",
                        align="center",
                        padding_top="1em",
                        class_name="slide-in-left",
                    ),
                    align="start",
                    padding_left="5em",
                ),
                width="100%",
            ),
            height="100%",
            align_items="center",
            justify="center",
        ),
        id="home",
        background_image="url('/wallpaper.jpg')",
        bg_size="cover",
        bg_position="center",
        bg_repeat="no-repeat",
        height="100vh",
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
