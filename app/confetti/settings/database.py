from os import getenv

DATABASES = {
    "default": {
        "NAME": getenv("DB_NAME"),
        "ENGINE": "django.db.backends.postgresql",
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FIELD_META = {
    # User
    "confirmation_key": {"max_length": 255, "min_length": 4},
    "email": {"max_length": 255, "min_length": 3},
    "first_name": {"max_length": 50, "min_length": 3},
    "last_name": {"max_length": 50, "min_length": 3},
    "password": {"min_length": 6},
    "username": {"min_length": 3, "max_length": 30},
}
