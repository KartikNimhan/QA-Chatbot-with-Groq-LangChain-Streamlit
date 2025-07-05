# 🤖 Q&A Chatbot with Groq, LangChain & Streamlit

This project is a conversational AI chatbot built using:

- 🧠 **Groq** – Ultra-fast LLM inference platform
- 🔗 **LangChain** – Powerful framework for chaining LLM calls and prompts
- 🌐 **Streamlit** – Interactive and user-friendly web app interface

It allows users to ask questions and get smart, fast responses from models like `mistral-saba-24b`, `llama3`, and `gemma2`.

---

## 🚀 Features

✅ Interactive chatbot UI  
✅ Model selection (Groq models)  
✅ Custom temperature & token control  
✅ LangChain-powered prompt templating  
✅ Real-time LLM responses via Groq API  

---

## 🧰 Tech Stack

| Layer        | Tool          |
|--------------|---------------|
| LLM Backend  | Groq API      |
| LLM Chain    | LangChain     |
| UI Frontend  | Streamlit     |
| Output Parser| LangChain Core|

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables (Optional: for LangSmith tracking)

Create a `.env` file and add:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

---

## 🔑 Groq API Setup

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign in and get your **Groq API key**
3. Paste the key into the sidebar of the app when running

---

## 🧠 Supported Models

You can select these models from the sidebar:

* `mistral-saba-24b`
* `llama3-70b-8192`
* `gemma2-9b-it`

Want more? You can easily add them by modifying the `selectbox()` in the Streamlit sidebar.

---

## 🛠 Running the App

```bash
streamlit run app.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

```
.
├── app.py                # Main Streamlit app
├── .env                  # (Optional) Environment config for LangChain
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📸 Preview

![screenshot](<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/39543fac-a742-4862-91b7-020837d3ee47" />) <!-- Replace with actual screenshot link if available -->

---

## 🙋 Author

Made with ❤️ by [Kartik Nimhan](https://github.com/KartikNimhan)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```
```
