from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from .agents import AGENTS
from .database import SessionLocal, init_db
from .models import Agent, Domain, Task, TaskStatus

app = FastAPI(title="AI Operating System Kernel", version="0.1.0")


@app.on_event("startup")
def startup() -> None:
    init_db()
    with SessionLocal() as db:
        existing = {a.name for a in db.query(Agent).all()}
        for definition in AGENTS:
            if definition.name not in existing:
                db.add(Agent(name=definition.name, description=definition.description, domain=definition.domain, permissions=definition.permissions))
        db.commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = ""
    domain: Domain
    agent_name: str | None = None
    priority: int = Field(default=5, ge=1, le=10)
    requires_approval: bool = False
    payload: dict = Field(default_factory=dict)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "ai-os-kernel"}


@app.get("/agents")
def agents(db: Session = Depends(get_db)):
    return [{"id": str(a.id), "name": a.name, "domain": a.domain.value, "status": a.status.value, "permissions": a.permissions} for a in db.query(Agent).all()]


@app.get("/tasks")
def tasks(db: Session = Depends(get_db)):
    return [{"id": str(t.id), "title": t.title, "domain": t.domain.value, "status": t.status.value, "priority": t.priority, "agent": t.agent.name if t.agent else None} for t in db.query(Task).order_by(Task.priority.desc(), Task.created_at.desc()).all()]


@app.post("/tasks", status_code=201)
def create_task(request: TaskCreate, db: Session = Depends(get_db)):
    agent = None
    if request.agent_name:
        agent = db.query(Agent).filter(Agent.name == request.agent_name).first()
        if agent is None:
            return {"error": "agent_not_found"}
    task = Task(title=request.title, description=request.description, domain=request.domain, agent=agent, priority=request.priority, requires_approval=request.requires_approval, payload=request.payload, status=TaskStatus.QUEUED)
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"id": str(task.id), "status": task.status.value, "agent": agent.name if agent else None}
