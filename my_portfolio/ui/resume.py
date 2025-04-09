import reflex as rx

def resume_content() -> rx.Component:
    return rx.center(
        rx.box(
            rx.html('''
                <iframe 
                    src="/Juan_Carlos_Garzon_Resume.pdf" 
                    width="100%" 
                    height="750px" 
                    style="border: none;"
                ></iframe>
            '''),
            max_width="1200px",
            width="100%",
            padding="2em",
            bg="linear-gradient(to right, #1f1f2e, #2e144f)",
            border_radius="25px",
            box_shadow="lg",
            color="white"
        )
    )