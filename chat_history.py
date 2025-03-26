#chat_history.py
# chat_history.py
import os

class ChatHistory:
    def __init__(self, history_file="chat_history.txt"):
        self.history_file = history_file
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                return file.readlines()
        return []

    def save_history(self):
        with open(self.history_file, "w") as file:
            file.writelines(self.history)

    def add_to_history(self, message):
        self.history.append(message + "\n")
        self.save_history()

    def clear_history(self):
        self.history = []
        self.save_history()

    def display_history(self):
        if self.history:
            print("[italic green]Chat History:[/italic green]")
            for line in self.history:
                print(line.strip())
        else:
            print("[italic red]No chat history found.[/italic red]")
