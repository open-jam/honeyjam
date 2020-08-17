from rest_framework import serializers

from libs.django.serializers import BaseSerializer


class GagQnAAddRequestSerializer(BaseSerializer):
    question = serializers.CharField(required=True, label='문')
    answer = serializers.CharField(required=True, label='답')
