from django.db import IntegrityError, transaction
from django.utils.translation import gettext
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.apps.user_management.models import User
from app.apps.user_management.permissions import IsObjectOwner
from app.apps.user_management.serializers import UserSerializer, UserWriteOnlySerializer
from app.utils.views.viewsets import RetrieveUpdateModelViewSet

from .models import (
    AcademicRecord,
    Certification,
    HonorOrAward,
    Language,
    Project,
    Publication,
    Skill,
    UserPreference,
    WebLink,
    WorkExperience,
)
from .serializers import (
    AcademicRecordSerializer,
    CertificationSerializer,
    HonorOrAwardSerializer,
    LanguageSerializer,
    LanguageWriteOnlySerializer,
    MemberProfileExtendedSerializer,
    MemberProfileSerializer,
    ProjectSerializer,
    PublicationSerializer,
    SkillSerializer,
    SkillWriteOnlySerializer,
    UserPreferenceSerializer,
    UserPreferenceWriteOnlySerializer,
    WebLinkSerializer,
    WorkExperienceSerializer,
    WorkExperienceWriteOnlySerializer,
)
from .viewsets import ProfileSectionViewSet


class MemberViewSet(RetrieveUpdateModelViewSet):  # pylint: disable=too-many-ancestors
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

        # NOTE: Do not serialize user preferences
        serializer = MemberProfileSerializer(instance)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get", "patch"],
        url_name="retrieve-or-update-current-user",
    )  # pylint: disable=invalid-name
    def me(self, request):
        user = request.user

        with transaction.atomic():
            if request.method == "PATCH":
                self.kwargs["pk"] = user.pk
                self.partial_update(request, pk=user.pk)

                return Response(MemberProfileExtendedSerializer(self.updated_instance).data)

        return Response(MemberProfileExtendedSerializer(user).data)

    @action(detail=False, methods=["patch"], url_name="update-current-user-preferences")
    def preferences(self, request):
        user = request.user

        try:
            with transaction.atomic():
                preference = UserPreference.objects.get(user=user)
                serializer = UserPreferenceWriteOnlySerializer(preference, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                model_instance = serializer.save()

                return Response(UserPreferenceSerializer(model_instance).data)
        except UserPreference.DoesNotExist as exception:
            print("User preference object not found")
            raise APIException(gettext("Something went wrong.")) from exception
        except ValidationError as exception:
            raise exception
        except IntegrityError as exception:
            print(exception)
            raise APIException(gettext("Something went wrong.")) from exception
        except Exception as exception:
            print(exception)
            raise APIException(gettext("Something went wrong.")) from exception


class AcademicRecordViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = AcademicRecordSerializer
    queryset = AcademicRecord.objects.all()


class SkillViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = SkillSerializer
    serializer_class_write_only = SkillWriteOnlySerializer
    queryset = Skill.objects.all()


class WebLinkViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = WebLinkSerializer
    queryset = WebLink.objects.all()


class WorkExperienceViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = WorkExperienceSerializer
    serializer_class_write_only = WorkExperienceWriteOnlySerializer
    queryset = WorkExperience.objects.all()


class LanguageViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = LanguageSerializer
    serializer_class_write_only = LanguageWriteOnlySerializer
    queryset = Language.objects.all()


class ProjectViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class PublicationViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()


class HonorOrAwardViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = HonorOrAwardSerializer
    queryset = HonorOrAward.objects.all()


class CertificationViewSet(ProfileSectionViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = CertificationSerializer
    queryset = Certification.objects.all()
