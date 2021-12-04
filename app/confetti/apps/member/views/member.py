from django.db import IntegrityError, transaction
from django.utils.translation import gettext
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, NotFound, PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from confetti.apps.core.models import User
from confetti.apps.core.permissions import IsObjectOwner
from confetti.apps.core.serializers import UserSerializer, UserWriteOnlySerializer
from confetti.apps.core.viewsets import ModelViewSet
from confetti.apps.member.models import MemberPreference
from confetti.apps.member.serializers import (
    MemberPreferenceSerializer,
    MemberPreferenceWriteOnlySerializer,
    MemberProfileExtendedSerializer,
    MemberProfileSerializer,
)
from confetti.services import kafka


class MemberViewSet(ModelViewSet):
    serializer_class = UserSerializer
    serializer_class_write_only = UserWriteOnlySerializer
    queryset = User.objects.all()
    permission_classes_by_action = {
        "retrieve": [IsAuthenticated, IsObjectOwner],
        "me": [IsAuthenticated],
        "preferences": [IsAuthenticated],
    }
    lookup_fields = ["username", "pk"]
    allowed_actions = ['retrieve', 'me', 'preferences']

    def retrieve(self, request, *args, **kwargs):
        del request, args, kwargs

        instance = self.get_object()
        serializer = MemberProfileExtendedSerializer(instance)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get", "patch"],
        url_name="retrieve-or-update-current-user",
    )
    def me(self, request):
        user = request.user
        extended_profile = None

        try:
            with transaction.atomic():
                if request.method == "PATCH":
                    self.kwargs["pk"] = user.pk
                    partial_update_res = self.partial_update(request, pk=user.pk)

                    extended_profile = MemberProfileExtendedSerializer(
                        self.updated_instance if self.updated_instance else user
                    ).data
                    # kafka.send_resume_build_message(extended_profile)

                    return partial_update_res
        except kafka.errors.MessageNotSent:
            return Response(
                {"detail": gettext("Something went wrong.")},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(extended_profile if extended_profile else MemberProfileExtendedSerializer(user).data)

    @action(detail=False, methods=["patch"], url_name="update-current-user-preferences")
    def preferences(self, request):
        user = request.user

        try:
            with transaction.atomic():
                preference = MemberPreference.objects.get(user=user)
                serializer = MemberPreferenceWriteOnlySerializer(preference, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                model_instance = serializer.save()

                # extended_profile = MemberProfileExtendedSerializer(user).data
                # kafka.send_resume_build_message(extended_profile)

                return Response(MemberPreferenceSerializer(model_instance).data)
        except MemberPreference.DoesNotExist:
            print("member preference object not found")
            raise APIException(gettext("Something went wrong."))
        except kafka.errors.MessageNotSent as e:
            print(e)
            raise APIException(gettext("Something went wrong."))
        except ValidationError as e:
            raise e
        except IntegrityError as e:
            print(e)
            raise APIException(gettext("Something went wrong."))
        except Exception as ex:
            print(ex)
            raise APIException(gettext("Something went wrong."))


__all__ = ["MemberViewSet"]
