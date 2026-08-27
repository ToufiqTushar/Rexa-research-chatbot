from utils.document_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import (
    create_embeddings,
    create_query_embedding
)
from utils.vector_store import (
    create_vector_store,
    search_vector_store
)


# Document
file_path = "research-paper.pdf"


# Extract text
text = extract_text(file_path)


# Split into chunks
chunks = split_text(text)


# Create embeddings
embeddings = create_embeddings(chunks)


# Create FAISS vector store
index = create_vector_store(embeddings)


# User question
question = "What were the Six Points?"


# Convert question into embedding
query_embedding = create_query_embedding(question)


# Search for relevant chunks
distances, indices = search_vector_store(
    index,
    query_embedding,
    top_k=3
)


print("\nQuestion:")
print(question)

print("\nMost Relevant Chunks:")

for i, index_number in enumerate(indices[0]):

    print("\n" + "=" * 60)
    print(f"RESULT {i + 1}")
    print(f"Distance: {distances[0][i]}")
    print("=" * 60)

    print(chunks[index_number])