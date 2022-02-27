from rest_framework.routers import SimpleRouter

from .views import ResumeViewSet

app_name = "storage"  # pylint: disable=invalid-name

router = SimpleRouter()
router.register(r"resume", ResumeViewSet, basename="resume")

urlpatterns = router.urls
