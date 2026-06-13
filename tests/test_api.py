import httpx
import pytest

from nexus_api.main import app


@pytest.mark.asyncio
async def test_health_endpoint() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "nexus-api"}


@pytest.mark.asyncio
async def test_run_goal_endpoint_returns_completed_trace() -> None:
    objective = "Analyze the AI healthcare market and identify three startup opportunities."

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.post("/goals/run", json={"objective": objective})

    assert response.status_code == 200
    trace = response.json()
    assert trace["objective"] == objective
    assert all(task["status"] == "complete" for task in trace["plan"]["tasks"])
    assert objective in trace["report"]


@pytest.mark.asyncio
async def test_run_goal_rejects_short_objective() -> None:
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.post("/goals/run", json={"objective": "Too short"})

    assert response.status_code == 422
