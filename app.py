# app.py
import streamlit as st
import faiss
import pickle
from gemini_utils import ask_legal_question
from langchain_utils import get_relevant_chunks

st.set_page_config(page_title="Indian Constitution Chatbot 🇮🇳", page_icon="📜")
st.title("📜 Indian Constitution Chatbot")

index_path = "data/index.faiss"
chunks_path = "data/chunks.pkl"

# 🧹 Clear chat button
if st.button("🧹 Clear Chat and Reset"):
    st.session_state.clear()
    st.rerun()

# Load FAISS index and chunks only once
if "index" not in st.session_state:
    try:
        with st.spinner("🔍 Loading the Constitution..."):
            index = faiss.read_index(index_path)
            with open(chunks_path, "rb") as f:
                chunks = pickle.load(f)
            st.session_state.index = index
            st.session_state.chunks = chunks
    except Exception as e:
        st.error("❌ Failed to load index or chunks. Please run `indexing.py` first.")
        st.stop()

# Initialize memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show conversation history
for turn in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(turn["user"])
    with st.chat_message("assistant"):
        st.markdown(turn["bot"])

# Chat input
question = st.chat_input("Ask a question about the Indian Constitution...")

if question:
    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("📚 Consulting the Constitution..."):
        top_chunks = get_relevant_chunks(
            question, st.session_state.index, st.session_state.chunks
        )
        context = "\n\n".join(top_chunks)

        # Add minimal memory to context
        memory_prompt = ""
        for turn in st.session_state.chat_history[-3:]:
            memory_prompt += f"User: {turn['user']}\nConstitution Expert: {turn['bot']}\n"
        memory_prompt += f"User: {question}\nConstitution Expert:"

        full_prompt = context + "\n\nConstitutional Conversation:\n" + memory_prompt
        try:
            answer = ask_legal_question(question, full_prompt)
        except Exception as e:
            answer = "⚠️ An error occurred while fetching the answer. Please try again."

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.chat_history.append({"user": question, "bot": answer})
