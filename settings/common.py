from pathlib import Path

from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RESUME_TEMPLATE_TEMPORARY_DIR = BASE_DIR / "resume_templates"

APP_URL = config("APP_URL")

USE_S3 = config("USE_S3", default=False, cast=bool)
