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
from utils.llm import ask_llm


# --------------------------------
# 1. Load document
# --------------------------------

file_path = "research-paper.pdf"

text = extract_text(file_path)


# --------------------------------
# 2. Split document
# --------------------------------

chunks = split_text(text)


# --------------------------------
# 3. Create embeddings
# --------------------------------

embeddings = create_embeddings(chunks)


# --------------------------------
# 4. Create FAISS index
# --------------------------------

index = create_vector_store(embeddings)


# --------------------------------
# 5. User question
# --------------------------------

question = "What were the Six Points?"


# --------------------------------
# 6. Create question embedding
# --------------------------------

query_embedding = create_query_embedding(question)


# --------------------------------
# 7. Retrieve relevant chunks
# --------------------------------

distances, indices = search_vector_store(
    index,
    query_embedding,
    top_k=3
)


# --------------------------------
# 8. Build context
# --------------------------------

relevant_chunks = []

for index_number in indices[0]:

    relevant_chunks.append(
        chunks[index_number]
    )


context = "\n\n".join(relevant_chunks)


# --------------------------------
# 9. Ask GPT-OSS-120B
# --------------------------------

answer = ask_llm(
    question,
    context
)


# --------------------------------
# 10. Display result
# --------------------------------

print("\n" + "=" * 60)
print("QUESTION")
print("=" * 60)

print(question)


print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(answer)