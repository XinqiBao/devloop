# Workflow Lifecycle

This lifecycle defines required phases from request intake to process improvement.

## 1. clarify

Inputs:
- Problem statement or change request
- Known constraints and desired outcomes

Outputs:
- Confirmed scope
- Explicit assumptions and success criteria

Acceptance criteria:
- Request intent is unambiguous
- Scope boundaries and risks are documented

## 2. design

Inputs:
- Clarified scope and constraints
- Existing architecture and governance context

Outputs:
- Evaluated solution options with trade-offs
- Approved design direction

Acceptance criteria:
- Design decisions are documented with rationale
- Stakeholder approval is captured before planning

## 3. plan

Inputs:
- Approved design
- Repository context and dependency graph

Outputs:
- Ordered implementation tasks
- Verification commands for each task

Acceptance criteria:
- Tasks are executable and testable
- Dependencies and checkpoints are explicit

## 4. execute

Inputs:
- Approved implementation plan
- Isolated working branch/workspace

Outputs:
- Incremental changes aligned with planned tasks
- Task-level evidence logs

Acceptance criteria:
- Work follows planned order unless approved deviation
- Each completed task includes command-based verification

## 5. verify

Inputs:
- Implemented changes
- Task-level verification outputs

Outputs:
- Consolidated verification summary
- Pass/fail decision for release readiness

Acceptance criteria:
- All required checks pass
- No unresolved critical issues remain

## 6. improve

Inputs:
- Verification summary
- Execution friction notes

Outputs:
- Governance updates (status/changelog/decisions as needed)
- Actionable improvements for future runs

Acceptance criteria:
- At least one concrete improvement or explicit "no changes needed" record
- Canonical docs remain consistent with actual workflow behavior
