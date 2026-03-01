# Quality Gates

Completion requires passing every gate below.

## Gate 1: Scoped Acceptance

Required evidence:
- Documented scope and acceptance criteria
- Explicit out-of-scope notes when needed

Fail conditions:
- Execution starts without agreed criteria
- Scope keeps changing without recorded approval

## Gate 2: Plan Traceability

Required evidence:
- Ordered task list linked to design decisions
- Verification command listed for each task or batch

Fail conditions:
- Tasks are executed ad hoc without traceable plan mapping
- Verification steps are missing or ambiguous

## Gate 3: Implementation Integrity

Required evidence:
- Changes correspond to planned tasks
- Dependency order respected for stateful edits

Fail conditions:
- Unapproved scope expansion
- Mixed unrelated changes that cannot be reviewed independently

## Gate 4: Verification Evidence

Required evidence:
- Executed commands and concise result summaries
- Explicit pass/fail statement per gate-relevant check

Fail conditions:
- Completion claims rely on intuition only
- Failed checks are ignored or not addressed

## Gate 5: Governance Consistency

Required evidence:
- Canonical docs updated for policy/process changes
- Legacy paths either removed or converted to pointers

Fail conditions:
- Multiple conflicting authoritative docs remain
- Active onboarding paths point to obsolete material

## Gate 6: Integration Provenance

Required evidence:
- PR identifier (or local merge record) and merge method
- Confirmation that task-level commits are preserved
- Explicit statement that squash merge was not used

Fail conditions:
- Squash merge collapses task-level commit history
- History rewrite occurs without explicit approval
- Merge method is undocumented in completion report

## Evidence Format

Use this compact format for each verification block:

- command: `<exact command>`
- result: `<pass/fail + short factual summary>`
- artifacts: `<changed files or commit ids, if applicable>`

A task or batch is complete only when all required gates are satisfied.
