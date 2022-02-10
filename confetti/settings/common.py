from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

CV_TEMPLATE_TEMPORARY_DIR = BASE_DIR / "cv_templates"
