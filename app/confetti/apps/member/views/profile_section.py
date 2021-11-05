from confetti.apps.member.models import (
    AcademicRecord,
    Certification,
    HonorOrAward,
    Language,
    Project,
    Publication,
    Skill,
    WebLink,
    WorkExperience,
)
from confetti.apps.member.serializers import (
    AcademicRecordSerializer,
    CertificationSerializer,
    HonorOrAwardSerializer,
    LanguageSerializer,
    LanguageWriteOnlySerializer,
    ProjectSerializer,
    PublicationSerializer,
    SkillSerializer,
    SkillWriteOnlySerializer,
    WebLinkSerializer,
    WorkExperienceSerializer,
    WorkExperienceWriteOnlySerializer,
)
from confetti.apps.member.viewsets import ProfileSectionViewSet


class AcademicRecordViewSet(ProfileSectionViewSet):
    serializer_class = AcademicRecordSerializer
    queryset = AcademicRecord.objects.all()


class SkillViewSet(ProfileSectionViewSet):
    serializer_class = SkillSerializer
    write_only_serializer_class = SkillWriteOnlySerializer
    queryset = Skill.objects.all()


class WebLinkViewSet(ProfileSectionViewSet):
    serializer_class = WebLinkSerializer
    queryset = WebLink.objects.all()


class WorkExperienceViewSet(ProfileSectionViewSet):
    serializer_class = WorkExperienceSerializer
    write_only_serializer_class = WorkExperienceWriteOnlySerializer
    queryset = WorkExperience.objects.all()


class LanguageViewSet(ProfileSectionViewSet):
    serializer_class = LanguageSerializer
    write_only_serializer_class = LanguageWriteOnlySerializer
    queryset = Language.objects.all()


class ProjectViewSet(ProfileSectionViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class PublicationViewSet(ProfileSectionViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()


class HonorOrAwardViewSet(ProfileSectionViewSet):
    serializer_class = HonorOrAwardSerializer
    queryset = HonorOrAward.objects.all()


class CertificationViewSet(ProfileSectionViewSet):
    serializer_class = CertificationSerializer
    queryset = Certification.objects.all()


__all__ = [
    "AcademicRecordViewSet",
    "SkillViewSet",
    "WebLinkViewSet",
    "WorkExperienceViewSet",
    "LanguageViewSet",
    "ProjectViewSet",
    "PublicationViewSet",
    "HonorOrAwardViewSet",
    "CertificationViewSet",
]
