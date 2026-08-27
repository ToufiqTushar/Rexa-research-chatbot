import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS vector store using cosine similarity.
    """

    embeddings = np.asarray(embeddings).astype("float32")

    # Normalize vectors
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    # Inner Product on normalized vectors = cosine similarity
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index


def search_vector_store(index, query_embedding, top_k=3):
    """
    Search the vector store using cosine similarity.
    """

    query_embedding = np.asarray(
        query_embedding
    ).astype("float32")

    # Normalize query vector
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(
        query_embedding,
        top_k
    )

    return scores, indices