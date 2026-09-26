# Engineering Communication

Engineering artifacts should let future engineers and agents understand a decision or continue the work without unnecessary interpretation. State the engineering point directly, with the facts, reasoning, limits, and uncertainty needed to use it after the author is gone.

## Make the judgment visible

Lead with the conclusion or question the reader needs to act on. Expose the reason it follows from the evidence and the assumptions on which it depends. A design note recommending caching, for example, should identify the repeated work it avoids and the amount of stale data the system can tolerate. "Cache for performance" leaves the decision's boundary hidden.

State the concrete problem before introducing abstract terms. Prefer ordinary, precise language unless technical terminology adds useful precision. Keep each sentence focused on one main point so readers need not unpack unrelated ideas at once.

Use a short example when it shows why judgment changes between cases. Remove detail that does not help the reader, but retain reasoning needed to apply or reassess the conclusion. Avoid process narration that makes readers reconstruct the point from the sequence in which the author discovered it.

## Match form to information

| Information | Useful form |
| --- | --- |
| One principle or conclusion | Direct sentence |
| Cause or tradeoff | Short prose |
| Independent factors | List with parallel items |
| Options compared on the same dimensions | Table |
| Flow, dependency, hierarchy, or ownership | Diagram when text is materially harder to follow |
| A boundary between nearby cases | Short contrast or example |

These are choices, not an artifact template. Make important structure visible in headings and structured elements so a reader can scan the model before reading its qualifications. Do not add lists, tables, or diagrams merely for variety. When a diagram is warranted, a maintainable text format such as Mermaid may suit a substantial relationship; simple ASCII may suit a small one. Keep the essential meaning available in text.

## Leave useful signal

Keep tracked engineering artifacts in English by default, subject to explicit task intent and project conventions. Omit prompt residue, agent narration, and automatic agent or tool attribution unless they affect a decision, provenance, reproducibility, or interpretation. Decorative structure and fixed templates add reading cost without improving judgment.
