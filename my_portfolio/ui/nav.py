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
                            cursor="pointer",
                            on_click=rx.scroll_to("home"),
                        ),
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
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.box(
                    rx.link(
                        rx.image(
                            src="/logo.png",
                            width="10em",
                            height="auto",
                            border_radius="25%",
                            cursor="pointer",
                            on_click=rx.scroll_to("home"),
                        ),
                    ),
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30),
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_select=rx.scroll_to("home")),
                        rx.menu.item("About Me", on_select=rx.scroll_to("about")),
                        rx.menu.item("Resume", on_select=rx.scroll_to("resume")),
                        rx.menu.item("Contact", on_select=rx.scroll_to("contact")),
                    ),
                ),
                justify="between",
                align_items="center",
                width="100%",
                padding_x="1em",
            )
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
        rx.fragment(
            rx.desktop_only(
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
                            spacing="5",
                            align="center",
                        ),
                        width=["100%", "33%"],
                        justify="start",
                        align="center",
                        padding_left="5em",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.link(
                                rx.image(
                                    src="/GitHub2.svg",
                                    width="2em",
                                    height="2em",
                                    style={"filter": "invert(1)"}, 
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
                        padding_right="10em",
                    ),
                    direction="row",
                    wrap="wrap",
                    justify="between",
                    align="center",
                    width="100%",
                    padding_x="0",
                )
            ),
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="/icon.png",
                            width="2em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.text(
                            "© 2025 Juan Carlos Garzon. All rights reserved.",
                            size="2",
                            weight="medium",
                            color="white",
                            text_align="center",
                        ),
                        spacing="2",
                        align="center",
                        justify="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.link(
                            rx.image(src="/GitHub2.svg", width="1.5em", height="1.5em",
                                     style={"filter": "invert(1)"}, 
                                    _hover={"filter": "grayscale(100%)"},        
                            ),
                            href="https://github.com/Juank0621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.image(src="/LinkedIn.svg", width="1.4em", height="1.4em"),
                            href="https://www.linkedin.com/in/juancarlosgarzon",
                            is_external=True,
                        ),
                        rx.link(
                            rx.image(src="/Instagram.svg", width="1.4em", height="1.4em"),
                            href="https://www.instagram.com/juank920621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.image(src="/Kaggle.svg", width="1.4em", height="1.4em"),
                            href="https://www.kaggle.com/juancarlosgarzon",
                            is_external=True,
                        ),
                        spacing="3",
                        justify="center",
                        align="center",
                        wrap="wrap",
                        padding_top="0.5em",
                    ),
                    spacing="2",
                    align="center",
                    width="100%",
                )
            ),
        ),
        padding_y="1.5em",
        width="100%",
        bg="rgba(0, 0, 0, 1)",  
        backdrop_filter="blur(6px)",
    )