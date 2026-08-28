from rag.retriever import BugRetriever


retriever = BugRetriever()

query = """
The application crashes when a user opens their profile.
The profile object is null and causes a NullPointerException.
"""

results = retriever.retrieve(query, n_results=3)

print("RAG RETRIEVAL SUCCESS")
print("Retrieved:", len(results))

for bug in results:
    print(
        bug["bug_id"],
        "| Severity:", bug["metadata"]["severity"],
        "| Priority:", bug["metadata"]["priority"]
    )