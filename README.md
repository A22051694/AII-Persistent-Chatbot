# AI Persistent Chatbot (CLI)

A powerful **CLI-based AI chatbot** powered by **Ollama** with **persistent memory** for recalling past interactions. It supports **chat history management, profession-specific knowledge, and user-defined facts**.

## 🔥 Features
- **Persistent Chat Memory**: Remembers previous chats even after restarting.
- **Ollama Integration**: Supports AI models like `Llama3`, `Mistral`, etc.
- **Custom Commands**: Manage chat history, stored facts, and quick responses.
- **Lightweight CLI**: No heavy dependencies, works offline once installed.

## 🚀 Installation
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/ai_persistent_chatbot.git
cd ai_persistent_chatbot
```

### 2️⃣ **Install Dependencies**
Ensure you have **Python 3.10+** installed. Then install the required libraries:
```sh
pip install -r requirements.txt
```

### 3️⃣ **Run the Chatbot**
```sh
python main.py
```

## 🎮 Commands
| Command          | Description |
|-----------------|-------------|
| `help`          | Lists all available commands |
| `delete history` | Clears chat history but **keeps facts** |
| `show facts`    | Displays stored knowledge/facts |
| `delete fact <fact>` | Deletes a specific fact |
| `clear facts`   | Removes all stored facts |
| `exit`          | Exits the chatbot |

## 🛠 Configuration
- **AI Model:** Default is `llama3`, but can be changed in `config.py`.
- **Data Storage:** Saves chat history and facts in `memory.json`.

## 📌 Contributing
1. **Fork** the repository.
2. **Create a feature branch** (`git checkout -b feature-name`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to GitHub** (`git push origin feature-name`).
5. **Create a Pull Request** for review.

## 🐟 License
This project is licensed under the MIT License.

---
🔗 Developed by **A22051694**
