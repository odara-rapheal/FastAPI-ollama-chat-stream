from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import requests

app = FastAPI()

""" Allow frontend to connect

    NB: For production use, allow only the necessary URLs (frontend)
    to connect to this backend.

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:2.1b"

def stream_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True
    }
    with requests.post(OLLAMA_URL, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                yield line.decode("utf-8") + "\n"

@app.post("/api/stream")
async def stream_prompt(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt")
    if not user_prompt:
        return {"error": "Prompt is required"}
    return StreamingResponse(stream_ollama(user_prompt), media_type="text/event-stream")
