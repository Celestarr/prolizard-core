from rest_framework.routers import SimpleRouter

from .views import DownloadResumeViewSet

router = SimpleRouter()

router.register(r"member-resume", DownloadResumeViewSet, basename="store-member-resume")

urlpatterns = router.urls
