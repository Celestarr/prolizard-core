from django.conf import settings
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from confetti.apps.core.models.user_email import UserEmail


class MemberSignUpSerializer(serializers.Serializer):
    agree = serializers.BooleanField(required=True)
    first_name = serializers.CharField(
        label=_("first name"),
        max_length=settings.FIELD_META["first_name"]["max_length"],
        min_length=settings.FIELD_META["first_name"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid first name."),
            "blank": _("Enter a valid first name."),
            "max_length": _("Enter a valid first name."),
            "min_length": _("Enter a valid first name."),
        },
    )
    last_name = serializers.CharField(
        label=_("last name"),
        max_length=settings.FIELD_META["last_name"]["max_length"],
        min_length=settings.FIELD_META["last_name"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid last name."),
            "blank": _("Enter a valid last name."),
            "max_length": _("Enter a valid last name."),
            "min_length": _("Enter a valid last name."),
        },
    )
    email = serializers.EmailField(
        label=_("email"),
        max_length=settings.FIELD_META["email"]["max_length"],
        min_length=settings.FIELD_META["email"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid email address."),
            "blank": _("Enter a valid email address."),
            "max_length": _("Enter a valid email address."),
            "min_length": _("Enter a valid email address."),
        },
    )
    password = serializers.CharField(
        label=_("password"),
        min_length=settings.FIELD_META["password"]["min_length"],
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid password."),
            "blank": _("Enter a valid password."),
            "max_length": _("Enter a valid password."),
            "min_length": _("Enter a valid password."),
        },
    )
    confirm_password = serializers.CharField(
        label=_("confirm password"),
        min_length=settings.FIELD_META["password"]["min_length"],
        required=True,
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid confirm password."),
            "blank": _("Enter a valid confirm password."),
            "max_length": _("Enter a valid confirm password."),
            "min_length": _("Enter a valid confirm password."),
        },
    )

    def validate_agree(self, value):
        if not value:
            raise serializers.ValidationError(gettext("You must agree to the terms and conditions."))

        return value

    def validate_email(self, value):
        try:
            UserEmail.objects.get(email=value)
            raise serializers.ValidationError(gettext("Email is invalid or already taken."))
        except UserEmail.DoesNotExist:
            return value

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(gettext("Password and confirm password do not match."))

        return super().validate(attrs)


class EmailConfirmationSerializer(serializers.Serializer):
    user = serializers.CharField(
        label=_("username"),
        max_length=settings.FIELD_META["username"]["max_length"],
        min_length=settings.FIELD_META["username"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid username."),
            "blank": _("Enter a valid username."),
            "max_length": _("Enter a valid username."),
            "min_length": _("Enter a valid username."),
        },
    )
    email = serializers.EmailField(
        label=_("email"),
        max_length=settings.FIELD_META["email"]["max_length"],
        min_length=settings.FIELD_META["email"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid email address."),
            "blank": _("Enter a valid email address."),
            "max_length": _("Enter a valid email address."),
            "min_length": _("Enter a valid email address."),
        },
    )
    key = serializers.CharField(
        label=_("confirmation key"),
        max_length=settings.FIELD_META["confirmation_key"]["max_length"],
        min_length=settings.FIELD_META["confirmation_key"]["min_length"],
        required=True,
        write_only=True,
        error_messages={
            "invalid": _("Enter a valid confirmation key."),
            "blank": _("Enter a valid confirmation key."),
            "max_length": _("Enter a valid confirmation key."),
            "min_length": _("Enter a valid confirmation key."),
        },
    )


class MemberSignInSerializer(serializers.Serializer):
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
    remember = serializers.BooleanField(
        label="Remember me",
        required=True,
        write_only=True,
    )
