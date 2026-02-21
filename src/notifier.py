"""Notifications: Telegram Bot and Email."""

from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage

import requests

from src.config import TelegramConfig, EmailConfig

log = logging.getLogger(__name__)


def send_telegram(config: TelegramConfig, message: str) -> None:
    """Send a message via Telegram Bot API direct to the owner."""
    if not config.bot_token or not config.chat_id:
        log.debug("Telegram not configured, skipping")
        return

    url = f"https://api.telegram.org/bot{config.bot_token}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": config.chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }, timeout=10)

    if resp.status_code != 200:
        log.warning("Telegram send failed: %s %s", resp.status_code, resp.text)


def send_email(config: EmailConfig, subject: str, body: str) -> None:
    """Send an email via SMTP."""
    if not config.enabled:
        log.debug("Email not enabled, skipping")
        return

    msg = EmailMessage()
    msg["Subject"] = f"[devloop] {subject}"
    msg["From"] = config.from_addr
    msg["To"] = config.to_addr
    msg.set_content(body)

    with smtplib.SMTP(config.smtp_host, config.smtp_port) as smtp:
        smtp.starttls()
        smtp.login(config.smtp_user, config.smtp_pass)
        smtp.send_message(msg)

    log.info("Email sent: %s", subject)
