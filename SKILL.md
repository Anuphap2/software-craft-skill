---
name: software-craft-skill
description: Autonomous Virtual Product & Engineering Squad (PM, UI/UX, Dev, QA). Operates in Dual Modes: (1) Autonomous Builder with Self-Healing Loop (Builds features and self-audits until Health Score >= 90) and (2) Deep-Audit & Remediation (Inspects codebases for Big-O, OWASP Security, Zero AI-Slop, and Pre-deploy standards).
---

# Software Craft Skill: Virtual Product & Engineering Squad

This skill equips any AI Agent (Antigravity, Cursor, Claude Code, Copilot) with the disciplined methodology of an elite **Virtual Product Squad (PM, UI/UX Designer, Dev, QA)**. It operates in **Dual Modes**:
1. 🏗️ **Autonomous Builder & Self-Healing Engine:** Creates new projects and features end-to-end, then autonomously runs local heuristic scanners on its own code to self-heal until meeting enterprise quality standards ($\ge 90/100$).
2. 🔍 **Deep-Audit & Remediation Inspector:** Evaluates existing codebases for Computer Science rigor, UI/UX Zero AI-Slop, Security vulnerabilities, and Pre-deployment readiness.

---

## The 4 Core Dimensions

Whether building or auditing, the agent applies the rigorous principles across all 4 pillars:

```
┌─────────────────────────────────────────────────────────────────┐
│                    VIRTUAL PRODUCT SQUAD                        │
├─────────────────┬──────────────────┬─────────────────┬──────────┤
│ 1. PM           │ 2. UI/UX         │ 3. DEV          │ 4. QA    │
│ Architecture    │ Zero AI-Slop     │ ComSci/Big-O    │ Tests    │
│ Framework Fit   │ WCAG 2.2 AA      │ OWASP Defense   │ Pre-Deploy│
│ Release Plan    │ Design Tokens    │ Concurrency     │ Standards│
└─────────────────┴──────────────────┴─────────────────┴──────────┘
```

Read each domain's detailed criteria:
1. **PM:** `rules/pm-architecture.md`
2. **UI/UX:** `rules/uiux-zero-slop-wcag.md`
3. **Dev (ComSci & Security):** `rules/dev-big-o-security.md`
4. **QA & DevOps:** `rules/qa-deploy-standards.md`

---

## Operating Mode 1: Autonomous Builder & Self-Healing Loop

Use this mode when the user asks to **create, implement, scaffold, or refactor a feature or project**:

```
[User Request] 
      │
      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 1. PM Phase  │ ──► │ 2. UI/UX     │ ──► │ 3. Dev Phase │ ──► │ 4. QA Phase  │
│ Architecture │     │ Tokens & UX  │     │ Big-O & Sec  │     │ Edge Tests   │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
┌────────────────────────────────────────────────────────┐     ┌──────────────┐
│ 6. Ship Certified Code (Health Score >= 90 / 100)      │ ◄── │ 5. Self-Audit│
└────────────────────────────────────────────────────────┘     │ Run Scanners │
                               ▲                               └──────────────┘
                               │                                      │
                               └──── [Score < 90: Auto-Heal] ◄────────┘
```

### Execution Steps for Building:
1. **PM Phase (Architecture & Scope):**
   - Define domain boundaries using Clean Architecture.
   - Choose frameworks suited for the concurrency and rendering workload.
2. **UI/UX Phase (Design Tokens & Anti-Slop):**
   - Establish semantic color tokens (`bg-background`, `text-foreground`, `border-border`).
   - Eliminate AI-slop: use Lucide SVG icons (no raw emojis), distinct typography hierarchy, contrast $\ge 4.5:1$, and touch targets $\ge 44\times 44\text{px}$.
   - Ensure all 7 interactive states (Default, Hover, Active, Focus, Disabled, Skeleton, Empty).
3. **Dev Phase (ComSci Rigor & Security):**
   - Implement data structures that guarantee optimal asymptotic complexity ($O(1)$ or $O(N)$ instead of nested $O(N^2)$ loops).
   - Use parameterized database queries and input sanitization to eliminate SQL injection and XSS.
   - Guard asynchronous code against race conditions and event loop blocking.
4. **QA Phase (Boundary Tests):**
   - Write automated unit tests (Jest/Vitest/Pytest) verifying Boundary Value Analysis (Null, empty, overflow, negative values).
5. **Self-Audit & Auto-Healing Gate (MANDATORY):**
   - Execute the local heuristic scanners on the newly written code:
     ```bash
     python scripts/generate_report.py <directory> <version>
     ```
   - **Auto-Healing Rule:** If the overall score is $< 90$ or any **CRITICAL** / **HIGH** issue is detected:
     1. Analyze the issue output.
     2. Refactor the code immediately to eliminate the flaw.
     3. Re-scan until the score is $\ge 90/100$.
6. **Deliver Certified Code:** Hand over the completed code along with the passing verification score.

---

## Operating Mode 2: Deep-Audit & Remediation Inspector

Use this mode when the user asks to **audit, inspect, benchmark, or review an existing codebase**:

### Execution Steps for Auditing:
1. **Detect Ecosystem & Runtime:** Inspect package manifests (`package.json`, `go.mod`, `Cargo.toml`, `requirements.txt`).
2. **Run Heuristic Scanners:**
   ```bash
   python scripts/ast_complexity.py <directory>
   python scripts/slop_detector.py <directory>
   python scripts/security_scanner.py <directory>
   ```
3. **Synthesize Findings:** Combine AST metrics with qualitative reasoning against `rules/*.md`.
4. **Calculate Health Score:**
   $$\text{Overall Score} = 0.20(\text{PM}) + 0.25(\text{UI/UX}) + 0.35(\text{Dev}) + 0.20(\text{QA})$$
5. **Generate Versioned Report & Patches:**
   - Render report via `templates/version_audit_report.md`.
   - Provide unified Git diff patches (`.patch`) ready for immediate application.
