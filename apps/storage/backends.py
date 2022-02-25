import posixpath

from django.core.files.storage import FileSystemStorage as BaseFileSystemStorage
from storages.utils import get_available_overwrite_name


class FileSystemStorage(BaseFileSystemStorage):
    @staticmethod
    def _clean_name(name: str) -> str:
        """Cleans the name so that Windows style paths work.

        Taken from S3Boto3Storage class.
        """
        # Normalize Windows style paths
        clean_name = posixpath.normpath(name).replace("\\", "/")

        # os.path.normpath() can strip trailing slashes so we implement
        # a workaround here.
        if name.endswith("/") and not clean_name.endswith("/"):
            # Add a trailing slash as it was stripped.
            clean_name += "/"
        return clean_name

    def get_available_name(self, name, max_length=None):
        name = self._clean_name(name)
        return get_available_overwrite_name(name, max_length)
