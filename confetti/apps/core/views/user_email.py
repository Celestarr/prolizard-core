from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from confetti.apps.core.models.user_email import UserEmail
from confetti.apps.core.serializers.user_email import UserEmailSerializer
from confetti.apps.core.viewsets import ModelViewSet


@extend_schema(tags=["User Email"])
@extend_schema_view(
    list=extend_schema(
        summary="List All User Email",
        description="Return a list of all user emails in the system.",
    ),
    create=extend_schema(
        summary="Create User Email",
        description="Create a new instance of user email.",
    ),
    retrieve=extend_schema(
        summary="Retrieve User Email",
        description="Retrieve an instance of user email.",
    ),
    update=extend_schema(
        summary="Update User Email",
        description="Update an instance of user email.",
    ),
    partial_update=extend_schema(
        summary="Partially Update User Email",
        description="Update an instance of user email.",
    ),
    destroy=extend_schema(
        summary="Delete User Email",
        description="Delete an instance of user email.",
    ),
)
class UserEmailViewSet(ModelViewSet):
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]
