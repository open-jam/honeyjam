import logging.config
import sys

from libs.log.constants import LogLevel


def setup_logging(debug: bool = False) -> None:
    log_level = LogLevel.DEBUG if debug else LogLevel.INFO
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
                'datefmt': '%Y-%b-%d %H:%M:%S',
            },
        },
        'handlers': {
            'stream': {
                'level': log_level,
                'class': 'logging.StreamHandler',
                'stream': sys.stderr,
                'formatter': 'default'
            },
        },
        'loggers': {
            '': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'common': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'django': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'django.request': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'django.template': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
        },
    })
