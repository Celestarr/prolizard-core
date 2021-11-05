from os import getenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [host for host in getenv("ALLOWED_HOSTS", "").split(",") if host]

# Application definition

ROOT_URLCONF = "confetti.urls"

WSGI_APPLICATION = "confetti.wsgi.application"

APPEND_SLASH = False

# Cors

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = []

SESSION_COOKIE_SECURE = getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"


# External urls

PASSAGE_SERVER_URL = getenv("PASSAGE_SERVER_URL")

KAFKA_SERVER_URL = getenv("KAFKA_SERVER_URL")
