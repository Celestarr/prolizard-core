from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Consumer/user API endpoints.
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
        "id/",
        include(
            [
                path("oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
                path("dj/", include("django.contrib.auth.urls")),
                path("", include("app.apps.user_management.urls")),
            ]
        ),
    ),
    # Routes related to the application's internal functionality.
    path(
        "sys/",
        include(
            [
                path("admin/", admin.site.urls),
            ]
        ),
    ),
]
