"""Scheduler: orchestrates the devloop cycle."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from src.config import Config, load_config
from src.monitor import check_quota
from src.notifier import send_telegram, send_email
from src.picker import pick_issue
from src.worker import execute_task, TaskResult

log = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = Path.home() / ".config" / "devloop" / "config.yaml"


def run_cycle(config: Config, prompts_dir: Path) -> str:
    """Run one full scheduling cycle. Returns outcome string."""

    # Step 1: Check quota
    if not check_quota():
        send_telegram(config.notifications.telegram, "devloop: quota exhausted, skipping cycle")
        return "quota_exhausted"

    # Step 2-3: Pick an issue from any registered project
    selected_issue = None
    selected_project = None
    for project in config.projects:
        issue = pick_issue(project)
        if issue:
            selected_issue = issue
            selected_project = project
            break

    if not selected_issue or not selected_project:
        log.info("No actionable issues found across all projects")
        return "no_issues"

    # Step 4: Execute
    log.info("Executing issue #%d: %s", selected_issue.number, selected_issue.title)
    send_telegram(
        config.notifications.telegram,
        f"devloop: starting issue #{selected_issue.number}: {selected_issue.title}",
    )

    result = execute_task(
        repo_path=Path(selected_project.local_path),
        repo=selected_project.repo,
        issue_number=selected_issue.number,
        issue_title=selected_issue.title,
        issue_body=selected_issue.body,
        prompts_dir=prompts_dir,
        max_turns=config.worker.max_turns,
        model=config.worker.model,
        timeout_seconds=config.scheduler.max_runtime_minutes * 60,
    )

    # Step 5: Notify
    if result.success:
        msg = f"devloop: PR created for issue #{selected_issue.number}\n{result.pr_url}"
        send_telegram(config.notifications.telegram, msg)
        return "success"
    elif result.skip_reason:
        msg = f"devloop: skipped issue #{selected_issue.number}\nReason: {result.skip_reason}"
        send_telegram(config.notifications.telegram, msg)
        return "skipped"
    else:
        msg = f"devloop: failed on issue #{selected_issue.number}\nError: {result.error}"
        send_telegram(config.notifications.telegram, msg)
        return "failed"


def main():
    """CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    parser = argparse.ArgumentParser(description="devloop scheduler")
    parser.add_argument(
        "--config", type=Path, default=DEFAULT_CONFIG_PATH,
        help="Path to config file",
    )
    parser.add_argument(
        "--prompts-dir", type=Path, default=Path(__file__).parent.parent / "prompts",
        help="Path to prompts directory",
    )
    parser.add_argument(
        "--once", action="store_true",
        help="Run a single cycle and exit",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    outcome = run_cycle(config, prompts_dir=args.prompts_dir)
    log.info("Cycle outcome: %s", outcome)


if __name__ == "__main__":
    main()
