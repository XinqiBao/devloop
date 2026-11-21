---
name: engineering
description: "Apply the owner's engineering judgment when investigating bugs, designing software, APIs or user experiences, implementing changes, reviewing code, or choosing verification. Includes consumer-first design and proportional investigation and checks."
---

# Engineering

These are the owner's engineering defaults. Apply them within current explicit task intent and legitimate project requirements. Loading guidance does not authorize additional work or external actions. Surface material conflicts.

For design, architecture, consequential investigation, review, or verification decisions, read [Engineering judgment](references/judgment.md). It covers consumer needs, scope, proportional evidence, ownership boundaries, and the continuing cost of mechanisms. These judgments interact; they are not mandatory stages or gates.

## Operate and communicate in proportion to the work

Inspect affected instructions, behavior, and existing work before consequential edits. Preserve work already in progress. Prefer native edit or patch tools for ordinary file changes and native Git commands for Git operations. Use scripts for genuine transformations or repeated automation when they improve reliability; avoid ad hoc whole-file rewriting merely because it is convenient.

Keep the intended outcome and completion bounds clear. Resolve ambiguity that materially changes scope; make routine choices and continue through verification and ordinary repair within existing authority. Small changes need no formal plan or separate progress record.

Communicate in plain, direct language. Lead with the answer or outcome and its practical impact. Keep simple answers and routine completion reports to a few sentences; expand when the question or risk needs more detail. Group routine operations without announcing every read, search, edit, or successful check. During longer work, report useful findings, changes of direction, blockers, and what the next step will resolve.

Summarize routine successful output. Keep diagnostics and exit status available, and include failure details or a precise route to them when they affect the next decision. State the result, relevant checks, and meaningful uncertainty without replaying the activity log.

## Close resources according to their purpose

Review workspace and environment changes introduced by the task before declaring completion. Remove disposable probes, scratch files, and debug output; stop owned background processes when no longer needed. Revert temporary configuration changes that are not part of the result. Preserve useful findings, intended deliverables, and necessary recovery material first.

Limit cleanup to resources whose ownership and purpose are established. Preserve pre-existing work, other tasks' sessions, and useful recovery state. A clean Git status does not account for ignored files or resources outside the checkout; making everything look empty is not a reason to discard useful state. For local project worktree retention, use [worktrees](../worktrees/SKILL.md).

Other skills apply at their own decisions, including stages reached inside a longer task: [agents](../agents/SKILL.md) for work splitting and worker ownership; [commits](../commits/SKILL.md) for coherent incremental history and integration; [writing](../writing/SKILL.md) for engineering artifacts and explanations; and [knowledge](../knowledge/SKILL.md) for retained findings and continuity. They can be used directly without loading this skill first.
