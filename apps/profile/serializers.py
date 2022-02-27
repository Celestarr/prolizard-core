from typing import Optional

from rest_framework import serializers

from apps.identity.models import User
from apps.identity.serializers import UserSerializer

from .models import (
    AcademicRecord,
    Certification,
    EmploymentType,
    HonorOrAward,
    Language,
    LanguageProficiencyLevel,
    PortfolioTemplate,
    Project,
    Publication,
    ResumeTemplate,
    Skill,
    SkillProficiencyLevel,
    UserPreference,
    WebLink,
    WorkExperience,
)


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = EmploymentType


class PortfolioTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = PortfolioTemplate


class ResumeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = ResumeTemplate


class UserPreferenceSerializer(serializers.ModelSerializer):
    portfolio_template = PortfolioTemplateSerializer()
    resume_template = ResumeTemplateSerializer()

    class Meta:
        exclude = [
            "created_at",
            "id",
            "updated_at",
            "user",
        ]
        model = UserPreference


class UserPreferenceWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(UserPreferenceSerializer.Meta):
        pass


class SkillProficiencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = SkillProficiencyLevel


class LanguageProficiencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = LanguageProficiencyLevel


class AcademicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = AcademicRecord
        extra_kwargs = {
            "user": {"write_only": True},
        }


class AcademicRecordSerializerForResumeTemplate(AcademicRecordSerializer):
    date_line = serializers.SerializerMethodField()
    degree_line = serializers.SerializerMethodField()

    class Meta(AcademicRecordSerializer.Meta):
        pass

    def get_date_line(self, obj: AcademicRecord):  # pylint: disable=no-self-use
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return f"{start_line} - {end_line}"

    def get_degree_line(self, obj: AcademicRecord):  # pylint: disable=no-self-use
        if obj.degree and obj.field_of_study:
            return f"{obj.degree}, {obj.field_of_study}"

        if obj.degree:
            return obj.degree

        if obj.field_of_study:
            return obj.field_of_study

        return None


class SkillSerializer(serializers.ModelSerializer):
    proficiency = SkillProficiencyLevelSerializer()

    class Meta:
        exclude = ("created_at", "updated_at")
        model = Skill
        extra_kwargs = {
            "user": {"write_only": True},
        }


class SkillWriteOnlySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = Skill
        extra_kwargs = {
            "user": {"write_only": True},
        }


class WebLinkSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = WebLink
        extra_kwargs = {
            "user": {"write_only": True},
        }


class WebLinkSerializerForResumeTemplate(WebLinkSerializer):
    icon_class = serializers.SerializerMethodField()

    class Meta(WebLinkSerializer.Meta):
        pass

    def get_icon_class(self, obj: WebLink):  # pylint: disable=no-self-use
        if "github.com" in obj.href:
            return "fab fa-github-alt"

        if "linkedin.com" in obj.href:
            return "fab fa-linkedin-in"

        return "fas fa-globe"


class WorkExperienceSerializer(serializers.ModelSerializer):
    employment_type = EmploymentTypeSerializer()

    class Meta:
        exclude = ("created_at", "updated_at")
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

    def get_date_line(self, obj: WorkExperience):  # pylint: disable=no-self-use
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return f"{start_line} - {end_line}"


class LanguageSerializer(serializers.ModelSerializer):
    proficiency = LanguageProficiencyLevelSerializer()

    class Meta:
        exclude = ("created_at", "updated_at")
        model = Language
        extra_kwargs = {
            "user": {"write_only": True},
        }


class LanguageWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(LanguageSerializer.Meta):
        pass


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = Project
        extra_kwargs = {
            "user": {"write_only": True},
        }


class ProjectSerializerForResumeTemplate(ProjectSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(ProjectSerializer.Meta):
        pass

    def get_date_line(self, obj: Project):  # pylint: disable=no-self-use
        start_line = obj.start_date.strftime("%b %Y")
        end_line = "Present" if obj.is_ongoing else obj.end_date.strftime("%b %Y")

        return f"{start_line} - {end_line}"


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = Publication
        extra_kwargs = {
            "user": {"write_only": True},
        }


class PublicationSerializerForResumeTemplate(PublicationSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(PublicationSerializer.Meta):
        pass

    def get_date_line(self, obj: Publication):  # pylint: disable=no-self-use
        if obj.publication_date:
            return obj.publication_date.strftime("%b %Y")

        return None


class HonorOrAwardSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = HonorOrAward
        extra_kwargs = {
            "user": {"write_only": True},
        }


class HonorOrAwardSerializerForResumeTemplate(HonorOrAwardSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(HonorOrAwardSerializer.Meta):
        pass

    def get_date_line(self, obj: HonorOrAward):  # pylint: disable=no-self-use
        if obj.issue_date:
            return obj.issue_date.strftime("%b %Y")

        return None


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = Certification
        extra_kwargs = {
            "user": {"write_only": True},
        }


class CertificationSerializerForResumeTemplate(CertificationSerializer):
    date_line = serializers.SerializerMethodField()

    class Meta(CertificationSerializer.Meta):
        pass

    def get_date_line(self, obj: Certification):  # pylint: disable=no-self-use
        if obj.issue_date:
            return obj.issue_date.strftime("%b %Y")

        return None


class MemberProfileSerializer(UserSerializer):
    academic_records = AcademicRecordSerializer(many=True, read_only=True, source="academic_record_set")
    certifications = CertificationSerializer(many=True, read_only=True, source="certification_set")
    honors_or_awards = HonorOrAwardSerializer(many=True, read_only=True, source="honor_or_award_set")
    languages = LanguageSerializer(many=True, read_only=True, source="language_set")
    projects = ProjectSerializer(many=True, read_only=True, source="project_set")
    publications = PublicationSerializer(many=True, read_only=True, source="publication_set")
    skills = SkillSerializer(many=True, read_only=True, source="skill_set")
    web_links = WebLinkSerializer(many=True, read_only=True, source="web_link_set")
    work_experiences = WorkExperienceSerializer(many=True, read_only=True, source="work_experience_set")

    class Meta(UserSerializer.Meta):
        pass


class MemberProfileExtendedSerializer(MemberProfileSerializer):
    preferences = UserPreferenceSerializer(many=False, read_only=True, source="preference")

    class Meta(MemberProfileSerializer.Meta):
        pass


class MemberProfileSerializerForResumeTemplate(MemberProfileSerializer):
    location = serializers.SerializerMethodField()
    academic_records = AcademicRecordSerializerForResumeTemplate(
        many=True, read_only=True, source="academic_record_set"
    )
    certifications = CertificationSerializerForResumeTemplate(many=True, read_only=True, source="certification_set")
    honors_or_awards = HonorOrAwardSerializerForResumeTemplate(many=True, read_only=True, source="honor_or_award_set")
    languages = LanguageSerializer(many=True, read_only=True, source="language_set")
    projects = ProjectSerializerForResumeTemplate(many=True, read_only=True, source="project_set")
    publications = PublicationSerializerForResumeTemplate(many=True, read_only=True, source="publication_set")
    skills = SkillSerializer(many=True, read_only=True, source="skill_set")
    web_links = WebLinkSerializerForResumeTemplate(many=True, read_only=True, source="web_link_set")
    work_experiences = WorkExperienceSerializerForResumeTemplate(
        many=True, read_only=True, source="work_experience_set"
    )

    class Meta(MemberProfileSerializer.Meta):
        pass

    def get_location(self, obj: User) -> Optional[str]:  # pylint: disable=no-self-use
        if obj.address and obj.country:
            return f"{obj.address}, {obj.country.name}"

        if obj.address:
            return obj.address

        if obj.country:
            return obj.country.name

        return None
