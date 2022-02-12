from rest_framework import serializers

from apps.member.models import LanguageProficiencyLevel, SkillProficiencyLevel


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
