from utils.data_loader import load_historical_bug_models
from rag.vector_store import BugVectorStore


bugs = load_historical_bug_models()

print("Historical bugs loaded:", len(bugs))

vector_store = BugVectorStore()

vector_store.add_bugs(bugs)

print("Bugs stored in ChromaDB:", vector_store.count())