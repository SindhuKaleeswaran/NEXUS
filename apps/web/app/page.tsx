"use client";

import { Activity, BrainCircuit, Database, GitBranch, Goal, Gauge, Network, ShieldCheck } from "lucide-react";
import { useMemo, useState } from "react";

type Trace = {
  objective: string;
  plan: { tasks: Array<{ title: string; owner: string; description: string; status: string }> };
  agent_results: Array<{ agent: string; summary: string; artifacts: Record<string, unknown>; evidence: Array<{ title: string; score: number }> }>;
  evaluation: Array<{ category: string; score: number; rationale: string }>;
  report: string;
  memory_records: Array<{ memory_type: string; content: string }>;
};

const demoTrace: Trace = {
  objective: "Analyze the AI healthcare market and identify three startup opportunities.",
  plan: {
    tasks: [
      { title: "Market landscape research", owner: "research", status: "complete", description: "Collect market, adoption, buyer pain, and regulatory evidence." },
      { title: "Competitor and funding analysis", owner: "research", status: "complete", description: "Map companies, funding patterns, partnerships, and underserved niches." },
      { title: "Opportunity synthesis", owner: "reasoning", status: "complete", description: "Generate and rank startup opportunities." },
      { title: "Critical review", owner: "critic", status: "complete", description: "Challenge unsupported claims and missing evidence." },
      { title: "Evaluation and memory update", owner: "evaluator", status: "complete", description: "Score output and persist accepted learning." }
    ]
  },
  agent_results: [
    { agent: "planner", summary: "Created a five-stage execution graph.", artifacts: {}, evidence: [] },
    { agent: "research", summary: "Retrieved evidence across market, funding, regulation, and operations.", artifacts: {}, evidence: [{ title: "Healthcare AI adoption and workflow automation trends", score: 0.93 }] },
    { agent: "reasoning", summary: "Synthesized evidence into three prioritized startup opportunities.", artifacts: {}, evidence: [{ title: "Funding patterns in healthcare AI infrastructure", score: 0.89 }] },
    { agent: "critic", summary: "Flagged regulatory, sales-cycle, and live-data validation risks.", artifacts: {}, evidence: [] },
    { agent: "consensus", summary: "Accepted recommendations with human review and market refresh gate.", artifacts: {}, evidence: [] }
  ],
  evaluation: [
    { category: "factual_accuracy", score: 0.91, rationale: "Cited evidence references were attached to agent outputs." },
    { category: "reasoning_quality", score: 0.86, rationale: "Reasoning was synthesized, challenged, and reconciled." },
    { category: "report_quality", score: 0.88, rationale: "Report includes ranked recommendations, risks, and traceability." }
  ],
  report: "Recommended opportunities: clinical workflow automation, AI governance validation, and patient operations intelligence.",
  memory_records: [
    { memory_type: "episodic", content: "Completed healthcare AI opportunity analysis." },
    { memory_type: "semantic", content: "Healthcare AI opportunities are strongest where workflow ROI and governance are measurable." },
    { memory_type: "procedural", content: "Market analysis workflow now includes research, synthesis, critique, evaluation, and memory update." },
    { memory_type: "strategic", content: "Prioritize defensible data access and enterprise integration paths." }
  ]
};

const nav = [
  { label: "Goals", icon: Goal },
  { label: "Agents", icon: BrainCircuit },
  { label: "Graph", icon: Network },
  { label: "Memory", icon: Database },
  { label: "Evaluation", icon: ShieldCheck },
  { label: "Metrics", icon: Gauge }
];

const apiUrl = process.env.NEXT_PUBLIC_NEXUS_API_URL ?? "http://localhost:8000";

export default function Page() {
  const [objective, setObjective] = useState(demoTrace.objective);
  const [trace, setTrace] = useState<Trace>(demoTrace);
  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const averageScore = useMemo(() => {
    if (trace.evaluation.length === 0) {
      return 0;
    }
    const total = trace.evaluation.reduce((sum, item) => sum + item.score, 0);
    return Math.round((total / trace.evaluation.length) * 100);
  }, [trace]);

  async function runGoal() {
    const normalizedObjective = objective.trim();
    if (normalizedObjective.length < 10) {
      setError("Enter an objective with at least 10 characters.");
      return;
    }

    setIsRunning(true);
    setError(null);
    try {
      const response = await fetch(`${apiUrl}/goals/run`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ objective: normalizedObjective })
      });
      if (!response.ok) {
        throw new Error(`The workflow service returned ${response.status}.`);
      }
      setTrace(await response.json());
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : "Unable to run the workflow.");
    } finally {
      setTimeout(() => setIsRunning(false), 450);
    }
  }

  return (
    <main className="shell">
      <aside className="sidebar" aria-label="Primary navigation">
        <div className="brand">
          <GitBranch size={22} />
          <span>NEXUS</span>
        </div>
        <nav>
          {nav.map((item) => (
            <button key={item.label} title={item.label} className="navButton">
              <item.icon size={18} />
              <span>{item.label}</span>
            </button>
          ))}
        </nav>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="eyebrow">Autonomous enterprise intelligence</p>
            <h1>Goal Execution Control Plane</h1>
          </div>
          <div className="statusPill">
            <Activity size={16} />
            {isRunning ? "Running" : "Observable"}
          </div>
        </header>

        <section className="goalBand">
          <div className="goalInput">
            <label htmlFor="objective">Objective</label>
            <textarea
              id="objective"
              value={objective}
              onChange={(event) => setObjective(event.target.value)}
            />
            {error && <p className="errorMessage" role="alert">{error}</p>}
          </div>
          <button onClick={runGoal} disabled={isRunning || objective.trim().length < 10}>
            <BrainCircuit size={18} />
            {isRunning ? "Executing" : "Run Goal"}
          </button>
        </section>

        <section className="metricsGrid">
          <div className="metric"><span>Tasks</span><strong>{trace.plan.tasks.length}</strong></div>
          <div className="metric"><span>Agents</span><strong>{trace.agent_results.length}</strong></div>
          <div className="metric"><span>Quality</span><strong>{averageScore}%</strong></div>
          <div className="metric"><span>Memories</span><strong>{trace.memory_records.length}</strong></div>
        </section>

        <section className="contentGrid">
          <div className="panel wide">
            <h2>Execution DAG</h2>
            <div className="timeline">
              {trace.plan.tasks.map((task, index) => (
                <div className="task" key={task.title}>
                  <div className="taskIndex">{index + 1}</div>
                  <div>
                    <strong>{task.title}</strong>
                    <p>{task.owner} · {task.description}</p>
                  </div>
                  <span>{task.status}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="panel">
            <h2>Agent Monitor</h2>
            {trace.agent_results.map((result) => (
              <article className="agent" key={`${result.agent}-${result.summary}`}>
                <strong>{result.agent}</strong>
                <p>{result.summary}</p>
              </article>
            ))}
          </div>

          <div className="panel">
            <h2>Evaluation</h2>
            {trace.evaluation.map((item) => (
              <div className="score" key={item.category}>
                <div><strong>{item.category.replace("_", " ")}</strong><span>{Math.round(item.score * 100)}%</span></div>
                <progress value={item.score} max={1} />
                <p>{item.rationale}</p>
              </div>
            ))}
          </div>

          <div className="panel">
            <h2>Memory Explorer</h2>
            {trace.memory_records.map((record) => (
              <article className="memory" key={`${record.memory_type}-${record.content}`}>
                <span>{record.memory_type}</span>
                <p>{record.content}</p>
              </article>
            ))}
          </div>

          <div className="panel wide">
            <h2>Final Report</h2>
            <pre>{trace.report}</pre>
          </div>
        </section>
      </section>
    </main>
  );
}
