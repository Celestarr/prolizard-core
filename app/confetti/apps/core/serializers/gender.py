from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ("id", "name")
