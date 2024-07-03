from rest_framework.routers import SimpleRouter

from .views import JobTrackerViewSet

app_name = "career"  # pylint: disable=invalid-name

router = SimpleRouter()
router.register(r"job-trackers", JobTrackerViewSet)

urlpatterns = router.urls
