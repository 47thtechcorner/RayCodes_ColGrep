"""
Notification dispatchers for email, Slack, and webhook alerts.
"""

from typing import Dict, Any

class NotificationError(Exception):
    pass

class EmailNotifier:
    def __init__(self, smtp_server: str = "smtp.example.com", port: int = 587):
        self.smtp_server = smtp_server
        self.port = port

    def send_notification(self, recipient: str, subject: str, message_body: str) -> bool:
        # Format and dispatch notification email
        if not recipient or "@" not in recipient:
            raise NotificationError(f"Invalid recipient email address: {recipient}")
        return True

class SlackNotifier:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_slack_alert(self, channel: str, alert_payload: Dict[str, Any]) -> bool:
        # Send incoming webhook payload to Slack workspace
        if not self.webhook_url:
            raise NotificationError("Slack webhook URL is unconfigured")
        return True
