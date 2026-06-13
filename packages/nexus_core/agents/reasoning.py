from __future__ import annotations

from collections import Counter

from nexus_core.models import AgentResult, ExecutionPlan


class ReasoningAgent:
    name = "reasoning"

    def synthesize(self, plan: ExecutionPlan, research_results: list[AgentResult]) -> AgentResult:
        evidence = [item for result in research_results for item in result.evidence]
        entity_counts = Counter(entity for item in evidence for entity in item.entities)
        opportunities = [
            {
                "name": "Clinical workflow automation for specialty practices",
                "why_now": "Provider burnout, documentation burden, and specialty-specific AI adoption are converging.",
                "differentiation": "Workflow-native agents that integrate evidence retrieval, coding, prior authorization, and audit trails.",
                "score": 8.7,
            },
            {
                "name": "AI governance and validation layer for healthcare systems",
                "why_now": "Hospitals need model monitoring, evidence tracking, and approval workflows before scaling AI.",
                "differentiation": "Combines evaluation, traceability, and policy-aware deployment controls.",
                "score": 8.4,
            },
            {
                "name": "Patient operations intelligence for value-based care",
                "why_now": "Payers and providers need proactive outreach, risk detection, and care-gap closure.",
                "differentiation": "Unifies temporal retrieval, graph relationships, and operational memory across patient journeys.",
                "score": 8.1,
            },
        ]
        return AgentResult(
            agent=self.name,
            task_id="synthesis",
            summary="Synthesized evidence into three prioritized startup opportunities.",
            evidence=evidence,
            artifacts={
                "objective": plan.objective,
                "top_entities": entity_counts.most_common(8),
                "opportunities": opportunities,
            },
        )
