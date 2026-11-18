import unittest

from research import (
    load_settings,
    search_sources,
    validate_query,
    offline_summary,
    validate_summary,
)


class ResearchTests(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(load_settings()["provider"], "openai")

    def test_all_frameworks(self):
        self.assertEqual(len(search_sources("Compare frameworks")), 4)

    def test_targeted_research(self):
        self.assertEqual(len(search_sources("LangGraph and CrewAI")), 2)

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            validate_query("")

    def test_oversized_query(self):
        with self.assertRaises(ValueError):
            validate_query("x" * 501)

    def test_valid_citations(self):
        sources = search_sources("LangGraph")
        self.assertTrue(
            validate_summary(offline_summary(sources), sources)
        )

    def test_invalid_citations(self):
        with self.assertRaises(ValueError):
            validate_summary("Invalid [XX99]", [{"id": "LG01"}])

    def test_missing_citations(self):
        with self.assertRaises(ValueError):
            validate_summary("No citation", [{"id": "LG01"}])
