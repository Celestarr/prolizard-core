from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer as BaseTokenRefreshSerializer


class TokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("email"),
        max_length=settings.FIELD_META["email"]["max_length"],
        min_length=settings.FIELD_META["email"]["min_length"],
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        label=_("password"),
        min_length=settings.FIELD_META["password"]["min_length"],
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    access = serializers.CharField(label=_("access token"), read_only=True)
    refresh = serializers.CharField(label=_("refresh token"), read_only=True)


class TokenRefreshPairSerializer(serializers.Serializer):
    access = serializers.CharField(label=_("access token"), read_only=True)
    refresh = serializers.CharField(label=_("refresh token"))


class TokenObtainPairInternalSerializer(BaseTokenObtainPairSerializer):
    username_field = "email"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField(
            error_messages={
                "invalid": _("Enter a valid email address."),
                "blank": _("Enter a valid email address."),
                "max_length": _("Enter a valid email address."),
                "min_length": _("Enter a valid email address."),
            },
            label=_("email"),
            max_length=settings.FIELD_META["email"]["max_length"],
            min_length=settings.FIELD_META["email"]["min_length"],
            required=True,
            write_only=True,
        )
        self.fields["password"] = serializers.CharField(
            error_messages={
                "invalid": _("Enter a valid password."),
                "blank": _("Enter a valid password."),
                "max_length": _("Enter a valid password."),
                "min_length": _("Enter a valid password."),
            },
            label=_("password"),
            min_length=settings.FIELD_META["password"]["min_length"],
            required=True,
            style={"input_type": "password"},
            trim_whitespace=False,
            write_only=True,
        )


class TokenRefreshInternalSerializer(BaseTokenRefreshSerializer):
    refresh = serializers.CharField(
        label=_("refresh token"),
        error_messages={
            "invalid": _("Enter a valid refresh token."),
            "blank": _("Enter a valid refresh token."),
            "max_length": _("Enter a valid refresh token."),
            "min_length": _("Enter a valid refresh token."),
        },
        required=True,
    )
