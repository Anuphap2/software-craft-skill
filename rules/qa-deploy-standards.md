# QA Dimension: Verification & Pre-Deployment Standards

## 1. Objective
Guide testing and deployment readiness verification while strictly respecting the project's existing test framework and user intent.
Always report verification status honestly based on executed commands, never on fabricated assumptions.

---

## 2. Respecting Project Test Tooling

When evaluating or generating tests, follow these rules:

### 2.1 Inspect Before Executing
* **Inspect Manifests:** Check `package.json` scripts, `pytest.ini`, `Makefile`, or `go.mod` to see what test runner is installed (`vitest`, `jest`, `pytest`, `go test`, `cargo test`).
* **Do Not Force Uninstalled Tools:** If a project does not have a test framework installed, do NOT attempt to run uninstalled binaries. Report: `"No automated test runner detected in project manifests."`
* **Do Not Fabricate Test Passes:** Never report that tests "passed" unless a real test command was actually executed and exited with code 0.

### 2.2 Boundary Value Analysis (BVA) Guidelines
When writing tests for new or modified code, focus on high-yield boundary cases:
1. **Empty / Nil / Zero states:** `[]`, `""`, `null`, `undefined`, `0`.
2. **Extremes & Numerical Boundaries:** Negative numbers, `MAX_SAFE_INTEGER`, floating point values.
3. **Unexpected Types / Malformed Inputs:** Graceful error handling and descriptive exceptions instead of unhandled crashes.

---

## 3. Practical Pre-Deployment Checklist

Use as an advisory checklist for production readiness:

- [ ] **Build Validation:** Project compiles cleanly via `npm run build`, `tsc --noEmit`, `go build`, or equivalent.
- [ ] **Environment Configuration:** Required runtime secrets and configuration keys are documented (e.g. in `.env.example`) and validated at startup.
- [ ] **Secret Hygiene:** Ensure `.env`, certificates, and private credentials are listed in `.gitignore`.
- [ ] **Liveness / Health Monitoring:** High-availability web services provide a `/healthz` or status endpoint.
- [ ] **Safe Database Migrations:** Schema changes do not perform destructive column drops without a backward-compatible deprecation window.
