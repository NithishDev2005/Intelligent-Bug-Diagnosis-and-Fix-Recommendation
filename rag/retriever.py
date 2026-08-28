from rag.vector_store import BugVectorStore


class BugRetriever:

    def __init__(self):
        self.vector_store = BugVectorStore()

    def retrieve(self, query: str, n_results: int = 3) -> list[dict]:

        results = self.vector_store.search(
            query=query,
            n_results=n_results,
        )

        retrieved_bugs = []

        for i, bug_id in enumerate(results["ids"][0]):
            retrieved_bugs.append({
                "bug_id": bug_id,
                "document": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
            })

        return retrieved_bugs