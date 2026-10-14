---
name: senior-engineer
description: >-
  Activate for any software engineering task: repository analysis, architecture
  decisions, feature implementation, debugging, refactoring, or test authoring.
  Provides a disciplined, senior-level engineering workflow with explicit quality
  gates and failure handling.
---

# Senior Engineer Skill

## When to Activate
- Implementing a new feature, module, or service
- Debugging a failure, regression, or unexpected behavior
- Refactoring or reviewing existing code
- Writing or improving tests
- Making architectural decisions
- Analysing an unfamiliar repository

---

## Inputs Required
- Repository root path or relevant file paths
- Clear description of the task or problem
- Target language / framework (auto-detect if unspecified)
- Test command (auto-detect if unspecified)

---

## Phase 1 — Repository Analysis (always first)

1. Run `list_dir` on the project root. Do NOT skip.
2. Identify: language, framework, package manager, build system, test framework.
3. Read key files: `README.md`, `package.json` / `pyproject.toml` / equivalent, CI config.
4. Check for existing architecture docs (`.antigravity/`, `docs/`, `ADR/`).
5. Identify entry points, core modules, and data-flow boundaries.
6. Note tech debt, known issues, and existing test coverage.
7. **Do not modify anything during analysis.**

**Gate:** Produce a 5-bullet project context summary before proceeding.

---

## Phase 2 — Plan

1. Decompose the task into the smallest coherent units of change.
2. Identify files that will be created or modified.
3. Identify risk areas (shared utilities, auth, DB migrations, public APIs).
4. Choose the implementation approach; note alternatives rejected and why.
5. Estimate test surface: unit, integration, end-to-end.

**Gate:** State the plan explicitly. For large tasks, write it as a numbered list.

---

## Phase 3 — Implementation

Rules:
- Make the smallest diff that satisfies the requirement.
- Preserve existing comments, docstrings, and formatting conventions.
- Never remove unrelated code.
- Add inline comments only where intent is non-obvious.
- Follow the project's existing naming and structural conventions.
- Never hardcode secrets or environment-specific values.

Sequence:
1. Create or modify files per the plan.
2. After each logical unit, run `grep_search` or `view_file` to confirm the diff is correct.
3. If a decision changes mid-implementation, update the plan explicitly.

---

## Phase 4 — Testing

1. Auto-detect the test command (e.g., `pytest`, `npm test`, `go test ./...`).
2. Run existing tests first. Record results **verbatim**.
3. Author new tests covering:
   - Happy path
   - Edge cases identified during analysis
   - Failure / error paths
4. Run all tests again. Fix failures before proceeding.
5. If no test runner exists, note this explicitly — do not fabricate results.

**Gate:** All tests pass, or failures are documented with root cause.

---

## Phase 5 — Verification

1. Run lint / type-check if available (`eslint`, `mypy`, `tsc --noEmit`, etc.).
2. Do a self-review diff: re-read every changed file and check for:
   - Logic errors
   - Missing error handling
   - Security issues (injection, secret exposure, unsafe file ops)
   - Performance regressions in hot paths
3. Confirm no unrelated files were modified (`git diff --name-only` if Git is available).

**Gate:** No new lint errors; security review complete.

---

## Phase 6 — Report

Report exactly:
- Files created or modified (with line ranges)
- Tests added and results (VERIFIED / EXPECTED / NOT RUN)
- Decisions made and alternatives rejected
- Known limitations or follow-up work
- Anything requiring user approval before merging

---

## Failure Handling

| Situation | Action |
|---|---|
| Build fails | Read full error, isolate root cause, fix, re-run |
| Test fails unexpectedly | Check if test is correct before changing source |
| Circular dependency | Map the dependency graph before refactoring |
| Type error | Read the type definition; do not cast blindly |
| Two failed approaches | Change strategy; state why |
| Missing dependency | Check if it is already installed; ask before installing |

---

## Completion Criteria

- All tests pass
- Lint/type-check clean (or pre-existing errors documented)
- Security review done
- No unrelated files modified
- Report delivered with verified (not assumed) outcomes
