# 🦙 Ollama Chat Stream

A full-stack local AI chat app using **LLaMA 3 (2.1B)** with a **FastAPI** backend and **React/Next.js** frontend — streaming responses just like ChatGPT.

> 💻 Everything runs **100% locally**. No API keys. No cloud.

---

## 🚀 Features

- 🔁 Real-time streaming output (like ChatGPT)
- 🧠 LLaMA 3 running locally
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

ollama-chat-stream/
├── FastAPI-ollama-chat-stream/
│ ├── main.py
│ └── requirements.txt
├── frontend/
│ └── (Next.js app files)
├── README.md


---

## 🧠 1. Run Ollama with LLaMA 3

Install and run Ollama:

```bash
brew install ollama
ollama run llama3:2.1b

Ollama will run the model locally on http://localhost:11434

---

## 2. Backend Setup (FastAPI)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
