import os
from dotenv import load_dotenv
import streamlit as st
from google import genai 
from PIL import Image

# Milestone 2: Configure API key
# 1. Load local .env file (useful for your local VS Code testing)
load_dotenv()

# 2. Step 2 Update: Try to get the key from Streamlit Secrets (Cloud)
# If not found in Secrets, it falls back to your local environment variable (.env)
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Missing GOOGLE_API_KEY. Please set it in Streamlit Secrets or a .env file.")
    st.stop()

# Initialize the modern unified SDK with the retrieved key
client = genai.Client(api_key=api_key)

def get_gemini_response(input_text, image, prompt):
    # Milestone 4: Using Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image, input_text]
    )
    return response.text

# Page Configuration & Header
st.set_page_config(page_title="Gemini Historical Artifact Description")
st.header("🏛 Gemini Historical Artifact Description App")

# Step 5.2: User Inputs
input_text = st.text_input("Input Prompt (e.g., 'Focus on its religious use'):", key="input")

uploaded_file = st.file_uploader(
    "Choose an image of a historical artifact...",
    type=["jpg", "jpeg", "png"]
)

# Step 5.3: Show Uploaded Image
if uploaded_file:
    image = Image.open(uploaded_file)
    # Replaced deprecated use_column_width with width="stretch"
    st.image(image, caption="Uploaded Image", width="stretch")

# Step 5.4: Generate Button
submit = st.button("Generate Artifact Description")

input_prompt = """
You are a historian. Analyze the historical artifact in the image and provide:
- Name of the artifact
- Origin
- Historical significance
- Approximate time period
"""

# Milestone 5: Output Generation
if submit:
    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            
            with st.spinner("📜 Historian is analyzing..."):
                response = get_gemini_response(input_text, image, input_prompt)

            st.subheader("📜 Description of the Artifact:")
            st.write(response)
            
            # Add the Download Button
            st.download_button(
                label="📥 Download Description as TXT",
                data=response,
                file_name="artifact_description.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please upload an image first!")