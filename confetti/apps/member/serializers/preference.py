from rest_framework import serializers

from confetti.apps.member.models import MemberPreference

from .template import PortfolioTemplateSerializer, ResumeTemplateSerializer


class MemberPreferenceSerializer(serializers.ModelSerializer):
    portfolio_template = PortfolioTemplateSerializer()
    resume_template = ResumeTemplateSerializer()

    class Meta:
        exclude = [
            "created_at",
            "id",
            "updated_at",
            "user",
        ]
        model = MemberPreference


class MemberPreferenceWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(MemberPreferenceSerializer.Meta):
        pass
