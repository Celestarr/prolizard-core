from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from confetti.apps.core.views import SignInView, SignUpView
from confetti.apps.core.views.common import MetadataViewSet, NotFoundView

router = SimpleRouter()
router.register(r"api/meta", MetadataViewSet, basename="metadata")

urlpatterns = [
    # path("sign-in/", SignInView.as_view(), name="sign-in"),
    # path("sign-up/", SignUpView.as_view(), name="sign-up"),
    *router.urls,
    # Fallback route, raises 404 - not found.
    # re_path(r"^.*$", NotFoundView.as_view(), name="not-found"),
]
