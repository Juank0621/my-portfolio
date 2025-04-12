import reflex as rx

def contact_content() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Contact", size="8", color="white", text_align="center"),
                rx.text(
                    "Feel free to reach out to me",
                    font_size="1.2em",
                    color="gray",
                    margin_top="0.5em",
                    margin_bottom="2em",
                    text_align="center"
                ),
                rx.hstack(
                    rx.box(
                        rx.flex(
                            rx.image(src="/envelope.svg", width="3em", filter="invert(1)"),
                            rx.text("contact@juancarlosgarzon.com", color="white", font_size="1em"),
                            spacing="4",
                            align="center",
                            justify="center",
                            width="100%",
                        ),
                        padding="1.5em",
                        bg="linear-gradient(to right, #2e144f, #1f1f2e)",
                        border_radius="15px",
                        box_shadow="lg",
                        width="400px",
                    ),
                    rx.box(
                        rx.flex(
                            rx.image(src="/telephone.svg", width="3em", filter="invert(1)"),
                            rx.text("+1 (438) 773-4784", color="white", font_size="1em"),
                            spacing="4",
                            align="center",
                            justify="center",
                            width="100%",
                        ),
                        padding="1.5em",
                        bg="linear-gradient(to right, #2e144f, #1f1f2e)",
                        border_radius="15px",
                        box_shadow="lg",
                        width="400px",
                    ),
                    spacing="3",
                    justify="center",
                    wrap="wrap",
                    width="100%",
                ),
                spacing="4",
                align="center",
                width="100%",
                padding_y="5em",
            ),
            max_width="1000px",
            width="100%",
            padding_bottom="15em",
        ),
        width="100%"
    )
