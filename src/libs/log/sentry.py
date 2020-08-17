from django.conf import settings


def before_send(event, hint):
    if 'exc_info' in hint:
        _, exc_value, _ = hint['exc_info']

        sentry_ignore_errors = getattr(settings, 'SENTRY_IGNORE_ERRORS', None)
        if sentry_ignore_errors and isinstance(exc_value, sentry_ignore_errors):
            return None

    return event
