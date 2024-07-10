from rest_framework import serializers

from .models import JobTracker


class JobTrackerReadSerializer(serializers.ModelSerializer):
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
