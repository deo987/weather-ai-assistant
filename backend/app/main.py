from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import traceback

from app.models import UserQuery
from app.agent import run_agent
from app.database import collection

# 🔥 CREATE APP FIRST
app = FastAPI()

# 🔥 ADD CORS AFTER app IS CREATED
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 ROUTES COME AFTER app DEFINITION
@app.post("/chat")
def chat(query: UserQuery):
    try:
        print("🔥 /chat HIT")
        print("User message:", query.message)

        response = run_agent(query.message)

        print("LLM response:", response)

        return {"response": response}

    except Exception as e:
        print("❌ ERROR IN /chat")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
