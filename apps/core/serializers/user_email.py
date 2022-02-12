from rest_framework import serializers

from apps.core.models.user_email import UserEmail


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        exclude = ()
