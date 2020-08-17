from typing import Dict, List

from django.conf import settings
from slacker import Slacker


def slack_notify(channel: str, text: str = None, username: str = 'ghost', attachments: List[Dict] = None):
    if not settings.SLACK_API_KEY:
        return

    Slacker(settings.SLACK_API_KEY).chat.post_message(
        channel=channel, text=text, username=username, attachments=attachments, icon_emoji=':ghost:'
    )
