# Headline2Img

## Introduction
Headline2Img is a Streamlit application that generates images based on user-provided news headlines using Azure's DALL-E 3 API. It offers an interactive UI where users can input a headline, choose image generation parameters (size, quality, style), and receive a visually generated image corresponding to the headline.

## Prerequisites
- Python 3.8 or higher
- An Azure account with access to the DALL-E 3 API
- API key and endpoint from Azure for the DALL-E 3 service

## Setup
1. **Clone the repository**:
git clone https://github.com/estevan-mccalley/Headline2Img.git
cd Headline2Img

2. **Create a virtual environment** (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install required packages**:
pip install -r requirements.txt

4. **Set up environment variables**:
- Create a `.env` file in the project directory.
- Add your Azure DALL-E 3 API key and endpoint to the `.env` file:
  ```
  AZURE_OPENAI_DALLE3_API_KEY=your_api_key_here
  AZURE_OPENAI_API_ENDPOINT_DALLE3=your_api_endpoint_here
  ```

## Usage
Run the Streamlit application with:
streamlit run main.py

Navigate to the provided URL in your web browser to interact with the application. You can enter news headlines, select image generation parameters, and generate images based on your inputs. Example headlines are provided for quick demonstrations, and a "Reset" button is available to clear inputs and generated images.

## Features
- **Customizable Image Generation**: Choose between different sizes, qualities, and styles for the generated images.
- **Example Headlines**: Quickly generate images using pre-defined example headlines.
- **Interactive UI**: Streamlit-based UI for an intuitive user experience.

## Disclaimer
This project is for educational and demonstration purposes only. Please adhere to Azure's API usage policies and guidelines.


