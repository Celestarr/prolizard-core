from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# from django.conf.urls.static import static
from django.urls import path

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

static_urlpatterns = []

if settings.DEBUG:
    static_urlpatterns.append(*static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    static_urlpatterns.append(*static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

api_urlpatterns = [
    path("api/members/", include("confetti.apps.member.urls")),
]

common_urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("api/store/", include("confetti.apps.storage.urls")),
    path("", include("confetti.apps.core.urls")),
]

urlpatterns = admin_urlpatterns + static_urlpatterns + api_urlpatterns + common_urlpatterns
