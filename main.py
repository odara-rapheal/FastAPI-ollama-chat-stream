from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ideally, restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:2.1b"

@app.post("/api/prompt")
async def prompt_model(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt")

    if not user_prompt:
        return {"error": "Prompt is required"}

    payload = {
        "model": MODEL_NAME,
        "prompt": user_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()
