import traceback
from functools import wraps
from typing import Callable, Tuple, Type

from libs.log.logger import logger

_DEFAULT_RETRY_COUNT = 5


class RetryFailException(Exception):
    pass


def retry(
        retry_count: int = _DEFAULT_RETRY_COUNT,
        retriable_exceptions: Tuple[Type[BaseException]] = (BaseException,),
        print_stacktrace: bool = False,
):
    def _decorator(func: Callable):
        def _wrapper(*args, **kwargs):
            stacktraces = []

            for _ in range(0, retry_count):
                try:
                    value = func(*args, **kwargs)
                except Exception as e:
                    if is_retriable_exception(e, retriable_exceptions):
                        stacktraces.append(traceback.format_exc())
                        continue

                    raise e
                else:
                    return value

            if print_stacktrace:
                logger.info('[RetryFail][StackTrace] %s', stacktraces)

            raise RetryFailException

        return wraps(func)(_wrapper)

    return _decorator


def is_retriable_exception(exception: Type[BaseException], retriable_exceptions: Tuple[Type[BaseException]]) -> bool:
    is_class = isinstance(exception, type)

    if is_class:
        return issubclass(exception, retriable_exceptions)

    return isinstance(exception, retriable_exceptions)
