---
name: context-economy
description: >-
  Activate when managing a long or expensive task to minimise token usage,
  avoid repeated work, maintain progress checkpoints, and keep context tight.
  Use proactively on any multi-phase task exceeding ~10 tool calls.
---

# Context Economy Skill

## When to Activate
- Starting a multi-phase task (>10 estimated tool calls)
- Returning to a task after an interruption
- Noticing repeated tool calls on the same files
- Context window is growing large (>50 turns or many large file reads)
- Before reading a large file (>500 lines)
- When the user says "continue", "resume", or "where were we"

---

## Core Principles

1. **Read once, remember.** Never re-read the same file section unless it was modified.
2. **Targeted reads.** Use `StartLine`/`EndLine` in `view_file` instead of reading whole files.
3. **Search before reading.** Use `grep_search` to find the exact lines needed before loading a file.
4. **No redundant confirmations.** Do not repeat what was just done in the same turn.
5. **Checkpoint over re-derive.** Write a checkpoint note before complex multi-step sequences.
6. **Single tool call per logical goal.** Do not call the same tool twice when one suffices.

---

## Phase 1 — Task Sizing (before starting work)

Classify the task:

| Class | Estimated tool calls | Strategy |
|---|---|---|
| **Micro** | 1–3 | No special management needed |
| **Small** | 4–10 | Brief mental plan; proceed |
| **Medium** | 11–30 | Write a checkpoint; use targeted reads |
| **Large** | 31–100 | Create a progress file; phase the work |
| **XL** | 100+ | Decompose into sub-tasks; use `/goal` command |

For Medium and above: write a checkpoint at the start of each phase.

---

## Phase 2 — Context Selection Rules

Before loading any file:
1. Do you already have the relevant content in context? → **Skip the read.**
2. Do you need the whole file, or just a function/section? → **Use grep + targeted range.**
3. Is the file > 200 lines? → **Read only the relevant section.**
4. Is the file a config or manifest? → **Read the whole file once; cache in your summary.**
5. Is the file a large data file (JSON/CSV > 100 rows)? → **Use grep_search; do not load whole file.**

---

## Phase 3 — Checkpoint Format

At the start of each phase (for Medium/Large tasks), write a compact checkpoint:

```
CHECKPOINT — <Phase Name>
========================
Completed:
  - [x] <action 1>
  - [x] <action 2>
In Progress:
  - [ ] <current action>
Remaining:
  - [ ] <next action>
  - [ ] <future action>
Key Context (do NOT re-derive):
  - <file>: <one-line summary of what was read>
  - <decision>: <what was decided and why>
Blocked: <reason, or NONE>
```

Write this as a response note or to a scratch file if the task is XL.

---

## Phase 4 — Tool Usage Discipline

### Batching
- When multiple independent reads/searches are needed, call them in parallel (one `<function_calls>` block with multiple tools).
- When a later tool depends on an earlier result, wait for the result before calling the next tool.

### Search-first protocol
Before `view_file` on a large file:
```
grep_search → find exact line numbers → view_file with StartLine/EndLine
```

### Write verification
After writing a file, do NOT re-read it to confirm unless the content is complex.
Trust the write confirmation response for simple files.

### Command output discipline
- Pipe long commands through `head` or `| Select-Object -First 50` in PowerShell.
- Do not run commands whose output you do not need.

---

## Phase 5 — Avoiding Repeated Work

Common patterns to eliminate:

| Anti-pattern | Correction |
|---|---|
| Re-reading the same file each turn | Read once; summarise key facts in checkpoint |
| Re-running tests after unrelated changes | Only re-run tests for changed modules |
| Re-deriving project structure | Write it in the checkpoint; reference it |
| Searching for the same symbol repeatedly | Note the file:line in the checkpoint |
| Re-explaining the plan each turn | Reference the checkpoint; do not restate |

---

## Phase 6 — Progress Tracking for XL Tasks

For tasks spanning many turns:
1. Create `<project-root>/.antigravity/progress.md` (or use the artifacts scratch dir).
2. Update it at the end of each phase:
   ```markdown
   # Task Progress
   Last updated: <timestamp>
   Overall: Phase N of M complete

   ## Phases
   - [x] Phase 1: <name>
   - [ ] Phase 2: <name> ← CURRENT
   - [ ] Phase 3: <name>

   ## Decisions Log
   - <decision>: <rationale>

   ## Files Modified
   - <file>: <change summary>
   ```
3. At session start, read `progress.md` first before any other file.

---

## Completion Criteria

- Task phases tracked with checkpoints
- No file read more than once unless modified
- No tool called with redundant intent
- Progress file exists and is current (for Large/XL tasks)
- User receives a concise summary, not a dump of intermediate steps
