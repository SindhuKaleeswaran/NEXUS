# NEXUS

NEXUS is a production-shaped autonomous enterprise intelligence platform scaffold. It turns high-level organizational goals into observable, evidence-backed execution through coordinated agents, hybrid retrieval, persistent memory, evaluation, and report generation.

This repository is intentionally built as a deployable foundation rather than a toy chatbot. The current implementation includes a deterministic end-to-end demo workflow that can run locally without model keys, while preserving service boundaries for LLMs, Qdrant, Neo4j, PostgreSQL, Redis, evaluators, and cloud deployment.

## What It Does

- Decomposes broad goals into task graphs.
- Runs specialized planner, research, retrieval, reasoning, critic, evaluator, and consensus agents.
- Grounds conclusions in an evidence set with temporal, vector-style, and graph-style signals.
- Scores factual support, reasoning quality, and report utility.
- Stores episodic, semantic, procedural, and strategic memory records.
- Produces an executive report and machine-readable workflow trace.
- Provides a Next.js enterprise dashboard scaffold for goal submission, agent monitoring, memory, graph, evaluation, and metrics.

## Repository Layout

```text
apps/
  api/                 FastAPI gateway for workflow execution
  web/                 Next.js TypeScript frontend
packages/
  nexus_core/          Core orchestration, agents, retrieval, memory, evaluation
infra/
  docker/              Docker Compose stack for local services
  k8s/                 Kubernetes manifests
  terraform/           Cloud infrastructure starting point
examples/              Demo objectives and sample outputs
docs/                  Architecture and operations notes
scripts/               Local demo utilities
```

## Quick Start

Run the deterministic workflow locally:

```powershell
python scripts/run_demo.py
```

Run the API after installing dependencies:

```powershell
python -m pip install -e .
uvicorn nexus_api.main:app --app-dir apps/api --reload
```

Run the frontend after installing dependencies in `apps/web`:

```powershell
cd apps/web
npm install
npm run dev
```

## Demo Objective

```text
Analyze the AI healthcare market and identify three startup opportunities.
```

The demo creates a plan, spawns agents, retrieves market evidence, performs critique and evaluation, generates a report, and stores organizational memory.

