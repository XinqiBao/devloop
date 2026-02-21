# devloop

AI autonomous development loop scheduler.

## Quick Reference

- Language: Python 3.10+
- Tests: `pytest tests/ -v`
- Install dev deps: `pip install -e ".[dev]"`
- Run manually: `python -m src.scheduler --once`

## Code Conventions

- Type hints on all function signatures
- Docstrings only where behavior is non-obvious
- No classes unless state management requires it; prefer functions + dataclasses
- All subprocess calls go through helper functions (never raw subprocess in business logic)
- Config values are never hardcoded; always read from config.yaml or environment

## Project Structure

- `src/` - Core modules (scheduler, worker, picker, reviewer, monitor, notifier, config)
- `tests/` - Pytest tests mirroring src/ structure
- `prompts/` - Prompt templates for Claude Code CLI
- `configs/` - Example configuration files (no secrets)
- `scripts/` - Deployment and maintenance scripts

## Testing

- Mock all external calls (subprocess, HTTP, file I/O to external paths)
- Test config validation with both valid and invalid inputs
- Test worker validation logic with synthetic git diffs
