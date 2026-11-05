# Changelog

All notable changes to this project are documented in this file.
This changelog is derived directly from the verified Git repository commit and release history.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.4] - 2026-11-05
### Documentation
- Aligned test counts across all documentation sections to 17 passing tests (`3581ac1`).
- Synced default versioning across `generate_report.py` and `README.md`.

## [1.2.3] - 2026-11-05
### Added
- Dedicated security pattern for hardcoded Bearer authorization tokens (`SUSPICIOUS_BEARER_TOKEN`) (`4890dda`).
- Automated regression test verifying standalone Bearer token detection and multi-pass redaction.

## [1.2.2] - 2026-11-05
### Security
- Implemented multi-pass sequential secret redaction (`sanitize_all_secrets_in_line`) ensuring multiple credentials on the same line are all sanitized (`ba62133`).
- Added automated regression tests asserting raw credentials never appear in issue outputs or markdown reports.
### Documentation
- Clarified multi-OS and multi-Python environment matrix as "CI Configured" with live GitHub Actions run link.

## [1.2.1] - 2026-11-05
### Fixed
- Masked matched credentials in report outputs to prevent accidental secret leakage (`e86f736`).
- Pruned dependency directories (`node_modules`, `vendor`, `.venv`) from project artifact inspection.
- Improved JavaScript/TypeScript brace counting to prevent sibling loops in the same function from being falsely flagged as nested.
### Added
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) matrix for Ubuntu, Windows, macOS across Python 3.10–3.12.
- Renamed scenario runner to `evals/validate_spec.py` to accurately reflect structural schema validation.

## [1.2.0] - 2026-11-05
### Changed
- Replaced exaggerated production guarantees with Heuristic Quality Index (HQI) and transparent verification boundaries (`c372ff0`).
- Added confidence ratings (`HIGH`, `MEDIUM`, `LOW`) and scale context ($N \le 20$ considerations) to Big-O heuristics.
- Structured `SKILL.md` into 4 specialized workflows (Feature Builder, Code Review, Surgical Bug Fix, Pre-Release Diff) following progressive disclosure.
- Relaxed dogmatic UI rules to focus on objective WCAG 2.2 AA usability criteria.
### Added
- Agent benchmark scenario specification suite (`evals/eval_scenarios.json`).

## [1.1.0] - 2026-11-05
### Added
- Dual-operating mode workflow adding builder mode with self-healing verification loop (`6655f53`).

## [1.0.0] - 2026-11-05
### Added
- Initial release of `software-craft-skill` (`97b2bad`).
- Core heuristic scanners: AST complexity, UI/UX accessibility, and security patterns.
- Foundational domain rules across PM, UI/UX, Dev, and QA dimensions.
