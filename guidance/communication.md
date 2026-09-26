# Engineering Communication

Engineering artifacts should help their readers make a decision or continue the work. Before writing documentation, a plan, an investigation note, or a review, identify what the reader needs to understand and do. Keep the relevant facts, reasoning, uncertainty, and boundaries visible after the author is gone.

## Explain the engineering reason

State the concrete problem before introducing abstract terms. Explain why a recommendation follows from the evidence and when it might change. For example, a design note that recommends caching should say what repeated work it avoids and how much stale data the system can tolerate. "Cache for performance" alone leaves the next engineer unable to judge whether the choice still fits.

Prefer direct sentences with one main point each. Use an example when it teaches a real boundary. Be concise by removing detail the reader does not need, not by removing reasoning that supports a decision.

## Choose a useful form

Use prose for a short explanation, bullets for distinct factors, and a table when readers need to compare the same dimensions across cases. Use a diagram when a flow, dependency, or ownership relationship is materially easier to understand visually. A text-based format such as Mermaid can make a substantial diagram easier to maintain when readers can render it; simple ASCII may be clearer for a small relationship. Keep the essential meaning in surrounding text so a diagram is not the only way to understand the guidance.

Avoid process narration, decorative structure, and fixed templates that make readers search for the point. Keep tracked engineering artifacts in English by default, subject to explicit task intent and project conventions. Prompt residue and automatic agent or tool attribution usually add little; retain them when they matter to a decision, provenance, reproducibility, or later interpretation.
