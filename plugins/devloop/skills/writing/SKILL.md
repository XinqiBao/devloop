---
name: writing
description: "Apply the owner's writing preferences when drafting or revising code comments, docstrings, engineering documents, pull request descriptions, or durable explanations. Does not set the language or format of ordinary conversation."
---

# Writing

These are the owner's defaults; apply them within current task intent and project requirements.

Use concise English for tracked engineering artifacts unless current intent or legitimate project conventions call for another language. This does not set the language of ordinary conversation.

Engineering artifacts should let future engineers and agents understand a decision or continue the work. State the decision and the facts, reasoning, limits, and uncertainty needed to use it later.

## State the decision and its basis

Lead with the conclusion or question the reader needs to act on, then give the evidence and assumptions behind it. Order the explanation for the reader's decision rather than the author's discovery process.

For example, a caching decision should name the repeated work it avoids and the acceptable amount of stale data. "Cache for performance" does not show when the choice is valid.

State the concrete problem before introducing abstract terms. Prefer ordinary, precise language; use technical terms when they add precision. Keep each sentence focused on one point.

State concrete behavior and evidence instead of promotional language or unsupported claims of quality. Remove repeated caveats and boilerplate qualifications; retain conditions that affect correctness or the reader's decision.

Preserve technical meaning when editing. Do not invent guarantees, causes, or broader scope to make an explanation read smoothly.

Use a short example when it shows why judgment changes between cases. Remove details that do not affect the decision, but keep the reasoning needed to apply or reassess it. Do not compress several decisions into one sentence to save space.

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

When a diagram makes a relationship clearer than text, prefer Mermaid where the target surface renders it; simple ASCII can suffice for a small relationship. Keep diagrams consistent with the actual behavior and accompanying explanation, and keep the essential meaning available in text.

## Keep artifacts focused

Write for the intended reader's knowledge and decisions. Delivered documentation should explain the project, its behavior, and necessary caveats; omit basic tool tutorials and development-only trial instructions unless those are its purpose.

Use code comments and docstrings for contracts, constraints, or intent that is not clear from the code. Keep them accurate for current behavior; omit line-by-line paraphrases and accounts of the editing process.

Omit prompt residue, agent narration, and automatic agent or tool attribution unless they affect a decision, provenance, reproducibility, or interpretation. Avoid decorative structure and fixed templates that add reading cost.
