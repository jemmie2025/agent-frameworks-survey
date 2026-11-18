import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_settings():
    return json.loads(
        (ROOT / "config/settings.json").read_text()
    )


def validate_query(query):
    query = query.strip()
    limit = load_settings()["max_query_chars"]

    if not query or len(query) > limit:
        raise ValueError(
            f"Query must contain 1-{limit} characters"
        )

    return query


def search_sources(query):
    query = validate_query(query).casefold()
    settings = load_settings()

    sources = json.loads(
        (ROOT / settings["research_source"]).read_text()
    )

    selected = [
        source for source in sources
        if source["framework"].casefold() in query
    ]

    return selected or sources


def offline_summary(sources):
    return "\n".join(
        f'- {source["framework"]}: '
        f'{source["content"]} [{source["id"]}]'
        for source in sources
    )


def validate_summary(summary, sources):
    expected = {source["id"] for source in sources}
    citations = set(
        re.findall(r"\[([A-Z]{2}\d{2})\]", summary)
    )

    if not summary.strip() or citations != expected:
        raise ValueError("Source citation validation failed")

    return True
