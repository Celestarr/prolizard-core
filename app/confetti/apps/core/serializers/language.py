from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models import Language, Locale


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "iso_639_1_code", "iso_639_2_code", "name", "native_name")


class LocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locale
        fields = ("id", "locale_tag", "name")
