import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color="purple.300"),  # Texto morado
        href=url,
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="8em",  # Reducir el tamaño del logo
                        height="auto",
                        border_radius="25%",
                    ),
                    href="/",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("Resume", "/resume"),
                    navbar_link("Contact", "/contact"),
                    spacing="6",
                ),
                rx.hstack(
                    rx.link(
                        rx.icon(tag="github", color="purple.400"),  # Ícono morado
                        href="https://github.com/Juank0621",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon(tag="linkedin", color="purple.400"),  # Ícono morado
                        href="https://www.linkedin.com/in/juancarlosgarzon",
                        is_external=True,
                    ),
                    rx.color_mode.button(),  # Botón de cambio de modo
                    spacing="4",  # Espaciado entre los íconos
                ),
                justify="between",  # Cambiar de 'space-between' a 'between'
                align_items="center",
                padding_x="2em",  # Añadir padding horizontal
                id="my-navbar-hstack-desktop",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold", color="purple.300"),  # Texto morado
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30, color="purple.400")),  # Ícono morado
                    rx.menu.content(
                        navbar_link("Home", "/"),
                        navbar_link("About", "/about"),
                        navbar_link("Resume", "/resume"),
                        navbar_link("Contact", "/contact"),
                        rx.link(
                            rx.icon(tag="github", color="purple.400"),  # Ícono morado
                            href="https://github.com/Juank0621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.icon(tag="linkedin", color="purple.400"),  # Ícono morado
                            href="https://www.linkedin.com/in/juancarlosgarzon",
                            is_external=True,
                        ),
                        rx.color_mode.button(),  # Botón de cambio de modo
                    ),
                ),
                justify="between",  # Cambiar de 'space-between' a 'between'
                align_items="center",
                padding_x="2em",  # Añadir padding horizontal
            ),
        ),
        bg="#000000",  # Fondo negro
        padding="1em",
        width="100%",
        id="my-main-navbar",
    )

def about_content() -> rx.Component:
    return rx.box(
        rx.heading("About", size="5", weight="bold", color="purple.300"),
        rx.text("More personal information will be added here later.", color="white"),
    )

def resume_content() -> rx.Component:
    return rx.box(
        rx.heading("Resume", size="5", weight="bold", color="purple.300"),
        rx.html('''
            <iframe src="/Juan_Carlos_Garzon_Resume.pdf" width="100%" height="600px" style="border:none;"></iframe>
        '''),
        color="white"
    )

class FormState(rx.State):
    @rx.event
    def submit(self, form_data):
        return rx.toast(form_data)

def contact_content() -> rx.Component:
    return rx.card(
        rx.form(
            rx.hstack(
                rx.image(src="/envelope.png", width="2.5em"),
                rx.vstack(
                    rx.heading("Contact Me", color="purple.400"),
                    rx.text("Feel free to reach out using the form below.", color="white"),
                ),
                spacing="4"
            ),
            rx.vstack(
                rx.text("Name ", rx.text.span("*", color="purple.500")),
                rx.input(name="name", required=True, bg="#1f1f1f", color="white"),
            ),
            rx.vstack(
                rx.text("Email ", rx.text.span("*", color="purple.500")),
                rx.input(name="email", type="email", required=True, bg="#1f1f1f", color="white"),
            ),
            rx.vstack(
                rx.text("Message"),
                rx.text_area(name="message", bg="#1f1f1f", color="white"),
            ),
            rx.button("Send", type="submit", bg="purple.600", color="white"),
            on_submit=FormState.submit,
        ),
        padding="2em",
        bg="#2a2a2a",
        color="white"
    )


