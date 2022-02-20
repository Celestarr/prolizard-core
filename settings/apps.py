DJANGO_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "drf_spectacular",
    "rest_framework",
    "django_filters",
    "oauth2_provider",
]

LOCAL_APPS = [
    "apps.AdminConfig",
    "apps.common",
    "apps.identity",
    "apps.profile",
    "apps.storage",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
