from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("", include("app.apps.common.urls")),
                path("profile/", include("app.apps.profile.urls")),
                path("storage/", include("app.apps.storage.urls")),
            ]
        ),
    ),
    path(
        "identity/",
        include(
            [
                path("", include("app.apps.identity.urls")),
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


if not settings.AWS_S3_SECRET_ACCESS_KEY and not settings.AWS_S3_ACCESS_KEY_ID:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
