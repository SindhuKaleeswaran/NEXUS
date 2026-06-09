from __future__ import annotations

from datetime import UTC, datetime

from nexus_core.agents.consensus import ConsensusAgent
from nexus_core.agents.critic import CriticAgent
from nexus_core.agents.evaluator import EvaluatorAgent
from nexus_core.agents.planner import PlannerAgent
from nexus_core.agents.reasoning import ReasoningAgent
from nexus_core.agents.research import ResearchAgent
from nexus_core.memory.store import MemoryStore
from nexus_core.models import WorkflowTrace
from nexus_core.reports.generator import ReportGenerator
from nexus_core.retrieval.hybrid import HybridRetriever


class NexusEngine:
    """Coordinates the NEXUS autonomous execution workflow."""

    def __init__(self) -> None:
        self.retriever = HybridRetriever()
        self.memory = MemoryStore()
        self.planner = PlannerAgent()
        self.research = ResearchAgent(self.retriever)
        self.reasoning = ReasoningAgent()
        self.critic = CriticAgent()
        self.evaluator = EvaluatorAgent()
        self.consensus = ConsensusAgent()
        self.reporter = ReportGenerator()

    def run(self, objective: str) -> WorkflowTrace:
        plan = self.planner.create_plan(objective)
        trace = WorkflowTrace(objective=objective, plan=plan, agent_results=[], evaluation=[], report="", memory_records=[])

        research_results = [self.research.execute(task) for task in plan.tasks if task.owner == "research"]
        trace.agent_results.extend(research_results)

        reasoning_result = self.reasoning.synthesize(plan, research_results)
        critique_result = self.critic.review(reasoning_result)
        consensus_result = self.consensus.resolve([reasoning_result, critique_result])

        trace.agent_results.extend([reasoning_result, critique_result, consensus_result])
        trace.evaluation = self.evaluator.score(trace.agent_results)
        trace.report = self.reporter.generate(objective, plan, trace.agent_results, trace.evaluation)
        trace.memory_records = self.memory.persist_workflow(trace)
        trace.completed_at = datetime.now(UTC)
        return trace

