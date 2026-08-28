import requests


class LLMService:
    """
    Local LLM service using Ollama.
    """

    def __init__(self, model: str = "llama3.2:1b"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the local Ollama model.
        """

        response = requests.post(
            self.url,
            json={
    "model": self.model,
    "prompt": prompt,
    "stream": False,
    "options": {
        "num_ctx": 2048,
        "num_predict": 150,
    },
},
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]