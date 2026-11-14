# Status Lines

A status line can keep a few useful session facts visible while working with a coding agent. Treat it as an optional interface preference, not an instruction to the agent. Keep it short enough for the terminal in use.

Start with the current model, a compact project or working-directory name, the Git branch when relevant, and context-window usage when available. These help identify the session and notice when context is getting crowded. Show a rate limit or estimated session cost when that figure is available and helps decide what to do next. A rate limit and a cost estimate answer different questions; choose for the account and workflow rather than displaying both by default.

Raw token totals, session IDs, lines changed, and API wait time have narrower uses. Add them for a specific need instead of filling the status line with every available field. Omit unavailable values rather than displaying a misleading zero, and distinguish estimated cost from an actual bill.

## Apply in supported tools

- **Codex CLI:** Use [`/statusline`](https://learn.chatgpt.com/docs/developer-commands#configure-footer-items-with-statusline) to select and order the available footer items. It persists the selection in `config.toml`.
- **Claude Code:** Use [`/statusline`](https://code.claude.com/docs/en/statusline) to describe the desired display. Claude Code generates a status-line script and configures it in settings. Review the generated script and its dependencies for the target environment.

Check the installed tool's current capabilities before applying this preference. Keep the resulting settings in that tool's native configuration and verify the display in a representative session.
