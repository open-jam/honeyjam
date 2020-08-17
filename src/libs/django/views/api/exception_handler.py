from rest_framework.views import exception_handler as rest_exception_handler


def exception_handler(exc, context):
    response = rest_exception_handler(exc, context)

    if response is None:
        return response

    if 'status_code' in response.data:
        del response.data['status_code']

    if 'detail' in response.data:
        message = response.data['detail']
        del response.data['detail']
        response.data['message'] = message

    return response
