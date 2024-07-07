from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("career/", include("app.apps.career.urls")),
                path("profile/", include("app.apps.profile.urls")),
                path("rm/", include("app.apps.reference_management.urls")),
                path("storage/", include("app.apps.storage.urls")),
                path("", include("app.apps.core.urls")),
            ]
        ),
    ),
    path(
        "identity/",
        include(
            [
                path("oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
                path("dj/", include("django.contrib.auth.urls")),
                path("", include("app.apps.user_management.urls")),
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
