from django.conf import settings
from storages.backends.s3 import S3ManifestStaticStorage as BaseS3ManifestStaticStorage


class S3ManifestStaticStorage(BaseS3ManifestStaticStorage):
    def path(self, name):
        pass

    def get_accessed_time(self, name):
        pass

    def get_created_time(self, name):
        pass

    def get_default_settings(self):
        default_settings = super().get_default_settings()

        return {
            **default_settings,
            "bucket_name": settings.AWS_STATIC_BUCKET_NAME,
        }
