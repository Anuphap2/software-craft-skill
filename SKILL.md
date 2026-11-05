---
name: software-craft-skill
description: Autonomous Virtual Product & Engineering Squad (PM, UI/UX, Dev, QA). Audits codebases for Computer Science rigor (Big-O, OWASP Security), Zero AI-Slop UI/UX (WCAG 2.2 AA, Design Tokens), Architecture fit, and Pre-deployment standards, producing versioned reports and actionable patches.
---

# Software Craft Skill: Virtual Product & Engineering Squad

This skill equips any AI Agent (Antigravity, Cursor, Claude Code, Copilot) with the disciplined methodology of an elite **Virtual Product Squad (PM, UI/UX Designer, Dev, QA)**. It replaces superficial "AI code summaries" with rigorous Computer Science, Human-Computer Interaction (HCI), and Software Engineering inspections.

## When to Trigger This Skill
Activate this skill whenever the user:
- Asks for a comprehensive codebase audit, review, or health check.
- Requests evaluation across PM, UI/UX, Dev, or QA perspectives.
- Mentions "Big-O", "time complexity", "memory complexity", or algorithmic bottlenecks.
- Asks to review UI/UX for design standards, accessibility (WCAG), or to eliminate "AI slop".
- Requests a pre-deployment readiness check or version release audit (e.g., `v1.0.0` vs `v1.1.0`).
- Wants actionable Git diff patches for detected defects.

---

## The 4 Core Dimensions

When reviewing a codebase or pull request, conduct inspections across all 4 pillars:

```
┌────────────────────────────────────────────────────────┐
│               VIRTUAL PRODUCT SQUAD                    │
├───────────────┬────────────────┬───────────────┬───────┤
│ 1. PM         │ 2. UI/UX       │ 3. DEV        │ 4. QA │
│ Architecture  │ Zero AI-Slop   │ ComSci/Big-O  │ Tests │
│ Framework Fit │ WCAG 2.2 AA    │ OWASP Sec     │ Deploy│
│ Release Plan  │ Design Tokens  │ Concurrency   │ Ready │
└───────────────┴────────────────┴───────────────┴───────┘
```

Read each domain's detailed criteria before performing the evaluation:
1. **PM:** `rules/pm-architecture.md`
2. **UI/UX:** `rules/uiux-zero-slop-wcag.md`
3. **Dev (ComSci & Security):** `rules/dev-big-o-security.md`
4. **QA & DevOps:** `rules/qa-deploy-standards.md`

---

## Standard Execution Procedure

Follow this systematic 5-step workflow:

### Step 1: Ecosystem & Stack Auto-Detection
Detect the project's primary languages and frameworks by inspecting configuration manifests:
- `package.json` -> Node.js / Next.js / React / Vue / Vite
- `go.mod` -> Go (Golang)
- `Cargo.toml` -> Rust
- `requirements.txt` / `pyproject.toml` -> Python / FastAPI / Django
- `pom.xml` / `build.gradle` -> Java / Kotlin
Identify the concurrency model (Single-threaded event loop, Goroutines, OS threads) and target deployment runtime.

### Step 2: Run Local Heuristic Scripts
Execute the bundled Python inspection scripts located in `scripts/`:
```bash
# 1. Scan for algorithmic complexity and nested loops (Python AST / heuristic scanner)
python scripts/ast_complexity.py <project_directory>

# 2. Scan front-end code for AI slop, unstyled emojis, and missing accessible states
python scripts/slop_detector.py <project_directory>

# 3. Scan for hardcoded credentials, SQL injection patterns, and security risks
python scripts/security_scanner.py <project_directory>
```
Collect the raw JSON/Text metrics output by these tools.

### Step 3: Deep-Tech Qualitative Reasoning
Combine script metrics with LLM reasoning against the 4 domain rules:
- **PM**: Is the selected framework appropriate for the team's workload? Are separation of concerns and Clean Architecture respected?
- **UI/UX**: Are there unstyled raw emojis, generic purple gradients, or arbitrary non-token styles (`p-[17px]`)? Are touch targets at least 44×44px? Is contrast $\ge 4.5:1$?
- **Dev**: Which specific functions operate at $O(N^2)$ or worse? Can nested searches be optimized to $O(1)$ with Hash Maps/Sets? Are there race conditions or OWASP vulnerabilities?
- **QA**: Which critical business logic lacks unit tests? Is there an env validation schema, Dockerfile hygiene, and `/healthz` endpoint before production deployment?

### Step 4: Health Scoring (0 - 100)
Calculate the weighted health score based on severity penalties:
* **Critical Issue** (e.g., SQL Injection, Hardcoded secret, $O(N^3)$ on critical path): -20 pts
* **High Issue** (e.g., Missing WCAG contrast, unhandled race condition, missing deploy env check): -10 pts
* **Medium Issue** (e.g., $O(N^2)$ on small datasets, arbitrary CSS values, missing empty state): -5 pts
* **Low / Nit Issue** (e.g., Typo in log, minor formatting inconsistency): -2 pts

Sub-scores are assigned to each pillar:
$$\text{Overall Score} = 0.20(\text{PM}) + 0.25(\text{UI/UX}) + 0.35(\text{Dev}) + 0.20(\text{QA})$$

### Step 5: Deliver Versioned Report & Actionable Patches
Render the audit using `templates/version_audit_report.md`.
For every identified defect, provide:
1. **Theoretical Rationale**: The Computer Science, HCI, or Software Architecture justification.
2. **Unified Git Diff Patch**: A copy-pasteable or downloadable `.patch` that resolves the issue immediately.
