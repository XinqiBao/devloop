import pytest
from unittest.mock import patch, MagicMock
from src.notifier import send_telegram, send_email
from src.config import TelegramConfig, EmailConfig


@patch("src.notifier.requests.post")
def test_send_telegram(mock_post):
    mock_post.return_value = MagicMock(status_code=200)
    tg = TelegramConfig(bot_token="fake-token", chat_id="12345")
    send_telegram(tg, "Test message")
    mock_post.assert_called_once()
    call_url = mock_post.call_args[0][0]
    assert "fake-token" in call_url
    assert mock_post.call_args[1]["json"]["chat_id"] == "12345"
    assert mock_post.call_args[1]["json"]["text"] == "Test message"


@patch("src.notifier.requests.post")
def test_send_telegram_skips_when_unconfigured(mock_post):
    tg = TelegramConfig()
    send_telegram(tg, "Test")
    mock_post.assert_not_called()


@patch("src.notifier.smtplib.SMTP")
def test_send_email(mock_smtp_class):
    mock_smtp = MagicMock()
    mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_smtp)
    mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)
    email = EmailConfig(
        enabled=True, smtp_host="smtp.test.com", smtp_port=587,
        smtp_user="user", smtp_pass="pass",
        from_addr="from@test.com", to_addr="to@test.com",
    )
    send_email(email, "Subject", "Body")
    mock_smtp.send_message.assert_called_once()


@patch("src.notifier.smtplib.SMTP")
def test_send_email_skips_when_disabled(mock_smtp_class):
    email = EmailConfig(enabled=False)
    send_email(email, "Subject", "Body")
    mock_smtp_class.assert_not_called()
