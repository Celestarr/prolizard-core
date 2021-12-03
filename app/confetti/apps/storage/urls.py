from django.urls import path

from .views import DownloadResumeViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'member-resume', DownloadResumeViewSet, basename='store-member-resume')

urlpatterns = router.urls
