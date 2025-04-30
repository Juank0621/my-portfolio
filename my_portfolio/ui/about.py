import reflex as rx

def about_content() -> rx.Component:
    return rx.center(
        rx.box(
            rx.fragment(
                rx.desktop_only(
                    rx.hstack(
                        rx.box(
                            rx.image(
                                src="/profile.jpg",
                                width="24em",
                                height="24em",
                                border_radius="100%",
                                object_position="center",
                                object_fit="cover",
                                box_shadow="lg",
                                class_name="slide-in-left",
                            ),
                            width="100%",
                            max_width="28em",
                            min_width="26em",
                            padding_right="2em",
                            display="flex",
                            justify="center",
                            align="center",
                        ),
                        rx.box(
                            rx.vstack(
                                rx.heading(
                                    "About Me", 
                                    size="8", 
                                    weight="bold", 
                                    color="white", 
                                    class_name="slide-in-right"
                                ),
                                rx.text(
                                    "Computer Engineer with 5 years of experience in Data Analysis within the Colombian Aerospace Force and 2 years in Artificial Intelligence. "
                                    "Specializing in Computer Vision, Real-Time Object Detection, and NLP using Transformers and LLMs. Experienced in developing and deploying "
                                    "machine learning models with TensorFlow, Hugging Face, and PyTorch. Skilled in building scalable APIs with FastAPI and working with tools "
                                    "like Ultralytics YOLO. Experienced in incorporating LLMs to create specialized AI Agents tailored to company-specific information for question answering. "
                                    "Proficient in Python, SQL, and development environments like JupyterLab, Google Colab, VS Code, LangChain, and LlamaIndex. Also experienced in Generative AI "
                                    "for images using models such as GANs and VAEs.",
                                    font_size="1.2em",
                                    color="white",
                                    line_height="1.8",
                                    text_align="justify",
                                    margin_top="1em",
                                    class_name="slide-in-right",
                                ),
                                rx.text(
                                    "Languages, Frameworks & Tools",
                                    size="6",
                                    font_weight="bold",
                                    color="white",
                                    margin_top="2em",
                                    class_name="slide-in-right",
                                ),
                                rx.spacer(height="1em"),
                                rx.hstack(
                                    *[
                                        rx.image(
                                            src=icon,
                                            width="3em",
                                            class_name="slide-in-bottom",
                                            _hover={"filter": "grayscale(100%)"}
                                        )
                                        for icon in [
                                            "/Python.svg", "/FastAPI.svg",
                                            "/scikit-learn.svg", "/TensorFlow.svg", "/PyTorch.svg", "/HF.svg",
                                            "/MongoDB.svg", "/PostgreSQL.svg", "/Langchain.svg", "/Llamaindex.svg",
                                            "/Colab.svg", "/VSCode.svg", "/Ubuntu.svg", "/Git.svg",
                                            "/Jira.svg", "/GoogleCloud.svg", "/AWS.svg"
                                        ]
                                    ],
                                    spacing="4",
                                    wrap="wrap",
                                    justify="center"
                                ),
                                spacing="3",
                                align_items="center",
                            ),
                            width="70%",
                        ),
                        spacing="6",
                        align="center",
                        max_width="1500px",
                        width="100%",
                        padding="6em",
                    )
                ),
                rx.mobile_and_tablet(
                    rx.vstack(
                        rx.image(
                            src="/profile.jpg",
                            width="16em",
                            height="16em",
                            border_radius="100%",
                            object_position="center",
                            object_fit="cover",
                            box_shadow="lg",
                        ),
                        rx.heading(
                            "About Me", 
                            size="6", 
                            weight="bold", 
                            color="white", 
                            margin_top="1.5em",
                            text_align="center"
                        ),
                        rx.text(
                            "Computer Engineer with 5 years of experience in Data Analysis within the Colombian Aerospace Force and 2 years in Artificial Intelligence. "
                            "Specializing in Computer Vision, Real-Time Object Detection, and NLP using Transformers and LLMs. Experienced in developing and deploying "
                            "machine learning models with TensorFlow, Hugging Face, and PyTorch. Skilled in building scalable APIs with FastAPI and working with tools "
                            "like Ultralytics YOLO. Experienced in incorporating LLMs to create specialized AI Agents tailored to company-specific information for question answering. "
                            "Proficient in Python, SQL, and development environments like JupyterLab, Google Colab, VS Code, LangChain, and LlamaIndex. Also experienced in Generative AI "
                            "for images using models such as GANs and VAEs.",
                            font_size="0.8em",
                            color="white",
                            line_height="1.8",
                            text_align="justify",
                            margin_top="1em",
                        ),
                        rx.text(
                            "Languages, Frameworks & Tools",
                            size="5",
                            font_weight="bold",
                            color="white",
                            margin_top="2em",
                            text_align="center"
                        ),
                        rx.spacer(height="1em"),
                        rx.hstack(
                            *[
                                rx.image(
                                    src=icon,
                                    width="3em",
                                    _hover={"filter": "grayscale(100%)"}
                                )
                                for icon in [
                                    "/Python.svg", "/FastAPI.svg",
                                    "/scikit-learn.svg", "/TensorFlow.svg", "/PyTorch.svg", "/HF.svg",
                                    "/MongoDB.svg", "/PostgreSQL.svg", "/Langchain.svg", "/Llamaindex.svg",
                                    "/Colab.svg", "/VSCode.svg", "/Ubuntu.svg", "/Git.svg",
                                    "/Jira.svg", "/GoogleCloud.svg", "/AWS.svg"
                                ]
                            ],
                            spacing="4",
                            wrap="wrap",
                            justify="center"
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                        padding="2em",
                    )
                ),
            ),
            width="100%",
            overflow_x="hidden",
        )
    )