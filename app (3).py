import os
from pathlib import Path

# Libraries for file reading
from docx import Document
import PyPDF2
from pptx import Presentation

# --- Function to extract text from different file types ---
def extract_text(file_path):
    ext = file_path.suffix.lower()
    
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    
    elif ext == ".pdf":
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    
    elif ext == ".pptx":
        prs = Presentation(file_path)
        text = ""
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text:
                    text += shape.text + "\n"
        return text
    
    else:
        return f"[Unsupported file type: {ext}]"

# --- Main App Logic ---
def process_folder(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            print(f"Processing: {file.name}")
            text = extract_text(file)
            # Here you can process 'text' with your existing app logic
            print(f"Extracted Text:\n{text[:500]}...\n")  # Preview first 500 chars

if __name__ == "__main__":
    app_folder = "C:/Users/Lyla/Downloads/myproject"  # Update if needed
    process_folder(app_folder)
