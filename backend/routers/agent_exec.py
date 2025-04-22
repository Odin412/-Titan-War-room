from fastapi import APIRouter, Request
from agent.llm_engine import run_rag_chain

router = APIRouter()

@router.post("/execute")
async def execute(request: Request):
    data = await request.json()
    return {"response": run_rag_chain(data.get("query", ""), data.get("agent_id"))}
