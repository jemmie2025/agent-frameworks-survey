# Operational Runbook

## Local Setup

Requires Python 3.10, Docker and GNU Make.

```bash
python3 -m venv .venv-langgraph
python3 -m venv .venv-crewai

.venv-langgraph/bin/python -m pip install -r requirements/langgraph.lock.txt
.venv-crewai/bin/python -m pip install -r requirements/crewai.lock.txt
```

## Execution and Validation

```bash
.venv-langgraph/bin/python langgraph_demo.py
.venv-crewai/bin/python crewai_demo.py

make test
make benchmark
make docker-build
make docker-test
```

## Optional Live Execution

Requires authorized OpenAI API credentials and available API credits.

```bash
read -rs -p "OpenAI API key: " OPENAI_API_KEY
echo
export OPENAI_API_KEY

timeout 240s .venv-langgraph/bin/python langgraph_demo.py --live
timeout 240s .venv-crewai/bin/python crewai_demo.py --live

unset OPENAI_API_KEY
```

Never commit credentials. Live execution remains unverified.

## Troubleshooting

| Issue | Resolution |
|---|---|
| Dependency conflict | Reinstall from the appropriate lock file |
| Invalid citation | Inspect research corpus and source identifiers |
| Missing credentials | Inject authorized environment variables |
| Docker unavailable | Verify Docker Desktop and docker info |
| CI failure | Inspect the failed workflow job |
| Deprecation warning | Review upstream releases |

## Monitoring and Recovery

Inspect execution JSON for run ID, latency, source count, token usage and validation status.

For rollback, use a known-good Git revision and its dependency lock files. Production state recovery and backup restoration require additional validation.
