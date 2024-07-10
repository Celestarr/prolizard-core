from app.utils.views.viewsets import UserModelViewSet

from .models import JobTracker
from .serializers import JobTrackerWriteSerializer


class JobTrackerViewSet(UserModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = JobTracker.objects.all()
    search_fields = [
        "interview_round",
        "notes",
        "organization_name",
        "position_title",
        "status",
    ]
    serializer_class = JobTrackerWriteSerializer
    serializer_class_write_only = JobTrackerWriteSerializer
