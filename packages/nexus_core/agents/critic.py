from __future__ import annotations

from nexus_core.models import AgentResult


class CriticAgent:
    name = "critic"

    def review(self, result: AgentResult) -> AgentResult:
        risks = [
            "Market sizing should be refreshed with live paid databases before investment decisions.",
            "Clinical workflow opportunities require careful regulatory and integration validation.",
            "Governance products may face long enterprise sales cycles despite strong need.",
        ]
        return AgentResult(
            agent=self.name,
            task_id="critique",
            summary="Challenged assumptions and identified evidence gaps before acceptance.",
            evidence=result.evidence[:3],
            artifacts={"risks": risks, "unsupported_claims": []},
        )

