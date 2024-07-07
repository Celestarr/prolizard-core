from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from app.apps.profile.models import EmploymentType, LanguageProficiencyLevel, ResumeTemplate, SkillProficiencyLevel
from app.apps.profile.serializers import (
    EmploymentTypeSerializer,
    LanguageProficiencyLevelSerializer,
    ResumeTemplateSerializer,
    SkillProficiencyLevelSerializer,
)
from app.utils.views.pagination import PageNumberPaginationFull
from app.utils.views.viewsets import ListOnlyModelViewSet

from .models import Country, Gender, SupportedLocale, TimeZone
from .serializers import CountrySerializer, GenderSerializer, LocaleSerializer, TimeZoneSerializer


@extend_schema(exclude=True)
class NotFoundView(ListAPIView):
    def get(self, request, *args, **kwargs):
        del request, args, kwargs
        raise NotFound(detail=_("Requested resource does not exist."))


class CountryViewSet(ListOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPaginationFull


class GenderViewSet(ListOnlyModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    pagination_class = PageNumberPaginationFull


class LocaleViewSet(ListOnlyModelViewSet):
    queryset = SupportedLocale.objects.all()
    serializer_class = LocaleSerializer
    pagination_class = PageNumberPaginationFull


class TimeZoneViewSet(ListOnlyModelViewSet):
    queryset = TimeZone.objects.all()
    serializer_class = TimeZoneSerializer
    pagination_class = PageNumberPaginationFull


class EmploymentTypeViewSet(ListOnlyModelViewSet):
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer
    pagination_class = PageNumberPaginationFull


class SkillProficiencyLevelViewSet(ListOnlyModelViewSet):
    queryset = SkillProficiencyLevel.objects.all()
    serializer_class = SkillProficiencyLevelSerializer
    pagination_class = PageNumberPaginationFull


class ResumeTemplateViewSet(ListOnlyModelViewSet):
    queryset = ResumeTemplate.objects.all()
    serializer_class = ResumeTemplateSerializer
    pagination_class = PageNumberPaginationFull


class LanguageProficiencyLevelViewSet(ListOnlyModelViewSet):
    queryset = LanguageProficiencyLevel.objects.all()
    serializer_class = LanguageProficiencyLevelSerializer
    pagination_class = PageNumberPaginationFull
