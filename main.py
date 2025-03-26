#main.py
# main.py
import os
import sys
import time
from rich.console import Console
from rich.table import Table
from memory import Memory
from chatbot import get_ai_response

# Initialize console and memory
console = Console()
memory = Memory()

# Model selection
MODEL_NAME = "llama3"

def display_chat_history():
    """Displays previous chat history if available."""
    messages = memory.get_messages()
    if messages:
        console.print("\n[bold cyan]🔄 Previous Chat History:[/bold cyan]")
        for msg in messages:
            role = "[bold magenta]You:[/bold magenta]" if msg["role"] == "user" else "[bold green]AI:[/bold green]"
            console.print(f"{role} {msg['content']}")
        print("\n")

def show_help():
    """Displays available commands."""
    table = Table(title="Available Commands", show_lines=True)
    table.add_column("Command", style="cyan", justify="left")
    table.add_column("Description", style="white")

    table.add_row("[bold]help[/bold]", "Show available commands")
    table.add_row("[bold]delete history[/bold]", "Delete all chat history (keeps facts)")
    table.add_row("[bold]show facts[/bold]", "Display stored user facts")
    table.add_row("[bold]delete fact <fact>[/bold]", "Remove a specific fact")
    table.add_row("[bold]clear facts[/bold]", "Delete all stored facts")
    table.add_row("[bold]exit[/bold]", "Quit the chatbot")

    console.print(table)

def chat_loop():
    """Main chat loop."""
    display_chat_history()  # Show past history on startup

    while True:
        user_input = console.input("\n[bold magenta]You:[/bold magenta] ")

        if user_input.lower() == "exit":
            console.print("[bold red]Exiting...[/bold red] 👋")
            sys.exit()

        elif user_input.lower() == "help":
            show_help()
            continue  # Skip AI processing

        elif user_input.lower() == "delete history":
            memory.clear_history()
            console.print("[bold yellow]🗑 Chat history deleted![/bold yellow]")
            continue  # Skip AI processing

        elif user_input.lower() == "show facts":
            facts = memory.get_facts()
            if facts:
                console.print("[bold cyan]Stored Facts:[/bold cyan]")
                for fact in facts:
                    console.print(f"- {fact}")
            else:
                console.print("[italic]No facts stored.[/italic]")
            continue  # Skip AI processing

        elif user_input.startswith("delete fact "):
            fact_to_remove = user_input.replace("delete fact ", "").strip()
            if memory.remove_fact(fact_to_remove):
                console.print(f"[bold yellow]✅ Fact '{fact_to_remove}' removed.[/bold yellow]")
            else:
                console.print(f"[bold red]⚠ Fact not found: '{fact_to_remove}'[/bold red]")
            continue  # Skip AI processing

        elif user_input.lower() == "clear facts":
            memory.clear_facts()
            console.print("[bold yellow]🗑 All stored facts deleted![/bold yellow]")
            continue  # Skip AI processing

        # Process AI response only if not a command
        memory.add_message("user", user_input)
        ai_response = get_ai_response(MODEL_NAME, memory.get_messages())
        memory.add_message("assistant", ai_response)
        console.print(f"[bold green]AI:[/bold green] {ai_response}")

if __name__ == "__main__":
    console.print("\n[bold cyan]Welcome to your CLI AI Chatbot![/bold cyan] 🤖")
    console.print(f"[bold]Current Model:[/bold] {MODEL_NAME}")
    chat_loop()
