FROM python:3.10-slim

ARG FRAMEWORK=langgraph

ENV FRAMEWORK=${FRAMEWORK} \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANGSMITH_TRACING=false \
    CREWAI_DISABLE_TELEMETRY=true \
    CREWAI_TRACING_ENABLED=false \
    OTEL_SDK_DISABLED=true

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/ /tmp/requirements/

RUN case "$FRAMEWORK" in \
      langgraph|crewai) ;; \
      *) exit 1 ;; \
    esac \
    && python -m pip install --no-cache-dir \
       -r "/tmp/requirements/${FRAMEWORK}.lock.txt" \
    && python -m pip check

RUN useradd --create-home --uid 10001 appuser

COPY research.py langgraph_demo.py crewai_demo.py ./
COPY config/ config/
COPY data/ data/
COPY tests/ tests/

USER appuser

CMD ["sh", "-c", "exec python \"${FRAMEWORK}_demo.py\""]
