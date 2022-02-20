from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from apps.profile.models import EmploymentType, LanguageProficiencyLevel, ResumeTemplate, SkillProficiencyLevel
from apps.profile.serializers import (
    EmploymentTypeSerializer,
    LanguageProficiencyLevelSerializer,
    ResumeTemplateSerializer,
    SkillProficiencyLevelSerializer,
)

from .models import Country, Gender, SupportedLocale, TimeZone
from .serializers import CountrySerializer, GenderSerializer, LocaleSerializer, TimeZoneSerializer
from .viewsets import ModelViewSet


@extend_schema(exclude=True)
class NotFoundView(ListAPIView):
    def get(self, request, *args, **kwargs):
        del request, args, kwargs
        raise NotFound(detail=_("Requested resource does not exist."))


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class GenderViewSet(ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class LocaleViewSet(ModelViewSet):
    queryset = SupportedLocale.objects.all()
    serializer_class = LocaleSerializer


class TimeZoneViewSet(ModelViewSet):
    queryset = TimeZone.objects.all()
    serializer_class = TimeZoneSerializer


class EmploymentTypeViewSet(ModelViewSet):
    queryset = EmploymentType.objects.all()
    serializer_class = EmploymentTypeSerializer


class SkillProficiencyLevelViewSet(ModelViewSet):
    queryset = SkillProficiencyLevel.objects.all()
    serializer_class = SkillProficiencyLevelSerializer


class ResumeTemplateViewSet(ModelViewSet):
    queryset = ResumeTemplate.objects.all()
    serializer_class = ResumeTemplateSerializer


class LanguageProficiencyLevelViewSet(ModelViewSet):
    queryset = LanguageProficiencyLevel.objects.all()
    serializer_class = LanguageProficiencyLevelSerializer
