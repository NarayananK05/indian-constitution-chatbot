# Indian Constitution Chatbot

This project is an AI-powered chatbot designed to answer questions related to the Indian Constitution. It uses document retrieval techniques combined with Google Gemini API to provide contextual, accurate responses based on real constitutional text.

## Features

- Query-specific retrieval from the Constitution of India (PDF).
- Context-aware chat with memory of previous user interactions.
- Fast and efficient semantic search using local FAISS indexing.
- Clean Streamlit-based frontend with real-time interaction.
- Easy deployment on Streamlit Cloud.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Embedding Model**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS
- **Language Model**: Google Gemini API (via `google-generativeai`)
- **PDF Parsing**: PyMuPDF (`fitz`)
- **Context Memory**: Simple chat history stored via Streamlit session state

## Folder Structure

indian-constitution-chatbot/
├── app.py # Main Streamlit app
├── preprocess_pdf.py # One-time script to process PDF
├── pdf_utils.py # PDF text extraction logic
├── langchain_utils.py # Chunking and semantic search
├── gemini_utils.py # Prompting via Gemini API
├── requirements.txt # Python dependencies
├── .gitignore # Files to exclude from Git
├── .streamlit/
│ └── secrets.toml # (Local) API key storage (do not upload)
├── data/
│ ├── constitution.pdf # Source PDF
│ ├── chunks.pkl # Precomputed text chunks
│ └── index.faiss # FAISS vector index

## Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/indian-constitution-chatbot.git
cd indian-constitution-chatbot

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Add Your API Key (Locally)
Create a .streamlit/secrets.toml file:
toml
Copy
Edit
[general]
gemini_api_key = "your-gemini-api-key"
Important: Make sure this file is included in .gitignore.

5. Preprocess the PDF
Run this script once to generate vector index:
bash
Copy
Edit
python preprocess_pdf.py
6. Run the Application
bash
Copy
Edit
streamlit run app.py
