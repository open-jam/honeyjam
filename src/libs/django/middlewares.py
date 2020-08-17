from django.conf import settings
from django.shortcuts import redirect


def redirect_to_www_domain_middleware(get_response):
    def middleware(request):
        if request.META['HTTP_HOST'] == settings.PARENT_HOST:
            return redirect(f'https://www.{settings.PARENT_HOST}')

        return get_response(request)

    return middleware
