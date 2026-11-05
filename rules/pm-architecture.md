# PM & Product Architecture Rules

## 1. Objective
Guide the agent to evaluate the project's high-level architecture, tech stack fit, domain boundaries, and version release lifecycle with the strategic rigor of a Principal Technical Product Manager.

---

## 2. Framework & Tech Stack Suitability Matrix

Evaluate whether the chosen framework fits the application's core requirements:

| Workload Requirement | Optimal Stack / Framework | Anti-Pattern / Warning Signs |
| :--- | :--- | :--- |
| **SEO, Fast Initial Paint, Content/E-commerce** | Next.js (App Router / SSR / SSG), Astro, Remix | Heavy Client-Only SPA (Vite/React) with slow blank-screen bundle |
| **High-frequency Concurrency / Real-time / Streaming** | Go, Elixir (Phoenix), Node.js (with Worker Threads / BullMQ) | Synchronous Python/Django blocking main thread on long I/O |
| **Data Intensive / Machine Learning** | Python (FastAPI), Rust bindings | Node.js trying to perform heavy matrix math on event loop |
| **High-density Enterprise Internal Tools** | Vite + React + TanStack Table / NestJS | Overcomplicated micro-frontends with excessive overhead |

### Evaluation Criteria:
- **I/O Bound vs. Compute Bound:** Does the framework choice respect the language's threading/concurrency model?
- **Over-Engineering vs. Under-Engineering:** Are microservices used where a modular monolith would be $10\times$ simpler and faster?

---

## 3. Structural & Architectural Integrity
Inspect the folder organization and separation of concerns:
1. **Clean Architecture / Layered Separation:**
   - **Domain / Entities:** Pure business logic, independent of UI or Database frameworks.
   - **Use Cases / Services:** Application business rules orchestrating data flow.
   - **Controllers / Presenters:** Translates requests/responses.
   - **Infrastructure / Data Access:** Database drivers, external API clients, file storage.
2. **Flag Violations:**
   - Raw SQL queries or database ORM calls directly inside UI view components (e.g., inside React client components).
   - Business calculation logic tightly coupled inside HTTP controller handlers.
   - Circular dependencies between domain modules.

---

## 4. Semantic Versioning (SemVer) & Release Management
Check the project's release readiness:
* **Version Format:** `MAJOR.MINOR.PATCH`
  * `MAJOR`: Incompatible API changes or schema breaking changes.
  * `MINOR`: Backward-compatible feature additions.
  * `PATCH`: Backward-compatible bug fixes.
* **Breaking Changes Tracking:**
  * Are deleted or renamed database columns preceded by a migration deprecation window?
  * Are public API route changes accompanied by versioning (`/v1`, `/v2`) or deprecation headers?
* **Changelog Hygiene:** Does every version increment have an explicit, categorized changelog (Added, Changed, Deprecated, Removed, Fixed, Security)?
