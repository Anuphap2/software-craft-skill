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
        self.test_file = "sample_service.py"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_detects_raw_sql_injection_pattern(self):
        code = 'query = "SELECT * FROM users WHERE email = \'" + user_email + "\'"'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "SUSPICIOUS_RAW_SQL_CONCATENATION" for i in issues))

    def test_detects_dangerous_eval(self):
        code = 'result = eval(user_untrusted_input)'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "SUSPICIOUS_DYNAMIC_EXECUTION" for i in issues))

    def test_detects_suspicious_aws_key(self):
        code = 'AWS_KEY = "AKIA3F4H7K9M2P5R8T1W"'
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(code)

        issues = scan_file(self.test_file)
        self.assertTrue(any(i["type"] == "SUSPICIOUS_AWS_KEY_PATTERN" for i in issues))


if __name__ == "__main__":
    unittest.main()
