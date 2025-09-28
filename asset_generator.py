# asset_generator.py
import os
import requests
import streamlit as st
from typing import Dict, List
from PIL import Image
from io import BytesIO

# --- Helper function to call the Stability AI API ---
def generate_image_from_api(prompt: str, aspect_ratio: str = "1:1"):
    """
    Calls the Stability AI API to generate an image based on a prompt.
    """
    api_key = os.getenv("STABILITY_API_KEY")
    if not api_key:
        raise ValueError("STABILITY_API_KEY not found in .env file.")

    # Using the latest Stable Diffusion 3 model
    engine_id = "stable-diffusion-3"
    api_host = 'https://api.stability.ai'
    
    response = requests.post(
        f"{api_host}/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
        },
    )

    if response.status_code != 200:
        raise Exception(f"Stability AI API Error: {response.text}")

    return Image.open(BytesIO(response.content))

# --- Core function for generating brand assets ---
def generate_brand_assets(brand_info: Dict) -> Dict[str, Image.Image]:
    """
    Orchestrates the generation of different brand assets.
    """
    name = brand_info["name"]
    style = brand_info["style"]
    palette = ", ".join(brand_info["palette"]) # Convert color list to string

    generated_assets = {}

    # --- 1. Logo Generation ---
    # Prompt engineering for a high-quality logo
    logo_prompt = (
        f"A modern, professional logo for a brand named '{name}'. "
        f"The logo should be a vector graphic, flat design, suitable for a website. "
        f"Style: {style}. "
        f"Color palette: {palette}. "
        "The design should be clean and easily recognizable. White background."
    )
    st.write("Generating logo...") # Feedback for the user
    generated_assets["logo"] = generate_image_from_api(logo_prompt, aspect_ratio="1:1")

    # --- 2. Social Media Post Generation ---
    post_prompt = (
        f"An eye-catching, visually consistent social media post for the brand '{name}'. "
        f"The post should feature abstract shapes and gradients. No text. "
        f"Aesthetic: {style}. "
        f"Primary colors: {palette}. "
        "The overall mood should be inspiring and professional."
    )
    st.write("Generating social media post...")
    generated_assets["social_post"] = generate_image_from_api(post_prompt, aspect_ratio="1:1")

    # --- 3. Website Banner Generation ---
    banner_prompt = (
        f"A professional website banner (hero image) for the brand '{name}'. "
        f"The image should be a beautiful, high-resolution photograph or abstract graphic that evokes the brand's essence. "
        f"Style: {style}. "
        f"Color scheme: {palette}. "
        "Subtle, elegant, and modern design. Lots of clean copy space for text."
    )
    st.write("Generating website banner...")
    generated_assets["banner"] = generate_image_from_api(banner_prompt, aspect_ratio="16:9")
    
    st.write("All assets generated!")
    return generated_assets