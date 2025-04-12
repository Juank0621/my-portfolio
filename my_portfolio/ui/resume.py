import reflex as rx

def resume_content() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("My Resume", size="7", color="white", margin_bottom="1.5em"),
            rx.box(
                rx.html('''
                    <iframe 
                        src="/Juan_Carlos_Garzon_Resume.pdf" 
                        width="100%" 
                        height="900px" 
                        style="border: none;"
                    ></iframe>
                '''),
                width="100%",
                max_width="1200px",
            ),
            rx.link(
                rx.button(
                    "Download",
                    bg="gray",
                    color="white",
                    border_radius="xl",
                    padding="1em 2.5em",
                    font_size="1.2em",
                    _hover={
                        "bg": "#2e144f",
                        "transform": "scale(1.05)",
                    },
                    transition="all 0.3s ease-in-out",
                ),
                href="/Juan_Carlos_Garzon_Resume.pdf",
                is_external=True,
                download=True,
                margin_top="2em",
            ),
            spacing="1",
            align="center",
            width="100%",
            padding="1em",
        ),
        width="100%",
    )
