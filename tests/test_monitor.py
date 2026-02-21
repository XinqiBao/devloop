import subprocess
import pytest
from unittest.mock import patch, MagicMock
from src.monitor import check_quota


@patch("src.monitor.subprocess.run")
def test_check_quota_available(mock_run):
    mock_run.return_value = MagicMock(returncode=0, stdout='{"result":"ok"}', stderr="")
    assert check_quota() is True


@patch("src.monitor.subprocess.run")
def test_check_quota_exhausted(mock_run):
    mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="rate limit")
    assert check_quota() is False


@patch("src.monitor.subprocess.run")
def test_check_quota_timeout(mock_run):
    mock_run.side_effect = subprocess.TimeoutExpired(cmd="claude", timeout=30)
    assert check_quota() is False
