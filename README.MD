# IconBuilder

## Introduction
IconBuilder is a Streamlit application that generates app icons based on user-provided app names using Azure's DALL-E 3 API. It offers an interactive UI where users can input an app name, choose image generation parameters (quality, style), and receive a visually generated icon corresponding to the app name.

## Prerequisites
- Python 3.8 or higher

## Setup
1. **Clone the repository**:
```
git clone https://github.com/thermofisher/dpe-gene-ai-accel-web-iconBuilder.git
cd dpe-gene-ai-accel-web-iconBuilder
```

2. **Create a virtual environment** (optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. **Install required packages**:
pip install -r requirements.txt

## Usage
Run the Streamlit application with:
streamlit run main.py

Navigate to the provided URL in your web browser to interact with the application. You can enter app names, select image generation parameters, and generate icons based on your inputs. Example app names are provided for quick demonstrations, and a "Reset" button is available to clear inputs and generated images.

## Features
- **Customizable Icon Generation**: Choose between qualities and styles for the generated icons.
- **Example App Names**: Quickly generate icons using pre-defined example app names.
- **Interactive UI**: Streamlit-based UI for an intuitive user experience.


