import os
from openai import AzureOpenAI  # Import client for Azure OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

# Get API key and endpoint from environment variable
AZURE_OPENAI_DALLE3_API_KEY = os.getenv("AZURE_OPENAI_DALLE3_API_KEY")
AZURE_OPENAI_API_ENDPOINT_DALLE3 = os.getenv("AZURE_OPENAI_API_ENDPOINT_DALLE3")

# Function to query Azure DALL-E 3 for an image
def query_azure_dalle_for_image(app_name, api_key, api_endpoint, quality, style):
    # Hardcoded size as per the requirement
    size = "1024x1024"
    client = AzureOpenAI(
        api_key=api_key,  
        api_version="2023-12-01-preview",
        azure_endpoint=api_endpoint
    )
    # Updated prompt with the system instruction and appending app_name
    prompt = f"Rounded edges square mobile app logo design without text, 3d origami of a '{app_name}' GPT, subtle gradient, minimal blue background. Conveys the idea of the APPLICATION NAME: '{app_name}'"
    try:
        response = client.images.generate(
            model="dalle-3",
            prompt=prompt,
            size=size,
            quality=quality,
            style=style,
            n=1,  # Number of images to generate
        )
        image_url = response.data[0].url  
        return image_url
    except Exception as e:
        st.error(f"An error occurred during Azure DALL-E 3 query: {e}")
        return None  # Return None to indicate an error without text

# Main Streamlit app
def main():
    st.title("IconBuilder: DALL-E 3 Icon Generator")
    st.subheader("Please be patient after every submission")
    
    # Sidebar for model parameters with tooltips
    st.sidebar.header("Model Parameters")
    quality = st.sidebar.selectbox(
        "Quality", 
        ["standard", "hd"], 
        index=0, 
        help="“Standard” quality will create attractive images quickly and at low cost. Users can specify “hd” (and pay a higher price) to give the model more time to generate images, resulting in higher image quality, but also higher latency."
    )
    style = st.sidebar.selectbox(
        "Style", 
        ["vivid", "natural"], 
        index=0, 
        help="Style provides advanced control of the visual style of the generation."
    )

    # Reset functionality
    if st.button("Reset"):
        # Clear specific session state keys or reset the entire session state as needed
        for key in ["image_url", "title"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()

    example_icons = [
        "IntelliPrompt",
        "SmartChat",
        "Headline2Image",
        "IconBuilder"
    ]
    
    st.header("Example App Icons")
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1, col2, col3, col4]
    
    for i, icon in enumerate(example_icons):
        if columns[i % 4].button(icon):
            st.session_state.title = icon  # Save the chosen icon in session state
            # Generate icon for the chosen app name
            image_url = query_azure_dalle_for_image(icon, AZURE_OPENAI_DALLE3_API_KEY, AZURE_OPENAI_API_ENDPOINT_DALLE3, quality, style)
            if image_url:
                st.session_state.image_url = image_url  # Save the image URL in session state

    # User input for the app icon
    icon = st.text_input("Or provide your own app name:", value="", key="icon")
    
    if st.button("Generate Icon"):
        if icon:
            image_url = query_azure_dalle_for_image(icon, AZURE_OPENAI_DALLE3_API_KEY, AZURE_OPENAI_API_ENDPOINT_DALLE3, quality, style)
            if image_url:
                st.session_state.image_url = image_url  # Save the image URL in session state

    # Display the image if available
    if "image_url" in st.session_state and st.session_state.image_url:
        st.image(st.session_state.image_url, caption="Generated Icon")

if __name__ == "__main__":
    main()