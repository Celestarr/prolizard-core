from rest_framework import serializers

from ..core.serializers import CountrySerializer
from .models import JobTracker


class JobTrackerReadSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        exclude = ("created_at", "updated_at")
        model = JobTracker
        extra_kwargs = {
            "user": {"write_only": True},
        }


class JobTrackerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("created_at", "updated_at")
        model = JobTracker
        extra_kwargs = {
            "user": {"write_only": True},
        }
