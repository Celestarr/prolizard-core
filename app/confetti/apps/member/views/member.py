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
    write_only_serializer_class = UserWriteOnlySerializer
    queryset = User.objects.all()
    permission_classes_by_action = {
        "create": [AllowAny],
        "destroy": [IsAuthenticated, IsObjectOwner],
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated, IsObjectOwner],
        "update": [IsAuthenticated, IsObjectOwner],
        "retrieve_profile_by_username": [AllowAny],
        "me": [IsAuthenticated],
        "generate_resume": [IsAuthenticated],
        "preferences": [IsAuthenticated],
    }

    @action(detail=False, methods=["get", "patch"], url_name="retrieve-or-update-current-user")
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
            return Response({"detail": gettext("Something went wrong.")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

    @action(
        detail=False, methods=["get"], url_name="retrieve-profile-by-username", url_path="profile/(?P<username>.+)"
    )
    def retrieve_profile_by_username(self, request, username):
        del request

        try:
            user = User.objects.get(username=username)
            return Response(MemberProfileExtendedSerializer(user).data)
        except User.DoesNotExist:
            raise NotFound(gettext("Member profile not found."))

    # @action(
    #     detail=False,
    #     methods=["get"],
    #     url_name="generate-resume-by-username",
    #     url_path="generate-resume/(?P<username>.+)",
    # )
    # def generate_resume(self, _, username):
    #     response_data = {}
    #     response_content_type = "application/json"
    #     response_status_code = status.HTTP_200_OK
    #     resume_generator_endpoint = urljoin(settings.PDF_GENERATOR_URL, "generate-resume")
    #     try:
    #         user = User.objects.filter(username=username)
    #         if user:
    #             user_data = UserExtendedSerializer(user[0]).data
    #             resume_generator_payload = {
    #                 "user": user_data,
    #             }
    #             res = requests.post(resume_generator_endpoint, json=resume_generator_payload)
    #             if res.ok:
    #                 response_data = res.content
    #                 response_content_type = "application/pdf"
    #             else:
    #                 response_data["detail"] = "Could not generate resume."
    #                 response_status_code = status.HTTP_502_BAD_GATEWAY
    #         else:
    #             response_data["detail"] = "User not found."
    #             response_status_code = status.HTTP_404_NOT_FOUND
    #     except Exception as ex:
    #         print(ex)
    #         response_data["detail"] = str(ex)
    #         response_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    #     finally:
    #         if response_content_type == "application/json":
    #             return Response(response_data, status=response_status_code)
    #         else:
    #             return HttpResponse(response_data, content_type=response_content_type, status=response_status_code)


__all__ = ["MemberViewSet"]
