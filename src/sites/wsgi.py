import os

from django.core.wsgi import get_wsgi_application
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

from infras.secrets.constants import SecretKey
from libs.secrets.secrets import Secrets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'sites.settings.{Secrets.get(SecretKey.ENVIRONMENT)}')

application = SentryWsgiMiddleware(get_wsgi_application())
