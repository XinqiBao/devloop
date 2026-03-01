# Core Principles

This file defines non-negotiable workflow rules. Platform adapters may map these rules to tooling, but cannot redefine them.

## quality-first

Every implementation must start with explicit acceptance criteria and quality targets.

Enforcement:
- Do not begin execution until scope, constraints, and acceptance criteria are written.
- Prefer the smallest change that satisfies requirements with maintainable quality.
- If quality gates fail, work is not complete.

## evidence-before-claim

No completion claim is valid without concrete verification evidence.

Enforcement:
- Every task must include verification commands.
- Reports must include command result summaries tied to acceptance criteria.
- "Looks good" is not evidence.

## context-budget

Work must be structured to fit available context without losing correctness.

Enforcement:
- Keep canonical rules in one place to avoid repeating large instructions.
- Split large initiatives into bounded batches with explicit checkpoints.
- Use concise state handoff notes when pausing or switching sessions.

## parallel-when-safe

Use parallel execution only when tasks are independent and state-isolated.

Enforcement:
- Run independent reads/checks/analysis in parallel to reduce cycle time.
- Force serial execution for shared-state edits or ordered dependencies.
- If dependency is unclear, treat as serial.

## self-improvement-loop

Each completed initiative should improve the workflow system itself.

Enforcement:
- Capture friction points discovered during execution.
- Record concrete process changes in governance documents.
- Prefer small iterative improvements over infrequent large rewrites.
