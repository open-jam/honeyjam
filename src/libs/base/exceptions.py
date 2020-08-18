class RootException(Exception):
    __slots__ = ['_msg', ]

    def __init__(self, msg: str = ''):
        super().__init__()
        self._msg = msg

    def __str__(self) -> str:
        return self._msg


class ErrorException(RootException):
    pass


class NotAllowedAccessException(ErrorException):
    pass
