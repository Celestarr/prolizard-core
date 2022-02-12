from os import getenv

DATABASES = {
    "default": {
        "NAME": getenv("RDS_DB_NAME") or getenv("DB_NAME"),
        "ENGINE": "django.db.backends.postgresql",
        "USER": getenv("RDS_USERNAME") or getenv("DB_USER"),
        "PASSWORD": getenv("RDS_PASSWORD") or getenv("DB_PASSWORD"),
        "HOST": getenv("RDS_HOSTNAME") or getenv("DB_HOST"),
        "PORT": getenv("RDS_PORT") or getenv("DB_PORT"),
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
