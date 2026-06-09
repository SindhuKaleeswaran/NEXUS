from __future__ import annotations

from nexus_core.models import AgentResult


class ConsensusAgent:
    name = "consensus"

    def resolve(self, results: list[AgentResult]) -> AgentResult:
        evidence = [item for result in results for item in result.evidence]
        return AgentResult(
            agent=self.name,
            task_id="consensus",
            summary="Accepted the ranked opportunities with explicit caveats and validation requirements.",
            evidence=evidence[:5],
            artifacts={
                "decision": "Proceed with deeper validation on all three opportunities.",
                "approval_required": True,
                "next_gate": "Human review plus live market data refresh",
            },
        )

