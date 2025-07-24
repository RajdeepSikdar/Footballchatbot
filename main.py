from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
import httpx

# Load .env
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Static and Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

# Gemini API URL
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"


# Home route
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# Chat API
@app.post("/chat")
async def chat(message: str = Form(...)):
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [{
            "parts": [{"text": message}]
        }]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_API_URL, headers=headers, json=body)

    if response.status_code == 200:
        data = response.json()
        try:
            reply = data['candidates'][0]['content']['parts'][0]['text']
            return JSONResponse(content={"reply": reply})
        except:
            return JSONResponse(content={"reply": "⚠️ No answer received from Gemini."})
    else:
        return JSONResponse(content={"reply": f"⚠️ Error from Gemini: {response.text}"})
