from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.member.models import EmploymentType


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
        ]
        model = EmploymentType


__all__ = ["EmploymentType"]
