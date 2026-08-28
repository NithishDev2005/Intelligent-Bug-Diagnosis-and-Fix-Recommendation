from utils.data_loader import load_historical_bug_models
from rag.document_builder import bug_to_document, bug_to_metadata


bugs = load_historical_bug_models()

first_bug = bugs[0]

document = bug_to_document(first_bug)
metadata = bug_to_metadata(first_bug)

print("DOCUMENT")
print("=" * 60)
print(document)

print("\nMETADATA")
print("=" * 60)
print(metadata)