from rest_framework import serializers

from .services import GoogleScholarService


class ArticleSearchParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1, max_value=10, min_value=1)
    query = serializers.CharField(trim_whitespace=True)
    sorting = serializers.ChoiceField(
        choices=GoogleScholarService.SORTING_CRITERIA, default=GoogleScholarService.SORT_BY_RELEVANCE
    )

    def validate_query(self, value: str):
        # Transform the name to lowercase
        return value.lower()
