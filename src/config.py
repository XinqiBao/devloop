"""Configuration loading and validation for devloop."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


class ConfigError(Exception):
    """Raised when configuration is invalid."""


@dataclass
class SchedulerConfig:
    interval_hours: int = 5
    max_runtime_minutes: int = 60


@dataclass
class WorkerConfig:
    max_turns: int = 30
    model: str = "claude-opus-4-6"


@dataclass
class ProjectConfig:
    name: str
    repo: str
    local_path: str
    labels_include: list[str] = field(default_factory=list)
    labels_exclude: list[str] = field(default_factory=list)


@dataclass
class TelegramConfig:
    bot_token: str = ""
    chat_id: str = ""


@dataclass
class EmailConfig:
    enabled: bool = False
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_pass: str = ""
    from_addr: str = ""
    to_addr: str = ""


@dataclass
class NotificationsConfig:
    telegram: TelegramConfig = field(default_factory=TelegramConfig)
    email: EmailConfig = field(default_factory=EmailConfig)


@dataclass
class MonitorConfig:
    fallback_model: str | None = None


@dataclass
class Config:
    scheduler: SchedulerConfig = field(default_factory=SchedulerConfig)
    worker: WorkerConfig = field(default_factory=WorkerConfig)
    projects: list[ProjectConfig] = field(default_factory=list)
    notifications: NotificationsConfig = field(default_factory=NotificationsConfig)
    monitor: MonitorConfig = field(default_factory=MonitorConfig)


ENV_VAR_PATTERN = re.compile(r"\$\{(\w+)\}")


def _substitute_env_vars(value: str) -> str:
    """Replace ${VAR_NAME} with environment variable values."""
    def replacer(match: re.Match) -> str:
        var_name = match.group(1)
        val = os.environ.get(var_name)
        if val is None:
            raise ConfigError(
                f"Environment variable {var_name} is referenced in config but not set"
            )
        return val
    return ENV_VAR_PATTERN.sub(replacer, value)


def _walk_and_substitute(obj: Any) -> Any:
    """Recursively substitute env vars in all string values."""
    if isinstance(obj, str):
        return _substitute_env_vars(obj)
    if isinstance(obj, dict):
        return {k: _walk_and_substitute(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_walk_and_substitute(item) for item in obj]
    return obj


def _build_dataclass(cls: type, data: dict | None) -> Any:
    """Build a dataclass instance from a dict, ignoring unknown keys."""
    if data is None:
        return cls()
    known_fields = {f.name for f in cls.__dataclass_fields__.values()}
    filtered = {k: v for k, v in data.items() if k in known_fields}
    return cls(**filtered)


def load_config(path: Path) -> Config:
    """Load and validate configuration from a YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ConfigError("Config file must be a YAML mapping")

    raw = _walk_and_substitute(raw)

    for section in ("scheduler", "worker", "projects"):
        if section not in raw:
            raise ConfigError(f"Missing required config section: {section}")

    scheduler = _build_dataclass(SchedulerConfig, raw.get("scheduler"))
    worker = _build_dataclass(WorkerConfig, raw.get("worker"))

    projects = []
    for p in raw.get("projects", []):
        projects.append(_build_dataclass(ProjectConfig, p))

    tg = _build_dataclass(TelegramConfig, (raw.get("notifications") or {}).get("telegram"))
    email = _build_dataclass(EmailConfig, (raw.get("notifications") or {}).get("email"))
    notifications = NotificationsConfig(telegram=tg, email=email)

    monitor = _build_dataclass(MonitorConfig, raw.get("monitor"))

    return Config(
        scheduler=scheduler,
        worker=worker,
        projects=projects,
        notifications=notifications,
        monitor=monitor,
    )
