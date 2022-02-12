from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.core.models.user import User
from apps.core.serializers.common import ErrorSerializer
from apps.core.serializers.user import UserSerializer
from apps.core.viewsets import ModelViewSet


@extend_schema(tags=["User"])
@extend_schema_view(
    list=extend_schema(
        summary="List All User",
        description="Return a list of all users in the system.",
        responses={
            200: UserSerializer(many=True),
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
    create=extend_schema(
        summary="Create User",
        description="Create a new instance of user.",
        responses={
            201: UserSerializer,
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
    retrieve=extend_schema(
        summary="Retrieve User",
        description="Retrieve an instance of user.",
        responses={
            200: UserSerializer,
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
    update=extend_schema(
        summary="Update User",
        description="Update an instance of user.",
        responses={
            200: UserSerializer,
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
    partial_update=extend_schema(
        summary="Partially Update User",
        description="Update an instance of user.",
        responses={
            200: UserSerializer,
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
    destroy=extend_schema(
        summary="Delete User",
        description="Delete an instance of user.",
        responses={
            204: None,
            401: ErrorSerializer,
            403: ErrorSerializer,
            404: ErrorSerializer,
            500: ErrorSerializer,
        },
    ),
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]
