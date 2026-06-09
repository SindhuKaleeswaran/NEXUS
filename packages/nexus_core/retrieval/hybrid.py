from __future__ import annotations

from datetime import date

from nexus_core.models import Evidence


class HybridRetriever:
    """Deterministic hybrid retriever stub.

    Production adapters should replace the local corpus with Qdrant vector search,
    Neo4j entity traversal, temporal scoring, and cross-encoder reranking.
    """

    def __init__(self) -> None:
        self.corpus = [
            Evidence(
                source_id="report-health-ai-2026",
                title="Healthcare AI adoption and workflow automation trends",
                url="https://example.com/healthcare-ai-adoption",
                published_at="2026-04-18",
                summary="Hospitals are prioritizing AI for documentation, care operations, and administrative burden reduction.",
                entities=["Healthcare", "Clinical AI", "Workflow Automation", "Hospitals"],
                score=0.93,
            ),
            Evidence(
                source_id="funding-health-ai-2026",
                title="Funding patterns in healthcare AI infrastructure",
                url="https://example.com/health-ai-funding",
                published_at="2026-03-11",
                summary="Investors favor infrastructure, governance, and measurable operational ROI over broad AI assistants.",
                entities=["Healthcare", "Venture Capital", "AI Governance", "Infrastructure"],
                score=0.89,
            ),
            Evidence(
                source_id="regulatory-ai-2026",
                title="Operational requirements for safe clinical AI deployment",
                url="https://example.com/clinical-ai-governance",
                published_at="2026-02-02",
                summary="Healthcare organizations require monitoring, audit trails, human review, and model validation.",
                entities=["Regulation", "Audit Trails", "Model Evaluation", "Healthcare"],
                score=0.91,
            ),
            Evidence(
                source_id="value-care-ops-2025",
                title="Care gap closure and value-based operations",
                url="https://example.com/value-based-care-ai",
                published_at="2025-12-08",
                summary="Value-based care teams need longitudinal intelligence to prioritize outreach and reduce avoidable cost.",
                entities=["Value-Based Care", "Patient Operations", "Temporal Retrieval", "Payers"],
                score=0.86,
            ),
        ]

    def search(self, query: str, limit: int = 4) -> list[Evidence]:
        today = date.today()
        query_terms = {term.lower().strip(".,") for term in query.split()}

        def rank(item: Evidence) -> float:
            lexical = sum(1 for term in query_terms if term and term in item.summary.lower()) * 0.04
            year = int(item.published_at[:4])
            recency = max(0.0, 1.0 - ((today.year - year) * 0.15))
            graph_bonus = 0.05 if "Healthcare" in item.entities else 0.0
            return item.score + lexical + recency * 0.1 + graph_bonus

        return sorted(self.corpus, key=rank, reverse=True)[:limit]

