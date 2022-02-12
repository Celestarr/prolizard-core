from rest_framework import serializers

from apps.core.models import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ("id", "name")
