# Agent Frameworks Survey

[![CI](https://github.com/jemmie2025/agent-frameworks-survey/actions/workflows/ci.yml/badge.svg)](https://github.com/jemmie2025/agent-frameworks-survey/actions)

## Overview

Engineering evaluation of LangGraph, CrewAI, AutoGen and Claude Agent SDK to determine their suitability for enterprise AI orchestration, operational reliability and deployment efficiency.

## Implementations

- **LangGraph:** Stateful research workflow with explicit graph execution, checkpointing and citation validation.
- **CrewAI:** Role-based research and summarization agents with controlled tool execution and sequential task handoff.

Both implementations use a shared research corpus and configurable model settings.

## Verified Results

| Metric | LangGraph | CrewAI |
|---|---:|---:|
| Benchmark success | 5/5 | 5/5 |
| Median workflow latency | 10 ms | 190.7 ms |
| Mean end-to-end latency | 903.71 ms | 4145.19 ms |
| Docker disk usage | 298 MB | 1.51 GB |

- 16 automated tests passed.
- Consistent source-referenced outputs.
- Non-root, network-isolated containers.
- Successful GitHub Actions validation.

Results represent deterministic offline execution, not live LLM inference.

## Quick Start

Requirements: Docker and GNU Make.

```bash
git clone https://github.com/jemmie2025/agent-frameworks-survey.git
cd agent-frameworks-survey
make docker-build
make docker-test
```

No API credentials are required for offline execution.

## Engineering Controls

Pinned dependencies, isolated environments, configurable execution limits, restricted tools, protected credentials, structured execution metrics and automated CI validation.

## Documentation

- [Technical Evaluation and Decision Matrix](report.md)
- [System Architecture](docs/architecture.md)
- [Operational Runbook](docs/runbook.md)
- [Performance Benchmarks](evidence/benchmark-results.json)
- [Automated Test Results](evidence/test-results.txt)

## Recommendation

Adopt LangGraph for controlled, stateful enterprise workflows and CrewAI for collaborative multi-agent workloads. Consider Claude Agent SDK for Claude-native automation.

AutoGen is archived; evaluate Microsoft Agent Framework for new implementations.

## Status

Validated offline proof of concept. Live inference, persistent recovery, vulnerability scanning and production load testing remain outstanding.

## Validation Evidence

### Automated Testing

All 16 automated tests passed across both framework implementations.

![Automated Test Results](evidence/screenshots/01-agent-framework-test-results.png)

### Performance and Container Validation

Repeated benchmarks, Docker image comparison and non-root execution validation.

![Performance and Docker Validation](evidence/screenshots/02-performance-and-docker-validation.png)
