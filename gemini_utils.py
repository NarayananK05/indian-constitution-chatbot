import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["general"]["gemini_api_key"])
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_legal_question(question, context_text):
    prompt = f"""
You are a Constitution Expert and scholar of Indian law. You will answer user questions **strictly using only the text provided from the Constitution of India**.

Use formal language. If the question refers to an Article number like "51A" or a keyword, try to match it even if the match is partial or not exact. Do not assume anything outside the provided content. If the information is not in the provided text, respond with "The Constitution text does not provide enough detail to answer this."

Context from the Constitution:
\"\"\"
{context_text[:20000]}
\"\"\"

User Question: {question}
"""
    response = model.generate_content(prompt)
    return response.text
