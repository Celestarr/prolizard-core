from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ArticleSearchParamsSerializer
from .services import GoogleScholarService

google_scholar_service = GoogleScholarService()


class ArticleSearchViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=["get"])
    def search(self, request):
        params_serializer = ArticleSearchParamsSerializer(data=request.query_params)
        params_serializer.is_valid(raise_exception=True)

        params = params_serializer.data
        query = params.pop("query")

        res = google_scholar_service.search(query, **params)

        return Response(res)
