from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models.confirmation_key import ConfirmationKey


class ConfirmationKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationKey
        exclude = ()
