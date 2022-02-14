from django.db import IntegrityError, transaction
from django.utils.translation import gettext
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.core.models import User
from apps.core.permissions import IsObjectOwner
from apps.core.serializers import UserSerializer, UserWriteOnlySerializer
from apps.core.viewsets import ModelViewSet
from apps.member.models import MemberPreference
from apps.member.serializers import (
    MemberPreferenceSerializer,
    MemberPreferenceWriteOnlySerializer,
    MemberProfileExtendedSerializer,
)


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
    allowed_actions = ["retrieve", "me", "preferences"]

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

        with transaction.atomic():
            if request.method == "PATCH":
                self.kwargs["pk"] = user.pk
                partial_update_res = self.partial_update(request, pk=user.pk)

                extended_profile = MemberProfileExtendedSerializer(
                    self.updated_instance if self.updated_instance else user
                ).data

                return partial_update_res

        return Response(extended_profile if extended_profile else MemberProfileExtendedSerializer(user).data)

    @action(detail=False, methods=["patch"], url_name="update-current-user-preferences")
    def preferences(self, request):  # pylint: disable=no-self-use
        user = request.user

        try:
            with transaction.atomic():
                preference = MemberPreference.objects.get(user=user)
                serializer = MemberPreferenceWriteOnlySerializer(preference, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                model_instance = serializer.save()

                return Response(MemberPreferenceSerializer(model_instance).data)
        except MemberPreference.DoesNotExist as exception:
            print("member preference object not found")
            raise APIException(gettext("Something went wrong.")) from exception
        except ValidationError as exception:
            raise exception
        except IntegrityError as exception:
            print(exception)
            raise APIException(gettext("Something went wrong.")) from exception
        except Exception as exception:
            print(exception)
            raise APIException(gettext("Something went wrong.")) from exception


__all__ = ["MemberViewSet"]
