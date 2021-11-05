from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from confetti.apps.core.models.confirmation_key import ConfirmationKey
from confetti.apps.core.serializers.confirmation_key import ConfirmationKey, ConfirmationKeySerializer
from confetti.apps.core.viewsets import ModelViewSet


@extend_schema(tags=["Confirmation Key"])
@extend_schema_view(
    list=extend_schema(
        summary="List All Confirmation Key",
        description="Return a list of all confirmation keys in the system.",
    ),
    create=extend_schema(
        summary="Create Confirmation Key",
        description="Create a new instance of confirmation key.",
    ),
    retrieve=extend_schema(
        summary="Retrieve Confirmation Key",
        description="Retrieve an instance of confirmation key.",
    ),
    update=extend_schema(
        summary="Update Confirmation Key",
        description="Update an instance of confirmation key.",
    ),
    partial_update=extend_schema(
        summary="Partially Update Confirmation Key",
        description="Update an instance of confirmation key.",
    ),
    destroy=extend_schema(
        summary="Delete Confirmation Key",
        description="Delete an instance of confirmation key.",
    ),
)
class ConfirmationKeyViewSet(ModelViewSet):
    queryset = ConfirmationKey.objects.all()
    serializer_class = ConfirmationKeySerializer
    permission_classes = [IsAuthenticated & IsAdminUser]
