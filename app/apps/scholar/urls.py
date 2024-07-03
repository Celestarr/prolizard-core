from rest_framework.routers import SimpleRouter

from .views import ArticleSearchViewSet

app_name = "scholar"  # pylint: disable=invalid-name

router = SimpleRouter()
router.register(r"articles", ArticleSearchViewSet, basename="article-search")

urlpatterns = router.urls
