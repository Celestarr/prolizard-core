import random

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, extend_schema_view
from psycopg2.errors import UniqueViolation
from rest_framework import status
from rest_framework.exceptions import ParseError, PermissionDenied, ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.viewsets import GenericViewSet

from confetti.apps.core.models.confirmation_key import ConfirmationKey
from confetti.apps.core.models.user_email import UserEmail
from confetti.apps.core.models.utils import get_username_sequence_value
from confetti.apps.core.serializers.common import ErrorSerializer, GenericSuccessSerializer
from confetti.apps.core.serializers.user import UserSerializer, UserWriteOnlySerializer
from confetti.apps.core.serializers.user_email import UserEmailSerializer
from confetti.apps.member.models.preference import MemberPreference
from confetti.apps.member.serializers import (
    EmailConfirmationSerializer,
    MemberSignInSerializer,
    MemberSignUpSerializer,
)
from confetti.apps.member.serializers.preference import MemberPreferenceWriteOnlySerializer

EMAIL_CONFIRMATION_REQUIRED = settings.EMAIL_CONFIRMATION_REQUIRED


@extend_schema_view(
    create=extend_schema(
        summary="Member Sign Up",
        description="Sign up as a new member.",
        tags=["Member"],
        responses={
            200: GenericSuccessSerializer,
            400: ErrorSerializer,
            500: ErrorSerializer,
        },
        request=MemberSignUpSerializer,
    )
)
class MemberSignUpViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserWriteOnlySerializer
    permission_classes = (AllowAny,)

    @staticmethod
    def make_user_serializer_data(serializer: MemberSignUpSerializer) -> ReturnDict:
        serializer_data = serializer.validated_data
        seq = get_username_sequence_value()

        return {
            "first_name": serializer_data["first_name"],
            "last_name": serializer_data["last_name"],
            "email": serializer_data["email"],
            "password": make_password(serializer_data["password"]),
            "username": str(seq),
            "is_active": not EMAIL_CONFIRMATION_REQUIRED,
        }

    def perform_create(self, serializer):
        user_instance = serializer.save()

        MemberPreference.objects.create(user=user_instance)

        confirmation_key = None

        if EMAIL_CONFIRMATION_REQUIRED:
            while True:
                try:
                    confirmation_key = ConfirmationKey.objects.create(
                        key=get_random_string(random.SystemRandom().randint(44, 86)),
                        expires_at=timezone.now() + timezone.timedelta(days=1),
                    )
                    break
                except IntegrityError as e:
                    if hasattr(e, "__cause__") and isinstance(e.__cause__, UniqueViolation):
                        continue
                    raise

        user_email_serializer = UserEmailSerializer(
            data={
                "confirmation_key": confirmation_key.id if confirmation_key else None,
                "email": user_instance.email,
                "user": user_instance.id,
                "is_verified": not EMAIL_CONFIRMATION_REQUIRED,
            }
        )
        user_email_serializer.is_valid(raise_exception=True)
        user_email_serializer.save()

    def create(self, request, *args, **kwargs) -> Response:
        del args, kwargs
        sign_up_serializer = MemberSignUpSerializer(data=request.data)
        sign_up_serializer.is_valid(raise_exception=True)

        serializer = self.get_serializer(data=self.make_user_serializer_data(sign_up_serializer))
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                self.perform_create(serializer)
        except (IntegrityError, ValidationError) as e:
            print(e)
            return Response({"detail": gettext("Something went wrong.")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(e)
            return Response({"detail": gettext("Something went wrong.")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if EMAIL_CONFIRMATION_REQUIRED:
            return Response({"message": gettext("Signed up successfully. Please confirm your email to continue.")})

        return Response({"message": gettext("Signed up successfully.")})


@extend_schema_view(
    create=extend_schema(
        summary="Member Sign In",
        description="Sign in as an existing member.",
        tags=["Member"],
        responses={
            200: GenericSuccessSerializer,
            400: ErrorSerializer,
            500: ErrorSerializer,
        },
        request=MemberSignInSerializer,
    )
)
class MemberSignInViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = MemberSignInSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs) -> Response:
        del args, kwargs

        sign_in_serializer = self.get_serializer(data=request.data)
        sign_in_serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=sign_in_serializer.validated_data["email"], password=sign_in_serializer.validated_data["password"]
        )

        if not user:
            raise PermissionDenied(gettext("Incorrect email or password."), code="sign_in_failure")

        login(request, user)

        if not sign_in_serializer.validated_data["remember"]:
            request.session.set_expiry(0)

        return Response({"message": gettext("Sign in success!")})


@extend_schema_view(
    create=extend_schema(
        summary="Member Confirm Email",
        description="Confirm email.",
        tags=["Member"],
        responses={
            200: GenericSuccessSerializer,
            400: ErrorSerializer,
            500: ErrorSerializer,
        },
        request=EmailConfirmationSerializer,
    )
)
class MemberConfirmEmailViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs) -> Response:
        del args, kwargs

        serializer = EmailConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.validated_data

        try:
            with transaction.atomic():
                user_email_instance = UserEmail.objects.get(
                    Q(user__username=serializer_data["user"])
                    & Q(email=serializer_data["email"])
                    & Q(is_verified=False)
                    & Q(confirmation_key__key=serializer_data["key"])
                    & Q(confirmation_key__expires_at__gte=timezone.now())
                )
                user_email_instance.is_verified = True
                user_email_instance.save()

                user_email_instance.user.is_active = True
                user_email_instance.user.save()
        except UserEmail.DoesNotExist:
            raise ParseError(detail=_("Confirmation key might be invalid for this user."))
        except (IntegrityError, ValidationError):
            return Response({"detail": _("Something went wrong.")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": _("Email confirmed successfully.")})


@extend_schema_view(
    create=extend_schema(
        summary="Member Sign Out",
        description="Sign out.",
        tags=["Member"],
        responses={
            200: GenericSuccessSerializer,
            400: ErrorSerializer,
            500: ErrorSerializer,
        },
        request=None,
    )
)
class MemberSignOutViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs) -> Response:
        del args, kwargs

        logout(request)

        return Response({"message": _("Signed out successfully.")})


__all__ = ["MemberConfirmEmailViewSet", "MemberSignInViewSet", "MemberSignUpViewSet", "MemberSignOutViewSet"]
