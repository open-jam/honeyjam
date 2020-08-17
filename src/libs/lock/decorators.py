from datetime import datetime, timedelta

from filelock import FileLock, Timeout

from libs.log.logger import logger


def f_lock(key_prefix: str, lock_ttl: int = 600, lock_waiting_timeout: int = 0):
    def _decorator(_func):
        def _wrapped_view(request, *args, **kwargs):
            key = f'{key_prefix}.lock'
            _lock = FileLock(key, timeout=lock_ttl)
            start = datetime.now()

            try:
                _lock.acquire(timeout=lock_waiting_timeout)

            except Timeout:
                return None

            try:
                return _func(request, *args, **kwargs)

            finally:
                _lock.release()
                end = datetime.now()
                time_taken = end - start

                if time_taken > timedelta(seconds=lock_ttl):
                    logger.error('[LOCK] %s is over lock ttl. - %s sec.', key, time_taken)

                elif time_taken > timedelta(seconds=lock_ttl * 0.5):
                    logger.error('[LOCK] Be careful! %s is over lock ttl margin. - %s} sec.', key, time_taken)

        return _wrapped_view

    return _decorator
