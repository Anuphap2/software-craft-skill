#!/usr/bin/env python3
"""
AST & Algorithmic Complexity Scanner (Big-O & Loop Nesting Analyzer)
Part of software-craft-skill.
Inspects source files for nested loops, inner array lookups, and algorithmic bottlenecks.
"""

import ast
import os
import re
import sys
import json
from typing import List, Dict, Any

class ComplexityVisitor(ast.NodeVisitor):
    """AST visitor for Python files to measure loop depth and nested operations."""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.current_loop_depth = 0
        self.max_loop_depth = 0
        self.issues: List[Dict[str, Any]] = []

    def visit_For(self, node):
        self._enter_loop(node)
        self.generic_visit(node)
        self._exit_loop()

    def visit_While(self, node):
        self._enter_loop(node)
        self.generic_visit(node)
        self._exit_loop()

    def _enter_loop(self, node):
        self.current_loop_depth += 1
        if self.current_loop_depth > self.max_loop_depth:
            self.max_loop_depth = self.current_loop_depth

        if self.current_loop_depth >= 2:
            self.issues.append({
                "file": self.filepath,
                "line": node.lineno,
                "type": "NESTED_LOOP",
                "depth": self.current_loop_depth,
                "estimated_complexity": f"O(N^{self.current_loop_depth})",
                "severity": "CRITICAL" if self.current_loop_depth >= 3 else "HIGH",
                "message": f"Nested loop detected with depth {self.current_loop_depth} (Potential O(N^{self.current_loop_depth}) complexity)."
            })

    def _exit_loop(self):
        self.current_loop_depth -= 1


def scan_js_ts_complexity(filepath: str, content: str) -> List[Dict[str, Any]]:
    """Heuristic scanner for JS/TS/JSX/TSX files detecting nested loops and inner array scans."""
    issues = []
    lines = content.splitlines()

    # Pattern for inner lookups inside loops: .find, .filter, .includes, .some, .every
    inner_lookup_pattern = re.compile(r'\.(find|filter|includes|some|every|indexOf)\s*\(')
    loop_pattern = re.compile(r'\b(for\s*\(|while\s*\(|\.forEach\s*\(|\.map\s*\()')

    loop_stack = []

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        # Count open braces to approximate scope
        if loop_pattern.search(stripped):
            loop_stack.append(idx)
            if len(loop_stack) >= 2:
                issues.append({
                    "file": filepath,
                    "line": idx,
                    "type": "NESTED_LOOP",
                    "depth": len(loop_stack),
                    "estimated_complexity": f"O(N^{len(loop_stack)})",
                    "severity": "CRITICAL" if len(loop_stack) >= 3 else "HIGH",
                    "message": f"Nested iteration loop detected at depth {len(loop_stack)} (Potential O(N^{len(loop_stack)}) bottleneck)."
                })
        
        # Check for inner linear search within any active loop
        if len(loop_stack) >= 1:
            match = inner_lookup_pattern.search(stripped)
            if match:
                method = match.group(1)
                issues.append({
                    "file": filepath,
                    "line": idx,
                    "type": "INNER_LINEAR_SEARCH",
                    "depth": len(loop_stack) + 1,
                    "estimated_complexity": "O(N * M)",
                    "severity": "HIGH",
                    "message": f"Inner linear search `.{method}()` detected inside iteration loop at line {idx}. Consider pre-indexing into a Map or Set for O(1) lookup."
                })

        # Rough heuristic for block exit
        if '}' in stripped and loop_stack:
            loop_stack.pop()

    return issues


def scan_file(filepath: str) -> List[Dict[str, Any]]:
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if filepath.endswith(".py"):
            try:
                tree = ast.parse(content, filename=filepath)
                visitor = ComplexityVisitor(filepath)
                visitor.visit(tree)
                issues.extend(visitor.issues)
            except SyntaxError:
                pass
        elif any(filepath.endswith(ext) for ext in [".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"]):
            issues.extend(scan_js_ts_complexity(filepath, content))
    except Exception as e:
        sys.stderr.write(f"Error scanning {filepath}: {e}\n")

    return issues


def scan_directory(target_dir: str) -> Dict[str, Any]:
    all_issues = []
    scanned_files = 0
    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", "__pycache__", ".venv", "venv"}

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in {".py", ".js", ".jsx", ".ts", ".tsx"}:
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
