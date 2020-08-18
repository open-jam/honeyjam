from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response


def handler400(request, *args, **kawgs):
    response = render_to_response('error.html', {
        'title': '잘못된 요청입니다.',
        'status_code': 400,
    })
    response.status_code = 400
    return response


def handler403(request, *args, **kawgs):
    response = render_to_response('error.html', {
        'title': '접근할 수 없습니다.',
        'status_code': 403,
    })
    response.status_code = 403
    return response


def handler404(request, *args, **kawgs):
    response = render_to_response('error.html', {
        'title': '페이지를 찾을 수 없습니다.',
        'status_code': 404,
    })
    response.status_code = 404
    return response


def handler500(request, *args, **kawgs):
    response = render_to_response('error.html', {
        'title': 'Internal Server Error',
        'status_code': 500,
        'message': '서버에 접속할수 없습니다. 잠시후 다시 시도해주세요.',
    })
    response.status_code = 500
    return response


def get_csrf_token(request):
    return JsonResponse({'csrf_token': get_token(request)})
