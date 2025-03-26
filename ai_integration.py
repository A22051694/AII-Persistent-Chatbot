#ai_integration.py
# ai_integration.py
import ollama

class AIIntegration:
    def __init__(self):
        self.client = ollama.Client()

    def get_response(self, user_input, model="Llama3"):
        try:
            response = self.client.chat(model=model, messages=[{"role": "user", "content": user_input}])
            return response["text"]
        except Exception as e:
            return f"Error: {e}"
