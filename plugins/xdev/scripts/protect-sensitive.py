#!/usr/bin/env python3
"""PreToolUse hook: block editing sensitive files."""

import json
import re
import sys

SENSITIVE_PATTERN = re.compile(
    r'(\.env$|\.env\.|credentials|secret|\.pem$|\.key$|id_rsa|id_ed25519)',
    re.IGNORECASE
)

MSG_BLOCK = """\
**Sensitive File Protection**

This file matches sensitive patterns (*.env, *credentials*, *secret*, \
*.pem, *.key, SSH keys).

These files may contain secrets, API keys, or private credentials. \
Edit them manually outside of Claude Code if needed."""


def main():
    try:
        input_data = json.load(sys.stdin)
        tool_input = input_data.get('tool_input', {})
        file_path = tool_input.get('file_path', '')

        if not file_path:
            print('{}')
            sys.exit(0)

        if SENSITIVE_PATTERN.search(file_path):
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny"
                },
                "systemMessage": MSG_BLOCK
            }))
            sys.exit(2)

        print('{}')
        sys.exit(0)

    except Exception:
        print('{}')
        sys.exit(0)


if __name__ == '__main__':
    main()
