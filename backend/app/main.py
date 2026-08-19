from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Operating System", version="0.1.0")

AGENTS = [
    {"id": "chief-of-staff", "name": "Chief of Staff", "domain": "company", "status": "ready"},
    {"id": "project-manager", "name": "Project Manager", "domain": "projects", "status": "ready"},
    {"id": "research", "name": "Research Agent", "domain": "research", "status": "ready"},
    {"id": "literature", "name": "Literature Review Agent", "domain": "research", "status": "ready"},
    {"id": "developer", "name": "Developer Agent", "domain": "products", "status": "ready"},
    {"id": "marketing", "name": "Marketing Agent", "domain": "company", "status": "ready"},
    {"id": "analytics", "name": "Data & Analytics Agent", "domain": "company", "status": "ready"},
    {"id": "monitor", "name": "Monitoring & Recovery Agent", "domain": "system", "status": "ready"},
]

class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=300)
    domain: str = "company"
    priority: int = Field(default=3, ge=1, le=5)
    requires_approval: bool = False

TASKS: list[dict] = []

@app.get("/")
def root():
    return {"name": "AI Operating System", "status": "online", "time": datetime.now(timezone.utc)}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "api", "time": datetime.now(timezone.utc)}

@app.get("/api/agents")
def agents():
    return {"agents": AGENTS}

@app.get("/api/tasks")
def tasks():
    return {"tasks": TASKS, "count": len(TASKS)}

@app.post("/api/tasks")
def create_task(task: TaskIn):
    item = {"id": len(TASKS) + 1, **task.model_dump(), "status": "pending", "created_at": datetime.now(timezone.utc).isoformat()}
    TASKS.append(item)
    return item

@app.get("/api/overview")
def overview():
    return {
        "system": "online",
        "agents": len(AGENTS),
        "tasks": len(TASKS),
        "pending_approvals": sum(1 for t in TASKS if t["requires_approval"] and t["status"] == "pending"),
        "domains": ["company", "projects", "research", "products"],
        "24x7": True,
    }
