from rest_framework.routers import SimpleRouter

from .views import ResumeViewSet

router = SimpleRouter()

router.register(r"resume", ResumeViewSet, basename="store-resume")

urlpatterns = router.urls
