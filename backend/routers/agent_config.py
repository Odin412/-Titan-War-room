from fastapi import APIRouter
from models import AgentConfig
from uuid import uuid4

router = APIRouter()
agents_config_store: list[AgentConfig] = []

@router.post("/")
def create(agent: AgentConfig):
    agent.id = str(uuid4())
    agents_config_store.append(agent)
    return agent

@router.get("/")
def list_all():
    return agents_config_store
