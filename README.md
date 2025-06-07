
# 🦙 FastAPI Llama Chat Stream

A full-stack local AI chat app using **LLaMA 3 (2.1B)** , with a **FastAPI** backend and **React/Next.js** frontend — streaming responses just like ChatGPT.

> 💻 Everything runs **100% locally**. No API keys. No cloud.

---

## 🚀 Features

- 🔁 Real-time streaming output (like ChatGPT)
- 🧠 LLaMA 3 via Ollama running locally
- ⚡ FastAPI backend with streaming support
- 💬 React/Next.js frontend
- 🔌 Simple setup & easy to extend
- 🛡️ CORS-enabled backend

---


## 📦 Tech Stack

| Layer     | Tech                            |
|-----------|----------------------------------|
| Model     | [LLaMA 3 (2.1B)] via Ollama     |
| Backend   | FastAPI + Uvicorn + Python      |
| Frontend  | React (Next.js) + Fetch stream  |
| Protocol  | `text/event-stream` (NDJSON)    |

---

## 📂 Project Structure

```
ollama-chat-stream/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   └── (Next.js app files)
├── README.md
```

---

## 🧠 1. Run Ollama with LLaMA 3

Install and run Ollama:

```bash
brew install ollama
ollama run llama3:2.1b
```

Ollama will run the model locally on `http://localhost:11434`.

---

## 🔧 2. Backend Setup (FastAPI)

### ✅ Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 📄 `requirements.txt`

```txt
fastapi
uvicorn
requests
```


### ▶️ Run Backend

```bash
uvicorn main:app --reload --port 8000
```

---

## ⚛️ 3. Frontend Setup (React/Next.js)

### ✅ Create App

You can use `create-next-app` or clone from this repo.

```bash
cd ../frontend
npm install
npm run dev
```

Runs on: `http://localhost:3000`


---

## ✅ Sample Interaction

```json
POST http://localhost:8000/api/stream
{
  "prompt": "Explain black holes like I'm 5."
}
```

Response stream:
```json
{"response": "Okay!"}
{"response": " A black hole is..."}
```

---

## 📌 Notes

- Ensure Ollama is running before you start the FastAPI backend.
- Use a proxy or CORS middleware for real deployment.
- You can switch `model` in `main.py` to any other Ollama model.

---

## 📄 License

MIT License — use freely and modify for your needs.

---

## 👤 Author

Made with ❤️ by [Odara Rapheal](https://github.com/odara-rapheal)

---

## 🌐 Useful Links

- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Next.js Docs](https://nextjs.org/docs)
- [LLaMA 3 Info](https://llama.meta.com/llama3/)
