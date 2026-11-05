#!/usr/bin/env python3
"""
Unit tests for slop_detector.py
Part of software-craft-skill.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from slop_detector import scan_content


class TestSlopDetector(unittest.TestCase):
    def test_detects_unstyled_emoji_in_button(self):
        content = '<button className="px-4 py-2">🚀 Launch Product</button>'
        issues = scan_content("sample.tsx", content)
        self.assertTrue(any(i["type"] == "UNSTYLED_EMOJI" for i in issues))

    def test_detects_generic_purple_gradient(self):
        content = '<div className="bg-gradient-to-r from-purple-600 to-blue-500 p-8">'
        issues = scan_content("sample.tsx", content)
        self.assertTrue(any(i["type"] == "GENERIC_PURPLE_GRADIENT" for i in issues))

    def test_detects_arbitrary_tailwind_values(self):
        content = '<div className="p-[17px] text-[#341255]">'
        issues = scan_content("sample.tsx", content)
        self.assertTrue(any(i["type"] == "ARBITRARY_CSS_VALUE" for i in issues))

    def test_detects_outline_none_without_focus_visible(self):
        content = '<button className="outline-none bg-blue-500">Click me</button>'
        issues = scan_content("sample.tsx", content)
        self.assertTrue(any(i["type"] == "REMOVED_OUTLINE_WITHOUT_FOCUS_VISIBLE" for i in issues))


if __name__ == "__main__":
    unittest.main()
