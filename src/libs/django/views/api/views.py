from django.http import JsonResponse
from rest_framework.views import APIView

from libs.django.views.api.mixins import ResponseMixin


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse(data={}, status=401)
        return super().dispatch(request, *args, **kwargs)


class BaseApiView(ResponseMixin, APIView):
    pass
