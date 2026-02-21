import os
import pytest
from pathlib import Path
from src.config import load_config, ConfigError


VALID_CONFIG = """
scheduler:
  interval_hours: 5
  max_runtime_minutes: 60
worker:
  max_turns: 30
  model: claude-opus-4-6
projects:
  - name: TestProject
    repo: owner/repo
    local_path: /tmp/test-repo
    labels_include: [auto]
    labels_exclude: [wontfix]
notifications:
  telegram:
    bot_token: "test-token"
    chat_id: "12345"
  email:
    enabled: false
monitor:
  fallback_model: null
"""


def test_load_valid_config(tmp_path):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(VALID_CONFIG)
    config = load_config(cfg_file)
    assert config.scheduler.interval_hours == 5
    assert config.worker.max_turns == 30
    assert len(config.projects) == 1
    assert config.projects[0].name == "TestProject"


def test_env_var_substitution(tmp_path, monkeypatch):
    monkeypatch.setenv("TEST_TOKEN", "secret-123")
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(VALID_CONFIG.replace(
        '"test-token"', "${TEST_TOKEN}"
    ))
    config = load_config(cfg_file)
    assert config.notifications.telegram.bot_token == "secret-123"


def test_missing_env_var_raises(tmp_path):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(VALID_CONFIG.replace(
        '"test-token"', "${NONEXISTENT_VAR}"
    ))
    with pytest.raises(ConfigError, match="NONEXISTENT_VAR"):
        load_config(cfg_file)


def test_missing_required_field(tmp_path):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text("scheduler:\n  interval_hours: 5\n")
    with pytest.raises(ConfigError):
        load_config(cfg_file)


def test_config_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_config(Path("/nonexistent/config.yaml"))
