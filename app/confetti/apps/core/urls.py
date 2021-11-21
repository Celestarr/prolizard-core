from rest_framework.routers import SimpleRouter

from confetti.apps.core.views.common import MetadataViewSet, HealthViewSet

router = SimpleRouter()
router.register(r"api/meta", MetadataViewSet, basename="metadata")
router.register(r"health", HealthViewSet, basename="health")

urlpatterns = router.urls
