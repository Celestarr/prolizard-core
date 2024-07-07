"""
Django settings for this project.
"""

from pathlib import Path
from urllib.parse import urljoin

import requests
from corsheaders.defaults import default_headers as cors_default_headers
from decouple import config

# Common variables

APP_ENV = config("APP_ENV", default="development")

APP_URL = config("APP_URL")

AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID", default="")

AWS_S3_SECRET_ACCESS_KEY = config("AWS_S3_SECRET_ACCESS_KEY", default="")

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.parent / "data"

RESUME_TEMPLATE_TEMPORARY_DIR = BASE_DIR / "resume_templates"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# Auth
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth

APP_LOGIN_URL = urljoin(APP_URL, "/login")  # Internal

AUTHENTICATION_BACKENDS = ("app.apps.user_management.backends.ModelBackend",)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "user_management.User"

EMAIL_CONFIRMATION_REQUIRED = False  # Internal

LOGIN_URL = "/id/login/"

OAUTH2_PROVIDER = {
    # 'ACCESS_TOKEN_EXPIRE_SECONDS': 60 + 15,
    # "OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.JSONOAuthLibCore",
    "OAUTH2_VALIDATOR_CLASS": "app.utils.oauth2.RequestValidator",
    # this is the list of available scopes
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "groups": "Access to your groups",
        "member": "Member access",
        "openid": "OpenID Connect scope",
        "profile": "Member access",
        "email": "Member access",
    },
    "PKCE_REQUIRED": True,
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": config("OIDC_RSA_PRIVATE_KEY").replace("\\n", "\n"),
}

PASSWORD_HASHERS = ("django.contrib.auth.hashers.Argon2PasswordHasher",)


# Core
# https://docs.djangoproject.com/en/5.0/ref/settings/#core-settings

ALLOWED_HOSTS = [host for host in config("ALLOWED_HOSTS").split(",") if host]

try:
    ALLOWED_HOSTS.append(requests.get("http://169.254.169.254/latest/meta-data/local-ipv4", timeout=5).text.strip())
except requests.exceptions.RequestException:
    pass

APPEND_SLASH = True

DATABASES = {
    "default": {
        "NAME": config("DB_NAME"),
        "ENGINE": "django.db.backends.postgresql",
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

DEBUG = config("DEBUG", default=False, cast=bool)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FIELD_META = {
    "confirmation_key": {"max_length": 255, "min_length": 4},
    "email": {"max_length": 255, "min_length": 3},
    "first_name": {"max_length": 50, "min_length": 3},
    "last_name": {"max_length": 50, "min_length": 3},
    "password": {"min_length": 6},
    "username": {"min_length": 3, "max_length": 30},
}  # Internal

INSTALLED_APPS = (
    # Django apps
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "corsheaders",
    "drf_spectacular",
    "rest_framework",
    "django_filters",
    "oauth2_provider",
    # Project apps
    "app.apps.AdminConfig",
    "app.apps.core",
    "app.apps.career",
    "app.apps.user_management",
    "app.apps.profile",
    "app.apps.reference_management",
    "app.apps.storage",
)

LANGUAGE_CODE = "en-us"

LANGUAGES = (
    ("bn", "Bengali"),
    ("de", "German"),
    ("en", "English"),
)

LOCALE_PATHS = (BASE_DIR / "locale",)

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

MIDDLEWARE = (
    "app.middlewares.LoggingMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.middlewares.HealthCheckMiddleware",
)

ROOT_URLCONF = "app.urls"

SECRET_KEY = config("SECRET_KEY")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = "app.wsgi.application"

X_FRAME_OPTIONS = "SAMEORIGIN"


# django-cors-headers
# https://github.com/adamchainz/django-cors-headers#configuration

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = (APP_URL, *(host for host in config("CORS_ALLOWED_ORIGINS").split(",") if host))

CORS_ALLOW_HEADERS = list(cors_default_headers) + [
    "auth0-client",
]

# Django REST framework

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "app.middlewares.global_exception_handler.global_exception_handler",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "app.utils.views.pagination.PageNumberPagination",
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ProLizard API",
    "DESCRIPTION": "Primary API Service for ProLizard.",
    "VERSION": "0.0.1",
    "SERVERS": [
        {"url": "http://localhost:8000"},
    ],
}


# Messages
# https://docs.djangoproject.com/en/5.0/ref/settings/#messages

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"


# Security
# https://docs.djangoproject.com/en/5.0/ref/settings/#security

CSRF_COOKIE_DOMAIN = config("CSRF_COOKIE_DOMAIN")

CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=False, cast=bool)


# Sessions
# https://docs.djangoproject.com/en/5.0/ref/settings/#sessions

SESSION_COOKIE_DOMAIN = config("SESSION_COOKIE_DOMAIN")

SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=False, cast=bool)


# Static files
# https://docs.djangoproject.com/en/5.0/ref/settings/#static-files

AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ENDPOINT_URL", default=None)

AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL", default=None)

AWS_S3_REGION_NAME = config("AWS_S3_ENDPOINT_URL", default=None)

AWS_S3_SECRET_ACCESS_KEY = config("AWS_S3_ENDPOINT_URL", default=None)

AWS_QUERYSTRING_AUTH = False

AWS_STORAGE_BUCKET_NAME = config("AWS_S3_ENDPOINT_URL", default=None)

# Custom setting. Only used for static files with no queryauth.
AWS_STATIC_BUCKET_NAME = config("AWS_STATIC_BUCKET_NAME", default=None)

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

if APP_ENV == "production":
    STORAGES["staticfiles"]["BACKEND"] = "app.services.storage_backends.S3ManifestStaticStorage"

# The absolute path to the directory where `collectstatic` will collect static files for deployment.
STATIC_ROOT = BASE_DIR / "static" / "dist"

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static" / "assets",  # Raw assets that do not require compilation.
    BASE_DIR / "static" / "build",  # Built assets from static/src.
]

MEDIA_MAX_SIZE = config("MEDIA_MAX_SIZE", cast=int, default=5 * 1024 * 1024)
