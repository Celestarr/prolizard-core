from rest_framework import serializers

from apps.core.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "iso_4217_code", "name", "symbol")


__all__ = ["CurrencySerializer"]
