from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models import TimeZone


class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = ("id", "name", "offset_display_text", "offset_minutes")
