---
name: devloop-knowledge
description: "Decide what engineering findings, rationale, or active task state to retain, where to put them, and when to retire them. Use during substantial investigations, handoffs, or resumption when continuity matters; small edits do not require new notes."
---

# Knowledge and Continuity

These are the owner's defaults; apply them within current task intent and project requirements.

Keep information after a task when its loss would make a future decision harder, less reliable, or require avoidable investigation. Preserve what is needed to apply or reassess the conclusion, not the full investigation record.

This skill decides what to retain, where it belongs, and when it expires. [devloop-communication](../devloop-communication/SKILL.md) governs how to express it.

## Record what future decisions need

Depending on the decision, useful durable information may include:

- **Constraints and decisions** that future changes must respect.
- **Non-obvious rationale and evidence** needed to judge whether a conclusion still holds.
- **Exact identifiers and provenance** needed to locate or reproduce a finding.
- **Unresolved uncertainty** that would change how confidently the conclusion can be used.

These are possibilities, not fields to fill in. State the scope of each claim. An observation about one module does not establish a project-wide rule; a conclusion without its essential evidence or limits can mislead future work.

Preserve decision provenance when it matters. Explicit owner requirements, accepted provisional recommendations, and inferred defaults have different force; do not relabel one as another during a handoff or extraction.

## Place current facts at the point of use

Place a current fact near the code, interface, or project guidance where readers need it. Keep one authoritative source for each project fact. Link to that source from other entry points instead of copying it; copies can drift.

For example, state a current API constraint near the interface. Link to the commit that introduced it if the rationale matters. The interface states what applies now; history explains why it changed.

## Close out investigation notes

During active work, observations, hypotheses, and failed approaches may help continuity. At completion, retain only conclusions and supporting detail future work needs. Keep a failed approach when its reason for failure would otherwise be rediscovered; retire the rest.

Before cleanup or migration, check for unique authored knowledge and necessary evidence even in ignored or generated-looking locations. Distill it into existing project surfaces where appropriate. Historical existence alone does not justify a permanent archive, and a cleaner directory is not worth losing useful information.

When creating or maintaining temporary working state, handing off, or resuming interrupted work, read [Working context](references/working-context.md). Use [devloop-communication](../devloop-communication/SKILL.md) when writing the conclusions that remain.
