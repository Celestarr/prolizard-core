from common.models import (
    Country,
    EmploymentType,
    Gender,
    LanguageProficiencyLevel,
    PortfolioTemplate,
    ResumeTemplate,
    SkillProficiencyLevel,
)
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Country


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = EmploymentType


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = Gender


class SkillProficiencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = SkillProficiencyLevel


class LanguageProficiencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = LanguageProficiencyLevel


class PortfolioTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = PortfolioTemplate


class ResumeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = ResumeTemplate
