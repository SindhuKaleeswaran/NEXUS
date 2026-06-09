from __future__ import annotations

import sys
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "packages"))

from nexus_core import NexusEngine  # noqa: E402

app = FastAPI(
    title="NEXUS API",
    description="Autonomous enterprise intelligence workflow gateway.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = NexusEngine()


class GoalRequest(BaseModel):
    objective: str = Field(..., min_length=10)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "nexus-api"}


@app.post("/goals/run")
def run_goal(request: GoalRequest) -> dict:
    trace = engine.run(request.objective)
    return asdict(trace)
