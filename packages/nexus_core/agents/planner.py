from __future__ import annotations

from nexus_core.models import ExecutionPlan, Task


class PlannerAgent:
    name = "planner"

    def create_plan(self, objective: str) -> ExecutionPlan:
        tasks = [
            Task(
                title="Market landscape research",
                description="Collect recent evidence about market size, adoption, buyer pain, and regulatory forces.",
                owner="research",
            ),
            Task(
                title="Competitor and funding analysis",
                description="Map notable companies, funding patterns, partnerships, and underserved niches.",
                owner="research",
            ),
            Task(
                title="Opportunity synthesis",
                description="Generate and rank startup opportunities using evidence, feasibility, and differentiation.",
                owner="reasoning",
            ),
            Task(
                title="Critical review",
                description="Challenge unsupported claims, weak assumptions, and missing evidence.",
                owner="critic",
            ),
            Task(
                title="Evaluation and memory update",
                description="Score the output, store accepted findings, and update reusable procedures.",
                owner="evaluator",
            ),
        ]
        return ExecutionPlan(
            objective=objective,
            tasks=tasks,
            milestones=[
                "Evidence set assembled",
                "Opportunities scored",
                "Critique resolved",
                "Final report stored in memory",
            ],
        )

