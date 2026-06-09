# Operations

## Local Development

Run the deterministic demo:

```powershell
python scripts/run_demo.py
```

Run the API:

```powershell
python -m pip install -e .
uvicorn nexus_api.main:app --app-dir apps/api --reload
```

Run the dashboard:

```powershell
cd apps/web
npm install
npm run dev
```

## Local Infrastructure

```powershell
docker compose -f infra/docker/docker-compose.yml up --build
```

## Production Concerns

- Require authenticated users and scoped agent identities.
- Store every agent action in immutable audit logs.
- Gate memory writes through evaluator scores and approval rules.
- Emit OpenTelemetry traces for workflow steps and retrieval calls.
- Track model cost, latency, source utilization, and failure rate.
- Periodically compress memory into reusable semantic and procedural abstractions.

