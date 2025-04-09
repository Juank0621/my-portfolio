import reflex as rx

def about_content() -> rx.Component:
    return rx.center(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.heading("👨‍💻 About Me", size="5", weight="bold", color="purple"),
                        rx.text(
                            "Computer Engineer with 5 years of experience in Data Analysis within the Colombian Aerospace Force and 2 years in Artificial Intelligence. "
                            "Specializing in Computer Vision, Real-Time Object Detection, and NLP using Transformers and LLMs. Experienced in developing and deploying "
                            "machine learning models with TensorFlow, Hugging Face, and PyTorch. Skilled in building scalable APIs with FastAPI and working with tools "
                            "like Ultralytics YOLO. Experienced in incorporating LLMs to create specialized AI Agents tailored to company-specific information for question answering. "
                            "Proficient in Python, SQL, and development environments like JupyterLab, Google Colab, VS Code, LangChain, and LlamaIndex. Also experienced in Generative AI "
                            "for images using models such as GANs and VAEs.",
                            font_size="1em",
                            color="white",
                            line_height="1.8",
                            text_align="justify",
                            margin_top="1em",
                        ),
                        rx.heading("🛠️ Technical Skills", size="4", weight="bold", color="purple", margin_top="2em"),
                        rx.text("Programming & Frameworks:", font_weight="bold", color="white"),
                        rx.hstack(
                            rx.badge("Python"), rx.badge("SQL"), rx.badge("TensorFlow"),
                            rx.badge("PyTorch"), rx.badge("Hugging Face"),
                            rx.badge("scikit-learn"), rx.badge("FastAPI"),
                            rx.badge("Streamlit"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.text("Big Data & Databases:", font_weight="bold", color="white", margin_top="1em"),
                        rx.hstack(
                            rx.badge("MongoDB"), rx.badge("SQL Server"),
                            rx.badge("SQLite"), rx.badge("PostgreSQL"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.text("Computer Vision:", font_weight="bold", color="white", margin_top="1em"),
                        rx.hstack(
                            rx.badge("Ultralytics YOLO"),
                            rx.badge("OpenCV"),
                            rx.badge("Hugging Face Vision Models"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.text("NLP & LLMs:", font_weight="bold", color="white", margin_top="1em"),
                        rx.hstack(
                            rx.badge("Hugging Face Text Models"),
                            rx.badge("LLMs"),
                            rx.badge("AI Agents"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.text("Generative AI:", font_weight="bold", color="white", margin_top="1em"),
                        rx.hstack(
                            rx.badge("GANs"),
                            rx.badge("VAEs"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.text("Dev Tools:", font_weight="bold", color="white", margin_top="1em"),
                        rx.hstack(
                            rx.badge("JupyterLab"),
                            rx.badge("Google Colab"),
                            rx.badge("VS Code"),
                            rx.badge("LangChain"),
                            rx.badge("LlamaIndex"),
                            spacing="2",
                            wrap="wrap",
                        ),
                        rx.heading("💡 Soft Skills", size="4", weight="bold", color="purple", margin_top="2em"),
                        rx.text(
                            "Creative problem-solving, decision-making, adaptability and resilience, goal-oriented, effective communication, leadership, teamwork, and collaboration.",
                            font_size="1em",
                            color="white",
                            line_height="1.8",
                            text_align="justify",
                            margin_top="1em",
                        ),
                        spacing="3",
                        align_items="start",
                    ),
                    width="70%",
                ),
                rx.box(
                    rx.image(
                        src="/juangarzon.png",
                        width="18em",
                        height="18em",
                        border_radius="100%",
                        object_position="center",
                        object_fit="cover",
                        box_shadow="lg",
                    ),
                    width="30%",
                    align="start",
                ),
                spacing="6",
                align="start",
            ),
            max_width="1100px",
            width="100%",
            padding="2em",
            border_radius="25px",
            box_shadow="lg",
            bg="linear-gradient(to right, #1f1f2e, #2e144f)",
        )
    )