from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models import SupportedLocale


class LocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportedLocale
        fields = ("id", "locale_tag", "name", "native_name")
