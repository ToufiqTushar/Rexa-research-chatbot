from utils.document_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings


file_path = "research-paper.pdf"


# Extract document text
text = extract_text(file_path)


# Split document into chunks
chunks = split_text(text)


# Create embeddings
embeddings = create_embeddings(chunks)


print("\nEmbedding process completed!")

print(f"Number of chunks: {len(chunks)}")
print(f"Embedding shape: {embeddings.shape}")