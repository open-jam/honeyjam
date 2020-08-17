from django.http import JsonResponse


# HTTP Error 400
def bad_request(request, exception):
    context = {
        'message': exception
    }

    response = JsonResponse(context)
    response.status_code = 400
    return response


# HTTP Error 403
def permission_denied(request, exception):
    response = JsonResponse({'message': 'Permission denied.'})
    response.status_code = 403
    return response


# HTTP Error 404
def page_not_found(request, exception):
    response = JsonResponse({'message': 'Not found.'})
    response.status_code = 404
    return response


# HTTP Error 500
def server_error(request):
    response = JsonResponse({'message': 'Internal server error.'})
    response.status_code = 500
    return response
