from __future__ import annotations

from nexus_core.models import MemoryRecord, MemoryType, WorkflowTrace


class MemoryStore:
    """In-process memory store with the same taxonomy used by production stores."""

    def __init__(self) -> None:
        self.records: list[MemoryRecord] = []

    def persist_workflow(self, trace: WorkflowTrace) -> list[MemoryRecord]:
        records = [
            MemoryRecord(
                memory_type=MemoryType.EPISODIC,
                content=f"Completed objective: {trace.objective}",
                metadata={"agent_count": len(trace.agent_results), "task_count": len(trace.plan.tasks)},
            ),
            MemoryRecord(
                memory_type=MemoryType.SEMANTIC,
                content="Healthcare AI opportunities are strongest where workflow ROI, governance, and operational memory are measurable.",
                metadata={"domain": "healthcare_ai"},
            ),
            MemoryRecord(
                memory_type=MemoryType.PROCEDURAL,
                content="For market opportunity analysis, run landscape research, competitor analysis, synthesis, critique, evaluation, and memory update.",
                metadata={"workflow": "market_opportunity_analysis"},
            ),
            MemoryRecord(
                memory_type=MemoryType.STRATEGIC,
                content="Prioritize evidence-backed opportunities with defensible data access and enterprise integration paths.",
                metadata={"priority": "enterprise_ai"},
            ),
        ]
        self.records.extend(records)
        return records

