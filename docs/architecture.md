# NEXUS Architecture

NEXUS is organized around independently deployable services connected by explicit workflow traces.

## Service Boundaries

- API Gateway: receives goals, exposes workflow status, and enforces auth.
- Planner Service: decomposes goals into task DAGs and milestones.
- Agent Service: executes specialized agent roles and records outputs.
- Retrieval Service: combines vector retrieval, graph traversal, temporal ranking, and reranking.
- Memory Service: persists episodic, semantic, procedural, and strategic memory.
- Evaluation Service: scores factual support, reasoning quality, retrieval quality, and report usefulness.
- Observability Service: exports traces, costs, latency, errors, and source utilization.
- Frontend Service: provides goal submission, agent monitoring, reasoning visualization, memory exploration, and dashboards.

## Data Planes

- Qdrant stores dense vectors for semantic similarity.
- Neo4j stores entities and relationships for multi-hop graph retrieval.
- PostgreSQL stores workflow state, structured memories, approvals, identities, and audit logs.
- Redis provides cache and short-lived workflow coordination.
- Object storage stores source documents, reports, and evaluation artifacts.

## Control Plane

The orchestration engine runs a DAG for each objective:

1. Plan the goal.
2. Retrieve evidence.
3. Synthesize conclusions.
4. Critique assumptions.
5. Reach consensus.
6. Evaluate quality.
7. Store accepted memory.
8. Publish report and trace.

The local implementation uses deterministic adapters. Production deployments can swap in LangGraph, Temporal, Ray, Kafka, Qdrant, Neo4j, PostgreSQL, Redis, Langfuse, Prometheus, Grafana, OpenTelemetry, and MLflow without changing the user-facing contract.

