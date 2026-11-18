.RECIPEPREFIX := >
.DEFAULT_GOAL := help

.PHONY: help test benchmark docker-build docker-test

help:
> @echo "make test         - Run automated test suites"
> @echo "make benchmark    - Benchmark both frameworks"
> @echo "make docker-build - Build both container images"
> @echo "make docker-test  - Validate both containers"

test:
> python3 -m unittest discover -s tests -p 'test_research.py' -v
> .venv-langgraph/bin/python -m unittest discover -s tests -p 'test_langgraph.py' -v
> .venv-crewai/bin/python -m unittest discover -s tests -p 'test_crewai.py' -v

benchmark:
> python3 benchmark.py

docker-build:
> docker build --build-arg FRAMEWORK=langgraph -t agent-survey-langgraph:1.0.0 .
> docker build --build-arg FRAMEWORK=crewai -t agent-survey-crewai:1.0.0 .

docker-test:
> docker run --rm --network none agent-survey-langgraph:1.0.0
> docker run --rm --network none agent-survey-crewai:1.0.0
> docker run --rm --network none agent-survey-langgraph:1.0.0 id
> docker run --rm --network none agent-survey-crewai:1.0.0 id
