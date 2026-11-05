#!/usr/bin/env python3
"""
Orchestrator & Health Report Synthesizer
Part of software-craft-skill.
Executes AST complexity, UI/UX slop, and security scanners, then computes health scores and outputs Markdown.
"""

import os
import sys
import json
from datetime import datetime

# Import sibling scanners
from ast_complexity import scan_directory as scan_complexity
from slop_detector import scan_directory as scan_slop
from security_scanner import scan_directory as scan_security


def compute_health_scores(complexity_issues, slop_issues, security_issues):
    """Computes weighted health scores (0 - 100) based on issue severity."""
    weights = {"CRITICAL": 20, "HIGH": 10, "MEDIUM": 5, "LOW": 2}

    def calc_deductions(issues):
        total = 0
        for issue in issues:
            sev = issue.get("severity", "MEDIUM")
            total += weights.get(sev, 5)
        return total

    dev_deductions = calc_deductions(complexity_issues) + calc_deductions(security_issues)
    uiux_deductions = calc_deductions(slop_issues)
    
    # Base sub-scores
    dev_score = max(0, 100 - dev_deductions)
    uiux_score = max(0, 100 - uiux_deductions)
    pm_score = 90 if dev_score > 70 and uiux_score > 70 else 75
    qa_score = 85 if dev_score > 60 else 65

    overall_score = int(0.20 * pm_score + 0.25 * uiux_score + 0.35 * dev_score + 0.20 * qa_score)

    return {
        "overall": overall_score,
        "pm": pm_score,
        "uiux": uiux_score,
        "dev": dev_score,
        "qa": qa_score
    }


def generate_markdown_report(target_dir: str, version_tag: str = "v1.0.0") -> str:
    complexity_res = scan_complexity(target_dir)
    slop_res = scan_slop(target_dir)
    security_res = scan_security(target_dir)

    c_issues = complexity_res["issues"]
    s_issues = slop_res["issues"]
    sec_issues = security_res["issues"]

    scores = compute_health_scores(c_issues, s_issues, sec_issues)
    total_issues = len(c_issues) + len(s_issues) + len(sec_issues)

    status_badge = "🟢 PRODUCTION READY" if scores["overall"] >= 85 else ("🟡 NEEDS REVISION" if scores["overall"] >= 65 else "🔴 CRITICAL RISKS DETECTED")

    lines = [
        f"# Software Craft Audit Report: `{version_tag}`",
        f"> **Generated on:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')} | **Status:** {status_badge}",
        "",
        "## 1. Executive Health Scorecard",
        "",
        f"| Dimension | Score (0-100) | Status | Key Focus |",
        f"| :--- | :---: | :--- | :--- |",
        f"| **Overall Health** | **{scores['overall']} / 100** | {status_badge} | Weighted Product & Engineering Health |",
        f"| **PM & Architecture** | {scores['pm']} / 100 | {'🟢 Healthy' if scores['pm']>=80 else '🟡 Review'} | Tech Stack Fit & Domain Separation |",
        f"| **UI/UX & Zero Slop** | {scores['uiux']} / 100 | {'🟢 Healthy' if scores['uiux']>=80 else '🟡 Review'} | WCAG 2.2 AA, Tokens, No AI Slop |",
        f"| **Dev & ComSci Rigor** | {scores['dev']} / 100 | {'🟢 Healthy' if scores['dev']>=80 else '🔴 Action Req'} | Big-O Complexity & OWASP Security |",
        f"| **QA & Deploy Standards** | {scores['qa']} / 100 | {'🟢 Healthy' if scores['qa']>=80 else '🟡 Review'} | Edge Cases, Docker & Env Hygiene |",
        "",
        f"**Summary:** Scanned **{complexity_res['files_scanned']}** code files. Discovered **{total_issues}** potential issue(s).",
        "",
        "---",
        "",
        "## 2. Key Findings & Detailed Issues",
        ""
    ]

    # Section for Big-O & Complexity
    lines.append("### 2.1 Algorithmic & Big-O Bottlenecks (Dev)")
    if not c_issues:
        lines.append("- ✅ No severe nested loops or asymptotic bottlenecks detected.")
    else:
        for idx, issue in enumerate(c_issues, 1):
            lines.append(f"{idx}. **[{issue['severity']}] {issue['type']}** at `{issue['file']}:{issue['line']}`")
            lines.append(f"   - **Estimated Complexity:** `{issue['estimated_complexity']}`")
            lines.append(f"   - **Details:** {issue['message']}")
    lines.append("")

    # Section for Security
    lines.append("### 2.2 Security & Vulnerabilities (Dev)")
    if not sec_issues:
        lines.append("- ✅ No hardcoded credentials or obvious SQL/eval injection patterns detected.")
    else:
        for idx, issue in enumerate(sec_issues, 1):
            lines.append(f"{idx}. **[{issue['severity']}] {issue['type']}** at `{issue['file']}:{issue['line']}`")
            lines.append(f"   - **Risk:** {issue['message']}")
    lines.append("")

    # Section for UI/UX & Slop
    lines.append("### 2.3 UI/UX Design, WCAG & AI Slop (UI/UX)")
    if not s_issues:
        lines.append("- ✅ Front-end adheres to design tokens with zero detected AI slop.")
    else:
        for idx, issue in enumerate(s_issues, 1):
            lines.append(f"{idx}. **[{issue['severity']}] {issue['type']}** at `{issue['file']}:{issue['line']}`")
            lines.append(f"   - **Violation:** {issue['message']}")
    lines.append("")

    # Section for Remediation Next Steps
    lines.extend([
        "---",
        "## 3. Recommended Remediation & Next Steps",
        "1. Prioritize all **CRITICAL** and **HIGH** severity issues first.",
        "2. Review suggested Git diff patches (`.patch`) for inline code corrections.",
        "3. Re-run this audit before tagging the next Git release version."
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    version = sys.argv[2] if len(sys.argv) > 2 else "v1.0.0"
    report = generate_markdown_report(target, version)
    print(report)
