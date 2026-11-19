# System Architecture

## Implemented Workflows

```mermaid
flowchart TD
    Q[Research Query] --> I[Input Validation]
    I --> L[LangGraph Research Node]
    I --> C[CrewAI Researcher]
    L --> R[Shared Research Corpus]
    C --> R
    R --> LS[LangGraph Summarization Node]
    R --> CS[CrewAI Summarizer]
    L -.-> M[In-Memory Checkpoint]
    LS -.-> M
    LS --> V[Citation Validation]
    CS --> V
    V --> O[Structured Output and Metrics]
```

Both implementations use isolated dependencies, shared model configuration and non-root Docker containers.

## Proposed Production Architecture

```mermaid
flowchart TD
    U[Client] --> A[Authenticated API]
    A --> Q[Task Queue]
    Q --> W[Agent Workers]
    W --> P[PostgreSQL]
    W --> G[Model Gateway]
    W --> T[Approved Tools and MCP]
    G --> L[LLM Providers]
    V[Vault] -.-> W
    W --> O[OpenTelemetry]
    O --> M[Monitoring and Logging]
```

## Design Decisions

| Decision | Rationale |
|---|---|
| Isolated workers | Dependency and workload separation |
| Model gateway | Routing, quotas and cost management |
| Persistent state | Recovery and workflow continuity |
| Restricted tools | Least-privilege execution |
| Centralized telemetry | Operational visibility and auditability |

The production architecture is proposed. Only the offline proof-of-concept workflows have been deployed locally and validated.
