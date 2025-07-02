# preprocess_pdf.py

import os
import pickle
import faiss
from pdf_utils import extract_text_from_pdf, clean_text, split_pdf_to_chunks
from langchain_utils import create_vectorstore

# Paths
pdf_path = "data/constitution.pdf"
output_index_path = "data/index.faiss"
output_chunks_path = "data/chunks.pkl"

# Make sure output dir exists
os.makedirs("data", exist_ok=True)

print("📄 Extracting text from PDF...")
text = extract_text_from_pdf(pdf_path)

print("🧹 Cleaning text...")
cleaned_text = clean_text(text)

print("✂️ Splitting into chunks...")
chunks = split_pdf_to_chunks(cleaned_text)

print(f"📝 Total Chunks: {len(chunks)}")
print("💾 Saving chunks to disk...")
with open(output_chunks_path, "wb") as f:
    pickle.dump(chunks, f)

print("🧠 Creating FAISS index...")
index, _ = create_vectorstore(chunks)

print("📦 Saving index to disk...")
faiss.write_index(index, output_index_path)

print("✅ Preprocessing complete. You can now run `streamlit run app.py`")
