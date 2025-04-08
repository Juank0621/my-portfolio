import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color="purple"),
        href=url,
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/logo.png",
                        width="3em",  
                        height="auto",
                        border_radius="25%",
                    ),
                    href="/",
                ),
                rx.text(
                    "Juan Garzon",
                    font_size="1.5em",
                    font_weight="bold",
                    color="white",
                    font_family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
                ),
                rx.spacer(),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("Resume", "/resume"),
                    navbar_link("Contact", "/contact"),
                    spacing="6",
                ),
                rx.hstack(
                    rx.link(
                        rx.icon(tag="github", color="purple"),
                        href="https://github.com/Juank0621",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon(tag="linkedin", color="purple"),
                        href="https://www.linkedin.com/in/juancarlosgarzon",
                        is_external=True,
                    ),
                    rx.color_mode.button(bg="purple", color="white"),
                    spacing="4",
                ),
                justify="center",
                align_items="center",
                padding_x="2em",
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
                    rx.heading("Juan Garzon", size="6", weight="bold", color="purple"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30, color="purple")),
                    rx.menu.content(
                        navbar_link("Home", "/"),
                        navbar_link("About", "/about"),
                        navbar_link("Resume", "/resume"),
                        navbar_link("Contact", "/contact"),
                        rx.link(
                            rx.icon(tag="github", color="purple"),
                            href="https://github.com/Juank0621",
                            is_external=True,
                        ),
                        rx.link(
                            rx.icon(tag="linkedin", color="purple"),
                            href="https://www.linkedin.com/in/juancarlosgarzon",
                            is_external=True,
                        ),
                        rx.color_mode.button(color="purple"),
                    ),
                ),
                justify="center",
                align_items="center",
                padding_x="2em",
            ),
        ),
        bg="#000000",
        padding="1em",
        width="100%",
        id="my-main-navbar",
    )

def about_content() -> rx.Component:
    return rx.box(
        rx.heading("About", size="5", weight="bold", color="purple"),
        rx.text("More personal information will be added here later.", color="white"),
    )

def resume_content() -> rx.Component:
    return rx.box(
        rx.heading("Resume", size="5", weight="bold", color="purple"),
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
                    rx.heading("Contact Me", color="purple"),
                    rx.text("Feel free to reach out using the form below.", color="white"),
                ),
                spacing="4"
            ),
            rx.vstack(
                rx.text("Name ", rx.text.span("*", color="purple")),
                rx.input(name="name", required=True, bg="#1f1f1f", color="white"),
            ),
            rx.vstack(
                rx.text("Email ", rx.text.span("*", color="purple")),
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

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_3() -> rx.Component:
    return rx.flex(
        rx.heading(
            "ABOUT US", size="4", weight="bold", as_="h3"
        ),
        footer_item("Our Team", "/#"),
        footer_item("Careers", "/#"),
        footer_item("Contact Us", "/#"),
        footer_item("Privacy Policy", "/#"),
        footer_item("Terms of Service", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%",
    )

def footer_three_columns() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                footer_items_1(),
                footer_items_2(),
                footer_items_3(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2025 Juan Carlos Garzon. All rights reserved.",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    rx.text(
                        "Contact: juank920621@gmail.com",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        color="purple",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                socials(),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
    )


