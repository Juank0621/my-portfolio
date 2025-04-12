import reflex as rx
from .nav import navbar, footer

def base_page(child: rx.Component, hide_navbar: bool = False, on_load: rx.Var = None, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid component", size="6", color="red")

    return rx.box(
        rx.flex(
            rx.vstack(
                navbar() if not hide_navbar else None,
                rx.box(
                    child,
                    padding="0",
                    width="100%",
                    bg="#1c1c1e", 
                    flex="1",
                ),
                footer() if not hide_navbar else None,
                spacing="0",
            ),
            direction="column",
        ),
        on_load=on_load,
        style={"scroll-behavior": "smooth"},
    )

