from services.llm_service import LLMService


llm = LLMService()

response = llm.generate(
    "Explain a NullPointerException in one simple sentence."
)

print("\nLLM RESPONSE:")
print(response)