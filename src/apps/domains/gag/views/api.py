from django.shortcuts import redirect, render
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema

from apps.domains.gag import schemas
from apps.domains.gag.repositories import GagRepository
from apps.domains.gag.serializers import GagQnAAddRequestSerializer
from apps.domains.gag.services.gag_create_service import GagCreateService
from infras.network.constants.api_status_code import ApiStatusCodes
from libs.django.views.api.views import BaseApiView, LoginRequiredMixin


class GagAddView(LoginRequiredMixin, BaseApiView):
    @swagger_auto_schema(**schemas.GagQnAAddSchema.to_swagger_schema())
    def post(self, request):
        serializer = GagQnAAddRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_400_BAD_REQUEST), data=serializer.errors)

        GagCreateService.create_qna(request.user, serializer.validated_data['question'], serializer.validated_data['answer'])

        return self.success_response()


class GagView(LoginRequiredMixin, BaseApiView):
    def get(self, request, gag_id: int):
        gag = GagRepository.get_active_by_id(gag_id)
        return self.success_response()

    def put(self, request, gag_id: int):
        gag = GagRepository.get_active_by_id(gag_id)
        if request.user.id != gag.user_id:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_403_FORBIDDEN), )

        return self.success_response()

    def delete(self, request, gag_id: int):
        gag = GagRepository.get_active_by_id(gag_id)
        if request.user.id != gag.user_id:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_403_FORBIDDEN), )

        gag.is_active = False
        gag.save()

        return self.success_response()
