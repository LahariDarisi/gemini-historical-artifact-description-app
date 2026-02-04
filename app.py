from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Milestone 2: Configure API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Updated Function: Must accept image_data to "see" the artifact
def get_gemini_response(input_text, image_data, prompt):
    # Milestone 4: Using Gemini 2.5 Flash
    model = genai.GenerativeModel("gemini-2.5-flash")
    # Pass text and image together as a list
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

# Milestone 3: Function for Image Setup
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# UI Setup
st.set_page_config(page_title="Gemini Historical Artifact Description")
st.header("🏛 Gemini Historical Artifact Description App")

input_text = st.text_input("Input Prompt (e.g., 'Focus on its religious use'):", key="input")
uploaded_file = st.file_uploader("Choose an image of a historical artifact...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

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
            # 1. Prepare the image
            image_data = input_image_setup(uploaded_file)
            
            # 2. Get response using text + image
            with st.spinner("📜 Historian is analyzing..."):
                response = get_gemini_response(input_text, image_data, input_prompt)

            st.subheader("📜 Description of the Artifact:")
            st.write(response)
            
            # 3. Add the Download Button
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