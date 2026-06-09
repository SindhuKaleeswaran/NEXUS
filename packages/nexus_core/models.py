from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"


class MemoryType(str, Enum):
    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    PROCEDURAL = "procedural"
    STRATEGIC = "strategic"


@dataclass(frozen=True)
class Evidence:
    source_id: str
    title: str
    url: str
    published_at: str
    summary: str
    entities: list[str]
    score: float


@dataclass
class Task:
    title: str
    description: str
    owner: str
    dependencies: list[str] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = TaskStatus.PENDING.value
    result: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionPlan:
    objective: str
    tasks: list[Task]
    milestones: list[str]


@dataclass
class AgentResult:
    agent: str
    task_id: str
    summary: str
    evidence: list[Evidence] = field(default_factory=list)
    artifacts: dict[str, Any] = field(default_factory=dict)


@dataclass
class EvaluationScore:
    category: str
    score: float
    rationale: str


@dataclass
class MemoryRecord:
    memory_type: MemoryType
    content: str
    metadata: dict[str, Any]
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class WorkflowTrace:
    objective: str
    plan: ExecutionPlan
    agent_results: list[AgentResult]
    evaluation: list[EvaluationScore]
    report: str
    memory_records: list[MemoryRecord]
    started_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    completed_at: datetime | None = None
