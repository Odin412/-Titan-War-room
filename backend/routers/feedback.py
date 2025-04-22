from fastapi import APIRouter
from models import ExecutionFeedback
from uuid import uuid4
from datetime import datetime

router = APIRouter()
feedback_store: list[ExecutionFeedback] = []

@router.post("/")
def submit(data: dict):
    feedback = ExecutionFeedback(
        id=str(uuid4()),
        node_id=data["node_id"],
        agent_id=data["agent_id"],
        input=data["input"],
        output=data["output"],
        rating=data["rating"],
        comment=data.get("comment", ""),
        timestamp=datetime.now()
    )
    feedback_store.append(feedback)
    return {"message": "Feedback recorded"}

@router.get("/")
def list_feedback():
    return feedback_store
