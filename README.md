# 🛡️ Software Craft Skill: Engineering Squad Router

[![Version: 1.2.1](https://img.shields.io/badge/Version-1.2.1-blue.svg)](https://github.com/Anuphap2/software-craft-skill/releases)
[![CI Tests](https://github.com/Anuphap2/software-craft-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/Anuphap2/software-craft-skill/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%20--%203.12%20(Stdlib)-yellow.svg)](scripts/)
[![Standard: WCAG 2.2 AA](https://img.shields.io/badge/Standard-WCAG%202.2%20AA%20Aligned-indigo.svg)](rules/uiux-zero-slop-wcag.md)

> **Equip your AI Agent (Antigravity, Cursor, Claude Code, Copilot) with pragmatic, disciplined engineering workflows:**  
> **PM** (Scope & Architecture) • **UI/UX** (WCAG 2.2 AA & Usability) • **Dev** (Big-O Heuristics & Redacted Security Screening) • **QA** (Real Verification & Pre-Deploy Checks)

---

## 🧭 Why Software Craft Skill?

Most AI coding assistants either provide superficial code summaries or claim impossible "100% bug-free guarantees" based on simple regex wrappers. 

**Software Craft Skill** replaces hype with **pragmatic engineering discipline**:
1. **Context-Aware Heuristics:** Identifies Big-O bottlenecks and security patterns as *candidates for human review*, considering actual data scale ($N$) and project boundaries.
2. **Credential Redaction:** Detected API keys and credentials are automatically masked in reports (`AKIA[REDACTED_KEY]`) to prevent accidental secret leakage.
3. **Dependency-Safe Artifact Inspection:** Scans only project-level files, actively pruning `node_modules`, `vendor`, and `.venv` from artifact detection.
4. **Strict Scope Containment:** Enforces surgical bug fixes that do not rewrite unrelated files or force unrequested library migrations.
5. **Honest Verification:** Reports actual test and build outcomes based on executed commands, never fabricating false pass scores when test runners are absent.
6. **Progressive Disclosure:** Keeps the main skill router concise, loading deep-tech criteria from `rules/` on-demand (aligned with Microsoft Agent Framework & Anthropic Agent Skills best practices).

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

## 💻 Tested Environments & Compatibility

| Platform / Environment | Verification Level | Verification Evidence |
| :--- | :---: | :--- |
| **Operating Systems** | ✅ CI Verified | Tested on Ubuntu, Windows, and macOS via GitHub Actions CI matrix. |
| **Python Runtimes** | ✅ CI Verified | Tested on Python 3.10, 3.11, and 3.12. **Zero external pip dependencies.** |
| **Google Antigravity** | ✅ Locally Tested | Tested locally on Windows with native `~/.gemini/config/skills/` integration. |
| **Cursor IDE** | ℹ️ Expected to Work | Supported via `.cursor/rules/` directory or project rules configuration. |
| **Claude Code / Desktop** | ℹ️ Expected to Work | Supported via system prompt rules and local bash tool invocation. |

---

## 📂 Repository Structure

```
software-craft-skill/
├── .github/workflows/
│   └── ci.yml                     # Multi-OS & Multi-Python CI test matrix
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
│   ├── ast_complexity.py          # Loop nesting & Big-O candidate scanner (sibling-loop aware)
│   ├── slop_detector.py           # WCAG accessibility & styling consistency scanner
│   ├── security_scanner.py        # Suspicious pattern scanner with automated secret redaction
│   └── generate_report.py         # Heuristic Quality Index (HQI) report generator
│
├── evals/                         # Agent Scenario Specifications
│   ├── eval_scenarios.json        # Standardized benchmark scenario definitions
│   └── validate_spec.py           # Scenario specification schema validator
│
├── templates/
│   └── version_audit_report.md    # Standardized markdown report template
│
└── tests/                         # Automated test suite (14 passing tests)
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
python scripts/generate_report.py /path/to/project v1.2.1
```

---

## 🧪 Testing & Validation

### Run Unit Tests
```bash
python -m unittest discover tests -v
```

### Run Scenario Specification Validator
```bash
python evals/validate_spec.py
```

---

## ⚠️ Scope & Verification Boundaries

**What this skill DOES:**
* Identifies high-risk algorithmic candidates for human engineering review.
* Automatically redacts sensitive tokens in generated report outputs.
* Flags accessible labeling and focus-visible omissions under WCAG 2.2 AA.
* Screens code for suspicious security patterns (unparameterized SQL strings, unescaped HTML, exposed key formats).
* Guides agents toward surgical changes, dependency pruning, and honest test reporting.

**What this skill DOES NOT replace:**
* Formal Static Application Security Testing (SAST) such as Snyk, Semgrep, or SonarQube.
* Real test execution (`npm test`, `pytest`, `go test`).
* Build compilation checks (`tsc --noEmit`, `npm run build`).
* Penetration testing or dynamic production load testing.
* Live agent trace evaluation (the `evals/` suite currently validates scenario specifications).

---

## 📄 License
Released under the [MIT License](LICENSE).
