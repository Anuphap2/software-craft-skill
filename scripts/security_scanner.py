#!/usr/bin/env python3
"""
Security & Vulnerability Scanner (OWASP Top 10 & Secret Leaks)
Part of software-craft-skill.
Detects hardcoded API keys, raw SQL query concatenation, dangerous evals, and injection risks.
"""

import os
import re
import sys
import json
from typing import List, Dict, Any

# Security patterns
PATTERNS = [
    {
        "type": "HARDCODED_AWS_KEY",
        "severity": "CRITICAL",
        "pattern": re.compile(r'\b(AKIA[0-9A-Z]{16})\b'),
        "message": "Potential hardcoded AWS Access Key ID detected. Move to environment variables immediately."
    },
    {
        "type": "HARDCODED_PRIVATE_KEY",
        "severity": "CRITICAL",
        "pattern": re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
        "message": "Private encryption key embedded directly in source code. Revoke and move to secure secret storage."
    },
    {
        "type": "HARDCODED_GENERIC_SECRET",
        "severity": "HIGH",
        "pattern": re.compile(r'(?:api[_-]?key|secret|auth[_-]?token|password)\s*[:=]\s*["\']([a-zA-Z0-9_\-\.]{16,})["\']', re.IGNORECASE),
        "message": "Suspected hardcoded API key, token, or password found in assignment."
    },
    {
        "type": "RAW_SQL_INJECTION_RISK",
        "severity": "CRITICAL",
        "pattern": re.compile(r'(?:SELECT|INSERT|UPDATE|DELETE)\s+.*(?:\+\s*[\w\.]+|\$\{[^\}]+\})', re.IGNORECASE),
        "message": "Raw SQL query concatenation detected. Use parameterized queries or prepared statements to prevent SQL Injection."
    },
    {
        "type": "DANGEROUS_EVAL_EXEC",
        "severity": "CRITICAL",
        "pattern": re.compile(r'\b(?:eval|exec)\s*\('),
        "message": "Direct use of `eval()` or `exec()` detected. Dynamic code execution leads to Remote Code Execution (RCE)."
    },
    {
        "type": "UNSAFE_INNER_HTML",
        "severity": "HIGH",
        "pattern": re.compile(r'\bdangerouslySetInnerHTML\b|\.innerHTML\s*='),
        "message": "Unsafe direct HTML injection detected (`dangerouslySetInnerHTML` / `.innerHTML`). Susceptible to Cross-Site Scripting (XSS)."
    },
    {
        "type": "REDOS_VULNERABLE_REGEX",
        "severity": "HIGH",
        "pattern": re.compile(r'\(\s*[\w\.\+\*]+\s*[\+\*]\s*\)\s*[\+\*]'),
        "message": "Nested quantifier regex detected (e.g. `(a+)+`). Vulnerable to Regular Expression Denial of Service (ReDoS)."
    }
]


def scan_file(filepath: str) -> List[Dict[str, Any]]:
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            # Skip pure comment lines
            if stripped.startswith("//") or stripped.startswith("#") or stripped.startswith("/*"):
                continue

            for check in PATTERNS:
                if check["pattern"].search(stripped):
                    issues.append({
                        "file": filepath,
                        "line": idx,
                        "category": "DEV_SECURITY",
                        "severity": check["severity"],
                        "type": check["type"],
                        "message": check["message"]
                    })
    except Exception as e:
        sys.stderr.write(f"Error scanning {filepath}: {e}\n")

    return issues


def scan_directory(target_dir: str) -> Dict[str, Any]:
    all_issues = []
    scanned_files = 0
    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", "__pycache__", ".venv", "venv", ".idea", "tests"}
    code_exts = {".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".php", ".rb", ".json", ".env"}

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in code_exts or file.startswith(".env"):
                # Warning for committed .env files containing real secrets
                filepath = os.path.join(root, file)
                issues = scan_file(filepath)
                all_issues.extend(issues)
                scanned_files += 1

    return {
        "target_directory": os.path.abspath(target_dir),
        "files_scanned": scanned_files,
        "total_issues": len(all_issues),
        "issues": all_issues
    }


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    result = scan_directory(target)
    print(json.dumps(result, indent=2))
