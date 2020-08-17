from typing import Dict, List, Optional, Union

from drf_yasg.openapi import Parameter, Response, Schema, SchemaRef
from inflection import camelize
from rest_framework.serializers import Serializer

REQUEST_BODY = Union[Schema, SchemaRef, Serializer]
QUERY_SERIALIZER = Optional[Serializer]
MANUAL_PARAMETERS = List[Parameter]
RESPONSES = Dict[str, Union[Schema, SchemaRef, Response, str, Serializer]]


class BaseSchema:
    request_body: REQUEST_BODY = None
    query_serializer: QUERY_SERIALIZER = None
    manual_parameters: MANUAL_PARAMETERS = None
    responses: RESPONSES = None
    operation_id: str = None
    operation_description: str = None

    @classmethod
    def to_swagger_schema(cls) -> Dict:
        _schema = {'manual_parameters': []}
        if cls.operation_id:
            _schema['operation_id'] = camelize(cls.operation_id, uppercase_first_letter=False)
        if cls.request_body:
            _schema['request_body'] = cls.request_body
        if cls.query_serializer:
            _schema['query_serializer'] = cls.query_serializer
        if cls.manual_parameters:
            _schema['manual_parameters'] = cls.manual_parameters
        if cls.responses:
            _schema['responses'] = cls.responses
        if cls.operation_description:
            _schema['operation_description'] = cls.operation_description
        return _schema
