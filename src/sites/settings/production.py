from libs.log.setup import setup_logging

# flake8: noqa: F403
# pylint:disable=wildcard-import, unused-wildcard-import
# noinspection PyUnresolvedReferences
from .base import *

DEBUG = False

setup_logging(DEBUG)

PARENT_HOST = 'honeyjam.dev'
ALLOWED_HOSTS = [
    'honeyjam.dev',
]
STATIC_URL = f'https://cdn.{PARENT_HOST}/static/'
MEDIA_URL = f'https://cdn.{PARENT_HOST}/media/'

# HSTS
SECURE_HSTS_SECONDS = 31536000  # 365 * 24 * 60 * 60
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
