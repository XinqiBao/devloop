# Engineering Communication

Engineering artifacts should let future engineers and agents understand a decision or continue the work. State the decision and the facts, reasoning, limits, and uncertainty needed to use it later.

## State the decision and its basis

Lead with the conclusion or question the reader needs to act on. State the evidence and assumptions behind it.

For example, a caching decision should name the repeated work it avoids and the acceptable amount of stale data. "Cache for performance" does not show when the choice is valid.

State the concrete problem before introducing abstract terms. Prefer ordinary, precise language; use technical terms when they add precision. Keep each sentence focused on one point.

Use a short example when it shows why judgment changes between cases. Remove details that do not affect the decision, but keep the reasoning needed to apply or reassess it. Do not compress several decisions into one sentence to save space.

Present the conclusion and its basis directly. Do not make readers reconstruct them from the order in which the author discovered them.

## Match form to information

| Information | Useful form |
| --- | --- |
| One principle or conclusion | Direct sentence |
| Cause or tradeoff | Short prose |
| Independent factors | List with parallel items |
| Options compared on the same dimensions | Table |
| Flow, dependency, hierarchy, or ownership | Diagram when text is materially harder to follow |
| A boundary between nearby cases | Short contrast or example |

These are choices, not an artifact template. Use headings and structure to make important distinctions easy to scan. Do not add lists, tables, or diagrams merely for variety.

When a diagram makes a relationship clearer than text, use a maintainable format. Mermaid may suit a substantial relationship; simple ASCII may suit a small one. Keep the essential meaning available in text.

## Keep artifacts focused

Keep tracked engineering artifacts in English by default, subject to task intent and project conventions.

Omit prompt residue, agent narration, and automatic agent or tool attribution unless they affect a decision, provenance, reproducibility, or interpretation. Avoid decorative structure and fixed templates that add reading cost.
