from __future__ import annotations

from nexus_core.models import AgentResult, Task
from nexus_core.retrieval.hybrid import HybridRetriever


class ResearchAgent:
    name = "research"

    def __init__(self, retriever: HybridRetriever) -> None:
        self.retriever = retriever

    def execute(self, task: Task) -> AgentResult:
        task.status = "running"
        evidence = self.retriever.search(task.description)
        task.status = "complete"
        return AgentResult(
            agent=self.name,
            task_id=task.id,
            summary=f"Retrieved {len(evidence)} evidence items for {task.title.lower()}.",
            evidence=evidence,
            artifacts={"retrieval_strategy": "hybrid(vector, graph, temporal, rerank)"},
        )
