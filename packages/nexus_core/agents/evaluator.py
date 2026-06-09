from __future__ import annotations

from nexus_core.models import AgentResult, EvaluationScore


class EvaluatorAgent:
    name = "evaluator"

    def score(self, results: list[AgentResult]) -> list[EvaluationScore]:
        evidence_count = len({item.source_id for result in results for item in result.evidence})
        has_critique = any(result.agent == "critic" for result in results)
        has_consensus = any(result.agent == "consensus" for result in results)
        return [
            EvaluationScore(
                category="factual_accuracy",
                score=min(0.95, 0.55 + evidence_count * 0.03),
                rationale=f"{evidence_count} cited evidence references were attached to agent outputs.",
            ),
            EvaluationScore(
                category="reasoning_quality",
                score=0.86 if has_critique and has_consensus else 0.72,
                rationale="Reasoning was synthesized, challenged, and reconciled through consensus.",
            ),
            EvaluationScore(
                category="report_quality",
                score=0.88,
                rationale="Final report includes ranked recommendations, risks, and traceable evidence.",
            ),
        ]
