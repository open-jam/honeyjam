from infras.network.constants.http_status_code import HttpStatusCodes


class StatusCode:
    def __init__(self, status: int, code: str = None):
        self.status = status
        self.code = code

    def has_code(self) -> bool:
        return self.code is not None


class DefaultApiHttpCodes:
    C_100_CONTINUE = StatusCode(HttpStatusCodes.C_100_CONTINUE)
    C_101_SWITCHING_PROTOCOLS = StatusCode(HttpStatusCodes.C_101_SWITCHING_PROTOCOLS)
    C_200_OK = StatusCode(HttpStatusCodes.C_200_OK)
    C_201_CREATED = StatusCode(HttpStatusCodes.C_201_CREATED)
    C_202_ACCEPTED = StatusCode(HttpStatusCodes.C_202_ACCEPTED)
    C_203_NON_AUTHORITATIVE_INFORMATION = StatusCode(HttpStatusCodes.C_203_NON_AUTHORITATIVE_INFORMATION)
    C_204_NO_CONTENT = StatusCode(HttpStatusCodes.C_204_NO_CONTENT)
    C_205_RESET_CONTENT = StatusCode(HttpStatusCodes.C_205_RESET_CONTENT)
    C_206_PARTIAL_CONTENT = StatusCode(HttpStatusCodes.C_206_PARTIAL_CONTENT)
    C_207_MULTI_STATUS = StatusCode(HttpStatusCodes.C_207_MULTI_STATUS)
    C_208_ALREADY_REPORTED = StatusCode(HttpStatusCodes.C_208_ALREADY_REPORTED)
    C_300_MULTIPLE_CHOICES = StatusCode(HttpStatusCodes.C_300_MULTIPLE_CHOICES)
    C_301_MOVED_PERMANENTLY = StatusCode(HttpStatusCodes.C_301_MOVED_PERMANENTLY)
    C_302_FOUND = StatusCode(HttpStatusCodes.C_302_FOUND)
    C_303_SEE_OTHER = StatusCode(HttpStatusCodes.C_303_SEE_OTHER)
    C_304_NOT_MODIFIED = StatusCode(HttpStatusCodes.C_304_NOT_MODIFIED)
    C_305_USE_PROXY = StatusCode(HttpStatusCodes.C_305_USE_PROXY)
    C_306_RESERVED = StatusCode(HttpStatusCodes.C_306_RESERVED)
    C_307_TEMPORARY_REDIRECT = StatusCode(HttpStatusCodes.C_307_TEMPORARY_REDIRECT)
    C_400_BAD_REQUEST = StatusCode(HttpStatusCodes.C_400_BAD_REQUEST)
    C_401_UNAUTHORIZED = StatusCode(HttpStatusCodes.C_401_UNAUTHORIZED)
    C_402_PAYMENT_REQUIRED = StatusCode(HttpStatusCodes.C_402_PAYMENT_REQUIRED)
    C_403_FORBIDDEN = StatusCode(HttpStatusCodes.C_403_FORBIDDEN)
    C_404_NOT_FOUND = StatusCode(HttpStatusCodes.C_404_NOT_FOUND)
    C_405_METHOD_NOT_ALLOWED = StatusCode(HttpStatusCodes.C_405_METHOD_NOT_ALLOWED)
    C_406_NOT_ACCEPTABLE = StatusCode(HttpStatusCodes.C_406_NOT_ACCEPTABLE)
    C_407_PROXY_AUTHENTICATION_REQUIRED = StatusCode(HttpStatusCodes.C_407_PROXY_AUTHENTICATION_REQUIRED)
    C_408_REQUEST_TIMEOUT = StatusCode(HttpStatusCodes.C_408_REQUEST_TIMEOUT)
    C_409_CONFLICT = StatusCode(HttpStatusCodes.C_409_CONFLICT)
    C_410_GONE = StatusCode(HttpStatusCodes.C_410_GONE)
    C_411_LENGTH_REQUIRED = StatusCode(HttpStatusCodes.C_411_LENGTH_REQUIRED)
    C_412_PRECONDITION_FAILED = StatusCode(HttpStatusCodes.C_412_PRECONDITION_FAILED)
    C_413_REQUEST_ENTITY_TOO_LARGE = StatusCode(HttpStatusCodes.C_413_REQUEST_ENTITY_TOO_LARGE)
    C_414_REQUEST_URI_TOO_LONG = StatusCode(HttpStatusCodes.C_414_REQUEST_URI_TOO_LONG)
    C_415_UNSUPPORTED_MEDIA_TYPE = StatusCode(HttpStatusCodes.C_415_UNSUPPORTED_MEDIA_TYPE)
    C_416_REQUESTED_RANGE_NOT_SATISFIABLE = StatusCode(HttpStatusCodes.C_416_REQUESTED_RANGE_NOT_SATISFIABLE)
    C_417_EXPECTATION_FAILED = StatusCode(HttpStatusCodes.C_417_EXPECTATION_FAILED)
    C_422_UNPROCESSABLE_ENTITY = StatusCode(HttpStatusCodes.C_422_UNPROCESSABLE_ENTITY)
    C_423_LOCKED = StatusCode(HttpStatusCodes.C_423_LOCKED)
    C_424_FAILED_DEPENDENCY = StatusCode(HttpStatusCodes.C_424_FAILED_DEPENDENCY)
    C_428_PRECONDITION_REQUIRED = StatusCode(HttpStatusCodes.C_428_PRECONDITION_REQUIRED)
    C_429_TOO_MANY_REQUESTS = StatusCode(HttpStatusCodes.C_429_TOO_MANY_REQUESTS)
    C_431_REQUEST_HEADER_FIELDS_TOO_LARGE = StatusCode(HttpStatusCodes.C_431_REQUEST_HEADER_FIELDS_TOO_LARGE)
    C_451_UNAVAILABLE_FOR_LEGAL_REASONS = StatusCode(HttpStatusCodes.C_451_UNAVAILABLE_FOR_LEGAL_REASONS)
    C_500_INTERNAL_SERVER_ERROR = StatusCode(HttpStatusCodes.C_500_INTERNAL_SERVER_ERROR)
    C_501_NOT_IMPLEMENTED = StatusCode(HttpStatusCodes.C_501_NOT_IMPLEMENTED)
    C_502_BAD_GATEWAY = StatusCode(HttpStatusCodes.C_502_BAD_GATEWAY)
    C_503_SERVICE_UNAVAILABLE = StatusCode(HttpStatusCodes.C_503_SERVICE_UNAVAILABLE)
    C_504_GATEWAY_TIMEOUT = StatusCode(HttpStatusCodes.C_504_GATEWAY_TIMEOUT)
    C_505_HTTP_VERSION_NOT_SUPPORTED = StatusCode(HttpStatusCodes.C_505_HTTP_VERSION_NOT_SUPPORTED)
    C_507_INSUFFICIENT_STORAGE = StatusCode(HttpStatusCodes.C_507_INSUFFICIENT_STORAGE)
    C_511_NETWORK_AUTHENTICATION_REQUIRED = StatusCode(HttpStatusCodes.C_511_NETWORK_AUTHENTICATION_REQUIRED)


class ApiStatusCodes(DefaultApiHttpCodes):
    X_400_DUPLICATE_API = StatusCode(HttpStatusCodes.C_400_BAD_REQUEST, 'DUPLICATE_API_CALL')
