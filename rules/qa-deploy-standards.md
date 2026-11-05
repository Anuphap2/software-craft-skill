# QA Dimension: Testing & Pre-Deployment Production Rules

## 1. Objective
Ensure code is verified through rigorous automated testing strategies (Boundary Value Analysis, Edge Case Matrices) and satisfies all enterprise-grade pre-deployment standards before shipping to production.

---

## 2. Test Strategy & Edge Case Verification

Evaluate whether automated tests cover critical failure paths and boundary conditions:

### 2.1 Boundary Value Analysis (BVA) & Edge Cases
Every business function and API route MUST be tested against boundary conditions:
1. **Empty / Null / Undefined:** Empty arrays `[]`, empty strings `""`, `null`, `undefined`, empty JSON objects `{}`.
2. **Numeric Boundaries:** $0$, negative numbers, maximum safe integer ($2^{53}-1$ or `MAX_INT`), floating point precision errors ($0.1 + 0.2 \neq 0.3$), division by zero.
3. **Strings & Encodings:** Multi-byte Unicode, emojis, very long strings ($10^6$ characters) to test memory exhaustion.
4. **Time & Concurrency:** Leap years, timezone offsets, leap seconds, simultaneous requests testing idempotency.

### 2.2 Test Structure & Assertions
* **Deterministic Tests:** Tests must not depend on external live networks or shared global mutable state. Use mocks, stubs, or ephemeral test databases.
* **TDD Integrity:** Tests must assert exact state and error messages, not merely check that "no exception was thrown".

---

## 3. Production Deployment Standards Checklist

Audit the repository against the **Production-Readiness Checklist**:

### 3.1 Configuration & Environment Hygiene
- [ ] **Strict Environment Variable Validation:** All required variables must be validated at application startup using a schema validator (Zod, Pydantic, Envalid, Joi) so the service fails fast rather than crashing mid-request.
- [ ] **No `.env` Secrets in Git:** Verify `.gitignore` contains `.env`, `.env.local`, `*.pem`, `*.key`.

### 3.2 Container & Dockerfile Standards
- [ ] **Multi-Stage Builds:** Separate build dependencies from runtime dependencies to minimize container image attack surface and size.
- [ ] **Non-Root Execution:** Container must switch to a non-privileged user (e.g., `USER node` or `USER appuser`) before runtime.
- [ ] **Deterministic Base Images:** Pin explicit image versions or digests (e.g., `node:20-alpine`, `python:3.12-slim`), never unpinned `:latest`.

### 3.3 HTTP, Network & Security Headers
- [ ] **Health Check Endpoints:** Provide `/healthz` (liveness) and `/readyz` (readiness) endpoints returning HTTP 200 and checking database/redis ping status.
- [ ] **CORS Configuration:** Explicitly whitelist permitted origins; never use wildcard `Access-Control-Allow-Origin: *` when credentials/cookies are enabled.
- [ ] **Rate Limiting:** Protect public endpoints (login, forgot-password, search, file uploads) with rate-limiting middleware.
- [ ] **Security Headers:** Enforce `Strict-Transport-Security` (HSTS), `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and strict `Content-Security-Policy` (CSP).

### 3.4 Database Migration Safety
- [ ] **Backward-Compatible Migrations:** Schema changes must support rolling zero-downtime deployments (Add column -> Deploy new code -> Backfill data -> Drop old column in next release). Never drop active columns in a single migration step.
