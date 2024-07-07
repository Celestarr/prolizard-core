from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.utils.views.viewsets import UserModelViewSet

from .models import JobTracker, JobTrackerHistory
from .serializers import JobTrackerWriteSerializer


class JobTrackerViewSet(UserModelViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = JobTrackerWriteSerializer
    serializer_class_write_only = JobTrackerWriteSerializer
    queryset = JobTracker.objects.all()
