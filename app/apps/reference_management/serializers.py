from rest_framework import serializers

from .services import GoogleScholarService


class ArticleSearchParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1, max_value=100, min_value=1)
    query = serializers.CharField(trim_whitespace=True)
    sorting = serializers.ChoiceField(
        choices=GoogleScholarService.SORTING_CRITERIA, default=GoogleScholarService.SORT_BY_RELEVANCE
    )
    year_max = serializers.IntegerField(allow_null=True, min_value=1900, max_value=2050)
    year_min = serializers.IntegerField(allow_null=True, min_value=1900, max_value=2050)

    def validate_query(self, value: str):
        # Transform the name to lowercase
        return value.lower()

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)
