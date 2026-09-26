# Durable Knowledge

Keep information after a task when its loss would make a future decision harder, less reliable, or require avoidable investigation. Preserve what is needed to apply or reassess the conclusion, not the full investigation record.

## Record what future decisions need

Depending on the decision, useful durable information may include:

- **Constraints and decisions** that future changes must respect.
- **Non-obvious rationale and evidence** needed to judge whether a conclusion still holds.
- **Exact identifiers and provenance** needed to locate or reproduce a finding.
- **Unresolved uncertainty** that would change how confidently the conclusion can be used.

These are possibilities, not fields to fill in. State the scope of each claim. An observation about one module does not establish a project-wide rule; a conclusion without its essential evidence or limits can mislead future work.

## Place current facts at the point of use

Place a current fact near the code, interface, or project guidance where readers need it. Keep one authoritative source for each project fact. Link to that source from other entry points instead of copying it; copies can drift.

For example, state a current API constraint near the interface. Link to the commit that introduced it if the rationale matters. The interface states what applies now; history explains why it changed.

## Close out investigation notes

During active work, observations, hypotheses, and failed approaches may help continuity. At completion, retain only conclusions and supporting detail future work needs. Keep a failed approach when its reason for failure would otherwise be rediscovered; retire the rest.

[Working context](context.md) covers temporary continuity state. [Engineering communication](communication.md) covers how to express what remains.
