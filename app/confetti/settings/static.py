import os

from .common import BASE_DIR
from .core import DEBUG

AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_S3_ACCESS_KEY_ID")

AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY")

AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")

# If you’re using S3 as a CDN (via CloudFront), you’ll probably want this
# storage to serve those files using that:
# AWS_S3_CUSTOM_DOMAIN = 'cdn.myfolab.com'

AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

if not DEBUG:
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3ManifestStaticStorage"

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

if not DEBUG:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
