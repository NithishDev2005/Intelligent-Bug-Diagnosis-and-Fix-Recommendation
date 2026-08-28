from rag.vector_store import BugVectorStore


vector_store = BugVectorStore()

query = """
The application crashes when loading a user's profile.
The profile object is missing and causes a NullPointerException.
"""

results = vector_store.search(
    query=query,
    n_results=3,
)

print("SEARCH QUERY")
print("=" * 60)
print(query)

print("\nSIMILAR HISTORICAL BUGS")
print("=" * 60)

for i, bug_id in enumerate(results["ids"][0]):
    print(f"\nResult {i + 1}")
    print("Bug ID:", bug_id)
    print("Document:", results["documents"][0][i])