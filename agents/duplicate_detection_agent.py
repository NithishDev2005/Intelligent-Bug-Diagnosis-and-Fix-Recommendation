from models.agent_models import BugReport
from rag.retriever import BugRetriever


class DuplicateDetectionAgent:
    """
    Detects historically similar or duplicate bugs.
    """

    def __init__(self):
        self.retriever = BugRetriever()

    def analyze(self, bug: BugReport, n_results: int = 3) -> list[dict]:
        """
        Retrieve historically similar bugs.
        """

        query = (
            f"{bug.title}\n"
            f"{bug.description}\n"
            f"{bug.error_type or ''}\n"
            f"{bug.stack_trace or ''}"
        )

        similar_bugs = self.retriever.retrieve(
            query=query,
            n_results=n_results,
        )

        return similar_bugs