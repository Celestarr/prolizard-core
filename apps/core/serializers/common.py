from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ErrorSerializer(BaseSerializer):
    message = serializers.CharField(
        label=_("error message"),
        read_only=True,
    )


class GenericSuccessSerializer(BaseSerializer):
    message = serializers.CharField(
        label=_("success message"),
        read_only=True,
    )
