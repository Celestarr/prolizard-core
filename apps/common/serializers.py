from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Country, Currency, Gender, SupportedLocale, TimeZone


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


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "iso_3166_1_alpha_2_code", "iso_3166_1_alpha_3_code", "name")


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "iso_4217_code", "name", "symbol")


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ("id", "name")


class LocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportedLocale
        fields = ("id", "locale_tag", "name", "native_name")


class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fields = ("id", "name", "offset_display_text", "offset_minutes")
