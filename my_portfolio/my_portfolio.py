import reflex as rx
from rxconfig import config
from .ui.base import base_page
from .ui.nav import about_content, resume_content, contact_content, footer_three_columns

class State(rx.State):
    """The app state."""
    label = "My Portfolio"

    def handle_title_input(self, val):
        """Handle title input."""
        self.label = val

    def did_click(self):
        """Handle button click."""
        print("Button clicked!")
        return rx.redirect("/about")

# Define a global theme using Reflex config

def custom_theme():
    return rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="purple",
        background_color="#000000",  # Set the background to black
        text_color="purple.300",     # Set the default text color to purple
    )

rx.config.theme = custom_theme()


def index() -> rx.Component:
    """The main page of the app."""
    home_text = """
    Welcome to **My Portfolio**!  
    I am a passionate **Computer Engineer** with expertise in **Artificial Intelligence** and **Data Analysis**.  
    My mission is to create impactful solutions using cutting-edge technologies like **Computer Vision**, **Natural Language Processing**, and **Generative AI**.

    **What I Do**  
    - Build and deploy **AI-powered systems** for real-world applications.  
    - Develop **real-time object detection** and **transformer-based NLP models**.  
    - Create **scalable APIs** and **AI Agents** to enhance decision-making processes.  

    **Why Work With Me?**  
    I combine technical expertise with creativity, adaptability, and a results-driven mindset to deliver innovative solutions tailored to your needs.

    Let's build the future together!
    """
    my_child = rx.center(
        rx.vstack(
            rx.heading(State.label, size="6", color="purple.400", font_family="'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"),
            rx.markdown(home_text, font_size="1.2em", padding="1em", color="white", line_height="1.8"),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
            max_width="1000px",
            width="100%",
            bg="linear-gradient(135deg, #1a1a1a, #3a3a3a, #5a2a7a)",  # Fondo moderno con degradado
            padding="3em",
            border_radius="xl",
            box_shadow="2xl",
        ),
        padding_y="3em"
    )
    return base_page(my_child)


def about_page() -> rx.Component:
    return base_page(rx.center(
        rx.box(
            about_content(),
            max_width="1000px",
            width="100%",
            padding="2em",
            bg="#1a1a1a",
            border_radius="lg",
            box_shadow="lg",
        )
    ))

def resume_page() -> rx.Component:
    return base_page(rx.center(
        rx.box(
            resume_content(),
            max_width="1000px",
            width="100%",
            padding="2em",
            bg="#1a1a1a",
            border_radius="lg",
            box_shadow="lg",
        )
    ))

def contact_page() -> rx.Component:
    return base_page(rx.center(
        rx.box(
            contact_content(),
            max_width="600px",
            width="100%",
            padding="2em",
            bg="#1a1a1a",
            border_radius="lg",
            box_shadow="lg",
        )
    ))


app = rx.App()
app.add_page(index, route="/")
app.add_page(about_page, route="/about")
app.add_page(resume_page, route="/resume")
app.add_page(contact_page, route="/contact")

