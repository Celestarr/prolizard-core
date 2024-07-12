from app.utils.views.viewsets import UserModelViewSet

from .models import JobTracker
from .serializers import JobTrackerReadSerializer, JobTrackerWriteSerializer


class JobTrackerViewSet(UserModelViewSet):  # pylint: disable=too-many-ancestors
    ordering_fields = [
        "country__name",
        "id",
        "organization_name",
        "position_title",
        "status",
    ]
    queryset = JobTracker.objects.all()
    search_fields = [
        "country__name",
        "interview_round",
        "notes",
        "organization_name",
        "position_title",
        "status",
    ]
    serializer_class = JobTrackerReadSerializer
    serializer_class_write_only = JobTrackerWriteSerializer
