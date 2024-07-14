from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from app.apps.profile.models import ResumeTemplate
from app.apps.profile.serializers import ResumeTemplateSerializer
from app.utils.views.pagination import PageNumberPaginationFull
from app.utils.views.viewsets import ListOnlyModelViewSet

from .models import Country, SupportedLocale, TimeZone
from .serializers import CountrySerializer, LocaleSerializer, TimeZoneSerializer


@extend_schema(exclude=True)
class NotFoundView(ListAPIView):
    def get(self, request, *args, **kwargs):
        del request, args, kwargs
        raise NotFound(detail=_("Requested resource does not exist."))


class CountryViewSet(ListOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPaginationFull


class LocaleViewSet(ListOnlyModelViewSet):
    queryset = SupportedLocale.objects.all()
    serializer_class = LocaleSerializer
    pagination_class = PageNumberPaginationFull


class TimeZoneViewSet(ListOnlyModelViewSet):
    queryset = TimeZone.objects.all()
    serializer_class = TimeZoneSerializer
    pagination_class = PageNumberPaginationFull


class ResumeTemplateViewSet(ListOnlyModelViewSet):
    queryset = ResumeTemplate.objects.all()
    serializer_class = ResumeTemplateSerializer
    pagination_class = PageNumberPaginationFull
