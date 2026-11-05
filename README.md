# 🛡️ Software Craft Skill: Engineering Squad Router

[![Version: 1.2.0](https://img.shields.io/badge/Version-1.2.0-blue.svg)](https://github.com/Anuphap2/software-craft-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests: Passing](https://img.shields.io/badge/Tests-12%2F12%20Passing-emerald.svg)](tests/)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%20--%203.12%20(Stdlib)-yellow.svg)](scripts/)
[![Standard: WCAG 2.2 AA](https://img.shields.io/badge/Standard-WCAG%202.2%20AA%20Aligned-indigo.svg)](rules/uiux-zero-slop-wcag.md)

> **Equip your AI Agent (Antigravity, Cursor, Claude Code, Copilot) with pragmatic, disciplined engineering workflows:**  
> **PM** (Scope & Architecture) • **UI/UX** (WCAG 2.2 AA & Usability) • **Dev** (Big-O Heuristics & Security Screening) • **QA** (Real Verification & Pre-Deploy Checks)

---

## 🧭 Why Software Craft Skill?

Most AI coding assistants either provide superficial code summaries or claim impossible "100% bug-free guarantees" based on simple regex wrappers. 

**Software Craft Skill** replaces hype with **pragmatic engineering discipline**:
1. **Context-Aware Heuristics:** Identifies Big-O bottlenecks and security patterns as *candidates for human review*, considering actual data scale ($N$) and project boundaries.
2. **Strict Scope Containment:** Enforces surgical bug fixes that do not rewrite unrelated files or force unrequested library migrations.
3. **Honest Verification:** Reports actual test and build outcomes based on executed commands, never fabricating false pass scores when test runners are absent.
4. **Progressive Disclosure:** Keeps the main skill router concise, loading deep-tech criteria from `rules/` on-demand (aligned with Microsoft Agent Framework & Anthropic Agent Skills best practices).

---

## 🚦 4 Specialized Workflows

The skill routes tasks across four distinct operational workflows based on user intent:

| Workflow | Goal | Execution Characteristics |
| :--- | :--- | :--- |
| **1. Feature Builder** | Incremental feature scaffolding | Respects repo conventions, generates accessible UI states, runs heuristic checks, and verifies real tests if present. |
| **2. Code Review & Audit** | Read-only inspection of PRs or code | Strictly non-destructive; rates findings with confidence levels (`HIGH`/`MEDIUM`/`LOW`) and explicitly lists what was not checked. |
| **3. Surgical Bug Fix** | Precise defect remediation | Targets only the root cause; preserves surrounding code and formatting; avoids sweeping rewrites. |
| **4. Pre-Release Diff** | Version release readiness | Compares current changes against a Git baseline (`base_tag..HEAD`); validates env hygiene and deployment checklists. |

---

## 💻 Tested Environments & Compatibility Matrix

| Platform / Agent | Status | Notes |
| :--- | :---: | :--- |
| **Google Antigravity** | ✅ Verified | Full support via native `~/.gemini/config/skills/` integration. |
| **Cursor IDE** | ✅ Verified | Full support via `.cursor/rules/` or project rules directory. |
| **Claude Code / Desktop** | ✅ Verified | Works via system prompt instructions and local tool invocation. |
| **Python Environment** | ✅ 3.10 - 3.12 | **Zero external pip dependencies.** Built purely on Python Standard Library (`ast`, `re`, `json`). |
| **Operating Systems** | ✅ Win / Mac / Linux | Cross-platform paths and UTF-8 console output safe (handles Windows `cp1252`). |

---

## 📂 Repository Structure

```
software-craft-skill/
├── SKILL.md                       # Main Agent Skill router & workflow definitions
├── README.md                      # Comprehensive documentation
├── LICENSE                        # MIT License
│
├── rules/                         # Progressive deep-tech guidelines
│   ├── pm-architecture.md         # Scope control, framework fit, SemVer
│   ├── uiux-zero-slop-wcag.md     # WCAG 2.2 AA accessibility & design system respect
│   ├── dev-big-o-security.md      # Big-O heuristics & suspicious security patterns
│   └── qa-deploy-standards.md     # Respecting project test tooling & pre-deploy checks
│
├── scripts/                       # Zero-dependency heuristic scanners
│   ├── ast_complexity.py          # Loop nesting & Big-O candidate scanner
│   ├── slop_detector.py           # WCAG accessibility & styling consistency scanner
│   ├── security_scanner.py        # Suspicious pattern & secret leakage scanner
│   └── generate_report.py         # Heuristic Quality Index (HQI) report generator
│
├── evals/                         # Agent Behavioral Evaluation Benchmark Suite
│   ├── eval_scenarios.json        # Standardized behavioral test scenarios
│   └── runner.py                  # Evaluation benchmark verification runner
│
├── templates/
│   └── version_audit_report.md    # Standardized markdown report template
│
└── tests/                         # Automated test suite (12/12 passing)
    ├── test_ast_complexity.py
    ├── test_slop_detector.py
    ├── test_security_scanner.py
    └── test_eval_scenarios.py
```

---

## 🚀 Quickstart & Installation

### Option 1: Install into Google Antigravity
Clone directly into your Antigravity skills directory:
```bash
git clone https://github.com/Anuphap2/software-craft-skill.git ~/.gemini/config/skills/software-craft-skill
```

### Option 2: Install into Cursor / Claude Code
Copy `SKILL.md` and the `rules/` folder into your project's `.cursor/rules/` or system prompt.

### Option 3: Standalone CLI Execution (Zero Setup)
```bash
# Run heuristic screening directly
python scripts/generate_report.py /path/to/project v1.2.0
```

---

## 🧪 Testing & Evaluation

### Run Unit Tests
```bash
python -m unittest discover tests -v
```

### Run Behavioral Benchmark Verification
```bash
python evals/runner.py
```

---

## ⚠️ Scope & Verification Boundaries

**What this skill DOES:**
* Identifies high-risk algorithmic candidates for human engineering review.
* Flags accessible labeling and focus-visible omissions under WCAG 2.2 AA.
* Screens code for suspicious security patterns (unparameterized SQL strings, unescaped HTML, exposed key formats).
* Guides agents toward surgical changes and honest test reporting.

**What this skill DOES NOT replace:**
* Formal Static Application Security Testing (SAST) such as Snyk, Semgrep, or SonarQube.
* Real test execution (`npm test`, `pytest`, `go test`).
* Build compilation checks (`tsc --noEmit`, `npm run build`).
* Penetration testing or dynamic production load testing.

---

## 📄 License
Released under the [MIT License](LICENSE).
