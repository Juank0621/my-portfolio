import reflex as rx

def navbar_link(text: str, section_id: str, is_active: bool = False) -> rx.Component:
    return rx.text(
        text,
        size="4",
        weight="medium",
        color="white",
        position="relative",
        padding_bottom="0.5em",
        cursor="pointer",
        _after={
            "content": '""',
            "position": "absolute",
            "left": "0",
            "bottom": "0",
            "width": "100%" if is_active else "0%",
            "height": "3px",
            "background": "purple",
            "transition": "width 0.4s ease-in-out",
        },
        _hover={
            "color": "gray",
            "_after": {"width": "100%"},
        },
        transition="all 0.3s ease-in-out",
        on_click=rx.scroll_to(section_id),
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.box(
                    rx.link(
                        rx.image(
                            src="/logo.png",
                            width="18em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href="/",
                    ),
                    width="20%",
                ),
                rx.box(width="20%"),
                rx.box(
                    rx.hstack(
                        navbar_link("HOME", "home"),
                        navbar_link("ABOUT ME", "about"),
                        navbar_link("RESUME", "resume"),
                        navbar_link("CONTACT", "contact"),
                        spacing="6",
                        justify="end",
                    ),
                    width="60%",
                    justify="end",
                ),
                align_items="center",
                width="100%",
                padding_x="4em",
            ),
        ),
        bg="rgba(0, 0, 0, 0.2)",
        backdrop_filter="blur(6px)",
        padding="1em",
        width="100%",
        z_index="999",
        position="fixed",
        top="0",
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.flex(
            rx.box(
                rx.hstack(
                    rx.image(
                        src="/icon.png",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2025 Juan Carlos Garzon. All rights reserved.",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color="white",
                    ),
                    spacing="2",
                    align="center",
                ),
                width=["100%", "33%"],
                justify="start",
                align="center",
                padding_left="5em",
            ),
            rx.box(
                rx.center(
                    rx.text(
                        "contact@juancarlosgarzon.com",
                        size="5",
                        color="white",
                    )
                ),
                width=["100%", "33%"],
                justify="center",
                align="center",
            ),
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/GitHub.svg",
                            width="2em",
                            height="2em",
                            _hover={"filter": "grayscale(100%)"},
                        ),
                        href="https://github.com/Juank0621",
                        is_external=True,
                    ),
                    rx.link(
                        rx.image(
                            src="/LinkedIn.svg",
                            width="1.8em",
                            height="1.8em",
                            _hover={"filter": "grayscale(100%)"},
                            filter="none",
                        ),
                        href="https://www.linkedin.com/in/juancarlosgarzon",
                        is_external=True,
                    ),
                    rx.link(
                        rx.image(
                            src="/Instagram.svg",
                            width="1.8em",
                            height="1.8em",
                            _hover={"filter": "grayscale(100%)"},
                            filter="none",
                        ),
                        href="https://www.instagram.com/juank920621",
                        is_external=True,
                    ),
                    rx.link(
                        rx.image(
                            src="/Kaggle.svg",
                            width="1.8em",
                            height="1.8em",
                            _hover={"filter": "grayscale(100%)"},
                            filter="none",
                        ),
                        href="https://www.kaggle.com/juancarlosgarzon",
                        is_external=True,
                    ),
                    spacing="4",
                    justify="end",
                    align="center",
                ),
                width=["100%", "33%"],
                justify="end",
                align="center",
                padding_right="7em",
            ),
            direction="row",
            wrap="wrap",
            justify="between",
            align="center",
            width="100%",
            padding_x="0",
        ),
        padding_y="1.5em",
        width="100%",
        bg="rgba(0, 0, 0, 0.01)",
        backdrop_filter="blur(6px)",
    )