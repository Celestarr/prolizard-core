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
    "confetti.apps.AdminConfig",
    "confetti.apps.core",
    "confetti.apps.identity",
    "confetti.apps.member",
    "confetti.apps.storage",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
