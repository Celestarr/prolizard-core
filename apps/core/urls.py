from rest_framework.routers import SimpleRouter

from apps.core.views.common import MetadataViewSet

router = SimpleRouter()
router.register(r"meta", MetadataViewSet, basename="metadata")


urlpatterns = router.urls

urlpatterns += []
