from fastapi import FastAPI
from pydantic import BaseModel

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
    return {
        "success": True,
        "lead": lead
    }