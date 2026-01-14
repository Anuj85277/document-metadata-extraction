from src.ocr import extract_text_from_image
from src.docx_reader import extract_text_from_docx
from src.llm_extractor import extract_metadata

def process_document(file_path: str) -> dict:
    if file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith(".png"):
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format")

    return extract_metadata(text)
