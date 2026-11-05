#!/usr/bin/env python3
"""
Unit tests for security_scanner.py
Part of software-craft-skill.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from security_scanner import scan_file


class TestSecurityScanner(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_sample_sec.py"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_detects_raw_sql_injection(self):
        code = 'query = "SELECT * FROM users WHERE email = \'" + user_email + "\'"'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "RAW_SQL_INJECTION_RISK" for i in issues))

    def test_detects_dangerous_eval(self):
        code = 'result = eval(user_untrusted_input)'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "DANGEROUS_EVAL_EXEC" for i in issues))

    def test_detects_hardcoded_aws_key(self):
        code = 'AWS_KEY = "AKIAIOSFODNN7EXAMPLE"'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "HARDCODED_AWS_KEY" for i in issues))


if __name__ == "__main__":
    unittest.main()
