---
name: software-craft-skill
description: Pragmatic Product & Engineering Squad skill for AI agents. Routes tasks across 4 disciplined workflows (Feature Builder, Code Review, Surgical Bug Fix, Pre-Release Audit). Applies progressive disclosure to inspect Big-O complexity heuristics, WCAG accessibility, OWASP patterns, and production verification evidence.
---

# Software Craft Skill: Engineering Squad Router

This skill equips AI agents with the disciplined engineering workflows of a balanced Product & Engineering Squad (**PM, UI/UX, Dev, QA**). It emphasizes **pragmatic scope containment, honest verification, and progressive disclosure**.

---

## 🛡️ Core Safety & Scope Guardrails (MANDATORY)

Before executing any action, adhere strictly to these rules:
1. **Scope Containment:** On bug fixes or small changes, make surgical edits only. Never rewrite unrelated files, refactor architecture, or swap libraries unless explicitly asked.
2. **Honest Verification:** Never fabricate test pass scores. If test tools are missing or not executed, report truthfully: *"Tests not run (No test runner detected or not requested)"*.
3. **No Destructive Actions Without Approval:** Never execute destructive commands (`rm -rf`, `git reset --hard`, `git push --force`) without explicit user confirmation.
4. **Respect Project Conventions:** Use the project's existing framework, UI library, and styling approach (e.g. do NOT force Tailwind onto a project using vanilla CSS or Chakra UI).

---

## 🚦 Workflow Router (Select Based on User Intent)

Match the user's prompt to one of the 4 specialized workflows:

```
                                [User Request]
                                      │
         ┌────────────────────┬───────┴────────────┬────────────────────┐
         ▼                    ▼                    ▼                    ▼
   [Workflow 1]         [Workflow 2]         [Workflow 3]         [Workflow 4]
  Feature Builder        Code Review       Surgical Bug Fix     Pre-Release Diff
```

---

### Workflow 1: Feature Builder (Incremental & Verified)
**When to trigger:** User asks to create, scaffold, or implement a new feature or project.
1. **Inspect Repo First:** Check existing conventions, folder structure, and manifests (`package.json`, `go.mod`, etc.).
2. **Progressive Criteria Loading:**
   - Architecture & Scope: Consult `rules/pm-architecture.md`
   - UI/UX & Accessibility: Consult `rules/uiux-zero-slop-wcag.md`
   - Algorithm & Security: Consult `rules/dev-big-o-security.md`
3. **Implement Feature:** Write clean, modular code respecting existing patterns.
4. **Heuristic Screening (Self-Check):**
   ```bash
   python scripts/generate_report.py <project_directory> <version_tag>
   ```
5. **Verify Real Tests (If Available):** If the project has an existing test command (e.g. `npm test`, `pytest`), run it. If no test suite exists, suggest how the user can test it.
6. **Report Delivery:** Deliver code with summary of implemented features and verification evidence.

---

### Workflow 2: Read-Only Code Review & Audit
**When to trigger:** User asks to review a pull request, inspect a repo, or check code health.
1. **Strictly Read-Only:** Do NOT modify or overwrite any user files.
2. **Run Heuristic Scanners:**
   ```bash
   python scripts/ast_complexity.py <project_directory>
   python scripts/slop_detector.py <project_directory>
   python scripts/security_scanner.py <project_directory>
   ```
3. **Qualitative Review with Confidence:**
   - Label findings with confidence levels (`HIGH`, `MEDIUM`, `LOW`).
   - Differentiate suspicious patterns from confirmed security vulnerabilities.
   - Consider input scale $N$ before claiming Big-O issues (small bounded arrays are negligible).
4. **State Verification Boundaries:** Explicitly inform the user what was NOT checked (dynamic runtime, real build, penetration test).

---

### Workflow 3: Surgical Bug Fix & Refactor
**When to trigger:** User asks to fix an error, debug an issue, or optimize a specific function.
1. **Locate Root Cause:** Identify the exact file and lines responsible.
2. **Surgical Diff:** Modify only the minimal necessary lines.
3. **Regression Prevention:** Run existing relevant tests for that module if a test command exists.
4. **Explain Fix:** Provide a clear explanation of *why* the bug occurred and *how* the fix resolves it.

---

### Workflow 4: Pre-Release & Version Diff (Baseline Comparison)
**When to trigger:** User asks for release readiness, version audit (e.g. `v1.0.0` vs `v1.1.0`), or pre-deploy check.
1. **Baseline Comparison:** Compare current changes against the previous Git tag or commit baseline (`git diff <base_tag>..HEAD`).
2. **Consult Checklist:** Review `rules/qa-deploy-standards.md` for environment validation, secret leakage, and build checks.
3. **Verify Build & Tests:** Request or run actual build (`npm run build`, `go build`) and real test suite.
4. **Output Report:** Render findings using `templates/version_audit_report.md`.
