from drf_yasg import openapi

from apps.domains.gag.serializers import GagQnAAddRequestSerializer, GagQnAModifyRequestSerializer, GagResponseSerializer
from libs.django.swagger.schemas import BaseSchema


class GagQnAAddSchema(BaseSchema):
    operation_id = 'gag_qna_add'
    operation_description = 'QnA 타입 개그 추가'
    request_body = GagQnAAddRequestSerializer()
    responses = {
        '200': openapi.Response('Ok', schema=GagResponseSerializer(), ),
        '400': openapi.Response('Bad Request', ),
        '401': openapi.Response('Not Authorized'),
    }


class GagSchema(BaseSchema):
    operation_id = 'gag'
    operation_description = '개그'
    responses = {
        '200': openapi.Response('Ok', ),
        '401': openapi.Response('Not Authorized'),
    }


class GagQnAModifySchema(BaseSchema):
    operation_id = 'gag_qna_modify'
    operation_description = '개그 수정'
    request_body = GagQnAModifyRequestSerializer()
    responses = {
        '200': openapi.Response('Ok', ),
        '400': openapi.Response('Bad Request', ),
        '401': openapi.Response('Not Authorized'),
        '403': openapi.Response('Forbidden'),
    }


class GagQnADeleteSchema(BaseSchema):
    operation_id = 'gag_qna_delete'
    operation_description = '개그 제거'
    responses = {
        '200': openapi.Response('Ok', ),
        '401': openapi.Response('Not Authorized'),
        '403': openapi.Response('Forbidden'),
    }
