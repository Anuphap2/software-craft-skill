# Dev Dimension: Computer Science & Security Rules

## 1. Objective
Ensure codebase implementation adheres to rigorous Computer Science theory: optimal Big-O algorithmic complexity, efficient data structure utilization, concurrency safety, and comprehensive defense against security attacks (OWASP Top 10).

---

## 2. Algorithmic Complexity (Big-O Analysis)

Inspect functions, loops, and data transformations for asymptotic time and space complexity:

### 2.1 Complexity Classes & Thresholds
| Complexity | Verdict | Action Required |
| :--- | :--- | :--- |
| **$O(1)$** | **Optimal** | Constant time (Hash map lookups, direct array index, stack push/pop). |
| **$O(\log N)$** | **Excellent** | Binary search, balanced tree operations. |
| **$O(N)$** | **Acceptable** | Single linear pass through collections. |
| **$O(N \log N)$** | **Standard** | Efficient sorting (MergeSort, QuickSort, Timsort). |
| **$O(N^2)$** | **Warning / Critical** | Nested loops over unbounded datasets, inner `.find()`, `.filter()`, or `.includes()` inside loops. |
| **$O(2^N)$ or $O(N!)$** | **Fatal** | Exponential recursive algorithms without memoization (Dynamic Programming required). |

### 2.2 Common Big-O Anti-Patterns & Remediations
1. **Hidden Nested Search in Loops ($O(N^2) \to O(N)$):**
   ```javascript
   // ❌ Bad: O(N * M) - array.find inside map
   const enriched = users.map(user => ({
     ...user,
     profile: profiles.find(p => p.userId === user.id) // O(M) inside O(N)
   }));

   // ✅ Good: O(N + M) - Pre-index profiles in Map
   const profileMap = new Map(profiles.map(p => [p.userId, p])); // O(M)
   const enriched = users.map(user => ({
     ...user,
     profile: profileMap.get(user.id) // O(1) lookup
   }));
   ```

2. **Database N+1 Query Problem:**
   * Querying related records individually in a loop instead of performing a single `JOIN`, `IN (...)`, or using ORM eager loading (`include:` / `select_related`).

3. **String Concatenation in Loops:**
   * In languages with immutable strings, repeatedly concatenating strings inside a loop creates $O(N^2)$ memory copies. Use string builders or array `.join()`.

---

## 3. Data Structures & Concurrency Safety

### 3.1 Data Structure Selection
* **Set / Map vs. Array:** If membership checks (`has()`, `includes()`) or key-value lookups are frequent, use `Set` / `Map` ($O(1)$) instead of linear arrays ($O(N)$).
* **Queue vs. Array Shift:** In JavaScript, `array.shift()` is $O(N)$ because every remaining element must be re-indexed. For high-throughput queues, use a linked list or circular buffer.

### 3.2 Concurrency & Asynchronous Patterns
* **Event Loop Starvation (Node.js / Python asyncio):** Never execute CPU-heavy synchronous loops (cryptography, image processing, large JSON parsing) on the main event loop thread. Delegate to Worker Threads or background queues.
* **Race Conditions & Mutexes:** When multiple async routines read, modify, and write shared in-memory state, protect operations with atomic locks or idempotency tokens.
* **Deadlock Prevention:** Ensure resource locks are always acquired in a consistent hierarchical order.

---

## 4. Security & Attack Defense (OWASP Top 10)

Inspect every input and boundary for vulnerabilities:

### 4.1 Injection Flaws (SQL, Command, NoSQL)
* **SQL Injection:**
  * **❌ Ban:** String concatenation into raw SQL queries (`"SELECT * FROM users WHERE email = '" + input + "'"`).
  * **✅ Require:** Parameterized queries, prepared statements, or type-safe ORMs (Prisma, Drizzle, SQLAlchemy).
* **Command Injection:** Never pass unsanitized user inputs into `exec()`, `spawn()` with `shell: true`, or `eval()`.

### 4.2 Cross-Site Scripting (XSS) & Data Sanitization
* Never inject unescaped HTML (`dangerouslySetInnerHTML`, `innerHTML`, `v-html`) with user-supplied text.
* Sanitize markdown and rich text inputs using libraries like DOMPurify before rendering.

### 4.3 Secrets & Credential Exposure
* Detect hardcoded API keys, private keys, database passwords, or AWS tokens.
* Require all secrets to be sourced from environment variables (`process.env`, `os.environ`) and verified at startup.

### 4.4 Regular Expression Denial of Service (ReDoS)
* Detect polynomial or exponential regex backtracks (e.g., `(a+)+$`, `([a-zA-Z]+)*`). Ensure timeout limits or safe non-backtracking engines on user-supplied regexes.
