import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_path):
    """
    Extracts full text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text.strip()

def clean_text(text):
    """
    Cleans extracted text by removing extra whitespace.
    """
    return ' '.join(text.split())

def split_pdf_to_chunks(text, chunk_size=1000, chunk_overlap=200):
    """
    Splits long text into overlapping chunks for embedding + retrieval.
    Uses recursive strategy with intelligent separators.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)
