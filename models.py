from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AgentConfig(BaseModel):
    id: str
    name: str
    prompt: str
    tools: List[str]

class ExecutionFeedback(BaseModel):
    id: str
    node_id: str
    agent_id: str
    input: str
    output: str
    rating: int
    comment: str
    timestamp: datetime
