from rest_framework import serializers

from apps.core.models import SupportedLocale


class LocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportedLocale
        fields = ("id", "locale_tag", "name", "native_name")
