from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from datetime import datetime, timezone
from uuid import uuid4

app = FastAPI(title="AI Operating System API", version="0.1.0")

class Risk(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
    title: str
    domain: str = "company"
    risk: Risk = Risk.low

agents = [
    {"id": "chief-of-staff", "name": "Chief of Staff", "domain": "company"},
    {"id": "project-manager", "name": "Project Manager", "domain": "projects"},
    {"id": "research", "name": "Research Agent", "domain": "research"},
    {"id": "literature", "name": "Literature Review Agent", "domain": "research"},
    {"id": "developer", "name": "Developer Agent", "domain": "product"},
    {"id": "marketing", "name": "Marketing Agent", "domain": "company"},
    {"id": "analytics", "name": "Data & Analytics Agent", "domain": "company"},
    {"id": "monitor", "name": "Monitoring & Recovery Agent", "domain": "system"},
]
tasks = []

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ai-os-api", "time": datetime.now(timezone.utc).isoformat()}

@app.get("/api/agents")
def list_agents():
    return {"agents": agents}

@app.get("/api/tasks")
def list_tasks():
    return {"tasks": tasks}

@app.post("/api/tasks")
def create_task(payload: TaskCreate):
    task = {"id": str(uuid4()), **payload.model_dump(), "status": "queued", "created_at": datetime.now(timezone.utc).isoformat()}
    tasks.append(task)
    return task

@app.get("/api/overview")
def overview():
    return {
        "system": "online",
        "agents": len(agents),
        "active_tasks": sum(t["status"] in {"queued", "running"} for t in tasks),
        "research_items": 0,
        "projects": 0,
        "approval_required": sum(t["risk"] != "low" for t in tasks),
    }
