from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("api/members/", include("confetti.apps.member.urls")),
    path("api/store/", include("confetti.apps.storage.urls")),
    path("", include("confetti.apps.core.urls")),
    path("identity/", include("confetti.apps.identity.urls")),
    path("identity/oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("identity/dj/", include("django.contrib.auth.urls")),
    path("internal/admin/", admin.site.urls),
]
