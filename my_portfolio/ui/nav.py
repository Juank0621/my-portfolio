import reflex as rx

def navbar_link(text: str, url: str, is_active: bool = False) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            size="4",
            weight="medium",
            color="gray",
            position="relative",
            padding_bottom="0.5em",
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
                "_after": {
                    "width": "100%",
                },
            },
        ),
        href=url,
        text_decoration="none",
        display="flex",
        align_items="center",
        height="100%",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                # Logo a la izquierda
                rx.box(
                    rx.link(
                        rx.image(src="/logo.png", width="18em", height="auto", border_radius="25%"),
                        href="/",
                    ),
                    width="20%",  # ajusta según el tamaño real de tu logo
                ),

                # Enlaces centrados
                rx.box(
                    rx.hstack(
                        navbar_link("HOME", "/"),
                        navbar_link("ABOUT ME", "/about"),
                        navbar_link("RESUME", "/resume"),
                        navbar_link("CONTACT", "/contact"),
                        spacing="6",
                        justify="center",
                    ),
                    width="60%",  # espacio central para los enlaces
                    justify="center",
                ),

                # Redes sociales a la derecha
                rx.box(
                    rx.hstack(
                        rx.link(
                            rx.image(
                                src="/Github.svg",
                                width="2.5em",
                                height="2.5em",
                                filter="grayscale(100%)",
                                _hover={"filter": "none"},
                            ),
                            href="https://github.com/Juank0621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.image(
                                src="/LinkedIn.svg",
                                width="2em",
                                height="2em",
                                filter="grayscale(100%)",
                                _hover={"filter": "none"},
                            ),
                            href="https://www.linkedin.com/in/juancarlosgarzon",
                            is_external=True,
                        ),
                        rx.link(
                            rx.image(
                                src="/Instagram.svg",
                                width="2em",
                                height="2em",
                                filter="grayscale(100%)",
                                _hover={"filter": "none"},
                            ),
                            href="https://www.instagram.com/juank920621",
                            is_external=True,
                        ),
                        spacing="6",
                        justify="end",
                        align_items="center",
                    ),
                    width="20%",  # ancho del bloque derecho
                ),

                align_items="center",
                width="100%",
                padding_x="4em",
            ),
        ),
        bg="rgba(0, 0, 0, 0.6)",
        backdrop_filter="blur(6px)",
        padding="1em",
        width="100%",
        z_index="10",
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.hstack(
            rx.hstack(
                rx.image(src="/icon.png", width="3em", height="auto", border_radius="25%"),
                rx.text(
                    "© 2025 Juan Carlos Garzon. All rights reserved.",
                    size="3",
                    white_space="nowrap",
                    weight="medium",
                    color="gray",
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.link(
                    rx.text("juank920621@gmail.com", size="3", color="gray"),
                    href="/contact",
                    text_decoration="none",
                    _hover={"text_decoration": "none"},
                ),
                rx.link(
                    rx.image(
                        src="/Github.svg",
                        width="2.5em",
                        height="2.5em",
                        filter="grayscale(100%)",
                        _hover={"filter": "none"},
                    ),
                    href="https://github.com/Juank0621",
                    is_external=True,
                ),
                rx.link(
                    rx.image(
                        src="/LinkedIn.svg",
                        width="2em",
                        height="2em",
                        filter="grayscale(100%)",
                        _hover={"filter": "none"},
                    ),
                    href="https://www.linkedin.com/in/juancarlosgarzon",
                    is_external=True,
                ),
                rx.link(
                    rx.image(
                        src="/Instagram.svg",
                        width="2em",
                        height="2em",
                        filter="grayscale(100%)",
                        _hover={"filter": "none"},
                    ),
                    href="https://www.instagram.com/juank920621",
                    is_external=True,
                ),
                spacing="6",
                align_items="center",
            ),
            spacing="6",
            align="center",
            justify="between",
            padding_x="5em",
            width="100%",
        ),
        padding_y="1.5em",
        min_height="6em",
        max_height="8em",
        width="100%",
        bg="rgba(0, 0, 0, 0.6)",
        backdrop_filter="blur(6px)",
    )