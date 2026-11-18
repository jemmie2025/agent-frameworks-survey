import unittest
from langgraph_demo import run, build_graph


class LangGraphTests(unittest.TestCase):

    def test_workflow(self):
        result = run("Compare frameworks")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["sources_retrieved"], 4)
        self.assertTrue(result["citation_validation"])

    def test_checkpoint(self):
        graph = build_graph()
        config = {"configurable": {"thread_id": "test"}}

        graph.invoke(
            {"query": "LangGraph", "live": False},
            config=config,
        )

        self.assertTrue(graph.get_state(config).values["validated"])

    def test_offline_usage(self):
        result = run("LangGraph")
        self.assertEqual(result["usage"]["input_tokens"], 0)
        self.assertEqual(result["usage"]["output_tokens"], 0)

    def test_targeted_research(self):
        result = run("LangGraph and CrewAI")
        self.assertEqual(result["sources_retrieved"], 2)
