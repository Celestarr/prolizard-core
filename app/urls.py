from django.conf.urls import include
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
