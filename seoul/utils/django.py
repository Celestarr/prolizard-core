from django.conf import settings


def build_file_field_download_url(request, file_field) -> str:
    url = file_field.url

    if not url.startswith("/"):
        return url

    return request.build_absolute_uri(url)


def remove_media_file(file_path: str, silent: bool = True) -> None:
    (settings.BASE_DIR / settings.MEDIA_ROOT / file_path).unlink(missing_ok=silent)
