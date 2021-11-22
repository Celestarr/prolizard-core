from rest_framework.routers import SimpleRouter

from confetti.apps.core.views.common import MetadataViewSet

router = SimpleRouter()
router.register(r"api/meta", MetadataViewSet, basename="metadata")

urlpatterns = router.urls
