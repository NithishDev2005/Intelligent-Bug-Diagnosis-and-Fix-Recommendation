from models.embedding import EmbeddingModel


embedding_model = EmbeddingModel()

text = "Application crashes because UserProfile object is null."

embedding = embedding_model.embed_text(text)

print("Embedding generated successfully!")
print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])