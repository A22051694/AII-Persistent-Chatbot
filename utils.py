#utils.py
from rich.console import Console
from rich.panel import Panel

def display_header(console, model_name):
    """Display chatbot header."""
    console.print(Panel(f"Welcome to your CLI AI Chatbot!\n[bold cyan]Current Model:[/bold cyan] {model_name}", expand=True))
