from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = []

if not settings.USE_S3:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("api/", include("apps.common.urls")),
    path("api/profile/", include("apps.profile.urls")),
    path("api/store/", include("apps.storage.urls")),
    path("identity/", include("apps.identity.urls")),
    path("identity/oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("identity/dj/", include("django.contrib.auth.urls")),
    path("internal/admin/", admin.site.urls),
]
