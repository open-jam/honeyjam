from rest_framework import serializers

from apps.domains.gag.models import Gag
from libs.django.serializers import BaseModelSerializer, BaseSerializer


class GagQnAAddRequestSerializer(BaseSerializer):
    question = serializers.CharField(required=True, label='문')
    answer = serializers.CharField(required=True, label='답')


class GagSerializer(BaseModelSerializer):
    class Meta:
        model = Gag
        fields = (
            'id', 'gag_type', 'user_id', 'question', 'answer', 'is_active', 'create_time', 'update_time',
        )


class GagResponseSerializer(BaseSerializer):
    gag = GagSerializer(label='gag')


class GagQnAModifyRequestSerializer(BaseSerializer):
    question = serializers.CharField(required=True, label='문')
    answer = serializers.CharField(required=True, label='답')
