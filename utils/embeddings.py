from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts):
    """
    Convert a list of text chunks into embeddings.
    """

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


def create_query_embedding(query):
    """
    Convert a user question into an embedding.
    """

    embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    return embedding