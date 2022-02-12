from rest_framework import serializers

from apps.core.models.confirmation_key import ConfirmationKey


class ConfirmationKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationKey
        exclude = ()
