from rest_framework.routers import SimpleRouter

from app.utils.views.routers import HyphenatedSimpleRouter

from .views import ResumeViewSet

app_name = "storage"  # pylint: disable=invalid-name

router = HyphenatedSimpleRouter()
router.register(r"resume", ResumeViewSet, basename="resume")

urlpatterns = router.urls
