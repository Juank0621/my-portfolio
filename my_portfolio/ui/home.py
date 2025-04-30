import reflex as rx

def home_section() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Hi There!", font_size="2em", color="white", class_name="slide-in-left"),
                            rx.text("👋", font_size="2em", class_name="wave-hand"),
                            rx.text("I'm", font_size="2em", color="white", class_name="slide-in-left"),
                            spacing="1",
                            width="100%",
                            margin_bottom="2em",
                        ),
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
                        rx.text(
                            "2 Years of Experience",
                            font_size="1.5em",
                            color="white",
                            text_align="left",
                            class_name="slide-in-left",
                            margin_top="0.5em",
                        ),
                        rx.hstack(
                            *[
                                rx.link(
                                    rx.flex(
                                        rx.image(src=icon, width="2.5em", height="2.5em",),
                                        _hover={"filter": "grayscale(100%)"},
                                        align="center",
                                        justify="center",
                                    ),
                                    href=link,
                                    is_external=True,
                                )
                                for icon, link in [
                                    ("/GitHub.svg", "https://github.com/Juank0621"),
                                    ("/LinkedIn.svg", "https://www.linkedin.com/in/juancarlosgarzon"),
                                    ("/Instagram.svg", "https://www.instagram.com/juank920621"),
                                    ("/Kaggle.svg", "https://www.kaggle.com/juancarlosgarzon"),
                                ]
                            ],
                            spacing="5",
                            align="center",
                            margin_top="0.5em",
                            class_name="slide-in-left",
                        ),
                        align="start",
                        padding_left="5em",
                    ),
                    width="100%",
                ),
                height="100vh",
                align_items="center",
                justify="center",
                width="100%",
            )
        ),

        rx.mobile_and_tablet(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text("Hi There!", font_size="1.3em", color="white"),
                        rx.text("👋", font_size="1.3em", class_name="wave-hand"),
                        rx.text("I'm", font_size="1.3em", color="white"),
                        spacing="1",
                        width="100%",
                        justify="start",
                        margin_bottom="0.5em",
                    ),
                    rx.heading(
                        "Juan Garzon",
                        size="3",
                        color="white",
                        font_weight="bold",
                        font_size="2.5em",
                        text_align="left",
                        _hover={"color": "gray"},
                        width="100%",
                    ),
                    rx.text(
                        "Computer Vision Engineer",
                        font_size="1.2em",
                        font_weight="bold",
                        color="#7c3aed",
                        width="100%",
                        margin_top="0.5em",
                    ),
                    rx.text(
                        "2 Years of Experience",
                        font_size="1em",
                        color="white",
                        text_align="left",
                        width="100%",
                    ),
                    rx.hstack(
                        *[
                            rx.link(
                                rx.image(src=icon, width="1.6em", height="1.6em",),
                                href=link,
                                is_external=True,
                            )
                            for icon, link in [
                                ("/GitHub.svg", "https://github.com/Juank0621"),
                                ("/LinkedIn.svg", "https://www.linkedin.com/in/juancarlosgarzon"),
                                ("/Instagram.svg", "https://www.instagram.com/juank920621"),
                                ("/Kaggle.svg", "https://www.kaggle.com/juancarlosgarzon"),
                            ]
                        ],
                        spacing="3",
                        justify="start",
                        align="center",
                        wrap="wrap",
                        width="100%",
                    ),
                    spacing="2",
                    align="start",
                    justify="start",
                    padding_x="2em",
                    padding_top="14em",
                    width="100%",
                ),
                width="100%",
                height="auto",
                bg="transparent",
            )
        ),

        id="home",
        background_image=rx.breakpoints(initial="none", lg="url('/wallpaper.jpg')"),
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
            },
            ".wave-hand": {
                "display": "inline-block",
                "animation": "wave 2s infinite",
                "transform-origin": "70% 70%",
            },
        },
    )