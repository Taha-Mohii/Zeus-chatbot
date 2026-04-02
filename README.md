# Zeus AI Chatbot 🤖

Zeus is a personal AI chatbot built using Python and the Groq API. It features a clean web interface, conversation memory, and context-aware responses.

## 🚀 Features

- 🧠 Conversation memory (remembers previous messages)
- 🤖 Context-aware AI responses
- ⚡ Powered by Groq API (LLaMA 3.3 70B)
- 🌐 Web interface built with Flask
- 💬 Typing indicator and modern chat UI
- 🛡 Error handling for API failures

## 🛠 Tech Stack

- Python
- Flask
- Groq API
- dotenv

## 📂 Project Structure
```
Zeus_chatbot/
├── app.py
├── templates/
│   └── index.html
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/Taha-Mohii/Zeus-chatbot.git
cd Zeus-chatbot
```

2️⃣ Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

3️⃣ Install dependencies
```bash
pip install groq flask python-dotenv
```

4️⃣ Add your Groq API key in a `.env` file
```
GROQ_API_KEY=your_api_key_here
```

5️⃣ Run the app
```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## 👤 Author

Taha Mohii..
