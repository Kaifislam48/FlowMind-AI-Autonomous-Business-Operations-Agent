import json
from fastapi import FastAPI
from pydantic import BaseModel
from services.gemini_service import score_lead
from services.storage_service import save_lead

app = FastAPI(
    title="FlowMind AI",
    description="Autonomous Business Operations Agent",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "project": "FlowMind AI",
        "status": "running"
    }


class Lead(BaseModel):
    name: str
    email: str
    message: str


@app.post("/lead")
def create_lead(lead: Lead):

    analysis = score_lead(
        lead.message
    )

    lead_data = {
        "name": lead.name,
        "email": lead.email,
        "message": lead.message,
        "analysis": analysis
    }

    save_lead(lead_data)

    return {
        "success": True,
        "lead": lead,
        "analysis": analysis
    }
    
@app.get("/leads")
def get_leads():

    with open("data/leads.json", "r") as f:
        return json.load(f)