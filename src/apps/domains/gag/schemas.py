from drf_yasg import openapi

from apps.domains.gag.serializers import GagQnAAddRequestSerializer
from libs.django.swagger.schemas import BaseSchema


class GagQnAAddSchema(BaseSchema):
    operation_id = 'gag_qna_add'
    operation_description = 'QnA 타입 개그 추가'
    request_body = GagQnAAddRequestSerializer()
    responses = {
        '200': openapi.Response('Ok', ),
        '400': openapi.Response('Bad Request', ),
        '401': openapi.Response('Not Authorized'),
    }
