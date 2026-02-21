"""Monitor: quota checking and health status."""

from __future__ import annotations

import logging
import subprocess

log = logging.getLogger(__name__)


def check_quota(timeout_seconds: int = 30) -> bool:
    """Probe Claude Code CLI to check if quota is available.

    Runs a minimal prompt and checks for success. Returns False on
    rate limit errors or timeouts.
    """
    try:
        result = subprocess.run(
            [
                "claude", "-p", "Reply with exactly: ok",
                "--dangerously-skip-permissions",
                "--max-turns", "1",
                "--output-format", "json",
            ],
            capture_output=True, text=True,
            timeout=timeout_seconds,
        )
        if result.returncode != 0:
            log.warning("Quota probe failed (exit %d): %s", result.returncode, result.stderr)
            return False
        return True

    except subprocess.TimeoutExpired:
        log.warning("Quota probe timed out after %ds", timeout_seconds)
        return False
