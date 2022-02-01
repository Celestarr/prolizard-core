from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models.user_email import UserEmail


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        exclude = ()
