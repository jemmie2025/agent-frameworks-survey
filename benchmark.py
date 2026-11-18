import json
import platform
import statistics
import subprocess
import time
from pathlib import Path

from research import load_settings

ROOT = Path(__file__).resolve().parent
RUNS = 5

FRAMEWORKS = {
    "LangGraph": [
        ".venv-langgraph/bin/python",
        "langgraph_demo.py",
    ],
    "CrewAI": [
        ".venv-crewai/bin/python",
        "crewai_demo.py",
    ],
}


def metrics(samples):
    return {
        "samples_ms": samples,
        "mean_ms": round(statistics.mean(samples), 2),
        "median_ms": round(statistics.median(samples), 2),
        "minimum_ms": round(min(samples), 2),
        "maximum_ms": round(max(samples), 2),
    }


def main():
    settings = load_settings()

    report = {
        "mode": "offline",
        "model": "deterministic-baseline",
        "runs_per_framework": RUNS,
        "platform": platform.platform(),
        "python": platform.python_version(),
        "results": {},
    }

    summaries = set()

    for framework, command in FRAMEWORKS.items():
        durations = []
        wall_times = []

        for _ in range(RUNS):
            started = time.perf_counter()

            process = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=settings["run_timeout_seconds"],
                check=True,
            )

            wall_times.append(round(
                (time.perf_counter() - started) * 1000, 2
            ))

            result = json.loads(process.stdout)

            if (
                result["status"] != "success"
                or not result["citation_validation"]
                or result["sources_retrieved"] != 4
                or result["mode"] != "offline"
            ):
                raise RuntimeError(
                    f"{framework} validation failed"
                )

            durations.append(round(
                result["duration_seconds"] * 1000, 2
            ))

            summaries.add(result["summary"])

        report["results"][framework] = {
            "successful_runs": len(durations),
            "orchestration": metrics(durations),
            "end_to_end": metrics(wall_times),
        }

    report["summary_consistency"] = len(summaries) == 1

    if not report["summary_consistency"]:
        raise RuntimeError("Framework outputs differ")

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
