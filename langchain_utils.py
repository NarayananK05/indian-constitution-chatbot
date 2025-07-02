import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=1000, overlap=100):
    """
    Manually splits text into overlapping chunks.
    Used only if RecursiveTextSplitter is not preferred.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def embed_texts(texts):
    """
    Converts list of strings into embeddings using SentenceTransformer.
    """
    embeddings = model.encode(texts)
    return np.array(embeddings).astype("float32")

def create_vectorstore(chunks):
    """
    Creates a FAISS vector store from list of text chunks.
    Returns FAISS index and the original chunks list.
    """
    vectors = embed_texts(chunks)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, chunks

def get_relevant_chunks(query, index, chunks, k=6):
    """
    Retrieves top-k relevant chunks using both vector similarity and keyword matching.
    """
    # Vector search
    q_vector = embed_texts([query])
    D, I = index.search(q_vector, k)
    retrieved_chunks = [chunks[i] for i in I[0]]

    # Fallback: keyword match
    keyword_hits = [chunk for chunk in chunks if query.lower() in chunk.lower()]

    # Combine and deduplicate
    combined = list(dict.fromkeys(retrieved_chunks + keyword_hits))
    return combined[:k]
