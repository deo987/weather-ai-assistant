# 🌦️ Weather AI Assistant

A full-stack AI-powered weather application built as part of the **SanchAI Analytics – Internship Tech Assessment**.  
The application allows users to ask natural-language questions about the weather of any city and receive intelligent responses through an agent-based backend.

---

## 🚀 Project Overview

The Weather AI Assistant is a minimal yet complete end-to-end application that demonstrates:

- React-based frontend (Vite)
- FastAPI-based backend
- Agent-oriented architecture using LangChain concepts
- Tool-based weather fetching
- MongoDB Atlas integration
- Production-ready project structure

The system is designed to integrate with LLM providers (OpenAI / OpenRouter).  
For evaluation purposes, a fallback mechanism is implemented to ensure the application works even when API credits are unavailable.

---

---

## ✨ Features

- 🌍 Ask weather for any city using natural language  
- 🧠 Agent-based backend logic  
- 🔧 Tool-based weather fetching  
- 🗂️ MongoDB Atlas logging (queries & responses)  
- 🔄 Graceful fallback when LLM credits are unavailable  
- 🎨 Clean and responsive UI  

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite.js
- JavaScript
- CSS

### Backend
- FastAPI
- Python
- LangChain (agent architecture)
- MongoDB Atlas
- REST APIs

### AI / LLM Layer
- Designed for OpenAI / OpenRouter compatibility
- Mocked fallback used during evaluation due to API credit constraints

---

## 🔄 Application Flow

1. User enters a query (e.g. *"Weather in Nashik"*)
2. Frontend sends request to FastAPI backend
3. Backend processes the query via agent logic
4. Weather tool fetches live weather data
5. Response is returned to frontend
6. Query and response are stored in MongoDB
7. Frontend displays the result to the user
8. <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/db46d373-b8c9-4983-bb02-c34a009f12cb" />


---

## ⚠️ LLM Credit Note (Important)

The backend is architected to support OpenAI / OpenRouter LLMs using LangChain agents.  
However, since OpenRouter requires paid credits for inference, a **graceful fallback response** is implemented for evaluation and demo purposes.

> Enabling live LLM inference requires only adding API credits — no architectural changes are needed.

This approach ensures:
- The full agent + tool workflow is demonstrated
- The application remains stable and testable
- External billing does not block evaluation

---

## ▶️ How to Run the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

### Backend runs at:
http://127.0.0.1:8000

### Frontend runs at:
cd frontend
npm install
npm run dev
