from libs.base.exceptions import ErrorException


class UseReservedWordException(ErrorException):
    # '데이터 필드명 중 예약어가 포함되어 있습니다.'
    pass
