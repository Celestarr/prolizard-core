from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

CV_TEMPLATE_TEMPORARY_DIR = BASE_DIR / "cv_templates"

APP_URL = getenv("APP_URL")
