from os import getenv

import requests

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [host for host in getenv("ALLOWED_HOSTS", "").split(",") if host]

EC2_PRIVATE_IP = None

try:
    EC2_PRIVATE_IP = requests.get("http://169.254.169.254/latest/meta-data/local-ipv4", timeout=5).text.strip()
except requests.exceptions.RequestException:
    pass

ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

# Application definition

ROOT_URLCONF = "confetti.urls"

WSGI_APPLICATION = "confetti.wsgi.application"

APPEND_SLASH = False

# Cors

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [host for host in getenv("CORS_ALLOWED_ORIGINS", "").split(",") if host]

SESSION_COOKIE_SECURE = getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"

SESSION_COOKIE_DOMAIN = getenv("SESSION_COOKIE_DOMAIN")

# External urls

PASSAGE_SERVER_URL = getenv("PASSAGE_SERVER_URL")

KAFKA_SERVER_URL = getenv("KAFKA_SERVER_URL")

FLUENTD_SERVER_URL = getenv("FLUENTD_SERVER_URL")
