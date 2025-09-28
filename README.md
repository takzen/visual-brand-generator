# AI-Powered Visual Brand Generator

### An AI-powered application that generates a consistent set of visual brand assets (logos, social media posts, banners) based on user-defined style prompts and color palettes.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-orange?logo=streamlit) ![Stability AI](https://img.shields.io/badge/Stability_AI-API-black?logo=stabilityai)
## 🚀 Overview

This project showcases a creative and practical application of generative AI for a common business need: creating a consistent visual identity. The application empowers users to define their brand's essence through simple inputs—a name, descriptive keywords, and a color palette. It then orchestrates a series of calls to a state-of-the-art image generation model (**Stable Diffusion 3**) to produce a complete, visually cohesive set of marketing assets.

The core challenge and achievement of this project is **prompt engineering for visual consistency**, demonstrating an advanced understanding of how to guide generative models to produce a suite of related, rather than random, outputs.

## ✨ Key Features & Techniques

*   **Creative AI Application:** Moves beyond data analysis to showcase skills in **creative content generation**, a key area of Generative AI.
*   **Prompt Engineering for Consistency:** The application's backend contains a sophisticated "prompt engine" that translates high-level user input into detailed, specific instructions for the AI model to ensure all generated assets share a common aesthetic.
*   **Multi-Asset Generation:** The system is designed to generate different types of visual assets (logos, square posts, wide banners) by dynamically adjusting prompts and model parameters (like aspect ratio).
*   **State-of-the-Art Image Model:** Integrates with the **Stability AI API** to leverage the power of **Stable Diffusion 3**, a model known for its quality and ability to render text.
*   **Interactive Front-End:** Uses **Streamlit** to create an intuitive interface where users can easily input their brand vision and see the results, including interactive elements like color pickers.

## 🛠️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/takzen/visual-brand-generator.git
    cd visual-brand-generator
    ```

2.  **Set up the Stability AI API Key:**
    *   Create a file named `.env` in the root of the project.
    *   Add your API key: `STABILITY_API_KEY="YOUR_STABILITY_AI_KEY"`

3.  **Create a virtual environment and install dependencies:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install streamlit python-dotenv requests Pillow
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

## 🖼️ Showcase

| 1. Define Your Brand                                    | 2. AI-Generated Assets                                     |
| :------------------------------------------------------ | :--------------------------------------------------------- |
| ![User Input](images/01_user_input.png)                 | ![Generated Assets](images/02_generated_assets.png)        |
| *The user defines their brand's name, style, and color palette in an intuitive form.* | *The application generates a cohesive set of assets, including a logo, social media post, and website banner.* |