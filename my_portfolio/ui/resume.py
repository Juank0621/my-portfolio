import reflex as rx

def resume_content() -> rx.Component:
    return rx.center(
        rx.box(
            rx.fragment(
                rx.heading("My Resume", size="7", color="white", margin_bottom="1.5em", text_align="center"),

                rx.desktop_only(
                    rx.box(
                        rx.html('''
                            <iframe 
                                src="/Juan_Carlos_Garzon_Resume.pdf" 
                                width="100%" 
                                style="border: none; height: 1000px;"
                                loading="lazy"
                            ></iframe>
                        '''),
                        width="100%",
                        max_width="1000px",
                        margin="0 auto",
                    )
                ),
                rx.mobile_and_tablet(
                    rx.box(
                        rx.html('''
                            <iframe 
                                src="/Juan_Carlos_Garzon_Resume.pdf" 
                                width="100%" 
                                style="border: none; height: 500px;"
                                loading="lazy"
                            ></iframe>
                        '''),
                        width="100%",
                        max_width="1000px",
                        margin="0 auto",
                    )
                ),

                rx.flex(
                    rx.link(
                        rx.button(
                            "Download",
                            bg="#2e144f",
                            color="white",
                            border_radius="xl",
                            padding=["0.8em 2em", "1em 2.5em"],
                            font_size=["1em", "1.2em"],
                            _hover={
                                "bg": "gray",
                                "transform": "scale(1.05)",
                            },
                            transition="all 0.3s ease-in-out",
                        ),
                        href="/Juan_Carlos_Garzon_Resume.pdf",
                        is_external=True,
                        download=True,
                    ),
                    justify="center",
                    margin_top="2em",
                ),
            ),
            width="100%",
            padding="2em",
            align="center",
            display="flex",
            flex_direction="column",
            gap="1em",
        ),
        width="100%",
    )