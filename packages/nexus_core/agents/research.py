from __future__ import annotations

from nexus_core.models import AgentResult, Task, TaskStatus
from nexus_core.retrieval.hybrid import HybridRetriever


class ResearchAgent:
    name = "research"

    def __init__(self, retriever: HybridRetriever) -> None:
        self.retriever = retriever

    def execute(self, task: Task) -> AgentResult:
        task.status = TaskStatus.RUNNING.value
        evidence = self.retriever.search(task.description)
        task.status = TaskStatus.COMPLETE.value
        return AgentResult(
            agent=self.name,
            task_id=task.id,
            summary=f"Retrieved {len(evidence)} evidence items for {task.title.lower()}.",
            evidence=evidence,
            artifacts={"retrieval_strategy": "hybrid(vector, graph, temporal, rerank)"},
        )
