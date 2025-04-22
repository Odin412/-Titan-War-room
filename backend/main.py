from fastapi import FastAPI
from routers import agent_config, agent_exec, feedback, exporter

app = FastAPI()

app.include_router(agent_config.router, prefix='/api/agent-config')
app.include_router(agent_exec.router, prefix='/api/agent')
app.include_router(feedback.router, prefix='/api/feedback')
app.include_router(exporter.router, prefix='/api/export')
