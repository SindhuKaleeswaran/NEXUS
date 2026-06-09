from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "packages"))

from nexus_core import NexusEngine  # noqa: E402


def main() -> None:
    objective = "Analyze the AI healthcare market and identify three startup opportunities."
    trace = NexusEngine().run(objective)
    output_dir = ROOT / "examples"
    output_dir.mkdir(exist_ok=True)
    (output_dir / "latest_report.md").write_text(trace.report, encoding="utf-8")
    (output_dir / "latest_trace.json").write_text(
        json.dumps(asdict(trace), indent=2, default=str),
        encoding="utf-8",
    )
    print(trace.report)
    print("\nSaved examples/latest_report.md and examples/latest_trace.json")


if __name__ == "__main__":
    main()

