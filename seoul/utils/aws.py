from typing import Optional

import boto3
from botocore.exceptions import ClientError
from django.conf import settings


def aws_s3_create_presigned_url(src_url: str, expiration: int = 3600) -> Optional[str]:
    """Generate a presigned URL to share an S3 object"""

    object_name = src_url.split(f"{settings.AWS_STORAGE_BUCKET_NAME}/")[-1]

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
    )

    try:
        response = s3_client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "Key": object_name,
            },
            ExpiresIn=expiration,
        )
    except ClientError:
        return None

    # The response contains the presigned URL
    return response
