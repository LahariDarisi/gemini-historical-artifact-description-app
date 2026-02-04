import os
from dotenv import load_dotenv
import streamlit as st
from google import genai  # Migrated to the modern unified SDK
from PIL import Image

# Milestone 2: Configure API key
load_dotenv()
# The new SDK automatically reads GOOGLE_API_KEY from environment/secrets
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    # Milestone 4: Using Gemini 2.5 Flash with the new stateless Client
    # We can now pass the PIL image directly without extra setup
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
    # FIX: Replaced deprecated use_column_width with width="stretch"
    st.image(image, caption="Uploaded Image", width="stretch")

# Step 5.4: Generate Button & Prompt
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
            # Prepare image data (The new SDK accepts PIL images directly!)
            image = Image.open(uploaded_file)
            
            with st.spinner("📜 Historian is analyzing..."):
                response = get_gemini_response(input_text, image, input_prompt)

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