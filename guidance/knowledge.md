# Durable Knowledge

Keep information after a task when losing it would make a future decision harder, less reliable, or require avoidable investigation. Preserve enough to apply or reassess a conclusion, not the full record of how it was reached.

## Keep what future decisions need

Depending on the decision, useful durable information may include:

- **Constraints and decisions** that future changes must respect.
- **Non-obvious rationale and evidence** needed to judge whether a conclusion still holds.
- **Exact identifiers and provenance** needed to locate or reproduce a finding.
- **Unresolved uncertainty** that would change how confidently the conclusion can be used.

These are possibilities, not fields to fill in. State the scope of a claim: an observation about one module does not establish a project-wide rule. A bare conclusion can mislead when its evidence or limits are essential to applying it.

## Put current truth near its readers

Place a fact where readers will look while making the relevant decision: near the code, interface, or project guidance it concerns. Keep one authoritative home for a project fact and link to it from other entry points when needed. Copies can drift and leave readers unsure which version to trust.

An API constraint kept only in an old commit message is easy to miss during API work. State the current constraint near the interface; link to the historical decision if its rationale matters. History explains why a change happened, while the active location states what applies now.

## Distill and retire investigation state

While work is active, observations, hypotheses, and failed approaches may help continuity. When it ends, retain the conclusions and supporting detail future work needs. Keep a failed approach if its reason for failure would otherwise be rediscovered; retire the rest instead of preserving a transcript.

[Working context](context.md) covers temporary continuity state. [Engineering communication](communication.md) covers how to express what remains.
