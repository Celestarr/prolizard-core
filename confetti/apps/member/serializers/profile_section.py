from rest_framework import serializers

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

from .employment_type import EmploymentTypeSerializer
from .proficiency_level import LanguageProficiencyLevelSerializer, SkillProficiencyLevelSerializer


class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = (
            "created_at",
            "updated_at",
        )
        model = AcademicRecord
        extra_kwargs = {
            "user": {"write_only": True},
        }


class AcademicRecordSerializerForResumeTemplate(AcademicRecordSerializer):
    date_line = serializers.SerializerMethodField()
    degree_line = serializers.SerializerMethodField()

    class Meta(AcademicRecordSerializer.Meta):
        pass

    def get_date_line(self, obj: AcademicRecord):
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return "{} - {}".format(start_line, end_line)

    def get_degree_line(self, obj: AcademicRecord):
        if obj.degree and obj.field_of_study:
            return "{}, {}".format(obj.degree, obj.field_of_study)

        if obj.degree:
            return obj.degree

        if obj.field_of_study:
            return obj.field_of_study


class SkillSerializer(serializers.ModelSerializer):
    proficiency = SkillProficiencyLevelSerializer()

    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Skill
        extra_kwargs = {
            "user": {"write_only": True},
        }


class SkillWriteOnlySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Skill
        extra_kwargs = {
            "user": {"write_only": True},
        }


class WebLinkSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = WebLink
        extra_kwargs = {
            "user": {"write_only": True},
        }


class WebLinkSerializerForResumeTemplate(WebLinkSerializer):
    icon_class = serializers.SerializerMethodField()

    class Meta(WebLinkSerializer.Meta):
        pass

    def get_icon_class(self, obj: WebLink):
        if "github.com" in obj.href:
            return "fab fa-github-alt"

        if "linkedin.com" in obj.href:
            return "fab fa-linkedin-in"

        return "fas fa-globe"


class WorkExperienceSerializer(serializers.ModelSerializer):
    employment_type = EmploymentTypeSerializer()

    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = WorkExperience
        extra_kwargs = {
            "user": {"write_only": True},
        }


class WorkExperienceWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(WorkExperienceSerializer.Meta):
        pass


class WorkExperienceSerializerForResumeTemplate(WorkExperienceSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(WorkExperienceSerializer.Meta):
        pass

    def get_date_line(self, obj: WorkExperience):
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return "{} - {}".format(start_line, end_line)


class LanguageSerializer(serializers.ModelSerializer):
    proficiency = LanguageProficiencyLevelSerializer()

    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Language
        extra_kwargs = {
            "user": {"write_only": True},
        }


class LanguageWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(LanguageSerializer.Meta):
        pass


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Project
        extra_kwargs = {
            "user": {"write_only": True},
        }


class ProjectSerializerForResumeTemplate(ProjectSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(ProjectSerializer.Meta):
        pass

    def get_date_line(self, obj: Project):
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return "{} - {}".format(start_line, end_line)


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Publication
        extra_kwargs = {
            "user": {"write_only": True},
        }


class PublicationSerializerForResumeTemplate(PublicationSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(PublicationSerializer.Meta):
        pass

    def get_date_line(self, obj: Publication):
        if obj.publication_date:
            return obj.publication_date.strftime("%b %Y")


class HonorOrAwardSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = HonorOrAward
        extra_kwargs = {
            "user": {"write_only": True},
        }


class HonorOrAwardSerializerForResumeTemplate(HonorOrAwardSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(HonorOrAwardSerializer.Meta):
        pass

    def get_date_line(self, obj: HonorOrAward):
        if obj.issue_date:
            return obj.issue_date.strftime("%b %Y")


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Certification
        extra_kwargs = {
            "user": {"write_only": True},
        }


class CertificationSerializerForResumeTemplate(CertificationSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(CertificationSerializer.Meta):
        pass

    def get_date_line(self, obj: Certification):
        if obj.issue_date:
            return obj.issue_date.strftime("%b %Y")


__all__ = [
    "AcademicRecordSerializer",
    "SkillSerializer",
    "SkillWriteOnlySerializer",
    "WebLinkSerializer",
    "WorkExperienceSerializer",
    "WorkExperienceWriteOnlySerializer",
    "LanguageSerializer",
    "LanguageWriteOnlySerializer",
    "ProjectSerializer",
    "PublicationSerializer",
    "HonorOrAwardSerializer",
    "CertificationSerializer",
    "ProjectSerializerForResumeTemplate",
    "PublicationSerializerForResumeTemplate",
    "HonorOrAwardSerializerForResumeTemplate",
    "CertificationSerializerForResumeTemplate",
    "AcademicRecordSerializerForResumeTemplate",
    "WorkExperienceSerializerForResumeTemplate",
    "WebLinkSerializerForResumeTemplate",
]
