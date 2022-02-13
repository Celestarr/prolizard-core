from os import getenv

AWS_S3_ACCESS_KEY_ID = getenv("AWS_S3_ACCESS_KEY_ID")

AWS_S3_SECRET_ACCESS_KEY = getenv("AWS_S3_SECRET_ACCESS_KEY")

AWS_S3_REGION_NAME = getenv("AWS_S3_REGION_NAME")

# If you’re using S3 as a CDN (via CloudFront), you’ll probably want this
# storage to serve those files using that:
# AWS_S3_CUSTOM_DOMAIN = 'cdn.myfolab.com'

AWS_STORAGE_BUCKET_NAME = getenv("AWS_STORAGE_BUCKET_NAME")

# Custom setting. Only used for static files with no queryauth.
AWS_STATIC_BUCKET_NAME = getenv("AWS_STATIC_BUCKET_NAME")
