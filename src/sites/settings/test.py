
# flake8: noqa: F403
# pylint:disable=wildcard-import, unused-wildcard-import
# noinspection PyUnresolvedReferences
from .base import *

DATABASE_ROUTERS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_PATH, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
