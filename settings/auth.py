AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 6,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "core.User"

AUTHENTICATION_BACKENDS = ["apps.core.backends.ModelBackend"]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]

EMAIL_CONFIRMATION_REQUIRED = False

LOGIN_URL = "/identity/login/"

OAUTH2_PROVIDER = {
    "OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.JSONOAuthLibCore",
    # this is the list of available scopes
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "groups": "Access to your groups",
        "member": "Member access",
    },
    "PKCE_REQUIRED": True,
}
