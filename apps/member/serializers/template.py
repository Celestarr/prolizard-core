from rest_framework import serializers

from apps.member.models import PortfolioTemplate, ResumeTemplate


class PortfolioTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = (
            "created_at",
            "updated_at",
        )
        model = PortfolioTemplate


class ResumeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = (
            "created_at",
            "updated_at",
        )
        model = ResumeTemplate
