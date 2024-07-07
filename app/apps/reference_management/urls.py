from rest_framework.routers import SimpleRouter

from app.utils.views.routers import HyphenatedSimpleRouter

from .views import ArticleSearchViewSet

app_name = "reference_management"  # pylint: disable=invalid-name

router = HyphenatedSimpleRouter()
router.register(r"articles", ArticleSearchViewSet, basename="article-search")

urlpatterns = router.urls
