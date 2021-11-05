from .common import BASE_DIR

LANGUAGE_CODE = "en-us"

LANGUAGES = (
    ("bn", "Bengali"),
    ("de", "German"),
    ("en", "English"),
)

LOCALE_PATHS = (BASE_DIR / "locale",)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True
