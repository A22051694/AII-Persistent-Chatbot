#knowledge.py
# knowledge.py
import json
import os

class KnowledgeManager:
    def __init__(self, knowledge_file="knowledge.json"):
        self.knowledge_file = knowledge_file
        self.knowledge = self.load_knowledge()

    def load_knowledge(self):
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, "r") as file:
                return json.load(file)
        return {}

    def save_knowledge(self):
        with open(self.knowledge_file, "w") as file:
            json.dump(self.knowledge, file, indent=4)

    def add_fact(self, key, value):
        self.knowledge[key] = value
        self.save_knowledge()

    def remove_fact(self, key):
        if key in self.knowledge:
            del self.knowledge[key]
            self.save_knowledge()

    def get_fact(self, key):
        return self.knowledge.get(key, "Fact not found.")

    def display_knowledge(self):
        if self.knowledge:
            print("[italic blue]Knowledge Base:[/italic blue]")
            for key, value in self.knowledge.items():
                print(f"[bold yellow]{key}[/bold yellow]: {value}")
        else:
            print("[italic red]Knowledge Base is empty.[/italic red]")
