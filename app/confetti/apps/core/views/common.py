from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from confetti.apps.core.models import Country, Gender, Language, Locale, TimeZone
from confetti.apps.core.serializers import (
    CountrySerializer,
    GenderSerializer,
    LanguageSerializer,
    LocaleSerializer,
    TimeZoneSerializer,
)
from confetti.apps.core.viewsets import ModelViewSet
from confetti.apps.member.models import EmploymentType, LanguageProficiencyLevel, SkillProficiencyLevel, ResumeTemplate
from confetti.apps.member.serializers import (
    EmploymentTypeSerializer,
    LanguageProficiencyLevelSerializer,
    SkillProficiencyLevelSerializer,
    ResumeTemplateSerializer
)


@extend_schema(exclude=True)
class NotFoundView(ListAPIView):
    def get(self, request, *args, **kwargs):
        del request, args, kwargs
        raise NotFound(detail=_("Requested resource does not exist."))


class MetadataViewSet(ModelViewSet):
    permission_classes_by_action = {}
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "head", "options"]

    def list(self, request, *args, **kwargs):
        del request, args, kwargs

        countries = CountrySerializer(Country.objects.all(), many=True).data
        locales = LocaleSerializer(Locale.objects.all(), many=True).data
        time_zones = TimeZoneSerializer(TimeZone.objects.all(), many=True).data
        genders = GenderSerializer(Gender.objects.all(), many=True).data
        employment_types = EmploymentTypeSerializer(EmploymentType.objects.all(), many=True).data
        language_proficiency_levels = LanguageProficiencyLevelSerializer(
            LanguageProficiencyLevel.objects.all(), many=True
        ).data
        skill_proficiency_levels = SkillProficiencyLevelSerializer(SkillProficiencyLevel.objects.all(), many=True).data
        resume_templates = ResumeTemplateSerializer(ResumeTemplate.objects.all(), many=True).data

        return Response(
            {
                "countries": countries,
                "locales": locales,
                "time_zones": time_zones,
                "genders": genders,
                "employment_types": employment_types,
                "language_proficiency_levels": language_proficiency_levels,
                "resume_templates": resume_templates,
                "skill_proficiency_levels": skill_proficiency_levels,
            }
        )


__all__ = ["MetadataViewSet", "NotFoundView"]
