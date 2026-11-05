# 🛡️ Software Craft Skill: Virtual Product & Engineering Squad

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests: Passing](https://img.shields.io/badge/Tests-9%2F9%20Passing-emerald.svg)](tests/)
[![Standard: Zero AI Slop](https://img.shields.io/badge/Standard-Zero%20AI%20Slop-indigo.svg)](rules/uiux-zero-slop-wcag.md)
[![Theory: Computer Science Rigor](https://img.shields.io/badge/Theory-Big--O%20%26%20OWASP-rose.svg)](rules/dev-big-o-security.md)

> **Equip your AI Agent (Antigravity, Cursor, Claude Code, Copilot) with the disciplined methodology of an elite Virtual Product Squad:**  
> **PM** (Architecture & Stack Fit) • **UI/UX** (Zero AI-Slop & WCAG 2.2 AA) • **Dev** (Big-O & OWASP Security) • **QA** (Pre-Deployment Standards)

---

## 🌟 Why This Skill?

Most AI coding assistants produce superficial code summaries or generic AI wrappers. **Software Craft Skill** replaces shallow reviews with deterministic Computer Science, Human-Computer Interaction (HCI), and Software Engineering inspections:

* 📐 **PM & Architecture:** Framework suitability evaluation, Clean Architecture boundaries, and SemVer release management.
* 🎨 **UI/UX & Zero AI Slop:** Strict ban on unstyled emojis, generic purple SaaS gradients, and arbitrary CSS. Enforces WCAG 2.2 AA contrast, 44×44px touch targets, and full interactive states (default, hover, loading/skeleton, empty).
* ⚡ **Dev ComSci Rigor:** Asymptotic Big-O complexity analysis ($O(1)$ to $O(N^2)$), data structure optimization, and OWASP Top 10 vulnerability detection (SQLi, XSS, Secret Leaks, ReDoS).
* 🚢 **QA & Pre-Deployment:** Boundary Value Analysis (BVA), strict environment variable validation, Dockerfile hygiene, and `/healthz` liveness checks.

---

## 📂 Repository Structure

```
software-craft-skill/
├── SKILL.md                       # Core Agent Skill definition & execution workflow
├── README.md                      # Complete documentation & quickstart
├── LICENSE                        # MIT License
│
├── rules/                         # 4 Specialized Engineering Dimensions
│   ├── pm-architecture.md         # Framework suitability & Clean Architecture
│   ├── uiux-zero-slop-wcag.md     # Zero AI-Slop & WCAG 2.2 AA guidelines
│   ├── dev-big-o-security.md      # Big-O complexity & OWASP attack defense
│   └── qa-deploy-standards.md     # Production deployment checklist & BVA tests
│
├── scripts/                       # Fast, zero-dependency Python heuristic scanners
│   ├── ast_complexity.py          # AST parser measuring loop depth & Big-O
│   ├── slop_detector.py           # Front-end scanner for AI slop & missing focus rings
│   ├── security_scanner.py        # Scans for hardcoded secrets & raw SQL injections
│   └── generate_report.py         # Consolidated Markdown audit generator
│
├── templates/                     # Standardized reporting templates
│   └── version_audit_report.md    # Executive health scorecard & diff templates
│
└── tests/                         # Automated test suite (9/9 passing)
    ├── test_ast_complexity.py
    ├── test_slop_detector.py
    └── test_security_scanner.py
```

---

## 🚀 Quickstart & Installation

### Option 1: Install into Google Antigravity
Clone or copy this repository into your Antigravity skills directory:
```bash
git clone https://github.com/your-username/software-craft-skill.git ~/.gemini/config/skills/software-craft-skill
```

### Option 2: Install into Cursor / Claude Code
Copy `SKILL.md` and the `rules/` folder into your project's `.cursor/rules/` or add to your system prompt instructions.

### Option 3: Standalone CLI Execution (Zero Setup)
Run the bundled scanners directly on any project without installing external dependencies:
```bash
# 1. Run Algorithmic Big-O scan
python scripts/ast_complexity.py /path/to/project

# 2. Run UI/UX AI-Slop & Accessibility scan
python scripts/slop_detector.py /path/to/project

# 3. Run OWASP Security scan
python scripts/security_scanner.py /path/to/project

# 4. Generate complete Version Audit Report
python scripts/generate_report.py /path/to/project v1.0.0
```

---

## 📊 Sample Audit Output

When invoked, the skill produces an executive health scorecard and actionable Git diff patches:

| Dimension | Score (0-100) | Status | Key Focus Area |
| :--- | :---: | :---: | :--- |
| **Overall Health** | **88 / 100** | 🟢 Healthy | Weighted Product & Engineering Health |
| **1. PM & Architecture** | 90 / 100 | 🟢 Healthy | Stack suitability, Domain separation, SemVer |
| **2. UI/UX & Zero Slop** | 85 / 100 | 🟢 Healthy | WCAG 2.2 AA, Design tokens, Zero AI Slop |
| **3. Dev & ComSci Rigor** | 90 / 100 | 🟢 Healthy | Big-O complexity, Data structures, OWASP |
| **4. QA & Deploy Standards** | 85 / 100 | 🟢 Healthy | Test edge cases, Docker & Env validation |

### Actionable Code Remediations (Unified Diff):
```diff
--- a/src/services/userService.ts
+++ b/src/services/userService.ts
@@ -14,6 +14,8 @@
-  // ❌ O(N * M) - linear search inside map
-  return users.map(u => ({ ...u, profile: profiles.find(p => p.id === u.id) }));
+  // ✅ O(N + M) - pre-indexed Map lookup
+  const profileMap = new Map(profiles.map(p => [p.id, p]));
+  return users.map(u => ({ ...u, profile: profileMap.get(u.id) }));
```

---

## 🧪 Testing

Run the automated test suite verifying scanner precision:
```bash
python -m unittest discover tests -v
```

---

## 📄 License
Released under the [MIT License](LICENSE).
