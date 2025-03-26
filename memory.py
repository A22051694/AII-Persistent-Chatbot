import os
import json

class Memory:
    def __init__(self, chat_file="chat_history.json", facts_file="facts.json"):
        self.chat_file = chat_file
        self.facts_file = facts_file
        self.load_memory()

    def load_memory(self):
        """Load chat history and facts from files."""
        self.history = self._load_file(self.chat_file)
        self.facts = self._load_file(self.facts_file)

    def _load_file(self, filename):
        """Helper to load JSON data."""
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def get_messages(self):
        """Retrieve stored chat messages."""
        return self.history

    def add_message(self, role, content):
        """Add a new message to chat history."""
        self.history.append({"role": role, "content": content})
        self._save_file(self.chat_file, self.history)

    def clear_history(self):
        """Clear chat history but keep facts."""
        self.history = []
        self._save_file(self.chat_file, self.history)

    def get_facts(self):
        """Retrieve stored facts."""
        return self.facts

    def add_fact(self, fact):
        """Store a new fact."""
        if fact not in self.facts:
            self.facts.append(fact)
            self._save_file(self.facts_file, self.facts)

    def remove_fact(self, fact):
        """Remove a specific fact."""
        if fact in self.facts:
            self.facts.remove(fact)
            self._save_file(self.facts_file, self.facts)
            return True
        return False

    def clear_facts(self):
        """Delete all stored facts."""
        self.facts = []
        self._save_file(self.facts_file, self.facts)

    def _save_file(self, filename, data):
        """Helper to save JSON data."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
