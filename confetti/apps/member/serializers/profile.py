from rest_framework import serializers

from confetti.apps.core.models import User
from confetti.apps.core.serializers import UserSerializer

from .preference import MemberPreferenceSerializer
from .profile_section import (
    AcademicRecordSerializer,
    AcademicRecordSerializerForResumeTemplate,
    CertificationSerializer,
    CertificationSerializerForResumeTemplate,
    HonorOrAwardSerializer,
    HonorOrAwardSerializerForResumeTemplate,
    LanguageSerializer,
    ProjectSerializer,
    ProjectSerializerForResumeTemplate,
    PublicationSerializer,
    PublicationSerializerForResumeTemplate,
    SkillSerializer,
    WebLinkSerializer,
    WebLinkSerializerForResumeTemplate,
    WorkExperienceSerializer,
    WorkExperienceSerializerForResumeTemplate,
)


class MemberProfileSerializer(UserSerializer):
    academic_records = AcademicRecordSerializer(many=True, read_only=True, source="member_academic_record_set")
    certifications = CertificationSerializer(many=True, read_only=True, source="member_certification_set")
    honors_or_awards = HonorOrAwardSerializer(many=True, read_only=True, source="member_honor_or_award_set")
    languages = LanguageSerializer(many=True, read_only=True, source="member_language_set")
    projects = ProjectSerializer(many=True, read_only=True, source="member_project_set")
    publications = PublicationSerializer(many=True, read_only=True, source="member_publication_set")
    skills = SkillSerializer(many=True, read_only=True, source="member_skill_set")
    web_links = WebLinkSerializer(many=True, read_only=True, source="member_web_link_set")
    work_experiences = WorkExperienceSerializer(many=True, read_only=True, source="member_work_experience_set")

    class Meta(UserSerializer.Meta):
        pass


class MemberProfileExtendedSerializer(MemberProfileSerializer):
    preferences = MemberPreferenceSerializer(many=False, read_only=True, source="member_preference")

    class Meta(MemberProfileSerializer.Meta):
        pass


class MemberProfileSerializerForResumeTemplate(MemberProfileSerializer):
    location = serializers.SerializerMethodField()
    academic_records = AcademicRecordSerializerForResumeTemplate(
        many=True, read_only=True, source="member_academic_record_set"
    )
    certifications = CertificationSerializerForResumeTemplate(
        many=True, read_only=True, source="member_certification_set"
    )
    honors_or_awards = HonorOrAwardSerializerForResumeTemplate(
        many=True, read_only=True, source="member_honor_or_award_set"
    )
    languages = LanguageSerializer(many=True, read_only=True, source="member_language_set")
    projects = ProjectSerializerForResumeTemplate(many=True, read_only=True, source="member_project_set")
    publications = PublicationSerializerForResumeTemplate(many=True, read_only=True, source="member_publication_set")
    skills = SkillSerializer(many=True, read_only=True, source="member_skill_set")
    web_links = WebLinkSerializerForResumeTemplate(many=True, read_only=True, source="member_web_link_set")
    work_experiences = WorkExperienceSerializerForResumeTemplate(
        many=True, read_only=True, source="member_work_experience_set"
    )

    class Meta(MemberProfileSerializer.Meta):
        pass

    def get_location(self, obj: User) -> str:
        if obj.address and obj.country:
            return "{}, {}".format(obj.address, obj.country.name)

        if obj.address:
            return obj.address

        if obj.country:
            return obj.country.name

        return None
