# PM & Architecture Guidelines (Pragmatic & Context-Aware)

## 1. Objective
Guide software architecture, technology selection, and scope management with practical, business-aligned judgment.
Prioritize pragmatic incremental improvement over dogmatic rewrites.

---

## 2. Scope Management & Change Boundaries

Determine the appropriate level of intervention based on user intent:

| Task Type | Permitted Scope | Prohibited Scope |
| :--- | :--- | :--- |
| **Small Bug Fix** | Edit ONLY the affected function/module. Preserve all existing patterns. | Do NOT restructure folders or refactor unrelated files. |
| **Feature Addition** | Add new modules following existing project conventions. | Do NOT change core libraries (e.g. switching ORMs or UI libraries) unless requested. |
| **Full Project Scaffold** | Apply Clean Architecture and modern framework best practices. | Do NOT introduce unnecessary microservices where a monolith suffices. |

---

## 3. Technology & Framework Suitability

Evaluate tech choices based on trade-offs rather than absolute preferences:
* **Respect Existing Choices:** If a team chose React SPA, Django, or NestJS, work within that ecosystem rather than declaring it obsolete.
* **Identify Real Constraints:** Flag architectural issues only when there is a concrete bottleneck (e.g. single-threaded CPU-heavy jobs blocking Node.js event loop, or missing caching on expensive external APIs).

---

## 4. Release Planning & Versioning
* **Semantic Versioning (SemVer):**
  - Major increment for breaking API/schema changes.
  - Minor increment for backward-compatible capabilities.
  - Patch increment for bug fixes.
* **Baseline Comparison:**
  - When reviewing versions, compare against the previous Git commit/tag baseline rather than relying on an isolated snapshot.
