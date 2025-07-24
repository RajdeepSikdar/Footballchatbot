# ⚽ Football Chatbot (FastAPI + HTML)

A simple chatbot web app built using **FastAPI**, **Jinja2 templates**, and **Python**, designed to answer football-related questions using an API (like Gemini or any NLP backend).

---

## 🚀 Features

- Ask football-related questions via a web interface
- FastAPI backend with POST/GET routing
- Jinja2 templating for frontend rendering
- API integration for smart chatbot responses

---

## 📁 Project Structure

football_chatbot/
├── main.py
├── templates/
│ └── chat.html
├── static/
│ └── style.css
├── .env # Contains your API key (ignored by Git)
├── .gitignore
└── README.md

Install the following dependencies:
bash
pip install fastapi uvicorn jinja2 python-dotenv
Create a .env file in your root folder:

Create a .env file in your root folder:
GEMINI_API_KEY=your_api_key_here
How to Run the Project
Use this command to run the FastAPI server with live reload:
uvicorn main:app --reload
http://127.0.0.1:8000

👨‍💻 Author
Rajdeep Sikdar
