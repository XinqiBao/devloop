# devloop

An AI autonomous development loop scheduler. Runs on a remote machine, picks up
GitHub issues, implements solutions via Claude Code CLI, and submits PRs.

## Features

- Automatic issue selection and prioritization
- Claude Code CLI execution in isolated git worktrees
- Safety validation before PR submission
- Telegram and email notifications
- Code review and issue discovery during idle time
- 5-hour scheduling aligned with Claude Pro quota refresh

## Quick Start

1. Clone: `git clone git@github.com:XinqiBao/devloop.git`
2. Install: `pip install -e ".[dev]"`
3. Configure: `cp configs/config.example.yaml ~/.config/devloop/config.yaml`
4. Edit config with your settings
5. Run once: `python -m src.scheduler --once`

## Documentation

- [Design Document](docs/plans/2026-02-21-devloop-design.md)

## License

MIT
