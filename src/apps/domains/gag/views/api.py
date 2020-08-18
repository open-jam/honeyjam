from drf_yasg.utils import swagger_auto_schema

from apps.domains.gag import schemas
from apps.domains.gag.repositories import GagRepository
from apps.domains.gag.serializers import GagQnAAddRequestSerializer, GagQnAModifyRequestSerializer, GagResponseSerializer
from apps.domains.gag.services.gag_service import GagService
from infras.network.constants.api_status_code import ApiStatusCodes
from libs.base.exceptions import NotAllowedAccessException
from libs.django.views.api.views import BaseApiView, LoginRequiredMixin


class GagAddView(LoginRequiredMixin, BaseApiView):
    @swagger_auto_schema(**schemas.GagQnAAddSchema.to_swagger_schema())
    def post(self, request):
        serializer = GagQnAAddRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_400_BAD_REQUEST), data=serializer.errors)

        GagService.create_qna(request.user, serializer.validated_data['question'], serializer.validated_data['answer'])

        return self.success_response()


class GagView(BaseApiView):
    @swagger_auto_schema(**schemas.GagSchema.to_swagger_schema())
    def get(self, request, gag_id: int):
        gag = GagRepository.get_active_by_id(gag_id)
        return self.success_response(data=GagResponseSerializer(gag).data)

    @swagger_auto_schema(**schemas.GagQnAModifySchema.to_swagger_schema())
    def put(self, request, gag_id: int):
        if request.user.is_anonymous:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_401_UNAUTHORIZED), )

        serializer = GagQnAModifyRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_400_BAD_REQUEST), data=serializer.errors)

        try:
            GagService.modify_qna(request.user, gag_id, serializer.validated_data['question'], serializer.validated_data['answer'])

        except NotAllowedAccessException:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_403_FORBIDDEN), )

        return self.success_response()

    @swagger_auto_schema(**schemas.GagQnADeleteSchema.to_swagger_schema())
    def delete(self, request, gag_id: int):
        if request.user.is_anonymous:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_401_UNAUTHORIZED), )

        try:
            GagService.delete_qna(request.user, gag_id)

        except NotAllowedAccessException:
            return self.fail_response(response_code=self.make_response_code(ApiStatusCodes.C_403_FORBIDDEN), )

        return self.success_response()
