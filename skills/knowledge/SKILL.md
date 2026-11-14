---
name: knowledge
description: "Organize and retain engineering findings, rationale, or active task state: decide what belongs in scoped local knowledge or tracked records, where to put it, and when to retire it. Use during substantial investigations, handoffs, or resumption when continuity matters; small edits do not require new notes."
---

# Knowledge and Continuity

These are the owner's defaults; apply them within current task intent and project requirements.

Keep information after a task when its loss would make a future decision harder, less reliable, or require avoidable investigation. Preserve what is needed to apply or reassess the conclusion, not the full investigation record.

This skill decides what to retain, where it belongs, and when it expires.

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

Prefer tracked project records for knowledge that another contributor or agent needs: shared conventions, supported behavior, design rationale, and collaboration boundaries. This makes the same information available across checkouts, machines, and parallel workers. Extend the relevant code, document, or project entry point rather than creating a separate agent-only copy.

Keep the default entry path short and route readers to the relevant detail. A project instruction file should expose operative rules and navigation, not accumulate every investigation or implementation detail. Temporary coordination state may also belong in a tracked project record when the participants need shared access; give it an owner and retire it when the work ends. Personal environment facts, raw transcripts, and each worker's live scratch state do not become shared policy merely because an agent uses them.

## Close out investigation notes

During active work, observations, hypotheses, and failed approaches may help continuity. At completion, retain only conclusions and supporting detail future work needs. Keep a failed approach when its reason for failure would otherwise be rediscovered; retire the rest.

Before cleanup or migration, check for unique authored knowledge and necessary evidence even in ignored or generated-looking locations. Distill it into existing project surfaces where appropriate. Historical existence alone does not justify a permanent archive, and a cleaner directory is not worth losing useful information.

When organizing scoped local knowledge, creating or maintaining temporary working state, handing off, or resuming interrupted work, read [Scoped context](references/scoped-context.md). Use [writing](../writing/SKILL.md) when writing the conclusions that remain.
