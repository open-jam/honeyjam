from django.utils.http import http_date
from rest_framework.response import Response

from infras.network.constants.api_status_code import ApiStatusCodes, StatusCode
from libs.django.views.api.dto import LastModified, ResponseCode
from libs.django.views.api.exceptions import UseReservedWordException


class ResponseMixin:

    @classmethod
    def success_response(cls, data=None, response_code: ResponseCode = None, last_modified: LastModified = None) -> Response:
        if response_code is None:
            response_code = ResponseCode(ApiStatusCodes.C_200_OK)
        return cls._make_response(response_code, data=data, last_modified=last_modified)

    @classmethod
    def fail_response(cls, response_code: ResponseCode, data=None) -> Response:
        return cls._make_response(response_code, data=data)

    @staticmethod
    def make_response_code(status_code: StatusCode, message: str = None) -> ResponseCode:
        return ResponseCode(status_code, message)

    @staticmethod
    def make_last_modified(last_modified: int = None, e_tag: str = None) -> LastModified:
        return LastModified(last_modified, e_tag)

    @staticmethod
    def _make_response(response_code: ResponseCode, data=None, last_modified: LastModified = None) -> Response:
        if data is None:
            data = {}

        if 'message' in data or 'code' in data:
            raise UseReservedWordException()

        if response_code.has_message():
            data['message'] = response_code.get_message()
        if response_code.has_code():
            data['code'] = response_code.get_code()

        headers = {}
        if last_modified is None:
            last_modified = LastModified()
        if last_modified.last_modified is not None:
            headers['Last-Modified'] = http_date(last_modified)
        if last_modified.e_tag is not None:
            headers['ETag'] = '"{}"'.format(last_modified.e_tag)

        return Response(data, status=response_code.get_status(), headers=headers)
