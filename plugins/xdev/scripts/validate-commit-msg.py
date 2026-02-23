#!/usr/bin/env python3
"""PreToolUse hook: validate git commit messages follow Conventional Commits."""

import json
import re
import sys

CONVENTIONAL_PATTERN = re.compile(
    r'^(feat|fix|refactor|docs|test|chore|perf|build)'
    r'(\([a-z0-9_-]+\))?'
    r': [a-z]'
)

COMMIT_CMD_PATTERN = re.compile(r'git\s+commit')

MSG_WARN = """\
**Conventional Commits Format Check**

Verify your commit message follows this format:

```
<type>(<scope>): <subject>
```

- **type**: feat/fix/refactor/docs/test/chore/perf/build
- **scope**: optional, lowercase, hyphens/underscores only
- **subject**: imperative mood, lowercase start, no period, max 50 chars

If the message does not match, abort and fix it."""


def extract_commit_message(command):
    """Extract commit message from git commit command."""
    # Match -m "message" or -m 'message'
    m = re.search(r'-m\s+["\'](.+?)["\']', command)
    if m:
        return m.group(1).strip()

    # Match heredoc style: -m "$(cat <<'EOF'\nmessage\nEOF\n)"
    m = re.search(r"-m\s+\"\$\(cat\s+<<'?EOF'?\n(.+?)\nEOF", command, re.DOTALL)
    if m:
        return m.group(1).strip()

    return None


def main():
    try:
        input_data = json.load(sys.stdin)
        tool_input = input_data.get('tool_input', {})
        command = tool_input.get('command', '')

        if not COMMIT_CMD_PATTERN.search(command):
            print('{}')
            sys.exit(0)

        msg = extract_commit_message(command)

        if msg is None:
            # Can't extract message (e.g., interactive commit) — warn
            print(json.dumps({"systemMessage": MSG_WARN}))
            sys.exit(0)

        # Check first line of message
        first_line = msg.split('\n')[0].strip()

        if CONVENTIONAL_PATTERN.match(first_line):
            # Valid format
            if len(first_line) > 50:
                print(json.dumps({
                    "systemMessage": f"**Commit subject too long** ({len(first_line)} chars). "
                                     "Keep under 50 characters."
                }))
            else:
                print('{}')
            sys.exit(0)

        # Invalid format — warn (not block, to avoid false positives)
        print(json.dumps({"systemMessage": MSG_WARN}))
        sys.exit(0)

    except Exception:
        print('{}')
        sys.exit(0)


if __name__ == '__main__':
    main()
