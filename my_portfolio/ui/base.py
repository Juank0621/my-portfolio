import reflex as rx
from .nav import navbar, footer

def base_page(child: rx.Component, hide_navbar: bool = False, on_load: rx.Var = None, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid component", size="6", color="red")

    if hide_navbar:
        return rx.container(
            child,
            #rx.logo(),
            rx.color_mode.button(position="bottom-left"),
        )

    return rx.box(
        rx.flex(
            rx.vstack(
                navbar(),
                rx.box(
                    child,
                    padding="1em",
                    width="100%",
                    bg="linear-gradient(to right, #1a1a1a, #2a2a2a)",
                    flex="1",
                ),
                footer(),
                spacing="0",
            ),
            direction="column",
            height="100vh",
        ),
        on_load=on_load,
    )