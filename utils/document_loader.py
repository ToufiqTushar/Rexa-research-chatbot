import pymupdf
from docx import Document


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""

    text = ""

    document = pymupdf.open(file_path)

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text(file_path):
    """Extract text based on the file extension."""

    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported file type. Please upload a PDF or DOCX file."
        )