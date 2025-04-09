import reflex as rx

class FormState(rx.State):
    @rx.event
    def submit(self, form_data):
        return rx.toast("Form submitted!")

def contact_content() -> rx.Component:
    return rx.flex(
        rx.center(
            rx.card(
                rx.form(
                    rx.hstack(
                        rx.image(src="/envelope.png", width="2em"),
                        rx.vstack(
                            rx.heading("Contact Me", size="5", color="white"),
                            rx.text("Feel free to reach out using the form below.", color="gray"),
                        ),
                        spacing="4",
                        align="center",
                    ),
                    rx.spacer(height="1em"),
                    rx.vstack(
                        rx.text("Name ", rx.text.span("*", color="red")),
                        rx.input(name="name", required=True, width="100%", bg="#1f1f1f", color="white"),
                    ),
                    rx.spacer(height="1em"),
                    rx.vstack(
                        rx.text("Email ", rx.text.span("*", color="red")),
                        rx.input(name="email", type="email", required=True, width="100%", bg="#1f1f1f", color="white"),
                    ),
                    rx.spacer(height="1em"),
                    rx.vstack(
                        rx.text("Message"),
                        rx.text_area(name="message", width="100%", bg="#1f1f1f", color="white", min_height="150px"),
                    ),
                    rx.spacer(height="1em"),
                    rx.button("Send", type="submit", bg="#2e144f", color="white", width="100%", margin_top="1em"),
                    on_submit=FormState.submit,
                    spacing="4",
                    width="100%",
                ),
                width="100%",
                max_width="600px",
                padding="2em",
                bg="linear-gradient(to right, #1f1f2e, #2e144f)",
                box_shadow="lg",
                border_radius="lg",
            ),
            width="100%",
        ),
        height="100%",
        align_items="center",
        justify_content="center",
        padding_y="6em",
    )