#!/usr/bin/env python3
"""
Unit test for Agent Behavioral Evaluation Scenarios
Part of software-craft-skill.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evals")))
from runner import run_benchmark_verification, load_scenarios


class TestAgentEvals(unittest.TestCase):
    def test_eval_scenarios_schema_and_integrity(self):
        result = run_benchmark_verification()
        self.assertEqual(result["status"], "PASS", f"Scenario validation errors: {result['errors']}")
        self.assertGreaterEqual(result["total_scenarios"], 4)

    def test_scenarios_cover_critical_behaviors(self):
        scenarios = load_scenarios()
        scenario_ids = {s["id"] for s in scenarios}
        self.assertIn("scenario_small_bug_fix", scenario_ids)
        self.assertIn("scenario_code_review_only", scenario_ids)
        self.assertIn("scenario_unavailable_test_runner", scenario_ids)
        self.assertIn("scenario_destructive_side_effects_guard", scenario_ids)


if __name__ == "__main__":
    unittest.main()
