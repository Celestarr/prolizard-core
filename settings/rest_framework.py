REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "middlewares.global_exception_handler.global_exception_handler",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "apps.common.pagination.PageNumberPagination",
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "MyFo API",
    "DESCRIPTION": "Primary API Service for MyFo.",
    "VERSION": "0.0.1",
    "SERVERS": [
        {"url": "http://localhost:8000"},
    ],
}
