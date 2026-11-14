#!/bin/sh
# Emit the body of the installed plugin's engineering defaults as SessionStart context.
set -eu

if [ -z "${CLAUDE_PLUGIN_ROOT:-}" ]; then
	printf 'devloop: CLAUDE_PLUGIN_ROOT is not set\n' >&2
	exit 2
fi

skill_dir="$CLAUDE_PLUGIN_ROOT/skills/engineering"
core="$skill_dir/SKILL.md"

if [ ! -f "$core" ] || [ ! -r "$core" ]; then
	printf 'devloop: cannot read core policy: %s\n' "$core" >&2
	exit 2
fi

body=$(awk '
	NR == 1 && $0 == "---" { frontmatter = 1; next }
	frontmatter && $0 == "---" { frontmatter = 0; next }
	!frontmatter {
		if (!started && $0 == "") next
		started = 1
		print
	}
' "$core")

if [ -z "$body" ]; then
	printf 'devloop: core policy has no body: %s\n' "$core" >&2
	exit 2
fi

printf 'devloop:engineering source: %s\n' "$core"
printf 'relative references resolve from: %s\n\n' "$skill_dir"
printf '%s\n' "$body"
