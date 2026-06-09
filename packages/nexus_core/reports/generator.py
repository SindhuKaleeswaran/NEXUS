from __future__ import annotations

from nexus_core.models import AgentResult, EvaluationScore, ExecutionPlan


class ReportGenerator:
    def generate(
        self,
        objective: str,
        plan: ExecutionPlan,
        results: list[AgentResult],
        evaluation: list[EvaluationScore],
    ) -> str:
        synthesis = next(result for result in results if result.agent == "reasoning")
        critique = next(result for result in results if result.agent == "critic")
        opportunities = synthesis.artifacts["opportunities"]
        evidence_titles = sorted({item.title for result in results for item in result.evidence})

        lines = [
            "# NEXUS Intelligence Report",
            "",
            f"Objective: {objective}",
            "",
            "## Execution Plan",
            *[f"- {task.title}: {task.description}" for task in plan.tasks],
            "",
            "## Recommended Startup Opportunities",
            *[
                f"- {item['name']} (score {item['score']}): {item['why_now']} Differentiation: {item['differentiation']}"
                for item in opportunities
            ],
            "",
            "## Critic Review",
            *[f"- {risk}" for risk in critique.artifacts["risks"]],
            "",
            "## Evaluation",
            *[f"- {score.category}: {score.score:.2f} - {score.rationale}" for score in evaluation],
            "",
            "## Evidence",
            *[f"- {title}" for title in evidence_titles],
        ]
        return "\n".join(lines)

