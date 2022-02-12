from rest_framework import serializers

from apps.core.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "iso_3166_1_alpha_2_code", "iso_3166_1_alpha_3_code", "name")
