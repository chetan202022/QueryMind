# QueryMind 🧠

QueryMind is a simple AI-powered command-line chatbot built with Python and the Groq API. It allows users to interact with the **Llama 3.3 70B Versatile** model and receive intelligent responses directly from the terminal.

## 🚀 Features

* Interactive command-line interface
* Powered by Groq's ultra-fast inference API
* Uses the Llama 3.3 70B Versatile model
* Secure API key management with `.env`
* Adjustable temperature and token limits
* Lightweight and beginner-friendly

## 🛠️ Technologies Used

* Python
* Requests
* python-dotenv
* Groq API
* Llama 3.3 70B Versatile

## 📂 Project Structure

```
QueryMind/
│
├── .env              # Stores Groq API key
├── .gitignore
├── app.py           # Main chatbot application
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chetan202022/QueryMind.git
cd QueryMind
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Setup Environment Variables

Create a `.env` file in the project directory and add:

```env
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run the Application

```bash
python main.py
```

Example:

```
Welcome to QueryMind! Type 'exit' to quit.

YourMind: What is machine learning?

QueryMind: Machine learning is a branch of artificial intelligence that enables computers to learn from data and improve their performance without being explicitly programmed.
```

## 🧩 Dependencies

Install manually if needed:

```bash
pip install requests python-dotenv
```

## ⚙️ Configuration

Current settings:

```python
model = "llama-3.3-70b-versatile"
temperature = 0
max_tokens = 100
```

These values can be modified according to your requirements.

## 📌 Future Enhancements

* Conversation history support
* Streaming responses
* Colored terminal output
* Multiple AI model selection
* Voice input and speech output
* Web interface using Flask or Streamlit
* Chat export functionality

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Chetan Yadav**

GitHub: https://github.com/chetan202022
LinkedIn: https://www.linkedin.com/in/chetan--yadav
