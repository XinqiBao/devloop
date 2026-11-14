---
name: devloop-core
description: Apply the owner's cross-project engineering defaults when investigating, changing, reviewing, or resuming software work. Load at engineering session start and restore after compaction; use the relevant situational skills as work progresses.
---

# Engineering Defaults

These are the owner's engineering defaults. Apply them within current explicit task intent and legitimate project requirements. Loading guidance does not authorize additional work or external actions. Surface material conflicts.

- Inspect affected behavior, instructions, existing work, and system boundaries before consequential changes. Preserve changes already in progress. Distinguish evidence from assumptions and investigate in proportion to uncertainty, impact, and recovery cost.
- Keep the intended outcome, authority, constraints, and completion bounds clear. Ask about ambiguity that materially changes those bounds; make routine choices and continue through verification and ordinary repair within them.
- Choose the least costly checks that cover the relevant failure risk. A build or unit test supports only what it exercises. Report what was checked, meaningful gaps, and uncertainty; revise a diagnosis or completion claim when contrary evidence appears.
- Keep substantial changes understandable and work resumable. Preserve only the state that would otherwise be costly to reconstruct. Do not require plans, progress notes, or a fixed workflow for every task.
- Retain durable knowledge and non-obvious reasoning where future decisions need them. Avoid competing sources, stale records, and mechanisms whose continuing cost exceeds their demonstrated benefit. Prefer sufficient native capabilities.
- Use concise English for tracked engineering artifacts unless current intent or legitimate project conventions call for another language. This does not set the language of conversation.

## Load guidance at the point of use

Use these installed skills when work enters the relevant situation, including stages reached inside a longer task. A plugin may prefix their names with its namespace.

- **devloop-commits:** before grouping changes into commits, writing commit messages, or assessing history. Use Conventional Commits and coherent engineering intent by default.
- **devloop-communication:** when writing engineering documents, pull request descriptions, or lasting explanations. Lead with the decision and useful evidence; omit incidental agent narration and automatic attribution unless useful or required.
- **devloop-knowledge:** when deciding what findings or active state to preserve, during a handoff, or when recovering substantial interrupted work. Small work may need no separate record.

For a consequential decision that needs more reasoning about investigation, authority, verification, continuity, or persistent mechanisms, read [Engineering judgment](references/judgment.md). These judgments interact; they are not mandatory stages or gates.
