import os
import requests

class GenAIClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ Missing GEMINI_API_KEY in environment variables")

    def generate_reply(self, prompt: str, model: str = "gemini-1.5-flash", max_tokens: int = 512):
        api_url = f"https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={self.api_key}"

        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ],
            "generationConfig": {
                "maxOutputTokens": max_tokens
            }
        }

        try:
            response = requests.post(
                api_url,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

            if "candidates" in data:
                return data["candidates"][0]["content"]["parts"][0]["text"]

            return str(data)
        except Exception as e:
            return f"⚠️ Error: {e}"
