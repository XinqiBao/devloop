import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.scheduler import run_cycle
from src.config import (
    Config, SchedulerConfig, WorkerConfig, ProjectConfig,
    NotificationsConfig, TelegramConfig, EmailConfig, MonitorConfig,
)
from src.picker import Issue


def _make_config(tmp_path):
    return Config(
        scheduler=SchedulerConfig(interval_hours=5, max_runtime_minutes=60),
        worker=WorkerConfig(max_turns=10, model="claude-opus-4-6"),
        projects=[ProjectConfig(
            name="Test", repo="owner/repo",
            local_path=str(tmp_path / "repo"),
            labels_include=["auto"], labels_exclude=["wontfix"],
        )],
        notifications=NotificationsConfig(
            telegram=TelegramConfig(bot_token="tok", chat_id="123"),
            email=EmailConfig(enabled=False),
        ),
        monitor=MonitorConfig(fallback_model=None),
    )


@patch("src.scheduler.check_quota", return_value=False)
@patch("src.scheduler.send_telegram")
def test_cycle_skips_when_no_quota(mock_tg, mock_quota, tmp_path):
    config = _make_config(tmp_path)
    result = run_cycle(config, prompts_dir=Path("prompts"))
    assert result == "quota_exhausted"
    mock_tg.assert_called_once()


@patch("src.scheduler.check_quota", return_value=True)
@patch("src.scheduler.pick_issue", return_value=None)
@patch("src.scheduler.send_telegram")
def test_cycle_runs_review_when_no_issues(mock_tg, mock_pick, mock_quota, tmp_path):
    config = _make_config(tmp_path)
    result = run_cycle(config, prompts_dir=Path("prompts"))
    assert result == "no_issues"


@patch("src.scheduler.check_quota", return_value=True)
@patch("src.scheduler.pick_issue")
@patch("src.scheduler.execute_task")
@patch("src.scheduler.send_telegram")
def test_cycle_executes_and_notifies_success(mock_tg, mock_exec, mock_pick, mock_quota, tmp_path):
    from src.worker import TaskResult
    mock_pick.return_value = Issue(
        number=42, title="feat: test", body="desc",
        labels=["auto"], created_at="2026-01-01",
    )
    mock_exec.return_value = TaskResult(success=True, pr_url="https://github.com/pr/1")
    config = _make_config(tmp_path)
    result = run_cycle(config, prompts_dir=Path("prompts"))
    assert result == "success"
    assert mock_tg.call_count == 2  # start + success


@patch("src.scheduler.check_quota", return_value=True)
@patch("src.scheduler.pick_issue")
@patch("src.scheduler.execute_task")
@patch("src.scheduler.send_telegram")
def test_cycle_handles_failure(mock_tg, mock_exec, mock_pick, mock_quota, tmp_path):
    from src.worker import TaskResult
    mock_pick.return_value = Issue(
        number=42, title="feat: test", body="desc",
        labels=["auto"], created_at="2026-01-01",
    )
    mock_exec.return_value = TaskResult(success=False, error="tests failed")
    config = _make_config(tmp_path)
    result = run_cycle(config, prompts_dir=Path("prompts"))
    assert result == "failed"
