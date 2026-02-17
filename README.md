# 🏛️ Gemini Historical Artifact Description App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-historical-artifact-description-app-fbbmzghmx96joo6plkc.streamlit.app/)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A professional GENAI-powered tool designed to bridge the gap between technology and history. This application leverages the **Gemini 2.5 Flash** multimodal model to analyze uploaded images of historical artifacts and generate insightful descriptions, including origin, significance, and time period.

---

## 🔗 Live Demo
You can access the live application here:  
🚀 **[Gemini Historical Artifact Description App](https://gemini-historical-artifact-description-app-fbbmzghmx96joo6plkc.streamlit.app/)**

---

## Project Demo Video

Watch the demo here: [Click to Watch](https://drive.google.com/file/d/1h5tfQE8xYMWQADFsmjcQivhY90shI83I/view?usp=sharing)

---
### 🚀 Key Features
* **Multimodal AI Analysis:** Advanced image recognition to identify and describe artifacts.
* **Custom Prompting:** Allows users to focus the AI's analysis on specific historical aspects.
* **Data Export:** Download the generated historical insights as a `.txt` file for offline research.
* **Secure Infrastructure:** Implements professional secret management for API keys.

---

### 🛠️ Technology Stack
* **Frontend:** [Streamlit](https://streamlit.io/) — Interactive UI and web hosting.
* **Backend & AI Logic:** [Google Gemini 2.5 Flash](https://ai.google.dev/) — Multimodal AI engine for artifact analysis.
* **Core Libraries:**
    * `google-genai`: Official SDK for AI communication.
    * `Pillow`: Image processing and handling.
    * `python-dotenv`: Management of environment variables and security.

---

### ⚙️ Local Setup Instructions
To run this project on your local machine, follow these steps:

#### 1. Clone the Repository
git clone https://github.com/LahariDarisi/gemini-historical-artifact-description-app.git

cd gemini-historical-artifact-description-app

#### 2. Install Dependencies:
   pip install -r requirements.txt

#### 3.Configure Secrets
   Create a .streamlit/secrets.toml file or a .env file with your API key:
   GOOGLE_API_KEY = "your_api_key_here"

#### 4.Launch the Application:
   streamlit run app.py
   
