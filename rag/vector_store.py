import chromadb

from models.embedding import EmbeddingModel


class BugVectorStore:
    """
    ChromaDB-based vector store for historical bug knowledge.
    """

    def __init__(self, persist_directory: str = "data/chroma_db"):
        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name="historical_bugs"
        )

        self.embedding_model = EmbeddingModel()

    def add_bug(
        self,
        bug_id: str,
        document: str,
        metadata: dict
    ):
        """
        Add one historical bug to ChromaDB.
        """

        embedding = self.embedding_model.embed_text(document)

        self.collection.upsert(
            ids=[bug_id],
            documents=[document],
            embeddings=[embedding],
            metadatas=[metadata],
        )

    def count(self) -> int:
        """
        Return the number of stored bugs.
        """

        return self.collection.count()

    def add_bugs(self, bugs: list):
        """
        Add multiple historical bugs to ChromaDB.
        """

        from rag.document_builder import (
            bug_to_document,
            bug_to_metadata,
        )

        for bug in bugs:
            document = bug_to_document(bug)
            metadata = bug_to_metadata(bug)

            self.add_bug(
                bug_id=bug.bug_id,
                document=document,
                metadata=metadata,
            )

    def search(self, query: str, n_results: int = 3):
        """
        Search for historically similar bugs.
        """

        query_embedding = self.embedding_model.embed_text(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )

        return results