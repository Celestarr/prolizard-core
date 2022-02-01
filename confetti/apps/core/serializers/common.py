from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(
        label=_("error message"),
        read_only=True,
    )


class GenericSuccessSerializer(serializers.Serializer):
    message = serializers.CharField(
        label=_("success message"),
        read_only=True,
    )
