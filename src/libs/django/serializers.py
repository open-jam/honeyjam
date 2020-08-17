from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class BaseModelSerializer(ModelSerializer):
    pass
