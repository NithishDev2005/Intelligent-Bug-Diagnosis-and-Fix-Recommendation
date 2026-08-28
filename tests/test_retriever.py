from rag.retriever import BugRetriever


retriever = BugRetriever()

query = """
The application crashes when opening a user profile
because the profile object is missing.
"""

results = retriever.retrieve(
    query=query,
    n_results=3,
)

print("Retrieved bugs:", len(results))

for i, bug in enumerate(results):
    print(f"\nResult {i + 1}")
    print("Bug ID:", bug["bug_id"])
    print("Severity:", bug["metadata"]["severity"])
    print("Priority:", bug["metadata"]["priority"])