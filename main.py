from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx
import os
from dotenv import load_dotenv
from collections import deque
from mangum import Mangum  # ✅ Add Mangum for Vercel

# Load environment variables from .env
load_dotenv()

app = FastAPI()

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# ✅ Thread-safe queue to store recent messages (last 10)
recent_messages = deque(maxlen=10)

@app.get("/")
async def root():
    return {"message": "FastAPI Messenger Bot is running!"}

# ✅ UI Page to Display Messages
@app.get("/messages", response_class=HTMLResponse)
async def get_messages():
    message_html = "<h2>Incoming Messages</h2><ul>"
    for msg in recent_messages:
        message_html += f"<li><b>{msg['sender']}:</b> {msg['text']}</li>"
    message_html += "</ul>"
    return message_html

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    if data.get("object") == "page":
        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event["sender"]["id"]
                if "message" in event and "text" in event["message"]:
                    user_message = event["message"]["text"]
                    
                    # ✅ Store the message in the queue
                    recent_messages.append({"sender": sender_id, "text": user_message})

                    # ✅ Send an automatic reply (optional)
                    await send_message(sender_id, f"You said: {user_message}")

    return {"status": "ok"}

async def send_message(recipient_id: str, text: str):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    headers = {"Content-Type": "application/json"}
    payload = {"recipient": {"id": recipient_id}, "message": {"text": text}}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json()

# ✅ Wrap the app with Mangum for Vercel
handler = Mangum(app)
