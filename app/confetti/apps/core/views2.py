from common.models import (
    Country,
    EmploymentType,
    Gender,
    LanguageProficiencyLevel,
    PortfolioTemplate,
    ResumeTemplate,
    SkillProficiencyLevel,
)
from common.serializers import (
    CountrySerializer,
    EmploymentTypeSerializer,
    GenderSerializer,
    LanguageProficiencyLevelSerializer,
    PortfolioTemplateSerializer,
    ResumeTemplateSerializer,
    SkillProficiencyLevelSerializer,
)
from common.viewsets import MflModelViewSet


class ChoiceViewSet(MflModelViewSet):
    pass


class CountryViewSet(ChoiceViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class EmploymentTypeViewSet(ChoiceViewSet):
    serializer_class = EmploymentTypeSerializer
    queryset = EmploymentType.objects.all()


class GenderViewSet(ChoiceViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class LanguageProficiencyLevelViewSet(ChoiceViewSet):
    serializer_class = LanguageProficiencyLevelSerializer
    queryset = LanguageProficiencyLevel.objects.all()


class SkillProficiencyLevelViewSet(ChoiceViewSet):
    serializer_class = SkillProficiencyLevelSerializer
    queryset = SkillProficiencyLevel.objects.all()


class PortfolioTemplateViewSet(ChoiceViewSet):
    serializer_class = PortfolioTemplateSerializer
    queryset = PortfolioTemplate.objects.all()


class ResumeTemplateViewSet(ChoiceViewSet):
    serializer_class = ResumeTemplateSerializer
    queryset = ResumeTemplate.objects.all()
