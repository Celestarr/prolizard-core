from decouple import config

AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID")

AWS_S3_SECRET_ACCESS_KEY = config("AWS_S3_SECRET_ACCESS_KEY")

AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")

# If you’re using S3 as a CDN (via CloudFront), you’ll probably want this
# storage to serve those files using that:
# AWS_S3_CUSTOM_DOMAIN = ''

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

# Custom setting. Only used for static files with no queryauth.
AWS_STATIC_BUCKET_NAME = config("AWS_STATIC_BUCKET_NAME")
