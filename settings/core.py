import requests
from decouple import config

from .common import APP_URL

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = [host for host in config("ALLOWED_HOSTS").split(",") if host]

EC2_PRIVATE_IP = None

try:
    EC2_PRIVATE_IP = requests.get("http://169.254.169.254/latest/meta-data/local-ipv4", timeout=5).text.strip()
except requests.exceptions.RequestException:
    pass

ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

# Application definition

ROOT_URLCONF = "urls"

WSGI_APPLICATION = "wsgi.application"

APPEND_SLASH = False

# Cors

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [host for host in config("CORS_ALLOWED_ORIGINS").split(",") if host]

CORS_ALLOWED_ORIGINS.append(APP_URL)

SESSION_COOKIE_DOMAIN = config("SESSION_COOKIE_DOMAIN")

SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", default=False, cast=bool)

CSRF_COOKIE_DOMAIN = config("CSRF_COOKIE_DOMAIN")

CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", default=False, cast=bool)
