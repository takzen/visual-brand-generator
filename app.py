# app.py
import streamlit as st
from dotenv import load_dotenv
from asset_generator import generate_brand_assets # Import the core logic

# Load environment variables from .env file
load_dotenv()

st.set_page_config(layout="wide")
st.title("Visual Brand Identity Generator 🎨")

st.header("1. Define Your Brand's Visual Style")

# --- User Input Form ---
with st.form("brand_form"):
    brand_name = st.text_input("Brand Name", "AuraZen")
    style_description = st.text_area("Style Description (Keywords)", "Minimalist, elegant, nature-inspired, high-tech, pastel colors, clean lines")
    
    st.subheader("Brand Color Palette")
    col1, col2, col3 = st.columns(3)
    with col1:
        color1 = st.color_picker("Primary Color", "#80CBC4")
    with col2:
        color2 = st.color_picker("Secondary Color", "#F8BBD0")
    with col3:
        color3 = st.color_picker("Accent Color", "#FFFFFF")

    submitted = st.form_submit_button("Generate Brand Assets")

# --- Asset Generation and Display ---
if submitted:
    with st.spinner("AI is crafting your brand visuals... This may take a minute or two."):
        try:
            brand_info = {
                "name": brand_name,
                "style": style_description,
                "palette": [color1, color2, color3]
            }
            # Call the generator function
            generated_assets = generate_brand_assets(brand_info)
            st.session_state.generated_assets = generated_assets
            st.success("Your brand assets have been successfully generated!")
        except Exception as e:
            st.error(f"An error occurred during generation: {e}")

# Display the results if they exist in the session state
if 'generated_assets' in st.session_state:
    st.header("2. Your Generated Brand Assets")
    assets = st.session_state.generated_assets

    # Display Logo
    st.subheader("Logo")
    st.image(assets.get("logo"), caption="A professional logo concept.", use_column_width=False, width=256)
    
    # Display Social Media Post
    st.subheader("Social Media Post")
    st.image(assets.get("social_post"), caption="A template for your social media presence.", use_column_width=False, width=512)

    # Display Website Banner
    st.subheader("Website Banner (Hero Image)")
    st.image(assets.get("banner"), caption="A banner for your website's homepage.", use_column_width=True)