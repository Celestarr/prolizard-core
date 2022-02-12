from rest_framework import serializers

from apps.member.models import EmploymentType


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = EmploymentType


__all__ = ["EmploymentType"]
