# Working Context

Working context holds useful state that is not yet in code or durable project records. Keep a note when an interruption would make important findings, decisions, or next steps costly or unreliable to reconstruct.

- A small change clear from its diff may need no note.
- A long investigation with unresolved hypotheses may need one.

An open task alone does not justify a persistent note.

## Scope and authority

Keep working context at the narrowest useful scope. A project-specific assumption in environment-wide guidance can mislead work in other projects.

Working context may live at environment, repository, or task scope. `~/.context/` and `<repo>/.context/` are examples, not required locations. A directory name does not determine the authority or lifetime of every file in it.

Working context is subordinate to tracked project truth. Check it against the present environment before relying on it, especially after an interruption. A stale assumption, plan, or unresolved issue can misdirect later work.

## Retire or promote

Keep working context current while it helps continuity. When that need ends, remove the note from the active path. Put any lasting conclusion in its proper durable location using [Durable Knowledge](knowledge.md). Do not leave a second authority for project facts.

Do not use `.context/` for:

- Prompt or transcript archives.
- Routine reports or duplicate project facts.
- Secrets or backups.

Ignored files are not automatically secure or durable. Store secrets and irreplaceable information in appropriate locations.
