from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "iso_4217_code", "name", "symbol")


__all__ = ["CurrencySerializer"]
