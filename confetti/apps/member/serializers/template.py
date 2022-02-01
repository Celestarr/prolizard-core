from rest_framework import serializers

from confetti.apps.member.models import PortfolioTemplate, ResumeTemplate


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
            "template_file_name",
            "puppeteer_config",
            "created_at",
            "updated_at",
        )
        model = ResumeTemplate
