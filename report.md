# Agent Frameworks Survey — Technical Evaluation

## 1. Executive Summary

This assessment evaluates four AI agent frameworks against orchestration control, model integration, tool extensibility, state management, observability and production maturity.

LangGraph and CrewAI were implemented and benchmarked using a shared research corpus. Both passed functional validation, automated testing and containerized execution.

LangGraph is the preferred option for controlled enterprise workflows, while CrewAI is recommended for specialized agent collaboration.

## 2. Framework Comparison Matrix

| Capability | LangGraph | CrewAI | AutoGen | Claude Agent SDK |
|---|---|---|---|---|
| Execution model | State graph | Role-based crews and flows | Conversational, event-driven | Autonomous agent loop |
| Execution control | Nodes, edges and routing | Tasks, processes and flows | Message passing | SDK-managed |
| Model support | Multiple providers | Multiple providers | Model client adapters | Claude models |
| Tool integration | Functions, LangChain, MCP | Custom tools, MCP | Functions, extensions, MCP | Built-in tools, custom tools, MCP |
| State management | Checkpointing | Flow state and persistence | Agent and team state | Sessions |
| Memory | Thread state and external stores | Configurable memory | Memory integrations | Session context |
| Observability | LangSmith, streaming | Tracing, event listeners | Logging, OpenTelemetry | Hooks, streaming, OpenTelemetry |
| Human approval | Interrupts | Human feedback | User interaction | Permission controls |
| Production maturity | Strong orchestration foundation | Suitable with controlled Flows | Archived | Claude-centric, requires secure hosting |
| Operational trade-off | More explicit engineering | Additional orchestration overhead | Unsupported lifecycle | Provider dependency |
| Best fit | Durable workflows | Agent collaboration | Legacy migration | Autonomous tool-driven automation |

Microsoft has archived AutoGen and recommends Microsoft Agent Framework for new implementations. Continued AutoGen deployment introduces maintenance and security risks.

## 3. Models and Configuration

| Parameter | Configuration |
|---|---|
| Validated model | Deterministic offline baseline |
| Configured live model | gpt-5.4-mini-2026-03-17 |
| Provider | OpenAI |
| Reasoning effort | none |
| Output token limit | 700 per configured request |
| Request timeout | 60 seconds |
| Benchmark process timeout | 240 seconds |
| Retry limit | 1 configured retry |
| CrewAI iteration limit | 3 per agent |
| Research tool limit | 3 calls |
| Maximum query length | 500 characters |

Configuration is centralized in config/settings.json.

LangGraph integrates the OpenAI Responses API; CrewAI uses its LLM abstraction.

Alternative model candidates include Claude Sonnet for Claude-native workflows and Qwen or Llama for self-hosted inference. These alternatives were not benchmarked.

## 4. Proof of Concept

**LangGraph:** StateGraph orchestrates research, summarization and citation validation. InMemorySaver provides thread-scoped checkpointing.

**CrewAI:** A researcher retrieves evidence through a restricted tool. A summarizer receives the research task output and produces a cited report. Delegation, caching and persistent memory are disabled.

Both workflows return structured execution metadata and source-referenced results.

## 5. Evaluation Methodology

Environment: WSL2 Ubuntu, Python 3.10.12, Docker 29.9.3.

Dependencies: LangGraph 1.2.22, CrewAI 1.15.39 and OpenAI SDK 2.54.0.

Five independent executions per framework used identical research inputs and a deterministic model baseline. Internal workflow latency and full process execution time were measured separately.

## 6. Measured Results

| Metric | LangGraph | CrewAI |
|---|---:|---:|
| Successful executions | 5/5 | 5/5 |
| Mean orchestration latency | 9.94 ms | 210.48 ms |
| Median orchestration latency | 10.00 ms | 190.70 ms |
| Minimum orchestration latency | 7.40 ms | 160.00 ms |
| Maximum orchestration latency | 13.30 ms | 292.50 ms |
| Mean end-to-end latency | 903.71 ms | 4145.19 ms |
| Median end-to-end latency | 878.37 ms | 4073.05 ms |
| Docker disk usage | 298 MB | 1.51 GB |
| Image content size | 65.2 MB | 355 MB |
| Sources retrieved | 4/4 | 4/4 |
| Citation validation | Passed | Passed |
| Network isolation | Passed | Passed |
| Non-root execution | Passed | Passed |

LangGraph demonstrated lower offline orchestration overhead and a smaller container footprint. Both frameworks produced consistent outputs.

These measurements do not establish live inference performance, model quality or production throughput.

## 7. Quality and Operational Controls

| Control | Verified implementation |
|---|---|
| Automated testing | 16 tests, zero failures |
| Reproducibility | Isolated, pinned dependency lock files |
| Container security | Non-root UID 10001 |
| Network security | Offline execution without network access |
| Input validation | Query length and empty-input rejection |
| Output validation | Expected source ID enforcement |
| Observability | Run ID, duration, token usage and execution status |
| CI | Matrix-based container and integration validation |
| Secrets | Environment-based credentials and Git/Docker exclusions |

## 8. Production Recommendations

Deploy workers through Kubernetes or Nomad behind an authenticated API and task queue.

Use PostgreSQL for durable state, Vault for secrets, a model gateway for routing and budgets, OpenTelemetry for tracing, and Prometheus/Grafana for monitoring.

Enforce tool permissions, network restrictions, resource limits, audit logging and human approval for sensitive operations.

These components constitute a proposed production architecture, not deployed infrastructure.

## 9. Decision Matrix by Use Case

| Use Case | Recommendation | Rationale |
|---|---|---|
| Enterprise workflow automation | LangGraph | Explicit execution control |
| Financial compliance | LangGraph | State and approval boundaries |
| RAG and knowledge assistants | LangGraph | Retrieval and state integration |
| Collaborative research | CrewAI | Specialized agent roles |
| Multi-agent reporting | CrewAI | Structured task collaboration |
| Autonomous coding | Claude Agent SDK | Native tools and permissions |
| Existing AutoGen workloads | Microsoft Agent Framework migration | Supported lifecycle |
| Simple summarization | Direct LLM API | Lower architectural complexity |

## 10. Limitations and Readiness Gates

Before production adoption, validate live inference, model accuracy, actual costs, concurrent workloads, persistent recovery, vulnerability scanning, external monitoring and adversarial tool-use scenarios.

Citation validation verifies source identifiers, not factual correctness. CrewAI dependency deprecation warnings require lifecycle monitoring but did not cause test failures.

## 11. Evidence and References

Evidence: [Automated tests](evidence/test-results.txt), [Benchmarks](evidence/benchmark-results.json), [Docker images](evidence/docker-images.txt), [LangGraph execution](evidence/langgraph-docker.json), [CrewAI execution](evidence/crewai-docker.json).

Official documentation:

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [CrewAI](https://docs.crewai.com/en/concepts/flows)
- [AutoGen](https://github.com/microsoft/autogen)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)

## Conclusion

LangGraph is the recommended baseline for controlled enterprise orchestration. CrewAI is a suitable alternative where agent specialization is essential. Final production selection requires workload-specific live model and security validation.
