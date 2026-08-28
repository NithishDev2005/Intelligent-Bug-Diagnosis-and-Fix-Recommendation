import chromadb.utils.embedding_functions as embedding_functions


class EmbeddingModel:
    """
    Wrapper around ChromaDB's default embedding model.
    """

    def __init__(self):
        self.embedding_function = (
            embedding_functions.DefaultEmbeddingFunction()
        )

    def embed_text(self, text: str) -> list[float]:
        """
        Convert text into an embedding vector.
        """

        embedding = self.embedding_function([text])[0]

        return embedding