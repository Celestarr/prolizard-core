from rest_framework import serializers

from app.apps.core.serializers import CountrySerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    joined_at = serializers.DateTimeField(source="created_at")

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "email": {"read_only": True},
            "id": {"read_only": True},
            # 'phone': {'read_only': True},
            "username": {"read_only": True},
        }


class UserWriteOnlySerializer(serializers.ModelSerializer):
    class Meta(UserSerializer.Meta):
        exclude = (
            "groups",
            "user_permissions",
            "is_staff",
            "is_superuser",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "id": {"read_only": True},
        }
