from django.conf import settings
from storages.backends.s3boto3 import S3ManifestStaticStorage as BaseS3ManifestStaticStorage


class S3ManifestStaticStorage(BaseS3ManifestStaticStorage):
    def path(self, name):
        return super().path(name)

    def get_accessed_time(self, name):
        return super().get_accessed_time(name)

    def get_created_time(self, name):
        return super().get_created_time(name)

    def get_default_settings(self):
        default_settings = super().get_default_settings()

        return {
            **default_settings,
            "bucket_name": settings.AWS_STATIC_BUCKET_NAME,
        }
