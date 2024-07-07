from app.utils.views.routers import HyphenatedSimpleRouter

from .views import JobTrackerViewSet

app_name = "career"  # pylint: disable=invalid-name

router = HyphenatedSimpleRouter()
router.register(r"job-trackers", JobTrackerViewSet)

urlpatterns = router.urls
