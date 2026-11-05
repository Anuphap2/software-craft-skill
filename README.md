# 🛡️ Software Craft Skill: Virtual Product & Engineering Squad

[![Version: 1.1.0](https://img.shields.io/badge/Version-1.1.0-blue.svg)](https://github.com/Anuphap2/software-craft-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests: Passing](https://img.shields.io/badge/Tests-9%2F9%20Passing-emerald.svg)](tests/)
[![Standard: Zero AI Slop](https://img.shields.io/badge/Standard-Zero%20AI%20Slop-indigo.svg)](rules/uiux-zero-slop-wcag.md)
[![Theory: Computer Science Rigor](https://img.shields.io/badge/Theory-Big--O%20%26%20OWASP-rose.svg)](rules/dev-big-o-security.md)

> **Equip your AI Agent (Antigravity, Cursor, Claude Code, Copilot) with the disciplined methodology of an elite Virtual Product Squad:**  
> **PM** (Architecture & Stack Fit) • **UI/UX** (Zero AI-Slop & WCAG 2.2 AA) • **Dev** (Big-O & OWASP Security) • **QA** (Pre-Deployment Standards)

---

## ⚡ Dual-Operating Modes (Build & Audit)

Unlike traditional linters or shallow prompt wrappers, **Software Craft Skill** operates in two powerful modes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🏗️ MODE 1: AUTONOMOUS BUILDER (With Self-Healing Verification Loop)         │
├─────────────────────────────────────────────────────────────────────────────┤
│ User Request ──► [PM: Architecture] ──► [UI/UX: Tokens] ──► [Dev: Big-O]    │
│                       ▲                                           │         │
│                       │                     [QA: Unit Tests] ◄────┘         │
│                       │                            │                        │
│               (Score < 90: Auto-Heal) ◄── [Run Heuristic Scanners]          │
│                       │                            │                        │
│                       └────────► [Score >= 90: Certified Delivery]          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🔍 MODE 2: DEEP-AUDIT & REMEDIATION INSPECTOR                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ Existing Codebase ──► Scan AST / Slop / Security ──► Versioned Audit Report │
│                                                  ──► Unified Git Diff Patch │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. 🏗️ Mode 1: Autonomous Builder & Self-Healing
When asked to build a new feature or project from scratch:
* **PM Phase:** Structures the project following Clean Architecture.
* **UI/UX Phase:** Enforces semantic design tokens, WCAG 2.2 AA contrast, 44×44px touch targets, and full interactive states (Skeleton, Hover, Empty) — zero AI slop.
* **Dev Phase:** Selects optimal data structures guaranteeing $O(1)$/$O(N)$ Big-O complexity and parameterized queries protecting against SQL injection and XSS.
* **QA Phase:** Generates comprehensive unit tests covering Boundary Value Analysis.
* **Self-Audit Gate:** The agent runs bundled scanners on its own code. If the health score is $< 90$, it **auto-refactors its own code** until meeting production standards before handing it over to you.

### 2. 🔍 Mode 2: Deep-Audit & Remediation
When asked to review an existing codebase:
* Scans for algorithmic complexity bottlenecks ($O(N^2)$ nested loops).
* Detects front-end AI-slop (unstyled emojis, generic purple gradients, arbitrary CSS).
* Flags OWASP Top 10 security vulnerabilities and hardcoded secrets.
* Outputs an **Executive Health Scorecard (0-100)** and ready-to-apply **Unified Git Diff Patches**.

---

## 📂 Repository Structure

```
software-craft-skill/
├── SKILL.md                       # Core Agent Skill definition & Dual-Mode workflows
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
Clone directly into your Antigravity skills directory:
```bash
git clone https://github.com/Anuphap2/software-craft-skill.git ~/.gemini/config/skills/software-craft-skill
```

### Option 2: Install into Cursor / Claude Code
Copy `SKILL.md` and the `rules/` folder into your project's `.cursor/rules/` or add to your agent system prompt instructions.

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
python scripts/generate_report.py /path/to/project v1.1.0
```

---

## 💬 How to Prompt Your AI Agent

Once installed, talk naturally to your AI Agent:

#### To Build with Self-Healing Verification:
> *"Create a user search and notification service using `software-craft-skill`. Ensure it passes the self-healing gate with a Health Score $\ge 90$."*

#### To Audit an Existing Codebase:
> *"Audit this repository using `software-craft-skill` across PM, UI/UX, Dev, and QA dimensions. Generate a versioned report and Git diff patches for `v1.0.0`."*

---

## 🧪 Testing

Run the automated test suite verifying scanner precision:
```bash
python -m unittest discover tests -v
```

---

## 📄 License
Released under the [MIT License](LICENSE).
