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
    path(
        "api/",
        include(
            [
                path("", include("apps.common.urls")),
                path("profile/", include("apps.profile.urls")),
                path("storage/", include("apps.storage.urls")),
            ]
        ),
    ),
    path(
        "identity/",
        include(
            [
                path("", include("apps.identity.urls")),
                path("oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
                path("dj/", include("django.contrib.auth.urls")),
            ]
        ),
    ),
    path(
        "internal/",
        include(
            [
                path("admin/", admin.site.urls),
            ]
        ),
    ),
]
