import os
from openai import AzureOpenAI  # Import client for Azure OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Get API key and endpoint from environment variable
AZURE_OPENAI_DALLE3_API_KEY = os.getenv("AZURE_OPENAI_DALLE3_API_KEY")
AZURE_OPENAI_API_ENDPOINT_DALLE3 = os.getenv("AZURE_OPENAI_API_ENDPOINT_DALLE3")

# Function to query Azure DALL-E 3 for an image
def query_azure_dalle_for_image(title, api_key, api_endpoint, size, quality, style):
    client = AzureOpenAI(
        api_key=api_key,  
        api_version="2023-12-01-preview",
        azure_endpoint=api_endpoint
    )
    try:
        response = client.images.generate(
            model="dalle-3",
            prompt=title,
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
    st.title("Headline2Img: DALL-E 3 Image Generator")
    
    # Sidebar for model parameters with tooltips
    st.sidebar.header("Model Parameters")
    size = st.sidebar.selectbox(
        "Size", 
        ["1024x1024", "1024x1792", "1792x1024"], 
        index=0, 
        help="DALL-E 3 was trained to generate 1024x1024, 1024x1792 or 1792x1024 images"
    )
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

    example_headlines = [
        "Futuristic Cityscape: A Vision of 2100",
        "Deep Sea Discoveries: New Species Unveiled",
        "Quantum Computing: Breaking the Speed Barrier",
        "Mars Colonization: First Human Settlement"
    ]
    
    st.header("Example Headlines")
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1, col2, col3, col4]
    
    for i, headline in enumerate(example_headlines):
        if columns[i % 4].button(headline):
            st.session_state.title = headline  # Save the chosen headline in session state
            # Generate image for the chosen headline
            image_url = query_azure_dalle_for_image(headline, AZURE_OPENAI_DALLE3_API_KEY, AZURE_OPENAI_API_ENDPOINT_DALLE3, size, quality, style)
            if image_url:
                st.session_state.image_url = image_url  # Save the image URL in session state

    # User input for the news headline
    title = st.text_input("Or provide your own headline:", value="", key="title")
    
    if st.button("Generate Image"):
        if title:
            image_url = query_azure_dalle_for_image(title, AZURE_OPENAI_DALLE3_API_KEY, AZURE_OPENAI_API_ENDPOINT_DALLE3, size, quality, style)
            if image_url:
                st.session_state.image_url = image_url  # Save the image URL in session state

    # Display the image if available
    if "image_url" in st.session_state and st.session_state.image_url:
        st.image(st.session_state.image_url, caption="Generated Image")

if __name__ == "__main__":
    main()