import unittest
from crewai_demo import run


class CrewAITests(unittest.TestCase):

    def test_workflow(self):
        result = run("Compare frameworks")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["sources_retrieved"], 4)
        self.assertTrue(result["citation_validation"])

    def test_agent_handoff(self):
        result = run("LangGraph and CrewAI")
        self.assertEqual(result["agents"], 2)
        self.assertEqual(result["tasks_completed"], 2)
        self.assertEqual(result["tool_calls"], 1)
        self.assertEqual(result["sources_retrieved"], 2)

    def test_offline_usage(self):
        result = run("CrewAI")
        self.assertEqual(result["usage"]["input_tokens"], 0)
        self.assertEqual(result["usage"]["output_tokens"], 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            run("")
