from nexus_core import NexusEngine
from nexus_core.models import TaskStatus


def test_engine_runs_healthcare_market_demo() -> None:
    trace = NexusEngine().run("Analyze the AI healthcare market and identify three startup opportunities.")

    assert trace.completed_at is not None
    assert len(trace.plan.tasks) == 5
    assert all(task.status == TaskStatus.COMPLETE.value for task in trace.plan.tasks)
    assert any(result.agent == "critic" for result in trace.agent_results)
    assert "Recommended Startup Opportunities" in trace.report
    assert len(trace.memory_records) == 4
