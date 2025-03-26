#chatbot.py (Handles AI interactions)
import ollama

def get_ai_response(model_name, messages):
    """Send chat history to Ollama and get AI response."""
    
    # Ensure all roles are mapped correctly
    valid_messages = []
    role_mapping = {"You": "user", "AI": "assistant"}

    for message in messages:
        role = role_mapping.get(message["role"], message["role"])  # Map roles
        valid_messages.append({"role": role, "content": message["content"]})

    response = ollama.chat(model=model_name, messages=valid_messages)
    return response["message"]["content"]
