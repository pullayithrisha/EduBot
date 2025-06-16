from PyPDF2 import PdfReader
from docx import Document
import io

async def extract_text_from_file(uploaded_file):
    content = await uploaded_file.read()

    if uploaded_file.filename.endswith(".pdf"):
        return extract_text_from_pdf(content)
    elif uploaded_file.filename.endswith(".docx"):
        return extract_text_from_docx(content)
    else:
        raise ValueError("Unsupported file format")

def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(io.BytesIO(content))
    text = ""
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        print(f"Page {i+1} text: {page_text[:100]}")  # log first 100 chars
        text += page_text or ""
    return text.strip()


def extract_text_from_docx(content: bytes) -> str:
    try:
        doc = Document(io.BytesIO(content))
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    except Exception:
        raise ValueError("Error reading DOCX")
