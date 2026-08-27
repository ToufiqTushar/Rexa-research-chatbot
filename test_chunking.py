from utils.document_loader import extract_text
from utils.text_splitter import split_text


file_path = "research-paper.pdf"


# Extract text
text = extract_text(file_path)


# Split text into chunks
chunks = split_text(text)


print(f"Total characters: {len(text)}")
print(f"Total chunks: {len(chunks)}")


for i, chunk in enumerate(chunks):

    print("\n" + "=" * 60)
    print(f"CHUNK {i + 1}")
    print("=" * 60)

    print(chunk)