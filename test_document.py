from utils.document_loader import extract_text


file_path = "research-paper.pdf"

text = extract_text(file_path)

print("Document loaded successfully!")
print("\nExtracted text:\n")
print(text[:5000])